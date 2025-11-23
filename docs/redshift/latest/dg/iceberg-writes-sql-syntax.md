Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

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

All other SQL statements, such as `DELETE`, `UPDATE`,
`MERGE`, and `ALTER TABLE`, are not yet supported on Iceberg
tables.

The following sections demonstrate SQL syntax for creating, inserting, and managing
Iceberg tables in Amazon Redshift.

###### Contents

- [CREATE TABLE](iceberg-writes-sql-syntax.md#iceberg-writes-create-table "iceberg-writes-sql-syntax.md#iceberg-writes-create-table")
- [CREATE TABLE AS SELECT](iceberg-writes-sql-syntax.md#iceberg-writes-create-table-as-select "iceberg-writes-sql-syntax.md#iceberg-writes-create-table-as-select")
- [SHOW TABLE](iceberg-writes-sql-syntax.md#iceberg-writes-show-table "iceberg-writes-sql-syntax.md#iceberg-writes-show-table")
- [INSERT INTO](iceberg-writes-sql-syntax.md#iceberg-writes-insert-into "iceberg-writes-sql-syntax.md#iceberg-writes-insert-into")
- [DROP TABLE](iceberg-writes-sql-syntax.md#iceberg-writes-drop-table "iceberg-writes-sql-syntax.md#iceberg-writes-drop-table")

## CREATE TABLE

```
CREATE TABLE [IF NOT EXISTS] `<external_schema>`.`<table_name>` (
  column_name data_type [, ...]
)
USING ICEBERG
[LOCATION 's3://`your-bucket-name`/prefix/']
[PARTITIONED BY [[column_name | transform_function]], ...]
[TABLE PROPERTIES ('compression_type'='<compression_value>')]
```

You can also use three-part notation for S3 table buckets:

```
CREATE TABLE "`<table_bucket_name>`@s3tablescatalog".`<database_name>`.`<table_name>` (
  column_name data_type [, ...]
)
USING ICEBERG
[PARTITIONED BY [[column_name | transform_function]], ...]
[TABLE PROPERTIES ('compression_type'='<compression_value>')]
```

Note that `<external_schema>` must
be an existing external schema name in which the external table will be created.
For more information about how to create and manage external schemas, see [CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md") in the Amazon Redshift documentation.

The `LOCATION` clause defines the table location for this newly
created Iceberg table. For Amazon S3 tables, `LOCATION` cannot be
specified as the table location is determined by Amazon S3 tables catalog
(`s3tablescatalog`).

In all other cases, `LOCATION` is required, and it should be an
empty location, meaning there are no existing Amazon S3 objects sharing this same
bucket and prefix. Note that the Amazon S3 bucket region must be in the same region
as Amazon Redshift cluster.

However, AWS provides a method to replicate data from Iceberg tables stored
in an AWS Glue Data Catalog in one AWS Region to a different AWS Region, which allows
you to replicate the write to a different region. For more information, see
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
for this Iceberg table. The only table property we support is
`compression_type` which defines the default Parquet data file
compression. If this is not specified, `snappy` is used as the
compression codec. The possible values for `compression_type` are:
`zstd`, `brotli`, `gzip`,
`snappy`, and `uncompressed`.

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

The `CREATE TABLE` clause here no longer allows you to specify the
data types as the column data types will be decided by the `SELECT`
query.

If the `SELECT` query fails for any reason, this query will fail
and the Iceberg table will not be created.

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

After creating tables, you can add data using `INSERT INTO`:

## INSERT INTO

```
INSERT INTO `<external_schema>`.`<table_name>` [(column_name [, ...])] VALUES (...)
INSERT INTO `<external_schema>`.`<table_name>` [(column_name [, ...])] (SELECT query)

-- Using three-part notation for S3 table buckets:
INSERT INTO "`<table_bucket_name>`@s3tablescatalog".`<database_name>`.`<table_name>` [(column_name [, ...])] VALUES (...)
INSERT INTO "`<table_bucket_name>`@s3tablescatalog".`<database_name>`.`<table_name>` [(column_name [, ...])] (SELECT query)
```

You can `INSERT INTO` existing Iceberg table using the above syntax. If
`VALUES` clause is used, you provide the values for columns listed by
`column_name`, or all columns if `column_name` part is
omitted.

When data is inserted into partitioned table, new rows are distributed according
to the predefined partition specification. If for any reason the `SELECT`
query fails, the query will fail and no data will be inserted into the Iceberg
table.

It's possible for you to `INSERT INTO` an Iceberg table that is not
created by Amazon Redshift. However, there are some limitations:

- The table must be an Iceberg v2 table.
- The table must be using Parquet as default data format.
- The table must not have metadata compression set to True.
- The table must not enable Write-Audit-Publish (WAP).

To remove an Iceberg table from the catalog, use the `DROP TABLE`
command:

## DROP TABLE

```
DROP TABLE `<external_schema>`.`<table_name>`
```

You can also use three-part notation with auto-mounted catalogs:

```
DROP TABLE "`<catalog_name>`.`<database_name>`.`<table_name>`
```

Dropping an Iceberg table is a metadata only operation. It removes the table entry
from AWS Glue Data Catalog and Amazon S3 table catalog, if this is an Amazon S3 table. Amazon Redshift doesn't
clean up or delete any existing data file or metadata files under the table
location. You can use features in AWS Glue and Amazon S3 tables to remove orphaned
files. For AWS Glue, see [Deleting orphan files](../../../glue/latest/dg/orphan-file-deletion.md "../../../glue/latest/dg/orphan-file-deletion.md").
For Amazon S3 tables, see [Table
maintenance](../../../AmazonS3/latest/userguide/s3-tables-maintenance.md "../../../AmazonS3/latest/userguide/s3-tables-maintenance.md").
