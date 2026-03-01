# Query Iceberg table data

To query an Iceberg dataset, use a standard `SELECT` statement like the
following. Queries follow the Apache Iceberg [format v2 spec](https://iceberg.apache.org/spec/#format-versioning "https://iceberg.apache.org/spec/#format-versioning") and
perform merge-on-read of both position and equality deletes.

```
SELECT * FROM [`db_name`.]`table_name` [WHERE `predicate`]
```

To optimize query times, all predicates are pushed down to where the data
lives.

For information about time travel and version travel queries, see [Perform time travel and version travel queries](querying-iceberg-time-travel-and-version-travel-queries.md "querying-iceberg-time-travel-and-version-travel-queries.md").

## Create and query views with Iceberg tables

To create and query Athena views on Iceberg tables, use `CREATE VIEW`
views as described in [Work with views](views.md "views.md").

Example:

```
CREATE VIEW view1 AS SELECT * FROM `iceberg_table`
```

```
SELECT * FROM view1
```

If you are interested in using the [Iceberg
view specification](https://github.com/apache/iceberg/blob/master/format/view-spec.md "https://github.com/apache/iceberg/blob/master/format/view-spec.md") to create views, contact [athena-feedback@amazon.com](mailto:athena-feedback@amazon.com "mailto:athena-feedback@amazon.com").

## Query Iceberg table metadata

In a `SELECT` query, you can use the following properties after
`table_name`to query Iceberg table metadata:

- $files – Shows a table's current data
  files.
- $manifests – Shows a table's current file
  manifests.
- $history – Shows a table's history.
- $partitions – Shows a table's current
  partitions.
- $snapshots – Shows a table's
  snapshots.
- $refs – Shows a table's references.

### Examples

The following statement lists the files for an Iceberg table.

```
SELECT * FROM "`dbname`"."`tablename`$files"
```

The following statement lists the manifests for an Iceberg table.

```
SELECT * FROM "`dbname`"."`tablename`$manifests"
```

The following statement shows the history for an Iceberg table.

```
SELECT * FROM "`dbname`"."`tablename`$history"
```

The following example shows the partitions for an Iceberg table.

```
SELECT * FROM "`dbname`"."`tablename`$partitions"
```

The following example lists the snapshots for an Iceberg table.

```
SELECT * FROM "`dbname`"."`tablename`$snapshots"
```

The following example shows the references for an Iceberg table.

```
SELECT * FROM "`dbname`"."`tablename`$refs"
```

## Use Lake Formation fine-grained access control

Athena engine version 3 supports Lake Formation fine-grained access control with Iceberg tables, including
column level and row level security access control. This access control works with
time travel queries and with tables that have performed schema evolution. For more
information, see [Lake Formation fine-grained access control and Athena workgroups](lf-athena-limitations.md#lf-athena-limitations-fine-grained-access-control "lf-athena-limitations.md#lf-athena-limitations-fine-grained-access-control").

If you created your Iceberg table outside of Athena, use [Apache Iceberg SDK](https://iceberg.apache.org/releases/ "https://iceberg.apache.org/releases/") version
0.13.0 or higher so that your Iceberg table column information is populated in the
AWS Glue Data Catalog. If your Iceberg table does not contain column information in AWS Glue, you
can use the Athena [ALTER TABLE SET TBLPROPERTIES](querying-iceberg-alter-table-set-properties.md "querying-iceberg-alter-table-set-properties.md") statement or the
latest Iceberg SDK to fix the table and update the column information in AWS Glue.
