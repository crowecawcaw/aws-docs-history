# Improve Hive performance

Amazon EMR offers features to help optimize performance when using Hive to query, read and
write data saved in Amazon S3.

S3 Select can improve query performance for CSV and JSON files in some applications by
“pushing down” processing to Amazon S3.

The EMRFS S3 optimized committer is an alternative to the [OutputCommitter](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/mapreduce/OutputCommitter.html "https://hadoop.apache.org/docs/current/api/org/apache/hadoop/mapreduce/OutputCommitter.html") class, that eliminates list and rename operations to
improve performance when writing files Amazon S3 using EMRFS.

###### Topics

- [Enabling Hive EMRFS S3 optimized
  committer](hive-optimized-committer.md "hive-optimized-committer.md")
- [Using S3 Select with Hive to improve
  performance](emr-hive-s3select.md "emr-hive-s3select.md")
- [MSCK Optimization](emr-msck-optimization.md "emr-msck-optimization.md")
