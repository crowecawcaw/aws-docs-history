# Monitoring snapshot exports for Amazon RDS

You can monitor DB snapshot exports using the AWS Management Console, the AWS CLI, or the RDS API.

###### To monitor DB snapshot exports

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Snapshots**.
3. To view the list of snapshot exports, choose the **Exports in Amazon
   S3** tab.
4. To view information about a specific snapshot export, choose the export task.
   To monitor DB snapshot exports using the AWS CLI, use the [describe-export-tasks](../../../cli/latest/reference/rds/describe-export-tasks.md "../../../cli/latest/reference/rds/describe-export-tasks.md") command.

The following example shows how to display current information about all of your snapshot
exports.

```
aws rds describe-export-tasks

{
    "ExportTasks": [
        {
            "Status": "CANCELED",
            "TaskEndTime": "2019-11-01T17:36:46.961Z",
            "S3Prefix": "something",
            "ExportTime": "2019-10-24T20:23:48.364Z",
            "S3Bucket": "`amzn-s3-demo-bucket`",
            "PercentProgress": 0,
            "KmsKeyId": "arn:aws:kms:`AWS_Region`:123456789012:key/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "ExportTaskIdentifier": "anewtest",
            "IamRoleArn": "arn:aws:iam::123456789012:role/export-to-s3",
            "TotalExtractedDataInGB": 0,
            "TaskStartTime": "2019-10-25T19:10:58.885Z",
            "SourceArn": "arn:aws:rds:`AWS_Region`:123456789012:snapshot:parameter-groups-test"
        },
{
            "Status": "COMPLETE",
            "TaskEndTime": "2019-10-31T21:37:28.312Z",
            "WarningMessage": "{\"skippedTables\":[],\"skippedObjectives\":[],\"general\":[{\"reason\":\"FAILED_TO_EXTRACT_TABLES_LIST_FOR_DATABASE\"}]}",
            "S3Prefix": "",
            "ExportTime": "2019-10-31T06:44:53.452Z",
            "S3Bucket": "`amzn-s3-demo-bucket1`",
            "PercentProgress": 100,
            "KmsKeyId": "arn:aws:kms:`AWS_Region`:123456789012:key/2Zp9Utk/h3yCo8nvbEXAMPLEKEY",
            "ExportTaskIdentifier": "thursday-events-test",
            "IamRoleArn": "arn:aws:iam::123456789012:role/export-to-s3",
            "TotalExtractedDataInGB": 263,
            "TaskStartTime": "2019-10-31T20:58:06.998Z",
            "SourceArn": "arn:aws:rds:`AWS_Region`:123456789012:snapshot:rds:example-1-2019-10-31-06-44"
        },
        {
            "Status": "FAILED",
            "TaskEndTime": "2019-10-31T02:12:36.409Z",
            "FailureCause": "The S3 bucket edgcuc-export isn't located in the current AWS Region. Please, review your S3 bucket name and retry the export.",
            "S3Prefix": "",
            "ExportTime": "2019-10-30T06:45:04.526Z",
            "S3Bucket": "`amzn-s3-demo-bucket2`",
            "PercentProgress": 0,
            "KmsKeyId": "arn:aws:kms:`AWS_Region`:123456789012:key/2Zp9Utk/h3yCo8nvbEXAMPLEKEY",
            "ExportTaskIdentifier": "wednesday-afternoon-test",
            "IamRoleArn": "arn:aws:iam::123456789012:role/export-to-s3",
            "TotalExtractedDataInGB": 0,
            "TaskStartTime": "2019-10-30T22:43:40.034Z",
            "SourceArn": "arn:aws:rds:`AWS_Region`:123456789012:snapshot:rds:example-1-2019-10-30-06-45"
        }
    ]
}
```

To display information about a specific snapshot export, include the
`--export-task-identifier` option with the
`describe-export-tasks` command. To filter the output,
include the `--Filters` option. For more options, see the [describe-export-tasks](../../../cli/latest/reference/rds/describe-export-tasks.md "../../../cli/latest/reference/rds/describe-export-tasks.md") command.

To display information about DB snapshot exports using the Amazon RDS API, use the [DescribeExportTasks](../APIReference/API_DescribeExportTasks.md "../APIReference/API_DescribeExportTasks.md")
operation.

To track completion of the export workflow or to initiate another workflow, you can subscribe to Amazon Simple Notification Service topics. For more
information on Amazon SNS, see [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md").
