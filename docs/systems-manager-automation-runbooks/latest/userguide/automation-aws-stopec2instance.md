# `AWS-StopEC2Instance`

**Description**

Stops one or more Amazon Elastic Compute Cloud (Amazon EC2) instances.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-StopEC2Instance "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-StopEC2Instance")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- InstanceId

Type: StringList

Description: (Required) EC2 instances to stop.
