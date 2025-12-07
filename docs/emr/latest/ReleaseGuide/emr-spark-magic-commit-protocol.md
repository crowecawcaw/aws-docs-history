# EMR Spark

MagicCommitProtocol

From EMR 6.15.0 onwards, MagicCommitProtocol becomes the default
FileCommitProtocol for Spark when utilizing the S3A
filesystem.

## MagicCommitProtocol

The MagicCommitProtocol is an alternative implementation of the [FileCommitProtocol](https://dlcdn.apache.org/spark/docs/2.4.2/api/java/org/apache/spark/internal/io/FileCommitProtocol.html "https://dlcdn.apache.org/spark/docs/2.4.2/api/java/org/apache/spark/internal/io/FileCommitProtocol.html") that is optimized for writing files with EMR
Spark to Amazon S3 when using the S3A filesystem. This protocol aims to improve
application performance by avoiding the use of rename operations in Amazon S3 during
the job and task commit phases.

The MagicCommitProtocol is the default FileCommitProtocol implementation used
by Spark running on Amazon Elastic Map Reduce (EMR) when the S3A filesystem is
utilized. The MagicCommitProtocol internally uses the [MagicV2Committer](s3a-magicv2-committer.md "s3a-magicv2-committer.md") to
perform the file writes to Amazon S3.

For static insert operations, the MagicCommitProtocol writes the files in the
job's output location during the task commit phase. In contrast, for dynamic
insert overwrite operations, the files written by task attempts only appear in
the job's output location upon job commit. This is achieved by exporting the
commit metadata back to the Spark driver on the task commit call.

## Enabling

MagicCommitProtocol

The MagicCommitProtocol is enabled by default for Spark running on Amazon
Elastic Map Reduce (EMR) when using the S3A filesystem.

In order to use the S3A filesystem, you can either:

1. Use the file scheme as `s3a://` when defining the table,
   partition, or directory.
2. Set the configuration
   `fs.s3.impl=org.apache.hadoop.fs.s3a.S3AFileSystem` in
   core-site.xml.

## Disabling the

MagicCommitProtocol

1. You can set
   `spark.sql.execution.datasources.SQLEmrOptimizedCommitProtocol.leverageMagicCommitProtocol`
   to false by hard-coding it in a `SparkConf`, passing it as a
   `--conf` parameter in the Spark shell or
   `spark-submit` and `spark-sql` tools, or in
   `conf/spark-defaults.conf`. For more information, see
   [Spark configuration](https://spark.apache.org/docs/latest/configuration.html "https://spark.apache.org/docs/latest/configuration.html") in the Apache Spark
   documentation.

The following example shows how to disable MagicCommitProtocol while
running a `spark-sql` command.

```
spark-sql \
  --conf spark.sql.execution.datasources.SQLEmrOptimizedCommitProtocol.leverageMagicCommitProtocol=false \
-e "INSERT OVERWRITE TABLE target_table SELECT * FROM source_table;"
```

2. Use the `spark-defaults` configuration classification to
   set the
   `spark.sql.execution.datasources.SQLEmrOptimizedCommitProtocol.leverageMagicCommitProtocol`
   property to false. For more information, see [Configure
   applications](emr-configure-apps.md "emr-configure-apps.md").

## MagicCommitProtocol

considerations

- For static partition insert, On Spark executors, the
  MagicCommitProtocol consumes a small amount of memory for each file
  written by a task attempt until the task gets committed or aborted. In
  most jobs, the amount of memory consumed is negligible. There is no
  extra memory requirement on the Spark driver
- For dynamic partition insert, on Spark drivers, the
  MagicCommitProtocol requires memory to store metadata info of each
  committed file until the job gets committed or aborted. In most jobs,
  default Spark driver memory setting is negligible.

For jobs that have long-running tasks that write a large number of
files, the memory that the commit protocol consumes may be noticeable
and require adjustments to the memory allocated for Spark, especially
for Spark executors. You can tune memory using the
`spark.driver.memory` property for Spark drivers, and the
`spark.executor.memory` property for Spark executors. As
a guideline, a single task writing 100,000 files would typically require
an additional 200MB of memory. For more information, see [Application properties](https://spark.apache.org/docs/latest/configuration.html#application-properties "https://spark.apache.org/docs/latest/configuration.html#application-properties") in the Apache Spark Configuration
documentation.
