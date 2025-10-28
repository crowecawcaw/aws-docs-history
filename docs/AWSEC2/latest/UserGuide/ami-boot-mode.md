# Determine the boot mode parameter of an Amazon EC2 AMI

The AMI boot mode parameter is optional. An AMI can have one of the following boot
mode parameter values: `uefi`, `legacy-bios`, or
`uefi-preferred`.

Some AMIs don't have a boot mode parameter. When an AMI has no boot mode parameter,
the instances launched from the AMI use the default value of the instance type, which is
`uefi` on Graviton, and `legacy-bios` on Intel and AMD
instance types.

Console

###### To determine the boot mode parameter of an AMI

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **AMIs**, and then
   select the AMI.
3. Inspect the **Boot mode** field.
   - A value of **uefi** indicates that the
     AMI supports UEFI.
   - A value of **uefi-preferred** indicates
     that the AMI supports both UEFI and Legacy BIOS.
   - If there is no value, the instances launched from the AMI
     use the default value of the instance type.

###### To determine the boot mode parameter of an AMI when launching an

instance

When launching an instance using the launch instance wizard, at the
step to select an AMI, inspect the **Boot mode** field.
For more information, see [Application and OS Images (Amazon Machine Image)](ec2-instance-launch-parameters.md#liw-ami "ec2-instance-launch-parameters.md#liw-ami").

AWS CLI

###### To determine the boot mode parameter of an AMI

Use the [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") command to determine
the boot mode of an AMI.

```
aws ec2 describe-images \
    --region `us-east-1` \
    --image-id `ami-0abcdef1234567890` \
    --query Images[].BootMode \
    --output text
```

The following is example output.

```
uefi
```

In the output, a
value of `uefi` indicates that the AMI supports UEFI. A value of
`uefi-preferred` indicates that the AMI supports both UEFI
and Legacy BIOS. If there is no value, the instances launched from the AMI
use the default value of the instance type.

PowerShell

###### To determine the boot mode parameter of an AMI

Use the [Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Image.md "../../../powershell/latest/reference/items/Get-EC2Image.md") cmdlet to determine the
boot mode of an AMI.

```
Get-EC2Image -Region `us-east-1` `
    -ImageId `ami-0abcdef1234567890` | Format-List Name, BootMode, TpmSupport
```

The following is example output.

```
Name       : TPM-Windows_Server-2016-English-Full-Base-2023.05.10
BootMode   : uefi
TpmSupport : v2.0
```

In the output, the value of `BootMode` indicates the boot mode of the AMI.
A value of `uefi` indicates that the AMI supports UEFI. A value of
`uefi-preferred` indicates that the AMI supports both UEFI
and Legacy BIOS. If there is no value, the instances launched from the AMI
use the default value of the instance type.
