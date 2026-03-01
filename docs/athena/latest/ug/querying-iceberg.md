# Query Apache Iceberg tables

You can use Athena to perform read, time travel, write, and DDL queries on Apache Iceberg
tables.

[Apache Iceberg](https://iceberg.apache.org/ "https://iceberg.apache.org/") is an open table format
for very large analytic datasets. Iceberg manages large collections of files as tables, and
it supports modern analytical data lake operations such as record-level insert, update,
delete, and time travel queries. The Iceberg specification allows seamless table evolution
such as schema and partition evolution and is designed for optimized usage on Amazon S3. Iceberg
also helps guarantee data correctness under concurrent write scenarios.

For more information about Apache Iceberg, see [https://iceberg.apache.org/](https://iceberg.apache.org/ "https://iceberg.apache.org/").

## Considerations and limitations

Athena support for Iceberg tables has the following considerations and
limitations:

- Iceberg version support – Athena supports
  Apache Iceberg version 1.4.2.
- Tables registered with Lake Formation – Athena does not currently
  support DDL operations on Iceberg tables that are registered with Lake Formation.
- Queries against information schema –
  When querying the information schema of Iceberg tables, Athena uses S3 metadata
  as the source of truth for column metadata. This means that column information
  is derived from the underlying S3 files rather than from the catalog metadata.
  This behavior differs from other table formats where catalog metadata might be
  the primary source for column information.
- Tables with AWS Glue catalog only – Only
  Iceberg tables created against the AWS Glue catalog based on specifications defined
  by the [open source glue catalog implementation](https://iceberg.apache.org/docs/latest/aws/#glue-catalog "https://iceberg.apache.org/docs/latest/aws/#glue-catalog") are supported from
  Athena.
- Table locking support by AWS Glue only –
  Unlike the open source Glue catalog implementation, which supports plug-in
  custom locking, Athena supports AWS Glue optimistic locking only. Using Athena to
  modify an Iceberg table with any other lock implementation will cause potential
  data loss and break transactions.
- Supported file formats – Athena engine version 3
  supports the following Iceberg file formats.
  - Parquet
  - ORC
  - Avro

- Iceberg restricted metadata – Lake Formation does
  not evaluate the Iceberg metadata tables. Hence, the Iceberg metadata tables are
  restricted if there are any Lake Formation row or cell filters present on the base table
  or if you do not have permissions to view all columns in the base table. For
  such cases, when you query the `$partitions`, `$files`,
  `$manifests`, and `$snapshots` Iceberg metadata
  tables, it fails and you get an `AccessDeniedException` error.
  Additionally, the metadata column `$path` has the same Lake Formation
  restrictions and fails when selected by the query. All other metadata tables can
  be queried regardless of the Lake Formation filters. For more information, see [Metadata tables](https://trino.io/docs/current/connector/iceberg.html#metadata-tables "https://trino.io/docs/current/connector/iceberg.html#metadata-tables").
- Iceberg v2 tables – Athena only creates
  and operates on Iceberg v2 tables. For the difference between v1 and v2 tables,
  see [Format version changes](https://iceberg.apache.org/spec/#appendix-e-format-version-changes "https://iceberg.apache.org/spec/#appendix-e-format-version-changes") in the Apache Iceberg documentation.
- Display of time types without time zone
  – The time and timestamp without time zone types are displayed in UTC. If
  the time zone is unspecified in a filter expression on a time column, UTC is
  used.
- Timestamp related data precision –
  Although Iceberg supports microsecond precision for the timestamp data type,
  Athena supports only millisecond precision for timestamps in both reads and
  writes. For data in time related columns that is rewritten during manual
  compaction operations, Athena retains only millisecond precision.
- Unsupported operations – The following
  Athena operations are not supported for Iceberg tables.
  - [ALTER TABLE SET LOCATION](alter-table-set-location.md "alter-table-set-location.md")

- Views – Use `CREATE VIEW` to
  create Athena views as described in [Work with views](views.md "views.md"). If you are interested in using the [Iceberg view specification](https://github.com/apache/iceberg/blob/master/format/view-spec.md "https://github.com/apache/iceberg/blob/master/format/view-spec.md") to create views, contact [athena-feedback@amazon.com](mailto:athena-feedback@amazon.com "mailto:athena-feedback@amazon.com").
- TTF management commands not supported in
  AWS Lake Formation – Although you can use Lake Formation to manage read access
  permissions for TransactionTable Formats (TTFs) like Apache Iceberg, Apache
  Hudi, and Linux Foundation Delta Lake, you cannot use Lake Formation to manage permissions
  for operations like `VACUUM`, `MERGE`, `UPDATE`
  or `OPTIMIZE` with these table formats. For more information about
  Lake Formation integration with Athena, see [Using AWS Lake Formation with
  Amazon Athena](../../../lake-formation/latest/dg/athena-lf.md "../../../lake-formation/latest/dg/athena-lf.md") in the _AWS Lake Formation Developer Guide_.
- Partitioning by nested fields –
  Partitioning by nested fields is not supported. Attempting to do so produces the
  message **`NOT_SUPPORTED: Partitioning by nested field is
 unsupported:`**
  `column_name`.`nested_field_name`.
- Skipping Amazon Glacier objects not supported –
  If objects in the Apache Iceberg table are in an Amazon Glacier storage class, setting the
  `read_restored_glacier_objects` table property to
  `false` has no effect.

For example, suppose you issue the following command:

```
ALTER TABLE `table_name` SET TBLPROPERTIES ('read_restored_glacier_objects' = 'false')
```

For Iceberg and Delta Lake tables, the command produces the error
**`Unsupported table property key:
 read_restored_glacier_objects`**. For Hudi tables, the `ALTER
 TABLE` command does not produce an error, but Amazon Glacier objects are still
not skipped. Running `SELECT` queries after the `ALTER
 TABLE` command continues to return all objects.

If you would like Athena to support a particular feature, send feedback to [athena-feedback@amazon.com](mailto:athena-feedback@amazon.com "mailto:athena-feedback@amazon.com").

###### Topics

- [Create Iceberg tables](querying-iceberg-creating-tables.md "querying-iceberg-creating-tables.md")
- [Query Iceberg table data](querying-iceberg-table-data.md "querying-iceberg-table-data.md")
- [Perform time travel and version travel queries](querying-iceberg-time-travel-and-version-travel-queries.md "querying-iceberg-time-travel-and-version-travel-queries.md")
- [Update Iceberg table data](querying-iceberg-updating-iceberg-table-data.md "querying-iceberg-updating-iceberg-table-data.md")
- [Manage Iceberg tables](querying-iceberg-managing-tables.md "querying-iceberg-managing-tables.md")
- [Evolve Iceberg table schema](querying-iceberg-evolving-table-schema.md "querying-iceberg-evolving-table-schema.md")
- [Perform other DDL operations on Iceberg tables](querying-iceberg-additional-operations.md "querying-iceberg-additional-operations.md")
- [Optimize Iceberg tables](querying-iceberg-data-optimization.md "querying-iceberg-data-optimization.md")
- [Query AWS Glue Data Catalog materialized views](querying-iceberg-gdc-mv.md "querying-iceberg-gdc-mv.md")
- [Supported data types for Iceberg tables in Athena](querying-iceberg-supported-data-types.md "querying-iceberg-supported-data-types.md")
- [Additional resources](querying-iceberg-additional-resources.md "querying-iceberg-additional-resources.md")
