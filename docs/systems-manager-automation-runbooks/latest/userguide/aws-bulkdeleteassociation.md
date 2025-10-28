# `AWS-BulkDeleteAssociation`

**Description**

The `AWS-BulkDeleteAssociation` runbook helps you to delete up to 50
Systems Manager State Manager associations at a time.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-BulkDeleteAssociation "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-BulkDeleteAssociation")

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

- AssociationIds

Type: StringList

Description: (Required) A comma-separated list of the IDs of the
associations you want to delete.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:DeleteAssociation`

**Document Steps**

- `aws:executeScript` - Deletes the associations you specify in the
  `AssociationIds` parameter.
