# `AWS-CloseSecurityGroup`

**Description**

This runbook removes all ingress and egress rules from the security group you
specify.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-CloseSecurityGroup "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-CloseSecurityGroup")

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

- SecurityGroupId

Type: String

Description: (Required) The ID of the security group you want to
close.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:DescribeSecurityGroups`
- `ec2:RevokeSecurityGroupEgress`
- `ec2:RevokeSecurityGroupIngress`
  **Document Steps**

- `aws:executeScript` - Removes all ingress and egress rules from
  the security group you specify in the `SecurityGroupId`
  parameter.
