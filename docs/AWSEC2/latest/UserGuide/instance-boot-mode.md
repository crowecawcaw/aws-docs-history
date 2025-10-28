# Determine the boot mode of an EC2 instance

The boot mode of an instance is displayed in the **Boot mode** field in the Amazon EC2 console, and by the
`currentInstanceBootMode` parameter in the AWS CLI.

When an instance is launched, the value for its boot mode parameter
is determined by the value of the boot mode
parameter of the AMI used to launch it, as follows:

- An AMI with a boot mode parameter of `uefi` creates an instance with a
  `currentInstanceBootMode` parameter of `uefi`.
- An AMI with a boot mode parameter of `legacy-bios` creates an instance with a
  `currentInstanceBootMode` parameter of`legacy-bios`.
- An AMI with a boot mode parameter of `uefi-preferred` creates an instance with
  a `currentInstanceBootMode` parameter of `uefi` if the
  instance type supports UEFI; otherwise, it creates an instance with a
  `currentInstanceBootMode` parameter of
  `legacy-bios`.
- An AMI with no boot mode parameter value creates an instance with a
  `currentInstanceBootMode` parameter value that is dependent on
  whether the AMI architecture is ARM or x86 and the supported boot mode of the
  instance type. The default boot mode is `uefi` on Graviton instance types, and
  `legacy-bios` on Intel and AMD instance types.

Console

###### To determine the boot mode of an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**, and then select your
   instance.
3. On the **Details** tab, inspect the **Boot mode**
   field.

AWS CLI

###### To determine the boot mode of an instance

Use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") command to determine
the boot mode of an instance. You can also determine the boot mode of
the AMI that was used to the create the instance.

```
aws ec2 describe-instances \
    --region `us-east-1` \
    --instance-ids `i-1234567890abcdef0` \
    --query Reservations[].Instances[].BootMode \
    --output text
```

The following is example output.

```
uefi
```

PowerShell

###### To determine the boot mode of an instance

Use the [Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md") cmdlet to determine the
boot mode of an instance. You can also determine the boot mode of the
AMI that was used to the create the instance.

```
(Get-EC2Instance `
    -InstanceId `i-1234567890abcdef0`).Instances | Format-List BootMode, CurrentInstanceBootMode, InstanceType, ImageId
```

The following is example output.

```
BootMode                : uefi
CurrentInstanceBootMode : uefi
InstanceType            : c5a.large
ImageId                 : ami-0abcdef1234567890
```
