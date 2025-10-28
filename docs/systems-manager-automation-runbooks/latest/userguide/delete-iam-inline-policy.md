# `AWS-DeleteIAMInlinePolicy`

**Description**

The `AWS-DeleteIAMInlinePolicy` runbook deletes all AWS Identity and Access Management (IAM)
inline policies attached to the IAM identities you specify.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-DeleteIAMInlinePolicy "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-DeleteIAMInlinePolicy")

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

- IamArns

Type: String

Description: (Required) A comma separated list of ARNs for the IAM
identities you want to delete inline policies from. This list can include
IAM users, groups, or roles.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `iam:DeleteGroupPolicy`
- `iam:DeleteRolePolicy`
- `iam:DeleteUserPolicy`
- `iam:ListGroupPolicies`
- `iam:ListRolePolicies`
- `iam:ListUserPolicies`
  **Document Steps**

- `aws:executeScript` - Deletes the IAM inline policies
  attached to the targeted IAM identities.
