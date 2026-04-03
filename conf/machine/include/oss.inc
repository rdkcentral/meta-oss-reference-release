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
        "rdk-arm7a-oss":  "da0afca627da79da0007059ba410d4e3ba5f01d032f570b36e1ebb69e0691ae6",
        "rdk-arm7ve-oss": "84145b68fd608fa13e2948c354ed280bb109c64997f8fd251789288f960f32ca",
        "rdk-arm64-oss":  "725e2ebec60cdcb3c54d2538c388f94f12d663298d6f355bf112d52df8ef31b7",
    }
    return  mapping.get(arch)

CVE_FILE_CHECKSUM = "${@get_cve_checksum(d)}"
CVE_LAYER_FEED_PATH += " ${REL_OSS_LAYER_EXTENSION}##${RDK_ARTIFACTS_BASE_URL}/rdk-oss-rel/${OSS_LAYER_VERSION}/${REL_OSS_MACHINE}/tarball/cve/${REL_OSS_LAYER_EXTENSION}.tgz;sha256sum=${CVE_FILE_CHECKSUM}"

