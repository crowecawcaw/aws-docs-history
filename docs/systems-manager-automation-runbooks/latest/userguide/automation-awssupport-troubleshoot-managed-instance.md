# `AWSSupport-TroubleshootManagedInstance`

**Description**

The `AWSSupport-TroubleshootManagedInstance` runbook helps you to
determine why an Amazon Elastic Compute Cloud (Amazon EC2) instance does not report as managed by AWS Systems Manager.
This runbook reviews the VPC configuration for the instance including security group
rules, VPC endpoints, network access control list (ACL) rules, and route tables. It
also confirms an AWS Identity and Access Management (IAM) instance profile that contains the required
permissions is attached to the instance.

###### Important

This automation runbook does not evaluate IPv6 rules.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootManagedInstance "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootManagedInstance")

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

Type: String

Description: (Required) The ID of the Amazon EC2 instance that is not reporting
as managed by Systems Manager.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:DescribeAutomationExecutions`
- `ssm:DescribeAutomationStepExecutions`
- `ssm:DescribeInstanceInformation`
- `ssm:DescribeInstanceProperties`
- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `ssm:GetDocument`
- `ssm:ListDocuments`
- `ssm:StartAutomationExecution`
- `iam:ListRoles`
- `iam:GetInstanceProfile`
- `iam:ListAttachedRolePolicies`
- `ec2:DescribeInstances`
- `ec2:DescribeNetworkAcls`
- `ec2:DescribeRouteTables`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeVpcEndpoints`

**Document Steps**

- `aws:executeScript` - Gathers the `PingStatus` of the
  instance.
- `aws:branch` - Branches based on whether the instance is already
  reporting as managed by Systems Manager.
- `aws:executeAwsApi` - Gathers details about the instance
  including the VPC configuration.
- `aws:executeScript` - If applicable, gathers additional details
  related to VPC endpoints that have been deployed to use with Systems Manager, and
  confirms the security groups attached to the VPC endpoint allow inbound
  traffic on TCP port 443 from the instance.
- `aws:executeScript` - Checks whether the route table allows
  traffic to the VPC endpoint or public Systems Manager endpoints.
- `aws:executeScript` - Checks whether the network ACL rules allow
  traffic to the VPC endpoint or public Systems Manager endpoints.
- `aws:executeScript` - Checks whether outbound traffic to the VPC
  endpoint or public Systems Manager endpoints is allowed by the security group
  associated with the instance.
- `aws:executeScript` - Checks if the instance profile attached to
  the instance includes a managed policy that provides the required
  permissions.
- `aws:branch` - Branches based on the operating system of the
  instance.
- `aws:executeScript` - Provides reference to
  `ssmagent-toolkit-linux` shell script.
- `aws:executeScript` - Provides reference to
  `ssmagent-toolkit-windows` PowerShell script.
- `aws:executeScript` - Generates final output for the automation.
- `aws:executeScript` - If the `PingStatus` of the
  instance is `Online` , returns that the instance is already
  managed by Systems Manager.
