# Using Network File System to mount EFS file

systems

Following, learn how to install the Network File System (NFS) client and how to
mount your Amazon EFS file system on an Amazon EC2 instance. You also can find an explanation of the
`mount` command and the available options for specifying your file system's
Domain Name System (DNS) name in the `mount` command. In addition, you can find how
to use the file `fstab` to automatically remount your file system after any
system restarts.

###### Note

In this section, you can learn how to mount your Amazon EFS file system without the
amazon-efs-utils package. To use encryption of data in transit with your file system, you
must mount your file system with Transport Layer Security (TLS). To do so, we recommend
using the amazon-efs-utils package. For more information, see [Installing the Amazon EFS client](using-amazon-efs-utils.md "using-amazon-efs-utils.md").

###### Topics

- [Prerequisites](#reqs-mount-nfs "#reqs-mount-nfs")
- [NFS support](#mounting-fs-nfs-info "#mounting-fs-nfs-info")
- [Installing the NFS client](mounting-fs-install-nfsclient.md "mounting-fs-install-nfsclient.md")
- [Recommended NFS mount settings](mounting-fs-nfs-mount-settings.md "mounting-fs-nfs-mount-settings.md")
- [Mounting on Amazon EC2 with a DNS name](mounting-fs-mount-cmd-dns-name.md "mounting-fs-mount-cmd-dns-name.md")
- [Mounting with an IP address](mounting-fs-mount-cmd-ip-addr.md "mounting-fs-mount-cmd-ip-addr.md")

## Prerequisites

Before you can mount a file system, make sure you meet the following
requirements:

- Create, configure, and launch your related
  AWS resources. For instructions, see [Getting started with Amazon EFS](getting-started.md "getting-started.md").
- Create VPC security groups for your Amazon EC2
  instances and mount targets with the required inbound and outbound access. For more information,
  see [Using VPC security groups](network-access.md "network-access.md").

## NFS support

Amazon EFS supports the Network File System versions 4.0 and 4.1 (NFSv4) protocols when
mounting your file systems on Amazon EC2 instances. Although NFSv4.0 is supported, we recommend
that you use NFSv4.1. Mounting your Amazon EFS file system on your Amazon EC2 instance also requires
an NFS client that supports your chosen NFSv4 protocol. Amazon EC2 Mac instances running macOS Big Sur only support NFS v4.0.

Amazon EFS does not support the `nconnect` mount option.

###### Note

For Linux kernel versions 5.4.\*, the Linux NFS client uses a default
`read_ahead_kb` value of 128 KB. We recommend increasing this value to 15 MB.
For more information, see [Optimizing the NFS read_ahead_kb size](performance-tips.md#efs-perf-optimize-nfs-read-ahead "performance-tips.md#efs-perf-optimize-nfs-read-ahead").

For optimal performance and to avoid a variety of known NFS client bugs, we recommend
working with a recent Linux kernel. If you are using an enterprise Linux distribution, we
recommend the following:

- Amazon Linux 2
- Amazon Linux 2017.09 or newer
- Red Hat Enterprise Linux (and derivatives such as CentOS) version 8 and newer
- Ubuntu 16.04 LTS and newer
- SLES 12 Sp2 or later

If you are using another distribution or a custom kernel, we recommend kernel version
4.3 or newer. To troubleshoot issues related to certain AMI or kernel versions when using
Amazon EFS from an EC2 instance, see [Troubleshooting AMI and kernel issues](troubleshooting-efs-ami-kernel.md "troubleshooting-efs-ami-kernel.md").

###### Note

Mounting EFS file systems with Amazon EC2 instances running Microsoft Windows is
not supported.
