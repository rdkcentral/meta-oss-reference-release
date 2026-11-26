# OSS Component Audit Report

- Generated: `2026-11-20T10:51:15Z`
- Configured repositories: `25`
- Failed repositories: `16`
- Total audited files: `574`
- Recipe and append files: `422`
- Files containing patch entries: `41`

## Files per repository

| Repository | Layer | Recipes | Files |
| --- | --- | ---: | ---: |
| rdkcentral/poky | upstream | 0 | 0 |
| rdkcentral/meta-openembedded | upstream | 0 | 0 |
| rdkcentral/meta-virtualization | upstream | 0 | 0 |
| rdkcentral/meta-clang | upstream | 0 | 0 |
| rdkcentral/meta-python2 | upstream | 313 | 397 |
| rdkcentral/meta-rust | upstream | 105 | 155 |
| rdkcentral/meta-rdk-oss-reference | oss | 0 | 0 |
| rdkcentral/meta-oss-reference-development | oss | 0 | 7 |
| rdkcentral/meta-oss-reference-release | oss | 0 | 2 |
| rdkcentral/meta-rdk-auxiliary | oss | 0 | 3 |
| rdk-e/meta-rdk-oss-ext | oss | 0 | 0 |
| rdk-e/rdke-oss-manifest | manifest | 0 | 0 |
| rdkcentral/rdk-oss-common-manifest | manifest | 0 | 0 |
| rdkcentral/rdke-oss-manifest | manifest | 0 | 0 |
| rdkcentral/meta-oss-common-config | oss-config | 0 | 0 |
| rdk-e/meta-rdk-oss-ext-vendor | vendor | 0 | 0 |
| rdk-e/meta-oss-vendor-realtek | vendor | 0 | 0 |
| rdk-e/meta-oss-vendor-amlogic | vendor | 0 | 0 |
| rdk-e/meta-oss-vendor-broadcom | vendor | 0 | 0 |
| rdk-e/meta-oss-vendor-mtk | vendor | 0 | 0 |
| rdkcentral/meta-rdk-oss-ext-middleware | middleware | 4 | 8 |
| rdk-e/rdke-assembler-manifest | assembler-manifest | 0 | 0 |
| rdk-e/meta-image-assembler | assembler | 0 | 0 |
| rdk-e/meta-cspc-image-assembler | assembler | 0 | 0 |
| rdkcentral/build-scripts | build-tools | 0 | 2 |

## Files by layer

| Layer | Files |
| --- | ---: |
| build-tools | 2 |
| middleware | 8 |
| oss | 12 |
| upstream | 552 |

## Files by type

| File type | Files |
| --- | ---: |
| bb | 416 |
| bbappend | 6 |
| conf | 11 |
| inc | 45 |
| patch | 86 |
| service | 1 |
| sh | 9 |

## Repository scan failures

| Repository | Error |
| --- | --- |
| rdkcentral/poky | Command '['git', 'clone', '--depth', '1', 'https://github.com/rdkcentral/poky.git', 'C:\\Users\\CSHARPA\\OneDrive - Capgemini\\Desktop\\Comcast\\Audit_Report\\meta-oss-reference-release\\reports\\oss-audit\\.audit-clones\\rdkcentral__poky']' returned non-zero exit status 128. |
| rdkcentral/meta-openembedded | Command '['git', 'clone', '--depth', '1', 'https://github.com/rdkcentral/meta-openembedded.git', 'C:\\Users\\CSHARPA\\OneDrive - Capgemini\\Desktop\\Comcast\\Audit_Report\\meta-oss-reference-release\\reports\\oss-audit\\.audit-clones\\rdkcentral__meta-openembedded']' returned non-zero exit status 128. |
| rdkcentral/meta-virtualization | Command '['git', 'clone', '--depth', '1', 'https://github.com/rdkcentral/meta-virtualization.git', 'C:\\Users\\CSHARPA\\OneDrive - Capgemini\\Desktop\\Comcast\\Audit_Report\\meta-oss-reference-release\\reports\\oss-audit\\.audit-clones\\rdkcentral__meta-virtualization']' returned non-zero exit status 128. |
| rdkcentral/meta-clang | Command '['git', 'clone', '--depth', '1', 'https://github.com/rdkcentral/meta-clang.git', 'C:\\Users\\CSHARPA\\OneDrive - Capgemini\\Desktop\\Comcast\\Audit_Report\\meta-oss-reference-release\\reports\\oss-audit\\.audit-clones\\rdkcentral__meta-clang']' returned non-zero exit status 128. |
| rdkcentral/meta-rdk-oss-reference | Command '['git', 'clone', '--depth', '1', 'https://github.com/rdkcentral/meta-rdk-oss-reference.git', 'C:\\Users\\CSHARPA\\OneDrive - Capgemini\\Desktop\\Comcast\\Audit_Report\\meta-oss-reference-release\\reports\\oss-audit\\.audit-clones\\rdkcentral__meta-rdk-oss-reference']' returned non-zero exit status 128. |
| rdk-e/meta-rdk-oss-ext | Command '['git', 'clone', '--depth', '1', 'https://github.com/rdk-e/meta-rdk-oss-ext.git', 'C:\\Users\\CSHARPA\\OneDrive - Capgemini\\Desktop\\Comcast\\Audit_Report\\meta-oss-reference-release\\reports\\oss-audit\\.audit-clones\\rdk-e__meta-rdk-oss-ext']' returned non-zero exit status 128. |
| rdk-e/rdke-oss-manifest | Command '['git', 'clone', '--depth', '1', 'https://github.com/rdk-e/rdke-oss-manifest.git', 'C:\\Users\\CSHARPA\\OneDrive - Capgemini\\Desktop\\Comcast\\Audit_Report\\meta-oss-reference-release\\reports\\oss-audit\\.audit-clones\\rdk-e__rdke-oss-manifest']' returned non-zero exit status 128. |
| rdkcentral/meta-oss-common-config | Command '['git', 'clone', '--depth', '1', 'https://github.com/rdkcentral/meta-oss-common-config.git', 'C:\\Users\\CSHARPA\\OneDrive - Capgemini\\Desktop\\Comcast\\Audit_Report\\meta-oss-reference-release\\reports\\oss-audit\\.audit-clones\\rdkcentral__meta-oss-common-config']' returned non-zero exit status 128. |
| rdk-e/meta-rdk-oss-ext-vendor | Command '['git', 'clone', '--depth', '1', 'https://github.com/rdk-e/meta-rdk-oss-ext-vendor.git', 'C:\\Users\\CSHARPA\\OneDrive - Capgemini\\Desktop\\Comcast\\Audit_Report\\meta-oss-reference-release\\reports\\oss-audit\\.audit-clones\\rdk-e__meta-rdk-oss-ext-vendor']' returned non-zero exit status 128. |
| rdk-e/meta-oss-vendor-realtek | Command '['git', 'clone', '--depth', '1', 'https://github.com/rdk-e/meta-oss-vendor-realtek.git', 'C:\\Users\\CSHARPA\\OneDrive - Capgemini\\Desktop\\Comcast\\Audit_Report\\meta-oss-reference-release\\reports\\oss-audit\\.audit-clones\\rdk-e__meta-oss-vendor-realtek']' returned non-zero exit status 128. |
| rdk-e/meta-oss-vendor-amlogic | Command '['git', 'clone', '--depth', '1', 'https://github.com/rdk-e/meta-oss-vendor-amlogic.git', 'C:\\Users\\CSHARPA\\OneDrive - Capgemini\\Desktop\\Comcast\\Audit_Report\\meta-oss-reference-release\\reports\\oss-audit\\.audit-clones\\rdk-e__meta-oss-vendor-amlogic']' returned non-zero exit status 128. |
| rdk-e/meta-oss-vendor-broadcom | Command '['git', 'clone', '--depth', '1', 'https://github.com/rdk-e/meta-oss-vendor-broadcom.git', 'C:\\Users\\CSHARPA\\OneDrive - Capgemini\\Desktop\\Comcast\\Audit_Report\\meta-oss-reference-release\\reports\\oss-audit\\.audit-clones\\rdk-e__meta-oss-vendor-broadcom']' returned non-zero exit status 128. |
| rdk-e/meta-oss-vendor-mtk | Command '['git', 'clone', '--depth', '1', 'https://github.com/rdk-e/meta-oss-vendor-mtk.git', 'C:\\Users\\CSHARPA\\OneDrive - Capgemini\\Desktop\\Comcast\\Audit_Report\\meta-oss-reference-release\\reports\\oss-audit\\.audit-clones\\rdk-e__meta-oss-vendor-mtk']' returned non-zero exit status 128. |
| rdk-e/rdke-assembler-manifest | Command '['git', 'clone', '--depth', '1', 'https://github.com/rdk-e/rdke-assembler-manifest.git', 'C:\\Users\\CSHARPA\\OneDrive - Capgemini\\Desktop\\Comcast\\Audit_Report\\meta-oss-reference-release\\reports\\oss-audit\\.audit-clones\\rdk-e__rdke-assembler-manifest']' returned non-zero exit status 128. |
| rdk-e/meta-image-assembler | Command '['git', 'clone', '--depth', '1', 'https://github.com/rdk-e/meta-image-assembler.git', 'C:\\Users\\CSHARPA\\OneDrive - Capgemini\\Desktop\\Comcast\\Audit_Report\\meta-oss-reference-release\\reports\\oss-audit\\.audit-clones\\rdk-e__meta-image-assembler']' returned non-zero exit status 128. |
| rdk-e/meta-cspc-image-assembler | Command '['git', 'clone', '--depth', '1', 'https://github.com/rdk-e/meta-cspc-image-assembler.git', 'C:\\Users\\CSHARPA\\OneDrive - Capgemini\\Desktop\\Comcast\\Audit_Report\\meta-oss-reference-release\\reports\\oss-audit\\.audit-clones\\rdk-e__meta-cspc-image-assembler']' returned non-zero exit status 128. |

> For detailed audit table, see [OSS Audit Report](https://github.com/rdkcentral/docs/tree/main/docs/OSS_Audit_Report)
