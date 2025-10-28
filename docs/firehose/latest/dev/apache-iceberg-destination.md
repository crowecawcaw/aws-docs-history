# Deliver data to Apache Iceberg Tables with

Amazon Data Firehose

Apache Iceberg is a high-performance open-source table format for performing big data
analytics. Apache Iceberg brings the reliability and simplicity of SQL tables to Amazon S3 data
lakes, and makes it possible for open-source analytics engines like Spark, Flink, Trino,
Hive, and Impala to work with the same data concurrently. For more information, see [Apache Iceberg](https://iceberg.apache.org "https://iceberg.apache.org") and [Considerations and limitations](apache-iceberg-considerations.md "apache-iceberg-considerations.md").

You can use Firehose to deliver streaming data to Apache Iceberg Tables in Amazon S3. Your Apache
Iceberg Tables can be in self-managed in Amazon S3 or hosted in Amazon S3 Tables. In self-managed
Iceberg tables, you manage all the table optimizations such as compaction, and snapshot
expiration. Amazon S3 Tables provide storage that is optimized for large-scale analytics
workloads, with features that continuously improve query performance and reduce storage
costs for tabular data. For more information on Amazon S3 Tables, see [Amazon S3
Tables](../../../AmazonS3/latest/userguide/s3-tables.md "../../../AmazonS3/latest/userguide/s3-tables.md").

This feature allows you to route records from a single stream into different Apache Iceberg
Tables. You can automatically apply insert, update, and delete operations to records in
those tables. It also supports fine-grained data access control on Apache Iceberg tables in
Amazon S3 with AWS Lake Formation. You can specify access controls centrally in AWS Lake Formation and provide more
granular table-level and column-level permissions for Firehose.
