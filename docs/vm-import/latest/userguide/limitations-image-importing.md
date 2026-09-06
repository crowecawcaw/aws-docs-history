

# Limitations for resources being imported with VM Import/Export
<a name="limitations-image-importing"></a>

Review the following limitations that apply when you import a VM into Amazon EC2.

**Topics**
+ [General limitations for your resources](#limitations-image-importing-general)
+ [Limitations for Linux/Unix resources](#limitations-image-importing-linux)
+ [Limitations for Windows resources](#limitations-image-importing-windows)

## General limitations for your resources
<a name="limitations-image-importing-general"></a>

The following limitations apply to any operating system that you can import.
+ VMs that are created as the result of a physical-to-virtual (P2V) conversion are not supported. A P2V conversion occurs when a disk image is created by performing a Linux or Windows installation process on a physical machine and then importing a copy of that Linux or Windows installation to a VM.
+ Importing VMs with dual-boot configurations isn't supported.
+ Importing VMs with encrypted volumes isn't supported.
+ VM Import/Export doesn't support VMs that use Raw Device Mapping (RDM). Only VMDK disk images are supported.
+ VM Import/Export doesn't support VMware SEsparse delta-file format.
+ If you import a VM that's compatible with UEFI using the `import-image` command while specifying an EBS snapshot, you must specify a value for the `platform` parameter. For more information, see [import-snapshot](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportImage.html) in the Amazon EC2 API Reference.
+ An imported VM may fail to boot if the root partition is not on the same virtual hard drive as the MBR.
+ A VM import task fails for VMs with more than 21 volumes attached. Additional disks can be individually imported using the `ImportSnapshot` API.
+ VM Import/Export assigns only private IPv4 addresses to your instances, regardless of the auto-assign public IP setting for the subnet. To use a public IPv4 address, you can allocate an Elastic IP address to your account and associate it with your instance. You can also add IPv6 addresses. For more information, see [IP addressing for your VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html) in the *Amazon Virtual Private Cloud User Guide.* 
+ Multiple network interfaces are not currently supported. After import, your VM has a single virtual network interface that uses DHCP to assign addresses.
+ Disk images must be less than 16 TiB. For disk images that are larger than 8 TiB, you must use a [manifest file](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/manifest.html).
  + You can use the `ImportInstance` operation to import VMs with disks up to the maximum supported size.
  + You can use the `ImportImage` operation to import VMs with disks less than 8 TiB in size.

## Limitations for Linux/Unix resources
<a name="limitations-image-importing-linux"></a>

The following limitations apply to Linux operating systems that you can import.
+ Imported Linux VMs must use 64-bit images. Migrating 32-bit Linux images isn't supported.
+ Imported Linux VMs should use default kernels for best results. VMs that use custom Linux kernels might not migrate successfully.
+ When preparing Linux VMs for import, make sure that there is sufficient disk space available on the root volume for installing drivers and other software.
+ To help ensure your Linux VM can import successfully and run on Amazon EC2 using the [AWS Nitro System](https://aws.amazon.com/ec2/nitro/), you can install the AWS NVMe and AWS Elastic Network Adapter (ENA) drivers before exporting your VM from its virtualization environment. For more information, see [Amazon EBS and NVMe on Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nvme-ebs-volumes.html) and [Enable enhanced networking with the Elastic Network Adapter (ENA) on Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html) in the *Amazon EC2 User Guide*.
+ If you import a Linux VM compatible with UEFI, you must have a fallback EFI binary, BOOTX64.EFI, located on the EFI System Partition.
  + Debian VMs that are missing a fallback EFI binary will have one automatically created from your GRUBX64.EFI, if it exists in your EFI System Partition.
+ Predictable network interface names are not supported for virtual machine imports.

## Limitations for Windows resources
<a name="limitations-image-importing-windows"></a>

The following limitations apply to Windows operating systems that you can import.
+ When preparing Windows VMs for import, make sure that there is sufficient disk space available on the root volume for installing drivers and other software. For Microsoft Windows VMs, configure a fixed page file size and ensure that there is at least 6 GiB of free space available on the root volume. If Windows is configured to use the "Automatically manage paging file size for all drives" setting, it might create 16 GB `pagefile.sys` files on the C drive of the instance.
+ If you import a Windows VM compatible with UEFI, we convert GPT boot volumes to MBR if the following are true: the image format is VHDX, the uncompressed size is 2 TiB or smaller, there are no more than three primary partitions, and the volume is not a dynamic disk.
+ If you import a Windows Server 2012 R2 VM, VM Import/Export installs the single root I/O virtualization (SR-IOV) drivers. These drivers are not required unless you plan to use enhanced networking, which provides higher performance (packets per second), lower latency, and lower jitter.
+ VM Import/Export does not support Emergency Management Services (EMS). If EMS is enabled for a source Windows VM, we disable it in the imported image.
+ Windows language packs that use UTF-16 (or non-ASCII) characters are not supported for import. We recommend using the English language pack when importing Windows VMs.
+ Windows Server VMs with the Hyper-V server role installed are not supported.