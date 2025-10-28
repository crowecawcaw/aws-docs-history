# Troubleshooting VM Import/Export

When you import or export a virtual machine (VM), most errors occur because of an attempt
to do something that isn't supported. To avoid these errors, be sure to check the
requirements and limitations carefully.

An import task might stop before it completes, and then fail. You can gather details about
the import task that appears to have stopped due to a failure before it changes to the
`completed` status. To gather such details, use the appropriate command for
the import operation you used to describe details of the conversion task that's in
progress:

- **ImportInstance** and **ImportVolume** – Use the [DescribeConversionTasks](../../../AWSEC2/latest/APIReference/API_DescribeConversionTasks.md "../../../AWSEC2/latest/APIReference/API_DescribeConversionTasks.md") operation.
- **ImportImage** – Use the
  [DescribeImportImageTasks](../../../AWSEC2/latest/APIReference/API_DescribeImportImageTasks.md "../../../AWSEC2/latest/APIReference/API_DescribeImportImageTasks.md") operation.
- **ImportSnapshot** – Use the
  [DescribeImportSnapshotTasks](../../../AWSEC2/latest/APIReference/API_DescribeImportSnapshotTasks.md "../../../AWSEC2/latest/APIReference/API_DescribeImportSnapshotTasks.md") operation.

###### Errors

- [Import image errors](#import-image-errors "#import-image-errors")
- [Import instance errors](#import-instance-errors "#import-instance-errors")
- [VM export errors](#instance-export-errors "#instance-export-errors")
- [Windows VM errors](#windows-vm-errors "#windows-vm-errors")
- [Linux VM errors](#linux-vm-errors "#linux-vm-errors")

## Import image errors

**Error Code: InvalidParameter, Error Message: Message: Parameter
disk-image-size=0 has an invalid format**

The specified image format is not supported. Retry the operation using one
of the following supported image formats: VHD, VHDX, VMDK, or raw.

**A client error (MalformedPolicyDocument) occurred when calling the CreateRole
operation: Syntax errors in policy**

You must include the `file://` prefix before the policy
document name.

**ClientError: Disk validation failed [OVF file parsing error: OVA with chunked
disk files is not supported]**

VM Import/Export does not support importing disks separated into multiple files.
Check the disk format and retry the operation with the VM disk as a single
file.

**ClientError: Disk validation failed [Unsupported VMDK File Format]**

The VMDK file must be stream-optimized. For more information, see [Image formats supported by VM Import/Export](prerequisites.md#vmimport-image-formats "prerequisites.md#vmimport-image-formats").

**ClientError: Multiple different grub/menu.lst files found**

VM Import/Export found duplicate files during the import task for at least one of
the following: `grub.cfg`,
`grub.conf`, or `menu.lst`. VMs with
dual-boot configurations are not supported. For more information, see [Limitations for resources being imported
with VM Import/Export](limitations-image-importing.md "limitations-image-importing.md").

**The service role `vmimport` does not exist or does not have
sufficient permissions for the service to continue**

The VM import service role is missing or incorrect. You may also receive
this error if the user, group, or role trying to start the import does not
have sufficient access privileges on Amazon EC2 resources.

This error can also occur if the user calling `ImportImage` has
`Decrypt` permission but the `vmimport` role does
not. If you use [Server-Side
Encryption with AWS KMS–Managed Keys (SSE-KMS)](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md") to secure your
at-rest data in Amazon S3, you need to assign additional `Decrypt`
permission to your service role as shown in the following JSON code:

```
{
   "Sid":"Allow vmimport to decrypt SSE-KMS key",
   "Effect":"Allow",
   "Principal":{
      "AWS":[
         "arn:aws:iam::accountid:role/vmimport"
      ]
   },
   "Action":[
      "kms:Decrypt"
   ],
   "Resource":"*"
}
```

## Import instance errors

**Error Code: InvalidParameter, Error Message: Message: Parameter
disk-image-size=0 has an invalid format**

The specified image format is not supported. Retry the operation using one
of the following supported image formats: OVA, VHD, VMDK, or raw.

**Client.Unsupported: No bootable partition found. (Service: AmazonEC2; Status
Code: 400; Error Code: Unsupported; Request ID: <RequestID>)**

The root volume is GUID Partition Table (GPT) partitioned. GPT partitioned
volumes are not supported. Convert the root volume to an MBR partition and
try again.

**ClientError: Footers not identical**

You attempted to import a differencing VHD, or there was an error in
creating the VHD. Export your VM again and retry importing it into
Amazon EC2.

**ClientError: Uncompressed data has an invalid length**

The VMDK file is corrupted. You can try repairing or recreating the VMDK
file, or use a different file.

**ERROR: Bucket <MyBucketName> is not in the <RegionName> Region,
it's in <RegionName>**

The Amazon Simple Storage Service (Amazon S3) bucket is not in the same AWS Region as the instance you want
to import. Try adding the `--ignore-region-affinity` option,
which ignores whether the bucket's Region matches the Region where the
import task is created. You can also create an S3 bucket using the
Amazon Simple Storage Service console and set the Region to the Region where you want to import
the VM. Run the command again and specify the new bucket you just
created.

**ERROR: File uses unsupported compression algorithm 0**

The VMDK was created using OVA format instead of OVF format. Create the
VMDK in OVF format.

**Invalid S3 source location**

The command syntax or S3 bucket name is incorrect. Create an S3 bucket
in the appropriate Region solely for VM Import and upload the VM files to
the root of the bucket.

**The given S3 bucket is not local to the Region**

The S3 bucket used for VM Import must reside in the same AWS Region
where you want to import the VM.

**ClientError: Unknown OS / Missing OS files**

The operating system is not recognized. Verify that your OS is listed as
support in the VM Import/Export [Requirements for resources that you import with
VM Import/Export](prerequisites.md "prerequisites.md").

## VM export errors

**Client.UnsupportedOperation: This instance has multiple volumes attached.
Please remove additional volumes.**

Detach volumes other than the root volume and try again. If you need the
data from the volumes, you can copy it to the root volume or import the
volumes to Amazon EBS.

**Client.NotExportable: This instance cannot be exported. (Service: AmazonEC2;
Status Code: 400; Error Code: NotExportable; Request ID:
<RequestID>)**

You can only export certain instances. For more information, see [Considerations for instance export](vmexport-limits.md "vmexport-limits.md").

**Error starting instances: Invalid value <instance ID> for instanceId.
Instance does not have a volume attached at root (/dev/sda1).**

You attempted to start the instance before the VM import process and all
conversion tasks were complete. Wait for the VM import process and all
conversion tasks to completely finish, and then start the instance.

**An error occurred (InvalidParameter) when calling the CreateInstanceExportTask
operation: The given S3 object is not local to the region.**

The EC2 instance and S3 bucket must be in the same AWS Region. You must
also ensure the `create-instance-export-task` command is being
run in the same Region as your resources being exported. You can specify the
Region by using `--region` parameter. For more information, see
[AWS CLI supported global command line options](../../../cli/latest/userguide/cli-configure-options.md#cli-configure-options-list "../../../cli/latest/userguide/cli-configure-options.md#cli-configure-options-list") in the
_AWS Command Line Interface User Guide_.

## Windows VM errors

### ClientError: Booter Networking

failure/instance not reachable. Please retry after installation of .Net
framework 3.5 SP1 or greater.

The EC2 Config Service requires the Microsoft .NET Framework 3.5 Service Pack 1 or
later. Install Microsoft .NET Framework 3.5 Service Pack 1 or later on your Windows
VM and try again.

### FirstBootFailure: This import request failed

because the Windows instance failed to boot and establish network
connectivity.

When you receive the `FirstBootFailure` error message, it means that
your virtual disk image was unable to perform one of the following steps:

- Boot up and start Windows.
- Install Amazon EC2 networking and disk drivers.
- Use a DHCP-configured network interface to retrieve an IP address.
- Activate Windows using the Amazon EC2 Windows volume license.

The following best practices can help you to avoid Windows first boot
failures:

- **Disable anti-virus and anti-spyware software and
  firewalls** — These types of software can prevent
  installing new Windows services or drivers or prevent unknown binaries from
  running. Software and firewalls can be re-enabled after importing.
- **Do not harden your operating system**
  — Security configurations, sometimes called hardening, can prevent
  unattended installation of Amazon EC2 drivers. There are numerous Windows
  configuration settings that can prevent import. These settings can be
  reapplied once imported.
- **Disable or delete multiple bootable
  partitions** — If your virtual machine boots and requires
  you to choose which boot partition to use, the import may fail.

This inability of the virtual disk image to boot up and establish network
connectivity could be due to any of the following causes:

**TCP/IP networking and DHCP are not enabled**

**Cause**: TCP/IP networking and DHCP
must be enabled.

**Resolution**: Ensure that TCP/IP
networking is enabled. For more information, see [Change TCP/IP settings](https://support.microsoft.com/en-us/help/15089/windows-change-tcp-ip-settings "https://support.microsoft.com/en-us/help/15089/windows-change-tcp-ip-settings") at the Microsoft Support website.
Ensure that DHCP is enabled. For more information, see [Dynamic Host Configuration Protocol (DHCP)](https://docs.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top "https://docs.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top") at the Microsoft
website.

**The Hyper-V server role is installed**

**Cause**: Importing a virtual machine
with the Hyper-V role installed is not supported.

**Resolution**: Remove the Hyper-V role
from the virtual machine and try the import again.

**A volume that Windows requires is missing from the virtual machine**

**Cause**: Importing a VM into Amazon EC2 only
imports the boot disk, all other disks must be detached and Windows must
able to boot before importing the virtual machine. For example, Active
Directory often stores the Active Directory database on the
`D:\` drive. A domain controller cannot boot if the
Active Directory database is missing or inaccessible.

**Resolution**: Detach any secondary and
network disks attached to the Windows VM before exporting. Move any
Active Directory databases from secondary drives or partitions onto the
primary Windows partition. For more information, see ["Directory Services cannot start" error message when you start your
Windows-based or SBS-based domain controller](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/0xc00002e1-error-start-domain-controller "https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/0xc00002e1-error-start-domain-controller") at the
Microsoft Support website.

**Windows always boots into System Recovery Options**

**Cause**: Windows can boot into System
Recovery Options for a variety of reasons, including when Windows is
pulled into a virtualized environment from a physical machine, also
known as a physical-to-virtual (P2V) conversion process.

**Resolution**: Ensure that Windows boots to a
login prompt before exporting and preparing for import.
Do not import virtualized Windows instances that have come from a physical
machine.

**The virtual machine was created using a physical-to-virtual (P2V)
conversion process**

**Cause**: A P2V conversion occurs when a
disk image is created by performing the Windows installation process on
a physical machine and then importing a copy of that Windows
installation into a VM. VMs that are created as the result of a P2V
conversion are not supported by VM Import/Export. VM Import/Export only supports Windows
images that were natively installed inside the source VM.

**Resolution**: Install Windows in a
virtualized environment and migrate your installed software to that new
VM.

**Windows activation fails**

**Cause**: During boot, Windows will
detect a change of hardware and attempt activation. During the import
process we attempt to switch the licensing mechanism in Windows to a
volume license provided by Amazon Web Services. However, if the Windows activation
process does not succeed, then the import fails.

**Resolution**: Ensure that the version
of Windows that you are importing supports volume licensing. Beta or
preview versions of Windows might not.

**No bootable partition found**

**Cause**: During the import process of a
virtual machine, we could not find the boot partition.

**Resolution**: Ensure that the disk you
are importing has a boot partition.

## Linux VM errors

**ClientError: Invalid configuration - Could not read fstab**

Linux VMs with dual-boot volumes or multiple `/etc`
directories are not supported.

**ClientError: BLSC-style GRUB found, but unable to detect default kernel**

VM Import/Export can’t detect the default kernel. This can occur when it has been
moved out of the main `grub.cfg` file. You can set the
configuration to `$saved_entry` and ensure the
`grubenv` contains the `bootloader` entry as the
default.

**ClientError: We were unable to read your import's initramfs/initrd to
determine what drivers your import requires to run in EC2**

We were unable to read required files while importing your Linux VM to
prepare it to run as an instance in Amazon EC2. You can run the
`lsinitramfs` command to verify the integrity of the file.
For example, you might use the following command:

```
lsinitramfs /boot/initrd.img-5.4.0-77-generic 2>&1 | less
```

If errors are returned in the output, you can try rebuilding the
`initramfs` file to resolve the issue and import the
VM again.

**ClientError: Unsupported configuration - Logical volume group activation
failed**

A logical volume on your virtual disk image failed to activate. This may
indicate file or disk corruption. Verify the uploaded disk image files.

**ClientError: Unsupported configuration - Multiple directories found**

Linux VMs with multi-boot volumes or multiple `/etc`
directories are not supported.

**ClientError: Unsupported kernel version**

The kernel version used by the operating system is not supported. Confirm
that your import meets the requirements listed for the operating system. For
more information, see [Operating systems supported by
VM Import/Export](prerequisites.md#vmimport-operating-systems "prerequisites.md#vmimport-operating-systems").

**Linux is not supported on the requested instance**

Linux VMs can be imported to specific instance types. Try again using one
of the following supported instance types.

- General purpose: `t2.micro` | `t2.small` | `t2.medium` | `m3.medium` | `m3.large` | `m3.xlarge` | `m3.2xlarge`
- Compute optimized: `c3.large` | `c3.xlarge` | `c3.2xlarge` | `c3.4xlarge` | `c3.8xlarge` | `cc1.4xlarge` | `cc2.8xlarge`
- Memory optimized: `r3.large` | `r3.xlarge` | `r3.2xlarge` | `r3.4xlarge` | `r3.8xlarge` | `cr1.8xlarge`
- Storage optimized: `i2.xlarge` | `i2.2xlarge` | `i2.4xlarge` | `i2.8xlarge` | `hi1.4xlarge` | `hi1.8xlarge`
