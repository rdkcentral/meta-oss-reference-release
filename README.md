# OSS Layer Release Notes
RDKE OSS Layer Release Notes

---

|Summary|Content|
|---|----|
|Classification|Public|
|Document Version|Issue 1|
|Date|15th May 2026|
|Author|RDKE OSS Team|

| Components | Tag |
|----------|--------|
| packagegroup-oss-layer | 4.13.0-r0|



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

The 4.13.0 OSS release, based on the kirkstone yocto version, delivers architecture-specific and platform-independent artifacts. Within this release, ARM architecture is accommodated with the following variations:
    1. rdk-arm7a-oss: Default tuning is set to armv7athf-neon.
    2. rdk-arm7ve-oss: Default tuning is set to armv7vethf-neon.
    3. rdk-arm64-oss: 64-bit ARM architecture with a multilib configuration and default tuning set to armv7vethf-neon for compatibility with 32-bit systems.
The IPK feed is automatically chosen based on the platform's default tuning configuration, with armv7vethf-neon being the default feed.


## Release layer and components
### OSS stack layer
| Layer | Tag |
|------|------|
|meta-rdk-auxiliary|1.9.0|
|meta-rdk-oss-reference|4.13.0|
|meta-openembedded|rdk-4.0.0|
|poky|rdk-4.7.0|
|meta-python2|rdk-4.0.0|
|meta-rdk-oss-ext|1.8.0|
|meta-virtualization|rdk-4.0.0|
|meta-clang|rdk-4.1.0|
|meta-lts-mixins|rdk-4.0.0|

### Components details in "packagegroup-oss-layer"
|#|OSS layer Component|(=version)|
|-|----------------------|---------|
|1| abseil-cpp | (20211102.0+git0+7c6608d0db-r1) |
|2| acl | (2.3.1-r0) |
|3| alsa-lib | (1.2.6.1-r1) |
|4| alsa-state | (0.2.0-r5) |
|5| alsa-topology-conf | (1.2.5.1-r0) |
|6| alsa-ucm-conf | (1.2.6.3-r0) |
|7| alsa-utils | (1.2.6-r0) |
|8| alsa-utils-scripts | (1.2.6-r0) |
|9| apparmor | (3.1.7-r1) |
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
|23| busybox | (1.35.0-r3) |
|24| bzip2 | (1.0.8-r0) |
|25| ca-certificates | (20211016-r2) |
|26| c-ares | (1.18.1-r0) |
|27| civetweb | (1.10+git+0+0f1b43536d-r0) |
|28| cjson | (1.7.18-r1) |
|29| coreutils | (6.9-r0) |
|30| cracklib | (2.9.8-r0) |
|31| crun | (1.7.2-r0) |
|32| ctemplate | (1.0.0+git0+4b7e6c52dc-r4) |
|33| cunit | (2.1-3-r0) |
|34| curl | (7.82.0-r3) |
|35| db | (5.3.28-r1) |
|36| dbus | (1.14.8-r1) |
|37| dbus-glib | (0.112-r0) |
|38| dibbler | (1.0.1+1.0.2RC1+gita7c6cf58a88a510cb00841351e75030ce78d36bf-r1) |
|39| dnsmasq | (2.90-r5) |
|40| dosfstools | (2.11-r0) |
|41| e2fsprogs | (1.46.5-r0) |
|42| ebtables | (2.0.11-r4) |
|43| elfutils | (0.186-r0) |
|44| ethtool | (5.16-r0) |
|45| evtest | (1.34-r0) |
|46| expat | (2.5.0-r0) |
|47| fcgi | (2.4.2-r1) |
|48| file | (5.41-r1) |
|49| findutils | (4.2.31-r0) |
|50| flac | (1.3.4-r0) |
|51| flex | (2.6.4-r0) |
|52| fmt | (8.1.1-r0) |
|53| fontconfig | (2.13.1-r1) |
|54| freetype | (2.11.1-r1) |
|55| fribidi | (1.0.13-r0) |
|56| gawk | (3.1.5-r4) |
|57| gcc-runtime | (11.3.0-r0) |
|58| gcc-sanitizers | (11.3.0-r0) |
|59| gdbm | (1.8.3-r4) |
|60| gdk-pixbuf | (2.42.10-r0) |
|61| gettext | (0.16.1-r6) |
|62| gflags | (2.2.2-r0) |
|63| glib-2.0 | (2.74.6-r0) |
|64| glibc | (2.35-r1) |
|65| glibc-locale | (2.35-r0) |
|66| glibc-mtrace | (2.35-r0) |
|67| glib-networking | (2.74.0-r0) |
|68| gmp | (4.2.1-r1) |
|69| gnutls | (3.3.30-r1) |
|70| gobject-introspection | (1.72.0-r0) |
|71| googletest | (1.11.0+git0+9e71237221-r0) |
|72| graphite2 | (1.3.6-r0) |
|73| grpc | (1.46.7-r1) |
|74| gssdp | (1.4.0.1-r0) |
|75| gssdp16 | (1.6.3-r0) |
|76| gupnp | (0.20.10-r1) |
|77| harfbuzz | (4.0.1-r0) |
|78| heaptrack | (1.5.0-r0) |
|79| hiredis | (1.0.2-r0) |
|80| icu | (70.1-r0) |
|81| initscripts | (1.0-r155) |
|82| init-system-helpers | (1.62-r0) |
|83| iperf3 | (3.14-r0) |
|84| iptables | (1.8.7-r4) |
|85| iw | (4.7-r0) |
|86| iso-codes | (4.15.0-r0) |
|87| jansson | (2.13.1-r0) |
|88| jquery | (1.0.0-r3) |
|89| json-c | (0.15-r0) |
|90| jsoncpp | (1.8.4-r0) |
|91| jsonrpc | (1.3.0-r0) |
|92| kbd | (2.4.0-r1) |
|93| keyutils | (1.6.1-r0) |
|94| kmod | (29-r0) |
|95| lcms | (2.13.1-r0) |
|96| libaio | (0.3.112-r0) |
|97| libarchive | (3.6.1-r3) |
|98| libatomic-ops | (7.6.14-r1) |
|99| libbsd | (0.11.5-r0) |
|100| libcap | (2.66-r1) |
|101| libcap-ng | (0.8.2-r0) |
|102| libcgroup | (2.0.2-r0) |
|103| libcheck | (0.15.2-r1) |
|104| libcroco | (0.6.13-r0) |
|105| libdaemon | (0.14-r0) |
|106| libdash | (1.0.0+git0+f5b5d991af-r1) |
|107| libdwarf | (20210528-r0) |
|108| liberation-fonts | (2.1.5-r0) |
|109| libev | (4.33-r0) |
|110| libevdev | (1.12.1-r1) |
|111| libevent | (2.1.12-r0) |
|112| libexif | (0.6.24-r0) |
|113| libffi | (3.4.4-r1) |
|114| libgcc | (11.3.0-r0) |
|115| libgcrypt | (1.9.4-r1) |
|116| libgpg-error | (1.44-r1) |
|117| libgudev | (237-r0) |
|118| libical | (3.0.16-r1) |
|119| libidn2 | (2.3.2-r0) |
|120| libinput | (1.19.4-r0) |
|121| libjpeg | (62.3.0-r0) |
|122| libmanette | (0.2.6-r5) |
|123| libmd | (1.0.4-r0) |
|124| libmicrohttpd | (0.9.76-r0) |
|125| libmng | (2.0.3-r0) |
|126| libmnl | (1.0.4-r0) |
|127| libndp | (1.8-r0) |
|128| libnewt | (0.52.23-r0) |
|129| libnl | (3.5.0-r1) |
|130| libnsl2 | (2.0.0-r0) |
|131| libnss-mdns | (0.15.1-r1) |
|132| liboauth | (1.0.3-r0) |
|133| libogg | (1.3.5-r0) |
|134| libol | (0.3.18-r0) |
|135| libomxil | (0.9.3-r1) |
|136| libopus | (1.3.1-r0) |
|137| libp11 | (0.4.17-r0) |
|138| libpam | (1.5.2-r0) |
|139| libpcap | (1.10.1-r2) |
|140| libpciaccess | (0.16-r0) |
|141| libpcre2 | (10.40-r0) |
|142| libpcre | (8.39-r0) |
|143| libpng | (1.6.39-r0) |
|144| libpsl | (0.21.1-r0) |
|145| libpthread-stubs | (0.4-r0) |
|146| libsamplerate0 | (0.2.2-r1) |
|147| libsdl | (1.2.15-r3) |
|148| libsdl-image | (1.2.12-r0) |
|149| libsdl-ttf | (2.0.11-r0) |
|150| libseccomp | (2.4.3-r1) |
|151| libsndfile1 | (1.0.31-r0) |
|152| libsolv | (0.7.22-r0) |
|153| libsoup-2.4 | (2.74.2-r1) |
|154| libsoup | (3.6.5-r1) |
|155| libstd-rs | (1.82.0-r0) |
|156| libtasn1 | (4.13-r1) |
|157| libtheora | (1.1.1-r1) |
|158| libtinyxml | (2.6.2-r5) |
|159| libtinyxml2 | (9.0.0-r0) |
|160| libtirpc | (1.3.2-r0) |
|161| libtool | (2.4.7-r1) |
|162| libunistring | (1.0-r0) |
|163| libunwind | (1.7.0-r0) |
|164| liburcu | (0.13.2-r1) |
|165| libusb1 | (1.0.27-r0) |
|166| libuv | (1.44.2-r0) |
|167| libvorbis | (1.3.7-r0) |
|168| libvpx | (1.12.0-r1) |
|169| libwebp | (1.3.2-r0) |
|170| libwebsockets | (4.2.2-r0) |
|171| libxcrypt | (4.4.33-r1) |
|172| libxkbcommon | (0.5.0-r0) |
|173| libxml2 | (2.9.14-r2) |
|174| libxslt | (1.1.35-r1) |
|175| libzip | (1.8.0-r0) |
|176| lighttpd | (1.4.53-r3) |
|177| linenoise | (1.0.0+git0+97d2850af1-r1) |
|178| linux-libc-headers | (4.9-r2) |
|179| log4c | (1.2.3-r0) |
|180| logrotate | (3.21.0-r2) |
|181| lsof | (4.94.0-r0) |
|182| lttng-ust | (2.13.6-r0) |
|183| lua | (5.4.4-r0) |
|184| lvm2 | (2.03.11-r0) |
|185| lz4 | (1.9.4-r1) |
|186| lzo | (2.10-r0) |
|187| m4 | (1.4.9-r2) |
|188| mbedtls | (2.16.3-r0) |
|189| mdns | (1556.80.2-r0) |
|190| minizip | (1.0.0+git0+71ef99f6a0-r0) |
|191| mongoose | (2.6-r0) |
|192| mosquitto | (2.0.18-r0) |
|193| msgpack-c | (4.0.0+git0+a9a48cea3a-r0) |
|194| mtdev | (1.1.6-r0) |
|195| mtd-utils | (2.1.5-r2) |
|196| nanomsg | (1.1.5-r0) |
|197| ncurses | (6.3+20220423-r2) |
|198| ndisc6 | (1.0.6-r0) |
|199| ne10 | (1.2.1gitr+0+18c4c982a5-r0) |
|200| nettle | (2.7.1-r1) |
|201| networkmanager | (1.43.7-r12) |
|202| nghttp2 | (1.48.0-r1) |
|203| nopoll | (0.3.2.b232-r0) |
|204| nspr | (4.29-r0) |
|205| nss | (3.74-r2) |
|206| openjpeg | (2.4.0-r0) |
|207| openssh | (8.9p1-r0) |
|208| openssl-1.1.1l | (1.1.1l-r0) |
|209| openssl | (3.0.15-r3) |
|210| opkg | (0.5.0-r4) |
|211| opkg-arch-config | (1.0-r1) |
|212| opkg-utils | (0.5.0-r2) |
|213| orc | (0.4.31-r0) |
|214| packagegroup-oss-layer | (4.13.0-r0) |
|215| paho-mqtt-c | (1.3.10-r0) |
|216| perl | (5.34.3-r0) |
|217| pixman | (0.40.0-r0) |
|218| popt | (1.18-r0) |
|219| procps | (3.3.17-r2) |
|220| protobuf | (3.19.6-r0) |
|221| protobuf-c | (1.4.1-r0) |
|222| python | (2.7.18-r0) |
|223| python3 | (3.10.15-r1) |
|224| python3-dbus | (1.2.18-r0) |
|225| qrencode | (4.1.1-r0) |
|226| rapidjson | (1.1.0+git0+0ccdbf364c-r0) |
|227| rdkperf | (1.0.0+git0+d802d561c4-r0) |
|228| re2 | (2020.11.01-r0) |
|229| readline | (5.2-r9) |
|230| redis | (7.0.13-r1) |
|231| run-postinsts | (1.0-r10) |
|232| safec | (3.7.1-r0) |
|233| safec-common-wrapper | (1.0-r0) |
|234| sbc | (1.5-r0) |
|235| sed | (4.1.2-r1) |
|236| shadow | (4.11.1-r0) |
|237| shadow-securetty | (4.6-r3) |
|238| shared-mime-info | (2.1-r0) |
|239| slang | (2.3.2-r0) |
|240| smcroute | (2.4.4-r0) |
|241| speex | (1.2.0-r0) |
|242| speexdsp | (1.2.0-r0) |
|243| sqlite | (2.8.17-r7) |
|244| sqlite3 | (3.38.5-r1) |
|245| strace | (5.16-r0) |
|246| stunnel | (5.65-r3) |
|247| sysfsutils | (2.1.0-r6) |
|248| syslog-ng | (3.36.1-r3) |
|249| systemd | (230+git0+3a74d4fc90-r13) |
|250| systemd-serialgetty | (1.0.0-r5) |
|251| taglib | (1.12-r0) |
|252| tcpdump | (4.99.4-r0) |
|253| tcp-wrappers | (7.6-r10) |
|254| tiff | (4.3.0-r0) |
|255| trace-cmd | (2.9.1-r0) |
|256| tremor | (20180319-r0) |
|257| trower-base64 | (1.0-r0) |
|258| tzdata | (2024a-r1) |
|259| udev-extraconf | (1.1-r1) |
|260| unzip | (6.0-r5) |
|261| update-rc.d | (0.8-r0) |
|262| util-linux | (2.37.4-r3) |
|263| util-linux-libuuid | (2.37.4-r0) |
|264| util-macros | (1.19.3-r0) |
|265| vala | (0.56.3-r0) |
|266| vmtouch | (1.3.1-r0) |
|267| wayland | (1.20.0-r0) |
|268| wayland-default-egl | (1.20.0-r0) |
|269| wayland-protocols | (1.25-r1) |
|270| websocketpp | (0.8.2-r0) |
|271| wireless-regdb | (2024.07.04-r0) |
|272| wireless-tools | (30.pre9-r0) |
|273| woff2 | (1.0.2-r0) |
|274| wpa-supplicant | (2.10-r11) |
|275| xkeyboard-config | (2.35.1-r0) |
|276| xmlsec1 | (1.2.33-r1) |
|277| xz | (5.2.6-r1) |
|278| yajl | (2.1.0-r1) |
|279| yaml-cpp | (0.7.0-r0) |
|280| zlib | (1.2.11-r1) |
|281| zstd | (1.5.2-r1) |

### Diff report of the meta layers contributing to this release of OSS layer project is available at below links
- [ ] meta-rdk-auxiliary [1.8.0-->1.9.0] (https://github.com/rdkcentral/meta-rdk-auxiliary/compare/1.8.0...1.9.0)
- [ ] meta-rdk-oss-reference [4.12.0-->4.13.0] (https://github.com/rdkcentral/meta-rdk-oss-reference/compare/4.12.0...4.13.0)
- [ ] poky [rdk-4.6.0-->rdk-4.7.0] (https://github.com/rdkcentral/poky/compare/rdk-4.6.0...rdk-4.7.0)
