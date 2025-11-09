# AMI types and characteristics in Amazon EC2

When you launch an instance, the AMI that you choose must be compatible with the instance
type that you choose. You can select an AMI to use based on the following characteristics:

- [Region](using-regions-availability-zones.md "using-regions-availability-zones.md")
- Operating system
- Processor architecture
- [Launch permissions](#launch-permissions "#launch-permissions")
- [Root volume type](#storage-for-the-root-device "#storage-for-the-root-device")
- [Virtualization types](#virtualization_types "#virtualization_types")

## Launch permissions

Launch permissions determine who can use an AMI to launch instances. You can think of
launch permissions as [sharing an AMI](sharing-amis.md "sharing-amis.md")—when
you grant launch permissions, you're sharing the AMI with other users. Only the
owner of an AMI can determine its availability by specifying launch permissions.
Launch permissions fall into the following categories.

| Launch permission | Description                                                                                                    |
| ----------------- | -------------------------------------------------------------------------------------------------------------- |
| public            | The owner grants launch permissions to all AWS accounts.                                                       |
| explicit          | The owner grants launch permissions to specific AWS accounts, organizations,<br>or organizational units (OUs). |
| implicit          | The owner has implicit launch permissions for an AMI.                                                          |

Amazon and the Amazon EC2 community provide a large selection of public AMIs. For more
information, see [Understand shared AMI usage in Amazon EC2](sharing-amis.md "sharing-amis.md").
Developers can charge for their AMIs. For more information, see [Paid AMIs in the AWS Marketplace for Amazon EC2 instances](paid-amis.md "paid-amis.md").

## Root volume type

All AMIs are categorized as either _backed by Amazon EBS_ or _backed
by Amazon S3_.

- Amazon EBS-backed AMI – The root volume for an instance launched from the AMI is an
  Amazon Elastic Block Store (Amazon EBS) volume created from an Amazon EBS snapshot. Supported for both
  Linux and Windows AMIs.
- Amazon S3-backed AMI – The root volume for an instance launched from the AMI is an
  instance store volume created from a template stored in Amazon S3. Supported for
  Linux AMIs only. Windows AMIs do not support instance store for the root
  volume.

For more information, see [Root volumes for your Amazon EC2 instances](RootDeviceStorage.md "RootDeviceStorage.md").

###### Note

Amazon S3-backed AMIs are considered end of life and are not recommended for new usage. They
are only supported on the following older instance types:
C1, C3, D2, I2, M1, M2, M3, R3, and X1.

The following table summarizes the important differences when using the two types of
AMIs.

| Characteristic            | Amazon EBS-backed AMI                                                                                                                                          | Amazon S3-backed AMI                                                                 |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Root volume               | EBS volume                                                                                                                                                     | Instance store volume                                                                |
| Boot time for an instance | Usually less than 1 minute                                                                                                                                     | Usually less than 5 minutes                                                          |
| Data persistence          | By default, the root volume is deleted when the instance terminates.\<br>• Data on any<br>other EBS volumes persists after instance termination by<br>default. | Data on any instance store volumes persists only during the life of the<br>instance. |
| Stopped state             | Can be in a stopped state. Even when the instance is stopped and not running, the root<br>volume is persisted in Amazon EBS.                                   | Cannot be in a stopped state; instances are running or terminated.                   |
| Modifications             | The instance type, kernel, RAM disk, and user data can be changed while the<br>instance is stopped.                                                            | Instance attributes are fixed for the life of an instance.                           |
| Charges                   | You're charged for instance usage, EBS volume usage, and storing your AMI as an EBS<br>snapshot.                                                               | You're charged for instance usage and storing your AMI in Amazon S3.                 |
| AMI creation/bundling     | Uses a single command/call                                                                                                                                     | Requires installation and use of AMI tools                                           |

\* By default, EBS root volumes have the `DeleteOnTermination` flag set to
`true`. For information about how to change this flag so that the
volume persists after termination, see [Keep an Amazon EBS root volume after an Amazon EC2 instance terminates](configure-root-volume-delete-on-termination.md "configure-root-volume-delete-on-termination.md").

\*\* Supported with `io2` EBS Block Express only. For more information, see
[Provisioned IOPS SSD Block Express volumes](../../../ebs/latest/userguide/provisioned-iops.md#io2-block-express "../../../ebs/latest/userguide/provisioned-iops.md#io2-block-express") in the _Amazon EBS User Guide_.

## Virtualization types

Amazon Machine Images use one of two types of virtualization: paravirtual (PV) or hardware
virtual machine (HVM). The main differences between PV and HVM AMIs are the way in which
they boot and whether they can take advantage of special hardware extensions (CPU, network,
and storage) for better performance. Windows AMIs are HVM AMIs.

The following table compares HVM and PV AMIs.

| Characteristic                                       | HVM                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | PV                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Description                                          | HVM AMIs are presented with a fully virtualized set of hardware and<br>boot by executing the master boot record of the root block device of your<br>image. This virtualization type provides the ability to run an operating<br>system directly on top of a virtual machine without any modification, as if<br>it were run on the bare-metal hardware. The Amazon EC2 host system emulates some<br>or all of the underlying hardware that is presented to the guest.                                              | PV AMIs boot with a special boot loader called PV-GRUB, which starts<br>the boot cycle and then chain loads the kernel specified in the<br>`menu.lst` file on your image. Paravirtual guests can<br>run on host hardware that does not have explicit support for virtualization.<br>For more information about PV-GRUB and its use in Amazon EC2, see [User provided kernels](../../../linux/al2/ug/UserProvidedKernels.md "../../../linux/al2/ug/UserProvidedKernels.md"). |
| Supported instance types                             | All current generation instance types support HVM AMIs.                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The following previous generation instance types support PV AMIs: C1, C3,<br>M1, M3, M2, and T1. Current generation instance types do not support PV<br>AMIs.                                                                                                                                                                                                                                                                                                               |
| Support for hardware extensions                      | HVM guests can take advantage of hardware extensions<br>that provide fast access to the underlying hardware on the host<br>system. They are required to use enhanced networking and GPU processing.<br>To pass through instructions to specialized network and GPU devices,<br>the OS must have access to the native hardware platform, and HVM<br>virtualization provides this access. For more information, see [Enhanced networking on Amazon EC2 instances](enhanced-networking.md "enhanced-networking.md"). | No, they can't take advantage of special hardware extensions such as<br>enhanced networking or GPU processing.                                                                                                                                                                                                                                                                                                                                                              |
| [How to find](finding-an-ami.md "finding-an-ami.md") | Verify that the virtualization type of the AMI is set to<br>`hvm`, using the console or the [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md")<br>command.                                                                                                                                                                                                                                                                            | Verify that the virtualization type of the AMI is set to<br>`paravirtual`, using the console or the [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md")<br>command.                                                                                                                                                                                                                              |

###### PV on HVM

Paravirtual guests traditionally performed better with storage and network operations
than HVM guests because they could leverage special drivers for I/O that avoided the
overhead of emulating network and disk hardware, whereas HVM guests had to translate
these instructions to emulated hardware. Now PV drivers are available for HVM guests, so
operating systems that cannot be ported to run in a paravirtualized environment can
still see performance advantages in storage and network I/O by using them. With these PV
on HVM drivers, HVM guests can get the same, or better, performance than paravirtual
guests.
