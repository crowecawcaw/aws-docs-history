# Rename columns

You may want to rename columns in your tables to correct spelling, make column names
more descriptive, or to reuse an existing column to avoid column reordering.

You can rename columns if you store your data in CSV and TSV, or in Parquet and ORC
that are configured to read by index. For information, see [Understand index access for Apache ORC and Apache Parquet](handling-schema-updates-chapter.md#index-access "handling-schema-updates-chapter.md#index-access").

Athena reads data in CSV and TSV in the order of the columns in the schema and returns
them in the same order. It does not use column names for mapping data to a column, which
is why you can rename columns in CSV or TSV without breaking Athena queries.

One strategy for renaming columns is to create a new table based on the same
underlying data, but using new column names. The following example creates a new
`orders_parquet` table called `orders_parquet_column_renamed`.
The example changes the column `o_totalprice` name to
`o_total_price` and then runs a query in Athena:

```
CREATE EXTERNAL TABLE orders_parquet_column_renamed (
   `o_orderkey` int,
   `o_custkey` int,
   `o_orderstatus` string,
   `o_total_price` double,
   `o_orderdate` string,
   `o_orderpriority` string,
   `o_clerk` string,
   `o_shippriority` int,
   `o_comment` string
)
STORED AS PARQUET
LOCATION 's3://amzn-s3-demo-bucket/orders_parquet/';

```

In the Parquet table case, the following query runs, but the renamed column does not
show data because the column was being accessed by name (a default in Parquet) rather
than by index:

```
SELECT *
FROM orders_parquet_column_renamed;
```

A query with a table in CSV looks similar:

```
CREATE EXTERNAL TABLE orders_csv_column_renamed (
   `o_orderkey` int,
   `o_custkey` int,
   `o_orderstatus` string,
   `o_total_price` double,
   `o_orderdate` string,
   `o_orderpriority` string,
   `o_clerk` string,
   `o_shippriority` int,
   `o_comment` string
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
LOCATION 's3://amzn-s3-demo-bucket/orders_csv/';

```

In the CSV table case, the following query runs and the data displays in all columns,
including the one that was renamed:

```
SELECT *
FROM orders_csv_column_renamed;
```
