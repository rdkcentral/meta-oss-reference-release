# To support layered ipk generation
# Artifactory URL has to be added here
RDK_ARTIFACTS_BASE_URL ?= ""
RDK_ARTIFACTS_URL ?= ""

OSS_LAYER_VERSION = "4.4.0"
def get_oss_machine(d):
    arch = ""
    default_tune = d.getVar('DEFAULTTUNE')

    # need to fix: Workaround to check for 64bit machine with multilib configuration
    multilib_support = d.getVar('MULTILIBS') or ""
    if multilib_support:
        arch = "rdk-arm64"
    elif "armv7athf-neon" in default_tune:
        arch = "rdk-arm7a"
    else:
        arch = "rdk-arm7ve"
    return arch

def get_oss_arch(d):
    arch = get_oss_machine(d)
    arch += "-oss"
    return arch

OSS_MACHINE = "${@get_oss_machine(d)}"
OSS_LAYER_ARCH = "${@get_oss_arch(d)}"
PACKAGE_EXTRA_ARCHS:append = " ${OSS_LAYER_ARCH}"
OSS_LAYER_EXTENSION = "${OSS_LAYER_ARCH}"
OSS_IPK_SERVER_PATH = "https://partners.artifactory.comcast.com/artifactory/rdk-oss-dbg/RDKOSS-337-cleanup-xione/rdk-arm7ve/ipks"

# To set the remote feeds
IPK_FEED_URIS += " \
                ${OSS_LAYER_EXTENSION}##${OSS_IPK_SERVER_PATH} "

