# Considerations for instance export

Exporting instances and volumes is subject to the following limitations:

- You must export your instances and volumes to one of the following image
  formats that your virtualization environment supports:
  - Open Virtual Appliance (OVA), which is compatible with VMware vSphere
    versions 4, 5, and 6.
  - Virtual Hard Disk (VHD), which is compatible with Citrix Xen and
    Microsoft Hyper-V virtualization products.
  - Stream-optimized ESX Virtual Machine Disk (VMDK), which is compatible
    with VMware ESX and VMware vSphere versions 4, 5, and 6.

- You can't export an instance if it contains third-party software provided by
  AWS. For example, VM Export cannot export Windows or SQL Server instances, or
  any instance created from an image in the AWS Marketplace.
- You can't export an instance with encrypted EBS snapshots in the block device
  mapping.
- You can't export an instance with instance store volumes in the block device
  mapping.
- You can only export EBS volumes that are specified in the block device
  mapping, not EBS volumes attached after instance launch.
- You can't export an instance launched from an imported image if you deleted
  the AMI or the EBS snapshot for the AMI. To work around the issue, create an AMI
  from the instance and export the AMI.
- You can't export an instance that has more than one virtual disk.
- You can't export an instance that has more than one network interface.
- You can't export an instance from Amazon EC2 if you've shared it from another AWS
  account.
- By default, you can't have more than 5 conversion tasks per Region in progress
  at the same time. This limit is adjustable up to 20.
- VMs with volumes larger than 1 TiB are not supported.
- You can export a volume to either an unencrypted S3 bucket or to a bucket
  encrypted using SSE-S3. You cannot export to an S3 bucket encrypted using
  SSE-KMS.
- VM Import/Export only supports exporting VMs to an S3 bucket in the same AWS account
  that you export them from.
- Export operations do not support hybrid configurations. GRUB2 must be enabled
  for either BIOS or UEFI, but it can't be enabled for both.
