# Remove columns

You may need to remove columns from tables if they no longer contain data, or to
restrict access to the data in them.

- You can remove columns from tables in JSON, Avro, and in Parquet and ORC if
  they are read by name. For information, see [Understand index access for Apache ORC and Apache Parquet](handling-schema-updates-chapter.md#index-access "handling-schema-updates-chapter.md#index-access").
- We do not recommend removing columns from tables in CSV and TSV if you want to
  retain the tables you have already created in Athena. Removing a column breaks
  the schema and requires that you recreate the table without the removed
  column.
  In this example, remove a column `totalprice` from a table in Parquet and
  run a query. In Athena, Parquet is read by name by default, this is why we omit the
  SERDEPROPERTIES configuration that specifies reading by name. Notice that the following
  query succeeds, even though you changed the schema:

```
CREATE EXTERNAL TABLE orders_parquet_column_removed (
   `o_orderkey` int,
   `o_custkey` int,
   `o_orderstatus` string,
   `o_orderdate` string,
   `o_orderpriority` string,
   `o_clerk` string,
   `o_shippriority` int,
   `o_comment` string
)
STORED AS PARQUET
LOCATION 's3://amzn-s3-demo-bucket/orders_parquet/';

```
