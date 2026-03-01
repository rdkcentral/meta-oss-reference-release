# To support layered ipk generation
# Artifactory URL has to be added here
RDK_ARTIFACTS_BASE_URL ?= ""
RDK_ARTIFACTS_URL ?= ""

REL_OSS_MACHINE = "${@get_oss_machine(d)}"
REL_OSS_LAYER_ARCH = "${@get_oss_arch(d)}"
PACKAGE_EXTRA_ARCHS:append = "${@ '' if '${REL_OSS_LAYER_ARCH}' == '${OSS_LAYER_ARCH}' else ' ${REL_OSS_LAYER_ARCH}'}"
REL_OSS_LAYER_EXTENSION = "${REL_OSS_LAYER_ARCH}"
REL_OSS_IPK_SERVER_PATH ?= "${RDK_ARTIFACTS_BASE_URL}/rdk-oss-rel/${OSS_LAYER_VERSION}/${REL_OSS_MACHINE}/ipks"

# To set the remote feeds
IPK_FEED_URIS += " \
                ${REL_OSS_LAYER_EXTENSION}##${REL_OSS_IPK_SERVER_PATH} "

def get_cve_checksum (d):
    arch = d.getVar('REL_OSS_LAYER_ARCH') or ''
    mapping = {
        "rdk-arm7a-oss":  "a953297d906bf7311be94d0efd8b9c32c2dd30cd86b400e98d0cc11289532d05",
        "rdk-arm7ve-oss": "68ea40be1f0a0bdeb50d358202b246b7fe11552f1e35f858010411de3f30c04d",
        "rdk-arm64-oss":  "04f29148179c3c56a0662554aa69734414dda880f8b0a0848ec2fe9cd2fe7d69",
    }
    return  mapping.get(arch)

CVE_FILE_CHECKSUM = "${@get_cve_checksum(d)}"
CVE_LAYER_FEED_PATH += " ${REL_OSS_LAYER_EXTENSION}##${RDK_ARTIFACTS_BASE_URL}/rdk-oss-rel/${OSS_LAYER_VERSION}/${REL_OSS_MACHINE}/tarball/cve/${REL_OSS_LAYER_EXTENSION}.tgz;sha256sum=${CVE_FILE_CHECKSUM}"

