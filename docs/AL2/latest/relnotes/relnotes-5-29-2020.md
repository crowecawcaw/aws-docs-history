# Amazon Linux 2 05/29/2020 release notes

These are release notes for Amazon Linux 2.

## Major updates

- Kernel includes fix for Important ALAS: https://alas.aws.amazon.com/AL2/ALAS-2020-1425.html
- Amazon Linux 2 Customers are encouraged to try out Kernel Live Patching Public Preview, which would apply CVE fixes without a reboot. See
  https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/al2-live-patching.html

## Package updates

Amazon Linux 2 includes the following packages.

| Packages                                       |
| ---------------------------------------------- |
| aws-cfn-bootstrap-1.4-32.amzn2.0.1             |
| awscli-1.16.300-1.amzn2.0.2                    |
| bind-export-libs-9.11.4-9.P2.amzn2.0.3         |
| bind-libs-9.11.4-9.P2.amzn2.0.3                |
| bind-libs-lite-9.11.4-9.P2.amzn2.0.3.          |
| bind-license-9.11.4-9.P2.amzn2.0.3             |
| bind-utils-9.11.4-9.P2.amzn2.0.3               |
| freeglut-3.0.0-8.amzn2                         |
| freetype-2.8-14.amzn2                          |
| gdisk-0.8.10-3.amzn2                           |
| glib2-2.56.1-5.amzn2.0.1                       |
| gnupg2-2.0.22-5.amzn2.0.4                      |
| kernel-4.14.177-139.254.amzn2                  |
| kernel-tools-4.14.177-139.254.amzn2            |
| langtable-0.0.31-4.amzn2                       |
| langtable-data-0.0.31-4                        |
| langtable-python-0.0.31-4                      |
| libX11-1.6.7-2.amzn2                           |
| libX11-common-1.6.7-2.amzn2                    |
| libXfont2-2.0.3-1.amzn2                        |
| libXrandr-1.5.1-2.amzn2.0.3                    |
| libdrm-2.4.97-2.amzn2                          |
| libfastjson-0.99.4-3.amzn2                     |
| libglvnd-1.0.1-0.1.git5baa1e5.amzn2.0.1        |
| libglvnd-egl-1.0.1-0.1.git5baa1e5.amzn2.0.1    |
| libglvnd-gles-1.0.1-0.1.git5baa1e5.amzn2.0.1   |
| libglvnd-glx-1.0.1-0.1.git5baa1e5.amzn2.0.1    |
| libicu-50.2-4.amzn2, libpng-1.5.13-7.amzn2.0.2 |
| libtirpc-0.2.4-0.16.amzn2                      |
| libwayland-client-1.17.0-1.amzn2               |
| libwayland-server-1.17.0-1.amzn2               |
| mesa-libEGL-18.3.4-5.amzn2.0.1                 |
| mesa-libGL-18.3.4-5.amzn2.0.1                  |
| mesa-libgbm-18.3.4-5.amzn2.0.1                 |
| mesa-libglapi-18.3.4-5.amzn2.0.1               |
| microcode_ctl-2.1-47.amzn2.0.6                 |
| openssl-1.0.2k-19.amzn2.0.3                    |
| openssl-libs-1.0.2k-19.amzn2.0.3               |
| python-pillow-2.0.0-20.gitd1c6db8.amzn2.0.1    |
| python2-rpm-4.11.3-40.amzn2.0.4                |
| rpm-4.11.3-40.amzn2.0.4                        |
| rpm-build-libs-4.11.3-40.amzn2.0.4             |
| rpm-libs-4.11.3-40.amzn2.0.4                   |
| rpm-plugin-systemd-inhibit-4.11.3-40.amzn2.0.4 |
| selinux-policy-3.13.1-192.amzn2.6.1            |
| selinux-policy-targeted-3.13.1-192.amzn2.6.1   |
| sudo-1.8.23-4.amzn2.2                          |
| xorg-x11-server-Xorg-1.20.4-7.amzn2.0.2        |
| xorg-x11-server-common-1.20.4-7.amzn2.0.2      |
| yum-3.4.3-158.amzn2.0.4                        |

## Kernel updates

Rebase kernel to upstream stable 4.14.177.

CVEs fixed:

- CVE-2020-10711 [netlabel: cope with NULL catmap]
- CVE-2020-12826 [Extend exec\_id to 64bits]
- CVE-2020-12657 [block, bfq: fix use-after-free in bfq\_idle\_slice\_timer\_body]
- CVE-2020-11565 [mm: mempolicy: require at least one nodeid for MPOL\_PREFERRED]
- CVE-2020-8648 [vt: selection, close sel\_buffer race]
- CVE-2020-1094 [vhost: Check docket sk\_family instead of call getname]
- CVE-2020-8649 [vgacon: Fix a UAF in vgacon\_invert\_region]
- CVE-2020-8647 [vgacon: Fix a UAF in vgacon\_invert\_region]
- CVE-2020-8648 [vt: selection, close sel\_buffer race]

Other Fixes:

- Divide by zero scheduler fix
- Enabled L2TP in the configuration
