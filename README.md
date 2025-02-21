# OSS Layer Release Notes
RDKE OSS Layer Release Notes

---

|Summary|Content|
|---|----|
|Classification|Public|
|Document Version|Issue 1|
|Date|10th January 2025|
|Author|RDKE Platform & Tools Team|

| Components | Tag |
|----------|--------|
| packagegroup-oss-layer | 4.4.0-r0|



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

The 4.4.0 OSS release, based on the kirkstone yocto version, delivers architecture-specific and platform-independent artifacts. Within this release, ARM architecture is accommodated with the following variations:
    1. rdk-arm7a-oss: Default tuning is set to armv7athf-neon.
    2. rdk-arm7ve-oss: Default tuning is set to armv7vethf-neon.
    3. rdk-arm64-oss: 64-bit ARM architecture with a multilib configuration and default tuning set to armv7vethf-neon for compatibility with 32-bit systems.
The IPK feed is automatically chosen based on the platform's default tuning configuration, with armv7vethf-neon being the default feed.


## Release layer and components
### OSS stack layer
| Layer | Tag |
|------|------|
|meta-rdk-auxiliary|4.1.4|
|meta-rdk-oss-reference|4.4.0|

### Components details in "packagegroup-oss-layer"

|#|OSS layer Component|(=version)|
|-|----------------------|---------|
|1| abseil-cpp | (20211102.0+git0+7c6608d0db-r0) |
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
|18| bind | (9.18.5-r0) |
|19| boost | (1.78.0-r0) |
|20| breakpad | (1.0-r1) |
|21| breakpad-wrapper | (1.0-r0) |
|22| brotli | (1.0.9-r0) |
|23| busybox | (1.35.0-r1) |
|24| bzip2 | (1.0.8-r0) |
|25| ca-certificates | (20211016-r2) |
|26| c-ares | (1.18.1-r0) |
|27| civetweb | (1.10+git+0+0f1b43536d-r0) |
|28| cjson | (1.7.15-r0) |
|29| coreutils | (6.9-r0) |
|30| cracklib | (2.9.8-r0) |
|31| crun | (1.7.2-r0) |
|32| ctemplate | (1.0.0+git0+4b7e6c52dc-r3) |
|33| cunit | (2.1-3-r0) |
|34| curl | (7.82.0-r1) |
|35| db | (5.3.28-r1) |
|36| dbus | (1.14.0-r0) |
|37| dbus-glib | (0.112-r0) |
|38| dibbler | (1.0.1+1.0.2RC1+gita7c6cf58a88a510cb00841351e75030ce78d36bf-r1) |
|39| dnsmasq | (2.86-r4) |
|40| dosfstools | (2.11-r0) |
|41| e2fsprogs | (1.46.5-r0) |
|42| ebtables | (2.0.11-r4) |
|43| elfutils | (0.186-r0) |
|44| evtest | (1.34-r0) |
|45| expat | (2.4.9-r0) |
|46| fcgi | (2.4.2-r0) |
|47| file | (5.41-r0) |
|48| findutils | (4.2.31-r0) |
|49| flac | (1.3.4-r0) |
|50| flex | (2.6.4-r0) |
|51| fontconfig | (2.13.1-r0) |
|52| freetype | (2.11.1-r1) |
|53| fribidi | (1.0.12-r0) |
|54| gawk | (3.1.5-r2) |
|55| gcc-runtime | (11.3.0-r0) |
|56| gcc-sanitizers | (11.3.0-r0) |
|57| gdb | (11.2-r0) |
|58| gdbm | (1.8.3-r4) |
|59| gdk-pixbuf | (2.42.9-r0) |
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
|72| grpc | (1.45.2-r0) |
|73| gssdp | (1.4.0.1-r0) |
|74| gupnp | (0.20.10-r1) |
|75| harfbuzz | (4.0.1-r0) |
|76| heaptrack | (1.5.0-r0) |
|77| hiredis | (1.0.2-r0) |
|78| icu | (70.1-r0) |
|79| initscripts | (1.0-r155) |
|80| init-system-helpers | (1.62-r0) |
|81| iperf3 | (3.11-r0) |
|82| iptables | (1.8.7-r0) |
|83| iso-codes | (4.11.0-r0) |
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
|95| libarchive | (3.6.1-r0) |
|96| libatomic-ops | (7.6.14-r0) |
|97| libbsd | (0.11.5-r0) |
|98| libcap | (2.65-r0) |
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
|111| libffi | (3.4.2-r0) |
|112| libgcc | (11.3.0-r0) |
|113| libgcrypt | (1.9.4-r0) |
|114| libgpg-error | (1.44-r0) |
|115| libgudev | (237-r0) |
|116| libical | (3.0.14-r0) |
|117| libidn2 | (2.3.2-r0) |
|118| libinput | (1.19.4-r0) |
|119| libjpeg | (62.3.0-r0) |
|120| libmanette | (0.2.6-r0) |
|121| libmd | (1.0.4-r0) |
|122| libmicrohttpd | (0.9.75-r0) |
|123| libmng | (2.0.3-r0) |
|124| libndp | (1.8-r0) |
|125| libnewt | (0.52.21-r0) |
|126| libnl | (3.5.0-r0) |
|127| libnsl2 | (2.0.0-r0) |
|128| libnss-mdns | (0.15.1-r0) |
|129| liboauth | (1.0.3-r0) |
|130| libogg | (1.3.5-r0) |
|131| libol | (0.3.18-r0) |
|132| libomxil | (0.9.3-r0) |
|133| libopus | (1.3.1-r0) |
|134| libpam | (1.5.2-r0) |
|135| libpcap | (1.10.1-r1) |
|136| libpciaccess | (0.16-r0) |
|137| libpcre2 | (10.40-r0) |
|138| libpcre | (8.39-r0) |
|139| libpng | (1.6.38-r0) |
|140| libpsl | (0.21.1-r0) |
|141| libpthread-stubs | (0.4-r0) |
|142| libsamplerate0 | (0.2.2-r1) |
|143| libsdl | (1.2.15-r3) |
|144| libsdl-image | (1.2.12-r0) |
|145| libsdl-ttf | (2.0.11-r0) |
|146| libseccomp | (2.4.3-r0) |
|147| libsndfile1 | (1.0.31-r0) |
|148| libsolv | (0.7.22-r0) |
|149| libsoup-2.4 | (2.74.2-r1) |
|150| libsoup | (3.4.2-r0) |
|151| libstd-rs | (1.72.0-r0) |
|152| libtasn1 | (4.13-r1) |
|153| libtheora | (1.1.1-r1) |
|154| libtinyxml | (2.6.2-r5) |
|155| libtinyxml2 | (9.0.0-r0) |
|156| libtirpc | (1.3.2-r0) |
|157| libtool | (2.4.7-r0) |
|158| libunistring | (1.0-r0) |
|159| libunwind | (1.7.0-r0) |
|160| liburcu | (0.13.2-r0) |
|161| libusb1 | (1.0.27-r0) |
|162| libuv | (1.44.2-r0) |
|163| libvorbis | (1.3.7-r0) |
|164| libvpx | (1.12.0-r0) |
|165| libwebp | (1.3.2-r0) |
|166| libwebsockets | (4.2.2-r0) |
|167| libxcrypt | (4.4.28-r0) |
|168| libxkbcommon | (0.5.0-r0) |
|169| libxml2 | (2.9.14-r0) |
|170| libxslt | (1.1.35-r0) |
|171| libzip | (1.8.0-r0) |
|172| lighttpd | (1.4.53-r2) |
|173| linenoise | (1.0.0+git0+97d2850af1-r1) |
|174| linux-libc-headers | (4.9-r1) |
|175| log4c | (1.2.3-r0) |
|176| logrotate | (3.21.0-r1) |
|177| lttng-ust | (2.13.3-r0) |
|178| lua | (5.4.4-r0) |
|179| lvm2 | (2.03.11-r0) |
|180| lz4 | (1.9.4-r0) |
|181| lzo | (2.10-r0) |
|182| m4 | (1.4.9-r2) |
|183| mbedtls | (2.16.3-r0) |
|184| mdns | (1556.80.2-r0) |
|185| minizip | (1.0.0+git0+71ef99f6a0-r0) |
|186| mongoose | (2.6-r0) |
|187| msgpack-c | (4.0.0+git0+a9a48cea3a-r0) |
|188| mtdev | (1.1.6-r0) |
|189| mtd-utils | (2.1.4-r1) |
|190| nanomsg | (1.1.5-r0) |
|191| ncurses | (6.3+20220423-r1) |
|192| ndisc6 | (1.0.6-r0) |
|193| ne10 | (1.2.1gitr+0+18c4c982a5-r0) |
|194| nettle | (2.7.1-r0) |
|195| networkmanager | (1.43.7-r1) |
|196| nghttp2 | (1.48.0-r1) |
|197| nopoll | (0.3.2.b232-r0) |
|198| nspr | (4.29-r0) |
|199| nss | (3.74-r0) |
|200| openjpeg | (2.4.0-r0) |
|201| openssh | (8.9p1-r0) |
|202| openssl-1.1.1l | (1.1.1l-r0) |
|203| openssl | (3.0.5-r0) |
|204| opkg | (0.5.0-r1) |
|205| opkg-arch-config | (1.0-r1) |
|206| opkg-utils | (0.5.0-r0) |
|207| orc | (0.4.31-r0) |
|208| packagegroup-core-tools-debug | (1.0-r0) |
|209| packagegroup-oss-layer | (4.4.0-r0) |
|210| perl | (5.34.1-r1) |
|211| pixman | (0.40.0-r0) |
|212| popt | (1.18-r0) |
|213| procps | (3.3.17-r1) |
|214| protobuf | (3.19.4-r0) |
|215| protobuf-c | (1.4.1-r0) |
|216| python | (2.7.18-r0) |
|217| python3 | (3.10.4-r1) |
|218| python3-dbus | (1.2.18-r0) |
|219| qrencode | (4.1.1-r0) |
|220| rapidjson | (1.1.0+git0+0ccdbf364c-r0) |
|221| rdkperf | (git-r0) |
|222| rdm | (1.0.1-r1) |
|223| re2 | (2020.11.01-r0) |
|224| readline | (5.2-r9) |
|225| redis | (7.0.4-r1) |
|226| run-postinsts | (1.0-r10) |
|227| safec | (3.7.1-r0) |
|228| safec-common-wrapper | (1.0-r0) |
|229| sbc | (1.5-r0) |
|230| sed | (4.1.2-r0) |
|231| shadow | (4.11.1-r0) |
|232| shadow-securetty | (4.6-r3) |
|233| shared-mime-info | (2.1-r0) |
|234| slang | (2.3.2-r0) |
|235| smcroute | (2.4.4-r0) |
|236| speex | (1.2.0-r0) |
|237| speexdsp | (1.2.0-r0) |
|238| sqlite | (2.8.17-r7) |
|239| sqlite3 | (3.38.5-r1) |
|240| strace | (5.16-r0) |
|241| stunnel | (5.65-r2) |
|242| sysfsutils | (2.1.0-r5) |
|243| syslog-ng | (3.36.1-r2) |
|244| systemd | (230+git0+3a74d4fc90-r10) |
|245| systemd-serialgetty | (1.0.0-r5) |
|246| taglib | (1.12-r0) |
|247| tcpdump | (4.99.1-r0) |
|248| tcp-wrappers | (7.6-r10) |
|249| tiff | (4.3.0-r0) |
|250| trace-cmd | (2.9.1-r0) |
|251| tremor | (20180319-r0) |
|252| trower-base64 | (1.0-r0) |
|253| tzdata | (2022c-r1) |
|254| udev-extraconf | (1.1-r1) |
|255| unzip | (6.0-r5) |
|256| update-rc.d | (0.8-r0) |
|257| util-linux | (2.37.4-r0) |
|258| util-linux-libuuid | (2.37.4-r0) |
|259| util-macros | (1.19.3-r0) |
|260| vala | (0.56.3-r0) |
|261| vmtouch | (1.3.1-r0) |
|262| wayland | (1.20.0-r0) |
|263| wayland-protocols | (1.25-r1) |
|264| websocketpp | (0.8.2-r0) |
|265| wireless-regdb | (2022.08.12-r0) |
|266| wireless-tools | (30.pre9-r0) |
|267| woff2 | (1.0.2-r0) |
|268| wpa-supplicant | (2.10-r6) |
|269| xkeyboard-config | (2.35.1-r0) |
|270| xmlsec1 | (1.2.33-r0) |
|271| xz | (5.2.6-r0) |
|272| yajl | (2.1.0-r0) |
|273| zlib | (1.2.11-r0) |
|274| zstd | (1.5.2-r0) |

### Diff report of the meta layers contributing to this release of OSS layer project is available at below links

- [ ] meta-rdk-oss-reference [4.3.0-->4.4.0] 
- [ ] meta-rdk-auxiliary [4.1.2-->4.1.4] 

