# Add instance store volumes to an Amazon EC2 AMI

You can create an AMI with a block device mapping that includes instance store volumes.

If you launch an instance that supports **non-NVMe instance store
volumes** using an AMI that specifies instance store volume block device mappings,
the instance includes the instance store volumes. If the number of instance store volume
block device mappings in the AMI exceeds the number of instance store volumes available to
the instance, the additional instance store volume block device mappings are ignored.

If you launch an instance that supports **NVMe instance store
volumes** using an AMI that specifies instance store volume block device mappings,
the instance store volume block device mappings are ignored. Instances that support NVMe
instance store volumes get all of their supported instance store volumes, regardless of the
block device mappings specified in the instance launch request and the AMI. The device
mapping of these volumes depends on the order in which the operating system enumerates the
volumes.

###### Considerations

- The number of available instance store volumes depends on the instance type. For
  more information, see [Available instance store volumes](instance-store-volumes.md#available-instance-store-volumes "instance-store-volumes.md#available-instance-store-volumes").
- You must specify a device name for each block device. For more information, see
  [Device names for volumes on Amazon EC2 instances](device_naming.md "device_naming.md").
- When you launch an instance, you can omit non-NVMe instance store volumes specified
  in the AMI block device mapping or add instance store volumes.
- For M3 instances, specify instance store volumes in the block device mapping of the
  instance, not the AMI. Amazon EC2 might ignore instance store volume block device mappings in
  the AMI.

Console

###### To add instance store volumes to an Amazon EBS-backed AMI

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances** and select the
   instance.
3. Choose **Actions**, **Image and templates**,
   **Create image**.
4. On the **Create image** page, enter a meaningful name and
   description for your image.
5. For each instance store volume to add, choose **Add volume**,
   from **Volume type** select an instance store volume, and from
   **Device** select a device name.
6. Choose **Create image**.

AWS CLI

###### To add instance store volumes to an AMI

Use the [create-image](../../../cli/latest/reference/ec2/create-image.md "../../../cli/latest/reference/ec2/create-image.md") command
with the `--block-device-mappings` option to specify a block device
mapping for an EBS-backed AMI. Use the [register-image](../../../cli/latest/reference/ec2/register-image.md "../../../cli/latest/reference/ec2/register-image.md") command with the
`--block-device-mappings` option to specify a block device mapping for
an iAmazon S3-backed AMI.

```
--block-device-mappings file://mapping.json
```

The following block device mapping adds two instance store volumes.

```
[
    {
        "DeviceName": "/dev/sdc",
        "VirtualName": "ephemeral0"
    },
    {
        "DeviceName": "/dev/sdd",
        "VirtualName": "ephemeral1"
    }
]
```

PowerShell

###### To add instance store volumes to an AMI

Use the [New-EC2Image](../../../powershell/latest/reference/items/New-EC2Image.md "../../../powershell/latest/reference/items/New-EC2Image.md") cmdlet
with the `-BlockDeviceMapping` parameter to specify a block device
mapping for an EBS-backed AMI. Use the [Register-EC2Image](../../../powershell/latest/reference/items/Register-EC2Image.md "../../../powershell/latest/reference/items/Register-EC2Image.md") cmdlet
with the `-BlockDeviceMapping` parameter to specify a block device
mapping for an Amazon S3-backed AMI.

```
-BlockDeviceMapping $bdm
```

The following block device mapping adds two instance store volumes.

```
$bdm = @()

$sdc = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping
$sdc.DeviceName = "/dev/sdc"
$sdc.VirtualName = "ephemeral0"
$bdm += $sdc

$sdd = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping
$sdd.DeviceName = "/dev/sdd"
$sdd.VirtualName = "ephemeral1"
$bdm += $sdd
```
