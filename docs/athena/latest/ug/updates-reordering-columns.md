# Reorder columns

You can reorder columns only for tables with data in formats that read by name, such
as JSON or Parquet, which reads by name by default. You can also make ORC read by name,
if needed. For information, see [Understand index access for Apache ORC and Apache
Parquet](handling-schema-updates-chapter.md#index-access "handling-schema-updates-chapter.md#index-access").

The following example creates a new table with the columns in a different
order:

```
CREATE EXTERNAL TABLE orders_parquet_columns_reordered (
   `o_comment` string,
   `o_orderkey` int,
   `o_custkey` int,
   `o_orderpriority` string,
   `o_orderstatus` string,
   `o_clerk` string,
   `o_shippriority` int,
   `o_orderdate` string
)
STORED AS PARQUET
LOCATION 's3://amzn-s3-demo-bucket/orders_parquet/';

```
