# Common challenges when scaling Trino workloads

The primary benefits of using Amazon S3 with Trino are S3's ability to scale for large
data volumes and S3's cost effectiveness. But when you query large data volumes, a collection of related performance issues can happen on occasion. These can result from how data is
stored, or
by configuration settings that restrict good performance, or from other reasons. When these issues occur, there are effective steps you can take to avoid or mitigate them.

This section begins with a list of general optimizations you can implement to increase query performance on large data volumes. Following that, common issues are detailed and
mitigations are provided for each one.

This topic is sourced from the following conference presentation: [Accelerate performance at scale: Best practices for Trino with Amazon S3](https://www.youtube.com/watch?v=cjUUcHlUKxQ "https://www.youtube.com/watch?v=cjUUcHlUKxQ").

## Optimizing data layout for large data sets

Performance bottlenecks aren't infrequent when you're querying large data sets. But there are best practices you can implement to give yourself a head start
when you use Trino to query data in Amazon S3. These include the following:

- **Partitioning** – Partitioning means to organize data in a hierarchy and to store related data
  together, based on related attributes. Partitioning makes it so queries don't have to scan as much irrelevant data and it results in better query
  performance. You can use various partitioning strategies, such as arranging source data
  with prefixes, specifically by date ranges regions, or other attributes. For more detailed information about
  partitioning data in Amazon S3 to increase performance, see the blog
  post [Get started managing partitions for Amazon S3 tables backed by
  the AWS Glue Data Catalog](https://aws.amazon.com/blogs/big-data/get-started-managing-partitions-for-amazon-s3-tables-backed-by-the-aws-glue-data-catalog/ "https://aws.amazon.com/blogs/big-data/get-started-managing-partitions-for-amazon-s3-tables-backed-by-the-aws-glue-data-catalog/") or the post [Top 10 Performance Tuning Tips for Amazon Athena](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/ "https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/").
- **Bucketing** – Bucketing is grouping related data together in common files. For instance, if you
  query data according to a geographic region, like a state, you can boost query performance by grouping all data for a particular state in the same file or group of
  files. For this to work best, base your bucketing on a data attribute with high cardinality, such as a state or province, for instance. Also, you can take your query
  patterns into account. An example of this could mean grouping data for California and Oregon together,
  if your queries typically read data from those states together.
- **Managing S3 prefixes** – You can use Amazon S3 prefixes to implement a partitioning strategy. If you use only a single prefix for an Amazon S3 bucket, like a particular date, for instance, this can lead to a high number of requests
  and can result in an HTTP 503 error. We recommend using prefixes to add additional conditions and organize your source data more effectively. For more information,
  see [Organizing objects using prefixes](../../../AmazonS3/latest/userguide/using-prefixes.md "../../../AmazonS3/latest/userguide/using-prefixes.md") in the Amazon S3 documentation. The following brief example shows a prefix that results in better
  request throughput: `s3://bucket/country=US/dt=2024-06-13`. In this sample, both the country and date are included in the prefix, which results in fewer reads than a
  case where the prefix includes only the date.

Mitigating HTTP 503 errors is discussed in more detail in the _HTTP slow down_ section that follows in this topic.

- **Optimizing data size** – You can run the OPTIMIZE command to set configuration that's conducive to queries that perform better.
  To run it against Hive external tables,
  follow these steps:
  - Use `OPTIMIZE` with the following parameter: `hive.non-managed-table-writes-enabled=true`. For more information about this property,
    see [Hive general configuration properties](https://trino.io/docs/current/connector/hive.html#hive-general-configuration-properties "https://trino.io/docs/current/connector/hive.html#hive-general-configuration-properties").
  - Set the following session parameter: `SET SESSION` ``catalog`.non_transactional_optimize_enabled=true`
  - Run the `OPTIMIZE` command: `ALTER TABLE `catalog`.`schema`.`table` EXECUTE optimize(file_size_threshold => '128MB')`.
    In this case, `file_size_threshold` is 100MB by default. Raising this threshold, as shown in the sample, will cause files below 128MB to be merged.

- **Configure retries** – You can increase the retry limit, which can mitigate the chance of HTTP 503 errors, by setting the
  following: `s3.max-error-retries`. This applies when you use the TrinoFileSystem API and Trino 449 version or later. On the other hand, in the case where you're using Amazon EMR with Trino, you use EMRFS to access Amazon S3. With EMRFS, you can increase the number of retires by
  changing the `fs.s3.maxRetries` parameter.
- **Choose an Amazon S3 storage class** – Choosing the appropriate storage class for data at different points in its lifecycle can help both with performance and
  cost, based on your requirements for specific data collections.
  For more information, see [Understanding and managing Amazon S3 storage classes](../../../AmazonS3/latest/userguide/storage-class-intro.md "../../../AmazonS3/latest/userguide/storage-class-intro.md") in
  the Amazon S3 documentation.
- **Migrate to Iceberg** – Another solution to mitigate performance issues, specifically regarding running queries on small files, is to migrate to Iceberg tables. Iceberg has features that handle small files well.
- **Use automatic data compaction** – If you utilize Iceberg tables, automatic data compaction with the AWS Glue Data Catalog can optimize data size and result in better query performance.

## Common challenges when you query large data sets

This section lists a collection of common issues that can occur when you accumulate a large data set in Amazon S3 and query it
with Trino. Each section shows you ways to solve the issue or reduce its impact on queries. Each of the issues described in the following sections has been reproduced and tested, using
a Hive connector.

### Large data scans

When your query has to scan large data sets, it can lead to issues like slow query performance and higher storage cost. Large data volumes can result from fast data growth or
planning that doesn't result in moving legacy data within an appropriate time frame. This can lead to slower queries.

To mitigate performance hits from scanning large data sets, we recommend that you utilize partitioning and bucketing:

- Partitioning groups related data together, based on its attributes. Using partitioning effectively can greatly
  improve query performance.
- Bucketing refers to grouping data in files or buckets according to specific, related data columns. Bucketing typically means physically keeping
  related source data files together.

To illustrate how mitigation can work for large data scans, assume you store and query data that has records with a state attribute,
which can be assigned to California or Alaska, and this state attribute is one of your query conditions. You can improve query performance by storing data for each
state in a separate S3 bucket, or partitioning your data based on the state, using an S3 prefix. This partitioning and bucketing can also cause performance improvement if
you base it on an additional column, like a date attribute, for example.

###### Note

If a column has high cardinality, and you want to use it to group data, we recommend using bucketing in this case. On the other hand, generally, partition keys
should have lower cardinality.

**Using various S3 storage types**

Generally, you choose storage types based on performance, data access, resiliency, and cost requirements for your workloads. There can be trade offs between cost and performance. It's important
to choose the appropriate Amazon S3 storage class that matches your data access patterns. There are two main access patterns:

- Data that's accessed in a known or predictable manner. Generally, if you have data that is accessed infrequently, S3 Standard IA can be a good choice, because it
  helps reduce cost. If you have frequently accessed data, S3 Standard is best for access with Amazon EMR and Trino.
- Data that's accessed in an unknown or unpredictable manner. This can call for using other Amazon S3 storage classes, There are trade offs between S3 storage classes. These include latency, storage
  cost and availability. You can choose an appropriate S3 storage type, based on your workloads and access patterns. For descriptions of the benefits of each class,
  see Amazon S3 Storage Classes.

**Using compaction**

You can also use Iceberg automatic compaction, if you use Iceberg tables, which results in more optimal file sizes, to increase query efficiency. For more
information, see [AWS Glue Data Catalog now
supports automatic compaction of Apache Iceberg tables](https://aws.amazon.com/blogs/aws/aws-glue-data-catalog-now-supports-automatic-compaction-of-apache-iceberg-tables/ "https://aws.amazon.com/blogs/aws/aws-glue-data-catalog-now-supports-automatic-compaction-of-apache-iceberg-tables/").

### HTTP slow-down errors

This occurs when the request rate exceeds a pre-configured threshold on an Amazon S3 prefix. The HTTP error that occurs most commonly when this state is reached is the
following: **Error 503: Please reduce your request rate**. The source for this issue can be rooted in the presence of a large
number of small files, because of the number of _splits_ that must be created in order to read the data. There are a couple ways to mitigate the issue:

- Increase the retry limit for Amazon S3 requests in Trino. This is set for EMRFS
  using `fs.s3.maxretries` in Trino 449.
- Optimize file sizes, which can also result in a lower request rate.

For more information about how Trino determines the number of splits in a set of data to query,
see [Performance tuning configuration properties](https://trino.io/docs/current/connector/hive.html#performance-tuning-configuration-properties "https://trino.io/docs/current/connector/hive.html#performance-tuning-configuration-properties") in the Hive connector documentation.

### Difficulty querying small files

Querying many small files can result in heavy I/O overhead, because of a high number of GET and LIST requests, and subsequently affect query performance
negatively. Optimizing file size can improve query performance. There are a few
ways to do this:

- Consolidate data into fewer larger files. (Generally, we recommend keeping file sizes at around 128 MB.) You can do this with tools when you ingest data, such as in an ETL pipeline, or you can consolidate data manually. If these solutions
  aren't available to you, the remaining options might be better suited for you.
- Run the `OPTIMIZE` command.
- Set the `SESSION` parameter.

Take note that Iceberg has a feature available to merge small files into larger files which is automatic compaction. It works with files managed
with the AWS Glue Data Catalog. For more information, see [AWS Glue Data Catalog now
supports automatic compaction of Apache Iceberg tables](https://aws.amazon.com/blogs/aws/aws-glue-data-catalog-now-supports-automatic-compaction-of-apache-iceberg-tables/ "https://aws.amazon.com/blogs/aws/aws-glue-data-catalog-now-supports-automatic-compaction-of-apache-iceberg-tables/").

### Queries that include data that isn't needed

It's common for data to grow, which makes it imperative to track your data-access patterns and to move data appropriately as it ages or becomes irrelevant. This is because
as data grows, query performance
can degrade over time, mainly because of the sheer volume of data to
scan when a query runs. Amazon S3 and other services offer guidance for data-lifecycle migration, which shows strategies for moving data to different storage locations
as it becomes cold. There is also a storage cost benefit to doing this.

In addition to data migration, you can use other strategies like removing source data that isn't
relevant to the queries you're running. This can take some work, as it might mean changing your source-data schema. But its positive result is to reduce data volume and
result in faster queries. For more information, see [Managing the lifecycle of objects](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md").
