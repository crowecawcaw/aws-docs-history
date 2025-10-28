# AWS Windows Server license-included

SQL Server AMIs

AWS Windows AMIs with Microsoft SQL Server include one of the
following SQL Server editions. Launching an instance from a Windows AMI
with Microsoft SQL Server enables you to run the instance as a database server.

- SQL Enterprise Edition
- SQL Server Standard
- SQL Server Express
- SQL Server Web
  For more information about running Microsoft SQL Server on EC2, see the [Microsoft SQL Server
  on Amazon EC2 User Guide](../../../sql-server-ec2/latest/userguide/sql-server-on-ec2-overview.md "../../../sql-server-ec2/latest/userguide/sql-server-on-ec2-overview.md").

Each AWS Windows AMIs with Microsoft SQL Server AMI also includes the
following features:

- Automatic Windows and SQL Server updates
- SQL Server Management Studio included
- Preconfigured SQL Server service accounts

## Find Windows Server AMIs with

Microsoft SQL Server

AWS managed AMIs always include the AMI creation date as part of the name.
The best way to ensure that your search returns the AMIs that you're looking for
is to add date filtering for the name. Use one of the following command line options
to find an AMI.

AWS CLI

###### Find the latest SQL AMIs

The following example retrieves a list of the latest Windows Server AMIs
that include Microsoft SQL Server.

```
`aws ssm get-parameters-by-path \
 --path "/aws/service/ami-windows-latest" \
 --recursive \
 --query 'Parameters[*].{Name:Name,Value:Value}' \
 --output text | grep ".*Windows_Server-.*SQL.*" | sort`
```

###### Find a specific AMI

The following example retrieves Windows Server AMIs
with Microsoft SQL Server by filtering on the AMI name,
the owner, the platform, and the creation date (year and month).
Output is formatted as a table with columns for the AMI name
and image ID.

```
`aws ec2 describe-images \
 --owners amazon \
 --filters \
 "Name=name,Values=*SQL*" \
 "Name=platform,Values=windows" \
 "Name=creation-date,Values=`2025-05`*" \
 --query 'Images[].[Name,ImageId]' \
 --output text | sort`
```

PowerShell (recommended)

###### Find the latest SQL AMIs

The following example retrieves a list of the latest Windows Server AMIs
that include Microsoft SQL Server.

```
`Get-SSMLatestEC2Image `
 -Path ami-windows-latest `
 -ImageName *Windows_Server-*SQL* | `
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
with Microsoft SQL Server by filtering on the AMI name, the
owner, the platform, and the creation date (year and month).
Output is formatted as a table with columns for the AMI name and
image ID.

```
`Get-EC2Image `
 -Owner amazon `
 -Filter @(
 @{Name = "name"; Values = @("*SQL*")},
 @{Name = "owner-alias"; Values = @("amazon")},
 @{Name = "platform"; Values = "windows"},
 @{Name = "creation-date"; Values = @("`2025-05`*")}
 ) | `
Sort-Object Name |`
Format-Table Name, ImageID -AutoSize`
```
