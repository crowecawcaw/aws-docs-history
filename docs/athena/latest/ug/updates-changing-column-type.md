# Change a column data type

You might want to use a different column type when the existing type can no longer
hold the amount of information required. For example, an ID column's values might exceed
the size of the `INT` data type and require the use of the
`BIGINT` data type.

## Considerations

When planning to use a different data type for a column, consider the following
points:

- In most cases, you cannot change the data type of a column directly.
  Instead, you re-create the Athena table and define the column with the new
  data type.
- Only certain data types can be read as other data types. See the table in
  this section for data types that can be so treated.
- For data in Parquet and ORC, you cannot use a different data type for a
  column if the table is not partitioned.
- For partitioned tables in Parquet and ORC, a partition's column type can
  be different from another partition's column type, and Athena will
  `CAST` to the desired type, if possible. For information, see
  [Avoid schema mismatch
  errors for tables with partitions](updates-and-partitions.md#partitions-dealing-with-schema-mismatch-errors "updates-and-partitions.md#partitions-dealing-with-schema-mismatch-errors").
- For tables created using the [LazySimpleSerDe](lazy-simple-serde.md "lazy-simple-serde.md") only, it is
  possible to use the `ALTER TABLE REPLACE COLUMNS` statement to
  replace existing columns with a different data type, but all existing
  columns that you want to keep must also be redefined in the statement, or
  they will be dropped. For more information, see [ALTER TABLE REPLACE
  COLUMNS](alter-table-replace-columns.md "alter-table-replace-columns.md").
- For Apache Iceberg tables only, you can use the [ALTER TABLE CHANGE
  COLUMN](querying-iceberg-alter-table-change-column.md "querying-iceberg-alter-table-change-column.md") statement
  to change the data type of a column. `ALTER TABLE REPLACE
COLUMNS` is not supported for Iceberg tables. For more
  information, see [Evolve Iceberg table
  schema](querying-iceberg-evolving-table-schema.md "querying-iceberg-evolving-table-schema.md").

###### Important

We strongly suggest that you test and verify your queries before performing
data type translations. If Athena cannot use the target data type, the
`CREATE TABLE` query may fail.

## Use

compatible data types

Whenever possible, use compatible data types. The following table lists data types
that can be treated as other data types:

| Original data type | Available target data types                    |
| ------------------ | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `STRING`           | `BYTE`, `TINYINT`, `SMALLINT`, `INT`, `BIGINT` |
| `BYTE`             | `TINYINT`, `SMALLINT`, `INT`, `BIGINT`         |
| `TINYINT`          | `SMALLINT`, `INT`, `BIGINT`                    |
| `SMALLINT`         | `INT`, `BIGINT`                                |
| `INT`              | `BIGINT`                                       |
| `FLOAT`            | `DOUBLE`                                       | The following example uses the `CREATE TABLE` statement for the original `orders_json` table to create a new table called `orders_json_bigint`. The new table uses `BIGINT` instead of `INT` as the data type for the `o_shippriority` column. ``CREATE EXTERNAL TABLE orders_json_bigint ( `o_orderkey` int, `o_custkey` int, `o_orderstatus` string, `o_totalprice` double, `o_orderdate` string, `o_orderpriority` string, `o_clerk` string, `o_shippriority` BIGINT ) ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe' LOCATION 's3://amzn-s3-demo-bucket/orders_json';`` The following query runs successfully, similar to the original `SELECT` query, before the data type change: `Select * from orders_json LIMIT 10;` |
