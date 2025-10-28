Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Materialized views on external data

lake tables in Amazon Redshift Spectrum

Materialized views can provide incremental maintenance on external data lake tables.
With incremental maintenance, Amazon Redshift updates the data in the materialized view with only
the changes to the data in the base tables since the last refresh. Incremental
maintenance is more cost effective than fully recomputing the materialized view after
every data change on the base table.

When you use materialized views on at least one external table, materialized view
creation is incremental on:

- Standard data lake tables, partitioned and unpartitioned, with data files
  in any supported format (Parquet, Avro, CSV, etc.).
- Apache Iceberg tables, partitioned and unpartitioned, with copy-on-write
  and merge-on-read.
- Amazon Redshift Spectrum tables joined with any Amazon Redshift table in the same database.
  Materialized view refresh is incremental on:

- Standard data lake tables after S3 DELETE or PUT overwrite (deletion of
  data files), if the materialized view doesn't perform aggregation.
- Apache Iceberg tables after INSERT, DELETE, UPDATE, or table
  compaction.
  For more information about Amazon Redshift Spectrum, see [Amazon Redshift Spectrum](c-using-spectrum.md "c-using-spectrum.md").

## Limitations

General limitations on materialized views still apply for materialized views on
data lake tables. For more information, see [Refreshing a materialized view](materialized-view-refresh.md "materialized-view-refresh.md").
In addition, consider the following limitations when you use materialized views on
external data lake tables.

- Materialized view creation is non-incremental on:
  - Hudi or Delta Lake tables.
  - Spectrum nested data access.
  - References to VARBYTE columns.

- Materialized view refresh falls back to full recomputation on:
  - Apache Iceberg tables when a required snapshot is expired, if the
    materialized view performs aggregation.
  - Standard data lake tables after deletion or update of data files
    on Amazon S3, if the materialized view performs aggregation.
  - Standard data lake tables refreshed more than once within a
    transaction block.
  - Standard data lake tables governed by a manifest. For more
    information about manifests, see [Using a manifest to specify
    data files](r_COPY_command_examples.md#copy-command-examples-manifest "r_COPY_command_examples.md#copy-command-examples-manifest").
  - Amazon Redshift falls back to full recompute if this is expected to be more
    performant, in particular for materialized views that contain joins
    and more than one base table has been updated since the last
    refresh.

- On Apache Iceberg tables, materialized view refresh can handle only up to
  4 million positions deleted in a single data file. Once this limit is
  reached, the Apache Iceberg base table must be compacted to continue
  refreshing the materialized view.
- On Apache Iceberg tables, concurrency scaling is not supported for
  materialized view creation and refresh.
- Autonomics features are not supported. These include [automated
  materialized views](materialized-view-auto-mv.md "materialized-view-auto-mv.md") and [automatic
  query rewrite](materialized-view-auto-rewrite.md "materialized-view-auto-rewrite.md").
- When an incremental materialized view is refreshed, IAM permissions
  apply only to the accessed portions of the Amazon Redshift base tables.
- Changes in permissions managed by Lake Formation are not verified on querying a materialized view.
  This means that if a materialized view is defined on a data lake table and select privileges are removed from the table
  with Lake Formation, then you can still query the materialized view.
