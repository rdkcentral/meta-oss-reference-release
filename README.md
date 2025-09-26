# OSS Layer Release Notes
RDKE OSS Layer Release Notes

---

|Summary|Content|
|---|----|
|Classification|Public|
|Document Version|Issue 1|
|Date|9th August 2025|
|Author|RDKE Platform & Tools Team|

| Components | Tag |
|----------|--------|
| packagegroup-oss-layer | 4.8.0-r0|



## Table of Contents

- [OSS Layer Release Notes](#oss-layer-release-notes)
  - [Table of Contents](#table-of-contents)
  - [Release Description](#release-description)
  - [Build Instructions](#build-instructions)
  - [OSS Contribution Guidelines](#oss-contribution-guidelines)
  - [Release layer and components](#release-layer-and-components)
    - [OSS stack layer](#oss-stack-layer)
    - [Components details in "packagegroup-oss-layer"](#components-details-in-packagegroup-oss-layer)
 


## Release Description
Major changes in this release are:

Unified OSS Layer - The components of the OSS (Open Source Software) layer, including bb, bbappends, patches, and configs, previously managed within various repositories across RDKE stack layers, have been consolidated into a single repository named meta-rdk-oss-reference. All future modifications to OSS components should be made exclusively within this repository.

This release will provide a versioned `"meta-oss-reference-release"` that will be used by other stack layes to resolve build and runtime dependencies.

The 4.8.0 OSS release, based on the kirkstone yocto version, delivers architecture-specific and platform-independent artifacts. Within this release, ARM architecture is accommodated with the following variations:
    1. rdk-arm7a-oss: Default tuning is set to armv7athf-neon.
    2. rdk-arm7ve-oss: Default tuning is set to armv7vethf-neon.
    3. rdk-arm64-oss: 64-bit ARM architecture with a multilib configuration and default tuning set to armv7vethf-neon for compatibility with 32-bit systems.
The IPK feed is automatically chosen based on the platform's default tuning configuration, with armv7vethf-neon being the default feed.


## Release layer and components
### OSS stack layer
| Layer | Tag |
|------|------|
|meta-rdk-auxiliary|1.5.0|
|meta-rdk-oss-reference|4.8.0|
|meta-openembedded|rdk-4.0.0|
|poky|rdk-4.4.1|
|meta-python2|rdk-4.0.0|
|meta-rdk-oss-ext|1.4.0|
|meta-virtualization|rdk-4.0.0|
|meta-clang|rdk-4.0.0|

### Components details in "packagegroup-oss-layer"

|#|OSS layer Component|(=version)|
|-|----------------------|---------|
|1| abseil-cpp | (20211102.0+git0+7c6608d0db-r1) |
|2| acl | (2.3.1-r0) |
|3| alsa-lib | (1.2.6.1-r0) |
|4| alsa-state | (0.2.0-r5) |
|5| alsa-topology-conf | (1.2.5.1-r0) |
|6| alsa-ucm-conf | (1.2.6.3-r0) |
|7| alsa-utils | (1.2.6-r0) |
|8| alsa-utils-scripts | (1.2.6-r0) |
|9| apparmor | (2.13.10-r0) |
|10| atk | (2.38.0-r0) |
|11| attr | (2.5.1-r0) |
|12| autoconf-archive | (2022.02.11-r0) |
|13| avahi | (0.8-r1) |
|14| base-files | (3.0.14-r89) |
|15| base-passwd | (3.5.29-r0) |
|16| bash | (3.2.57-r0) |
|17| bash-completion | (2.11-r0) |
|18| bind | (9.18.28-r0) |
|19| boost | (1.78.0-r0) |
|20| breakpad | (1.0-r1) |
|21| breakpad-wrapper | (1.0.0-r0) |
|22| brotli | (1.0.9-r0) |
|23| busybox | (1.35.0-r1) |
|24| bzip2 | (1.0.8-r0) |
|25| ca-certificates | (20211016-r2) |
|26| c-ares | (1.18.1-r0) |
|27| civetweb | (1.10+git+0+0f1b43536d-r0) |
|28| cjson | (1.7.18-r0) |
|29| coreutils | (6.9-r0) |
|30| cracklib | (2.9.8-r0) |
|31| crun | (1.7.2-r0) |
|32| ctemplate | (1.0.0+git0+4b7e6c52dc-r4) |
|33| cunit | (2.1-3-r0) |
|34| curl | (7.82.0-r1) |
|35| db | (5.3.28-r1) |
|36| dbus | (1.14.8-r0) |
|37| dbus-glib | (0.112-r0) |
|38| dibbler | (1.0.1+1.0.2RC1+gita7c6cf58a88a510cb00841351e75030ce78d36bf-r1) |
|39| dnsmasq | (2.90-r2) |
|40| dosfstools | (2.11-r0) |
|41| e2fsprogs | (1.46.5-r0) |
|42| ebtables | (2.0.11-r4) |
|43| elfutils | (0.186-r0) |
|44| ethtool | (5.16-r0) |
|45| evtest | (1.34-r0) |
|46| expat | (2.5.0-r0) |
|47| fcgi | (2.4.2-r0) |
|48| file | (5.41-r0) |
|49| findutils | (4.2.31-r0) |
|50| flac | (1.3.4-r0) |
|51| flex | (2.6.4-r0) |
|52| fontconfig | (2.13.1-r0) |
|53| freetype | (2.11.1-r1) |
|54| fribidi | (1.0.13-r0) |
|55| gawk | (3.1.5-r2) |
|56| gcc-runtime | (11.3.0-r0) |
|57| gcc-sanitizers | (11.3.0-r0) |
|58| gdbm | (1.8.3-r4) |
|59| gdk-pixbuf | (2.42.10-r0) |
|60| gettext | (0.16.1-r6) |
|61| gflags | (2.2.2-r0) |
|62| glib-2.0 | (2.72.3-r1) |
|63| glibc | (2.35-r1) |
|64| glibc-locale | (2.35-r0) |
|65| glibc-mtrace | (2.35-r0) |
|66| glib-networking | (2.72.2-r1) |
|67| gmp | (4.2.1-r0) |
|68| gnutls | (3.3.30-r1) |
|69| gobject-introspection | (1.72.0-r0) |
|70| googletest | (1.11.0+git0+9e71237221-r0) |
|71| graphite2 | (1.3.6-r0) |
|72| grpc | (1.46.7-r1) |
|73| gssdp | (1.4.0.1-r0) |
|74| gupnp | (0.20.10-r1) |
|75| harfbuzz | (4.0.1-r0) |
|76| heaptrack | (1.5.0-r0) |
|77| hiredis | (1.0.2-r0) |
|78| icu | (70.1-r0) |
|79| initscripts | (1.0-r155) |
|80| init-system-helpers | (1.62-r0) |
|81| iperf3 | (3.14-r0) |
|82| iptables | (1.8.7-r3) |
|83| iso-codes | (4.15.0-r0) |
|84| iw | (4.7-r0) |
|85| jansson | (2.13.1-r0) |
|86| jquery | (1.0.0-r3) |
|87| json-c | (0.15-r0) |
|88| jsoncpp | (1.8.4-r0) |
|89| jsonrpc | (1.3.0-r0) |
|90| kbd | (2.4.0-r0) |
|91| keyutils | (1.6.1-r0) |
|92| kmod | (29-r0) |
|93| lcms | (2.13.1-r0) |
|94| libaio | (0.3.112-r0) |
|95| libarchive | (3.6.1-r1) |
|96| libatomic-ops | (7.6.14-r0) |
|97| libbsd | (0.11.5-r0) |
|98| libcap | (2.66-r0) |
|99| libcap-ng | (0.8.2-r0) |
|100| libcgroup | (2.0.2-r0) |
|101| libcheck | (0.15.2-r0) |
|102| libcroco | (0.6.13-r0) |
|103| libdaemon | (0.14-r0) |
|104| libdash | (1.0.0+git0+f5b5d991af-r1) |
|105| libdwarf | (20210528-r0) |
|106| liberation-fonts | (2.1.5-r0) |
|107| libev | (4.33-r0) |
|108| libevdev | (1.12.1-r0) |
|109| libevent | (2.1.12-r0) |
|110| libexif | (0.6.24-r0) |
|111| libffi | (3.4.4-r0) |
|112| libgcc | (11.3.0-r0) |
|113| libgcrypt | (1.9.4-r0) |
|114| libgpg-error | (1.44-r0) |
|115| libgudev | (237-r0) |
|116| libical | (3.0.16-r1) |
|117| libidn2 | (2.3.2-r0) |
|118| libinput | (1.19.4-r0) |
|119| libjpeg | (62.3.0-r0) |
|120| libmanette | (0.2.6-r1) |
|121| libmd | (1.0.4-r0) |
|122| libmicrohttpd | (0.9.76-r0) |
|123| libmng | (2.0.3-r0) |
|124| libmnl | (1.0.4-r0) |
|125| libndp | (1.8-r0) |
|126| libnewt | (0.52.23-r0) |
|127| libnl | (3.5.0-r1) |
|128| libnsl2 | (2.0.0-r0) |
|129| libnss-mdns | (0.15.1-r1) |
|130| liboauth | (1.0.3-r0) |
|131| libogg | (1.3.5-r0) |
|132| libol | (0.3.18-r0) |
|133| libomxil | (0.9.3-r1) |
|134| libopus | (1.3.1-r0) |
|135| libpam | (1.5.2-r0) |
|136| libpcap | (1.10.1-r1) |
|137| libpciaccess | (0.16-r0) |
|138| libpcre2 | (10.40-r0) |
|139| libpcre | (8.39-r0) |
|140| libpng | (1.6.39-r0) |
|141| libpsl | (0.21.1-r0) |
|142| libpthread-stubs | (0.4-r0) |
|143| libsamplerate0 | (0.2.2-r1) |
|144| libsdl | (1.2.15-r3) |
|145| libsdl-image | (1.2.12-r0) |
|146| libsdl-ttf | (2.0.11-r0) |
|147| libseccomp | (2.4.3-r0) |
|148| libsndfile1 | (1.0.31-r0) |
|149| libsolv | (0.7.22-r0) |
|150| libsoup-2.4 | (2.74.2-r1) |
|151| libsoup | (3.6.5-r0) |
|152| libstd-rs | (1.72.0-r0) |
|153| libtasn1 | (4.13-r1) |
|154| libtheora | (1.1.1-r1) |
|155| libtinyxml | (2.6.2-r5) |
|156| libtinyxml2 | (9.0.0-r0) |
|157| libtirpc | (1.3.2-r0) |
|158| libtool | (2.4.7-r0) |
|159| libunistring | (1.0-r0) |
|160| libunwind | (1.7.0-r0) |
|161| liburcu | (0.13.2-r0) |
|162| libusb1 | (1.0.27-r0) |
|163| libuv | (1.44.2-r0) |
|164| libvorbis | (1.3.7-r0) |
|165| libvpx | (1.12.0-r0) |
|166| libwebp | (1.3.2-r0) |
|167| libwebsockets | (4.2.2-r0) |
|168| libxcrypt | (4.4.33-r0) |
|169| libxkbcommon | (0.5.0-r0) |
|170| libxml2 | (2.9.14-r1) |
|171| libxslt | (1.1.35-r0) |
|172| libzip | (1.8.0-r0) |
|173| lighttpd | (1.4.53-r3) |
|174| linenoise | (1.0.0+git0+97d2850af1-r1) |
|175| linux-libc-headers | (4.9-r2) |
|176| log4c | (1.2.3-r0) |
|177| logrotate | (3.21.0-r1) |
|178| lsof | (4.94.0-r0) |
|179| lttng-ust | (2.13.6-r0) |
|180| lua | (5.4.4-r0) |
|181| lvm2 | (2.03.11-r0) |
|182| lz4 | (1.9.4-r0) |
|183| lzo | (2.10-r0) |
|184| m4 | (1.4.9-r2) |
|185| mbedtls | (2.16.3-r0) |
|186| mdns | (1556.80.2-r0) |
|187| minizip | (1.0.0+git0+71ef99f6a0-r0) |
|188| mongoose | (2.6-r0) |
|189| msgpack-c | (4.0.0+git0+a9a48cea3a-r0) |
|190| mtdev | (1.1.6-r0) |
|191| mtd-utils | (2.1.5-r1) |
|192| nanomsg | (1.1.5-r0) |
|193| ncurses | (6.3+20220423-r1) |
|194| ndisc6 | (1.0.6-r0) |
|195| ne10 | (1.2.1gitr+0+18c4c982a5-r0) |
|196| nettle | (2.7.1-r0) |
|197| networkmanager | (1.43.7-r7) |
|198| nghttp2 | (1.48.0-r1) |
|199| nopoll | (0.3.2.b232-r0) |
|200| nspr | (4.29-r0) |
|201| nss | (3.74-r1) |
|202| openjpeg | (2.4.0-r0) |
|203| openssh | (8.9p1-r0) |
|204| openssl-1.1.1l | (1.1.1l-r0) |
|205| openssl | (3.0.15-r0) |
|206| opkg | (0.5.0-r1) |
|207| opkg-arch-config | (1.0-r1) |
|208| opkg-utils | (0.5.0-r1) |
|209| orc | (0.4.31-r0) |
|210| packagegroup-oss-layer | (4.8.0-r0) |
|211| perl | (5.34.3-r0) |
|212| pixman | (0.40.0-r0) |
|213| popt | (1.18-r0) |
|214| procps | (3.3.17-r1) |
|215| protobuf | (3.19.6-r0) |
|216| protobuf-c | (1.4.1-r0) |
|217| python | (2.7.18-r0) |
|218| python3 | (3.10.15-r1) |
|219| python3-dbus | (1.2.18-r0) |
|220| qrencode | (4.1.1-r0) |
|221| rapidjson | (1.1.0+git0+0ccdbf364c-r0) |
|222| rdkperf | (1.0.0+git0+d802d561c4-r0) |
|223| rdm | (1.0.1-r1) |
|224| re2 | (2020.11.01-r0) |
|225| readline | (5.2-r9) |
|226| redis | (7.0.13-r1) |
|227| run-postinsts | (1.0-r10) |
|228| safec | (3.7.1-r0) |
|229| safec-common-wrapper | (1.0-r0) |
|230| sbc | (1.5-r0) |
|231| sed | (4.1.2-r0) |
|232| shadow | (4.11.1-r0) |
|233| shadow-securetty | (4.6-r3) |
|234| shared-mime-info | (2.1-r0) |
|235| slang | (2.3.2-r0) |
|236| smcroute | (2.4.4-r0) |
|237| speex | (1.2.0-r0) |
|238| speexdsp | (1.2.0-r0) |
|239| sqlite | (2.8.17-r7) |
|240| sqlite3 | (3.38.5-r1) |
|241| strace | (5.16-r0) |
|242| stunnel | (5.65-r2) |
|243| sysfsutils | (2.1.0-r6) |
|244| syslog-ng | (3.36.1-r3) |
|245| systemd | (230+git0+3a74d4fc90-r12) |
|246| systemd-serialgetty | (1.0.0-r5) |
|247| taglib | (1.12-r0) |
|248| tcpdump | (4.99.4-r0) |
|249| tcp-wrappers | (7.6-r10) |
|250| tiff | (4.3.0-r0) |
|251| trace-cmd | (2.9.1-r0) |
|252| tremor | (20180319-r0) |
|253| trower-base64 | (1.0-r0) |
|254| tzdata | (2024a-r1) |
|255| udev-extraconf | (1.1-r1) |
|256| unzip | (6.0-r5) |
|257| update-rc.d | (0.8-r0) |
|258| util-linux | (2.37.4-r3) |
|259| util-linux-libuuid | (2.37.4-r0) |
|260| util-macros | (1.19.3-r0) |
|261| vala | (0.56.3-r0) |
|262| vmtouch | (1.3.1-r0) |
|263| wayland | (1.20.0-r0) |
|264| wayland-default-egl | (1.20.0-r0) |
|265| wayland-protocols | (1.25-r1) |
|266| websocketpp | (0.8.2-r0) |
|267| wireless-regdb | (2024.07.04-r0) |
|268| wireless-tools | (30.pre9-r0) |
|269| woff2 | (1.0.2-r0) |
|270| wpa-supplicant | (2.10-r7) |
|271| xkeyboard-config | (2.35.1-r0) |
|272| xmlsec1 | (1.2.33-r1) |
|273| xz | (5.2.6-r0) |
|274| yajl | (2.1.0-r0) |
|275| zlib | (1.2.11-r0) |
|276| zstd | (1.5.2-r0) |

### Diff report of the meta layers contributing to this release of OSS layer project is available at below links
- [ ] meta-oss-common-config [1.2.0-->1.3.0] (https://github.com/rdkcentral/meta-rdk-oss-reference/compare/1.2.0...1.3.0)
- [ ] meta-rdk-auxiliary [1.3.0-->1.5.0] (https://github.com/rdkcentral/meta-rdk-auxiliary/compare/1.3.0...1.5.0)
- [ ] meta-rdk-oss-reference [4.7.0-->4.8.0] (https://github.com/rdkcentral/meta-rdk-oss-reference/compare/4.7.0...4.8.0)
- [ ] poky [4.3.1-->4.4.1] (https://github.com/rdkcentral/poky/compare/4.3.1...4.4.1)
