# Improve Spark performance with Amazon S3

Amazon EMR offers features to help optimize performance when using Spark to query, read and
write data saved in Amazon S3.

[S3 Select](https://aws.amazon.com/blogs/aws/s3-glacier-select/ "https://aws.amazon.com/blogs/aws/s3-glacier-select/") can
improve query performance for CSV and JSON files in some applications by "pushing down"
processing to Amazon S3.

The EMRFS S3-optimized committer is an alternative to the [OutputCommitter](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/mapreduce/OutputCommitter.html "https://hadoop.apache.org/docs/current/api/org/apache/hadoop/mapreduce/OutputCommitter.html") class, which uses the multipart uploads feature of EMRFS to
improve performance when writing Parquet files to Amazon S3 using Spark, DataFrames, and
Datasets.

###### Topics

- [Use S3 Select with Spark to improve query
  performance](emr-spark-s3select.md "emr-spark-s3select.md")
- [EMR Spark
  MagicCommitProtocol](emr-spark-magic-commit-protocol.md "emr-spark-magic-commit-protocol.md")
- [Use the EMRFS S3-optimized
  committer](emr-spark-s3-optimized-committer.md "emr-spark-s3-optimized-committer.md")
- [Use the EMRFS S3-optimized
  commit protocol](emr-spark-s3-optimized-commit-protocol.md "emr-spark-s3-optimized-commit-protocol.md")
- [Retry Amazon S3 requests with
  EMRFS](emr-spark-emrfs-retry.md "emr-spark-emrfs-retry.md")
