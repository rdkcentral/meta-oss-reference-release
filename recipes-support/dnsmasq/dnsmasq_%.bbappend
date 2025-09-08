RDEPENDS:${PN}-service += " busybox"

PACKAGES:remove =+ "${PN}-service"

INSANE_SKIP:${PN} = "installed-vs-shipped"
