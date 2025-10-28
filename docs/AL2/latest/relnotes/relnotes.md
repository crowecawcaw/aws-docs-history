# Amazon Linux 2 release notes

These are release notes for Amazon Linux 2.

## Systemd

Amazon Linux 2 provides the systemd service and systems manager as replacements to System V init. As a result, applications running on Amazon Linux 1 might
require changes to run on Amazon Linux 2. Amazon Elastic Compute Cloud console (Amazon EC2) instances running Amazon Linux can no longer be upgraded to Amazon Linux 2 through rolling
upgrade mechanisms.

Amazon Linux 2 uses the systemd 219 init system to bootstrap userspace and manage system
processes. This is available as /sbin/init and replaces the System V-style init system that
was available in the previous generation of Amazon Linux. Do not put initscripts sin /etc/init.d.
systemctl {start|stop|restart}. Instead, use SERVICE_NAME.service. Service SERVICE_NAME
{start|stop|restart} is compatible with both Amazon Linux 1 and Amazon Linux 2.

## Extras

The extras mechanism provides the latest application software on a stable base of Amazon Linux 2. You can use it to balance operating system
stability and overall software “freshness”. Extras provides topics to select AWS curated software bundles. Each topic contains all the
dependencies required for the software to install and run on Amazon Linux 2.

The following is the Extras command to list the available topics.

```
`$` `amazon-linux-extras`
```

The following is the Extras command to install a topic.

```
`$` `sudo amazon-linux-extras install `topic name``
```

In the following example, the Extras command installs the rust1 topic.

```
`$` `sudo amazon-linux-extras install rust1`
```

The extras channel provides an AWS curated list of rapidly evolving technologies. These technologies might be updated more frequently
than they would otherwise be in the "core" repositories of Amazon Linux 2.

Over time, these technologies will continue to mature and stabilize and might eventually be added to the Amazon Linux 2 "core" channel to which the
Amazon Linux 2 Long Term Support policies apply.

## Docker is only in extras

The package for Docker is only available through extras. It is enabled by default. When new versions of Docker are released, support is
provided only for the most current stable packages.

## C Runtime, compiler, and tools

Amazon Linux 2 comes with GCC 7.3, Glibc 2.26, and Binutils 2.29.1.

## System directories moved into /usr

In Amazon Linux 2, /bin, /sbin, /lib, and /lib64 are symlinks to /usr/bin, /usr/sbin, /usr/lib, and /usr/lib64, respectively. Packages that have
Requires on specific binaries in /bin can't resolve. You can mitigate this by using the following logic for RPM package management.

```
%if 0%{?amzn} == 1
Requires: /bin/grep
%else
Requires: /usr/bin/grep
%endif
```

## cloud-init updates

Cloud-init has been updated to version 18.2 to handle early initialization of the operating system. Cloud-init sets the default locale and
instance hostname, and it generates SSH private keys and adds SSH keys into the user’s .ssh/authorized_keys entry. It also establishes
ephemeral mount points and configures the network devices.

## Virtual Machine images for on-premises use

Amazon Linux 2 virtual machine images are currently available for VMware ESXi, Microsoft Hyper-V, KVM, and Oracle VM VirtualBox virtualization
solutions for development and testing. After downloading the image, follow the Amazon Linux documentation to get started.

The minimum system requirement for running Amazon Linux 2 in a virtual machine instance is 512 MB of memory and one virtual CPUs.

## Automation of security patching at scale with AWS Systems Manager Patch Manager

[AWS Systems Manager Patch Manager](../../../systems-manager/latest/userguide/systems-manager-patch.md "../../../systems-manager/latest/userguide/systems-manager-patch.md")
now supports Amazon Linux 2. This enables the automated patching of fleets of Amazon Linux 2 EC2 instances and on-premises virtual machines (VMs). [AWS Systems Manager Patch Manager](../../../systems-manager/latest/userguide/systems-manager-patch.md "../../../systems-manager/latest/userguide/systems-manager-patch.md") can scan
instances for missing patches and automatically install all missing patches.

## Upgrading from Amazon Linux 2 LTS Candidate 2

To upgrade from Amazon Linux 2 LTS Candidate 2 to the LTS version of Amazon Linux 2, run the following commands.

```
`$` `sudo yum update system-release`

`$` `sudo yum update cloud-init`

`$` `sudo yum clean all`

`$` `sudo yum update`

`$` `sudo reboot`
```
