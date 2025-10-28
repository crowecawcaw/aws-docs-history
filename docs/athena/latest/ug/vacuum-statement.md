# VACUUM

The `VACUUM` statement performs table maintenance on Apache Iceberg tables by
performing [snapshot
expiration](https://iceberg.apache.org/docs/latest/spark-procedures/#expire_snapshots "https://iceberg.apache.org/docs/latest/spark-procedures/#expire_snapshots") and [orphan file removal](https://iceberg.apache.org/docs/latest/spark-procedures/#remove_orphan_files "https://iceberg.apache.org/docs/latest/spark-procedures/#remove_orphan_files").

###### Note

`VACUUM` is transactional and is supported only for Apache Iceberg tables
in Athena engine version 3.

The `VACUUM` statement optimizes Iceberg tables by reducing storage
consumption. For more information about using `VACUUM`, see [Optimize Iceberg tables](querying-iceberg-data-optimization.md "querying-iceberg-data-optimization.md"). Note that, because the
`VACUUM` statement makes API calls to Amazon S3, charges apply for the associated
requests to Amazon S3.

###### Warning

If you run a snapshot expiration operation, you can no longer time travel to expired
snapshots.

## Synopsis

To remove data files no longer needed for an Iceberg table, use the following
syntax.

```
VACUUM [`database_name`.]`target_table`
```

- `VACUUM` expects the Iceberg data to be in an Amazon S3 folder rather
  than an Amazon S3 bucket. For example, if your Iceberg data is at
  `s3://amzn-s3-demo-bucket`/ instead of
  `s3://amzn-s3-demo-bucket/myicebergfolder/`, the
  `VACUUM` statement fails with the error message
  **`GENERIC_INTERNAL_ERROR: Path missing in file system location:
`s3://amzn-s3-demo-bucket``**.
- For `VACUUM` to be able to delete data files, your query execution
  role must have `s3:DeleteObject` permissions on the bucket where your
  Iceberg tables, metadata, snapshots, and data files are located. If the
  permission is not present, the `VACUUM` query will succeed, but the
  files will not be deleted.
- To run `VACUUM` on a table with a name that begins with an
  underscore (for example, `_mytable`), enclose the table name in
  backticks, as in the following example. If you prefix the table name with a
  database name, do not enclose the database name in backticks. Note that double
  quotes will not work in place of backticks.

This behavior is particular to `VACUUM`. The `CREATE`
and `INSERT INTO` statements do not require backticks for table names
that begin with underscores.

```
VACUUM `_mytable`
VACUUM my_database.`_mytable`
```

## Operations performed

`VACUUM` performs the following operations:

- Removes snapshots that are older than the amount of time that is specified by
  the `vacuum_max_snapshot_age_seconds` table property. By default,
  this property is set to 432000 seconds (5 days).
- Removes snapshots that are not within the period to be retained that are in
  excess of the number specified by the `vacuum_min_snapshots_to_keep`
  table property. The default is 1.

You can specify these table properties in your `CREATE TABLE`
statement. After the table has been created, you can use the [ALTER TABLE SET
TBLPROPERTIES](querying-iceberg-alter-table-set-properties.md "querying-iceberg-alter-table-set-properties.md") statement to
update them.

- Removes any metadata and data files that are unreachable as a result of the
  snapshot removal. You can configure the number of old metadata files to be
  retained by setting the `vacuum_max_metadata_files_to_keep` table
  property. The default value is 100.
- Removes orphan files that are older than the time specified in the
  `vacuum_max_snapshot_age_seconds` table property. Orphan files
  are files in the table's data directory that are not part of the table
  state.

For more information about creating and managing Apache Iceberg tables in Athena, see
[Create Iceberg tables](querying-iceberg-creating-tables.md "querying-iceberg-creating-tables.md") and [Manage Iceberg tables](querying-iceberg-managing-tables.md "querying-iceberg-managing-tables.md").
