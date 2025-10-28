Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Amazon Redshift integration for Apache Spark

[Apache Spark](https://aws.amazon.com/emr/features/spark/ "https://aws.amazon.com/emr/features/spark/") is a
distributed processing framework and programming model that helps you do machine learning,
stream processing, or graph analytics. Similar to Apache Hadoop, Spark is an open-source,
distributed processing system commonly used for big data workloads. Spark has an optimized
directed acyclic graph (DAG)
execution engine and actively caches data in-memory. This can boost
performance, especially for certain algorithms and interactive queries.

This integration provides you with a Spark connector you can use to build Apache Spark
applications that read from and write to data in Amazon Redshift and Amazon Redshift Serverless. These
applications don't compromise on application performance or transactional consistency
of the data. This integration is automatically included in [Amazon EMR](../../../emr/latest/ReleaseGuide.md "../../../emr/latest/ReleaseGuide.md") and [AWS Glue](../../../glue/latest/dg.md "../../../glue/latest/dg.md"), so you can immediately run
Apache Spark jobs that access and load data into Amazon Redshift as part of your data ingestion and
transformation pipelines.

Currently, you can use the versions 3.3.0, 3.3.1, 3.3.2, and 3.4.0 of Spark with this
integration.

This integration provides the following:

- AWS Identity and Access Management (IAM) authentication. For more information, see [Identity and access management in Amazon Redshift.](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md")
- Predicate and query pushdown to improve performance.
- Amazon Redshift data types.
- Connectivity to Amazon Redshift and Amazon Redshift Serverless.

## Considerations and limitations

when using the Spark connector

- The tempdir URI points to an Amazon S3 location. This temp directory is not
  cleaned up automatically and could add additional cost. We recommend using
  [Amazon S3 lifecycle
  policies](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") in the _Amazon Simple Storage Service User Guide_ to define the
  retention rules for the Amazon S3 bucket.
- By default, copies between Amazon S3 and Redshift don't work if the S3 bucket and
  Redshift cluster are in different AWS Regions. To use separate AWS Regions,
  set the `tempdir_region` parameter to the Region of the S3 bucket
  used for the `tempdir`.
- Cross-Region writes between S3 and Redshift if writing Parquet data using the
  `tempformat` parameter.
- We recommend using [Amazon S3
  server-side encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md") to encrypt the Amazon S3 buckets used.
- We recommend [blocking public access to Amazon S3 buckets](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md").
- We recommend that the Amazon Redshift cluster should not be publicly accessible.
- We recommend turning on [Amazon Redshift audit logging](db-auditing.md "db-auditing.md").
- We recommend turning on [Amazon Redshift
  at-rest encryption](security-server-side-encryption.md "security-server-side-encryption.md").
- We recommend turning on SSL for the JDBC connection from Spark on Amazon EMR to
  Amazon Redshift.
- We recommend passing an IAM role using the parameter
  `aws_iam_role` for the Amazon Redshift authentication parameter.
