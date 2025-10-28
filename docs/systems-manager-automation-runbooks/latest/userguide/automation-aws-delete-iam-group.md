# `AWSConfigRemediation-DeleteUnusedIAMGroup`

**Description**

The `AWSConfigRemediation-DeleteUnusedIAMGroup` runbook deletes an
IAM group that does not contain any users.

The `AWSConfigRemediation-DeleteUnusedIAMGroup` runbook deletes an
IAM group that does not contain any users.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DeleteUnusedIAMGroup "https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DeleteUnusedIAMGroup")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf.

- GroupName

Type: String

Description: (Required) The name of the IAM group that you want to
delete.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `iam:DeleteGroup`
- `iam:DeleteGroupPolicy`
- `iam:DetachGroupPolicy`

**Document Steps**

- `aws:executeScript` - Removes managed and inline IAM policies
  attached to the target IAM group, and then deletes the IAM group.
