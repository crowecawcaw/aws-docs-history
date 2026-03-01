# Optimize your tables

Structuring your data is important if you encounter throttling issues. Although Amazon S3
can handle large amounts of data, throttling sometimes occurs because of the way the
data is structured.

The following sections offer some suggestions on how to structure your data in Amazon S3 to
avoid throttling issues.

## Use partitioning

You can use partitioning to reduce throttling by limiting the amount of data that
has to be accessed at any given time. By partitioning data on specific columns, you
can distribute requests evenly across multiple objects and reduce the number of
requests for a single object. Reducing the amount of data that must be scanned
improves query performance and lowers cost.

You can define partitions, which act as virtual columns, when you create a table.
To create a table with partitions in a `CREATE TABLE` statement, you use
the `PARTITIONED BY (`column_name`
`data_type`)` clause to define the keys to
partition your data.

To restrict the partitions scanned by a query, you can specify them as predicates
in a `WHERE` clause of the query. Thus, columns that are frequently used
as filters are good candidates for partitioning. A common practice is to partition
the data based on time intervals, which can lead to a multi-level partitioning
scheme.

Note that partitioning also has a cost. When you increase the number of partitions
in your table, the
time required
to retrieve and process partition metadata also increases. Thus,
over-partitioning can remove the benefits you gain by partitioning more judiciously.
If your data is heavily skewed to one partition value, and most queries use that
value, then you may incur the additional overhead.

For more information about partitioning in Athena, see [What is partitioning?](ctas-partitioning-and-bucketing-what-is-partitioning.md "ctas-partitioning-and-bucketing-what-is-partitioning.md")

## Bucket your data

Another way to partition your data is to bucket the data within a single
partition. With bucketing, you specify one or more columns that contain rows that
you want to group together. Then, you put those rows into multiple buckets. This
way, you query only the bucket that must be read, which reduces the number of rows
of data that must be scanned.

When you select a column to use for bucketing, select the column that has high
cardinality (that is, that has many distinct values), is uniformly distributed, and
is frequently used to filter the data. An example of a good column to use for
bucketing is a primary key, such as an ID column.

For more information about bucketing in Athena, see [What is bucketing?](ctas-partitioning-and-bucketing-what-is-bucketing.md "ctas-partitioning-and-bucketing-what-is-bucketing.md")

## Use AWS Glue partition indexes

You can use AWS Glue partition indexes to organize data in a table based on the
values of one or more partitions. AWS Glue partition indexes can reduce the number of
data transfers, the amount of data processing, and the time for queries to
process.

An AWS Glue partition index is a metadata file that contains information about the
partitions in the table, including the partition keys and their values. The
partition index is stored in an Amazon S3 bucket and is updated automatically by AWS Glue as
new partitions are added to the table.

When an AWS Glue partition index is present, queries attempt to fetch a subset of the
partitions instead of loading all the partitions in the table. Queries only run on
the subset of data that is relevant to the query.

When you create a table in AWS Glue, you can create a partition index on any
combination of partition keys defined on the table. After you have created one or
more partition indexes on a table, you must add a property to the table that enables
partition filtering. Then, you can query the table from Athena.

For information about creating partition indexes in AWS Glue, see [Working with
partition indexes in AWS Glue](../../../glue/latest/dg/partition-indexes.md "../../../glue/latest/dg/partition-indexes.md") in the _AWS Glue Developer Guide_. For information about adding a table property to
enable partition filtering, see [Optimize queries with AWS Glue partition indexing and filtering](glue-best-practices-partition-index.md "glue-best-practices-partition-index.md").

## Use data compression and file splitting

Data compression can speed up queries significantly if files are at their optimal
size or if they can be split into logical groups. Generally, higher compression
ratios require more CPU cycles to compress and decompress the data. For Athena, we
recommend that you use either Apache Parquet or Apache ORC, which compress data by
default. For information about data compression in Athena, see [Use compression in Athena](compression-formats.md "compression-formats.md").

Splitting files increases parallelism by allowing Athena to distribute the task of
reading a single file among multiple readers. If a single file is not splittable,
only a single reader can read the file while other readers are idle. Apache Parquet
and Apache ORC also support splittable files.

## Use optimized columnar data stores

Athena query performance improves significantly if you convert your data into a
columnar format. When you generate columnar files, one optimization technique to
consider is ordering the data based on partition key.

Apache Parquet and Apache ORC are commonly used open source columnar data stores.
For information on converting existing Amazon S3 data source to one of these formats, see
[Convert to columnar formats](columnar-storage.md#convert-to-columnar "columnar-storage.md#convert-to-columnar").

### Use a larger Parquet block size or ORC stripe size

Parquet and ORC have data storage parameters that you can tune for
optimization. In Parquet, you can optimize for block size. In ORC, you can
optimize for stripe size. The larger the block or stripe, the more rows that you
can store in each. By default, the Parquet block size is 128 MB, and the ORC
stripe size is 64 MB.

If an ORC stripe is less than 8 MB (the default value of
`hive.orc.max_buffer_size`), Athena reads the whole ORC stripe.
This is the tradeoff Athena makes between column selectivity and input/output
operations per second for smaller stripes.

If you have tables with
a very
large number of columns, a small block or
stripe size can cause more data to be scanned than necessary. In these cases, a
larger block size can be more efficient.

### Use ORC for complex types

Currently, when you query columns stored in Parquet that have complex data
types (for example, `array`, `map`, or
`struct`), Athena reads an entire row of data instead of selectively
reading only the specified columns. This is a known issue in Athena. As a
workaround, consider using ORC.

### Choose a compression algorithm

Another parameter that you can configure is the compression algorithm on data
blocks. For information about the compression algorithms supported for Parquet
and ORC in Athena, see [Athena compression support](compression-formats.md "compression-formats.md").

For more information about optimization of columnar storage formats in Athena,
see the section "Optimize columnar data store generation" in the AWS Big Data
Blog post [Top 10 Performance Tuning Tips for Amazon Athena](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/ "https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/").

## Use Iceberg tables

Apache Iceberg is an open table format for very large analytic datasets that is
designed for optimized usage on Amazon S3. You can use Iceberg tables to help reduce
throttling in Amazon S3.

Iceberg tables offer you the following advantages:

- You can partition Iceberg tables on one or more columns. This optimizes
  data access and reduces the amount of data that must be scanned by
  queries.
- Because Iceberg object storage mode optimizes Iceberg tables to work with
  Amazon S3, it can process large volumes of data and heavy query workloads.
- Iceberg tables in object storage mode are scalable, fault tolerant, and
  durable, which can help reduce throttling.
- ACID transaction support means that multiple users can add and delete Amazon S3
  objects in an atomic manner.

For more information about Apache Iceberg, see [Apache Iceberg](https://iceberg.apache.org/ "https://iceberg.apache.org/"). For more information
about using Apache Iceberg tables in Athena, see [Using
Iceberg tables](querying-iceberg.md "querying-iceberg.md").
