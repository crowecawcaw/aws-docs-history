# What is bucketing?

Bucketing is a way to organize the records of a dataset into categories called
_buckets_.

This meaning of _bucket_ and _bucketing_ is
different from, and should not be confused with, Amazon S3 buckets. In data bucketing,
records that have the same value for a property go into the same bucket. Records are
distributed as evenly as possible among buckets so that each bucket has roughly the same
amount of data.

In practice, the buckets are files, and a hash function determines the bucket that a
record goes into. A bucketed dataset will have one or more files per bucket per
partition. The bucket that a file belongs to is encoded in the file name.

## Bucketing benefits

Bucketing is useful when a dataset is bucketed by a certain property and you want
to retrieve records in which that property has a certain value. Because the data is
bucketed, Athena can use the value to determine which files to look at. For example,
suppose a dataset is bucketed by `customer_id` and you want to find all
records for a specific customer. Athena determines the bucket that contains those
records and only reads the files in that bucket.

Good candidates for bucketing occur when you have columns that have high
cardinality (that is, have many distinct values), are uniformly distributed, and
that you frequently query for specific values.

###### Note

Athena does not support using `INSERT INTO` to add new records to
bucketed tables.

## Data types supported for filtering on bucketed columns

You can add filters on bucketed columns with certain data types. Athena supports
filtering on bucketed columns with the following data types:

- BOOLEAN
- BYTE
- DATE
- DOUBLE
- FLOAT
- INT
- LONG
- SHORT
- STRING
- VARCHAR

## Hive and Spark support

Athena engine version 2 supports datasets bucketed using the Hive bucket algorithm, and Athena engine version 3
also supports the Apache Spark bucketing algorithm. Hive bucketing is the default.
If your dataset is bucketed using the Spark algorithm, use the
`TBLPROPERTIES` clause to set the `bucketing_format`
property value to `spark`.

###### Note

Athena has a limit of 100 partitions in a `CREATE TABLE AS SELECT`
([CTAS](ctas.md "ctas.md")) query. Similarly,
you can add only a maximum of 100 partitions to a destination table with an
[INSERT INTO](insert-into.md "insert-into.md") statement.

If you exceed this limitation, you may receive the error message
**`HIVE_TOO_MANY_OPEN_PARTITIONS: Exceeded limit of 100 open writers
 for partitions/buckets`**. To work around this limitation, you can
use a CTAS statement and a series of `INSERT INTO` statements that
create or insert up to 100 partitions each. For more information, see [Use CTAS and INSERT INTO to work around the 100 partition limit](ctas-insert-into.md "ctas-insert-into.md").

To create a table for an existing bucketed dataset, use the `CLUSTERED BY
 (`column`)` clause followed
by the `INTO `N` BUCKETS` clause. The
`INTO `N` BUCKETS` clause specifies the
number of buckets the data is bucketed into.

In the following `CREATE TABLE` example, the `sales`
dataset is bucketed by `customer_id` into 8 buckets using the Spark
algorithm. The `CREATE TABLE` statement uses the `CLUSTERED
 BY` and `TBLPROPERTIES` clauses to set the properties
accordingly.

```
CREATE EXTERNAL TABLE sales (...)
...
CLUSTERED BY (`customer_id`) INTO 8 BUCKETS
...
TBLPROPERTIES (
  'bucketing_format' = 'spark'
)
```

To specify bucketing with `CREATE TABLE AS`, use the
`bucketed_by` and `bucket_count` parameters, as in the
following example.

```
CREATE TABLE sales
WITH (
  ...
  bucketed_by = ARRAY['customer_id'],
  bucket_count = 8
)
AS SELECT ...
```

The following example query looks for the names of products that a specific
customer has purchased over the course of a week.

```
SELECT DISTINCT product_name
FROM sales
WHERE sales_date BETWEEN '2023-02-27' AND '2023-03-05'
AND customer_id = 'c123'
```

If this table is partitioned by `sales_date` and bucketed by
`customer_id`, Athena can calculate the bucket that the customer
records are in. At most, Athena reads one file per partition.
