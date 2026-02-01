# Canceling a snapshot export task

You can cancel a DB snapshot export task using the AWS Management Console, the AWS CLI, or the RDS
API.

###### Note

Canceling a snapshot export task doesn't remove any data that was exported to Amazon S3. For information about how to delete the
data using the console, see [How do I
delete objects from an S3 bucket?](../../../AmazonS3/latest/user-guide/delete-objects.md "../../../AmazonS3/latest/user-guide/delete-objects.md") To delete the data using the CLI, use the [delete-object](../../../cli/latest/reference/s3api/delete-object.md "../../../cli/latest/reference/s3api/delete-object.md") command.

###### To cancel a snapshot export task

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Exports in Amazon S3**.

DB snapshot exports are indicated in the **Source type** column. Export status is displayed
in the **Status** column. 3. Choose the snapshot export task that you want to cancel. 4. Choose **Cancel**. 5. Choose **Cancel export task** on the confirmation page.

To cancel a snapshot export task using the AWS CLI, use the [cancel-export-task](../../../cli/latest/reference/rds/cancel-export-task.md "../../../cli/latest/reference/rds/cancel-export-task.md")
command. The command requires the `--export-task-identifier`
option.

```
aws rds cancel-export-task --export-task-identifier my_export
{
    "Status": "CANCELING",
    "S3Prefix": "",
    "ExportTime": "2019-08-12T01:23:53.109Z",
    "S3Bucket": "`amzn-s3-demo-bucket`",
    "PercentProgress": 0,
    "KmsKeyId": "arn:aws:kms:`AWS_Region`:123456789012:key/K7MDENG/bPxRfiCYEXAMPLEKEY",
    "ExportTaskIdentifier": "my_export",
    "IamRoleArn": "arn:aws:iam::123456789012:role/export-to-s3",
    "TotalExtractedDataInGB": 0,
    "TaskStartTime": "2019-11-13T19:46:00.173Z",
    "SourceArn": "arn:aws:rds:`AWS_Region`:123456789012:snapshot:export-example-1"
}
```

To cancel a snapshot export task using the Amazon RDS API, use the [CancelExportTask](../APIReference/API_CancelExportTask.md "../APIReference/API_CancelExportTask.md")
operation with the `ExportTaskIdentifier` parameter.
