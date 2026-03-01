# Add columns at the beginning or in the middle of the table

Adding columns is one of the most frequent schema changes. For example, you may add a
new column to enrich the table with new data. Or, you may add a new column if the source
for an existing column has changed, and keep the previous version of this column, to
adjust applications that depend on them.

To add columns at the beginning or in the middle of the table, and continue running
queries against existing tables, use AVRO, JSON, and Parquet and ORC if their SerDe
property is set to read by name. For information, see [Understand index access for Apache ORC and Apache Parquet](handling-schema-updates-chapter.md#index-access "handling-schema-updates-chapter.md#index-access").

Do not add columns at the beginning or in the middle of the table in CSV and TSV, as
these formats depend on ordering. Adding a column in such cases will lead to schema
mismatch errors when the schema of partitions changes.

The following example creates a new table that adds an `o_comment` column
in the middle of a table based on JSON data.

```
CREATE EXTERNAL TABLE orders_json_column_addition (
   `o_orderkey` int,
   `o_custkey` int,
   `o_orderstatus` string,
   `o_comment` string,
   `o_totalprice` double,
   `o_orderdate` string,
   `o_orderpriority` string,
   `o_clerk` string,
   `o_shippriority` int,
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://amzn-s3-demo-bucket/orders_json/';

```
