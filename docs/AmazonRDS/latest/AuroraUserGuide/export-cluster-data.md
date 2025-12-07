# Monitoring DB cluster export tasks

You can monitor DB cluster exports using the AWS Management Console, the AWS CLI, or the RDS API.

###### To monitor DB cluster exports

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Exports in Amazon S3**.

DB cluster exports are indicated in the **Source type** column. Export status is displayed in
the **Status** column. 3. To view detailed information about a specific DB cluster export, choose the export task.
To monitor DB cluster export tasks using the AWS CLI, use the [describe-export-tasks](../../../cli/latest/reference/rds/describe-export-tasks.md "../../../cli/latest/reference/rds/describe-export-tasks.md") command.

The following example shows how to display current information about all of your DB cluster exports.

```
aws rds describe-export-tasks

{
    "ExportTasks": [
        {
            "Status": "CANCELED",
            "TaskEndTime": "2022-11-01T17:36:46.961Z",
            "S3Prefix": "something",
            "S3Bucket": "`amzn-s3-demo-bucket`",
            "PercentProgress": 0,
            "KmsKeyId": "arn:aws:kms:`us-west-2`:123456789012:key/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "ExportTaskIdentifier": "anewtest",
            "IamRoleArn": "arn:aws:iam::123456789012:role/export-to-s3",
            "TotalExtractedDataInGB": 0,
            "SourceArn": "arn:aws:rds:`us-west-2`:123456789012:cluster:parameter-groups-test"
        },
{
            "Status": "COMPLETE",
            "TaskStartTime": "2022-10-31T20:58:06.998Z",
            "TaskEndTime": "2022-10-31T21:37:28.312Z",
            "WarningMessage": "{\"skippedTables\":[],\"skippedObjectives\":[],\"general\":[{\"reason\":\"FAILED_TO_EXTRACT_TABLES_LIST_FOR_DATABASE\"}]}",
            "S3Prefix": "",
            "S3Bucket": "`amzn-s3-demo-bucket1`",
            "PercentProgress": 100,
            "KmsKeyId": "arn:aws:kms:`us-west-2`:123456789012:key/2Zp9Utk/h3yCo8nvbEXAMPLEKEY",
            "ExportTaskIdentifier": "thursday-events-test",
            "IamRoleArn": "arn:aws:iam::123456789012:role/export-to-s3",
            "TotalExtractedDataInGB": 263,
            "SourceArn": "arn:aws:rds:`us-west-2`:123456789012:cluster:example-1-2019-10-31-06-44"
        },
        {
            "Status": "FAILED",
            "TaskEndTime": "2022-10-31T02:12:36.409Z",
            "FailureCause": "The S3 bucket `amzn-s3-demo-bucket2` isn't located in the current AWS Region. Please, review your S3 bucket name and retry the export.",
            "S3Prefix": "",
            "S3Bucket": "`amzn-s3-demo-bucket2`",
            "PercentProgress": 0,
            "KmsKeyId": "arn:aws:kms:`us-west-2`:123456789012:key/2Zp9Utk/h3yCo8nvbEXAMPLEKEY",
            "ExportTaskIdentifier": "wednesday-afternoon-test",
            "IamRoleArn": "arn:aws:iam::123456789012:role/export-to-s3",
            "TotalExtractedDataInGB": 0,
            "SourceArn": "arn:aws:rds:`us-west-2`:123456789012:cluster:example-1-2019-10-30-06-45"
        }
    ]
}
```

To display information about a specific export task, include the `--export-task-identifier` option with
the `describe-export-tasks` command. To filter the output, include the `--Filters` option. For
more options, see the [describe-export-tasks](../../../cli/latest/reference/rds/describe-export-tasks.md "../../../cli/latest/reference/rds/describe-export-tasks.md")
command.

To display information about DB cluster exports using the Amazon RDS API, use the [DescribeExportTasks](../APIReference/API_DescribeExportTasks.md "../APIReference/API_DescribeExportTasks.md") operation.

To track completion of the export workflow or to initiate another workflow, you can subscribe to Amazon Simple Notification Service topics. For more
information on Amazon SNS, see [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md").
