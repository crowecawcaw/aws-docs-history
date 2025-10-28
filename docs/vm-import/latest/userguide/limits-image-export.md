# Considerations for image export

Exporting images and volumes is subject to the following limitations:

- You must export to one of the following image formats that your virtualization
  environment supports:
  - Virtual Hard Disk (VHD), which is compatible with Citrix Xen
    and Microsoft Hyper-V virtualization products.
  - Stream-optimized ESX Virtual Machine Disk (VMDK), which is compatible
    with VMware ESX and VMware vSphere versions 4, 5, and 6.
  - Raw format.

- The base AMI used to launch an instance must exist when you attempt to export
  the instance. If you have deleted the AMI, the export fails.
- VM Import/Export only supports exporting VMs to an S3 bucket in the same AWS account
  that you export them from.
- Export operations do not support hybrid configurations. GRUB2 must be enabled
  for either BIOS or UEFI, but it can't be enabled for both.
- You can't export an image if it contains third-party software provided by
  AWS. For example, VM Export cannot export Windows or SQL Server images, or any
  image created from an image in the AWS Marketplace.
- You can't export an image with encrypted EBS snapshots in the block device
  mapping.
- You can only export EBS data volumes that are specified in the block
  device mapping, not EBS volumes attached after instance launch.
- You can't export an image from Amazon EC2 if you've shared it from another AWS
  account.
- You can't have multiple export image tasks in progress for the same AMI
  at the same time.
- By default, you can't have more than 5 conversion tasks per Region in progress
  at the same time. This limit is adjustable up to 20.
- VMs with volumes larger than 1 TiB are not supported.
- You can export a volume to either an unencrypted S3 bucket or to a bucket
  encrypted using SSE-S3 encryption. You cannot export to an S3 bucket encrypted
  using SSE-KMS encryption.
