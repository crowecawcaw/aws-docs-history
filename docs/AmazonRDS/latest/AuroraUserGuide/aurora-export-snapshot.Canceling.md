

# Canceling a snapshot export task
<a name="aurora-export-snapshot.Canceling"></a>

You can cancel a DB snapshot export task using the AWS Management Console, the AWS CLI, or the RDS API.

**Note**  
Canceling a snapshot export task doesn't remove any data that was exported to Amazon S3. For information about how to delete the data using the console, see [ How do I delete objects from an S3 bucket?](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/delete-objects.html) To delete the data using the CLI, use the [delete-object](https://docs.aws.amazon.com/cli/latest/reference/s3api/delete-object.html) command.

## Console
<a name="aurora-export-snapshot.CancelConsole"></a>

**To cancel a snapshot export task**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Exports in Amazon S3**.

   DB snapshot exports are indicated in the **Source type** column. Export status is displayed in the **Status** column.

1. Choose the snapshot export task that you want to cancel.

1. Choose **Cancel**.

1. Choose **Cancel export task** on the confirmation page.

 

## AWS CLI
<a name="aurora-export-snapshot.CancelCLI"></a>

To cancel a snapshot export task using the AWS CLI, use the [cancel-export-task](https://docs.aws.amazon.com/cli/latest/reference/rds/cancel-export-task.html) command. The command requires the `--export-task-identifier` option.

**Example**  

```
 1. aws rds cancel-export-task --export-task-identifier my_export
 2. {
 3.     "Status": "CANCELING", 
 4.     "S3Prefix": "", 
 5.     "ExportTime": "2019-08-12T01:23:53.109Z", 
 6.     "S3Bucket": "{{amzn-s3-demo-bucket}}", 
 7.     "PercentProgress": 0, 
 8.     "KmsKeyId": "arn:aws:kms:{{AWS_Region}}:123456789012:key/K7MDENG/bPxRfiCYEXAMPLEKEY", 
 9.     "ExportTaskIdentifier": "my_export", 
10.     "IamRoleArn": "arn:aws:iam::123456789012:role/export-to-s3", 
11.     "TotalExtractedDataInGB": 0, 
12.     "TaskStartTime": "2019-11-13T19:46:00.173Z", 
13.     "SourceArn": "arn:aws:rds:{{AWS_Region}}:123456789012:snapshot:export-example-1"
14. }
```

## RDS API
<a name="aurora-export-snapshot.CancelAPI"></a>

To cancel a snapshot export task using the Amazon RDS API, use the [CancelExportTask](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CancelExportTask.html) operation with the `ExportTaskIdentifier` parameter.