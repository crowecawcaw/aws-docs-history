# Make schema updates

This topic describes some of the changes that you can make to the schema in `CREATE
 TABLE` statements without actually altering your data. To update a schema, you can
in some cases use an `ALTER TABLE` command, but in other cases you do not
actually modify an existing table. Instead, you create a table with a new name that modifies
the schema that you used in your original `CREATE TABLE` statement.

Depending on how you expect your schemas to evolve, to continue using Athena queries,
choose a compatible data format.

Consider an application that reads orders information from an `orders` table
that exists in two formats: CSV and Parquet.

The following example creates a table in Parquet:

```
CREATE EXTERNAL TABLE orders_parquet (
   `orderkey` int,
   `orderstatus` string,
   `totalprice` double,
   `orderdate` string,
   `orderpriority` string,
   `clerk` string,
   `shippriority` int
) STORED AS PARQUET
LOCATION 's3://amzn-s3-demo-bucket/orders_ parquet/';

```

The following example creates the same table in CSV:

```
CREATE EXTERNAL TABLE orders_csv (
   `orderkey` int,
   `orderstatus` string,
   `totalprice` double,
   `orderdate` string,
   `orderpriority` string,
   `clerk` string,
   `shippriority` int
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
LOCATION 's3://amzn-s3-demo-bucket/orders_csv/';

```

The following topics show how updates to these tables affect Athena queries.

###### Topics

- [Add columns at the beginning or in the middle of the table](updates-add-columns-beginning-middle-of-table.md "updates-add-columns-beginning-middle-of-table.md")
- [Add columns at the end of the table](updates-add-columns-end-of-table.md "updates-add-columns-end-of-table.md")
- [Remove columns](updates-removing-columns.md "updates-removing-columns.md")
- [Rename columns](updates-renaming-columns.md "updates-renaming-columns.md")
- [Reorder columns](updates-reordering-columns.md "updates-reordering-columns.md")
- [Change a column data type](updates-changing-column-type.md "updates-changing-column-type.md")
