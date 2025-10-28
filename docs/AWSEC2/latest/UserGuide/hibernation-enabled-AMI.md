# Configure a Linux AMI to support

hibernation

The following Linux AMIs can support hibernating an Amazon EC2 instance, provided you complete
the additional configuration steps described in this section.

###### Additional configuration required for:

- [AL2023 minimal AMI released
  2023.09.20 or later](#configure-AL2023-minimal-for-hibernation "#configure-AL2023-minimal-for-hibernation")
- [Amazon Linux 2 minimal AMI released
  2019.08.29 or later](#configure-AL2-minimal-for-hibernation "#configure-AL2-minimal-for-hibernation")
- [Amazon Linux 2 released before
  2019.08.29](#configure-AL2-for-hibernation "#configure-AL2-for-hibernation")
- [Amazon Linux released before
  2018.11.16](#configure-AL-for-hibernation "#configure-AL-for-hibernation")
- [CentOS version 8 or later](#configure-centos-for-hibernation "#configure-centos-for-hibernation")
- [Fedora version 34 or
  later](#configure-fedora-for-hibernation "#configure-fedora-for-hibernation")
- [Red Hat Enterprise Linux version 8
  or 9](#configure-RHEL-for-hibernation "#configure-RHEL-for-hibernation")
- [Ubuntu 20.04 LTS (Focal
  Fossa) released before serial number 20210820](#configure-ubuntu2004-for-hibernation "#configure-ubuntu2004-for-hibernation")
- [Ubuntu 18.04 (Bionic Beaver)
  released before serial number 20190722.1](#configure-ubuntu1804-for-hibernation "#configure-ubuntu1804-for-hibernation")
- [Ubuntu 16.04 (Xenial
  Xerus)](#configure-ubuntu1604-for-hibernation "#configure-ubuntu1604-for-hibernation")
  For the Linux and Windows AMIs that support hibernation and for which _no additional_ configuration is required, see [AMIs](hibernating-prerequisites.md#hibernation-prereqs-supported-amis "hibernating-prerequisites.md#hibernation-prereqs-supported-amis").

For more information, see [Update instance software on your Amazon Linux 2
instance](../../../linux/al2/ug/install-updates.md "../../../linux/al2/ug/install-updates.md").

## AL2023 minimal AMI released

2023.09.20 or later

###### To configure an AL2023 minimal AMI released 2023.09.20 or later to support

hibernation

1. Install the `ec2-hibinit-agent` package from the repositories.

```
`[ec2-user ~]$` sudo dnf install ec2-hibinit-agent
```

2. Restart the service.

```
`[ec2-user ~]$` sudo systemctl start hibinit-agent
```

## Amazon Linux 2 minimal AMI released

2019.08.29 or later

###### To configure an Amazon Linux 2 minimal AMI released 2019.08.29 or later to support

hibernation

1. Install the `ec2-hibinit-agent` package from the
   repositories.

```
`[ec2-user ~]$` sudo yum install ec2-hibinit-agent
```

2. Restart the service.

```
`[ec2-user ~]$` sudo systemctl start hibinit-agent
```

## Amazon Linux 2 released before

2019.08.29

###### To configure an Amazon Linux 2 AMI released before 2019.08.29 to support

hibernation

1. Update the kernel to `4.14.138-114.102` or later.

```
`[ec2-user ~]$` sudo yum update kernel
```

2. Install the `ec2-hibinit-agent` package from the
   repositories.

```
`[ec2-user ~]$` sudo yum install ec2-hibinit-agent
```

3. Reboot the instance.

```
`[ec2-user ~]$` sudo reboot
```

4. Confirm that the kernel version is updated to
   `4.14.138-114.102` or later.

```
`[ec2-user ~]$` uname -a
```

5. Stop the instance and create an AMI. For more information, see [Create an Amazon EBS-backed AMI](creating-an-ami-ebs.md "creating-an-ami-ebs.md").

## Amazon Linux released before

2018.11.16

###### To configure an Amazon Linux AMI released before 2018.11.16 to support

hibernation

1. Update the kernel to `4.14.77-70.59` or later.

```
`[ec2-user ~]$` sudo yum update kernel
```

2. Install the `ec2-hibinit-agent` package from the
   repositories.

```
`[ec2-user ~]$` sudo yum install ec2-hibinit-agent
```

3. Reboot the instance.

```
`[ec2-user ~]$` sudo reboot
```

4. Confirm that the kernel version is updated to `4.14.77-70.59`
   or greater.

```
`[ec2-user ~]$` uname -a
```

5. Stop the instance and create an AMI. For more information, see [Create an Amazon EBS-backed AMI](creating-an-ami-ebs.md "creating-an-ami-ebs.md").

## CentOS version 8 or later

###### To configure a CentOS version 8 or later AMI to support hibernation

1. Update the kernel to `4.18.0-305.7.1.el8_4.x86_64` or
   later.

```
`[ec2-user ~]$` sudo yum update kernel
```

2. Install the Fedora Extra Packages for Enterprise Linux (EPEL)
   repository.

```
`[ec2-user ~]$` sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
```

3. Install the `ec2-hibinit-agent` package from the
   repositories.

```
`[ec2-user ~]$` sudo yum install ec2-hibinit-agent
```

4. Enable the hibernate agent to start on boot.

```
`[ec2-user ~]$` sudo systemctl enable hibinit-agent.service
```

5. Reboot the instance.

```
`[ec2-user ~]$` sudo reboot
```

6. Confirm that the kernel version is updated to
   `4.18.0-305.7.1.el8_4.x86_64` or later.

```
`[ec2-user ~]$` uname -a
```

## Fedora version 34 or

later

###### To configure a Fedora version 34 or later AMI to support hibernation

1. Update the kernel to `5.12.10-300.fc34.x86_64` or later.

```
`[ec2-user ~]$` sudo yum update kernel
```

2. Install the `ec2-hibinit-agent` package from the
   repositories.

```
`[ec2-user ~]$` sudo dnf install ec2-hibinit-agent
```

3. Enable the hibernate agent to start on boot.

```
`[ec2-user ~]$` sudo systemctl enable hibinit-agent.service
```

4. Reboot the instance.

```
`[ec2-user ~]$` sudo reboot
```

5. Confirm that the kernel version is updated to
   `5.12.10-300.fc34.x86_64` or later.

```
`[ec2-user ~]$` uname -a
```

## Red Hat Enterprise Linux version 8

or 9

###### To configure a Red Hat Enterprise Linux 8 or 9 AMI to support

hibernation

1. Update the kernel to `4.18.0-305.7.1.el8_4.x86_64` or
   later.

```
`[ec2-user ~]$` sudo yum update kernel
```

2. Install the Fedora Extra Packages for Enterprise Linux (EPEL)
   repository.

RHEL version 8:

```
`[ec2-user ~]$` sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
```

RHEL version 9:

```
`[ec2-user ~]$` sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
```

3. Install the `ec2-hibinit-agent` package from the
   repositories.

```
`[ec2-user ~]$` sudo yum install ec2-hibinit-agent
```

4. Enable the hibernate agent to start on boot.

```
`[ec2-user ~]$` sudo systemctl enable hibinit-agent.service
```

5. Reboot the instance.

```
`[ec2-user ~]$` sudo reboot
```

6. Confirm that the kernel version is updated to
   `4.18.0-305.7.1.el8_4.x86_64` or later.

```
`[ec2-user ~]$` uname -a
```

## Ubuntu 20.04 LTS (Focal

Fossa) released before serial number 20210820

###### To configure an Ubuntu 20.04 LTS (Focal Fossa) AMI released before serial

number 20210820 to support hibernation

1. Update the linux-aws-kernel to `5.8.0-1038.40` or later, and
   grub2 to `2.04-1ubuntu26.13` or later.

```
`[ec2-user ~]$` sudo apt update
`[ec2-user ~]$` sudo apt dist-upgrade
```

2. Reboot the instance.

```
`[ec2-user ~]$` sudo reboot
```

3. Confirm that the kernel version is updated to `5.8.0-1038.40`
   or later.

```
`[ec2-user ~]$` uname -a
```

4. Confirm that the grub2 version is updated to
   `2.04-1ubuntu26.13` or later.

```
`[ec2-user ~]$` dpkg --list | grep grub2-common
```

## Ubuntu 18.04 (Bionic Beaver)

released before serial number 20190722.1

###### To configure an Ubuntu 18.04 LTS AMI released before serial number 20190722.1

to support hibernation

1. Update the kernel to `4.15.0-1044` or later.

```
`[ec2-user ~]$` sudo apt update
`[ec2-user ~]$` sudo apt dist-upgrade
```

2. Install the `ec2-hibinit-agent` package from the
   repositories.

```
`[ec2-user ~]$` sudo apt install ec2-hibinit-agent
```

3. Reboot the instance.

```
`[ec2-user ~]$` sudo reboot
```

4. Confirm that the kernel version is updated to `4.15.0-1044` or
   later.

```
`[ec2-user ~]$` uname -a
```

## Ubuntu 16.04 (Xenial

Xerus)

To configure Ubuntu 16.04 LTS to support hibernation, you need to install the
linux-aws-hwe kernel package version 4.15.0-1058-aws or later and the
ec2-hibinit-agent.

###### Important

The `linux-aws-hwe` kernel package is supported by Canonical. The
standard support for Ubuntu 16.04 LTS ended in April 2021, and the package no
longer receives regular updates. However, it will receive additional security
updates until the Extended Security Maintenance support ends in 2024. For more
information, see [Amazon EC2 Hibernation for Ubuntu 16.04 LTS now available](https://ubuntu.com/blog/amazon-ec2-hibernation-for-ubuntu-16-04-lts-now-available "https://ubuntu.com/blog/amazon-ec2-hibernation-for-ubuntu-16-04-lts-now-available") on the
Canonical Ubuntu Blog.

We recommend that you upgrade to the Ubuntu 20.04 LTS (Focal Fossa) AMI or the
Ubuntu 18.04 LTS (Bionic Beaver) AMI.

###### To configure an Ubuntu 16.04 LTS AMI to support hibernation

1. Update the kernel to `4.15.0-1058-aws` or later.

```
`[ec2-user ~]$` sudo apt update
`[ec2-user ~]$` sudo apt install linux-aws-hwe
```

2. Install the `ec2-hibinit-agent` package from the
   repositories.

```
`[ec2-user ~]$` sudo apt install ec2-hibinit-agent
```

3. Reboot the instance.

```
`[ec2-user ~]$` sudo reboot
```

4. Confirm that the kernel version is updated to `4.15.0-1058-aws`
   or later.

```
`[ec2-user ~]$` uname -a
```
