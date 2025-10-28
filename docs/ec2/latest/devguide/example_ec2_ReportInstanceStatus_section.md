# Use `ReportInstanceStatus` with a CLI

The following code examples show how to use `ReportInstanceStatus`.

CLI

**AWS CLI**

**To report status feedback for an instance**

This example command reports status feedback for the specified instance.

Command:

```
`aws ec2 report-instance-status --instances `i-1234567890abcdef0` --status `impaired` --reason-codes `unresponsive``

```

- For API details, see
  [ReportInstanceStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/report-instance-status.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/report-instance-status.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example reports status feedback for the specified instance.**

```
Send-EC2InstanceStatus -Instance i-12345678 -Status impaired -ReasonCode unresponsive

```

- For API details, see
  [ReportInstanceStatus](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example reports status feedback for the specified instance.**

```
Send-EC2InstanceStatus -Instance i-12345678 -Status impaired -ReasonCode unresponsive

```

- For API details, see
  [ReportInstanceStatus](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
