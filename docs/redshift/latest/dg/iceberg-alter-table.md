

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Altering table definitions
<a name="iceberg-alter-table"></a>

`ALTER TABLE` statements are used to change table definitions, including schema, partition specs, and properties. You can use these DDL statements to manage your Iceberg tables directly through Amazon Redshift.

All `ALTER TABLE` statements support using external schema references or three-part notation references for Iceberg tables. In the syntax examples below, `{{iceberg_table}}` can be any of the following:

```
-- External schema notation:
{{<external_schema>}}.{{<table_name>}}

-- Three-part notation for S3 table buckets:
"{{<table_bucket_name>}}@s3tablescatalog".{{<database_name>}}.{{<table_name>}}

-- Three-part notation for the awsdatacatalog root catalog:
awsdatacatalog.{{<database_name>}}.{{<table_name>}}
```

For more information, see [Referencing Iceberg tables in Amazon Redshift](referencing-iceberg-tables.md).

Consider the following when using `ALTER TABLE` statements:
+ `ALTER TABLE` statements currently only support Iceberg v2 or v3 tables.
+ All `ALTER TABLE` statements are metadata-only operations.
+ `ALTER TABLE` statements don't support tables with complex type columns.

**Contents**
+ [Upgrading to Iceberg v3](#iceberg-alter-table-upgrade-v3)
+ [ALTER TABLE RENAME COLUMN](#iceberg-alter-table-rename-column)
+ [ALTER TABLE ADD/DROP COLUMN](#iceberg-alter-table-add-drop-column)
+ [ALTER TABLE ALTER COLUMN](#iceberg-alter-table-alter-column)
+ [ALTER TABLE SET TABLE PROPERTIES](#iceberg-alter-table-set-properties)
+ [ALTER TABLE ADD, DROP, and REPLACE PARTITION FIELD](#iceberg-alter-table-partition-field)

## Upgrading to Iceberg v3
<a name="iceberg-alter-table-upgrade-v3"></a>

You can upgrade an Iceberg v2 table to v3 using `ALTER TABLE SET TABLE PROPERTIES`:

```
ALTER TABLE {{iceberg_table}}
SET TABLE PROPERTIES ('format-version' = '3');
```

For additional details, see [Upgrading from v2 to v3](iceberg-v3-features.md#iceberg-v3-upgrading).

## ALTER TABLE RENAME COLUMN
<a name="iceberg-alter-table-rename-column"></a>

```
ALTER TABLE {{iceberg_table}}
RENAME [COLUMN] {{col_name}} TO {{new_name}};
```

`ALTER TABLE RENAME COLUMN` renames an existing column. The `{{col_name}}` can be a partition column or a non-partitioned column. After the rename, the column data type and partition spec don't change.

**Note**  
`ALTER TABLE RENAME COLUMN` is not supported for AWS Lake Formation registered tables.

## ALTER TABLE ADD/DROP COLUMN
<a name="iceberg-alter-table-add-drop-column"></a>

```
ALTER TABLE {{iceberg_table}}
ADD [COLUMN] {{col_name}} {{col_type}};
```

```
ALTER TABLE {{iceberg_table}}
DROP [COLUMN] {{col_name}};
```

`ADD COLUMN` adds one column to an existing Iceberg table. You can use any data type that is supported by Amazon Redshift Iceberg writes. For more information, see [Supported data types with Apache Iceberg tables](querying-iceberg-supported-data-types.md).

`ADD COLUMN` is a metadata-only operation. The values of newly added columns on existing rows are `NULL`.

`DROP COLUMN` drops a column from an existing Iceberg table. For partitioned tables, you can't drop a column that belongs to the current partition spec. You must remove the partition field that involves the column first before dropping the column. For more information, see [ALTER TABLE ADD, DROP, and REPLACE PARTITION FIELD](#iceberg-alter-table-partition-field).

For Iceberg v3 tables, you can specify a default value when adding a column. Existing data files return the specified default instead of NULL for the newly added column without requiring a data rewrite. Default column values are supported only for Iceberg v3 tables. Amazon Redshift returns an error if you specify a default value on an Iceberg v2 table.

```
-- External schema notation
ALTER TABLE my_external_schema.orders
ADD COLUMN priority INT DEFAULT 0;

-- Three-part notation (awsdatacatalog / Glue)
ALTER TABLE awsdatacatalog.my_glue_db.orders
ADD COLUMN priority INT DEFAULT 0;

-- Three-part notation (S3 Table Buckets)
ALTER TABLE "amzn-s3-demo-bucket@s3tablescatalog".my_namespace.orders
ADD COLUMN priority INT DEFAULT 0;
```

For existing rows, the default value is filled in for the newly added column:

```
-- Existing table with rows
SELECT id FROM my_external_schema.orders;
--  1
--  2

-- Add a column with a default
ALTER TABLE my_external_schema.orders
ADD COLUMN status varchar DEFAULT 'active';

-- Existing rows return the default without a data rewrite
SELECT id, status FROM my_external_schema.orders;
--  1 | active
--  2 | active
```

## ALTER TABLE ALTER COLUMN
<a name="iceberg-alter-table-alter-column"></a>

```
ALTER TABLE {{iceberg_table}}
    ALTER COLUMN {{column_name}} TYPE {{updated_data_type}};
```

`ALTER TABLE ALTER COLUMN` changes the data type of an existing column. Only type widening is allowed, not narrowing. Because data isn't rewritten after the `ALTER`, narrowing data types could cause overflow when consuming the existing table data. The following type widenings are allowed per the Iceberg spec:

```
int → bigint
float → double
decimal(P, S) → decimal(P2, S) where P2 > P (scale cannot be changed)
```

In Amazon Redshift, data types can have aliases. For example, 4-byte integers use the type name `int` or `int4`. As long as they are mapped to 4-byte int in Iceberg types, type widening to 8-byte integers is allowed.

For example, an Iceberg table is created using 4-byte integer types:

```
CREATE TABLE {{iceberg_table}} (cint int) USING ICEBERG LOCATION 's3://{{your-bucket-name}}/prefix/';
```

It can be widened by this `ALTER` statement:

```
ALTER TABLE {{iceberg_table}} ALTER COLUMN cint TYPE int8;
```

For the full list of data type mappings between Amazon Redshift types and Iceberg types, see [Supported data types with Apache Iceberg tables](querying-iceberg-supported-data-types.md).

Widening the type of a column that belongs to the existing partition spec is not supported.

For Iceberg v3 tables, you can set or remove a default value on an existing column:

```
ALTER TABLE {{iceberg_table}}
ALTER COLUMN {{column_name}} SET DEFAULT {{literal_value}};

ALTER TABLE {{iceberg_table}}
ALTER COLUMN {{column_name}} DROP DEFAULT;
```

SET DEFAULT changes the default value of an existing column. The new default applies to data files written after the change. Existing data files continue to use the previous default.

DROP DEFAULT removes the default value that is applied to new writes, equivalent to setting the default to NULL. Data files that do not contain the column continue to return the column's initial default value.

```
-- External schema notation
ALTER TABLE my_external_schema.orders
ALTER COLUMN status SET DEFAULT 'active';
ALTER TABLE my_external_schema.orders
ALTER COLUMN status DROP DEFAULT;

-- Three-part notation (awsdatacatalog / Glue)
ALTER TABLE awsdatacatalog.my_glue_db.orders
ALTER COLUMN status SET DEFAULT 'active';
ALTER TABLE awsdatacatalog.my_glue_db.orders
ALTER COLUMN status DROP DEFAULT;

-- Three-part notation (S3 Table Buckets)
ALTER TABLE "amzn-s3-demo-bucket@s3tablescatalog".my_namespace.orders
ALTER COLUMN status SET DEFAULT 'active';
ALTER TABLE "amzn-s3-demo-bucket@s3tablescatalog".my_namespace.orders
ALTER COLUMN status DROP DEFAULT;
```

## ALTER TABLE SET TABLE PROPERTIES
<a name="iceberg-alter-table-set-properties"></a>

```
ALTER TABLE {{iceberg_table}}
SET TABLE PROPERTIES (
 'compression_type' = '{{compression_value}}');
```

This statement allows you to overwrite the default table property. Currently the only table property allowed for this statement is `compression_type`. You can overwrite it to use a different compression type for the Iceberg table Parquet files. Data inserted after the `ALTER` uses the new compression type.

The possible values for `compression_type` are: `brotli`, `gzip`, `snappy`, `uncompressed`, and `zstd`.

You can also upgrade an existing Iceberg v2 table to v3 by setting the format version:

```
ALTER TABLE {{iceberg_table}}
SET TABLE PROPERTIES ('format-version' = '3');
```

For additional details, see [Upgrading from v2 to v3](iceberg-v3-features.md#iceberg-v3-upgrading).

## ALTER TABLE ADD, DROP, and REPLACE PARTITION FIELD
<a name="iceberg-alter-table-partition-field"></a>

```
ALTER TABLE {{iceberg_table}}
    ADD PARTITION FIELD {{column_name}} | {{transform_function}};
```

```
ALTER TABLE {{iceberg_table}}
    DROP PARTITION FIELD {{column_name}} | {{transform_function}};
```

```
ALTER TABLE {{iceberg_table}}
    REPLACE PARTITION FIELD {{column_name}} | {{transform_function}}
        WITH {{column_name}} | {{transform_function}};
```

The `[ADD | DROP | REPLACE] PARTITION FIELD` statements allow you to change the existing table partition spec, supporting partition evolution through Amazon Redshift.

The `ALTER` statements for partition spec only change table metadata and don't re-partition the existing table data. After the `ALTER`, new data inserted into the table follows the newly defined partition spec.

Consider the following limitations for these statements:
+ When defining a new partition field through `ADD` or `REPLACE ... WITH ...`, the new field can't include a column that's already part of other partition fields. This is the same limitation as when you define the initial partition spec at `CREATE TABLE`. For more information, see [CREATE TABLE](iceberg-writes-sql-syntax.md#iceberg-writes-create-table).

  For example, when you have a table:

  ```
  CREATE TABLE {{iceberg_table}} ... PARTITIONED BY year(ship_date) USING ICEBERG ...;
  ```

  The following fails because `ship_date` is already part of an existing partition field:

  ```
  ALTER TABLE {{iceberg_table}} ADD PARTITION FIELD bucket(128, ship_date);
  ```
+ When adding a new partition field, the newly added field is always treated as the last level of partition of the table. For example:

  ```
  CREATE TABLE {{iceberg_table}} ... PARTITIONED BY year(ship_date) USING ICEBERG ...;
  ALTER TABLE {{iceberg_table}} ADD PARTITION FIELD bucket(256, item_id);
  ```

  The table partition spec is the same as:

  ```
  CREATE TABLE {{iceberg_table}} ... PARTITIONED BY (year(ship_date), bucket(256, item_id))
      USING ICEBERG ...;
  ```
+ When dropping a partition field, it's not limited to the last level of partition. You can drop any existing partition field. For example:

  ```
  CREATE TABLE {{iceberg_table}} ... PARTITIONED BY (year(ship_date), bucket(256, item_id))
      USING ICEBERG ...;
  ALTER TABLE {{iceberg_table}} DROP PARTITION FIELD year(ship_date);
  ```

  After this `ALTER`, the table is only partitioned by `bucket(256, item_id)`.
+ When calling `REPLACE PARTITION FIELD ... WITH ...`, the partition field to be replaced can be any field in the spec and is not limited to the last field. For example:

  ```
  CREATE TABLE {{iceberg_table}} ... PARTITIONED BY (year(ship_date), bucket(256, item_id))
      USING ICEBERG ...;
  ALTER TABLE {{iceberg_table}} REPLACE PARTITION FIELD year(ship_date) WITH month(ship_date);
  ```

  After this `ALTER`, the table partition becomes `(month(ship_date), bucket(256, item_id))`.
+ The `void` transform is not supported in partition `ALTER` statements.