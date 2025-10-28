# `AWS-CreateEncryptedRdsSnapshot`

**Description**

The `AWS-CreateEncryptedRdsSnapshot` runbook creates an encrypted
snapshot from an unencrypted Amazon Relational Database Service (Amazon RDS) instance.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-CreateEncryptedRdsSnapshot "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-CreateEncryptedRdsSnapshot")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Databases

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- DBInstanceIdentifier

Type: String

Description: (Required) The ID of the Amazon RDS instance you want to create a
snapshot of.

- DBSnapshotIdentifier

Type: String

Description: (Optional) The name template for the Amazon RDS snapshot. The
default name template is
`DBInstanceIdentifier-yyyymmddhhmmss`.

- EncryptedDBSnapshotIdentifier

Type: String

Description: (Optional) The name for the encrypted snapshot. The default
name is the value you specify for the `DBSnapshotIdentifier`
parameter appended with `-encrypted`.

- InstanceTags

Type: String

Description: (Optional) Tags to add to the DB instance. (Example:
Key=tagKey1,Value=tagValue1;Key=tagKey2,Value=tagValue2)'

- KmsKeyId

Type: String

Default: `alias/aws/rds`

Description: (Optional) The ARN, key ID, or the key alias of the of the
customer managed key you want to use to encrypt the snapshot.

- SnapshotTags

Type: String

Description: (Optional) Tags to add to the snapshot. (Example:
Key=tagKey1,Value=tagValue1;Key=tagKey2,Value=tagValue2)'
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `rds:AddTagsToResource`
- `rds:CopyDBSnapshot`
- `rds:CreateDBSnapshot`
- `rds:DeleteDBSnapshot`
- `rds:DescribeDBSnapshots`
  **Document Steps**

- `aws:executeScript` - Creates a snapshot of the DB instance you
  specify in the `DBInstanceIdentifier` parameter.
- `aws:executeScript` - Verifies the snapshot created in the
  previous step exists and is `available`.
- `aws:executeScript` - Copies the previously created snapshot to
  an encrypted snapshot.
- `aws:executeScript` - Verifies the encrypted snapshot created
  in the previous step exists.
  **Outputs**

CopyRdsSnapshotToEncryptedRdsSnapshot.EncryptedSnapshotId - The ID of the
encrypted Amazon RDS snapshot.
