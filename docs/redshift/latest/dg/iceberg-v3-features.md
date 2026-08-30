Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Apache Iceberg v3 features in Amazon Redshift

Amazon Redshift supports Apache Iceberg v3 tables. Iceberg v3 introduces
default column values, row lineage tracking, and deletion vectors.
You can create new v3 tables or upgrade existing v2 tables to
v3.

Iceberg v3 tables use the same SQL syntax for queries and DML
operations (INSERT, DELETE, UPDATE, MERGE) as v2 tables. The
features described on this page are specific to Iceberg v3.

## Creating an Iceberg v3 table

To create an Iceberg v3 table, specify
`'format-version'='3'` in the TABLE PROPERTIES
clause:

```
CREATE TABLE `external_schema`.`table_name` (
  column_name data_type [DEFAULT literal_value] [, ...]
)
USING ICEBERG
LOCATION 's3://`your-bucket-name`/`prefix`/'
[PARTITIONED BY [[column_name | transform_function]], ...]
TABLE PROPERTIES ('format-version'='3'
    [, 'compression_type'='`compression_value`']);
```

Example:

```
CREATE TABLE my_schema.orders (
  id int,
  status varchar DEFAULT 'pending',
  priority int DEFAULT 0
)
USING ICEBERG
LOCATION 's3://amzn-s3-demo-bucket/orders/'
TABLE PROPERTIES ('format-version'='3');
```

If you do not specify format-version, Amazon Redshift creates the
table as Iceberg v2.

## Upgrading from v2 to v3

You can upgrade an existing Iceberg v2 table to v3:

```
ALTER TABLE `iceberg_table`
SET TABLE PROPERTIES ('format-version' = '3');
```

Upgrading the format version is a metadata-only operation.
Existing data files are not rewritten. Existing v2 positional
delete files remain valid and are applied during reads. The
first write operation after an upgrade generates row lineage
values for the entire table. On subsequent DELETE, UPDATE, or
MERGE operations, Amazon Redshift merges v2 positional deletes into
deletion vectors for the data files affected by the
operation.

### Limitations

- Downgrading from v3 to v2 is not
  supported.
- Amazon Redshift does not support reading or writing
  complex types (struct, list, map, variant) in
  Iceberg v3 tables.
- Amazon Redshift does not support the following data types
  in Iceberg v3 tables: struct, list, map, variant,
  geometry, geography, binary, uuid, time,
  timestamp\_ns, timestamptz\_ns, and
  unknown.
- After upgrading a table to v3, the Iceberg
  `timestamptz` type is mapped to the
  Amazon Redshift TIMESTAMPTZ type. In v2 tables,
  `timestamptz` is mapped to the Amazon Redshift
  TIMESTAMP type. With v3, this means your queries
  output the timestamp based on their
  timezone.

## Default column values

Default column values are supported only for Iceberg v3
tables. Amazon Redshift returns an error if you specify a default value
on an Iceberg v2 table.

Default values specify a literal value that a column falls
back to when no explicit value is present. This lets you add
new columns to an existing table without rewriting data
files. Reads of previously written data files automatically
return the default value for the new column. The default is
also written when a DML statement
omits the column or specifies DEFAULT as the value.

Only literal values are supported as defaults. Nested data
types do not support default values.

CREATE TABLE AS SELECT does not inherit default column
values from the source table. To define defaults on the new
table, use ALTER TABLE ALTER COLUMN SET DEFAULT after
creation.

### Defining defaults at table creation

```
CREATE TABLE `external_schema`.`table_name` (
  column_name data_type DEFAULT literal_value [, ...]
)
USING ICEBERG
LOCATION '...'
TABLE PROPERTIES ('format-version'='3');
```

### Adding a column with a default

```
ALTER TABLE `iceberg_table`
ADD COLUMN column_name data_type DEFAULT literal_value;
```

Existing data files return the default value for the
newly added column without requiring a data
rewrite.

### Changing or removing a default

```
ALTER TABLE `iceberg_table`
ALTER COLUMN column_name SET DEFAULT literal_value;

ALTER TABLE `iceberg_table`
ALTER COLUMN column_name DROP DEFAULT;
```

SET DEFAULT changes the default value of an existing
column. The new default applies to data files written
after the change. Existing data files continue to use the
previous default.

DROP DEFAULT removes the default value from a column.
After this operation, new writes no longer apply a
default for the column. Data files that do not contain
the column continue to return the column's initial
default value.

### INSERT behavior

When inserting rows without specifying a column that
has a default value, the default value is written to the
data file.

### SHOW TABLE

SHOW TABLE displays default values in its
output.

## Row lineage

Row lineage is supported only for Iceberg v3 tables. It
provides two pseudo-columns that track row identity and
modification history. These columns are automatically managed
by Amazon Redshift. You do not set their values.

### Pseudo-columns

| Column                          | Data type | Description                                                                                  |
| ------------------------------- | --------- | -------------------------------------------------------------------------------------------- |
| `_row_id`                       | BIGINT    | Uniquely identifies each row in the<br>table. Assigned automatically on write<br>operations. |
| `_last_updated_sequence_number` | BIGINT    | The snapshot sequence number of the<br>last write operation that modified the<br>row.        |

### Querying row lineage

Row lineage columns must be explicitly named in the
SELECT list. They are not included in SELECT \*.

```
SELECT _row_id, _last_updated_sequence_number, *
FROM my_schema.my_iceberg_v3_table;
```

You can use row lineage columns in WHERE, ORDER BY,
GROUP BY, and JOIN clauses:

```
SELECT *
FROM my_schema.my_iceberg_v3_table
WHERE _last_updated_sequence_number >= 3
ORDER BY _row_id;
```

### Behavior on non-v3 tables

When querying a non-Iceberg v3 table,
`_row_id` and
`_last_updated_sequence_number` return
NULL.

### Behavior after v2-to-v3 upgrade

For tables upgraded from Iceberg v2 to v3, row lineage
values are not immediately available for pre-upgrade
data. Both `_row_id` and
`_last_updated_sequence_number` return NULL
until the first write operation after the upgrade, which
generates row lineage values for the entire table. This
is a metadata-only operation and does not rewrite
existing data files.

### Write behavior

Row lineage is automatically populated by Amazon Redshift on all
write operations (INSERT, CTAS, UPDATE, MERGE). Each row
receives a unique `_row_id`, and
`_last_updated_sequence_number` reflects the
snapshot sequence number of the commit that wrote the
row.

### Limitations

- Row lineage columns are not included in
  SELECT \*.
- Row lineage is not supported for Iceberg v2 or
  earlier tables.
- Pre-upgrade data in v2-to-v3 upgraded tables
  returns NULL for both pseudo-columns until the
  first write operation after the upgrade.

## Deletion vectors

Deletion vectors are the mechanism Iceberg v3 uses to
track row-level deletes. They replace the positional delete
files used by Iceberg v2.

When you run DELETE, UPDATE, or MERGE on an Iceberg v3
table, Amazon Redshift records deleted row positions in deletion vectors
rather than writing separate positional delete files. This is
handled automatically. No changes to SQL syntax are
required.

### How deletion vectors work

A deletion vector is a compressed bitmap that records
which row positions in a data file have been deleted.
Deletion vectors are stored in Puffin files in the same
S3 location as the table data. Each data file has at
most one deletion vector.

When reading an Iceberg v3 table, Amazon Redshift automatically
applies deletion vectors to exclude deleted rows from
query results.

### Benefits over positional delete files

- Deletion vectors are more compact than
  positional delete files.
- A single deletion vector per data file avoids
  the accumulation of many small delete
  files.
- Subsequent deletes on the same data file
  produce a new deletion vector that merges the
  previous deletions with the newly deleted
  positions, maintaining a single deletion vector
  per data file.
- Because deletion vectors are more compact and
  avoid accumulating many small files, reads and
  writes are faster compared to Iceberg v2
  positional delete files.

### Behavior after v2-to-v3 upgrade

After upgrading a table from Iceberg v2 to v3,
existing v2 positional delete files remain valid and are
applied during reads. On subsequent write operations
(DELETE, UPDATE, or MERGE), Amazon Redshift merges existing v2
positional deletes into deletion vectors, as defined by
the Iceberg specification.

### Limitations

- Deletion vectors are not supported for Iceberg
  v2 or earlier tables.
- Iceberg v3 tables cannot fall back to
  positional delete files for new write operations.
  This means Iceberg v3 tables can read existing
  positional delete files, but no new positional
  delete files can be added. Instead, Iceberg v3
  tables can only add new deletes using deletion
  vectors.
