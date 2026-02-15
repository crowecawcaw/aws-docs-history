# Requirements for the EMRFS

S3-optimized commit protocol

The EMRFS S3-optimized commit protocol is used when the following conditions
are met:

- You run Spark jobs that use Spark, DataFrames, or Datasets to
  overwrite partitioned tables.
- You run Spark jobs whose partition overwrite mode is
  `dynamic`.
- Multipart uploads are enabled in Amazon EMR . This is the default. For more
  information, see [The EMRFS S3-optimized
  commit protocol and multipart uploads](emr-spark-commit-protocol-multipart.md "emr-spark-commit-protocol-multipart.md").
- The filesystem cache for EMRFS is enabled. This is the default. Check
  that the setting `fs.s3.impl.disable.cache` is set to
  `false`.
- Spark's built-in data source support is used. Built-in data source
  support is used in the following circumstances:
  - When jobs write to built-in data sources or tables.
  - When jobs write to the Hive metastore Parquet table. This
    happens when
    `spark.sql.hive.convertInsertingPartitionedTable`
    and `spark.sql.hive.convertMetastoreParquet` are both
    set to true. These are the default settings.
  - When jobs write to the Hive metastore ORC table. This happens
    when
    `spark.sql.hive.convertInsertingPartitionedTable`
    and `spark.sql.hive.convertMetastoreOrc` are both set
    to `true`. These are the default settings.

- Spark job operations that write to a default partition location
  – for example, `${table_location}/k1=v1/k2=v2/`
  – use the commit protocol. The protocol is not used if a job
  operation writes to a custom partition location – for example, if
  a custom partition location is set using the `ALTER TABLE
SQL` command.
- The following values for Spark must be used:
  - `spark.sql.sources.commitProtocolClass` must be set
    to
    `org.apache.spark.sql.execution.datasources.SQLEmrOptimizedCommitProtocol`.
    This is the default setting for Amazon EMR releases 5.30.0 and
    higher, and 6.2.0 and higher.
  - The `partitionOverwriteMode` write option or
    `spark.sql.sources.partitionOverwriteMode` must
    be set to `dynamic`. The default setting is
    `static`.

  ###### Note

  The `partitionOverwriteMode` write option was
  introduced in Spark 2.4.0. For Spark version 2.3.2, included
  with Amazon EMR release 5.19.0, set the
  `spark.sql.sources.partitionOverwriteMode`
  property.
  - If Spark jobs overwrite to the Hive metastore Parquet table,
    `spark.sql.hive.convertMetastoreParquet`,
    `spark.sql.hive.convertInsertingPartitionedTable`,
    and
    `spark.sql.hive.convertMetastore.partitionOverwriteMode`
    must be set to `true`. There are the default
    settings.
  - If Spark jobs overwrite to the Hive metastore ORC table,
    `spark.sql.hive.convertMetastoreOrc`,
    `spark.sql.hive.convertInsertingPartitionedTable`,
    and
    `spark.sql.hive.convertMetastore.partitionOverwriteMode`
    must be set to `true`. There are the default
    settings.

###### Example– Dynamic partition overwrite mode

In this Scala example, optimization is triggered. First, you set the
`partitionOverwriteMode` property to `dynamic`.
This only overwrites those partitions to which you're writing data. Then,
you specify dynamic partition columns with `partitionBy` and set
the write mode to `overwrite`.

```
val dataset = spark.range(0, 10)
  .withColumn("dt", expr("date_sub(current_date(), id)"))

dataset.write.mode("overwrite")                 // "overwrite" instead of "insert"
  .option("partitionOverwriteMode", "dynamic")  // "dynamic" instead of "static"
  .partitionBy("dt")                            // partitioned data instead of unpartitioned data
  .parquet("s3://amzn-s3-demo-bucket1/output")    // "s3://" to use Amazon EMR file system, instead of "s3a://" or "hdfs://"
```

## When the EMRFS S3-optimized

commit protocol is not used

Generally, the EMRFS S3-optimized commit protocol works the same as open
source default Spark commit protocol,
`org.apache.spark.sql.execution.datasources.SQLHadoopMapReduceCommitProtocol`.
Optimization won't occur in the following situations.

| Situation                                               | Why the commit protocol is not used                                                                                                                                                                                 |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| When you write to HDFS                                  | The commit protocol only supports writing to<br>Amazon S3 using EMRFS.                                                                                                                                              |
| When you use the S3A file system                        | The commit protocol only supports EMRFS.                                                                                                                                                                            |
| When you use MapReduce or Spark's RDD API               | The commit protocol only supports using SparkSQL,<br>DataFrame, or Dataset APIs.                                                                                                                                    |
| When the dynamic partition overwrite isn't<br>triggered | The commit protocol only optimizes dynamic partition<br>overwrite cases. For other cases, see [Use the EMRFS S3-optimized<br>committer](emr-spark-s3-optimized-committer.md "emr-spark-s3-optimized-committer.md"). |

The following Scala examples demonstrate some additional situations that
the EMRFS S3-optimized commit protocol delegates to
`SQLHadoopMapReduceCommitProtocol`.

###### Example– Dynamic partition overwrite mode with custom partition

location

In this example, the Scala programs overwrites two partitions in
dynamic partition overwrite mode. One partition has a custom partition
location. The other partition uses the default partition location. The
EMRFS S3-optimized commit protocol only improves the partition that uses
the default partition location.

```
val table = "dataset"
val inputView = "tempView"
val location = "s3://bucket/table"

spark.sql(s"""
  CREATE TABLE $table (id bigint, dt date)
  USING PARQUET PARTITIONED BY (dt)
  LOCATION '$location'
""")

// Add a partition using a custom location
val customPartitionLocation = "s3://bucket/custom"
spark.sql(s"""
  ALTER TABLE $table ADD PARTITION (dt='2019-01-28')
  LOCATION '$customPartitionLocation'
""")

// Add another partition using default location
spark.sql(s"ALTER TABLE $table ADD PARTITION (dt='2019-01-29')")

def asDate(text: String) = lit(text).cast("date")

spark.range(0, 10)
  .withColumn("dt",
    when($"id" > 4, asDate("2019-01-28")).otherwise(asDate("2019-01-29")))
  .createTempView(inputView)

// Set partition overwrite mode to 'dynamic'
spark.sql(s"SET spark.sql.sources.partitionOverwriteMode=dynamic")

spark.sql(s"INSERT OVERWRITE TABLE $table SELECT * FROM $inputView")
```

The Scala code creates the following Amazon S3 objects:

```
custom/part-00001-035a2a9c-4a09-4917-8819-e77134342402.c000.snappy.parquet
custom_$folder$
table/_SUCCESS
table/dt=2019-01-29/part-00000-035a2a9c-4a09-4917-8819-e77134342402.c000.snappy.parquet
table/dt=2019-01-29_$folder$
table_$folder$
```

###### Note

Writing to custom partition locations in earlier Spark versions
may result in data loss. In this example, partition
`dt='2019-01-28'` would be lost. For more details,
see [SPARK-35106](https://issues.apache.org/jira/browse/SPARK-35106 "https://issues.apache.org/jira/browse/SPARK-35106"). This is fixed in Amazon EMR release 5.33.0 and
later, excluding 6.0.x and 6.1.x.

When writing to partitions at custom locations, Spark uses a commit
algorithm similar to the previous example, which is outlined below. As with
the earlier example, the algorithm results in sequential renames, which may
negatively impact performance.

The algorithm in Spark 2.4.0 follows these steps:

1. When writing output to a partition at a custom location, tasks
   write to a file under Spark's staging directory, which is created
   under the final output location. The name of the file includes a
   random UUID to protect against file collisions. The task attempt
   keeps track of each file along with the final desired output
   path.
2. When a task completes successfully, it provides the driver with
   the files and their final desired output paths.
3. After all tasks complete, the job commit phase sequentially
   renames all files that were written for partitions at custom
   locations to their final output paths.
4. The staging directory is deleted before the job commit phase
   completes.
