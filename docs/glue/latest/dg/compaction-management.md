# Compaction optimization

The Amazon S3 data lakes using open table formats like Apache Iceberg store data as S3
objects. Having thousands of small Amazon S3 objects in a data lake table increases metadata overhead
and affects read performance. AWS Glue Data Catalog provides managed compaction for Iceberg tables,
compacting small objects into larger ones for better read performance by AWS analytics
services like Amazon Athena and Amazon EMR, and AWS Glue ETL jobs. Data Catalog performs compaction
without interfering with concurrent queries and supports compaction only for Parquet format
tables.

The table optimizer continuously monitors table partitions and kicks off the compaction
process when the threshold is exceeded for the number of files and file sizes.

In the Data Catalog, the compaction process starts when a table or any of its
partitions have more than 100 files. Each file must be smaller than 75% of the target file
size. The target file size is defined by the `write.target-file-size-bytes` table property,
which defaults to 512 MB if not explicitly set.

For limitations, see [Supported formats and limitations for managed data
compaction](optimizer-notes.md#compaction-notes "optimizer-notes.md#compaction-notes") .

###### Topics

- [Enabling compaction optimizer](enable-compaction.md "enable-compaction.md")
- [Disabling compaction optimizer](disable-compaction.md "disable-compaction.md")
