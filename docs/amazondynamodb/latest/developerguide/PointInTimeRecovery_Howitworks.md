# Enable point-in-time recovery in

DynamoDB

Amazon DynamoDB point-in-time recovery (PITR) provides automatic backups of your DynamoDB table
data. This section provides an overview of how the process works in DynamoDB.

###### Note

DynamoDB charges for PITR based on the size of each DynamoDB table, including table data and
local secondary indexes. Changing the recovery window (for example, from 35 days to 1
day) doesn't reduce the price. The cost remains the same regardless of the recovery
period you choose. The configured maximum recovery period doesn't impact the price
you're charged for turning on PITR. To determine your backup charges, DynamoDB continuously
monitors the size of the tables that have PITR turned on. You're billed for PITR usage
until you turn off PITR for each table.

###### Topics

- [Enabling point-in-time recovery](#howitworks_enabling "#howitworks_enabling")
- [Enable PITR (console)](#howitworks-enable-pitr-console "#howitworks-enable-pitr-console")
- [Enable PITR (AWS CLI)](#howitworks-enable-pitr-cli "#howitworks-enable-pitr-cli")
- [Enable PITR (CloudFormation)](#howitworks-enable-pitr-cfn "#howitworks-enable-pitr-cfn")
- [Enable PITR (API)](#howitworks-enable-pitr-api "#howitworks-enable-pitr-api")
- [Recovery Period](#howitworks-pitr-recovery-period "#howitworks-pitr-recovery-period")
- [Edit PITR](#howitworks-pitr-editing "#howitworks-pitr-editing")
- [Delete a table with PITR
  enabled](#howitworks-pitr-deleting-table "#howitworks-pitr-deleting-table")

## Enabling point-in-time recovery

You can enable point-in-time recovery using the AWS Management Console, AWS Command Line Interface (AWS CLI), or the
DynamoDB API. When enabled, point-in-time recovery provides continuous backups until you
explicitly turn it off.

After you enable point-in-time recovery, you can restore to any point in time within
`EarliestRestorableDateTime` and `LatestRestorableDateTime`.
`LatestRestorableDateTime` is typically five minutes before the current
time. For more information, see [Restoring a DynamoDB table to a point in
time](PointInTimeRecovery.md "PointInTimeRecovery.md").

###### Note

The point-in-time recovery process always restores to a new table.

## Enable PITR (console)

###### To enable PITR using the DynamoDB console

1. Navigate to the DynamoDB console.
2. Choose **Tables** from the left navigation and select your
   DynamoDB table.
3. From the **Backups** tab, for the **Point in Time
   Recovery** option, choose **Edit**.
4. Choose **Turn on point-in-time recovery**.
5. Choose a value between 1 and 35 for your backup recovery period. This
   indicates the maximum time period for which the continuous backup is
   recoverable.

## Enable PITR (AWS CLI)

###### Note

If you receive errors when running AWS CLI commands, see [Troubleshoot AWS CLI errors](../../../cli/latest/userguide/cli-chap-troubleshooting.md "../../../cli/latest/userguide/cli-chap-troubleshooting.md"). Make sure you're using the most recent AWS CLI
version.

Run the [update-continuous-backups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-continuous-backups.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-continuous-backups.html") command with the
**point-in-time-recovery-specification** setting turned on:

```
aws dynamodb update-continuous-backups \
--table-name Music \
--point-in-time-recovery-specification PointInTimeRecoveryEnabled=true,RecoveryPeriodInDays=35
```

## Enable PITR (CloudFormation)

Use the [AWS::DynamoDB::Table](../../../AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.md") resource with the
`PointInTimeRecoverySpecification` property turned on:

```
Resources:
  iotCatalog:
    Type: AWS::DynamoDB::Table
      Properties:
      ...
      PointInTimeRecoverySpecification:
        PointInTimeRecoveryEnabled: true
        RecoveryPeriodInDays: 35
```

**Request syntax example:**

```
{
   "PointInTimeRecoverySpecification": {
      "PointInTimeRecoveryEnabled": boolean,
      "RecoveryPeriodInDays: number
   },
   "TableName": "string"
}
```

## Enable PITR (API)

Run the [UpdateContinuousBackups](../APIReference/API_UpdateContinuousBackups.md "../APIReference/API_UpdateContinuousBackups.md") API operation with the
`PointInTimeRecoverySpecification` parameter turned on.

**Request syntax example:**

```
{
   "PointInTimeRecoverySpecification": {
      "PointInTimeRecoveryEnabled": boolean,
      "RecoveryPeriodInDays" : number
   },
   "TableName": "string"
}
```

**Response syntax example:**

```
{
   "ContinuousBackupsDescription": {
      "ContinuousBackupsStatus": "string",
      "PointInTimeRecoveryDescription": {
         "PointInTimeRecoveryStatus": "string",
         "EarliestRestorableDateTime": number,
         "RecoveryPeriodInDays": number,
         "LatestRestorableDateTime": number
      }
   }
}
```

**Python**

```
import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.update_continuous_backups(
    TableName=<table_name>,
    PointInTimeRecoverySpecification={
        'PointInTimeRecoveryEnabled': True,
        'RecoveryPeriodInDays': 35
    }
)
```

## Recovery Period

You can set the recovery period for continuous backups to be any number between 1 and 35 days. This `RecoveryPeriodInDays` determines the time period for which your continuous backups are maintained. For example, if you set this value to be 30 days, you'll only have the ability to restore your table to any point in time from the past 30 days.

###### Note

DynamoDB charges for PITR based on the size of each DynamoDB table, including table data and local secondary indexes. The configured maximum recovery period doesn't impact the price you're charged for turning on PITR. For details on pricing, see [DynamoDB pricing](https://aws.amazon.com/dynamodb/pricing/on-demand/ "https://aws.amazon.com/dynamodb/pricing/on-demand/").

## Edit PITR

You can edit the PITR setting on your table and change the recovery period. If you
change the recovery period and increase it to a value higher than previously set, your
`EarliestRestorePoint` will not change immediately. Since the recovery
period is a rolling window, DynamoDB will continue to take automatic backups until the new
increased period reached. If you change the recovery period and decrease it to a value
lower than previously set, your `EarliestRestorePoint` will immediately
decrease to match you recovery period, and any continuous backups that fall outside of
the new set value will not be recoverable.

## Delete a table with PITR

enabled

When you delete a table that has point-in-time recovery enabled, DynamoDB automatically
creates a backup snapshot called a _system backup_ and retains it for
35 days (at no additional cost). You can use the system backup to restore the deleted
table to the state it was in before deletion. All system backups follow a standard
naming convention of
`table-name``$DeletedTableBackup`.

###### Note

Once a table with point-in-time recovery enabled is deleted, you can use system
backup to restore that table to a single point in time. The system backup will be
created upon table deletion, and is a snapshot of the table right before the table
is deleted.
