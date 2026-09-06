Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SQL commands

Apache Iceberg tables in Amazon Redshift provide a powerful way to manage large analytic
datasets in your data lake. These tables support ACID transactions, schema
evolution, and time travel capabilities while maintaining high performance for
analytics workloads. Using Apache Iceberg tables, you can efficiently organize and
partition your data, control file formats and compression, and seamlessly integrate
with other AWS services.

You can create partitioned and unpartitioned Iceberg tables using `CREATE TABLE
 ... USING ICEBERG` and `CREATE TABLE ... USING ICEBERG AS SELECT`
commands. You can reference Iceberg tables using either external schema notation
(`external_schema.table_name`) or three-part notation
(`"catalog_name".database_name.table_name`). The examples in this section
demonstrate both methods.

After you create a table, you can add data using standard `INSERT`
commands. Keep in mind that while Amazon Redshift works with many Iceberg data types, you might
need to convert some data formats when inserting information.

You can view Iceberg tables using `SHOW TABLES` command. If you want to
remove a table from the AWS Glue Data Catalog, you can use the `DROP TABLE` command.
Note that this only removes the table registration. The actual data will stay in storage
until you delete it separately.

You can also modify existing data using `DELETE`,
`UPDATE`, and `MERGE` commands. To change table definitions
such as schema, partition specs, and properties, see [Altering table definitions](iceberg-alter-table.md "iceberg-alter-table.md"). Other DDL
statements not documented there are not supported for Iceberg tables.

It's possible for you to write into an Iceberg table that is not created by Amazon Redshift.
However, there are some limitations:

- The table must be an Iceberg v2 or v3 table.
- The table must be using Parquet as default data format.
- The table must not have metadata compression set to True.
- The table must not enable Write-Audit-Publish (WAP).
  The following sections demonstrate SQL syntax for creating, inserting, modifying, and
  managing Iceberg tables in Amazon Redshift.

###### Contents

- [CREATE TABLE](iceberg-writes-sql-syntax.md#iceberg-writes-create-table "iceberg-writes-sql-syntax.md#iceberg-writes-create-table")
- [CREATE TABLE AS SELECT](iceberg-writes-sql-syntax.md#iceberg-writes-create-table-as-select "iceberg-writes-sql-syntax.md#iceberg-writes-create-table-as-select")
- [SHOW TABLE](iceberg-writes-sql-syntax.md#iceberg-writes-show-table "iceberg-writes-sql-syntax.md#iceberg-writes-show-table")
- [INSERT INTO](iceberg-writes-sql-syntax.md#iceberg-writes-insert-into "iceberg-writes-sql-syntax.md#iceberg-writes-insert-into")
- [DELETE](iceberg-writes-sql-syntax.md#iceberg-writes-delete "iceberg-writes-sql-syntax.md#iceberg-writes-delete")
- [UPDATE](iceberg-writes-sql-syntax.md#iceberg-writes-update "iceberg-writes-sql-syntax.md#iceberg-writes-update")
- [MERGE](iceberg-writes-sql-syntax.md#iceberg-writes-merge "iceberg-writes-sql-syntax.md#iceberg-writes-merge")
- [DROP TABLE](iceberg-writes-sql-syntax.md#iceberg-writes-drop-table "iceberg-writes-sql-syntax.md#iceberg-writes-drop-table")

## CREATE TABLE

```
CREATE TABLE [IF NOT EXISTS] `<external_schema>`.`<table_name>` (
  column_name data_type [DEFAULT literal_value] [, ...]
)
USING ICEBERG
[LOCATION 's3://`your-bucket-name`/prefix/']
[PARTITIONED BY [[column_name | transform_function]], ...]
[TABLE PROPERTIES (['format-version'='`<version>`'] [, 'compression_type'='<compression_value>'])]
```

You can also use three-part notation for S3 table buckets:

```
CREATE TABLE "`<table_bucket_name>`@s3tablescatalog".`<database_name>`.`<table_name>` (
  column_name data_type [DEFAULT literal_value] [, ...]
)
USING ICEBERG
[PARTITIONED BY [[column_name | transform_function]], ...]
[TABLE PROPERTIES (['format-version'='`<version>`'] [, 'compression_type'='<compression_value>'])]
```

For the auto-mounted root catalog `awsdatacatalog`:

```
CREATE TABLE awsdatacatalog.`<database_name>`.`<table_name>` (
  column_name data_type [DEFAULT literal_value] [, ...]
)
USING ICEBERG
LOCATION 's3://`your-bucket-name`/prefix/'
[PARTITIONED BY [[column_name | transform_function]], ...]
[TABLE PROPERTIES (['format-version'='`<version>`'] [, 'compression_type'='<compression_value>'])]
```

When using the external schema syntax, note that
`<external_schema>` must be an
existing external schema name in which the external table will be created.
For more information about how to create and manage external schemas, see [CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md") in the Amazon Redshift documentation.

The `LOCATION` clause defines the table location for this newly
created Iceberg table. `LOCATION` is required for tables created
using external schemas or the `awsdatacatalog` root catalog. It
should be an empty location, meaning there are no existing Amazon S3 objects sharing
this same bucket and prefix. The Amazon S3 bucket Region must be in the same Region
as the Amazon Redshift cluster. For Amazon S3 table buckets, `LOCATION` cannot
be specified as the table location is determined by the Amazon S3 tables catalog
(`s3tablescatalog`).

However, AWS provides a method to replicate data from Iceberg tables stored
in an AWS Glue Data Catalog in one AWS Region to a different AWS Region, which allows
you to replicate the write to a different Region. For more information, see
[Replicate data across AWS Regions](../../../prescriptive-guidance/latest/apache-iceberg-on-aws/best-practices-workloads.md#workloads-replication "../../../prescriptive-guidance/latest/apache-iceberg-on-aws/best-practices-workloads.md#workloads-replication").

`PARTITIONED BY` defines the Iceberg table partition. Amazon Redshift supports
all Iceberg v2 partition transforms except for `void`. Here is the
list of transforms that are supported:

- **identity**
- **bucket[N]**
- **truncate[W]**
- **year**
- **month**
- **day**
- **hour**

For the full definitions of these transforms and the compatible data types,
see [Partition
Transforms](https://iceberg.apache.org/spec/#partition-transforms "https://iceberg.apache.org/spec/#partition-transforms") in the Apache Iceberg documentation.

The `PARTITIONED BY` supports multi-level partitioning. For
example, you can run the following command:

```
CREATE TABLE ...
USING ICEBERG
LOCATION ...
PARTITIONED BY (bucket(16, id), year(ship_date));
```

However, Amazon Redshift doesn't support using a single column in more than one
transform. For example, the following syntax is not supported:

```
CREATE TABLE ...
USING ICEBERG
LOCATION ...
PARTITIONED BY (bucket(16, ship_date), year(ship_date));
```

The `TABLE PROPERTIES` clause defines the extra table properties
for this Iceberg table. The supported table properties are
`format-version` and `compression_type`.
The `format-version` property specifies the Iceberg table
format version. Possible values are `'2'` (default) and
`'3'`. The `compression_type` property
defines the default Parquet data file compression. If not specified,
`snappy` is used as the compression codec. The
possible values for `compression_type` are:
`zstd`, `brotli`, `gzip`,
`snappy`, and `uncompressed`.

For Iceberg v3 tables, you can specify default values for columns
using the DEFAULT keyword. Default column values are supported only
for Iceberg v3 tables. Amazon Redshift returns an error if you specify a default
value on an Iceberg v2 table. Only literal values are supported as
defaults.

```
CREATE TABLE `<external_schema>`.`<table_name>` (
  column_name data_type [DEFAULT literal_value] [, ...]
)
USING ICEBERG
LOCATION 's3://`your-bucket-name`/`prefix`/'
[PARTITIONED BY [[column_name | transform_function]], ...]
[TABLE PROPERTIES ('format-version'='3' [, 'compression_type'='`<compression_value>`'])];
```

Examples with defaults:

```
-- External schema notation
CREATE TABLE my_external_schema.orders (
  order_id INT,
  status VARCHAR DEFAULT 'pending',
  region VARCHAR DEFAULT 'us-east-1'
)
USING ICEBERG
LOCATION 's3://amzn-s3-demo-bucket/orders/'
TABLE PROPERTIES ('format-version'='3');

-- Three-part notation (awsdatacatalog / Glue)
CREATE TABLE awsdatacatalog.my_glue_db.orders (
  order_id INT,
  status VARCHAR DEFAULT 'pending',
  region VARCHAR DEFAULT 'us-east-1'
)
USING ICEBERG
LOCATION 's3://amzn-s3-demo-bucket/orders/'
TABLE PROPERTIES ('format-version'='3');

-- Three-part notation (S3 Table Buckets)
CREATE TABLE "amzn-s3-demo-bucket@s3tablescatalog".my_namespace.orders (
  order_id INT,
  status VARCHAR DEFAULT 'pending',
  region VARCHAR DEFAULT 'us-east-1'
)
USING ICEBERG
TABLE PROPERTIES ('format-version'='3');
```

###### Note

`CREATE TABLE ... LIKE ...` is not supported for Iceberg
tables. Iceberg tables also don't support column constraints and column
attributes like RMS table does.

Alternatively, you can create and populate an Iceberg table in a single
operation using `CREATE TABLE AS SELECT`:

## CREATE TABLE AS SELECT

```
CREATE TABLE `<external_schema>`.`<table_name>` [(
  column_name[, ...]
)]
USING ICEBERG
[LOCATION 's3://`your-bucket-name`/prefix/']
[PARTITIONED BY [[column_name | transform_function]], ...]
[TABLE PROPERTIES ('compression_type'='`<compression-value>`')]
AS
SELECT query
```

You can also use three-part notation to create tables in auto-mounted catalogs:

```
CREATE TABLE "`<catalog_name>`".`<database_name>`.`<table_name>` [(
  column_name[, ...]
)]
USING ICEBERG
[LOCATION 's3://`your-bucket-name`/prefix/']
[PARTITIONED BY [[column_name | transform_function]], ...]
[TABLE PROPERTIES ('compression_type'='`<compression-value>`')]
AS
SELECT query
```

This is similar to the `CREATE TABLE` statement except that
`CREATE` is followed by a `SELECT` statement to
populate the table with `SELECT` query results.

You can no longer specify the data types with the `CREATE TABLE`
clause here, because the `SELECT` query determines the column data types.

If the `SELECT` query fails for any reason, this query will fail
and the Iceberg table will not be created.

For Iceberg v3 tables, specify
`'format-version'='3'` in the TABLE PROPERTIES clause.
Default column values are not inherited from the source
table.

```
-- External schema notation
CREATE TABLE my_external_schema.orders_backup (
  order_id, status, region
)
USING ICEBERG
LOCATION 's3://amzn-s3-demo-bucket/orders-backup/'
TABLE PROPERTIES ('format-version'='3')
AS
SELECT order_id, status, region
FROM my_external_schema.orders;

-- Three-part notation (awsdatacatalog / Glue)
CREATE TABLE awsdatacatalog.my_glue_db.orders_backup (
  order_id, status, region
)
USING ICEBERG
LOCATION 's3://amzn-s3-demo-bucket/orders-backup/'
TABLE PROPERTIES ('format-version'='3')
AS
SELECT order_id, status, region
FROM awsdatacatalog.my_glue_db.orders;

-- Three-part notation (S3 Table Buckets)
CREATE TABLE "amzn-s3-demo-bucket@s3tablescatalog".my_namespace.orders_backup (
  order_id, status, region
)
USING ICEBERG
TABLE PROPERTIES ('format-version'='3')
AS
SELECT order_id, status, region
FROM "amzn-s3-demo-bucket@s3tablescatalog".my_namespace.orders;
```

You can view the structure of your Iceberg tables using `SHOW
 TABLE`:

## SHOW TABLE

```
SHOW TABLE `<external_schema>`.`<table_name>`
```

You can also use three-part notation with auto-mounted catalogs:

```
SHOW TABLE "`<catalog_name>`".`<database_name>`.`<table_name>`
```

`SHOW TABLE` displays the `CREATE TABLE` statement for
Iceberg table. The command will show the appropriate results based on the type of
the table. The following is an example of the `SHOW TABLE` output for
Iceberg table:

```
CREATE TABLE my_schema.items (id int, price decimal(5, 2))
USING ICEBERG
LOCATION 's3://my_s3_bucket/items/'
PARTITIONED BY (bucket(16, id))
TABLE PROPERTIES ('compression_type'='snappy')
```

###### Note

For Amazon S3 tables, since the table location is managed by Amazon S3 tables catalog,
the `LOCATION` clause will be omitted in the `SHOW TABLE`
results.

For Iceberg v3 tables, `SHOW TABLE` displays default column
values in its output.

```
SHOW TABLE my_external_schema.orders;

-- Output includes the default values in the column definitions:
CREATE TABLE my_external_schema.orders (
  id int,
  status varchar DEFAULT 'active',
  priority int DEFAULT 0
)
USING ICEBERG
LOCATION 's3://amzn-s3-demo-bucket/orders/'
TABLE PROPERTIES ('format-version'='3');
```

After creating tables, you can add data using `INSERT INTO`:

## INSERT INTO

```
INSERT INTO `<external_schema>`.`<table_name>` [(column_name [, ...])] VALUES (...)
INSERT INTO `<external_schema>`.`<table_name>` [(column_name [, ...])] (SELECT query)

-- Using three-part notation for S3 table buckets:
INSERT INTO "`<table_bucket_name>`@s3tablescatalog".`<database_name>`.`<table_name>` [(column_name [, ...])] VALUES (...)
INSERT INTO "`<table_bucket_name>`@s3tablescatalog".`<database_name>`.`<table_name>` [(column_name [, ...])] (SELECT query)

-- Using three-part notation for the awsdatacatalog root catalog:
INSERT INTO awsdatacatalog.`<database_name>`.`<table_name>` [(column_name [, ...])] VALUES (...)
INSERT INTO awsdatacatalog.`<database_name>`.`<table_name>` [(column_name [, ...])] (SELECT query)
```

You can `INSERT INTO` existing Iceberg table using the above syntax. If
`VALUES` clause is used, you provide the values for columns listed by
`column_name`, or all columns if `column_name` part is
omitted.

When data is inserted into partitioned table, new rows are distributed according
to the predefined partition specification. If for any reason the `SELECT`
query fails, the query will fail and no data will be inserted into the Iceberg
table.

For Iceberg v3 tables with default column values, if a column with a
default is omitted from the INSERT statement or DEFAULT is specified as
the value, the default value is written to the data file.

## DELETE

The `DELETE` query for Iceberg table uses the existing
`DELETE` syntax in the RMS table:

```
[ WITH [RECURSIVE] `common_table_expression` [, `common_table_expression` , ...] ]
DELETE [ FROM ] `iceberg_table`
[ { USING } `table_name, ...` ] [ WHERE `condition` ]
```

You can also use three-part notation for S3 table buckets:

```
[ WITH [RECURSIVE] `common_table_expression` [, `common_table_expression` , ...] ]
DELETE [ FROM ] "`<table_bucket_name>`@s3tablescatalog".`<database_name>`.`<table_name>`
[ { USING } `table_name, ...` ] [ WHERE `condition` ]
```

For the auto-mounted root catalog `awsdatacatalog`:

```
[ WITH [RECURSIVE] `common_table_expression` [, `common_table_expression` , ...] ]
DELETE [ FROM ] awsdatacatalog.`<database_name>`.`<table_name>`
[ { USING } `table_name, ...` ] [ WHERE `condition` ]
```

The `iceberg_table` can be referenced using
the ``<external_schema>`.`<external_table_name>``
form, or use the 3-part notation for auto mounted catalog. See [Referencing Iceberg
tables in Amazon Redshift](referencing-iceberg-tables.md "referencing-iceberg-tables.md").

The `table_name` in the
`USING` clause will be used to join with the target table for
deleting rows that are satisfied with the `WHERE` condition. The
`table_name` can be an Iceberg table or a
Amazon Redshift RMS table.

Since Iceberg uses hidden partition scheme, user can use `DELETE` query
to remove partitions, achieving the same effect as `ALTER TABLE ... DROP
 PARTITION ...` for Hive tables.

For example, consider a partitioned Iceberg table like the following:

```
CREATE TABLE my_external_schema.lineitem
(l_item_id int,
 l_ship_date varchar,
 ...
)
USING ICEBERG
LOCATION ...
PARTITIONED BY l_ship_date;
```

Then you can remove a partition by using a query like the following:

```
DELETE FROM my_external_schema.lineitem WHERE l_ship_date = '20251231';
```

For query like this, Amazon Redshift will optimize the execution to only conduct metadata
only operation and short circuit the execution. Thus unlike normal
`DELETE` query, the metadata only delete query doesn't show execution
steps in `EXPLAIN`:

```
explain DELETE FROM my_external_schema.lineitem WHERE l_ship_date = '20251231';

 QUERY PLAN
------------
"XN Seq Scan Metadata of my_external_schema.lineitem location: "s3://s3-path//table-location" format:ICEBERG (cost=0.00..0.01 rows=0 width=0)"
(0 rows)
```

## UPDATE

The `UPDATE` query syntax for Iceberg table is very similar to the
existing `UPDATE` syntax for the RMS table:

```
[ WITH [RECURSIVE] `common_table_expression` [, `common_table_expression` , ...] ]
UPDATE `iceberg_table` [ [ AS ] alias ] SET column = { `expression` } [,...]
[ FROM `fromlist` ]
[ WHERE `condition` ]
```

You can also use three-part notation for S3 table buckets:

```
[ WITH [RECURSIVE] `common_table_expression` [, `common_table_expression` , ...] ]
UPDATE "`<table_bucket_name>`@s3tablescatalog".`<database_name>`.`<table_name>` [ [ AS ] alias ] SET column = { `expression` } [,...]
[ FROM `fromlist` ]
[ WHERE `condition` ]
```

For the auto-mounted root catalog `awsdatacatalog`:

```
[ WITH [RECURSIVE] `common_table_expression` [, `common_table_expression` , ...] ]
UPDATE awsdatacatalog.`<database_name>`.`<table_name>` [ [ AS ] alias ] SET column = { `expression` } [,...]
[ FROM `fromlist` ]
[ WHERE `condition` ]
```

The `iceberg_table` can be referenced using
the ``<external_schema>`.`<external_table_name>``
form, or use the 3-part notation for auto mounted catalog. See [Referencing Iceberg
tables in Amazon Redshift](referencing-iceberg-tables.md "referencing-iceberg-tables.md").

You can update a table by referencing information in other tables. List these
other tables in the FROM clause or use a subquery as part of the WHERE condition.
The source tables can be either Iceberg tables or Amazon Redshift RMS tables.

`UPDATE` can also run on partitioned table. When
`UPDATE` changes column values that belongs to current partition
spec, the new updated row would be inserted into the new partition based on the
newly updated value.

For example, consider a partitioned Iceberg table like the following:

```
CREATE TABLE my_external_schema.lineitem
(l_item_id int,
 l_ship_date varchar,
 ...
)
USING ICEBERG
LOCATION ...
PARTITIONED BY l_ship_date;

INSERT INTO my_external_schema.lineitem VALUES (10099, '20251231', ...);
```

And when you run the following update query:

```
UPDATE my_external_schema.lineitem SET l_ship_date = '20260101'
WHERE l_item_id = 10099;
```

the row with `l_item_id` 10099 moves from partition
`20251231` to the new partition `20260101`.

It's also important to note that it's possible `UPDATE` has multiple
candidate values. Consider below query:

```
CREATE TABLE my_ext_schema.t1(x1 int, y1 int) USING ICEBERG LOCATION ...;
CREATE TABLE my_ext_schema.t2(x2 int, y2 int) USING ICEBERG LOCATION ...;
INSERT INTO my_ext_schema.t1 VALUES (1,10), (2,20), (3,30);
INSERT INTO my_ext_schema.t2 VALUES (2,40), (2,50);
UPDATE my_ext_schema.t1 SET y1=y2 FROM my_ext_schema.t2 WHERE x1=x2;
```

In this case, y1 can be 40 or 50. The result is nondeterministic. You can set the
configuration parameter
`error_on_nondeterministic_update` to true to force query error when
such case happens. This is consistent with the existing RMS table
`UPDATE` behavior. For more, refer to [error\_on\_nondeterministic\_update](r_error_on_nondeterministic_update.md "r_error_on_nondeterministic_update.md").

## MERGE

The `MERGE` query conditionally merges rows from a source table into a
target table. It shares the same `MERGE` query syntax as the existing RMS
table:

```
MERGE INTO `target_iceberg_table` USING `source_table` [ [ AS ] `alias` ]
ON `match_condition`
[ WHEN MATCHED THEN { UPDATE SET `col_name` = { `expr` } [,...] | DELETE }
  WHEN NOT MATCHED THEN INSERT [ ( `col_name` [,...] ) ]
  VALUES ( { `expr` } [, ...] )
| REMOVE DUPLICATES ]
```

You can also use three-part notation for S3 table buckets:

```
MERGE INTO "`<table_bucket_name>`@s3tablescatalog".`<database_name>`.`<table_name>` USING `source_table` [ [ AS ] `alias` ]
ON `match_condition`
[ WHEN MATCHED THEN { UPDATE SET `col_name` = { `expr` } [,...] | DELETE }
  WHEN NOT MATCHED THEN INSERT [ ( `col_name` [,...] ) ]
  VALUES ( { `expr` } [, ...] )
| REMOVE DUPLICATES ]
```

For the auto-mounted root catalog `awsdatacatalog`:

```
MERGE INTO awsdatacatalog.`<database_name>`.`<table_name>` USING `source_table` [ [ AS ] `alias` ]
ON `match_condition`
[ WHEN MATCHED THEN { UPDATE SET `col_name` = { `expr` } [,...] | DELETE }
  WHEN NOT MATCHED THEN INSERT [ ( `col_name` [,...] ) ]
  VALUES ( { `expr` } [, ...] )
| REMOVE DUPLICATES ]
```

The
`target_iceberg_table` can be referenced
using the ``<external_schema>`.`<external_table_name>``
form, or use the 3-part notation for auto mounted catalog. See [Referencing Iceberg
tables in Amazon Redshift](referencing-iceberg-tables.md "referencing-iceberg-tables.md").

The `source_table` can be either an Iceberg
table or a Amazon Redshift RMS table.

When `REMOVE DUPLICATES` is used, the `MERGE` command uses
simplified mode. For more details about simplified mode, please refer to the
original `MERGE`
[command
document](r_MERGE.md "r_MERGE.md").

While executing `MERGE` query, Amazon Redshift generates and stores intermediate
data files in the target table location. These files will be garbage collected at the
end of the query. Because of this, `MERGE` query would require
`DELETE` permission on Amazon S3 bucket in order to work properly. An
insufficient permission error would throw if the garbage collection operation is
failed. For Amazon S3 tables the garbage collection is managed by Amazon S3 tables service.
Hence `DELETE` permission is not required to execute `MERGE`
query.

## DROP TABLE

To remove an Iceberg table from the catalog, use the `DROP TABLE`
command:

```
DROP TABLE `<external_schema>`.`<table_name>`
```

You can also use three-part notation with auto-mounted catalogs:

```
DROP TABLE "`<catalog_name>`".`<database_name>`.`<table_name>`
```

Dropping an Iceberg table is a metadata only operation. It removes the table entry
from AWS Glue Data Catalog and Amazon S3 table catalog, if this is an Amazon S3 table. Amazon Redshift doesn't
clean up or delete any existing data file or metadata files under the table
location. You can use features in AWS Glue and Amazon S3 tables to remove orphaned
files. For AWS Glue, see [Deleting orphan files](../../../glue/latest/dg/orphan-file-deletion.md "../../../glue/latest/dg/orphan-file-deletion.md").
For Amazon S3 tables, see [Table
maintenance](../../../AmazonS3/latest/userguide/s3-tables-maintenance.md "../../../AmazonS3/latest/userguide/s3-tables-maintenance.md").
