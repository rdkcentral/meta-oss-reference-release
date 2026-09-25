#!/usr/bin/env python3

import argparse
import json
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "configs" / "oss_audit_repos.json"


def load_authorized_repositories(config_path: Path) -> set[str]:
    with config_path.open("r", encoding="utf-8") as handle:
        config = json.load(handle)

    return {
        entry["full_name"]
        for entry in config.get("authorized_repositories", [])
        if entry.get("full_name")
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Validate that a pull request originates from an authorized "
            "OSS repository."
        )
    )
    parser.add_argument(
        "--repos-file",
        type=Path,
        default=DEFAULT_CONFIG,
        help="Repository configuration JSON file.",
    )
    parser.add_argument(
        "--repository",
        default=os.environ.get("GITHUB_HEAD_REPO_FULL_NAME")
        or os.environ.get("GITHUB_REPOSITORY"),
        help=(
            "Repository to validate in owner/repository form. Defaults to "
            "GITHUB_HEAD_REPO_FULL_NAME or GITHUB_REPOSITORY."
        ),
    )
    args = parser.parse_args()

    if not args.repository:
        raise SystemExit(
            "ERROR: No repository supplied. Use --repository OWNER/REPO "
            "or set GITHUB_HEAD_REPO_FULL_NAME."
        )

    authorized = load_authorized_repositories(args.repos_file)

    if args.repository not in authorized:
        print(
            "ERROR: Repository '{}' is not authorized for OSS recipe "
            "changes.".format(args.repository),
            file=sys.stderr,
        )
        print(
            "Authorized repositories:",
            file=sys.stderr,
        )

        for repository in sorted(authorized):
            print("  - {}".format(repository), file=sys.stderr)

        raise SystemExit(1)

    print(
        "OSS repository authorization passed: {}".format(
            args.repository
        )
    )


if __name__ == "__main__":
    main()
