

# Creating snapshot export tasks
<a name="aurora-export-snapshot.Exporting"></a>

Create snapshot export tasks to export data from your snapshot to an Amazon S3 bucket. You can have up to five concurrent DB snapshot export tasks in progress per AWS account.

**Note**  
Exporting RDS snapshots can take a while depending on your database type and size. The export task first restores and scales the entire database before extracting the data to Amazon S3. The task's progress during this phase displays as **Starting**. When the task switches to exporting data to S3, progress displays as **In progress**.  
The time it takes for the export to complete depends on the data stored in the database. For example, tables with well-distributed numeric primary key or index columns export the fastest. Tables that don't contain a column suitable for partitioning and tables with only one index on a string-based column take longer. This longer export time occurs because the export uses a slower single-threaded process. 

You can export a DB snapshot to Amazon S3 using the AWS Management Console, the AWS CLI, or the RDS API.

If you use a Lambda function to export a snapshot, add the `kms:DescribeKey` action to the Lambda function policy. For more information, see [AWS Lambda permissions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-permissions.html).

## Console
<a name="aurora-export-snapshot.ExportConsole"></a>

The **Export to Amazon S3** console option appears only for snapshots that can be exported to Amazon S3. A snapshot might not be available for export because of the following reasons:
+ The DB engine isn't supported for S3 export.
+ The DB instance version isn't supported for S3 export.
+ S3 export isn't supported in the AWS Region where the snapshot was created.

**To export a DB snapshot**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Snapshots**.

1. From the tabs, choose the type of snapshot that you want to export.

1. In the list of snapshots, choose the snapshot that you want to export.

1. For **Actions**, choose **Export to Amazon S3**.

   The **Export to Amazon S3** window appears.

1. For **Export identifier**, enter a name to identify the export task. This value is also used for the name of the file created in the S3 bucket.

1. Choose the data to be exported:
   + Choose **All** to export all data in the snapshot.
   + Choose **Partial** to export specific parts of the snapshot. To identify which parts of the snapshot to export, enter one or more databases, schemas, or tables for **Identifiers**, separated by spaces.

     Use the following format:

     ```
     {{database}}[.{{schema}}][.{{table}}] {{database2}}[.{{schema2}}][.{{table2}}] ... {{database}}n[.{{schema}}n][.{{table}}n]
     ```

     For example:

     ```
     mydatabase mydatabase2.myschema1 mydatabase2.myschema2.mytable1 mydatabase2.myschema2.mytable2
     ```

1. For **S3 bucket**, choose the bucket to export to. 

   To assign the exported data to a folder path in the S3 bucket, enter the optional path for **S3 prefix**.

1. For **IAM role**, either choose a role that grants you write access to your chosen S3 bucket, or create a new role. 
   + If you created a role by following the steps in [Providing access to an Amazon S3 bucket using an IAM role](aurora-export-snapshot.Setup.md#aurora-export-snapshot.SetupIAMRole), choose that role.
   + If you didn't create a role that grants you write access to your chosen S3 bucket, then choose **Create a new role** to create the role automatically. Next, enter a name for the role in **IAM role name**.

1. For **AWS KMS key**, enter the ARN for the key to use for encrypting the exported data.

1. Choose **Export to Amazon S3**.

## AWS CLI
<a name="aurora-export-snapshot.ExportCLI"></a>

To export a DB snapshot to Amazon S3 using the AWS CLI, use the [start-export-task](https://docs.aws.amazon.com/cli/latest/reference/rds/start-export-task.html) command with the following required options:
+ `--export-task-identifier` 
+ `--source-arn` 
+ `--s3-bucket-name` 
+ `--iam-role-arn` 
+ `--kms-key-id` 

In the following examples, the snapshot export task is named {{my-snapshot-export}}, which exports a snapshot to an S3 bucket named {{amzn-s3-demo-destination-bucket}}.

**Example**  
For Linux, macOS, or Unix:  

```
1. aws rds start-export-task \
2.     --export-task-identifier {{my-snapshot-export}} \
3.     --source-arn arn:aws:rds:{{AWS_Region}}:123456789012:snapshot:{{snapshot-name}} \
4.     --s3-bucket-name {{amzn-s3-demo-destination-bucket}} \
5.     --iam-role-arn {{iam-role}} \
6.     --kms-key-id {{my-key}}
```
For Windows:  

```
1. aws rds start-export-task ^
2.     --export-task-identifier {{my-snapshot-export}} ^
3.     --source-arn arn:aws:rds:{{AWS_Region}}:123456789012:snapshot:{{snapshot-name}} ^
4.     --s3-bucket-name {{amzn-s3-demo-destination-bucket}} ^
5.     --iam-role-arn {{iam-role}} ^
6.     --kms-key-id {{my-key}}
```
Sample output follows.  

```
{
    "Status": "STARTING", 
    "IamRoleArn": "iam-role", 
    "ExportTime": "2019-08-12T01:23:53.109Z", 
    "S3Bucket": "{{amzn-s3-demo-destination-bucket}}", 
    "PercentProgress": 0, 
    "KmsKeyId": "my-key", 
    "ExportTaskIdentifier": "my-snapshot-export", 
    "TotalExtractedDataInGB": 0, 
    "TaskStartTime": "2019-11-13T19:46:00.173Z", 
    "SourceArn": "arn:aws:rds:AWS_Region:123456789012:snapshot:snapshot-name"
}
```
To provide a folder path in the S3 bucket for the snapshot export, include the `--s3-prefix` option in the [start-export-task](https://docs.aws.amazon.com/cli/latest/reference/rds/start-export-task.html) command.

## RDS API
<a name="aurora-export-snapshot.ExportAPI"></a>

To export a DB snapshot to Amazon S3 using the Amazon RDS API, use the [StartExportTask](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StartExportTask.html) operation with the following required parameters:
+ `ExportTaskIdentifier`
+ `SourceArn`
+ `S3BucketName`
+ `IamRoleArn`
+ `KmsKeyId`