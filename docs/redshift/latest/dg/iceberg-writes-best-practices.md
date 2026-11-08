

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Best practices
<a name="iceberg-writes-best-practices"></a>

Consider the following best practices when you write to an Apache Iceberg table:
+ For small, frequent writes or streaming workloads, consider using compaction features provided by AWS Glue Data Catalog or Amazon S3 tables to optimize file sizes for reads.
+ Set up orphan file removal before you use multi-statement transactions. A transaction that doesn't commit leaves data and metadata files that no snapshot references. For Amazon S3 table buckets, unreferenced file removal is turned on by default. For tables in the AWS Glue Data Catalog, turn on the orphan file deletion table optimizer. The optimizer removes only files that are created after you turn it on. For more information, see [Deleting orphan files](https://docs.aws.amazon.com/glue/latest/dg/orphan-file-deletion.html) in the *AWS Glue Developer Guide* and [Maintenance for table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html) in the *Amazon Simple Storage Service User Guide*.
+ The `DROP TABLE` command deregisters the table from the AWS Glue Data Catalog or the Amazon S3 tables catalog, but your files still remain. You can use features in AWS Glue and Amazon S3 tables to remove orphaned files. For AWS Glue, see [Deleting orphan files](https://docs.aws.amazon.com/glue/latest/dg/orphan-file-deletion.html). For Amazon S3 tables, see [Table maintenance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html).