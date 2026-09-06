

# Exporting DB cluster data to Amazon S3
<a name="export-cluster-data"></a>

You can export data from a live Amazon Aurora DB cluster to an Amazon S3 bucket. The export process runs in the background and doesn't affect the performance of your active DB cluster.

By default, all data in the DB cluster is exported. However, you can choose to export specific sets of databases, schemas, or tables.

Amazon Aurora clones the DB cluster, extracts data from the clone, and stores the data in an Amazon S3 bucket. The data is stored in an Apache Parquet format that is compressed and consistent. Individual Parquet files are usually 1–10 MB in size.

The faster performance that you can get with exporting snapshot data for Aurora MySQL version 2 and version 3 doesn't apply to exporting DB cluster data. For more information, see [Exporting DB cluster snapshot data to Amazon S3](aurora-export-snapshot.md).

You're charged for exporting the entire DB cluster, whether you export all or partial data. For more information, see the [Amazon Aurora pricing page](https://aws.amazon.com/rds/aurora/pricing/).

After the data is exported, you can analyze the exported data directly through tools like Amazon Athena or Amazon Redshift Spectrum. For more information on using Athena to read Parquet data, see [Parquet SerDe](https://docs.aws.amazon.com/athena/latest/ug/parquet-serde.html) in the *Amazon Athena User Guide*. For more information on using Redshift Spectrum to read Parquet data, see [COPY from columnar data formats](https://docs.aws.amazon.com/redshift/latest/dg/copy-usage_notes-copy-from-columnar.html) in the *Amazon Redshift Database Developer Guide*.

Feature availability and support varies across specific versions of each database engine and across AWS Regions. For more information on version and Region availability of exporting DB cluster data to S3, see [Supported Regions and Aurora DB engines for exporting cluster data to Amazon S3](Concepts.Aurora_Fea_Regions_DB-eng.Feature.ExportClusterToS3.md).

You use the following process to export DB cluster data to an Amazon S3 bucket. For more details, see the following sections.

**Overview of exporting DB cluster data**

1. Identify the DB cluster whose data you want to export.

1. Set up access to the Amazon S3 bucket.

   A *bucket* is a container for Amazon S3 objects or files. To provide the information to access a bucket, take the following steps:

   1. Identify the S3 bucket where the DB cluster data is to be exported. The S3 bucket must be in the same AWS Region as the DB cluster. For more information, see [Identifying the Amazon S3 bucket for export](export-cluster-data.Setup.md#export-cluster-data.SetupBucket).

   1. Create an AWS Identity and Access Management (IAM) role that grants the DB cluster export task access to the S3 bucket. For more information, see [Providing access to an Amazon S3 bucket using an IAM role](export-cluster-data.Setup.md#export-cluster-data.SetupIAMRole).

1. Create a symmetric encryption AWS KMS key for the server-side encryption. The KMS key is used by the cluster export task to set up AWS KMS server-side encryption when writing the export data to S3.

   The KMS key policy must include both the `kms:CreateGrant` and `kms:DescribeKey` permissions. For more information on using KMS keys in Amazon Aurora, see [AWS KMS key management](Overview.Encryption.Keys.md).

   If you have a deny statement in your KMS key policy, make sure to explicitly exclude the AWS service principal `export.rds.amazonaws.com`.

   You can use a KMS key within your AWS account, or you can use a cross-account KMS key. For more information, see [Using a cross-account AWS KMS key](aurora-export-snapshot.Setup.md#aurora-export-snapshot.CMK).

1. Export the DB cluster to Amazon S3 using the console or the `start-export-task` CLI command. For more information, see [Creating DB cluster export tasks](export-cluster-data.Exporting.md). 

1. To access your exported data in the Amazon S3 bucket, see [Uploading, downloading, and managing objects](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/upload-download-objects.html) in the *Amazon Simple Storage Service User Guide*.

Learn to set up, export, monitor, cancel, and troubleshoot DB cluster export tasks in the following sections.

**Topics**
+ [Considerations for DB cluster exports](export-cluster-data.Considerations.md)
+ [Setting up access to an Amazon S3 bucket](export-cluster-data.Setup.md)
+ [Creating DB cluster export tasks](export-cluster-data.Exporting.md)
+ [Monitoring DB cluster export tasks](export-cluster-data.Monitoring.md)
+ [Canceling a DB cluster export task](export-cluster-data.Canceling.md)
+ [Troubleshooting DB cluster exports](export-cluster-data.Troubleshooting.md)