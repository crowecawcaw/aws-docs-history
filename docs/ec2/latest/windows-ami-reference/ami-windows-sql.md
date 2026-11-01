

# AWS Windows Server license-included SQL Server AMIs
<a name="ami-windows-sql"></a>

AWS Windows AMIs with Microsoft SQL Server include one of the following SQL Server editions. Launching an instance from a Windows AMI with Microsoft SQL Server enables you to run the instance as a database server.
+ SQL Enterprise Edition
+ SQL Server Standard
+ SQL Server Express
+ SQL Server Web

For more information about running Microsoft SQL Server on EC2, see the [Microsoft SQL Server on Amazon EC2 User Guide](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-server-on-ec2-overview.html).

Each AWS Windows AMIs with Microsoft SQL Server AMI also includes the following features:
+ Automatic Windows and SQL Server updates
+ SQL Server Management Studio included
+ Preconfigured SQL Server service accounts

## Find Windows Server AMIs with Microsoft SQL Server
<a name="ami-windows-sql-find"></a>

AWS managed AMIs always include the AMI creation date as part of the name. The best way to ensure that your search returns the AMIs that you're looking for is to add date filtering for the name. Use one of the following command line options to find an AMI.

You can run the following commands from [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html), which comes with the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) and [AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-welcome.html) pre-installed. AWS CloudShell automatically configures your credentials. To run the PowerShell commands, run `pwsh`.

------
#### [ AWS CLI ]

**Find the latest SQL AMIs**  
Use the [get-parameters-by-path](https://docs.aws.amazon.com/cli/latest/reference/ssm/get-parameters-by-path.html) command to retrieve a list of the latest Windows Server AMIs that include Microsoft SQL Server.

```
aws ssm get-parameters-by-path \
    --path "/aws/service/ami-windows-latest" \
    --recursive \
    --query 'Parameters[*].{Name:Name,Value:Value}' \
    --output text | grep ".*Windows_Server-.*SQL.*" | sort
```

**Find a specific AMI**  
Use the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) command to retrieve Windows Server AMIs with Microsoft SQL Server by filtering on the AMI name, the owner, the platform, and the creation date (year and month). Output is formatted as a table with columns for the AMI name and image ID.

```
aws ec2 describe-images \
    --owners amazon \
    --filters \
        "Name=name,Values=*SQL*" \
        "Name=platform,Values=windows" \
        "Name=creation-date,Values={{2026-10}}*" \
    --query 'Images[].[Name,ImageId]' \
    --output text | sort
```

To narrow the results, use more specific values for the `name` filter. The following examples show additional name filters for the `describe-images` command.
+ English, SQL Server 2025 Standard Edition:

  ```
  "Name=name,Values=*English*SQL_2025*Standard*"
  ```
+ Windows Server 2025, English, and SQL Server 2025:

  ```
  "Name=name,Values=*Server-2025-English*SQL_2025*"
  ```

------
#### [ PowerShell ]

**Find the latest SQL AMIs**  
Use the [Get-SSMLatestEC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-SSMLatestEC2Image.html) cmdlet to retrieve a list of the latest Windows Server AMIs that include Microsoft SQL Server.

```
Get-SSMLatestEC2Image `
    -Path ami-windows-latest `
    -ImageName *Windows_Server-*SQL* |
Sort-Object Name
```

**Find a specific AMI**  
Use the [Get-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Image.html) cmdlet to retrieve Windows Server AMIs with Microsoft SQL Server by filtering on the AMI name, the owner, the platform, and the creation date (year and month). Output is formatted as a table with columns for the AMI name and image ID.

```
Get-EC2Image `
    -Owner amazon `
    -Filter @(
        @{Name = "name"; Values = @("*SQL*")}
        @{Name = "platform"; Values = @("windows")}
        @{Name = "creation-date"; Values = @("{{2026-10}}*")}
    ) |
Sort-Object Name |
Format-Table Name, ImageID -AutoSize
```

To narrow the results, use more specific values for the `name` filter. The following examples show additional name filters for the `Get-EC2Image` cmdlet.
+ English, SQL Server 2025 Standard Edition:

  ```
  @{Name = "name"; Values = @("*English*SQL_2025*Standard*")}
  ```
+ Windows Server 2025, English, and SQL Server 2025:

  ```
  @{Name = "name"; Values = @("*Server-2025-English*SQL_2025*")}
  ```

------