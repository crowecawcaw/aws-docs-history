# Enable hibernation for an Amazon EC2 instance

To hibernate an instance, you must first enable it for hibernation while launching the
instance.

###### Important

You can't enable or disable hibernation for an instance after you launch
it.

###### Tasks

- [Enable hibernation for
  On-Demand Instances](#enable-hibernation-for-on-demand-instances "#enable-hibernation-for-on-demand-instances")
- [Enable hibernation for
  Spot Instances](#enable-hibernation-for-spot-instances "#enable-hibernation-for-spot-instances")
- [View if an instance is
  enabled for hibernation](#view-if-instance-is-enabled-for-hibernation "#view-if-instance-is-enabled-for-hibernation")

## Enable hibernation for

On-Demand Instances

You can enable hibernation for your On-Demand Instances.

Console

###### To enable hibernation for an On-Demand Instance

1.  Follow the procedure to [launch an
    instance](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md"), but don't launch the instance until you've
    completed the following steps to enable hibernation.
2.  To enable hibernation, configure the following fields in the
    launch instance wizard:
    1.  Under **Application and OS Images (Amazon
        Machine Image)**, select an AMI that
        supports hibernation. For more information, see [AMIs](hibernating-prerequisites.md#hibernation-prereqs-supported-amis "hibernating-prerequisites.md#hibernation-prereqs-supported-amis").
    2.  Under **Instance type**, select a
        supported instance type. For more information, see [Instance families](hibernating-prerequisites.md#hibernation-prereqs-supported-instance-families "hibernating-prerequisites.md#hibernation-prereqs-supported-instance-families").
    3.  Under **Configure storage**, choose
        **Advanced** (at the right), and
        specify the following information for the root
        volume:

            * For **Size (GiB)**, enter the
             EBS root volume size. The volume must be large
             enough to store the RAM contents and accommodate
             your expected usage.
            * For **Volume type**, select a
             supported EBS volume type: General Purpose SSD (`gp2` and `gp3`) or
             Provisioned IOPS SSD (`io1` and `io2`).
            * For **Encrypted**, choose
             **Yes**. If you enabled
             encryption by default in this AWS Region,
             **Yes** is selected.
            * For **KMS key**, select the
             encryption key for the volume. If you enabled
             encryption by default in this AWS Region, the
             default encryption key is selected.

        For more information about the prerequisites for the
        root volume, see [Prerequisites for EC2 instance hibernation](hibernating-prerequisites.md "hibernating-prerequisites.md").

    4.  Expand **Advanced details**, and for
        **Stop - Hibernate behavior**,
        choose **Enable**.

3.  In the **Summary** panel, review your
    instance configuration, and then choose **Launch
    instance**. For more information, see [Launch an EC2 instance using the launch
    instance wizard in the console](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").

AWS CLI

###### To enable hibernation for an On-Demand Instance

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command to launch an instance. Specify
the EBS root volume parameters using the
`--block-device-mappings file://mapping.json`
parameter, and enable hibernation using the
`--hibernation-options Configured=true`
parameter.

```
aws ec2 run-instances \
    --image-id `ami-0abcdef1234567890` \
    --instance-type `m5.large` \
    --block-device-mappings file://`mapping`.json \
    --hibernation-options Configured=true \
    --count `1` \
    --key-name `MyKeyPair`
```

Specify the following in `mapping.json`.

```
[
    {
        "DeviceName": "`/dev/xvda`",
        "Ebs": {
            "VolumeSize": `30`,
            "VolumeType": "`gp2`",
            "Encrypted": true
        }
    }
]
```

The value for `DeviceName` must match the root device
name that's associated with the AMI. To find the root device name,
use the [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") command.

```
aws ec2 describe-images --image-id ami-`0abcdef1234567890`
```

If you enabled encryption by default in this AWS Region, you can
omit `"Encrypted": true`.

PowerShell

###### To enable hibernation for an On-Demand Instance

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md") command to launch an instance. Specify
the EBS root volume by first defining the block device mapping, and
then adding it to the command using the
`-BlockDeviceMappings` parameter. Enable hibernation
using the `-HibernationOptions_Configured $true`
parameter.

```
$ebs_encrypt = New-Object Amazon.EC2.Model.BlockDeviceMapping
$ebs_encrypt.DeviceName = "`/dev/xvda`"
$ebs_encrypt.Ebs = New-Object Amazon.EC2.Model.EbsBlockDevice
$ebs_encrypt.Ebs.VolumeSize = `30`
$ebs_encrypt.Ebs.VolumeType = "`gp2`"
$ebs_encrypt.Ebs.Encrypted = $true

New-EC2Instance `
    -ImageId `ami-0abcdef1234567890` `
    -InstanceType `m5.large` `
    -BlockDeviceMappings $ebs_encrypt `
    -HibernationOptions_Configured $true `
    -MinCount `1` `
    -MaxCount `1` `
    -KeyName `MyKeyPair`
```

The value for `DeviceName` must match the root device
name associated with the AMI. To find the root device name, use the
[Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Image.md "../../../powershell/latest/reference/items/Get-EC2Image.md") command.

```
Get-EC2Image -ImageId `ami-0abcdef1234567890`
```

If you enabled encryption by default in this AWS Region, you can
omit `Encrypted = $true` from the block device
mapping.

## Enable hibernation for

Spot Instances

You can enable hibernation for your Spot Instances. For more information about hibernating
a Spot Instance on interruption, see [Spot Instance interruptions](spot-interruptions.md "spot-interruptions.md").

Console

###### To enable hibernation for a Spot Instance

1.  Follow the procedure to [request a Spot Instance using
    the launch instance wizard](using-spot-instances-request.md "using-spot-instances-request.md"), but don't launch the
    instance until you've completed the following steps to enable
    hibernation.
2.  To enable hibernation, configure the following fields in the
    launch instance wizard:
    1.  Under **Application and OS Images (Amazon
        Machine Image)**, select an AMI that
        supports hibernation. For more information, see [AMIs](hibernating-prerequisites.md#hibernation-prereqs-supported-amis "hibernating-prerequisites.md#hibernation-prereqs-supported-amis").
    2.  Under **Instance type**, select a
        supported instance type. For more information, see [Instance families](hibernating-prerequisites.md#hibernation-prereqs-supported-instance-families "hibernating-prerequisites.md#hibernation-prereqs-supported-instance-families").
    3.  Under **Configure storage**, choose
        **Advanced** (at the right), and
        specify the following information for the root
        volume:

            * For **Size (GiB)**, enter the
             EBS root volume size. The volume must be large
             enough to store the RAM contents and accommodate
             your expected usage.
            * For **Volume type**, select a
             supported EBS volume type: General Purpose SSD (`gp2` and `gp3`) or
             Provisioned IOPS SSD (`io1` and `io2`).
            * For **Encrypted**, choose
             **Yes**. If you enabled
             encryption by default in this AWS Region,
             **Yes** is selected.
            * For **KMS key**, select the
             encryption key for the volume. If you enabled
             encryption by default in this AWS Region, the
             default encryption key is selected.

        For more information about the prerequisites for the
        root volume, see [Prerequisites for EC2 instance hibernation](hibernating-prerequisites.md "hibernating-prerequisites.md").

    4.  Expand **Advanced details**, and, in
        addition to the fields for configuring a Spot Instance, do the
        following:
        1. For **Request
           type**, choose
           **Persistent**.
        2. For **Interruption
           behavior**, choose
           **Hibernate**. Alternatively, for
           **Stop - Hibernate behavior**,
           choose **Enable**. Both fields
           enable hibernation on your Spot Instance. You need only
           configure one of them.

3.  In the **Summary** panel, review your
    instance configuration, and then choose **Launch
    instance**. For more information, see [Launch an EC2 instance using the launch
    instance wizard in the console](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").

AWS CLI

###### To enable hibernation for a Spot Instance

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command to request a Spot Instance. Specify the
EBS root volume parameters using the `--block-device-mappings
 file://mapping.json` parameter, and enable hibernation
using the `--hibernation-options Configured=true`
parameter. The Spot request type (`SpotInstanceType`)
must be `persistent`.

```
aws ec2 run-instances \
    --image-id `ami-0abcdef1234567890` \
    --instance-type `c4.xlarge` \
    --block-device-mappings file://`mapping`.json \
    **--hibernation-options Configured=true \**
    --count `1` \
    --key-name `MyKeyPair`
    --instance-market-options
        {
           "MarketType":"spot",
           "SpotOptions":{
              "MaxPrice":"`1`",
              **"SpotInstanceType":"persistent"**
            }
        }
```

Specify the EBS root volume parameters in `mapping.json` as
follows.

```
[
    {
        "DeviceName": "`/dev/xvda`",
        "Ebs": {
            "VolumeSize": `30`,
            "VolumeType": "`gp2`",
            "Encrypted": true
        }
    }
]
```

The value for `DeviceName` must match the root device
name that's associated with the AMI. To find the root device name,
use the [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") command.

```
aws ec2 describe-images --image-id ami-`0abcdef1234567890`
```

If you enabled encryption by default in this AWS Region, you can
omit `"Encrypted": true`.

PowerShell

###### To enable hibernation for a Spot Instance

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md") command to request a Spot Instance. Specify the
EBS root volume by first defining the block device mapping, and then
adding it to the command using the `-BlockDeviceMappings`
parameter. Enable hibernation using the
`-HibernationOptions_Configured $true`
parameter.

```
$ebs_encrypt = New-Object Amazon.EC2.Model.BlockDeviceMapping
$ebs_encrypt.DeviceName = "`/dev/xvda`"
$ebs_encrypt.Ebs = New-Object Amazon.EC2.Model.EbsBlockDevice
$ebs_encrypt.Ebs.VolumeSize = `30`
$ebs_encrypt.Ebs.VolumeType = "`gp2`"
$ebs_encrypt.Ebs.Encrypted = $true

New-EC2Instance `
    -ImageId `ami-0abcdef1234567890` `
    -InstanceType `m5.large` `
    -BlockDeviceMappings $ebs_encrypt `
    -HibernationOptions_Configured $true `
    -MinCount `1` `
    -MaxCount `1` `
    -KeyName `MyKeyPair` `
    -InstanceMarketOption @(
        MarketType = spot;
        SpotOptions @{
        MaxPrice = `1`;
        SpotInstanceType = persistent}
    )
```

The value for `DeviceName` must match the root device
name associated with the AMI. To find the root device name, use the
[Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Image.md "../../../powershell/latest/reference/items/Get-EC2Image.md") command.

```
Get-EC2Image -ImageId `ami-0abcdef1234567890`
```

If you enabled encryption by default in this AWS Region, you can
omit `Encrypted = $true` from the block device
mapping.

## View if an instance is

enabled for hibernation

You can check whether an instance is enabled for hibernation.

Console

###### To view if an instance is enabled for hibernation

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select the instance and, on the **Details**
   tab, in the **Instance details** section,
   inspect **Stop-hibernate behavior**.
   **Enabled** indicates that the instance is
   enabled for hibernation.

AWS CLI

###### To view if an instance is enabled for hibernation

Use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") command and specify the
`--filters
 "Name=hibernation-options.configured,Values=true"`
parameter to filter instances that are enabled for
hibernation.

```
aws ec2 describe-instances \
    --filters "Name=hibernation-options.configured,Values=true"
```

The following field in the output indicates that the instance is
enabled for hibernation.

```
"HibernationOptions": {
    "Configured": true
}
```

PowerShell

###### To view if an instance is enabled for hibernation

Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md") cmdlet and filter instances that
are enabled for hibernation.

```
(Get-EC2Instance `
    -Filter @{Name="hibernation-options.configured"; Values="true"}).Instances
```
