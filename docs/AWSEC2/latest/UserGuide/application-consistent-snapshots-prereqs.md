# Prerequisites to create Windows VSS

based EBS snapshots

You can create VSS based EBS snapshots with Systems Manager Run Command, AWS Backup, or Amazon Data Lifecycle Manager. The following
prerequisites apply for all solutions.

**[System requirements](#vss-sys-reqs "#vss-sys-reqs")**

Ensure that your EC2 Windows instance meets all of the system requirements to create
VSS based snapshots, including supported versions of the Windows operating system, .NET framework,
PowerShell, AWS Tools for Windows PowerShell, and the AWS Systems Manager Agent.

**[IAM permissions](vss-iam-reqs.md "vss-iam-reqs.md")**

The IAM role that's attached to your Amazon EC2 Windows instance must have permission to
create application-consistent snapshots with VSS. To grant the necessary permissions,
you can attach the `AWSEC2VssSnapshotPolicy` managed policy to your
instance profile.

**[VSS components](application-consistent-snapshots-getting-started.md "application-consistent-snapshots-getting-started.md")**

To create application-consistent snapshots on Windows operating systems, the
`AwsVssComponents` package must be installed on the instance. The
package contains an on-instance EC2 VSS Agent that functions as the VSS requester,
and an EC2 VSS provider for EBS volumes.

## System requirements

**Install the Systems Manager Agent**

VSS is orchestrated by the Systems Manager Agent using PowerShell. Ensure that you have
installed SSM Agent version `3.0.502.0` or later on your EC2 instance. If
you are already using an older version of the SSM Agent, update it using Run Command.
For more information, see [Setting up Systems Manager for Amazon EC2 instances](../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md "../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md") and [Working with
SSM Agent on Amazon EC2 instances for Windows Server](../../../systems-manager/latest/userguide/ssm-agent-windows.md "../../../systems-manager/latest/userguide/ssm-agent-windows.md") in the
_AWS Systems Manager User Guide_.

**Amazon EC2 Windows instance requirements**

VSS based EBS snapshots are supported for instances running
Windows Server 2016 and later.

**.NET Framework version**

The `AwsVssComponents` package requires .NET Framework version `4.6`
or later. Windows operating system versions prior to Windows Server 2016 default to an
earlier version of the .NET Framework. If your instance uses an earlier version of the
.NET Framework, you must install version `4.6` or later using Windows Update.

**AWS Tools for Windows PowerShell version**

Ensure that your instance is running AWS Tools for Windows PowerShell version `3.3.48.0` or later.
To check your version, run the following command in the PowerShell terminal on the
instance.

```
`C:\>` Get-AWSPowerShellVersion
```

If you need to update AWS Tools for Windows PowerShell on your instance, see [Installing the AWS Tools for Windows PowerShell](../../../powershell/latest/userguide/pstools-getting-set-up-windows.md "../../../powershell/latest/userguide/pstools-getting-set-up-windows.md") in the _AWS Tools for PowerShell User Guide_.

**Windows PowerShell version**

Ensure that your instance is running Windows PowerShell major version `3`,
`4`, or `5`. To check your version, run the following command
in a PowerShell terminal on the instance.

```
`C:\>` $PSVersionTable.PSVersion
```

**PowerShell language mode**

Ensure that your instance has the PowerShell language mode set to `FullLanguage`.
For more information, see [about_Language_Modes](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_language_modes?view=powershell-7.3 "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_language_modes?view=powershell-7.3") in the Microsoft documentation.
