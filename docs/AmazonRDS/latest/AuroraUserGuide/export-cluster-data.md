# Creating DB cluster export tasks

Create export tasks to export data from your Aurora DB cluster to an Amazon S3 bucket. You can have up to five concurrent DB cluster export tasks in progress per AWS account.

###### Note

Exporting DB cluster data can take a while depending on your database type and size. The export task first clones and
scales the entire database before extracting the data to Amazon S3. The task's progress during this phase displays as
**Starting**. When the task switches to exporting data to S3, progress displays as **In
progress**.

The time it takes for the export to complete depends on the data stored in the database. For example, tables with
well-distributed numeric primary key or index columns export the fastest. Tables that don't contain a column suitable
for partitioning and tables with only one index on a string-based column take longer because the export uses a slower
single-threaded process.

You can export DB cluster data to Amazon S3 using the AWS Management Console, the AWS CLI, or the RDS API.

If you use a Lambda function to export the DB cluster data, add the `kms:DescribeKey` action to the Lambda function
policy. For more information, see [AWS Lambda
permissions](../../../lambda/latest/dg/lambda-permissions.md "../../../lambda/latest/dg/lambda-permissions.md").

The **Export to Amazon S3** console option appears only for DB clusters that can be exported to Amazon S3. A DB
cluster might not be available for export because of the following reasons:

- The DB engine isn't supported for S3 export.
- The DB cluster version isn't supported for S3 export.
- S3 export isn't supported in the AWS Region where the DB cluster was created.

###### To export DB cluster data

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the DB cluster whose data you want to export.
4. For **Actions**, choose **Export to Amazon S3**.

The **Export to Amazon S3** window appears. 5. For **Export identifier**, enter a name to identify the export task. This value is also used
for the name of the file created in the S3 bucket. 6. Choose the data to be exported:

    * Choose **All** to export all data in the DB cluster.
    * Choose **Partial** to export specific parts of the DB cluster. To identify which
     parts of the cluster to export, enter one or more databases, schemas, or tables for
     **Identifiers**, separated by spaces.


    Use the following format:



    ```
    `database`[.`schema`][.`table`] `database2`[.`schema2`][.`table2`] ... `database`*n*[.`schema`*n*][.`table`*n*]
    ```

    For example:



    ```
    mydatabase mydatabase2.myschema1 mydatabase2.myschema2.mytable1 mydatabase2.myschema2.mytable2
    ```

7. For **S3 bucket**, choose the bucket to export to.

To assign the exported data to a folder path in the S3 bucket, enter the optional path for **S3
prefix**. 8. For **IAM role**, either choose a role that grants you write access to your chosen S3 bucket,
or create a new role.

    * If you created a role by following the steps in [Providing access to an Amazon S3 bucket using an IAM role](export-cluster-data.md#export-cluster-data.SetupIAMRole "export-cluster-data.md#export-cluster-data.SetupIAMRole"), choose that role.
    * If you didn't create a role that grants you write access to your chosen S3 bucket, then choose
     **Create a new role** to create the role automatically. Next, enter a name for the
     role in **IAM role name**.

9. For **KMS key**, enter the ARN for the key to use for encrypting the exported data.
10. Choose **Export to Amazon S3**.
    To export DB cluster data to Amazon S3 using the AWS CLI, use the [start-export-task](../../../cli/latest/reference/rds/start-export-task.md "../../../cli/latest/reference/rds/start-export-task.md") command with the following required options:

- `--export-task-identifier`
- `--source-arn` – the Amazon Resource Name (ARN) of the DB cluster
- `--s3-bucket-name`
- `--iam-role-arn`
- `--kms-key-id`
  In the following examples, the export task is named `my-cluster-export`, which exports the
  data to an S3 bucket named `amzn-s3-demo-destination-bucket`.

###### Example

For Linux, macOS, or Unix:

```
aws rds start-export-task \
    --export-task-identifier `my-cluster-export` \
    --source-arn arn:aws:rds:`us-west-2`:123456789012:cluster:`my-cluster` \
    --s3-bucket-name `amzn-s3-demo-destination-bucket` \
    --iam-role-arn `iam-role` \
    --kms-key-id `my-key`
```

For Windows:

```
aws rds start-export-task ^
    --export-task-identifier `my-DB-cluster-export` ^
    --source-arn arn:aws:rds:`us-west-2`:123456789012:cluster:`my-cluster` ^
    --s3-bucket-name `amzn-s3-demo-destination-bucket` ^
    --iam-role-arn `iam-role` ^
    --kms-key-id `my-key`
```

Sample output follows.

```
{
    "ExportTaskIdentifier": "my-cluster-export",
    "SourceArn": "arn:aws:rds:us-west-2:123456789012:cluster:my-cluster",
    "S3Bucket": "`amzn-s3-demo-destination-bucket`",
    "IamRoleArn": "arn:aws:iam:123456789012:role/ExportTest",
    "KmsKeyId": "my-key",
    "Status": "STARTING",
    "PercentProgress": 0,
    "TotalExtractedDataInGB": 0,
}
```

To provide a folder path in the S3 bucket for the DB cluster export, include the `--s3-prefix` option
in the [start-export-task](../../../cli/latest/reference/rds/start-export-task.md "../../../cli/latest/reference/rds/start-export-task.md") command.

To export DB cluster data to Amazon S3 using the Amazon RDS API, use the [StartExportTask](../APIReference/API_StartExportTask.md "../APIReference/API_StartExportTask.md") operation with the following required parameters:

- `ExportTaskIdentifier`
- `SourceArn` – the ARN of the DB cluster
- `S3BucketName`
- `IamRoleArn`
- `KmsKeyId`
