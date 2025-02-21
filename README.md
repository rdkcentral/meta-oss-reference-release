# OSS Layer Release Notes
RDKE OSS Layer Release Notes

---

|Summary|Content|
|---|----|
|Classification|Public|
|Document Version|Issue 1|
|Date|15th January 2025|
|Author|RDKE Platform & Tools Team|

| Components | Tag |
|----------|--------|
| packagegroup-oss-layer | 3.7.0-r0|



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

The 3.7.0 OSS release delivers architecture-specific and platform-independent artifacts. Within this release, ARM architecture is accommodated with the following variations:
    1. rdk-arm7a-oss: Default tuning is set to armv7athf-neon.
    2. rdk-arm7ve-oss: Default tuning is set to armv7vethf-neon.
    3. rdk-arm64-oss: 64-bit ARM architecture with a multilib configuration and default tuning set to armv7vethf-neon for compatibility with 32-bit systems.
The IPK feed is automatically chosen based on the platform's default tuning configuration, with armv7vethf-neon being the default feed.

New modules:
1. liberation-fonts

Removed modules:
1. fdk-aac
2. ffmpeg
3. x264 
4. gdb
5. packagegroup-core-tools-debug

Revision upgraded:
1. logrotate 
2. stunnel
3. systemd 

Version downgraded:
1. mdns

## Release layer and components
### OSS stack layer
| Layer | Tag |
|------|------|
|meta-rdk-oss-referenc|3.7.0|

### Components details in "packagegroup-oss-layer"

|#|OSS layer Component|(=version)|
|-|----------------------|---------|
|1| acl | (2.2.53-r0) |
|2| alsa-lib | (1.2.1.2-r0) |
|3| alsa-plugins | (1.2.1-r0) |
|4| alsa-state | (0.2.0-r5) |
|5| alsa-topology-conf | (1.2.1-r0) |
|6| alsa-ucm-conf | (1.2.1.2-r0) |
|7| alsa-utils | (1.2.1-r0) |
|8| alsa-utils-scripts | (1.2.1-r0) |
|9| apparmor | (2.13.10-r0) |
|10| atk | (2.34.1-r0) |
|11| attr | (2.4.48-r0) |
|12| autoconf-archive | (2019.01.06-r0) |
|13| avahi | (0.7-r1) |
|14| base-files | (3.0.14-r89) |
|15| base-passwd | (3.5.29-r0) |
|16| bash | (3.2.57-r0) |
|17| bash-completion | (2.10-r0) |
|18| bind | (9.11.37-r0) |
|19| boost | (1.72.0-r0) |
|20| breakpad | (1.0-r1) |
|21| breakpad-wrapper | (1.0-r0) |
|22| brotli | (1.0.7-r0) |
|23| busybox | (1.31.1-r1) |
|24| bzip2 | (1.0.8-r0) |
|25| ca-certificates | (20211016-r2) |
|26| c-ares | (1.18.1-r0) |
|27| civetweb | (1.10+git+0+0f1b43536d-r0) |
|28| cjson | (1.7.13-r0) |
|29| coreutils | (6.9-r0) |
|30| cracklib | (2.9.5-r0) |
|31| crun | (1.7.2-r0) |
|32| ctemplate | (1.0.0+git0+4b7e6c52dc-r3) |
|33| cunit | (2.1-3-r0) |
|34| curl | (7.69.1-r0) |
|35| db | (5.3.28-r1) |
|36| dbus | (1.12.24-r0) |
|37| dbus-glib | (0.110-r0) |
|38| dibbler | (1.0.1+1.0.2RC1+gitc4b0ed52e751da7823dd9a36e91f93a6310e5525-r1) |
|39| dnsmasq | (2.83-r4) |
|40| dosfstools | (2.11-r0) |
|41| e2fsprogs | (1.45.7-r0) |
|42| ebtables | (2.0.10-4-r4) |
|43| elfutils | (0.178-r0) |
|44| evtest | (1.34-r0) |
|45| expat | (2.2.9-r0) |
|46| fcgi | (2.4.0-r0) |
|47| file | (5.38-r0) |
|48| findutils | (4.2.31-r0) |
|49| flac | (1.3.3-r0) |
|50| flex | (2.6.4-r0) |
|51| fontconfig | (2.13.1-r0) |
|52| freetype | (2.10.2-r0) |
|53| fribidi | (1.0.9-r0) |
|54| gawk | (3.1.5-r2) |
|55| gcc-runtime | (9.5.0-r0) |
|56| gcc-sanitizers | (9.5.0-r0) |
|57| gdbm | (1.8.3-r4) |
|58| gdk-pixbuf | (2.40.0-r0) |
|59| gettext | (0.16.1-r6) |
|60| gflags | (2.2.2-r0) |
|61| glib-2.0 | (2.72.3-r1) |
|62| glibc | (2.31+git0+d4b7559457-r1) |
|63| glibc-locale | (2.31-r0) |
|64| glibc-mtrace | (2.31-r0) |
|65| glib-networking | (2.48.2-r0) |
|66| glib-openssl | (2.50.3-r0) |
|67| gmp | (4.2.1-r0) |
|68| gnutls | (3.3.30-r0) |
|69| gobject-introspection | (1.62.0-r0) |
|70| googletest | (1.10.0-r0) |
|71| graphite2 | (1.3.6-r0) |
|72| grpc | (1.24.3-r0) |
|73| gssdp | (1.2.3-r0) |
|74| gupnp | (0.20.10-r1) |
|75| harfbuzz | (2.6.4-r0) |
|76| heaptrack | (1.5.0-r0) |
|77| hiredis | (0.14.0-r0) |
|78| icu | (66.1-r0) |
|79| initscripts | (1.0-r155) |
|80| iperf3 | (3.7-r0) |
|81| iptables | (1.8.4-r0) |
|82| iso-codes | (4.4-r0) |
|83| iw | (4.7-r0) |
|84| jansson | (2.13.1-r0) |
|85| jquery | (1.0.0-r3) |
|86| json-c | (0.13.1-r0) |
|87| jsoncpp | (1.8.4-r0) |
|88| jsonrpc | (1.3.0-r0) |
|89| kbd | (2.2.0-r0) |
|90| keyutils | (1.6.1-r0) |
|91| kmod | (26-r0) |
|92| lcms | (2.9-r0) |
|93| libaio | (0.3.111-r0) |
|94| libarchive | (3.6.1-r0) |
|95| libatomic-ops | (7.6.10-r0) |
|96| libbsd | (0.10.0-r0) |
|97| libcap | (2.32-r0) |
|98| libcap-ng | (0.7.10-r0) |
|99| libcgroup | (0.41-r0) |
|100| libcheck | (0.14.0-r0) |
|101| libcroco | (0.6.13-r0) |
|102| libdaemon | (0.14-r0) |
|103| libdash | (1.0.0+git0+f5b5d991af-r1) |
|104| libdwarf | (20210528-r0) |
|105| liberation-fonts | (2.00.1-r0) |
|106| libev | (4.33-r0) |
|107| libevdev | (1.8.0-r0) |
|108| libevent | (2.1.11-r0) |
|109| libexif | (0.6.22-r0) |
|110| libffi | (3.3-r0) |
|111| libgcc | (9.5.0-r0) |
|112| libgcrypt | (1.8.5-r0) |
|113| libgpg-error | (1.37-r0) |
|114| libgudev | (233-r0) |
|115| libical | (3.0.7-r0) |
|116| libidn2 | (2.3.0-r0) |
|117| libinput | (1.15.2-r0) |
|118| libjpeg | (62.3.0-r0) |
|119| libmanette | (0.2.6-r0) |
|120| libmicrohttpd | (0.9.70-r0) |
|121| libmng | (2.0.3-r0) |
|122| libndp | (1.7-r0) |
|123| libnewt | (0.52.21-r0) |
|124| libnl | (3.5.0-r0) |
|125| libnsl2 | (1.2.0+git0+4a062cf418-r0) |
|126| libnss-mdns | (0.14.1-r0) |
|127| liboauth | (1.0.3-r0) |
|128| libogg | (1.3.4-r0) |
|129| libol | (0.3.18-r0) |
|130| libomxil | (0.9.3-r0) |
|131| libopus | (1.3.1-r0) |
|132| libpam | (1.3.1-r0) |
|133| libpcap | (1.9.1-r1) |
|134| libpciaccess | (0.16-r0) |
|135| libpcre2 | (10.34-r0) |
|136| libpcre | (8.39-r0) |
|137| libpng | (1.6.37-r0) |
|138| libpsl | (0.21.1-r0) |
|139| libpthread-stubs | (0.4-r0) |
|140| libsamplerate0 | (0.1.9-r1) |
|141| libsdl | (1.2.15-r3) |
|142| libsdl-image | (1.2.12-r0) |
|143| libsdl-ttf | (2.0.11-r0) |
|144| libseccomp | (2.4.3-r0) |
|145| libsndfile1 | (1.0.28-r0) |
|146| libsolv | (0.7.10-r0) |
|147| libsoup-2.4 | (2.68.4-r1) |
|148| libsoup | (3.4.2-r0) |
|149| libstd-rs | (1.58.1-r0) |
|150| libtasn1 | (4.13-r0) |
|151| libtheora | (1.1.1-r1) |
|152| libtinyxml | (2.6.2-r5) |
|153| libtinyxml2 | (8.0.0-r0) |
|154| libtirpc | (1.2.6-r0) |
|155| libtool | (2.4.6-r0) |
|156| libunistring | (0.9.10-r0) |
|157| libunwind | (1.3.1-r0) |
|158| liburcu | (0.11.1-r0) |
|159| libusb1 | (1.0.27-r0) |
|160| libuv | (1.36.0-r0) |
|161| libvorbis | (1.3.6-r0) |
|162| libvpx | (1.12.0-r0) |
|163| libwebp | (0.5.0-r0) |
|164| libwebsockets | (4.0.1-r1) |
|165| libxcrypt | (4.4.15-r0) |
|166| libxkbcommon | (0.5.0-r0) |
|167| libxml2 | (2.9.10-r0) |
|168| libxslt | (1.1.34-r0) |
|169| libzip | (1.6.1-r0) |
|170| lighttpd | (1.4.53-r2) |
|171| linenoise | (1.0.0+git0+97d2850af1-r1) |
|172| linux-libc-headers | (4.9-r1) |
|173| log4c | (1.2.3-r0) |
|174| logrotate | (3.21.0-r1) |
|175| lttng-ust | (2.11.2-r0) |
|176| lua | (5.3.6-r0) |
|177| lvm2 | (2.03.06-r0) |
|178| lz4 | (1.9.2-r0) |
|179| lzo | (2.10-r0) |
|180| m4 | (1.4.9-r2) |
|181| mbedtls | (2.16.3-r0) |
|182| mdns | (1556.80.2-r0) |
|183| minizip | (1.0.0+git0+71ef99f6a0-r0) |
|184| mongoose | (2.6-r0) |
|185| msgpack-c | (3.2.1+git0+8085ab8721-r0) |
|186| mtdev | (1.1.6-r0) |
|187| mtd-utils | (2.1.3-r1) |
|188| nanomsg | (1.1.5-r0) |
|189| ncurses | (6.2-r0) |
|190| ndisc6 | (1.0.4+git0+4c794b5512-r0) |
|191| ne10 | (1.2.1gitr+0+18c4c982a5-r0) |
|192| netbase | (6.1-r0) |
|193| nettle | (2.7.1-r0) |
|194| networkmanager | (1.43.7-r1) |
|195| nghttp2 | (1.48.0-r0) |
|196| nopoll | (0.3.2.b232-r0) |
|197| nspr | (4.25-r0) |
|198| nss | (3.51.1-r0) |
|199| openjpeg | (2.3.1-r0) |
|200| openssh | (8.2p1-r0) |
|201| openssl | (1.1.1l-r0) |
|202| opkg | (0.4.2-r1) |
|203| opkg-arch-config | (1.0-r1) |
|204| opkg-utils | (0.4.2-r0) |
|205| orc | (0.4.31-r0) |
|206| packagegroup-oss-layer | (3.7.0-r0) |
|207| perl | (5.30.1-r1) |
|208| pixman | (0.38.4-r0) |
|209| popt | (1.16-r0) |
|210| procps | (3.3.12-r1) |
|211| protobuf | (3.11.4-r0) |
|212| protobuf-c | (1.3.3-r0) |
|213| pulseaudio | (13.0-r0) |
|214| python | (2.7.18-r0) |
|215| python3 | (3.8.14-r0) |
|216| python3-dbus | (1.2.16-r0) |
|217| qrencode | (4.0.1+git0+7c83deb8f5-r0) |
|218| rapidjson | (1.1.0+git0+0ccdbf364c-r0) |
|219| rdkperf | (git-r0) |
|220| rdm | (1.0.1-r1) |
|221| readline | (5.2-r9) |
|222| redis | (5.0.14-r1) |
|223| run-postinsts | (1.0-r10) |
|224| safec | (3.5.1-r0) |
|225| safec-common-wrapper | (1.0-r0) |
|226| sbc | (1.4-r0) |
|227| sed | (4.1.2-r0) |
|228| shadow | (4.8.1-r0) |
|229| shadow-securetty | (4.6-r3) |
|230| shared-mime-info | (1.10-r0) |
|231| slang | (2.3.2-r0) |
|232| smcroute | (2.4.4-r0) |
|233| speex | (1.2.0-r0) |
|234| speexdsp | (1.2.0-r0) |
|235| sqlite | (2.8.17-r7) |
|236| sqlite3 | (3.31.1-r1) |
|237| strace | (5.5-r0) |
|238| stunnel | (5.57-r2) |
|239| sysfsutils | (2.1.0-r5) |
|240| syslog-ng | (3.24.1-r1) |
|241| systemd | (230+git0+3a74d4fc90-r9) |
|242| systemd-serialgetty | (1.0.0-r5) |
|243| taglib | (1.11.1-r0) |
|244| tcpdump | (4.9.3-r0) |
|245| tcp-wrappers | (7.6-r10) |
|246| tiff | (4.1.0-r0) |
|247| trace-cmd | (2.9.1-r0) |
|248| tremor | (20180319-r0) |
|249| trower-base64 | (1.0-r0) |
|250| tzdata | (2022g-r1) |
|251| udev-extraconf | (1.1-r1) |
|252| unzip | (6.0-r5) |
|253| update-rc.d | (0.8-r0) |
|254| util-linux | (2.35.1-r0) |
|255| util-macros | (1.19.2-r0) |
|256| vala | (0.46.6-r0) |
|257| vmtouch | (1.3.1-r0) |
|258| wayland | (1.18.0-r0) |
|259| wayland-protocols | (1.20-r1) |
|260| websocketpp | (0.8.2-r0) |
|261| wireless-regdb | (2023.02.13-r0) |
|262| wireless-tools | (30.pre9-r0) |
|263| woff2 | (1.0.2-r0) |
|264| wpa-supplicant | (2.10-r6) |
|265| xkeyboard-config | (2.28-r0) |
|266| xmlsec1 | (1.2.30-r0) |
|267| xz | (5.2.4-r0) |
|268| yajl | (2.1.0-r0) |
|269| zlib | (1.2.11-r0) |
|270| zstd | (1.4.5-r0) |

### Diff report of the meta layers contributing to this release of OSS layer project is available at below links
- [ ] meta-rdk-oss-reference [3.6.0-->3.7.0] 
