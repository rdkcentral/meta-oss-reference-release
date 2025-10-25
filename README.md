# OSS Layer Release Notes
RDKE OSS Layer Release Notes

---

|Summary|Content|
|---|----|
|Classification|Public|
|Document Version|Issue 1|
|Date|24th October 2025|
|Author|RDKE Platform & Tools Team|

| Components | Tag |
|----------|--------|
| packagegroup-oss-layer | 4.9.0-r0|



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

The 4.9.0 OSS release, based on the kirkstone yocto version, delivers architecture-specific and platform-independent artifacts. Within this release, ARM architecture is accommodated with the following variations:
    1. rdk-arm7a-oss: Default tuning is set to armv7athf-neon.
    2. rdk-arm7ve-oss: Default tuning is set to armv7vethf-neon.
    3. rdk-arm64-oss: 64-bit ARM architecture with a multilib configuration and default tuning set to armv7vethf-neon for compatibility with 32-bit systems.
The IPK feed is automatically chosen based on the platform's default tuning configuration, with armv7vethf-neon being the default feed.


## Release layer and components
### OSS stack layer
| Layer | Tag |
|------|------|
|meta-rdk-auxiliary|1.6.0|
|meta-rdk-oss-reference|4.9.0|
|meta-openembedded|rdk-4.0.0|
|poky|rdk-4.4.1|
|meta-python2|rdk-4.0.0|
|meta-rdk-oss-ext|1.5.0|
|meta-virtualization|rdk-4.0.0|
|meta-clang|rdk-4.0.0|
|meta-lts-mixins|rdk-4.0.0|

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
|9| apparmor | (3.1.7-r0) |
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
|36| dbus | (1.14.8-r1) |
|37| dbus-glib | (0.112-r0) |
|38| dibbler | (1.0.1+1.0.2RC1+gita7c6cf58a88a510cb00841351e75030ce78d36bf-r1) |
|39| dnsmasq | (2.90-r4) |
|40| dosfstools | (2.11-r0) |
|41| e2fsprogs | (1.46.5-r0) |
|42| ebtables | (2.0.11-r4) |
|43| elfutils | (0.186-r0) |
|44| ethtool | (5.16-r0) |
|45| evtest | (1.34-r0) |
|46| expat | (2.5.0-r0) |
|47| fcgi | (2.4.2-r1) |
|48| file | (5.41-r0) |
|49| findutils | (4.2.31-r0) |
|50| flac | (1.3.4-r0) |
|51| flex | (2.6.4-r0) |
|52| fmt | (8.1.1-r0) |
|53| fontconfig | (2.13.1-r0) |
|54| freetype | (2.11.1-r1) |
|55| fribidi | (1.0.13-r0) |
|56| gawk | (3.1.5-r2) |
|57| gcc-runtime | (11.3.0-r0) |
|58| gcc-sanitizers | (11.3.0-r0) |
|59| gdbm | (1.8.3-r4) |
|60| gdk-pixbuf | (2.42.10-r0) |
|61| gettext | (0.16.1-r6) |
|62| gflags | (2.2.2-r0) |
|63| glib-2.0 | (2.72.3-r1) |
|64| glibc | (2.35-r1) |
|65| glibc-locale | (2.35-r0) |
|66| glibc-mtrace | (2.35-r0) |
|67| glib-networking | (2.72.2-r2) |
|68| gmp | (4.2.1-r0) |
|69| gnutls | (3.3.30-r1) |
|70| gobject-introspection | (1.72.0-r0) |
|71| googletest | (1.11.0+git0+9e71237221-r0) |
|72| graphite2 | (1.3.6-r0) |
|73| grpc | (1.46.7-r1) |
|74| gssdp | (1.4.0.1-r0) |
|75| gupnp | (0.20.10-r1) |
|76| harfbuzz | (4.0.1-r0) |
|77| heaptrack | (1.5.0-r0) |
|78| hiredis | (1.0.2-r0) |
|79| icu | (70.1-r0) |
|80| initscripts | (1.0-r155) |
|81| init-system-helpers | (1.62-r0) |
|82| iperf3 | (3.14-r0) |
|83| iptables | (1.8.7-r3) |
|84| iso-codes | (4.15.0-r0) |
|85| iw | (4.7-r0) |
|86| jansson | (2.13.1-r0) |
|87| jquery | (1.0.0-r3) |
|88| json-c | (0.15-r0) |
|89| jsoncpp | (1.8.4-r0) |
|90| jsonrpc | (1.3.0-r0) |
|91| kbd | (2.4.0-r0) |
|92| keyutils | (1.6.1-r0) |
|93| kmod | (29-r0) |
|94| lcms | (2.13.1-r0) |
|95| libaio | (0.3.112-r0) |
|96| libarchive | (3.6.1-r2) |
|97| libatomic-ops | (7.6.14-r0) |
|98| libbsd | (0.11.5-r0) |
|99| libcap | (2.66-r0) |
|100| libcap-ng | (0.8.2-r0) |
|101| libcgroup | (2.0.2-r0) |
|102| libcheck | (0.15.2-r0) |
|103| libcroco | (0.6.13-r0) |
|104| libdaemon | (0.14-r0) |
|105| libdash | (1.0.0+git0+f5b5d991af-r1) |
|106| libdwarf | (20210528-r0) |
|107| liberation-fonts | (2.1.5-r0) |
|108| libev | (4.33-r0) |
|109| libevdev | (1.12.1-r1) |
|110| libevent | (2.1.12-r0) |
|111| libexif | (0.6.24-r0) |
|112| libffi | (3.4.4-r0) |
|113| libgcc | (11.3.0-r0) |
|114| libgcrypt | (1.9.4-r1) |
|115| libgpg-error | (1.44-r1) |
|116| libgudev | (237-r0) |
|117| libical | (3.0.16-r1) |
|118| libidn2 | (2.3.2-r0) |
|119| libinput | (1.19.4-r0) |
|120| libjpeg | (62.3.0-r0) |
|121| libmanette | (0.2.6-r1) |
|122| libmd | (1.0.4-r0) |
|123| libmicrohttpd | (0.9.76-r0) |
|124| libmng | (2.0.3-r0) |
|125| libmnl | (1.0.4-r0) |
|126| libndp | (1.8-r0) |
|127| libnewt | (0.52.23-r0) |
|128| libnl | (3.5.0-r1) |
|129| libnsl2 | (2.0.0-r0) |
|130| libnss-mdns | (0.15.1-r1) |
|131| liboauth | (1.0.3-r0) |
|132| libogg | (1.3.5-r0) |
|133| libol | (0.3.18-r0) |
|134| libomxil | (0.9.3-r1) |
|135| libopus | (1.3.1-r0) |
|136| libpam | (1.5.2-r0) |
|137| libpcap | (1.10.1-r1) |
|138| libpciaccess | (0.16-r0) |
|139| libpcre2 | (10.40-r0) |
|140| libpcre | (8.39-r0) |
|141| libpng | (1.6.39-r0) |
|142| libpsl | (0.21.1-r0) |
|143| libpthread-stubs | (0.4-r0) |
|144| libsamplerate0 | (0.2.2-r1) |
|145| libsdl | (1.2.15-r3) |
|146| libsdl-image | (1.2.12-r0) |
|147| libsdl-ttf | (2.0.11-r0) |
|148| libseccomp | (2.4.3-r1) |
|149| libsndfile1 | (1.0.31-r0) |
|150| libsolv | (0.7.22-r0) |
|151| libsoup-2.4 | (2.74.2-r1) |
|152| libsoup | (3.6.5-r1) |
|153| libstd-rs | (1.82.0-r0) |
|154| libtasn1 | (4.13-r1) |
|155| libtheora | (1.1.1-r1) |
|156| libtinyxml | (2.6.2-r5) |
|157| libtinyxml2 | (9.0.0-r0) |
|158| libtirpc | (1.3.2-r0) |
|159| libtool | (2.4.7-r0) |
|160| libunistring | (1.0-r0) |
|161| libunwind | (1.7.0-r0) |
|162| liburcu | (0.13.2-r0) |
|163| libusb1 | (1.0.27-r0) |
|164| libuv | (1.44.2-r0) |
|165| libvorbis | (1.3.7-r0) |
|166| libvpx | (1.12.0-r1) |
|167| libwebp | (1.3.2-r0) |
|168| libwebsockets | (4.2.2-r0) |
|169| libxcrypt | (4.4.33-r0) |
|170| libxkbcommon | (0.5.0-r0) |
|171| libxml2 | (2.9.14-r1) |
|172| libxslt | (1.1.35-r0) |
|173| libzip | (1.8.0-r0) |
|174| lighttpd | (1.4.53-r3) |
|175| linenoise | (1.0.0+git0+97d2850af1-r1) |
|176| linux-libc-headers | (4.9-r2) |
|177| log4c | (1.2.3-r0) |
|178| logrotate | (3.21.0-r2) |
|179| lsof | (4.94.0-r0) |
|180| lttng-ust | (2.13.6-r0) |
|181| lua | (5.4.4-r0) |
|182| lvm2 | (2.03.11-r0) |
|183| lz4 | (1.9.4-r0) |
|184| lzo | (2.10-r0) |
|185| m4 | (1.4.9-r2) |
|186| mbedtls | (2.16.3-r0) |
|187| mdns | (1556.80.2-r0) |
|188| minizip | (1.0.0+git0+71ef99f6a0-r0) |
|189| mongoose | (2.6-r0) |
|190| mosquitto | (2.0.18-r0) |
|191| msgpack-c | (4.0.0+git0+a9a48cea3a-r0) |
|192| mtdev | (1.1.6-r0) |
|193| mtd-utils | (2.1.5-r2) |
|194| nanomsg | (1.1.5-r0) |
|195| ncurses | (6.3+20220423-r1) |
|196| ndisc6 | (1.0.6-r0) |
|197| ne10 | (1.2.1gitr+0+18c4c982a5-r0) |
|198| nettle | (2.7.1-r1) |
|199| networkmanager | (1.43.7-r11) |
|200| nghttp2 | (1.48.0-r1) |
|201| nopoll | (0.3.2.b232-r0) |
|202| nspr | (4.29-r0) |
|203| nss | (3.74-r2) |
|204| openjpeg | (2.4.0-r0) |
|205| openssh | (8.9p1-r0) |
|206| openssl-1.1.1l | (1.1.1l-r0) |
|207| openssl | (3.0.15-r0) |
|208| opkg | (0.5.0-r1) |
|209| opkg-arch-config | (1.0-r1) |
|210| opkg-utils | (0.5.0-r1) |
|211| orc | (0.4.31-r0) |
|212| packagegroup-oss-layer | (4.9.0-r0) |
|213| paho-mqtt-c | (1.3.10-r0) |
|214| perl | (5.34.3-r0) |
|215| pixman | (0.40.0-r0) |
|216| popt | (1.18-r0) |
|217| procps | (3.3.17-r1) |
|218| protobuf | (3.19.6-r0) |
|219| protobuf-c | (1.4.1-r0) |
|220| python | (2.7.18-r0) |
|221| python3 | (3.10.15-r1) |
|222| python3-dbus | (1.2.18-r0) |
|223| qrencode | (4.1.1-r0) |
|224| rapidjson | (1.1.0+git0+0ccdbf364c-r0) |
|225| rdkperf | (1.0.0+git0+d802d561c4-r0) |
|226| rdm | (1.0.1-r1) |
|227| re2 | (2020.11.01-r0) |
|228| readline | (5.2-r9) |
|229| redis | (7.0.13-r1) |
|230| run-postinsts | (1.0-r10) |
|231| safec | (3.7.1-r0) |
|232| safec-common-wrapper | (1.0-r0) |
|233| sbc | (1.5-r0) |
|234| sed | (4.1.2-r0) |
|235| shadow | (4.11.1-r0) |
|236| shadow-securetty | (4.6-r3) |
|237| shared-mime-info | (2.1-r0) |
|238| slang | (2.3.2-r0) |
|239| smcroute | (2.4.4-r0) |
|240| speex | (1.2.0-r0) |
|241| speexdsp | (1.2.0-r0) |
|242| sqlite | (2.8.17-r7) |
|243| sqlite3 | (3.38.5-r1) |
|244| strace | (5.16-r0) |
|245| stunnel | (5.65-r2) |
|246| sysfsutils | (2.1.0-r6) |
|247| syslog-ng | (3.36.1-r3) |
|248| systemd | (230+git0+3a74d4fc90-r13) |
|249| systemd-serialgetty | (1.0.0-r5) |
|250| taglib | (1.12-r0) |
|251| tcpdump | (4.99.4-r0) |
|252| tcp-wrappers | (7.6-r10) |
|253| tiff | (4.3.0-r0) |
|254| trace-cmd | (2.9.1-r0) |
|255| tremor | (20180319-r0) |
|256| trower-base64 | (1.0-r0) |
|257| tzdata | (2024a-r1) |
|258| udev-extraconf | (1.1-r1) |
|259| unzip | (6.0-r5) |
|260| update-rc.d | (0.8-r0) |
|261| util-linux | (2.37.4-r3) |
|262| util-linux-libuuid | (2.37.4-r0) |
|263| util-macros | (1.19.3-r0) |
|264| vala | (0.56.3-r0) |
|265| vmtouch | (1.3.1-r0) |
|266| wayland | (1.20.0-r0) |
|267| wayland-default-egl | (1.20.0-r0) |
|268| wayland-protocols | (1.25-r1) |
|269| websocketpp | (0.8.2-r0) |
|270| wireless-regdb | (2024.07.04-r0) |
|271| wireless-tools | (30.pre9-r0) |
|272| woff2 | (1.0.2-r0) |
|273| wpa-supplicant | (2.10-r7) |
|274| xkeyboard-config | (2.35.1-r0) |
|275| xmlsec1 | (1.2.33-r1) |
|276| xz | (5.2.6-r0) |
|277| yajl | (2.1.0-r0) |
|278| zlib | (1.2.11-r0) |
|279| zstd | (1.5.2-r0) |

### Diff report of the meta layers contributing to this release of OSS layer project is available at below links
- [ ] meta-oss-common-config [1.3.0-->1.3.1] (https://github.com/rdkcentral/meta-oss-common-config/compare/1.3.0...1.3.1)
- [ ] meta-rdk-auxiliary [1.5.0-->1.6.0] (https://github.com/rdkcentral/meta-rdk-auxiliary/compare/1.5.0...1.6.0)
- [ ] meta-rdk-oss-reference [4.8.0-->4.9.0] (https://github.com/rdkcentral/meta-rdk-oss-reference/compare/4.8.0...4.9.0)
