# Exporting DB snapshot data to Amazon S3 for Amazon RDS

You can export DB snapshot data to an Amazon S3 bucket. The export process runs in the background
and doesn't affect the performance of your active database.

When you export a DB snapshot, Amazon RDS extracts data from the snapshot and stores it in an Amazon S3 bucket.
The data is stored in an Apache Parquet format that is compressed and consistent.

You can export all types of DB snapshots—including manual snapshots, automated system snapshots, and
snapshots created by the AWS Backup service. By default, all data in the snapshot is exported. However, you can choose to export specific
sets of databases, schemas, or tables.

After the data is exported, you can analyze the exported data directly through tools like Amazon Athena or Amazon Redshift Spectrum. For more
information on using Athena to read Parquet data, see [Parquet SerDe](../../../athena/latest/ug/parquet-serde.md "../../../athena/latest/ug/parquet-serde.md") in the
_Amazon Athena User Guide_. For more information on using Redshift Spectrum to read Parquet data, see [COPY from columnar data formats](../../../redshift/latest/dg/copy-usage_notes-copy-from-columnar.md "../../../redshift/latest/dg/copy-usage_notes-copy-from-columnar.md") in the
_Amazon Redshift Database Developer Guide_.

###### Warning

You can't restore exported snapshot data from S3 to a new DB instance or import snapshot data
from S3 into an existing DB instance. However, you can process the data using Amazon Athena or
Redshift Spectrum for analysis. Additionally, you can use AWS Glue to transform the data and then
import it into Amazon RDS using tools like AWS DMS or custom scripts.

For more information about exporting DB snapshots to Amazon S3, see the following topics.

###### Topics

- [Monitoring snapshot exports for Amazon RDS](USER_ExportSnapshot.md "USER_ExportSnapshot.md")
- [Canceling a snapshot export task for Amazon RDS](USER_ExportSnapshot.md "USER_ExportSnapshot.md")
- [Failure messages for Amazon S3 export tasks for Amazon RDS](USER_ExportSnapshot.md "USER_ExportSnapshot.md")
- [Troubleshooting RDS for PostgreSQL permissions
  errors](USER_ExportSnapshot.md "USER_ExportSnapshot.md")
- [File naming conventions for exports to Amazon S3 for Amazon RDS](USER_ExportSnapshot.md "USER_ExportSnapshot.md")
- [Data conversion when exporting to an Amazon S3
  bucket for Amazon RDS](USER_ExportSnapshot.md "USER_ExportSnapshot.md")

## Overview of exporting snapshot data

You use the following process to export DB snapshot data to an Amazon S3 bucket. For more details, see the following sections.

1. Identify the snapshot to export.

Use an existing automated or manual snapshot, or create a manual snapshot of a DB instance or
Multi-AZ DB cluster. 2. Set up access to the Amazon S3 bucket.

A _bucket_ is a container for Amazon S3 objects or files. To
provide the information to access a bucket, take the following steps:

    1. Identify the S3 bucket where the snapshot is to be exported to. The S3 bucket must be in
     the same AWS Region as the snapshot. For more information, see [Identifying the Amazon S3 bucket for export](#USER_ExportSnapshot.SetupBucket "#USER_ExportSnapshot.SetupBucket").
    2. Create an AWS Identity and Access Management (IAM) role that grants the snapshot export task access to the S3
     bucket. For more information, see [Providing access to an Amazon S3 bucket using an
     IAM role](#USER_ExportSnapshot.SetupIAMRole "#USER_ExportSnapshot.SetupIAMRole").

3. Create a symmetric encryption AWS KMS key for the server-side encryption. The KMS key is used by the snapshot
   export task to set up AWS KMS server-side encryption when writing the export data to S3.

The KMS key policy must include both the `kms:CreateGrant` and `kms:DescribeKey` permissions.
For more information on using KMS keys in Amazon RDS, see [AWS KMS key management](Overview.Encryption.md "Overview.Encryption.md").

If you have a deny statement in your KMS key policy, make sure to explicitly exclude the AWS service principal
`export.rds.amazonaws.com`.

You can use a KMS key within your AWS account, or you can use a cross-account KMS key.
For more information, see [Using a cross-account AWS KMS key for encrypting Amazon S3 exports](#USER_ExportSnapshot.CMK "#USER_ExportSnapshot.CMK"). 4. Export the snapshot to Amazon S3 using the console or the `start-export-task` CLI
command. For more information, see [Exporting a DB snapshot to an Amazon S3 bucket](#USER_ExportSnapshot.Exporting "#USER_ExportSnapshot.Exporting"). 5. To access your exported data in the Amazon S3 bucket, see [Uploading, downloading, and managing objects](../../../AmazonS3/latest/user-guide/upload-download-objects.md "../../../AmazonS3/latest/user-guide/upload-download-objects.md")
in the _Amazon Simple Storage Service User Guide_.

## Setting up access to an Amazon S3 bucket

To export DB snapshot data to an Amazon S3 file, you first give the snapshot permission to access
the Amazon S3 bucket. You then create an IAM role to allow the Amazon RDS service to write to the Amazon S3 bucket.

###### Topics

- [Identifying the Amazon S3 bucket for export](#USER_ExportSnapshot.SetupBucket "#USER_ExportSnapshot.SetupBucket")
- [Providing access to an Amazon S3 bucket using an
  IAM role](#USER_ExportSnapshot.SetupIAMRole "#USER_ExportSnapshot.SetupIAMRole")
- [Using a cross-account Amazon S3 bucket](#USER_ExportSnapshot.Setup.XAcctBucket "#USER_ExportSnapshot.Setup.XAcctBucket")
- [Using a cross-account AWS KMS key for encrypting Amazon S3 exports](#USER_ExportSnapshot.CMK "#USER_ExportSnapshot.CMK")

### Identifying the Amazon S3 bucket for export

Identify the Amazon S3 bucket to export the DB snapshot to. Use an existing S3 bucket or create
a new S3 bucket.

###### Note

The S3 bucket to export to must be in the same AWS Region as the snapshot.

For more information about working with Amazon S3 buckets, see the following in the _Amazon Simple Storage Service User Guide_:

- [How do I view the
  properties for an S3 bucket?](../../../AmazonS3/latest/user-guide/view-bucket-properties.md "../../../AmazonS3/latest/user-guide/view-bucket-properties.md")
- [How do I enable
  default encryption for an Amazon S3 bucket?](../../../AmazonS3/latest/user-guide/default-bucket-encryption.md "../../../AmazonS3/latest/user-guide/default-bucket-encryption.md")
- [How do I create an S3
  bucket?](../../../AmazonS3/latest/user-guide/create-bucket.md "../../../AmazonS3/latest/user-guide/create-bucket.md")

### Providing access to an Amazon S3 bucket using an

IAM role

Before you export DB snapshot data to Amazon S3, give the snapshot export tasks write-access
permission to the Amazon S3 bucket.

To grant this permission, create an IAM policy that provides access to the bucket, then create an IAM role and attach the
policy to the role. You later assign the IAM role to your snapshot export task.

For information about other Amazon S3 access management tools, see [Access control in Amazon S3](../../../AmazonS3/latest/userguide/access-management.md "../../../AmazonS3/latest/userguide/access-management.md") in the _Amazon S3 User Guide_.

###### Important

If you plan to use the AWS Management Console to export your snapshot, you can choose to create the IAM policy and the role
automatically when you export the snapshot. For instructions, see [Exporting a DB snapshot to an Amazon S3 bucket](#USER_ExportSnapshot.Exporting "#USER_ExportSnapshot.Exporting").

###### To give DB snapshot tasks access to Amazon S3

1. Create an IAM policy. This policy provides the bucket and object permissions that allow
   your snapshot export task to access Amazon S3.

In the policy, include the following required actions to allow the transfer of files from Amazon RDS to an S3 bucket:

    * `s3:PutObject*`
    * `s3:GetObject*`
    * `s3:ListBucket`
    * `s3:DeleteObject*`
    * `s3:GetBucketLocation`

In the policy, include the following resources to identify the S3 bucket and objects in the bucket. The following list of
resources shows the Amazon Resource Name (ARN) format for accessing Amazon S3.

    * `arn:aws:s3:::`amzn-s3-demo-bucket``
    * `arn:aws:s3:::`amzn-s3-demo-bucket`/*`

For more information on creating an IAM policy for Amazon RDS, see
[Creating and using an IAM policy for
IAM database access](UsingWithRDS.IAMDBAuth.md "UsingWithRDS.IAMDBAuth.md"). See also [Tutorial:
Create and attach your first customer managed policy](../../../IAM/latest/UserGuide/tutorial_managed-policies.md "../../../IAM/latest/UserGuide/tutorial_managed-policies.md") in the
_IAM User Guide_.

The following AWS CLI command creates an IAM policy named `ExportPolicy` with
these options. It grants access to a bucket named
`amzn-s3-demo-bucket`.

###### Note

After you create the policy, note the ARN of the policy. You need the ARN for a
subsequent step when you attach the policy to an IAM role.

```
aws iam create-policy  --policy-name ExportPolicy --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ExportPolicy",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject*",
                "s3:ListBucket",
                "s3:GetObject*",
                "s3:DeleteObject*",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-bucket`",
                "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
            ]
        }
    ]
}'
```

2. Create an IAM role, so that Amazon RDS can assume this IAM role on your behalf to access your Amazon S3 buckets. For more information,
   see [Creating a role to
   delegate permissions to an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.

The following example shows using the AWS CLI command to create a role named `rds-s3-export-role`.

```
aws iam create-role  --role-name rds-s3-export-role  --assume-role-policy-document '{
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
            "Service": "export.rds.amazonaws.com"
          },
         "Action": "sts:AssumeRole"
       }
     ]
   }'
```

3. Attach the IAM policy that you created to the IAM role that you
   created.

The following AWS CLI command attaches the policy created earlier to the role named
`rds-s3-export-role`. Replace
`your-policy-arn` with the
policy ARN that you noted in an earlier step.

```
aws iam attach-role-policy  --policy-arn `your-policy-arn`  --role-name rds-s3-export-role
```

### Using a cross-account Amazon S3 bucket

You can use Amazon S3 buckets across AWS accounts. To use a cross-account bucket, add
a bucket policy to allow access to the IAM role that you're using for the S3
exports. For more information, see [Example 2: Bucket owner granting cross-account bucket
permissions](../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md "../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md").

Attach a bucket policy to your bucket, as shown in the following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:role/Admin"
 },
 "Action": [
 "s3:PutObject*",
 "s3:ListBucket",
 "s3:GetObject*",
 "s3:DeleteObject*",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-destination-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-destination-bucket`/*"
 ]
 }
 ]
}`

```

### Using a cross-account AWS KMS key for encrypting Amazon S3 exports

You can use a cross-account AWS KMS key to encrypt Amazon S3 exports. First, you add a key policy to the local account, then
you add IAM policies in the external account. For more information, see [Allowing users in other accounts to use a
KMS key](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md").

###### To use a cross-account KMS key

1. Add a key policy to the local account.

The following example gives `ExampleRole` and `ExampleUser` in the external account
444455556666 permissions in the local account 123456789012.

```
{
    "Sid": "Allow an external account to use this KMS key",
    "Effect": "Allow",
    "Principal": {
        "AWS": [
            "arn:aws:iam::444455556666:role/ExampleRole",
            "arn:aws:iam::444455556666:user/ExampleUser"
        ]
    },
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:CreateGrant",
        "kms:DescribeKey",
        "kms:RetireGrant"
    ],
    "Resource": "*"
}
```

2. Add IAM policies to the external account.

The following example IAM policy allows the principal to use the KMS key in account 123456789012 for
cryptographic operations. To give this permission to `ExampleRole` and `ExampleUser` in
account 444455556666, [attach the policy](../../../IAM/latest/UserGuide/access_policies_managed-using.md#attach-managed-policy-console "../../../IAM/latest/UserGuide/access_policies_managed-using.md#attach-managed-policy-console") to them in that account.

```
{
    "Sid": "Allow use of KMS key in account 123456789012",
    "Effect": "Allow",
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:CreateGrant",
        "kms:DescribeKey",
        "kms:RetireGrant"
    ],
    "Resource": "arn:aws:kms:us-west-2:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"
}
```

## Exporting a DB snapshot to an Amazon S3 bucket

You can have up to five concurrent DB snapshot export tasks in progress per AWS account.

###### Note

Exporting RDS snapshots can take a while depending on your database type and size. The export task first restores and scales the
entire database before extracting the data to Amazon S3. The task's progress during this phase displays as
**Starting**. When the task switches to exporting data to S3, progress displays as **In
progress**.

The time it takes for the export to complete depends on the data stored in the database.
For example, tables with well-distributed numeric primary key or index columns
export the fastest. Tables that don't contain a column suitable for
partitioning and tables with only one index on a string-based column take longer.
This longer export time occurs because the export uses a slower single-threaded
process.

You can export a DB snapshot to Amazon S3 using the AWS Management Console, the AWS CLI, or the RDS
API. To export a DB snapshot to a cross-account Amazon S3 bucket, use the AWS CLI or the RDS API.

If you use a Lambda function to export a snapshot, add the `kms:DescribeKey`
action to the Lambda function policy. For more information, see [AWS Lambda
permissions](../../../lambda/latest/dg/lambda-permissions.md "../../../lambda/latest/dg/lambda-permissions.md").

The **Export to Amazon S3** console option appears only for snapshots that can be exported to Amazon S3. A
snapshot might not be available for export because of the following reasons:

- The DB engine isn't supported for S3 export.
- The DB engine version isn't supported for S3 export.
- S3 export isn't supported in the AWS Region where the snapshot was created.

###### To export a DB snapshot

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Snapshots**.
3. From the tabs, choose the type of snapshot that you want to export.
4. In the list of snapshots, choose the snapshot that you want to export.
5. For **Actions**, choose **Export to Amazon
   S3**.

The **Export to Amazon S3** window appears. 6. For **Export identifier**, enter a name to identify the export task.
This value is also used for the name of the file created in the S3
bucket. 7. Choose the data to be exported:

    * Choose **All** to export all data in the snapshot.
    * Choose **Partial** to export specific parts of the snapshot. To identify which parts of the snapshot to
     export, enter one or more databases, schemas, or tables for **Identifiers**, separated
     by spaces.


    Use the following format:



    ```
    `database`[.`schema`][.`table`] `database2`[.`schema2`][.`table2`] ... `database`*n*[.`schema`*n*][.`table`*n*]
    ```

    For example:



    ```
    mydatabase mydatabase2.myschema1 mydatabase2.myschema2.mytable1 mydatabase2.myschema2.mytable2
    ```

8. For **S3 bucket**, choose the bucket to export to.

To assign the exported data to a folder path in the S3 bucket, enter the optional path
for **S3 prefix**. 9. For **IAM role**, either choose a role that grants you write access to your
chosen S3 bucket, or create a new role.

    * If you created a role by following the steps in [Providing access to an Amazon S3 bucket using an
     IAM role](#USER_ExportSnapshot.SetupIAMRole "#USER_ExportSnapshot.SetupIAMRole"), choose that
     role.
    * If you didn't create a role that grants you write access to your chosen S3 bucket, then choose **Create a new
     role** to create the role automatically. Next, enter a name for the role in **IAM
     role name**.

10. For **AWS KMS key**, enter the ARN for the key to use for encrypting the
    exported data.
11. Choose **Export to Amazon S3**.
    To export a DB snapshot to Amazon S3 using the AWS CLI, use the [start-export-task](../../../cli/latest/reference/rds/start-export-task.md "../../../cli/latest/reference/rds/start-export-task.md") command with the following required
    options:

- `--export-task-identifier`
- `--source-arn`
- `--s3-bucket-name`
- `--iam-role-arn`
- `--kms-key-id`
  In the following examples, the snapshot export task is named `my-snapshot-export`, which exports a
  snapshot to an S3 bucket named `amzn-s3-demo-bucket`.

For Linux, macOS, or Unix:

```
aws rds start-export-task \
    --export-task-identifier `my-snapshot-export` \
    --source-arn arn:aws:rds:`AWS_Region`:123456789012:snapshot:`snapshot-name` \
    --s3-bucket-name `amzn-s3-demo-bucket` \
    --iam-role-arn `iam-role` \
    --kms-key-id `my-key`
```

For Windows:

```
aws rds start-export-task ^
    --export-task-identifier `my-snapshot-export` ^
    --source-arn arn:aws:rds:`AWS_Region`:123456789012:snapshot:`snapshot-name` ^
    --s3-bucket-name `amzn-s3-demo-bucket` ^
    --iam-role-arn `iam-role` ^
    --kms-key-id `my-key`
```

Sample output follows.

```
{
    "Status": "STARTING",
    "IamRoleArn": "iam-role",
    "ExportTime": "2019-08-12T01:23:53.109Z",
    "S3Bucket": "my-export-bucket",
    "PercentProgress": 0,
    "KmsKeyId": "my-key",
    "ExportTaskIdentifier": "my-snapshot-export",
    "TotalExtractedDataInGB": 0,
    "TaskStartTime": "2019-11-13T19:46:00.173Z",
    "SourceArn": "arn:aws:rds:AWS_Region:123456789012:snapshot:snapshot-name"
}
```

To provide a folder path in the S3 bucket for the snapshot export, include the
`--s3-prefix` option in the [start-export-task](../../../cli/latest/reference/rds/start-export-task.md "../../../cli/latest/reference/rds/start-export-task.md")
command.

To export a DB snapshot to Amazon S3 using the Amazon RDS API, use the [StartExportTask](../APIReference/API_StartExportTask.md "../APIReference/API_StartExportTask.md")
operation with the following required parameters:

- `ExportTaskIdentifier`
- `SourceArn`
- `S3BucketName`
- `IamRoleArn`
- `KmsKeyId`

## Region and version availability

Feature availability and support varies across specific versions of each database engine and across AWS Regions. For more
information on version and Region availability with exporting snapshots to S3, see [Supported
Regions and DB engines for exporting snapshots to S3 in Amazon RDS](Concepts.RDS_Fea_Regions_DB-eng.Feature.md "Concepts.RDS_Fea_Regions_DB-eng.Feature.md").

## Limitations

Exporting DB snapshot data to Amazon S3 has the following limitations:

- You can't run multiple export tasks for the same DB snapshot simultaneously. This applies to both full and partial
  exports.
- Exporting snapshots from databases that use magnetic storage isn't
  supported.
- Exports to S3 don't support S3 prefixes containing a colon (:).
- The following characters in the S3 file path are converted to underscores (\_) during export:

```
\ ` " (space)
```

- If a database, schema, or table has characters in its name other than the following, partial export isn't
  supported. However, you can export the entire DB snapshot.
  - Latin letters (A–Z)
  - Digits (0–9)
  - Dollar symbol ($)
  - Underscore (\_)

- Spaces ( ) and certain characters aren't supported in database table column names. Tables with the following
  characters in column names are skipped during export:

```
, ; { } ( ) \n \t = (space)
```

- Tables with slashes (/) in their names are skipped during export.
- RDS for PostgreSQL temporary and unlogged tables are skipped during export.
- If the data contains a large object, such as a BLOB or CLOB, that is close to or greater than 500 MB, then the export
  fails.
- If a table contains a large row that is close to or greater than 2 GB, then the table is skipped during export.
- For partial exports, the `ExportOnly` list has a maximum size of
  200 KB.
- We strongly recommend that you use a unique name for each export task. If you don't use a unique task name, you might
  receive the following error message:

**`ExportTaskAlreadyExistsFault: An error occurred (ExportTaskAlreadyExists) when calling the StartExportTask
 operation: The export task with the ID `xxxxx` already exists.`**

- You can delete a snapshot while you're exporting its data to S3, but you're still charged for the storage
  costs for that snapshot until the export task has completed.
- You can't restore exported snapshot data from S3 to a new
  DB instance or import snapshot data from S3 into an existing DB instance.
- You can have up to five concurrent DB snapshot export tasks in progress per AWS account.
- To export a DB snapshot to a cross-account Amazon S3 bucket, you must use the AWS CLI or the RDS API.
- After Amazon RDS completes an export task, you might have to wait a short time to start another export task from the same DB snapshot.
- You can't export views or materialized views.
- RDS Export to S3 doesn't support tag-based access control for GuardDuty Malware Protection for S3.
