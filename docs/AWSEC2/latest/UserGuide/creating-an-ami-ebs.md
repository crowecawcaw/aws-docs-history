# Create an Amazon EBS-backed AMI

You can create your own Amazon EBS-backed AMI from an Amazon EC2 instance or from a snapshot of the
root volume of an Amazon EC2 instance.

To create an Amazon EBS-backed AMI from an instance, start by launching an instance using an
existing Amazon EBS-backed AMI. This AMI can be one you obtained from the AWS Marketplace, created using
[VM Import/Export](../../../vm-import/latest/userguide/what-is-vmimport.md "../../../vm-import/latest/userguide/what-is-vmimport.md"), or any other AMI
that you can access. After customizing the instance to meet your specific requirements,
create and register a new AMI. You can then use the new AMI to launch new instances with
your customizations.

###### Note

To create an AMI that supports EC2 instance attestation, see [Attestable AMIs](attestable-ami.md "attestable-ami.md").

The procedures described below work for Amazon EC2 instances backed by encrypted Amazon Elastic Block Store
(Amazon EBS) volumes (including the root volume) as well as for unencrypted volumes.

The AMI creation process is different for Amazon S3-backed AMIs. For more information, see
[Create an Amazon S3-backed AMI](creating-an-ami-instance-store.md "creating-an-ami-instance-store.md").

###### Contents

- [Overview of AMI creation from an instance](#process-creating-an-ami-ebs "#process-creating-an-ami-ebs")
- [Create an AMI from an instance](#how-to-create-ebs-ami "#how-to-create-ebs-ami")
- [Create an AMI from a snapshot](#creating-launching-ami-from-snapshot "#creating-launching-ami-from-snapshot")

## Overview of AMI creation from an instance

The following diagram summarizes the process for creating an Amazon EBS-backed AMI from a
running EC2 instance: Start with an existing AMI, launch an instance, customize it,
create a new AMI from it, and finally launch an instance of your new AMI. The
numbers in the diagram match the numbers in the description that follows.

![Workflow for creating an AMI from an instance](images/running-instance.png)

**1 – AMI #1: Start with an existing
AMI**

Find an existing AMI that is similar to the AMI that you'd like to create.
This can be an AMI you have obtained from the AWS Marketplace, an AMI that you have created
using [VM Import/Export](../../../vm-import/latest/userguide/what-is-vmimport.md "../../../vm-import/latest/userguide/what-is-vmimport.md"), or any
other AMI that you can access. You'll customize this AMI for your needs.

In the diagram, **EBS root volume snapshot #1** indicates
that the AMI is an Amazon EBS-backed AMI and that information about the root
volume is stored in this snapshot.

**2 – Launch instance from existing
AMI**

The way to configure an AMI is to launch an instance from the AMI on
which you'd like to base your new AMI, and then customize the instance
(indicated at **3** in the diagram). Then, you'll create a
new AMI that includes the customizations (indicated at
**4** in the diagram).

**3 – EC2 instance #1: Customize the
instance**

Connect to your instance and customize it for your needs. Your new AMI
will include these customizations.

You can perform any of the following actions on your instance to customize
it:

- Install software and applications
- Copy data
- Reduce start time by deleting temporary files and defragmenting
  your hard drive
- Attach additional EBS volumes

**4 – Create image**

When you create an AMI from an instance, Amazon EC2 powers down the instance
before creating the AMI to ensure that everything on the instance is
stopped and in a consistent state during the creation process. If you're
confident that your instance is in a consistent state appropriate for AMI
creation, you can tell Amazon EC2 not to power down and reboot the instance. Some
file systems, such as XFS, can freeze and unfreeze activity, making it safe
to create the image without rebooting the instance.

During the AMI-creation process, Amazon EC2 creates snapshots of your
instance's root volume and any other EBS volumes attached to your instance.
You're charged for the snapshots until you [deregister the AMI](deregister-ami.md "deregister-ami.md")
and delete the snapshots. If any volumes attached to the
instance are encrypted, the new AMI only launches successfully on
instances that support Amazon EBS encryption.

Depending on the size of the volumes, it can take several minutes for the AMI-creation
process to complete (sometimes up to 24 hours). You might find it more
efficient to create snapshots of your volumes before creating your AMI.
This way, only small, incremental snapshots need to be created when the
AMI is created, and the process completes more quickly (the total time for
snapshot creation remains the same).

**5 – AMI #2: New AMI**

After the process completes, you have a new AMI and snapshot (**snapshot
#2**) created from the root volume of the instance. If you
added instance store volumes or EBS volumes to the instance, in addition to
the root volume, the block device mapping for the new AMI contains
information for these volumes.

Amazon EC2 automatically registers the AMI for you.

**6 – Launch instance from new
AMI**

You can use the new AMI to launch an instance.

**7 – EC2 instance #2: New
instance**

When you launch an instance using the new AMI, Amazon EC2 creates a new EBS volume for the
instance's root volume using the snapshot. If you added instance store
volumes or EBS volumes when you customized the instance, the block device
mapping for the new AMI contains information for these volumes, and the
block device mappings for instances that you launch from the new AMI
automatically contain information for these volumes. The instance store
volumes specified in the block device mapping for the new instance are new
and don't contain any data from the instance store volumes of the instance
you used to create the AMI. The data on EBS volumes persists. For more
information, see [Block device mappings for volumes on Amazon EC2 instances](block-device-mapping-concepts.md "block-device-mapping-concepts.md").

When you create a new instance from an EBS-backed AMI, you should
initialize both its root volume and any additional EBS storage before
putting it into production. For more information, see [Initialize Amazon EBS volumes](../../../ebs/latest/userguide/ebs-initialize.md "../../../ebs/latest/userguide/ebs-initialize.md")
in the _Amazon EBS User Guide_.

## Create an AMI from an instance

If you have an existing instance, you can create an AMI from this instance.

Console

###### To create an AMI

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select the instance from which to create the AMI, and then choose
   **Actions**, **Image and
   templates**, **Create image**.

###### Tip

If this option is disabled, your instance isn't an
Amazon EBS-backed instance. 4. On the **Create image** page, specify the
following information:

    1. For **Image name**, enter a unique name
     for the image, up to 127 characters.
    2. For **Image description**, enter an
     optional description of the image, up to 255
     characters.
    3. For **Reboot instance**, either keep the checkbox selected (the
     default), or clear it.




    	* If **Reboot instance** is selected, when Amazon EC2 creates the new
    	 AMI, it reboots the instance so that it can take
    	 snapshots of the attached volumes while data is at
    	 rest, in order to ensure a consistent state.
    	* If **Reboot instance** is cleared, when Amazon EC2 creates the new AMI,
    	 it does not shut down and reboot the
    	 instance.
    ###### Warning

    If you clear **Reboot instance**, we can't guarantee the file system
     integrity of the created image.
    4. **Instance volumes** – You can
     modify the root volume, and add additional Amazon EBS and
     instance store volumes, as follows:


    	1. The root volume is defined in the first
    	 row.




    		* To change the size of the root volume, for
    		 **Size**, enter the required
    		 value.
    		* If you select **Delete on
    		 termination**, when you terminate the
    		 instance created from this AMI, the EBS volume is
    		 deleted. If you clear **Delete on
    		 termination**, when you terminate the
    		 instance, the EBS volume is not deleted. For more
    		 information, see [Preserve data when an instance is
    		 terminated](preserving-volumes-on-termination.md "preserving-volumes-on-termination.md").
    	2. To add an EBS volume, choose **Add
    	 volume** (which adds a new row). For
    	 **Storage type**, choose
    	 **EBS**, and fill in the fields
    	 in the row. When you launch an instance from your
    	 new AMI, additional volumes are automatically
    	 attached to the instance. Empty volumes must be
    	 formatted and mounted. Volumes based on a snapshot
    	 must be mounted.
    	3. To add an instance store volume, see [Add instance store volumes to an Amazon EC2 AMI](adding-instance-storage-ami.md "adding-instance-storage-ami.md").
    	 When you launch an instance from your new AMI,
    	 additional volumes are automatically initialized and
    	 mounted. These volumes do not contain data from the
    	 instance store volumes of the running instance on
    	 which you based your AMI.
    5. **Snapshot destination** – If your instance volumes are in a
     Local Zone that supports EBS local snapshots, choose where
     to create the AMI’s snapshots:




    	* **AWS Region**: Create snapshots in the parent Region of the
    	 Local Zone of your volumes.
    	* **AWS Local Zone**: Create snapshots in the same Local Zone as
    	 your volumes.
    ###### Note

    This option appears only in Local Zones that support EBS local snapshots, and only
     if your instance was created in a Local Zone. If the
     volume is in a Region, this option does not appear, and
     the snapshot is automatically created in the same Region
     as the volume. For more information, see [Local snapshots in Local Zones](../../../ebs/latest/userguide/snapshots-localzones.md "../../../ebs/latest/userguide/snapshots-localzones.md") in the
     *Amazon EBS User Guide*.


    ###### Important

    All snapshots of the instance’s volumes must be in the same location. Verify the
     location of existing snapshots. If any existing
     snapshots are in a different location than your selected
     destination, the AMI creation will fail.
    6. **Tags** – You can tag the AMI and
     the snapshots with the same tags, or you can tag them with
     different tags.




    	* To tag the AMI and the snapshots with the
    	 *same* tags,
    	 choose **Tag image and snapshots
    	 together**. The same tags are applied to
    	 the AMI and every snapshot that is created.
    	* To tag the AMI and the snapshots with *different* tags, choose
    	 **Tag image and snapshots
    	 separately**. Different tags are applied
    	 to the AMI and the snapshots that are created.
    	 However, all the snapshots get the same tags; you
    	 can't tag each snapshot with a different tag.
    To add a tag, choose **Add tag**, and
     enter the key and value for the tag. Repeat for each
     tag.
    7. When you're ready to create your AMI, choose
     **Create image**.

5. To view the status of your AMI while it is being created:
   1. In the navigation pane, choose
      **AMIs**.
   2. Set the filter to **Owned by me**, and
      find your AMI in the list.

   Initially, the status is `pending` but should
   change to `available` after a few minutes.

6. (Optional) To view the snapshot that was created for the new
   AMI:
   1. Note the ID of your AMI that you located in the previous
      step.
   2. In the navigation pane, choose
      **Snapshots**.
   3. Set the filter to **Owned by me**, and
      then find the snapshot with the new AMI ID in the
      **Description** column.

   When you launch an instance from this AMI, Amazon EC2 uses this snapshot to create the
   instance's root volume.

AWS CLI

###### To create an AMI

Use the [create-image](../../../cli/latest/reference/ec2/create-image.md "../../../cli/latest/reference/ec2/create-image.md") command.

```
aws ec2 create-image \
    --instance-id `i-1234567890abcdef0` \
    --name "`my-web-server`" \
    --description "`My web server image`" \
    --no-reboot
```

PowerShell

###### To create an AMI

Use the [New-EC2Image](../../../powershell/latest/reference/items/New-EC2Image.md "../../../powershell/latest/reference/items/New-EC2Image.md") cmdlet.

```
New-EC2Image `
    -InstanceId `i-1234567890abcdef0` `
    -Name `"my-web-server"` `
    -Description "`My web server image`" `
    -NoReboot $true
```

## Create an AMI from a snapshot

If you have a snapshot of the root volume of an instance, you can create an AMI from this
snapshot.

###### Note

In most cases, AMIs for Windows, Red Hat, SUSE, and SQL Server require correct
licensing information to be present on the AMI. For more information, see [Understand AMI billing information](ami-billing-info.md "ami-billing-info.md"). When creating an
AMI from a snapshot, the `RegisterImage` operation derives the correct
billing information from the snapshot's metadata, but this requires the appropriate
metadata to be present. To verify if the correct billing information was applied,
check the **Platform details** field on the new AMI. If the field
is empty or doesn't match the expected operating system code (for example, Windows,
Red Hat, SUSE, or SQL), the AMI creation was unsuccessful, and you should discard
the AMI and follow the instructions in [Create an AMI from an instance](#how-to-create-ebs-ami "#how-to-create-ebs-ami").

Console

###### To create an AMI from a snapshot

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Snapshots**.
3. Select the snapshot from which to create the AMI, and then
   choose **Actions**, **Create image from
   snapshot**.
4. On the **Create image from snapshot** page,
   specify the following information:
   1. For **Image name**, enter a descriptive
      name for the image.
   2. For **Description**, enter a brief
      description for the image.
   3. For **Architecture**, choose the image
      architecture. Choose **i386** for 32-bit,
      **x86_64** for 64-bit,
      **arm64** for 64-bit ARM, or
      **x86_64** for 64-bit macOS.
   4. For **Root device name**, enter the device name to use for the root
      volume. For more information, see [Device names for volumes on Amazon EC2 instances](device_naming.md "device_naming.md").
   5. For **Virtualization type**, choose the
      virtualization type to be used by instances launched from
      this AMI. For more information, see [Virtualization types](ComponentsAMIs.md#virtualization_types "ComponentsAMIs.md#virtualization_types").
   6. (For paravirtual virtualization only) For **Kernel ID**, select the
      operating system kernel for the image. If you're using a
      snapshot of the root volume of an instance, select the same
      kernel ID as the original instance. If you're unsure, use
      the default kernel.
   7. (For paravirtual virtualization only) For **RAM
      disk ID**, select the RAM disk for the image.
      If you select a specific kernel, you may need to select a
      specific RAM disk with the drivers to support it.
   8. For **Boot mode**, choose the boot mode
      for the image, or choose **Use default** so
      that when an instance is launched with this AMI, it boots
      with the boot mode supported by the instance type. For more
      information, see [Set the boot mode of an Amazon EC2 AMI](set-ami-boot-mode.md "set-ami-boot-mode.md").
   9. (Optional) Under **Block device mappings**,
      customize the root volume and add additional data volumes.

   For each volume, you can specify the size, type, performance
   characteristics, the behavior of delete on termination, and
   encryption status. For the root volume, the size can't be
   smaller than the size of the snapshot. For volume type, General Purpose SSD
   `gp3` is the default selection. 10. (Optional) Under **Tags**, you can add one or more tags
   to the new AMI. To add a tag, choose **Add
   tag**, and enter the key and value for the tag.
   Repeat for each tag. 11. When you're ready to create your AMI, choose
   **Create image**.

5. (Windows, Red Hat, SUSE, and SQL Server only) To verify if the correct billing
   information was applied, check the **Platform
   details** field on the new AMI. If the field is empty
   or doesn't match the expected operating system code (for example,
   **Windows** or **Red Hat**),
   the AMI creation was unsuccessful, and you should discard the AMI
   and follow the instructions in [Create an AMI from an instance](#how-to-create-ebs-ami "#how-to-create-ebs-ami").

AWS CLI

###### To create an AMI from a snapshot using the AWS CLI

Use the [register-image](../../../cli/latest/reference/ec2/register-image.md "../../../cli/latest/reference/ec2/register-image.md") command.

```
aws ec2 register-image \
    --name `my-image` \
    --root-device-name `/dev/xvda` \
    --block-device-mappings DeviceName=`/dev/xvda`,Ebs={SnapshotId=`snap-0db2cf683925d191f`}
```

PowerShell

###### To create an AMI from a snapshot using PowerShell

Use the [Register-EC2Image](../../../powershell/latest/reference/items/Register-EC2Image.md "../../../powershell/latest/reference/items/Register-EC2Image.md") cmdlet.

```
$block = @{SnapshotId=`snap-0db2cf683925d191f`}
Register-EC2Image `
    -Name `my-image` `
    -RootDeviceName `/dev/xvda` `
    -BlockDeviceMapping @{DeviceName="/dev/xvda";Ebs=$block}
```
