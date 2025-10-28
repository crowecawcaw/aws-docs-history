# `AWS-RestoreDynamoDBTable`

**Description**

The `AWS-RestoreDynamoDBTable` runbook restores the Amazon DynamoDB table
that you specify using point-in-time recovery (PITR).

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-RestoreDynamoDBTable "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-RestoreDynamoDBTable")

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

- EnablePointInTimeRecoverAsNeeded

Type: Boolean

Default: true

Description: (Optional) Determines whether the automation turns on
point-in-time recovery as needed to restore the table.

- GlobalSecondaryIndexOverride

Type: String

Description: (Optional) The new global secondary indexes to replace the
existing secondary indexes for the new table.

- LocalSecondaryIndexOverride

Type: String

Description: (Optional) The new local secondary indexes to replace the
existing secondary indexes for the new table.

- RestoreDateTime

Type: String

Description: (Required) The point-in-time recovery that you want to
restore your table to during the last 35 days. Specify the date and time
using the following format: `DD/MM/YYYY HH:MM:SS`

- SourceTableArn

Type: String

Description: (Required) The ARN of the table that you want to
restore.

- SseSpecificationOverride

Type: String

Description: (Optional) The server-side encryption settings to use for the
new table.

- TargetTableName

Type: String

Description: (Required) The name of the table to restore.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `dynamodb:BatchWriteItem`
- `dynamodb:DeleteItem`
- `dynamodb:DescribeTable`
- `dynamodb:GetItem`
- `dynamodb:PutItem`
- `dynamodb:Query`
- `dynamodb:RestoreTableToPointInTime`
- `dynamodb:Scan`
- `dynamodb:UpdateItem`

**Document Steps**

- `aws:executeScript` - Restores the DynamoDB table that you specify
  in the `TargetTableName` parameter using point-in-time recovery.
