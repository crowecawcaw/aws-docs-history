

# Exporting DB cluster snapshot data to Amazon S3
<a name="aurora-export-snapshot"></a>

You can export DB cluster snapshot data to an Amazon S3 bucket. The export process runs in the background and doesn't affect the performance of your active DB cluster.

When you export a DB cluster snapshot, Amazon Aurora extracts data from the snapshot and stores it in an Amazon S3 bucket. You can export manual snapshots and automated system snapshots. By default, all data in the snapshot is exported. However, you can choose to export specific sets of databases, schemas, or tables.

**Note**  
Exporting data from a DB cluster snapshot requires restoring the snapshot. Restore times are impacted by various factors, such as the amount of network traffic an AWS Region receives relative to its available bandwidth. When there's a sudden increase in traffic, you might experience longer than expected completion times.  
An alternative for decreasing S3 export times for Aurora databases is live DB cluster export to S3. DB cluster export has shorter start times than DB snapshot export, because there's no need to restore a snapshot. For more information, see [Exporting DB cluster data to Amazon S3](export-cluster-data.md).

The data is stored in an Apache Parquet format that is compressed and consistent. Individual Parquet files are usually 1–10 MB in size.

After the data is exported, you can analyze the exported data directly through tools like Amazon Athena or Amazon Redshift Spectrum. For more information on using Athena to read Parquet data, see [Parquet SerDe](https://docs.aws.amazon.com/athena/latest/ug/parquet-serde.html) in the *Amazon Athena User Guide*. For more information on using Redshift Spectrum to read Parquet data, see [COPY from columnar data formats](https://docs.aws.amazon.com/redshift/latest/dg/copy-usage_notes-copy-from-columnar.html) in the *Amazon Redshift Database Developer Guide*.

Feature availability and support varies across specific versions of each database engine and across AWS Regions. For more information on version and Region availability of exporting DB cluster snapshot data to S3, see [Supported Regions and Aurora DB engines for exporting snapshot data to Amazon S3](Concepts.Aurora_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.md).

You use the following process to export DB snapshot data to an Amazon S3 bucket. For more details, see the following sections.

**Overview of exporting snapshot data**

1. Identify the snapshot to export.

   Use an existing automated or manual snapshot, or create a manual snapshot of a DB instance.

1. Set up access to the Amazon S3 bucket.

   A *bucket* is a container for Amazon S3 objects or files. To provide the information to access a bucket, take the following steps:

   1. Identify the S3 bucket where the snapshot is to be exported to. The S3 bucket must be in the same AWS Region as the snapshot. For more information, see [Identifying the Amazon S3 bucket for export](aurora-export-snapshot.Setup.md#aurora-export-snapshot.SetupBucket).

   1. Create an AWS Identity and Access Management (IAM) role that grants the snapshot export task access to the S3 bucket. For more information, see [Providing access to an Amazon S3 bucket using an IAM role](aurora-export-snapshot.Setup.md#aurora-export-snapshot.SetupIAMRole). 

1. Create a symmetric encryption AWS KMS key for the server-side encryption. The KMS key is used by the snapshot export task to set up AWS KMS server-side encryption when writing the export data to S3.

   The KMS key policy must include both the `kms:CreateGrant` and `kms:DescribeKey` permissions. For more information on using KMS keys in Amazon Aurora, see [AWS KMS key management](Overview.Encryption.Keys.md).

   If you have a deny statement in your KMS key policy, make sure to explicitly exclude the AWS service principal `export.rds.amazonaws.com`.

   You can use a KMS key within your AWS account, or you can use a cross-account KMS key. For more information, see [Using a cross-account AWS KMS key](aurora-export-snapshot.Setup.md#aurora-export-snapshot.CMK).

1. Export the snapshot to Amazon S3 using the console or the `start-export-task` CLI command. For more information, see [Creating snapshot export tasks](aurora-export-snapshot.Exporting.md). 

1. To access your exported data in the Amazon S3 bucket, see [Uploading, downloading, and managing objects](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/upload-download-objects.html) in the *Amazon Simple Storage Service User Guide*.

Learn to set up, export, monitor, cancel, and troubleshoot DB cluster snapshot export tasks in the following sections.

**Topics**
+ [Considerations for DB cluster snapshot exports](aurora-export-snapshot.Considerations.md)
+ [Setting up access to an Amazon S3 bucket](aurora-export-snapshot.Setup.md)
+ [Creating snapshot export tasks](aurora-export-snapshot.Exporting.md)
+ [Monitoring snapshot exports](aurora-export-snapshot.Monitoring.md)
+ [Canceling a snapshot export task](aurora-export-snapshot.Canceling.md)
+ [Export performance in Aurora MySQL](aurora-export-snapshot.parallel.md)
+ [Troubleshooting snapshot exports](aurora-export-snapshot.Troubleshooting.md)