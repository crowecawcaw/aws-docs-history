# Understanding partitioning in Babelfish

Starting with version 4.3.0, Babelfish introduces table and index partitioning with limited support.
The following sections provide details on creating partition functions, defining partition schemes, and implementing partitioned tables and indexes in Babelfish.

###### Topics

- [Introducing to partitioning in Babelfish](#babelfish-partition-function-views "#babelfish-partition-function-views")
- [Limitations and workarounds](#babelfish-partition-limitations "#babelfish-partition-limitations")

## Introducing to partitioning in Babelfish

- Partition functions:
  - `CREATE PARTITION FUNCTION:` Defines how a table or index is partitioned by specifying the partitioning column type and the range of values for each partition.
  - `DROP PARTITION FUNCTION:` Removes an existing partition function.

- Partition schemes:
  - `CREATE PARTITION SCHEME:` Defines the mapping between partitions and filegroups.

  ###### Note

  In Babelfish, filegroups are treated as dummy objects and do not represent physical storage locations.
  - `DROP PARTITION SCHEME:` Removes an existing partition scheme.

- System function:
  - `$PARTITION:` This system function returns the partition number to which a specified value in a partitioning column would belong in a specified partitioned table.

- Partitioned tables and indexes:
  - `CREATE TABLE ... ON partition_scheme_name (partition_column_name):` Creates a partitioned table based on a specified partition scheme and partitioning column.
  - `CREATE INDEX ... ON partition_scheme_name (partition_column_name):` Creates a partitioned index based on a specified partition scheme and partitioning column.

- System views for partitioning metadata:

The following system views are added to provide metadata related to partitioning:

    + `sys.destination_data_spaces`
    + `sys.partitions`
    + `sys.partition_functions`
    + `sys.partition_parameters`
    + `sys.partition_range_values`
    + `sys.partition_schemes`

## Limitations and workarounds

The following SQL Server partitioning capabilities aren't yet supported by Babelfish:

- `ALTER PARTITION FUNCTION` and `ALTER PARTITION SCHEME`.

###### Note

Babelfish doesn't support split and merge operations. Define all partitions in the
partition functions during creation because you can't add or remove partitions later.

- Computed columns as partitioning columns.
- `INSERT BULK` and `BCP` utility for partitioned tables.
- `LEFT` boundary option for partition functions.
- `SQL_VARIANT` data type for partition functions.
- `TRUNCATE TABLE ... WITH PARTITION`.
- `ALTER TABLE ... SWITCH PARTITION`.
- Un-aligned partitioned indexes such as partition scheme and partition column that differs from the partitioned table.
- DMS migration from Babelfish source is supported only for Full Load tasks on partitioned tables.
- Babelfish doesn't support these syntax options but provides workarounds:
  - Usage of partition scheme with constraints or indexes in the CREATE TABLE statement.
  - ALTER TABLE ... ADD CONSTRAINT ... ON partition_scheme_name (partition_column_name).

###### Note

You can set the `babelfishpg_tsql.escape_hatch_storage_on_partition` escape hatch to ignore. This will allow the parser to ignore the partition scheme option used with constraints or indexes,
and the backend will create individual constraints or indexes for each partition.
