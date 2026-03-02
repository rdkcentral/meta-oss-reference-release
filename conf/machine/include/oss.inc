# To support layered ipk generation
# Artifactory URL has to be added here
RDK_ARTIFACTS_BASE_URL ?= ""
RDK_ARTIFACTS_URL ?= ""

REL_OSS_MACHINE = "${@get_oss_machine(d)}"
REL_OSS_LAYER_ARCH = "${@get_oss_arch(d)}"
PACKAGE_EXTRA_ARCHS:append = "${@ '' if '${REL_OSS_LAYER_ARCH}' == '${OSS_LAYER_ARCH}' else ' ${REL_OSS_LAYER_ARCH}'}"
REL_OSS_LAYER_EXTENSION = "${REL_OSS_LAYER_ARCH}"
REL_OSS_IPK_SERVER_PATH ?= "${RDK_ARTIFACTS_BASE_URL}/rdk-oss-dbg/RDKEMW-11062-tv/${REL_OSS_MACHINE}/ipks"

# To set the remote feeds
IPK_FEED_URIS += " \
                ${REL_OSS_LAYER_EXTENSION}##${REL_OSS_IPK_SERVER_PATH} "

def get_cve_checksum (d):
    arch = d.getVar('REL_OSS_LAYER_ARCH') or ''
    mapping = {
        "rdk-arm7a-oss":  "fe379211bf571831cb3e4becbc884f0338b2f05b2124dfdb91afb129ec8db478",
        "rdk-arm7ve-oss": "68e724e5231fc0dce52037d3cecf1154415f95d4bac223606ef4d1358254df72",
        "rdk-arm64-oss":  "0db073343ed9c60e748f0534ddb427a887bdffafacc1077739f1dda86362b583",
    }
    return  mapping.get(arch)

CVE_FILE_CHECKSUM = "${@get_cve_checksum(d)}"
CVE_LAYER_FEED_PATH += " ${REL_OSS_LAYER_EXTENSION}##${RDK_ARTIFACTS_BASE_URL}/rdk-oss-rel/${OSS_LAYER_VERSION}/${REL_OSS_MACHINE}/tarball/cve/${REL_OSS_LAYER_EXTENSION}.tgz;sha256sum=${CVE_FILE_CHECKSUM}"

