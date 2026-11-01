

# Specialized AWS Windows AMIs
<a name="specialized-windows-amis"></a>

In addition to its standard operating system version AMIs, Amazon creates several types of specialized AWS Windows AMIs.

You can also create your own customized AMI from one of the AWS Windows AMIs with EC2 Image Builder. For more information, see the [EC2 Image Builder User Guide](https://docs.aws.amazon.com/imagebuilder/latest/userguide/).

**Note**  
Not all AMIs are available in all Regions.

## SQL Server license-included AMIs
<a name="specialized-sql-amis"></a>

Launching an instance from a Windows AMI with Microsoft SQL Server enables you to run the instance as a database server. See [AWS Windows Server license-included SQL Server AMIs](ami-windows-sql.md) for more information.

## STIG Hardened AMIs
<a name="specialized-stig-amis"></a>

STIG Hardened EC2 Windows Server AMIs are pre-configured with over 160 required security settings to help ensure that the instances that you launch follow the latest guidelines for STIG compliance. See [STIG Hardened AWS Windows Server AMIs](ami-windows-stig.md) for more information.

## NitroTPM-enabled AMIs
<a name="specialized-tpm-amis"></a>

Amazon creates a set of AMIs that are pre-configured with NitroTPM and UEFI Secure Boot requirements. See [AWS Windows Server NitroTPM enabled AMIs](ami-windows-tpm.md) for more information.

## Language-specific AMIs
<a name="find-language-specific-windows-amis"></a>

AWS Windows AMIs are available in Chinese, Czech, Dutch, English, French, German, Hungarian, Italian, Japanese, Korean, Polish, Portuguese, Russian, Spanish, Swedish, and Turkish.

------
#### [ AWS CLI ]

Use the [get-parameters-by-path](https://docs.aws.amazon.com/cli/latest/reference/ssm/get-parameters-by-path.html) command to retrieve the latest English-language AWS Windows AMIs.

```
aws ssm get-parameters-by-path \
    --path "/aws/service/ami-windows-latest" \
    --recursive \
    --query 'Parameters[*].{Name:Name,Value:Value}' \
    --output text | grep ".*Windows_Server-.*{{English}}.*" | sort
```

------
#### [ PowerShell ]

Use the [Get-SSMLatestEC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-SSMLatestEC2Image.html) cmdlet to retrieve the latest English-language AWS Windows AMIs.

```
Get-SSMLatestEC2Image `
    -Path ami-windows-latest `
    -ImageName *Windows_Server-*{{English}}* |
Sort-Object Name
```

------

## EC2Launch v2 AMIs
<a name="find-ec2launchv2-amis"></a>

Windows Server 2016 and 2019 AMIs include the EC2Launch v1 agent. Amazon also provides these AMIs repackaged with the EC2Launch v2 agent.

------
#### [ AWS CLI ]

Use the [get-parameters-by-path](https://docs.aws.amazon.com/cli/latest/reference/ssm/get-parameters-by-path.html) command to retrieve the latest AWS Windows AMIs that include the EC2Launch v2 agent.

```
aws ssm get-parameters-by-path \
    --path "/aws/service/ami-windows-latest" \
    --recursive \
    --query 'Parameters[*].{Name:Name,Value:Value}' \
    --output text | grep "EC2LaunchV2-Windows" | sort
```

------
#### [ PowerShell ]

Use the [Get-SSMLatestEC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-SSMLatestEC2Image.html) cmdlet to retrieve the latest AWS Windows AMIs that include the EC2Launch v2 agent.

```
Get-SSMLatestEC2Image `
    -Path ami-windows-latest `
    -ImageName EC2LaunchV2-Windows* |
Sort-Object Name
```

------

## BIOS AMIs
<a name="find-bios-amis"></a>

Windows Server 2025 AMIs use UEFI boot mode by default, which is not supported on EC2 metal instance sizes and some instance types. For those instances, use the BIOS AMIs, which use legacy BIOS boot mode.

------
#### [ AWS CLI ]

Use the [get-parameters-by-path](https://docs.aws.amazon.com/cli/latest/reference/ssm/get-parameters-by-path.html) command to retrieve the latest BIOS AWS Windows AMIs.

```
aws ssm get-parameters-by-path \
    --path "/aws/service/ami-windows-latest" \
    --recursive \
    --query 'Parameters[*].{Name:Name,Value:Value}' \
    --output text | grep "BIOS-Windows" | sort
```

------
#### [ PowerShell ]

Use the [Get-SSMLatestEC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-SSMLatestEC2Image.html) cmdlet to retrieve the latest BIOS AWS Windows AMIs.

```
Get-SSMLatestEC2Image `
    -Path ami-windows-latest `
    -ImageName BIOS-Windows* |
Sort-Object Name
```

------

You can run the preceding commands from [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html), which comes with the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) and [AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-welcome.html) pre-installed. AWS CloudShell automatically configures your credentials. To run the PowerShell commands, run `pwsh`.