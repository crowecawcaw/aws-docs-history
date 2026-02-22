# AWS Windows Server NitroTPM enabled AMIs

Amazon creates a set of AMIs that are pre-configured with NitroTPM and UEFI Secure Boot
requirements, as follows:

- The TPM 2.0 Command Response Buffer (CRB) driver is installed
- NitroTPM is enabled
- UEFI Secure Boot mode is enabled with Microsoft keys
  For more detailed information about NitroTPM, see [NitroTPM for Amazon EC2 instances](../../../AWSEC2/latest/UserGuide/nitrotpm.md "../../../AWSEC2/latest/UserGuide/nitrotpm.md") in the
  _Amazon EC2 User Guide_.

## Find Windows Server AMIs configured with

NitroTPM and UEFI Secure Boot

AWS managed AMIs always include the AMI creation date as part of the name.
The best way to ensure that your search returns the AMIs that you're looking for
is to add date filtering for the name. Use one of the following command line options
to find an AMI.

AWS CLI

###### Find the latest NitroTPM and UEFI Secure Boot AMIs

The following example retrieves a list of the latest Windows Server AMIs
that are configured for NitroTPM and UEFI Secure Boot.

```
`aws ssm get-parameters-by-path \
 --path "/aws/service/ami-windows-latest" \
 --recursive \
 --query 'Parameters[*].{Name:Name,Value:Value}' \
 --output text | grep "TPM-Windows_Server" | sort`
```

###### Find a specific AMI

The following example retrieves Windows Server AMIs that are
configured for NitroTPM and UEFI Secure Boot by filtering on the AMI name,
the owner, the platform, and the creation date (year and month). Output is
formatted as a table with columns for the AMI name and image ID.

```
`aws ec2 describe-images \
 --owners amazon \
 --filters \
 "Name=name,Values=TPM-Windows_Server-*" \
 "Name=platform,Values=windows" \
 "Name=creation-date,Values=`2025-05`*" \
 --query 'Images[].[Name,ImageId]' \
 --output text | sort`
```

PowerShell (recommended)

###### Find the latest NitroTPM and UEFI Secure Boot AMIs

The following example retrieves a list of the latest Windows Server AMIs
that are configured for NitroTPM and UEFI Secure Boot.

```
`Get-SSMLatestEC2Image `
 -Path ami-windows-latest `
 -ImageName TPM-Windows* |
Sort-Object Name`
```

###### Note

If this command doesn't run in your environment, you might be missing a PowerShell module. For
more information about this command, see [Get-SSMLatestEC2Image Cmdlet](../../../powershell/v4/reference/items/Get-SSMLatestEC2Image.md "../../../powershell/v4/reference/items/Get-SSMLatestEC2Image.md").

Alternatively, you can use the [CloudShell console](https://console.aws.amazon.com/cloudshell/home "https://console.aws.amazon.com/cloudshell/home")
and run `pwsh` to bring up a PowerShell prompt that already has all of the AWS tools installed.
For more information, see the [AWS CloudShell User Guide](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md").

###### Find a specific AMI

The following example retrieves Windows Server AMIs
that are configured for NitroTPM and UEFI Secure Boot by filtering on the AMI name,
the owner, the platform, and the creation date (year and month).
Output is formatted as a table with columns for the AMI name and
image ID.

```
`Get-EC2Image `
 -Owner amazon `
 -Filter @(
 @{Name = "name"; Values = @("TPM-Windows*")}
 @{Name = "platform"; Values = @("windows")}
 @{Name = "creation-date"; Values = @("`2026`*")}
 ) |
Sort-Object Name |
Format-Table Name, ImageID -AutoSize`
```
