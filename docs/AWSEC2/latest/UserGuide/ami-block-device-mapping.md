# Add block device mappings to an AMI

Each AMI has a block device mapping that specifies the block devices to attach to an
instance when it is launched from the AMI. To add more block devices to an AMI, you must
create your own AMI.

###### Contents

- [Specify a block device mapping for an AMI](#create-ami-bdm "#create-ami-bdm")
- [View the EBS volumes in an AMI block device mapping](#view-ami-bdm "#view-ami-bdm")

## Specify a block device mapping for an AMI

There are two ways to specify volumes in addition to the root volume when you create an
AMI. If you've already attached volumes to a running instance before you create an AMI from
the instance, the block device mapping for the AMI includes those same volumes. For EBS
volumes, the existing data is saved to a new snapshot, and it's this new snapshot that's
specified in the block device mapping. For instance store volumes, the data is not
preserved.

For an EBS-backed AMI, you can add EBS volumes and instance store volumes using a block
device mapping. For an Amazon S3-backed AMI, you can add instance store volumes only by
modifying the block device mapping entries in the image manifest file when registering the
image.

###### Note

For M3 instances, you must specify instance store volumes in the block device mapping
for the instance when you launch it. When you launch an M3 instance, instance store
volumes specified in the block device mapping for the AMI may be ignored if they are not
specified as part of the instance block device mapping.

Console

###### To add volumes to an AMI

1. Open the Amazon EC2 console.
2. In the navigation pane, choose **Instances**.
3. Select an instance and choose **Actions**,
   **Image and templates**, **Create image**.
4. Enter a name and a description for the image.
5. The instance volumes appear under **Instance volumes**. To add another
   volume, choose **Add volume**.
6. For **Volume type**, choose the volume type. For **Device**
   choose the device name. For an EBS volume, you can specify additional details, such as a snapshot,
   volume size, volume type, IOPS, and encryption state.
7. Choose **Create image**.

AWS CLI
**To add volumes to an AMI**

Use the [create-image](../../../cli/latest/reference/ec2/create-image.md "../../../cli/latest/reference/ec2/create-image.md")
command to specify a block device mapping for an EBS-backed AMI. Use the [register-image](../../../cli/latest/reference/ec2/register-image.md "../../../cli/latest/reference/ec2/register-image.md") command to specify
a block device mapping for an Amazon S3-backed AMI.

Specify the block device mapping using the `--block-device-mappings`
parameter. You can specified arguments encoded in JSON directly on the command line or
by referencing a JSON file, as shown here.

```
--block-device-mappings file://`mapping.json`
```

To add an instance store volume, use the following mapping. Note that NVMe
instance store volumes are added automatically.

```
{
    "DeviceName": "`device_name`",
    "VirtualName": "ephemeral0"
}
```

To add an empty 100 GiB volume, use the following mapping.

```
{
    "DeviceName": "`device_name`",
    "Ebs": {
      "VolumeSize": 100
    }
}
```

To add an EBS volume based on a snapshot, use the following mapping.

```
{
    "DeviceName": "`device_name`",
    "Ebs": {
      "SnapshotId": "`snap-1234567890abcdef0`"
    }
}
```

To omit a mapping for a device, use the following mapping.

```
{
    "DeviceName": "`device_name`",
    "NoDevice": ""
}
```

PowerShell
Use the [New-EC2Image](../../../powershell/latest/reference/items/New-EC2Image.md "../../../powershell/latest/reference/items/New-EC2Image.md")
cmdlet to specify a block device mapping for an EBS-backed AMI. Use the [Register-EC2Image](../../../powershell/latest/reference/items/Register-EC2Image.md "../../../powershell/latest/reference/items/Register-EC2Image.md") cmdlet to
specify a block device mapping for an Amazon S3-backed AMI.

Add the `-BlockDeviceMapping` option, specifying the updates in
`bdm`:

```
-BlockDeviceMapping $bdm
```

The following mapping adds a volume based on a snapshot.

```
$ebd = New-Object -TypeName Amazon.EC2.Model.EbsBlockDevice
$ebd.SnapshotId = "`snap-1234567890abcdef0`"
$bdm = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping
$bdm.DeviceName = "`device_name`"
$bdm.Ebs = $ebd
```

The following mapping adds an empty 100 GB volume.

```
$ebd = New-Object -TypeName Amazon.EC2.Model.EbsBlockDevice
$ebd.VolumeSize = `100`
$bdm = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping
$bdm.DeviceName = "`device_name`"
$bdm.Ebs = $ebd
```

## View the EBS volumes in an AMI block device mapping

You can easily enumerate the EBS volumes in the block device mapping for an AMI.

Console

###### To view the EBS volumes for an AMI

1.  Open the Amazon EC2 console.
2.  In the navigation pane, choose **AMIs**.
3.  Choose **EBS images** from the **Filter** list to
    get a list of EBS-backed AMIs.
4.  Select the desired AMI, and look at the **Details** tab. At a
    minimum, the following information is available for the root volume (where the
    term **root device** is equivalent to **root
    volume**):

        * **Root Device Type** (`ebs`)
        * **Root Device Name** (for example,
         `/dev/sda1`)
        * **Block Devices** (for example,
         `/dev/sda1=snap-1234567890abcdef0:8:true`)

    If the AMI was created with additional EBS volumes using a block device mapping, the
    **Block Devices** field displays the mapping for those additional
    volumes as well. (This screen doesn't display instance store volumes.)

AWS CLI

###### To view the EBS volumes for an AMI

Use the [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md")
command.

```
aws ec2 describe-images \
    --image-ids `ami-0abcdef1234567890` \
    --query Image[0].BlockDeviceMappings
```

PowerShell

###### To view the EBS volumes for an AMI

Use the [Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Image.md "../../../powershell/latest/reference/items/Get-EC2Image.md")
cmdlet.

```
(Get-EC2Image -ImageId `ami-0abcdef1234567890`).BlockDeviceMappings
```
