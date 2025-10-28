# Requirements for Amazon EBS volume modifications

The following requirements and limitations apply when you modify an Amazon EBS volume. To learn
more about the general requirements for EBS volumes, see [Amazon EBS volume constraints](volume_constraints.md "volume_constraints.md").

###### Topics

- [Supported instance types](#instance-support "#instance-support")
- [Operating system](#operating-system "#operating-system")

## Supported instance types

Elastic Volumes are supported on the following instances:

- All [current generation instances](../../../AWSEC2/latest/UserGuide/instance-types.md#current-gen-instances "../../../AWSEC2/latest/UserGuide/instance-types.md#current-gen-instances")
- The following previous-generation instances: C1, C3, C4, G2, I2, M1, M3, M4, R3, and R4

If your instance type does not support Elastic Volumes, see [Modify an EBS volume if Elastic Volumes is not
supported](requesting-ebs-volume-modifications.md#modify-volume-stop-start "requesting-ebs-volume-modifications.md#modify-volume-stop-start").

## Operating system

The following operating system requirements apply:

Linux AMIs require a GUID partition table (GPT) and GRUB 2 for boot volumes that are 2
TiB (2,048 GiB) or larger. Many Linux AMIs today still use the MBR partitioning scheme,
which only supports boot volume sizes up to 2 TiB. If your instance does not boot with a
boot volume larger than 2 TiB, the AMI you are using may be limited to a boot volume size of
less than 2 TiB. Non-boot volumes do not have this limitation on Linux instances.

Before attempting to resize a boot volume beyond 2 TiB, you can determine whether the
volume is using MBR or GPT partitioning by running the following command on your
instance:

```
`[ec2-user ~]$` `sudo gdisk -l /dev/xvda`
```

An Amazon Linux instance with GPT partitioning returns the following information:

```
GPT fdisk (gdisk) version 0.8.10

  Partition table scan:
    MBR: protective
    BSD: not present
    APM: not present
    GPT: present

  Found valid GPT with protective MBR; using GPT.
```

A SUSE instance with MBR partitioning returns the following information:

```
GPT fdisk (gdisk) version 0.8.8

  Partition table scan:
    MBR: MBR only
    BSD: not present
    APM: not present
    GPT: not present
```

By default, Windows initializes volumes with a Master Boot Record (MBR) partition table.
Because MBR supports only volumes smaller than 2 TiB (2,048 GiB), Windows prevents you from
resizing MBR volumes beyond this limit. In such a case, the **Extend
Volume** option is disabled in the Windows **Disk Management**
utility. If you use the AWS Management Console or AWS CLI to create an MBR-partitioned volume that exceeds
the size limit, Windows cannot detect or use the additional space.

To overcome this limitation, you can create a new, larger volume with a GUID partition
table (GPT) and copy over the data from the original MBR volume.

###### To create a GPT volume

1. Create a new, empty volume of the desired size in the Availability Zone of the EC2
   instance and attach it to your instance.

###### Note

The new volume must not be a volume restored from a snapshot. 2. Log in to your Windows system and open **Disk Management**
(**diskmgmt.exe**). 3. Open the context (right-click) menu for the new disk and choose
**Online**. 4. In the **Initialize Disk** window, select the new disk and choose
**GPT (GUID Partition Table)**, **OK**. 5. When initialization is complete, copy the data from the original volume to the new
volume, using a tool such as robocopy or teracopy. 6. In **Disk Management**, change the drive letters to appropriate
values and take the old volume offline. 7. In the Amazon EC2 console, detach the old volume from the instance, reboot the instance
to verify that it functions properly, and delete the old volume.
