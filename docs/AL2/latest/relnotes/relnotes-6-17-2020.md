# Amazon Linux 2 06/17/2020 release notes

These are release notes for Amazon Linux 2.

## Major updates

- Python 2.7 updated to most recent upstream version - 2.7.18.

###### Note

Amazon Linux will continue to provide security fixes to Python 2.7 according to our Amazon Linux 2 support timeline. See [Amazon Linux 2 FAQs](https://aws.amazon.com/amazon-linux-2/faqs/ "https://aws.amazon.com/amazon-linux-2/faqs/").

- ca-certificates fix for Sectigo intermediate CA expiration

###### Note

For more information, see [this forum
thread](https://forums.aws.amazon.com/thread.jspa?threadID=322837&tstart=0 "https://forums.aws.amazon.com/thread.jspa?threadID=322837&tstart=0").

- New Kernel with fixes for five CVEs (see below).

## Package updates

Amazon Linux 2 includes the following packages.

| Packages                             |
| ------------------------------------ |
| amazon-linux-extras-1.6.11-1         |
| bind-export-libs-9.11.4-9            |
| ca-certificates-2019.2.32-76         |
| cloud-init-19.3-3,freetype-2.8-14    |
| gdisk-0.8.10-3,glib2-2.56.1-5        |
| kernel-4.14.181-140.257              |
| libicu-50.2-4                        |
| libpng-1.5.13-7                      |
| python-2.7.18-1                      |
| python-devel-2.7.18-1                |
| python-libs-2.7.18-1                 |
| python2-rpm-4.11.3-40                |
| rpm-4.11.3-40                        |
| rpm-build-libs-4.11.3-40             |
| rpm-libs-4.11.3-40                   |
| rpm-plugin-systemd-inhibit-4.11.3-40 |
| selinux-policy-3.13.1-192            |
| selinux-policy-targeted-3.13.1-192   |
| yum-3.4.3-1                          |

## Kernel updates

Rebase kernel to upstream stable 4.14.181.

Updated ENA module to version 2.2.8.

CVEs fixed:

- CVE-2019-19319 [ext4: Protects journal inode's blocks using block\_validity]
- CVE-2020-10751 [selinux: Properly handles multiple messages in selinux\_netlink\_send()]
- CVE-2020-1749 [net: ipv6\_stub: Uses ip6\_dst\_lookup\_flow instead of ip6\_dst\_lookup]
- CVE-2019-19768 [blktrace: Protects q->blk\_trace with RCU]
- CVE-2020-12770 [scsi: sg: Adds sg\_remove\_request in sg\_write]

Other Fixes:

- Fix for a deadlock condition in xen-blkfront [xen-blkfront: Delay flush till queue lock dropped]
- Fix for ORC unwinding [x86/unwind/orc: Fix unwind\_get\_return\_address\_ptr() for inactive tasks]
