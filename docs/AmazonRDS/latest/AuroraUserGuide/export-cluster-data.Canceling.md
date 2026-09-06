

# Canceling a DB cluster export task
<a name="export-cluster-data.Canceling"></a>

You can cancel a DB cluster export task using the AWS Management Console, the AWS CLI, or the RDS API.

**Note**  
Canceling an export task doesn't remove any data that was exported to Amazon S3. For information about how to delete the data using the console, see [ How do I delete objects from an S3 bucket?](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/delete-objects.html) To delete the data using the CLI, use the [delete-object](https://docs.aws.amazon.com/cli/latest/reference/s3api/delete-object.html) command.

## Console
<a name="export-cluster-data.CancelConsole"></a>

**To cancel a DB cluster export task**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Exports in Amazon S3**.

   DB cluster exports are indicated in the **Source type** column. Export status is displayed in the **Status** column.

1. Choose the export task that you want to cancel.

1. Choose **Cancel**.

1. Choose **Cancel export task** on the confirmation page.

 

## AWS CLI
<a name="export-cluster-data.CancelCLI"></a>

To cancel an export task using the AWS CLI, use the [cancel-export-task](https://docs.aws.amazon.com/cli/latest/reference/rds/cancel-export-task.html) command. The command requires the `--export-task-identifier` option.

**Example**  

```
 1. aws rds cancel-export-task --export-task-identifier my-export
 2. {
 3.     "Status": "CANCELING",
 4.     "S3Prefix": "",
 5.     "S3Bucket": "{{amzn-s3-demo-bucket}}",
 6.     "PercentProgress": 0,
 7.     "KmsKeyId": "arn:aws:kms:{{us-west-2}}:123456789012:key/K7MDENG/bPxRfiCYEXAMPLEKEY",
 8.     "ExportTaskIdentifier": "my-export",
 9.     "IamRoleArn": "arn:aws:iam::123456789012:role/export-to-s3",
10.     "TotalExtractedDataInGB": 0,
11.     "SourceArn": "arn:aws:rds:{{us-west-2}}:123456789012:cluster:export-example-1"
12. }
```

## RDS API
<a name="export-cluster-data.CancelAPI"></a>

To cancel an export task using the Amazon RDS API, use the [CancelExportTask](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CancelExportTask.html) operation with the `ExportTaskIdentifier` parameter.