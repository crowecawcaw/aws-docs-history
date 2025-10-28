# Determine the supported boot modes of an EC2 instance type

You can determine the supported boot modes of an instance type.

The Amazon EC2 console does not display the supported boot modes of an instance type.

AWS CLI
Use the [describe-instance-types](../../../cli/latest/reference/ec2/describe-instance-types.md "../../../cli/latest/reference/ec2/describe-instance-types.md") command to determine
the supported boot modes of an instance type. The
`--query` parameter filters the output to return only the
supported boot modes.

The following example shows that the specified instance type supports both
UEFI and Legacy BIOS boot modes.

```
aws ec2 describe-instance-types \
    --instance-types `m5.2xlarge` \
    --query "InstanceTypes[*].SupportedBootModes"
```

The following is example output.

```
[
    [
        "legacy-bios",
        "uefi"
    ]
]
```

The following example shows that `t2.xlarge` supports only
Legacy BIOS.

```
aws ec2 describe-instance-types \
    --instance-types t2.xlarge \
    --query "InstanceTypes[*].SupportedBootModes"
```

The following is example output.

```
[
    [
        "legacy-bios"
    ]
]
```

PowerShell
Use the [Get-EC2InstanceType](../../../powershell/latest/reference/items/Get-EC2InstanceType.md "../../../powershell/latest/reference/items/Get-EC2InstanceType.md") cmdlet to determine
the supported boot modes of an instance type.

The following example shows that `m5.2xlarge` supports both
UEFI and Legacy BIOS boot modes.

```
Get-EC2InstanceType -InstanceType m5.2xlarge | Format-List InstanceType, SupportedBootModes
```

The following is example output.

```
InstanceType       : m5.2xlarge
SupportedBootModes : {legacy-bios, uefi}
```

The following example shows that `t2.xlarge` supports only
Legacy BIOS.

```
Get-EC2InstanceType -InstanceType t2.xlarge | Format-List InstanceType, SupportedBootModes
```

The following is example output.

```
InstanceType       : t2.xlarge
SupportedBootModes : {legacy-bios}
```

###### To determine the instance types that support UEFI

You can determine the instance types that support UEFI. The Amazon EC2 console
does not display the UEFI support of an instance type.

AWS CLI
The available instance types vary by AWS Region. To see the available instance types
that support UEFI in a Region, use the [describe-instance-types](../../../cli/latest/reference/ec2/describe-instance-types.md "../../../cli/latest/reference/ec2/describe-instance-types.md") command. Include the
`--filters` parameter to scope the results to the
instance types that support UEFI and the `--query` parameter
to scope the output to the value of `InstanceType`.

```
aws ec2 describe-instance-types \
    --filters Name=supported-boot-mode,Values=uefi \
    --query "InstanceTypes[*].[InstanceType]" --output text | sort

```

PowerShell
The available instance types vary by AWS Region. To see the available instance types
that support UEFI in a Region, use the [Get-EC2InstanceType](../../../powershell/latest/reference/items/Get-EC2InstanceType.md "../../../powershell/latest/reference/items/Get-EC2InstanceType.md") cmdlet.

```
Get-EC2InstanceType | `
	Where-Object {$_.SupportedBootModes -Contains "uefi"} | `
	Sort-Object InstanceType | `
	Format-Table InstanceType -GroupBy CurrentGeneration
```

###### To determine the instance types that support UEFI Secure Boot and persist non-volatile variables

Bare metal instances do not support UEFI Secure Boot and non-volatile
variables, so these examples exclude them from the output. For
information about UEFI Secure Boot, see [UEFI Secure Boot for Amazon EC2 instances](uefi-secure-boot.md "uefi-secure-boot.md").

AWS CLI
Use the [describe-instance-types](../../../cli/latest/reference/ec2/describe-instance-types.md "../../../cli/latest/reference/ec2/describe-instance-types.md") command, and exclude the
bare metal instances from the output.

```
aws ec2 describe-instance-types \
    --filters Name=supported-boot-mode,Values=uefi Name=bare-metal,Values=false \
    --query "InstanceTypes[*].[InstanceType]" \
    --output text | sort
```

PowerShell
Use the [Get-EC2InstanceType](../../../powershell/latest/reference/items/Get-EC2InstanceType.md "../../../powershell/latest/reference/items/Get-EC2InstanceType.md") cmdlet, and exclude the
bare metal instances from the output.

```
Get-EC2InstanceType | `
    Where-Object { `
        $_.SupportedBootModes -Contains "uefi" -and `
        $_.BareMetal -eq $False
        } | `
    Sort-Object InstanceType  | `
    Format-Table InstanceType, SupportedBootModes, BareMetal, `
        @{Name="SupportedArchitectures"; Expression={$_.ProcessorInfo.SupportedArchitectures}}
```
