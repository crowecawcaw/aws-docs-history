

# Requirements for resources that you import with VM Import/Export
<a name="prerequisites"></a>

Before you begin, you must be aware of the operating systems and image formats that VM Import/Export supports, and understand the limitations on importing instances and volumes.

**Topics**
+ [Image formats supported by VM Import/Export](#vmimport-image-formats)
+ [Operating systems supported by VM Import/Export](#vmimport-operating-systems)
+ [Boot modes supported by VM Import/Export](#vmimport-boot-modes)
+ [Volume types and file systems supported by VM Import/Export](#vmimport-volume-types)

## Image formats supported by VM Import/Export
<a name="vmimport-image-formats"></a>

VM Import/Export supports the following image formats for importing both disks and VMs:
+ Open Virtual Appliance (OVA) image format, which supports importing images with multiple hard disks.
+ Stream-optimized ESX Virtual Machine Disk (VMDK) image format, which is compatible with VMware ESX and VMware vSphere virtualization products.
+ Fixed and Dynamic Virtual Hard Disk (VHD/VHDX) image formats, which are compatible with Microsoft Hyper-V, Microsoft Azure, and Citrix Xen virtualization products.
+ Raw format for importing disks and VMs.

**Important**  
VMs that are created as the result of a physical-to-virtual (P2V) conversion are not supported. For more information, see [Limitations for resources being imported with VM Import/Export](limitations-image-importing.md).

## Operating systems supported by VM Import/Export
<a name="vmimport-operating-systems"></a>

The following operating systems (OS) can be imported to and exported from Amazon EC2. VMs using `ARM64` architecture are not currently supported.

**Important**  
Starting from April 1, 2026, VM Import Export will stop supporting i386 architecture. Import and Export tasks will stop working for i386 OS versions. These OS versions include Windows Server 2003 (32-bit), Windows Server 2003 R2 (32-bit), Windows Server 2008 (32-bit), Windows 7 (32-bit), Windows 8 (32-bit), CentOS 5 (32-bit), CentOS 6 (32-bit), Debian 6 (32-bit), Debian 7 (32-bit), Debian 10 (32-bit), Debian 11 (32-bit), Debian 12 (32-bit), Fedora 18 (32-bit), Fedora 19 (32-bit), Fedora 20 (32-bit), Oracle Linux 5 (32-bit), Oracle Linux 6 (32-bit), SUSE Linux Enterprise Server 11 (32-bit), Red Hat Enterprise Linux 5 (32-bit), Red Hat Enterprise Linux 6 (32-bit), Ubuntu 12.04 (32-bit), Ubuntu 12.10 (32-bit), Ubuntu 13.04 (32-bit), Ubuntu 13.10 (32-bit), Ubuntu 14.04 (32-bit), Ubuntu 14.10 (32-bit), Ubuntu 15.04 (32-bit), Ubuntu 16.04 (32-bit), Ubuntu 16.10 (32-bit), and Ubuntu 17.04 (32-bit). 

**Important**  
We strongly recommend that you avoid using OS versions that have reached End-of-Life (EOL). OS vendors typically don't provide security patches or other updates for versions that have reached EOL. Continuing to use an EOL system greatly increases the risk of not being able to apply upgrades, including security fixes, and other operational problems. VM Import Export functionalities are not tested on OS versions that have reached EOL. EOL OS versions include Windows Server 2003 (all versions), Windows Server 2003 R2 (all versions), Windows Server 2008 (all versions), Windows Server 2008 R2 (all versions), Windows Server 1709 (all versions), Windows Server 1803 (all versions), Windows 7 (all versions), Windows 8 (all versions), Windows 8.1 (all versions), CentOS 5 (all versions), CentOS 6 (all versions), CentOS 7 (all versions), CentOS 8 (all versions), Debian 6 (all versions), Debian 7 (all versions), Debian 10 (all versions), Fedora 18 (all versions), Fedora 19 (all versions), Fedora 20 (all versions), Fedora 37 (all versions), Fedora 38 (all versions), Fedora 39 (all versions), Fedora 40 (all versions), Oracle Linux 5 (all versions), Oracle Linux 6 (all versions), Red Hat Enterprise Linux 5 (all versions), Red Hat Enterprise Linux 6 (all versions), SUSE Linux Enterprise Server 11 (all versions), SUSE Linux Enterprise Server 12 (all versions), Ubuntu 12.04 (all versions), Ubuntu 12.10 (all versions), Ubuntu 13.04 (all versions), Ubuntu 13.10 (all versions), Ubuntu 14.04 (all versions), Ubuntu 14.10 (all versions), Ubuntu 15.04 (all versions), Ubuntu 16.04 (all versions), Ubuntu 16.10 (all versions), and Ubuntu 17.04 (all versions). 

### Linux/Unix
<a name="vmimport-operating-systems-linux"></a>

The following Linux/Unix operating systems are support by VM Import/Export.<a name="linux-operating-systems"></a>



- **Amazon Linux 2023**
  - **Version:** -
  - **Kernel:** 6.1
  - **Service pack:** -

- **Amazon Linux 2**
  - **Version:** -
  - **Kernel:** 4.14, 4.19, 5.4, 5.10
  - **Service pack:** -

- **CentOS**
  - **Version:** 5.1–5.11 / **Kernel:** 2.6.18 / **Service pack:** -
  - **Version:** 6.1–6.8 / **Kernel:** 2.6.32 / **Service pack:** -
  - **Version:** 7.0–7.9 / **Kernel:** 3.10.0 / **Service pack:** -
  - **Version:** 8.0–8.2 / **Kernel:** 4.18.0 / **Service pack:** -
  - **Version:** 9 / **Kernel:** 5.14.0 / **Service pack:** -

- **Debian**
  - **Version:** 6.0.0–6.0.8 / **Kernel:** 2.6.32 / **Service pack:** -
  - **Version:** 7.0.0–7.8.0 / **Kernel:** 3.2.0 / **Service pack:** -
  - **Version:** 10 / **Kernel:** 4.19.0 / **Service pack:** -
  - **Version:** 11 / **Kernel:** 5.10.0 / **Service pack:** -
  - **Version:** 12.2 / **Kernel:** 6.1.0 / **Service pack:** -
  - **Version:** 12.4 / **Kernel:** 6.1.0 / **Service pack:** -
  - **Version:** 12.7 / **Kernel:** 6.1.0 / **Service pack:** -

- **Fedora**
  - **Version:** 18 / **Kernel:** 3.2.5 / **Service pack:** -
  - **Version:** 19 / **Kernel:** 3.9.5 / **Service pack:** -
  - **Version:** 20 / **Kernel:** 3.11.10 / **Service pack:** -
  - **Version:** 37 / **Kernel:** 6.0.7 / **Service pack:** -
  - **Version:** 38 / **Kernel:** 6.2.9 / **Service pack:** -
  - **Version:** 39 / **Kernel:** 6.5.6 / **Service pack:** -
  - **Version:** 40 / **Kernel:** 6.8.5 / **Service pack:** -
  - **Version:** 41 / **Kernel:** 6.11.4 / **Service pack:** -
  - **Version:** 42 / **Kernel:** 6.14.0 / **Service pack:** -
  - **Version:** 43 / **Kernel:** 6.17.1 / **Service pack:** -

- ** Oracle Linux **
  - **Version:** 5.10–5.11  / **Kernel:** Unbreakable Enterprise Kernel (UEK) el5uek kernel suffixes  / **Service pack:** -
  - **Version:** 6.1–6.10 / **Kernel:** Red Hat Compatible Kernel (RHCK) 2.6.32, 2.6.39<br />Unbreakable Enterprise Kernel (UEK) 3.8.13, 4.1.12 / **Service pack:** -
  - **Version:** 7.0–7.6 / **Kernel:** Red Hat Compatible Kernel (RHCK) 3.10.0<br />Unbreakable Enterprise Kernel (UEK) 3.8.13, 4.1.12, 4.14.35, 5.4.17 / **Service pack:** -
  - **Version:** 8.0–8.9 / **Kernel:** Red Hat Compatible Kernel (RHCK) 4.18.0<br />Unbreakable Enterprise Kernel (UEK) 5.15.0 (el8uek) / **Service pack:** -
  - **Version:** 9.0–9.5 / **Kernel:** Red Hat Compatible Kernel (RHCK) 5.14.0, 5.15.0<br />Unbreakable Enterprise Kernel (UEK) 5.15.0 (el9uek) / **Service pack:** -
  - **Version:** 9.6–9.7 / **Kernel:** Red Hat Compatible Kernel (RHCK) 5.14.0<br />Unbreakable Enterprise Kernel (UEK) 6.12.0 (el9uek) / **Service pack:** -
  - **Version:** 10.0–10.1 / **Kernel:** Red Hat Compatible Kernel (RHCK) 6.12.0<br />Unbreakable Enterprise Kernel (UEK) 6.12.0 (el10uek) / **Service pack:** -

- ** Red Hat Enterprise Linux (RHEL) **
  - **Version:** 5 / **Kernel:** 2.6.18 / **Service pack:** -
  - **Version:** 6 / **Kernel:** 2.6.32 (except 2.6.32-71) / **Service pack:** -
  - **Version:** 7 / **Kernel:** 3.10.0 / **Service pack:** -
  - **Version:** 8.0–8.9 / **Kernel:** 4.18.0 / **Service pack:** -
  - **Version:** 9.0–9.7 / **Kernel:** 5.14.0 / **Service pack:** -
  - **Version:** 10.0–10.1 / **Kernel:** 6.12.0 / **Service pack:** -

- ** Rocky Linux **
  - **Version:** 9.0–9.7 / **Kernel:** 5.14.0 / **Service pack:** -
  - **Version:** 10.0–10.1 / **Kernel:** 6.12.0 / **Service pack:** -

- ** SUSE Linux Enterprise Server (SLES) **
  - **Version:** 11 / **Kernel:** 2.6.32.12 / **Service pack:** 1
  - **Kernel:** 3.0.13 / **Service pack:** 2
  - **Kernel:** 3.0.76, 3.0.101 / **Service pack:** 3
  - **Kernel:** 3.0.101 / **Service pack:** 4
  - **Version:** 12 / **Kernel:** 3.12.28 / **Service pack:** None
  - **Kernel:** 3.12.49 / **Service pack:** 1
  - **Kernel:** 4.4 / **Service pack:** 2, 3
  - **Kernel:** 4.12 / **Service pack:** 4, 5
  - **Version:** 15 / **Kernel:** 4.12 / **Service pack:** None, 1
  - **Kernel:** 5.3 / **Service pack:** 2, 3
  - **Kernel:** 5.14.21 / **Service pack:** 4, 5
  - **Kernel:** 6.4 / **Service pack:** 6

- ** Ubuntu **
  - **Version:** 12.04 / **Kernel:** 3.2.0 / **Service pack:** -
  - **Version:** 12.10 / **Kernel:** 3.5.0 / **Service pack:** -
  - **Version:** 13.04 / **Kernel:** 3.8.0 / **Service pack:** -
  - **Version:** 13.10 / **Kernel:** 3.11 / **Service pack:** -
  - **Version:** 14.04 / **Kernel:** 3.13.0, 3.16.0, 3.19.0 / **Service pack:** -
  - **Version:** 14.10 / **Kernel:** 3.16 / **Service pack:** -
  - **Version:** 15.04 / **Kernel:** 3.19.0 / **Service pack:** -
  - **Version:** 16.04 / **Kernel:** 4.2.0, 4.4.0, 4.8.0, 4.10.0, 4.15.0 / **Service pack:** -
  - **Version:** 16.10 / **Kernel:** 4.8.0 / **Service pack:** -
  - **Version:** 17.04 / **Kernel:** 4.10.0 / **Service pack:** -
  - **Version:** 18.04 / **Kernel:** 4.15.0, 5.4.0 / **Service pack:** -
  - **Version:** 20.04 / **Kernel:** 5.4.0 / **Service pack:** -
  - **Version:** 22.04 / **Kernel:** 5.15.0 / **Service pack:** -
  - **Version:** 23.04 / **Kernel:** 5.15.0 / **Service pack:** -
  - **Version:** 24.04 / **Kernel:** 6.8.0, 6.11.0 / **Service pack:** -
  - **Version:** 25.10 / **Kernel:** 6.17.0 / **Service pack:** -
  - **Version:** 26.04 / **Kernel:** 7.0.0 / **Service pack:** -



### Windows
<a name="vmimport-operating-systems-windows"></a>

The following Windows operating systems are supported by VM Import/Export.<a name="windows-operating-systems"></a>


| Operating system | Edition | Bit version | Available with non-default Regions | 
| --- | --- | --- | --- | 
| Windows Server 2003 (Service Pack 1 or later) | Standard, Datacenter, Enterprise | 32, 64 | No | 
| Windows Server 2003 R2 | Standard, Datacenter, Enterprise | 32, 64 | No | 
| Windows Server 2008 | Standard, Datacenter, Enterprise | 32, 64 | No | 
| Windows Server 2008 R2 | Standard, Web Server, Datacenter, Enterprise | 64 | Yes 5 | 
| Windows Server 2012 | Standard, Datacenter | 64 | Yes 5 | 
| Windows Server 2012 R2 | Standard, Datacenter | 64 | Yes 5 | 
| Windows Server 2016 | Standard, Datacenter 3 | 64 | Yes 5 | 
| Windows Server 1709 | Standard, Datacenter | 64 | Yes 5 | 
| Windows Server 1803 | Standard, Datacenter | 64 | Yes 5 | 
| Windows Server 2019 | Standard, Datacenter | 64 | Yes 5 | 
| Windows Server 2022 | Standard, Datacenter | 64 | Yes 5,6 | 
| Windows Server 2025 | Standard, Datacenter | 64 | Yes 5,6 | 
| Windows 7 1 | Home, Professional, Enterprise, Ultimate | 32, 64 4 | Yes 5 | 
| Windows 8 1 | Home, Professional, Enterprise | 32, 64 4 | Yes 5 | 
| Windows 8.1 1 | Professional, Enterprise | 64 | Yes 5 | 
| Windows 10 1 | Home, Professional, Enterprise, Education | 64 | Yes 5 | 
| Windows 11 1,2 | Home, Professional, Enterprise, Education | 64 | Yes 5,7 | 

1 The operating system must have its language set as `US English` during import.

2 Windows 11 requires the Unified Extensible Firmware Interface (UEFI) boot mode to function. To help ensure a successful import of your VM, we recommend that you specify the optional `--boot-mode` parameter as `uefi`. For more information, see [Boot modes supported by VM Import/Export](#vmimport-boot-modes).

3 Nano Server installations are not supported.

4 Only the 64-bit version of the OS is supported when launching instances within non-default AWS Regions. For more information, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in the *Amazon EC2 User Guide*.

5 You must first enable the Region before you can use the operating system there. For more information, see [Enable or disable AWS Regions in your account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) in the *AWS Account Management Reference Guide*.

6 Windows Server 2022 and Windows Server 2025 are not supported in the China (Beijing) and China (Ningxia) Regions.

7 Windows 11 isn't supported in the Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Melbourne), China (Beijing), China (Ningxia), Europe (Spain), Europe (Zurich), and Middle East (UAE) Regions.

## Boot modes supported by VM Import/Export
<a name="vmimport-boot-modes"></a>

When a computer boots, the first software that it runs is responsible for initializing the platform and providing an interface for the operating system to perform platform-specific operations. VM Import/Export supports two variants of the boot mode: Unified Extensible Firmware Interface (UEFI) and Legacy BIOS. You can choose whether to specify the optional `--boot-mode` parameter as `legacy-bios` or `uefi` when importing your VM.

Refer to the [Boot Modes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html) section of the *Amazon Elastic Compute Cloud User Guide* for more information about specifying a boot mode, and UEFI variables.

## Volume types and file systems supported by VM Import/Export
<a name="vmimport-volume-types"></a>

VM Import/Export supports importing Windows and Linux VMs with the following file systems.

### Linux/Unix
<a name="vmimport-volume-types-linux"></a>

MBR partitioned volumes and GUID Partition Table (GPT) partitioned volumes that are formatted using the ext2, ext3, ext4, Btrfs, JFS, or XFS file system are supported.

**Important**  
Btrfs subvolumes are not supported.

### Windows
<a name="vmimport-volume-types-windows"></a>

GUID Partition Table (GPT) and Master Boot Record (MBR) partitioned volumes that are formatted using the NTFS file system are supported. If no boot parameter is specified, and the VM is compatible in both boot modes, the GPT volumes will be converted to MBR partitioned volumes.

VM Import/Export will automatically detect the boot modes your Windows VM is compatible with. If the Windows VM is only compatible in a single boot mode, you don't need to specify a specific `--boot-mode` parameter.

If your Windows VM is compatible with both boot modes, and the following criteria is met for the imported disk, VM Import/Export will select Legacy BIOS by default. You can specify `uefi` for the `--boot-mode` parameter to override this behavior.
+ The disk is smaller than 2 terabytes
+ The disk does not contain more than 4 primary partitions
+ The disk is not a Windows dynamic disk
+ The file format is VHDX