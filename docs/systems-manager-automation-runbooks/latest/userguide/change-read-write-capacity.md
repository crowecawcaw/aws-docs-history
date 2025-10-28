# `AWS-ChangeDDBRWCapacityMode`

**Description**

The `AWS-ChangeDDBRWCapacityMode` runbook changes the read/write
capacity mode for one or more Amazon DynamoDB (DynamoDB) tables to either on-demand mode, or
provisioned mode.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-ChangeDDBRWCapacityMode "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-ChangeDDBRWCapacityMode")

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

- CapacityMode

Type: String

Valid values: PROVISIONED | PAY_PER_REQUEST

Description: (Required) The desired read/write capacity mode. When
switching from on-demand(pay-per-request) to provisioned capacity, initial
provisioned capacity values must be set. The initial provisioned capacity
values are estimated based on the consumed read and write capacity of your
table and global secondary indexes over the past 30 minutes.

- ReadCapacityUnits

Type: Integer

Default: 0

Description: (Optional) The maximum number of strongly consistent reads
consumed per second before DynamoDB returns a throttling exception.

- TableNames

Type: String

Description: (Required) Comma separated list of DynamoDB table names to
change the read/write capacity mode for..

- WriteCapacityUnits

Type: Integer

Default: 0

Description: (Optional) The maximum number of writes consumed per second
before DynamoDB returns a throttling exception.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `dynamodb:DescribeTable`
- `dynamodb:UpdateTable`
  **Document Steps**

- `aws:executeScript` - Changes the read/write capacity mode for
  the DynamoDB tables specified in the `TableNames` parameter.
  **Outputs**

ChangeDDBRWCapacityMode.SuccessesTables - List of DynamoDB table names where the
capacity mode was successfully changed

ChangeDDBRWCapacityMode.FailedTables - Maplist of DynamoDB table names where changing
the capacity mode failed and the reason for the failure.
