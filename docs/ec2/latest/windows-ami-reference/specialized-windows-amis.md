# Specialized AWS Windows AMIs

In addition to its standard operating system version AMIs, Amazon creates
the following types of specialized AWS Windows AMIs:

**SQL Server license-included AMIs**

Launching an instance from a Windows AMI with Microsoft SQL Server
enables you to run the instance as a database server. For more
information, see [AWS Windows Server license-included
SQL Server AMIs](ami-windows-sql.md "ami-windows-sql.md").

**STIG Hardened AMIs**

STIG Hardened EC2 Windows Server AMIs are pre-configured with over
160 required security settings to help ensure that the instances that you
launch follow the latest guidelines for STIG compliance. For more
information, see [STIG Hardened AWS Windows Server AMIs](ami-windows-stig.md "ami-windows-stig.md").

**NitroTPM enabled AMIs**

Amazon creates a set of AMIs that are pre-configured with NitroTPM and UEFI Secure Boot
requirements. For more information, see [AWS Windows Server NitroTPM enabled AMIs](ami-windows-tpm.md "ami-windows-tpm.md").

You can also create your own customized AMI from one of the AWS Windows AMIs with EC2 Image Builder.
For more information, see the [EC2 Image Builder
User Guide](../../../imagebuilder/latest/userguide.md "../../../imagebuilder/latest/userguide.md").

We recommend PowerShell for the command line examples in this section. To install PowerShell in your
environment, see the [Installation](../../../powershell/v4/userguide/pstools-getting-set-up.md "../../../powershell/v4/userguide/pstools-getting-set-up.md") page in the
_AWS Tools for PowerShell (version 4) User Guide_.

###### Note

Not all AMIs are available in all Regions.

## Find an AWS Windows AMI

Each of the specialized AMI pages linked above has its own filtered search examples, as follows:

- [Find Windows Server AMIs with
  Microsoft SQL Server](ami-windows-sql.md#ami-windows-sql-find "ami-windows-sql.md#ami-windows-sql-find")
- [Find a STIG Hardened AMI](ami-windows-stig.md#find-windows-stig-ami "ami-windows-stig.md#find-windows-stig-ami")
- [Find Windows Server AMIs configured with
  NitroTPM and UEFI Secure Boot](ami-windows-tpm.md#ami-windows-tpm-find "ami-windows-tpm.md#ami-windows-tpm-find")

You can also search for the latest Windows AMIs that include the EC2Launch v2 agent, as shown
in the following PowerShell example:

```
Get-SSMLatestEC2Image `
    -Path ami-windows-latest `
    -ImageName EC2LaunchV2-Windows* | `
Sort-Object Name

```

###### Note

If this command doesn't run in your environment, you might be missing a PowerShell module. For
more information about this command, see [Get-SSMLatestEC2Image Cmdlet](../../../powershell/v4/reference/items/Get-SSMLatestEC2Image.md "../../../powershell/v4/reference/items/Get-SSMLatestEC2Image.md").

Alternatively, you can use the [CloudShell console](https://console.aws.amazon.com/cloudshell/home "https://console.aws.amazon.com/cloudshell/home")
and run `pwsh` to bring up a PowerShell prompt that already has all of the AWS tools installed.
For more information, see the [AWS CloudShell User Guide](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md").

### Find an AWS Windows AMI in a

specific language

The following language-specific AWS Windows AMIs are included in the monthly
release:

- English
- Japanese
- Chinese
- Korean
- Czech
- Dutch
- French
- German
- Hungarian
- Italian
- Polish
- Russian
- Portuguese
- Spanish
- Swedish
- Turkish

The following example uses PowerShell to search for the latest English language
AWS Windows AMIs:

```
Get-SSMLatestEC2Image `
    -Path ami-windows-latest `
    -ImageName *Windows_Server-*English* | `
Sort-Object Name

```

###### Note

If this command doesn't run in your environment, you might be missing a PowerShell module. For
more information about this command, see [Get-SSMLatestEC2Image Cmdlet](../../../powershell/v4/reference/items/Get-SSMLatestEC2Image.md "../../../powershell/v4/reference/items/Get-SSMLatestEC2Image.md").

Alternatively, you can use the [CloudShell console](https://console.aws.amazon.com/cloudshell/home "https://console.aws.amazon.com/cloudshell/home")
and run `pwsh` to bring up a PowerShell prompt that already has all of the AWS tools installed.
For more information, see the [AWS CloudShell User Guide](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md").
