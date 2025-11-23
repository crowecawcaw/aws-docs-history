# Optimize Iceberg tables

Athena provides several optimization features to improve query performance on Apache Iceberg tables.
As data accumulates, queries can become less efficient due to increased file processing overhead and the
computational cost of applying row-level deletes stored in Iceberg delete files. To address these challenges,
Athena supports manual compaction and vacuum operators to optimize table structure. Athena also works with
Iceberg statistics to enable cost-based query optimization and Parquet column indexing for precise data
pruning during query execution. These features work together to reduce query execution time, minimize data
scanning, and lower costs. This topic describes how to use these optimization capabilities to maintain
high-performance queries on your Iceberg tables.

## OPTIMIZE

The `OPTIMIZE `table` REWRITE DATA` compaction
action rewrites data files into a more optimized layout based on their size and
number of associated delete files. For syntax and table property details, see [OPTIMIZE](optimize-statement.md "optimize-statement.md").

### Example

The following example merges delete files into data files and produces files
near the targeted file size where the value of `category` is
`c1`.

```
OPTIMIZE iceberg_table REWRITE DATA USING BIN_PACK
  WHERE category = 'c1'
```

## VACUUM

`VACUUM` performs [snapshot expiration](https://iceberg.apache.org/docs/latest/spark-procedures/#expire_snapshots "https://iceberg.apache.org/docs/latest/spark-procedures/#expire_snapshots") and [orphan file removal](https://iceberg.apache.org/docs/latest/spark-procedures/#remove_orphan_files "https://iceberg.apache.org/docs/latest/spark-procedures/#remove_orphan_files"). These actions reduce metadata size and remove
files not in the current table state that are also older than the retention period
specified for the table. For syntax details, see [VACUUM](vacuum-statement.md "vacuum-statement.md").

### Example

The following example uses a table property to configure the table
`iceberg_table` to retain the last three days of data, then uses
`VACUUM` to expire the old snapshots and remove the orphan files
from the table.

```
ALTER TABLE iceberg_table SET TBLPROPERTIES (
  'vacuum_max_snapshot_age_seconds'='259200'
)

VACUUM iceberg_table
```

## Use Iceberg table statistics

Athena's cost-based optimizer uses Iceberg statistics to produce optimal query plans. When statistics have been generated for your Iceberg tables,
Athena automatically uses this information to make intelligent decisions about join ordering, filters, and aggregation behavior, often improving query
performance and reducing costs.

Iceberg statistics are turned on by default when you use S3 Tables. For other Iceberg tables, Athena uses the table property `use_iceberg_statistics` to
determine whether to leverage statistics for cost-based optimization. To get started, see
[Optimizing query performance using column statistics](../../../glue/latest/dg/column-statistics.md "../../../glue/latest/dg/column-statistics.md") in
the _AWS Glue User Guide_ or use the [Athena console](cost-based-optimizer.md "cost-based-optimizer.md") to generate on-demand statistics on your Iceberg tables.

## Use Parquet column indexing

Parquet column indexing makes it possible for Athena to perform more precise data pruning during query execution by leveraging page-level
min/max statistics in addition to row group-level statistics. This allows Athena to skip unnecessary pages within row groups, significantly
reducing the amount of data scanned and improving query performance. It works best for queries with selective filter predicates on sorted columns,
improving both execution time and data scan efficiency while reducing the amount of data Athena needs to read from Amazon S3.

Athena uses Parquet column indexes by default with S3 Tables if column indexes are present in the underlying Parquet files. For other Iceberg tables,
Athena uses the `use_iceberg_parquet_column_index` property to determine whether to utilize the column indexes in the Parquet file. Set
this table property using the AWS Glue console or `UpdateTable` API.
