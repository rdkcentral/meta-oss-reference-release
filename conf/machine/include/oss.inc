# To support layered ipk generation
# Artifactory URL has to be added here
RDK_ARTIFACTS_BASE_URL ?= ""
RDK_ARTIFACTS_URL ?= ""

REL_OSS_MACHINE = "${@get_oss_machine(d)}"
REL_OSS_LAYER_ARCH = "${@get_oss_arch(d)}"
PACKAGE_EXTRA_ARCHS:append = "${@ '' if '${REL_OSS_LAYER_ARCH}' == '${OSS_LAYER_ARCH}' else ' ${REL_OSS_LAYER_ARCH}'}"
REL_OSS_LAYER_EXTENSION = "${REL_OSS_LAYER_ARCH}"
REL_OSS_IPK_SERVER_PATH = "${RDK_ARTIFACTS_BASE_URL}/rdk-oss-dbg/RDKOSS-541-ref/${REL_OSS_MACHINE}/ipks"

# To set the remote feeds
IPK_FEED_URIS += " \
                ${REL_OSS_LAYER_EXTENSION}##${REL_OSS_IPK_SERVER_PATH} "
