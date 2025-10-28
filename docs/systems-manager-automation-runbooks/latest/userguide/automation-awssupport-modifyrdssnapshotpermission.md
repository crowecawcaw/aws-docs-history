# `AWSSupport-ModifyRDSSnapshotPermission`

**Description**

The `AWSSupport-ModifyRDSSnapshotPermission` runbook helps you modify
permissions for multiple Amazon Relational Database Service (Amazon RDS) snapshots. Using this runbook, you can
make snapshots `Public` or `Private` and share them with other
AWS accounts. Snapshots encrypted with a default KMS key can't be shared with
other accounts using this runbook.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ModifyRDSSnapshotPermission "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ModifyRDSSnapshotPermission")

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

- AccountIds

Type: StringList

Default: none

Description: (Optional) The IDs of the accounts you want to share
snapshots with. This parameter is required if you enter `No` for
the value of the `Private` parameter.

- AccountPermissionOperation

Type: String

Valid values: add | remove

Default: none

Description: (Optional) The type of operation to perform.

- Private

Type: String

Valid values: Yes | No

Description: (Required) Enter `No` for the value if you want
to share snapshots with specific accounts.

- SnapshotIdentifiers

Type: StringList

Description: (Required) The names of the Amazon RDS snapshots whose permission
you want to modify.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `rds:DescribeDBSnapshots`
- `rds:ModifyDBSnapshotAttribute`

**Document Steps**

1. `aws:executeScript` - Verifies the IDs of the snapshots provided
   in the `SnapshotIdentifiers` parameter. After verifying the IDs,
   the script checks for encrypted snapshots and outputs a list if any are
   found.
2. `aws:branch` - Branches the automation based on the value you
   enter for the `Private` parameter.
3. `aws:executeScript` - Modifies permissions of the snapshots
   specified to share it with the accounts specified.
4. `aws:executeScript` - Modifies permissions of the snapshots to
   change them from `Public` to `Private` .

**Outputs**

ValidateSnapshots.EncryptedSnapshots

SharewithOtherAccounts.Result

MakePrivate.Result

MakePrivate.Commands
