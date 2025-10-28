# Add instance store volumes to an EC2 instance during launch

When you launch an instance type with **non-NVMe instance store volumes**,
such as C1, C3, M1, M2, M3, R3, D2, H1, I2, X1, and X1e, you must specify the block device
mappings for the instance store volumes that you want to attach at launch. The block device
mappings must be specified in the instance launch request or in the AMI used to launch the
instance.

If the AMI includes block device mappings for the instance store volumes, you do not need
to specify block device mappings in the instance launch request, unless you need more instance
store volumes than is included in the AMI.

If the AMI does not include block device mappings for instance store volumes, then you
must specify the block device mappings in the instance launch request.

For instance types with NVMe instance store volumes, all of the supported instance store
volumes are automatically attached to the instance at launch.

###### Considerations

- The number of available instance store volumes depends on the instance type. For
  more information, see [Available instance store volumes](instance-store-volumes.md#available-instance-store-volumes "instance-store-volumes.md#available-instance-store-volumes").
- You must specify a device name for each block device. For more information, see
  [Device names for volumes on Amazon EC2 instances](device_naming.md "device_naming.md").
- For M3 instances, you might receive instance store volumes even if you do not specify
  them in the block device mapping for the instance.

Console

###### To specify a block device mapping in an instance launch request

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the dashboard, choose **Launch instance**.
3. In the **Application and OS Images** section, select the AMI to
   use.
4. In the **Configure storage** section, the **Instance store
   volumes** section lists the instance store volumes that can be attached to the
   instance.
5. For each instance store volume to attach, for **Device name**,
   select the device name to use.
6. Configure the remaining instance settings as needed, and then choose **Launch
   instance**.

AWS CLI

###### To specify a block device mapping in an instance launch request

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md")
command with the `--block-device-mappings` option.

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

###### To specify a block device mapping in an instance launch request

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md")
cmdlet with the `-BlockDeviceMapping` option.

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
