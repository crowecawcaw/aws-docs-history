# Requirements for resources that you import with

VM Import/Export

Before you begin, you must be aware of the operating systems and image formats that
VM Import/Export supports, and understand the limitations on importing instances and
volumes.

###### Topics

- [Image formats supported by VM Import/Export](#vmimport-image-formats "#vmimport-image-formats")
- [Operating systems supported by
  VM Import/Export](#vmimport-operating-systems "#vmimport-operating-systems")
- [Boot modes supported by VM Import/Export](#vmimport-boot-modes "#vmimport-boot-modes")
- [Volume types and file systems supported by
  VM Import/Export](#vmimport-volume-types "#vmimport-volume-types")

## Image formats supported by VM Import/Export

VM Import/Export supports the following image formats for importing both disks and
VMs:

- Open Virtual Appliance (OVA) image format, which supports importing images
  with multiple hard disks.
- Stream-optimized ESX Virtual Machine Disk (VMDK) image format, which is
  compatible with VMware ESX and VMware vSphere virtualization
  products.
- Fixed and Dynamic Virtual Hard Disk (VHD/VHDX) image formats, which are
  compatible with Microsoft Hyper-V, Microsoft Azure, and Citrix Xen
  virtualization products.
- Raw format for importing disks and VMs.

###### Important

VMs that are created as the result of a physical-to-virtual (P2V) conversion
are not supported. For more information, see [Limitations for resources being imported
with VM Import/Export](limitations-image-importing.md "limitations-image-importing.md").

## Operating systems supported by

VM Import/Export

The following operating systems (OS) can be imported to and exported from Amazon EC2.
VMs using `ARM64` architecture are not currently supported.

###### Important

We strongly recommend that you avoid using OS versions that have reached End-of-Life (EOL).
OS vendors typically don't provide security patches or other updates for versions that have reached EOL.
Continuing to use an EOL system greatly increases the risk of not being able to apply upgrades, including security fixes, and other operational problems.
VM Import Export functionalities are not tested on OS versions that have reached EOL.

###### Important

Starting from February 1, 2026, VM Import Export will begin deprecating support for i386 architecture and End-of-Life OS versions.
This deprecation will start with Windows Server 2003 (all versions), Windows Server 2003 R2 (all versions), Windows Server 2008 (all versions),
Windows 7 (all versions), Windows 8 (all versions), Windows 8.1 (all versions),
CentOS 5 (all versions), CentOS 6 (all versions), CentOS 7 (all versions), CentOS 8 (all versions),
Debian 6 (all versions), Debian 7 (all versions), Debian 10 (all versions),
Fedora 18 (all versions), Fedora 19 (all versions), Fedora 20 (all versions), Fedora 37 (all versions), Fedora 38 (all versions), Fedora 39 (all versions),
Oracle Linux 5 (all versions), Oracle Linux 6 (all versions),
Red Hat Enterprise Linux 5 (all versions), Red Hat Enterprise Linux 6 (all versions), SUSE Linux Enterprise Server 11 (all versions),
Ubuntu 12.04 (all versions), Ubuntu 12.10(all versions), Ubuntu 13.04 (all versions), Ubuntu 13.10 (all versions), Ubuntu 14.04 (all versions), Ubuntu 14.10 (all versions), and Ubuntu 15.04 (all versions).

The following Linux/Unix operating systems are support by VM Import/Export.

| Operating system                    | Version                                                                                                           | Kernel                                                     | Service pack |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ------------ |
| Amazon Linux 2023                   | -                                                                                                                 | 6.1                                                        | -            |
| Amazon Linux 2                      | -                                                                                                                 | 4.14, 4.19, 5.4, 5.10                                      | -            |
| CentOS                              | 5.1–5.11                                                                                                          | 2.6.18                                                     | -            |
| 6.1–6.8                             | 2.6.32                                                                                                            | -                                                          |
| 7.0–7.9                             | 3.10.0                                                                                                            | -                                                          |
| 8.0–8.2                             | 4.18.0                                                                                                            | -                                                          |
| 9                                   | 5.14.0                                                                                                            | -                                                          |
| Debian                              | 6.0.0–6.0.8                                                                                                       | 2.6.32                                                     | -            |
| 7.0.0–7.8.0                         | 3.2.0                                                                                                             | -                                                          |
| 10                                  | 4.19.0                                                                                                            | -                                                          |
| 11                                  | 5.10.0                                                                                                            | -                                                          |
| 12.2                                | 6.1.0                                                                                                             | -                                                          |
| 12.4                                | 6.1.0                                                                                                             | -                                                          |
| Fedora                              | 18                                                                                                                | 3.2.5                                                      | -            |
| 19                                  | 3.9.5                                                                                                             | -                                                          |
| 20                                  | 3.11.10                                                                                                           | -                                                          |
| 37                                  | 6.0.7                                                                                                             | -                                                          |
| 38                                  | 6.2.9                                                                                                             | -                                                          |
| 39                                  | 6.5.6                                                                                                             | -                                                          |
| Oracle Linux                        | 5.10–5.11                                                                                                         | Unbreakable Enterprise Kernel (UEK) el5uek kernel suffixes | -            |
| 6.1–6.10                            | Red Hat Compatible Kernel (RHCK) 2.6.32, 2.6.39<br>Unbreakable Enterprise Kernel (UEK)<br>3.8.13, 4.1.12          | -                                                          |
| 7.0–7.6                             | Red Hat Compatible Kernel (RHCK) 3.10.0<br>Unbreakable Enterprise Kernel (UEK)<br>3.8.13, 4.1.12, 4.14.35, 5.4.17 | -                                                          |
| 8.0–8.9                             | Red Hat Compatible Kernel (RHCK) 4.18.0<br>Unbreakable Enterprise Kernel (UEK)<br>5.15.0 (el8uek)                 | -                                                          |
| 9.0–9.5                             | Red Hat Compatible Kernel (RHCK) 5.14.0, 5.15.0<br>Unbreakable Enterprise Kernel (UEK)<br>5.15.0 (el9uek)         | -                                                          |
| 9.6                                 | Red Hat Compatible Kernel (RHCK)<br>6.12.0<br>Unbreakable Enterprise Kernel (UEK)<br>6.12.0 (el9uek)              | -                                                          |
| Red Hat Enterprise Linux (RHEL)     | 5                                                                                                                 | 2.6.18                                                     | -            |
| 6                                   | 2.6.32 (except 2.6.32-71)                                                                                         | -                                                          |
| 7                                   | 3.10.0                                                                                                            | -                                                          |
| 8.0–8.9                             | 4.18.0                                                                                                            | -                                                          |
| 9.0–9.6                             | 5.14.0                                                                                                            | -                                                          |
| Rocky Linux                         | 9.0–9.6                                                                                                           | 5.14.0                                                     | -            |
| SUSE Linux Enterprise Server (SLES) | 11                                                                                                                | 2.6.32.12                                                  | 1            |
| 3.0.13                              | 2                                                                                                                 |
| 3.0.76, 3.0.101                     | 3                                                                                                                 |
| 3.0.101                             | 4                                                                                                                 |
| 12                                  | 3.12.28                                                                                                           | None                                                       |
| 3.12.49                             | 1                                                                                                                 |
| 4.4                                 | 2, 3                                                                                                              |
| 4.12                                | 4, 5                                                                                                              |
| 15                                  | 4.12                                                                                                              | None, 1                                                    |
| 5.3                                 | 2, 3                                                                                                              |
| 5.14.21                             | 4, 5                                                                                                              |
| 6.4                                 | 6                                                                                                                 |
| Ubuntu                              | 12.04                                                                                                             | 3.2.0                                                      | -            |
| 12.10                               | 3.5.0                                                                                                             | -                                                          |
| 13.04                               | 3.8.0                                                                                                             | -                                                          |
| 13.10                               | 3.11                                                                                                              | -                                                          |
| 14.04                               | 3.13.0, 3.16.0, 3.19.0                                                                                            | -                                                          |
| 14.10                               | 3.16                                                                                                              | -                                                          |
| 15.04                               | 3.19.0                                                                                                            | -                                                          |
| 16.04                               | 4.2.0, 4.4.0, 4.8.0, 4.10.0, 4.15.0                                                                               | -                                                          |
| 16.10                               | 4.8.0                                                                                                             | -                                                          |
| 17.04                               | 4.10.0                                                                                                            | -                                                          |
| 18.04                               | 4.15.0, 5.4.0                                                                                                     | -                                                          |
| 20.04                               | 5.4.0                                                                                                             | -                                                          |
| 22.04                               | 5.15.0                                                                                                            | -                                                          |
| 23.04                               | 5.15.0                                                                                                            | -                                                          |
|                                     | 24.04                                                                                                             | 6.8.0, 6.11.0                                              | -            |

The following Windows operating systems are supported by VM Import/Export.

| Operating system                                 | Edition                                         | Bit version | Available with non-default Regions |
| ------------------------------------------------ | ----------------------------------------------- | ----------- | ---------------------------------- |
| Windows Server 2003 (Service Pack 1 or<br>later) | Standard, Datacenter, Enterprise                | 32, 64      | No                                 |
| Windows Server 2003 R2                           | Standard, Datacenter, Enterprise                | 32, 64      | No                                 |
| Windows Server 2008                              | Standard, Datacenter, Enterprise                | 32, 64      | No                                 |
| Windows Server 2008 R2                           | Standard, Web Server, Datacenter,<br>Enterprise | 64          | Yes 5                              |
| Windows Server 2012                              | Standard, Datacenter                            | 64          | Yes 5                              |
| Windows Server 2012 R2                           | Standard, Datacenter                            | 64          | Yes 5                              |
| Windows Server 2016                              | Standard, Datacenter<br>3                       | 64          | Yes 5                              |
| Windows Server 1709                              | Standard, Datacenter                            | 64          | Yes 5                              |
| Windows Server 1803                              | Standard, Datacenter                            | 64          | Yes 5                              |
| Windows Server 2019                              | Standard, Datacenter                            | 64          | Yes 5                              |
| Windows Server 2022                              | Standard, Datacenter                            | 64          | Yes<br>5,6                         |
| Windows Server 2025                              | Standard, Datacenter                            | 64          | Yes<br>5,6                         |
| Windows<br>7 1                                   | Home, Professional, Enterprise,<br>Ultimate     | 32, 64 4    | Yes 5                              |
| Windows<br>8 1                                   | Home, Professional, Enterprise                  | 32, 64 4    | Yes 5                              |
| Windows<br>8.1 1                                 | Professional, Enterprise                        | 64          | Yes 5                              |
| Windows<br>10 1                                  | Home, Professional, Enterprise,<br>Education    | 64          | Yes 5                              |
| Windows<br>11 1,2                                | Home, Professional, Enterprise,<br>Education    | 64          | Yes<br>5,7                         |

1 The operating system must have its language
set as `US English` during import.

2 Windows 11 requires the Unified Extensible
Firmware Interface (UEFI) boot mode to function. To help ensure a successful
import of your VM, we recommend that you specify the optional
`--boot-mode` parameter as `uefi`. For more
information, see [Boot modes supported by VM Import/Export](#vmimport-boot-modes "#vmimport-boot-modes").

3 Nano Server installations are not
supported.

4 Only the 64-bit version of the OS is
supported when launching instances within non-default AWS Regions. For
more information, see [Available Regions](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-available-regions "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-available-regions") in the _Amazon EC2 User Guide_.

5 You must first enable the Region before you
can use the operating system there. For more information, see [Enable or
disable AWS Regions in your account](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md") in the
_AWS Account Management Reference Guide_.

6 Windows Server 2022 and Windows Server 2025
are not supported in the China (Beijing) and China (Ningxia)
Regions.

7 Windows 11 isn't supported in the
Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Melbourne),
China (Beijing), China (Ningxia), Europe (Spain),
Europe (Zurich), and Middle East (UAE) Regions.

## Boot modes supported by VM Import/Export

When a computer boots, the first software that it runs is responsible for
initializing the platform and providing an interface for the operating system to
perform platform-specific operations. VM Import/Export supports two variants of the boot mode:
Unified Extensible Firmware Interface (UEFI) and Legacy BIOS. You can choose whether
to specify the optional `--boot-mode` parameter as
`legacy-bios` or `uefi` when importing your VM.

Refer to the [Boot Modes](../../../AWSEC2/latest/UserGuide/ami-boot.md "../../../AWSEC2/latest/UserGuide/ami-boot.md") section of the
_Amazon Elastic Compute Cloud User Guide_ for more information
about specifying a boot mode, and UEFI variables.

## Volume types and file systems supported by

VM Import/Export

VM Import/Export supports importing Windows and Linux VMs with the following file
systems.

MBR partitioned volumes and GUID Partition Table (GPT) partitioned volumes
that are formatted using the ext2, ext3, ext4, Btrfs, JFS, or XFS file
system are supported.

###### Important

Btrfs subvolumes are not supported.

GUID Partition Table (GPT) and Master Boot Record (MBR) partitioned
volumes that are formatted using the NTFS file system are supported. If no
boot parameter is specified, and the VM is compatible in both boot modes,
the GPT volumes will be converted to MBR partitioned volumes.

VM Import/Export will automatically detect the boot modes your Windows VM is
compatible with. If the Windows VM is only compatible in a single boot mode,
you don't need to specify a specific `--boot-mode`
parameter.

If your Windows VM is compatible with both boot modes, and the following
criteria is met for the imported disk, VM Import/Export will select Legacy BIOS by
default. You can specify `uefi` for the `--boot-mode`
parameter to override this behavior.

- The disk is smaller than 2 terabytes
- The disk does not contain more than 4 primary partitions
- The disk is not a Windows dynamic disk
- The file format is VHDX
