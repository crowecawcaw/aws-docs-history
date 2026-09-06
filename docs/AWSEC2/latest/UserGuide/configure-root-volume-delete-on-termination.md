

# Keep an Amazon EBS root volume after an Amazon EC2 instance terminates
<a name="configure-root-volume-delete-on-termination"></a>

By default, the Amazon EBS root volume for an instance is deleted when the instance terminates. You can change the default behavior to ensure that an Amazon EBS root volume persists after the instance terminates. To change the default behavior, set the `DeleteOnTermination` attribute to `false`. You can do so either at instance launch or later on.

**Topics**
+ [Configure the root volume to persist during instance launch](#Using_ChangeRootDeviceVolumeToPersist)
+ [Configure the root volume to persist for an existing instance](#set-deleteOnTermination-aws-cli)
+ [Confirm that a root volume is configured to persist](#Using_ConfirmRootDeviceVolumeToPersist)

## Configure the root volume to persist during instance launch
<a name="Using_ChangeRootDeviceVolumeToPersist"></a>

You can configure the root volume to persist when you launch an instance.

------
#### [ Console ]

**To configure the root volume to persist when you launch an instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances** and then choose **Launch instances**.

1. Choose an Amazon Machine Image (AMI), choose and instance type, choose a key pair, and configure your network settings.

1. For **Configure storage**, choose **Advanced**.

1. Expand the root volume.

1. For **Delete on termination**, choose **No**.

1. When you are finished configuring your instance, choose **Launch instance**.

------
#### [ AWS CLI ]

**To configure the root volume to persist when you launch an instance**  
Use the [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command and include the following option.

```
--block-device-mappings file://mapping.json
```

In `mapping.json`, specify a block device mapping that sets the `DeleteOnTermination` attribute to `false`.

```
[
    {
        "DeviceName": "{{/dev/sda1}}",
        "Ebs": {
            "DeleteOnTermination": false
        }
    }
]
```

------
#### [ PowerShell ]

**To configure the root volume to persist when you launch an instance**  
Use the [New-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Instance.html) cmdlet and include the following parameter.

```
-BlockDeviceMapping $bdm
```

Create a block device mapping that sets the `DeleteOnTermination` attribute to `$false`.

```
$ebs = New-Object Amazon.EC2.Model.EbsBlockDevice
$ebs.DeleteOnTermination = $false
$bdm = New-Object Amazon.EC2.Model.BlockDeviceMapping
$bdm.DeviceName = "dev/xvda"
$bdm.Ebs = $ebs
```

------

## Configure the root volume to persist for an existing instance
<a name="set-deleteOnTermination-aws-cli"></a>

You can configure the root volume to persist for a running instance. Note that you can't complete this task using the Amazon EC2 console.

------
#### [ AWS CLI ]

**To configure the root volume to persist for an existing instance**  
Use the [modify-instance-attribute](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-instance-attribute.html) command with a block device mapping that sets the `DeleteOnTermination` attribute to `false`.

```
aws ec2 modify-instance-attribute \
    --instance-id {{i-1234567890abcdef0}} \
    --block-device-mappings file://mapping.json
```

Specify the following in `mapping.json`.

```
[
    {
        "DeviceName": "/dev/xvda",
        "Ebs": {
            "DeleteOnTermination": false
        }
    }
]
```

------
#### [ PowerShell ]

**To configure the root volume to persist for an existing instance**  
Use the [Edit-EC2InstanceAttribute](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2InstanceAttribute.html) cmdlet with a block device mapping that sets the `DeleteOnTermination` attribute to `$false`.

```
$ebs = New-Object Amazon.EC2.Model.EbsInstanceBlockDeviceSpecification
$ebs.DeleteOnTermination = $false
$bdm = New-Object Amazon.EC2.Model.InstanceBlockDeviceMappingSpecification
$bdm.DeviceName = "{{/dev/xvda}}"
$bdm.Ebs = $ebs
Edit-EC2InstanceAttribute `
    -InstanceId {{i-1234567890abcdef0}} `
    -BlockDeviceMapping $bdm
```

------

## Confirm that a root volume is configured to persist
<a name="Using_ConfirmRootDeviceVolumeToPersist"></a>

You can confirm that a root volume is configured to persist.

------
#### [ Console ]

**To confirm that a root volume is configured to persist**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances** and then select the instance.

1. In the **Storage** tab, under **Block devices**, locate the entry for the root volume. If **Delete on termination** is `No`, the volume is configured to persist.

------
#### [ AWS CLI ]

**To confirm that a root volume is configured to persist**  
Use the [describe-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html) command and verify that the `DeleteOnTermination` attribute is set to `false`.

```
aws ec2 describe-instances \
    --instance-id {{i-1234567890abcdef0}} \
    --query "Reservations[].Instances[].BlockDeviceMappings"
```

The following is example output.

```
[
    [
        {
            "DeviceName": "/dev/xvda",
            "Ebs": {
                "AttachTime": "2024-07-12T04:05:33.000Z",
                "DeleteOnTermination": false,
                "Status": "attached",
                "VolumeId": "vol-1234567890abcdef0"
                
        }
    ]              
]
```

------
#### [ PowerShell ]

**To confirm that a root volume is configured to persist**  
Use the [ Get-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Instance.html) cmdlet and verify that the `DeleteOnTermination` attribute is set to `False`.

```
(Get-EC2Instance -InstanceId i-i-1234567890abcdef0).Instances.BlockDeviceMappings.Ebs
```

The following is example output.

```
AssociatedResource  : 
AttachTime          : 7/12/2024 4:05:33 AM
DeleteOnTermination : False
Operator            : 
Status              : attached
VolumeId            : vol-1234567890abcdef0
```

------