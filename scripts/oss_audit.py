#!/usr/bin/env python3

import argparse
import base64
import html
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "configs" / "oss_audit_repos.json"

RECIPE_SUFFIXES = {".bb", ".bbappend"}

DEFAULT_AUDIT_SUFFIXES = {
    ".bb",
    ".bbappend",
    ".inc",
    ".conf",
    ".service",
    ".sh",
    ".patch",
}

ASSIGNMENT_RE = re.compile(
    r"^\s*([A-Za-z0-9_${}.:+-]+)\s*(\+=|=\+|\?=|:=|=)\s*(.*?)\s*$"
)

INCLUDE_RE = re.compile(
    r"^\s*(include|require)\s+(.+?)\s*$"
)

SUPPORTED_METADATA = {
    "LICENSE",
    "SRC_URI",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def get_repository_name(entry: dict) -> str:
    repository = entry.get("full_name") or entry.get("repository")

    if not repository:
        raise ValueError(
            "Repository entry must contain 'full_name' or 'repository'"
        )

    return repository


def git_environment(token: Optional[str]) -> dict:
    """
    Configure Git authentication without exposing the token in a URL.
    """
    environment = os.environ.copy()
    environment["GIT_TERMINAL_PROMPT"] = "0"

    if token:
        credentials = base64.b64encode(
            ("x-access-token:" + token).encode("utf-8")
        ).decode("ascii")

        environment["GIT_CONFIG_COUNT"] = "1"
        environment["GIT_CONFIG_KEY_0"] = (
            "http.https://github.com/.extraheader"
        )
        environment["GIT_CONFIG_VALUE_0"] = (
            "AUTHORIZATION: basic " + credentials
        )

    return environment


def run_git(
    arguments: List[str],
    cwd: Optional[Path],
    token: Optional[str],
) -> str:
    result = subprocess.run(
        ["git"] + arguments,
        cwd=str(cwd) if cwd else None,
        env=git_environment(token),
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    return result.stdout.strip()


def clone_repository(
    repository: str,
    work_dir: Path,
    token: Optional[str],
    ref: Optional[str] = None,
) -> Path:
    clone_path = work_dir / repository.replace("/", "__")
    shutil.rmtree(clone_path, ignore_errors=True)

    command = ["clone", "--depth", "1"]

    if ref:
        command.extend(["--branch", ref, "--single-branch"])

    command.extend(
        [
            "https://github.com/{0}.git".format(repository),
            str(clone_path),
        ]
    )

    run_git(command, None, token)
    return clone_path


def logical_lines(text: str) -> List[str]:
    """
    Join BitBake continuation lines.

    Example:

        SRC_URI = "file://one.patch \\
                   file://two.patch"

    becomes one logical line.
    """
    lines = []
    pending = ""

    for physical_line in text.splitlines():
        line = physical_line.rstrip()

        if pending:
            pending += " " + line.lstrip()
        else:
            pending = line

        if pending.endswith("\\"):
            pending = pending[:-1].rstrip()
            continue

        lines.append(pending)
        pending = ""

    if pending:
        lines.append(pending)

    return lines


def strip_inline_comment(value: str) -> str:
    """
    Remove comments outside quoted strings.
    """
    quote = None
    escaped = False

    for index, character in enumerate(value):
        if escaped:
            escaped = False
            continue

        if character == "\\":
            escaped = True
            continue

        if quote:
            if character == quote:
                quote = None
            continue

        if character in ("'", '"'):
            quote = character
            continue

        if character == "#":
            return value[:index].rstrip()

    return value.strip()


def clean_value(value: str) -> str:
    value = strip_inline_comment(value).strip()

    if (
        len(value) >= 2
        and value[0] == value[-1]
        and value[0] in ("'", '"')
    ):
        value = value[1:-1]

    return value.strip()


def normalize_metadata_name(variable: str) -> Optional[str]:
    """
    Normalize common BitBake variable variants:

      SRC_URI
      SRC_URI:append
      SRC_URI_append
      LICENSE:${PN}
    """
    for name in SUPPORTED_METADATA:
        if variable == name:
            return name

        if variable.startswith(name + ":"):
            return name

        if variable.startswith(name + "_"):
            return name

    return None


def merge_assignment(
    current: str,
    operation: str,
    value: str,
) -> str:
    if operation in ("+=", "=+"):
        return (current + " " + value).strip()

    if operation == "?=" and current:
        return current

    return value


def parse_file(path: Path) -> Tuple[dict, List[dict]]:
    """
    Parse LICENSE, SRC_URI, and include/require statements.

    This is static parsing. It does not evaluate BitBake overrides,
    variable expansion, anonymous Python, or inherited classes.
    """
    text = path.read_text(
        encoding="utf-8",
        errors="replace",
    )

    metadata = {
        "LICENSE": "",
        "SRC_URI": "",
    }

    includes = []

    for line in logical_lines(text):
        stripped = line.strip()

        if not stripped or stripped.startswith("#"):
            continue

        include_match = INCLUDE_RE.match(stripped)

        if include_match:
            includes.append(
                {
                    "directive": include_match.group(1),
                    "requested": strip_inline_comment(
                        include_match.group(2)
                    ).strip(),
                }
            )
            continue

        assignment = ASSIGNMENT_RE.match(stripped)

        if not assignment:
            continue

        variable, operation, raw_value = assignment.groups()
        metadata_name = normalize_metadata_name(variable)

        if not metadata_name:
            continue

        value = clean_value(raw_value)

        metadata[metadata_name] = merge_assignment(
            metadata[metadata_name],
            operation,
            value,
        )

    return metadata, includes


def split_src_uri(value: str) -> List[str]:
    if not value:
        return []

    try:
        values = shlex.split(
            value,
            comments=False,
            posix=True,
        )
    except ValueError:
        values = value.replace("\\", " ").split()

    return [
        item.strip()
        for item in values
        if item.strip() and item.strip() != "\\"
    ]


def recipe_name_from_path(relative_path: str) -> str:
    """
    Derive the recipe name from a .bb or .bbappend filename.

    Examples:

      westeros-simplebuffer_1.0.bb
      westeros-simplebuffer_%.bbappend

    become:

      westeros-simplebuffer
    """
    filename = Path(relative_path).name

    if filename.endswith(".bbappend"):
        filename = filename[:-len(".bbappend")]
    elif filename.endswith(".bb"):
        filename = filename[:-len(".bb")]

    if "_" in filename:
        filename = filename.rsplit("_", 1)[0]

    return filename


def build_file_index(repository_root: Path) -> Dict[str, List[Path]]:
    """
    Index repository files by repository-relative path and basename.
    """
    index: Dict[str, List[Path]] = {}

    for path in repository_root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue

        relative_path = path.relative_to(repository_root).as_posix()

        index.setdefault(relative_path, []).append(path)
        index.setdefault(path.name, []).append(path)

    return index


def include_candidates(include_name: str) -> List[str]:
    """
    Return possible static include names.

    Dynamic includes containing ${...} or $(...) are not expanded.
    """
    try:
        values = shlex.split(
            include_name,
            comments=False,
            posix=True,
        )
    except ValueError:
        values = include_name.split()

    if not values:
        return []

    value = values[0].strip()

    if "${" in value or "$(" in value:
        return []

    return [
        value,
        value.lstrip("./"),
        Path(value).name,
    ]


def resolve_include(
    current_file: Path,
    include_name: str,
    repository_root: Path,
    file_index: Dict[str, List[Path]],
) -> Optional[Path]:
    for candidate in include_candidates(include_name):
        local_path = current_file.parent / candidate

        if local_path.is_file():
            return local_path.resolve()

        root_path = repository_root / candidate

        if root_path.is_file():
            return root_path.resolve()

        indexed_paths = file_index.get(candidate, [])

        if indexed_paths:
            return indexed_paths[0].resolve()

    return None


def collect_src_uri(
    path: Path,
    repository_root: Path,
    file_index: Dict[str, List[Path]],
    visited: Optional[Set[Path]] = None,
) -> Tuple[dict, List[dict], List[dict]]:
    """
    Recursively collect LICENSE, SRC_URI, and include/require entries.

    A visited set prevents recursive include cycles.
    """
    if visited is None:
        visited = set()

    path = path.resolve()

    if path in visited:
        return (
            {
                "LICENSE": "",
                "SRC_URI": "",
            },
            [],
            [],
        )

    visited.add(path)

    metadata, include_statements = parse_file(path)

    include_records = []
    src_records = []

    for source in split_src_uri(metadata["SRC_URI"]):
        src_records.append(
            {
                "src_uri": source,
            }
        )

    for include in include_statements:
        include_path = resolve_include(
            path,
            include["requested"],
            repository_root,
            file_index,
        )

        include_record = {
            "directive": include["directive"],
            "requested": include["requested"],
            "resolved": "",
        }

        if include_path:
            include_record["resolved"] = (
                include_path.relative_to(repository_root).as_posix()
            )

            (
                included_metadata,
                nested_include_records,
                nested_src_records,
            ) = collect_src_uri(
                include_path,
                repository_root,
                file_index,
                visited,
            )

            if not metadata["LICENSE"]:
                metadata["LICENSE"] = included_metadata["LICENSE"]

            if included_metadata["SRC_URI"]:
                metadata["SRC_URI"] = (
                    metadata["SRC_URI"]
                    + " "
                    + included_metadata["SRC_URI"]
                ).strip()

            include_records.extend(nested_include_records)
            src_records.extend(nested_src_records)

        include_records.append(include_record)

    return metadata, include_records, src_records


def unique_values(values: List[str]) -> List[str]:
    """
    Deduplicate values while preserving their original order.
    """
    seen = set()
    result = []

    for value in values:
        if value and value not in seen:
            seen.add(value)
            result.append(value)

    return result


def format_src_uri(src_records: List[dict]) -> str:
    """
    Store all direct and included SRC_URI entries in one field.

    No origin labels are added.
    """
    values = unique_values(
        [
            record["src_uri"]
            for record in src_records
        ]
    )

    return "; ".join(values)


def is_patch_src_uri(src_uri: str) -> bool:
    """
    Identify patch entries, including entries with BitBake parameters.

    Examples:

      file://fix.patch
      file://fix.patch;striplevel=1
      https://example.org/fix.patch;downloadfilename=fix.patch
    """
    location = src_uri.split(";", 1)[0]
    location = location.split("?", 1)[0]

    return location.lower().endswith(".patch")


def format_patch_entries(src_records: List[dict]) -> str:
    patches = [
        record["src_uri"]
        for record in src_records
        if is_patch_src_uri(record["src_uri"])
    ]

    return "; ".join(unique_values(patches))


def format_includes(include_records: List[dict]) -> str:
    values = []

    for record in include_records:
        requested = record["requested"]
        resolved = record.get("resolved")

        if resolved:
            values.append(
                "{0}:{1} -> {2}".format(
                    record["directive"],
                    requested,
                    resolved,
                )
            )
        else:
            values.append(
                "{0}:{1} -> unresolved".format(
                    record["directive"],
                    requested,
                )
            )

    return "; ".join(values)


def scan_repository(
    repository_entry: dict,
    repository_root: Path,
    extensions: Set[str],
) -> List[dict]:
    repository = get_repository_name(repository_entry)
    layer = repository_entry.get("layer", "unknown")
    file_index = build_file_index(repository_root)
    audit_rows = []

    for path in sorted(repository_root.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue

        suffix = path.suffix.lower()

        if suffix not in extensions:
            continue

        relative_path = path.relative_to(repository_root).as_posix()

        row = {
            "repository": repository,
            "layer": layer,
            "recipe": "",
            "path": relative_path,
            "file_type": suffix.lstrip("."),
            "SRC_URI": "",
            "LICENSE": "",
            "Patch": "",
            "include": "",
        }

        if suffix in RECIPE_SUFFIXES:
            row["recipe"] = recipe_name_from_path(relative_path)

            metadata, include_records, src_records = collect_src_uri(
                path,
                repository_root,
                file_index,
            )

            row["SRC_URI"] = format_src_uri(src_records)
            row["LICENSE"] = metadata["LICENSE"]
            row["Patch"] = format_patch_entries(src_records)
            row["include"] = format_includes(include_records)

        audit_rows.append(row)

    return audit_rows


def recipe_group_directory(row: dict) -> str:
    """
    Return the directory used to group a recipe with its supporting files.

    Common Yocto layouts include:

      recipes-multimedia/gstreamer/gstreamer1.0_1.18/
        gstreamer1.0-libav_1.18.5.bbappend
        files/
          0050-example.patch

    The recipe and patch are grouped under:

      recipes-multimedia/gstreamer/gstreamer1.0_1.18
    """
    path = Path(row["path"])
    parent = path.parent

    if "files" in parent.parts:
        parts = list(parent.parts)
        files_index = parts.index("files")

        group = Path(*parts[:files_index])
        return group.as_posix()

    return parent.as_posix()


def audit_row_sort_key(row: dict) -> tuple:
    """
    Sort rows deterministically.

    Ordering:

      1. repository
      2. recipe/supporting-file group directory
      3. .bb/.bbappend before supporting files
      4. recipe path before other paths

    This places a recipe or bbappend above sibling files/patches.
    """
    recipe_priority = (
        0
        if row["file_type"] in {"bb", "bbappend"}
        else 1
    )

    return (
        row["repository"],
        recipe_group_directory(row),
        recipe_priority,
        row["path"],
    )


def escape_html(value: Optional[str]) -> str:
    if value is None:
        return ""

    normalized = str(value)
    normalized = normalized.replace("\r", " ")
    normalized = normalized.replace("\n", " ")

    return html.escape(
        normalized.strip(),
        quote=True,
    )


def wrap_path(value: str) -> str:
    """
    Add safe wrapping opportunities to paths and repository names.
    """
    return escape_html(value).replace("/", "/<wbr>")


def split_display_values(value: str) -> List[str]:
    if not value:
        return []

    return [
        item.strip()
        for item in value.split("; ")
        if item.strip()
    ]


def wrap_list_value(value: str) -> str:
    """
    Render semicolon-separated values on separate lines.
    """
    values = split_display_values(value)
    rendered = []

    for item in values:
        escaped = escape_html(item)
        escaped = escaped.replace("/", "/<wbr>")
        escaped = escaped.replace(";", ";<wbr>")
        rendered.append(escaped)

    return "<br>\n".join(rendered)


def html_audit_table(rows: List[dict]) -> str:
    """
    Render the audit table as HTML.

    Native Markdown tables do not support reliable column widths.
    """
    lines = [
        "<table>",
        "  <colgroup>",
        '    <col width="12%">',
        '    <col width="7%">',
        '    <col width="11%">',
        '    <col width="18%">',
        '    <col width="6%">',
        '    <col width="18%">',
        '    <col width="7%">',
        '    <col width="11%">',
        '    <col width="10%">',
        "  </colgroup>",
        "  <thead>",
        "    <tr>",
        "      <th>Repository</th>",
        "      <th>Layer</th>",
        "      <th>Recipe</th>",
        "      <th>Path</th>",
        "      <th>File type</th>",
        "      <th>SRC_URI</th>",
        "      <th>LICENSE</th>",
        "      <th>Patch</th>",
        "      <th>Include</th>",
        "    </tr>",
        "  </thead>",
        "  <tbody>",
    ]

    for row in rows:
        lines.extend(
            [
                "    <tr>",
                "      <td>{0}</td>".format(
                    wrap_path(row.get("repository", ""))
                ),
                "      <td>{0}</td>".format(
                    escape_html(row.get("layer", ""))
                ),
                "      <td>{0}</td>".format(
                    escape_html(row.get("recipe", ""))
                ),
                "      <td>{0}</td>".format(
                    wrap_path(row.get("path", ""))
                ),
                "      <td>{0}</td>".format(
                    escape_html(row.get("file_type", ""))
                ),
                "      <td>{0}</td>".format(
                    wrap_list_value(row.get("SRC_URI", ""))
                ),
                "      <td>{0}</td>".format(
                    wrap_list_value(row.get("LICENSE", ""))
                ),
                "      <td>{0}</td>".format(
                    wrap_list_value(row.get("Patch", ""))
                ),
                "      <td>{0}</td>".format(
                    wrap_list_value(row.get("include", ""))
                ),
                "    </tr>",
            ]
        )

    lines.extend(
        [
            "  </tbody>",
            "</table>",
        ]
    )

    return "\n".join(lines)


def write_markdown_report(
    path: Path,
    generated_at: str,
    repositories: List[dict],
    audit_rows: List[dict],
    per_repo_counts: List[dict],
    failures: List[dict],
) -> None:
    layer_counts = Counter(
        row["layer"]
        for row in audit_rows
    )

    type_counts = Counter(
        row["file_type"]
        for row in audit_rows
    )

    total_recipe_count = sum(
        1
        for row in audit_rows
        if row["file_type"] in {"bb", "bbappend"}
    )

    patch_count = sum(
        1
        for row in audit_rows
        if row["Patch"]
    )

    lines = [
        "# OSS Component Audit Report",
        "",
        "- Generated: `{0}`".format(generated_at),
        "- Configured repositories: `{0}`".format(
            len(repositories)
        ),
        "- Failed repositories: `{0}`".format(
            len(failures)
        ),
        "- Total audited files: `{0}`".format(
            len(audit_rows)
        ),
        "- Recipe and append files: `{0}`".format(
            total_recipe_count
        ),
        "- Files containing patch entries: `{0}`".format(
            patch_count
        ),
        "",
        "## Files per repository",
        "",
        "| Repository | Layer | Recipes | Files |",
        "| --- | --- | ---: | ---: |",
    ]

    for entry in per_repo_counts:
        lines.append(
            "| {0} | {1} | {2} | {3} |".format(
                entry["repository"],
                entry["layer"],
                entry["recipes"],
                entry["files"],
            )
        )

    lines.extend(
        [
            "",
            "## Files by layer",
            "",
            "| Layer | Files |",
            "| --- | ---: |",
        ]
    )

    for layer, count in sorted(layer_counts.items()):
        lines.append(
            "| {0} | {1} |".format(
                layer,
                count,
            )
        )

    lines.extend(
        [
            "",
            "## Files by type",
            "",
            "| File type | Files |",
            "| --- | ---: |",
        ]
    )

    for file_type, count in sorted(type_counts.items()):
        lines.append(
            "| {0} | {1} |".format(
                file_type,
                count,
            )
        )

    if failures:
        lines.extend(
            [
                "",
                "## Repository scan failures",
                "",
                "| Repository | Error |",
                "| --- | --- |",
            ]
        )

        for failure in failures:
            error = failure["error"]
            error = error.replace("|", "\\|")
            error = error.replace("\n", " ")

            lines.append(
                "| {0} | {1} |".format(
                    failure["repository"],
                    error,
                )
            )

    lines.extend(
        [
            "",
            "## Audit table",
            "",
            html_audit_table(audit_rows),
            "",
            "## Audit columns",
            "",
            "- `Repository`: repository containing the file.",
            "- `Layer`: configured repository layer.",
            "- `Recipe`: recipe name for `.bb` and `.bbappend` files.",
            "- `Path`: repository-relative file path.",
            "- `File type`: file extension without the leading dot.",
            "- `SRC_URI`: direct and included SRC_URI values.",
            "- `LICENSE`: license from the recipe or resolved include.",
            "- `Patch`: patch entries extracted from SRC_URI.",
            "- `Include`: include/require statements and resolved paths.",
            "",
        ]
    )

    path.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Generate an OSS audit report as Markdown for Yocto recipes "
            "and supporting files."
        )
    )

    parser.add_argument(
        "--repos-file",
        type=Path,
        default=DEFAULT_CONFIG,
        help="Repository configuration JSON file.",
    )

    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("reports/oss-audit"),
        help="Directory for generated audit files.",
    )

    parser.add_argument(
        "--work-dir",
        type=Path,
        help="Directory used for temporary repository clones.",
    )

    parser.add_argument(
        "--token",
        default=os.environ.get("GITHUB_TOKEN"),
        help="GitHub token for private repositories.",
    )

    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help=(
            "Generate a partial report when one or more repositories "
            "cannot be cloned or scanned."
        ),
    )

    parser.add_argument(
        "--keep-clones",
        action="store_true",
        help="Keep cloned repositories for troubleshooting.",
    )

    args = parser.parse_args()

    config = load_config(args.repos_file)

    repositories = config.get(
        "authorized_repositories",
        [],
    )

    configured_extensions = config.get(
        "audited_extensions",
        sorted(DEFAULT_AUDIT_SUFFIXES),
    )

    extensions = {
        extension.lower()
        if extension.startswith(".")
        else "." + extension.lower()
        for extension in configured_extensions
    }

    output_dir = args.output_dir.resolve()

    work_dir = (
        args.work_dir.resolve()
        if args.work_dir
        else output_dir / ".audit-clones"
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    work_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    audit_rows = []
    per_repo_counts = []
    failures = []

    for repository_entry in repositories:
        repository = get_repository_name(repository_entry)
        layer = repository_entry.get("layer", "unknown")

        print(
            "Scanning {0}...".format(repository),
            flush=True,
        )

        try:
            repository_root = clone_repository(
                repository,
                work_dir,
                args.token,
                repository_entry.get("ref"),
            )

            repository_rows = scan_repository(
                repository_entry,
                repository_root,
                extensions,
            )

            audit_rows.extend(repository_rows)

            recipe_row_count = sum(
                1
                for row in repository_rows
                if row["file_type"] in {"bb", "bbappend"}
            )

            file_row_count = len(repository_rows)

            per_repo_counts.append(
                {
                    "repository": repository,
                    "layer": layer,
                    "recipes": recipe_row_count,
                    "files": file_row_count,
                }
            )

            print(
                "  recipes={0} files={1}".format(
                    recipe_row_count,
                    file_row_count,
                ),
                flush=True,
            )

        except Exception as error:
            failures.append(
                {
                    "repository": repository,
                    "error": str(error),
                }
            )

            per_repo_counts.append(
                {
                    "repository": repository,
                    "layer": layer,
                    "recipes": 0,
                    "files": 0,
                }
            )

            print(
                "ERROR: failed to scan {0}: {1}".format(
                    repository,
                    error,
                ),
                file=sys.stderr,
            )

    audit_rows.sort(key=audit_row_sort_key)

    generated_at = utc_now()

    report = {
        "generated_at": generated_at,
        "repositories": repositories,
        "failures": failures,
        "per_repository_counts": per_repo_counts,
        "audit": audit_rows,
    }

    (output_dir / "oss-audit.json").write_text(
        json.dumps(
            report,
            indent=2,
        ),
        encoding="utf-8",
    )

    write_markdown_report(
        output_dir / "oss-audit.md",
        generated_at,
        repositories,
        audit_rows,
        per_repo_counts,
        failures,
    )

    if not args.keep_clones:
        shutil.rmtree(
            work_dir,
            ignore_errors=True,
        )

    total_recipe_count = sum(
        entry["recipes"]
        for entry in per_repo_counts
    )

    print(
        "Generated {0} recipe records, {1} audit rows (all file types) "
        "across {2} repositories.".format(
            total_recipe_count,
            len(audit_rows),
            len(repositories),
        )
    )

    if failures and not args.continue_on_error:
        raise SystemExit(
            "Audit incomplete: {0} repository scan(s) failed.".format(
                len(failures)
            )
        )


if __name__ == "__main__":
    main()
