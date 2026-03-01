# What is partitioning?

Partitioning means organizing data into directories (or "prefixes") on Amazon S3 based on a
particular property of the data. Such properties are called _partition
keys_. A common partition key is the date or some other unit of time such
as the year or month. However, a dataset can be partitioned by more than one key. For
example, data about product sales might be partitioned by date, product category, and
market.

## Deciding how to partition

Good candidates for partition keys are properties that are always or frequently
used in queries and have low cardinality. There is a trade-off between having too
many partitions and having too few. With too many partitions, the increased number
of files creates overhead. There is also some overhead from filtering the partitions
themselves. With too few partitions, queries often have to scan more data.

## Create a partitioned table

When a dataset is partitioned, you can create a partitioned table in Athena. A
partitioned table is a table that has partition keys. When you use `CREATE
 TABLE`, you add partitions to the table. When you use `CREATE TABLE
 AS`, the partitions that are created on Amazon S3 are automatically added to
the table.

In a `CREATE TABLE` statement, you specify the partition keys in the
`PARTITIONED BY (`column_name`
`data_type`)` clause. In a `CREATE TABLE
 AS` statement, you specify the partition keys in a `WITH
 (partitioned_by = ARRAY['`partition_key`'])`
clause, or `WITH (partitioning =
 ARRAY['`partition_key`'])` for Iceberg
tables. For performance reasons, partition keys should always be of type
`STRING`. For more information, see [Use string as the data type for partition keys](data-types-timestamps.md#data-types-timestamps-partition-key-types "data-types-timestamps.md#data-types-timestamps-partition-key-types").

For additional `CREATE TABLE` and `CREATE TABLE AS` syntax
details, see [CREATE TABLE](create-table.md "create-table.md") and [CTAS table properties](create-table-as.md#ctas-table-properties "create-table-as.md#ctas-table-properties").

## Query partitioned tables

When you query a partitioned table, Athena uses the predicates in the query to
filter the list of partitions. Then it uses the locations of the matching partitions
to process the files found. Athena can efficiently reduce the amount of data scanned
by simply not reading data in the partitions that don't match the query
predicates.

### Examples

Suppose you have a table partitioned by `sales_date` and
`product_category` and want to know the total revenue over a week
in a specific category. You include predicates on the `sales_date`
and `product_category` columns to ensure that Athena scans only the
minimum amount of data, as in the following example.

```
SELECT SUM(amount) AS total_revenue
FROM sales
WHERE sales_date BETWEEN '2023-02-27' AND '2023-03-05'
AND product_category = 'Toys'
```

Suppose you have a dataset that is partitioned by date but also has a
fine-grained timestamp.

With Iceberg tables, you can declare a partition key to have a relationship to
a column, but with Hive tables the query engine has no knowledge of
relationships between columns and partition keys. For this reason, you must
include a predicate on both the column and the partition key in your query to
make sure the query does not scan more data than necessary.

For example, suppose the `sales` table in the previous example also
has a `sold_at` column of the `TIMESTAMP` data type. If
you want the revenue only for a specific time range, you would write the query
like this:

```
SELECT SUM(amount) AS total_revenue
FROM sales
WHERE sales_date = '2023-02-28'
AND sold_at BETWEEN TIMESTAMP '2023-02-28 10:00:00' AND TIMESTAMP '2023-02-28 12:00:00'
AND product_category = 'Toys'
```

For more information about this difference between querying Hive and Iceberg
tables, see [How to write queries for timestamp fields that are also time-partitioned](data-types-timestamps.md#data-types-timestamps-how-to-write-queries-for-timestamp-fields-that-are-also-time-partitioned "data-types-timestamps.md#data-types-timestamps-how-to-write-queries-for-timestamp-fields-that-are-also-time-partitioned").
