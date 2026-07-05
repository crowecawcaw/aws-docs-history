Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Best practices

Consider the following best practices when you write to an Apache Iceberg
table:

- For small, frequent writes or streaming workloads, consider using compaction
  features provided by AWS Glue Data Catalog or Amazon S3 tables to optimize file
  sizes for reads.

- The `DROP TABLE` command deregisters the table from the AWS Glue Data Catalog
  or the Amazon S3 tables catalog, but your files still remain. You can
  use features in AWS Glue and Amazon S3 tables to remove orphaned files. For
  AWS Glue, see [Deleting orphan
  files](../../../glue/latest/dg/orphan-file-deletion.md "../../../glue/latest/dg/orphan-file-deletion.md"). For Amazon S3 tables, see [Table
  maintenance](../../../AmazonS3/latest/userguide/s3-tables-maintenance.md "../../../AmazonS3/latest/userguide/s3-tables-maintenance.md").
