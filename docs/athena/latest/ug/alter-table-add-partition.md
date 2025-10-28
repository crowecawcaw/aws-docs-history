# ALTER TABLE ADD PARTITION

Creates one or more partition columns for the table. Each partition consists of one or
more distinct column name/value combinations. A separate data directory is created for each
specified combination, which can improve query performance in some circumstances.
Partitioned columns don't exist within the table data itself, so if you use a column name
that has the same name as a column in the table itself, you get an error. For more
information, see [Partition your data](partitions.md "partitions.md").

In Athena, a table and its partitions must use the same data formats but their schemas may
differ. For more information, see [Update tables with partitions](updates-and-partitions.md "updates-and-partitions.md").

For information about the resource-level permissions required in IAM policies (including
`glue:CreatePartition`), see [AWS Glue API permissions: Actions and
resources reference](../../../glue/latest/dg/api-permissions-reference.md "../../../glue/latest/dg/api-permissions-reference.md") and [Configure access to databases and
tables in the AWS Glue Data Catalog](fine-grained-access-to-glue-resources.md "fine-grained-access-to-glue-resources.md"). For troubleshooting information
about permissions when using Athena, see the [Permissions](troubleshooting-athena.md#troubleshooting-athena-permissions "troubleshooting-athena.md#troubleshooting-athena-permissions") section of the [Troubleshoot issues in Athena](troubleshooting-athena.md "troubleshooting-athena.md") topic.

## Synopsis

```
ALTER TABLE table_name ADD [IF NOT EXISTS]
  PARTITION
  (partition_col1_name = partition_col1_value
  [,partition_col2_name = partition_col2_value]
  [,...])
  [LOCATION 'location1']
  [PARTITION
  (partition_colA_name = partition_colA_value
  [,partition_colB_name = partition_colB_value
  [,...])]
  [LOCATION 'location2']
  [,...]
```

## Parameters

When you add a partition, you specify one or more column name/value pairs for the
partition and the Amazon S3 path where the data files for that partition reside.

**[IF NOT EXISTS]**

Causes the error to be suppressed if a partition with the same definition
already exists.

**PARTITION (partition_col_name = partition_col_value [,...])**

Creates a partition with the column name/value combinations that you
specify. Enclose `partition_col_value` in string characters only
if the data type of the column is a string.

**[LOCATION 'location']**

Specifies the directory in which to store the partition defined by the
preceding statement. The `LOCATION` clause is optional when the
data uses Hive-style partitioning (`pk1=v1/pk2=v2/pk3=v3`). With
Hive-style partitioning, the full Amazon S3 URI is constructed automatically from
the table's location, the partition key names, and the partition key values.
For more information, see [Partition your data](partitions.md "partitions.md").

## Considerations

Amazon Athena does not impose a specific limit on the number of partitions you can add in
a single `ALTER TABLE ADD PARTITION` DDL statement. However, if you need to
add a significant number of partitions, consider breaking the operation into smaller
batches to avoid potential performance issues. The following example uses successive
commands to add partitions individually and uses `IF NOT EXISTS` to avoid
adding duplicates.

```
ALTER TABLE `table_name` ADD IF NOT EXISTS PARTITION (ds='2023-01-01')
ALTER TABLE `table_name` ADD IF NOT EXISTS PARTITION (ds='2023-01-02')
ALTER TABLE `table_name` ADD IF NOT EXISTS PARTITION (ds='2023-01-03')
```

When working with partitions in Athena, also keep in mind the following points:

- Although Athena supports querying AWS Glue tables that have 10 million partitions,
  Athena cannot read more than 1 million partitions in a single scan.
- To optimize your queries and reduce the number of partitions scanned, consider
  strategies like partition pruning or using partition indexes.

For additional considerations regarding working with partitions in Athena, see [Partition your data](partitions.md "partitions.md").

## Examples

The following example adds a single partition to a table for Hive-style partitioned
data.

```
ALTER TABLE orders ADD
  PARTITION (dt = '2016-05-14', country = 'IN');
```

The following example adds multiple partitions to a table for Hive-style partitioned
data.

```
ALTER TABLE orders ADD
  PARTITION (dt = '2016-05-31', country = 'IN')
  PARTITION (dt = '2016-06-01', country = 'IN');
```

When the table is not for Hive-style partitioned data, the `LOCATION`
clause is required and should be the full Amazon S3 URI for the prefix that contains the
partition's data.

```
ALTER TABLE orders ADD
  PARTITION (dt = '2016-05-31', country = 'IN') LOCATION 's3://amzn-s3-demo-bucket/path/to/INDIA_31_May_2016/'
  PARTITION (dt = '2016-06-01', country = 'IN') LOCATION 's3://amzn-s3-demo-bucket/path/to/INDIA_01_June_2016/';
```

To ignore errors when the partition already exists, use the `IF NOT EXISTS`
clause, as in the following example.

```
ALTER TABLE orders ADD IF NOT EXISTS
  PARTITION (dt = '2016-05-14', country = 'IN');
```

## Zero byte

`_$folder$` files

If you run an `ALTER TABLE ADD PARTITION` statement and mistakenly specify
a partition that already exists and an incorrect Amazon S3 location, zero byte placeholder
files of the format
``partition_value`\_$folder$` are created
in Amazon S3. You must remove these files manually.

To prevent this from happening, use the `ADD IF NOT EXISTS` syntax in your
`ALTER TABLE ADD PARTITION` statement, as in the following
example.

```
ALTER TABLE table_name ADD IF NOT EXISTS PARTITION […]
```
