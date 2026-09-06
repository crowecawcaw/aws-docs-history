

# Preserve data when an instance is terminated
<a name="preserving-volumes-on-termination"></a>

When an Amazon EC2 instance is terminated, you can preserve the data on your instance store volumes or Amazon EBS volumes. This topic explains how to ensure your data persists beyond instance termination.

## How instance termination affects root and data volumes
<a name="how-instance-termination-affects-root-and-data-volumes"></a>

**Instance store volumes**  
When an instance is terminated, the instance store volumes are automatically deleted and the data is lost. To preserve this data beyond the lifetime of the instance, before terminating the instance, manually copy the data to persistent storage, such as an Amazon EBS volume, an Amazon S3 bucket, or an Amazon EFS file system. For more information, see [Storage options for your Amazon EC2 instances](Storage.md).

**Amazon EBS volumes**  
When an instance is terminated, the EBS volumes are either deleted or preserved, depending on the value of the `DeleteOnTermination` attribute for each volume:
+ **Yes** (console) / `true` (CLI) – The volume is deleted when the instance is terminated.
+ **No** (console) / `false` (CLI) – The volume is preserved when the instance is terminated. Preserved volumes continue to incur charges.
**Note**  
After an instance terminates, you can take a snapshot of the preserved volume or attach it to another instance. To avoid incurring charges, you must delete the volume.

## Default deletion behavior for EBS volumes
<a name="default-deletion-behavior-for-ebs-volumes"></a>

The default `DeleteOnTermination` value differs depending on the volume type, whether the volume was attached at launch or after, and the method (console or CLI) used to attach the volume:


| Volume type | Attached when | Method for attaching | Default behavior on instance termination | 
| --- | --- | --- | --- | 
| Root volume | At launch | Console or CLI | Delete | 
| Root volume | After launch | Console or CLI | Preserve | 
| Data volume | At launch | Console | Preserve | 
| Data volume | At launch | CLI | Delete | 
| Data volume | After launch | Console and CLI | Preserve | 

## Check volume persistence settings
<a name="check-ebs-volume-persistence-settings"></a>

The default value at launch for an EBS volume is determined by the `DeleteOnTermination` attribute set on the AMI. You can change the value at instance launch, overriding the AMI setting. We recommend that you verify the default setting for the `DeleteOnTermination` attribute after you launch an instance.

**To check if an Amazon EBS volume will be deleted on instance termination**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Select the instance.

1. Choose the **Storage** tab.

1. Under **Block devices**, scroll right to check the **Delete on termination** column.
   + If **Yes**, the volume is deleted when the instance is terminated.
   + If **No**, the volume is not be deleted when the instance is terminated. Any volumes not deleted continue to incur charges.

## Change the root volume to persist at launch
<a name="delete-on-termination-ebs-volume"></a>

You can change the `DeleteOnTermination` attribute of an EBS root volume when you launch an instance. You can also use the following procedure for a data volume.

------
#### [ Console ]

**To change the root volume of an instance to persist at launch**

1. Follow the procedure to [launch an instance](ec2-launch-instance-wizard.md), but don't launch the instance until you've completed the following steps to change the root volume to persist.

1. On the **Configure storage** pane, choose **Advanced**.

1. Under **EBS volumes**, expand the root volume information.

1. For **Delete on termination**, choose **No**.

1. In the **Summary** panel, review your instance configuration, and then choose **Launch instance**. For more information, see [Launch an EC2 instance using the launch instance wizard in the console](ec2-launch-instance-wizard.md).

------
#### [ AWS CLI ]

**To change the root volume of an instance to persist at launch**  
Use the [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command to change the value of `DeleteOnTermination` in the block device mapping.

Add the `--block-device-mappings` option:

```
--block-device-mappings file://mapping.json
```

In `mapping.json`, specify the device name, for example `/dev/sda1` or `/dev/xvda`, and for `DeleteOnTermination`, specify `false`.

```
[
  {
    "DeviceName": "{{device_name}}",
    "Ebs": {
      "DeleteOnTermination": false
    }
  }
]
```

------
#### [ PowerShell ]

**To change the root volume of an instance to persist at launch**  
Use the [New-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Instance.html) cmdlet to change the value of `DeleteOnTermination` in the block device mapping.

Add the `-BlockDeviceMapping` option:

```
-BlockDeviceMapping $bdm
```

In `bdm`, specify the device name, for example `/dev/sda1` or `/dev/xvda`, and for `DeleteOnTermination`, specify `false`.

```
$ebd = New-Object -TypeName Amazon.EC2.Model.EbsBlockDevice
$ebd.DeleteOnTermination = false
$bdm = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping
$bdm.DeviceName = "{{/dev/sda1}}"
$bdm.Ebs = $ebd
```

------

## Change the root volume of a running instance to persist
<a name="delete-on-termination-running-instance"></a>

You can change the EBS root volume of a running instance to persist. You can also use the following procedure for a data volume.

------
#### [ AWS CLI ]

**To change the root volume to persist**  
Use the [modify-instance-attribute](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-instance-attribute.html) command.

```
aws ec2 modify-instance-attribute \
    --instance-id {{i-1234567890abcdef0}}  \
    --block-device-mappings file://mapping.json
```

In `mapping.json`, specify the device name, for example `/dev/sda1` or `/dev/xvda`, and for `--DeleteOnTermination`, specify `false`.

```
[
  {
    "DeviceName": "{{device_name}}",
    "Ebs": {
      "DeleteOnTermination": false
    }
  }
]
```

------
#### [ PowerShell ]

**To change the root volume to persist**  
Use the [Edit-EC2InstanceAttribute](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2InstanceAttribute.html) cmdlet.

Add the `-BlockDeviceMapping` option:

```
-BlockDeviceMapping $bdm
```

In `bdm`, specify the device name, for example `/dev/sda1` or `/dev/xvda`, and for `DeleteOnTermination`, specify `false`.

```
$ebd = New-Object -TypeName Amazon.EC2.Model.EbsBlockDevice
$ebd.DeleteOnTermination = false
$bdm = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping
$bdm.DeviceName = "{{/dev/sda1}}"
$bdm.Ebs = $ebd
```

------