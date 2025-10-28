# Table optimizer API

The table optimizer API describes the AWS Glue API for enabling
compaction to improve read performance.

## Data types

- [TableOptimizer structure](#aws-glue-api-table-optimizers-TableOptimizer "#aws-glue-api-table-optimizers-TableOptimizer")
- [TableOptimizerConfiguration structure](#aws-glue-api-table-optimizers-TableOptimizerConfiguration "#aws-glue-api-table-optimizers-TableOptimizerConfiguration")
- [TableOptimizerVpcConfiguration structure](#aws-glue-api-table-optimizers-TableOptimizerVpcConfiguration "#aws-glue-api-table-optimizers-TableOptimizerVpcConfiguration")
- [CompactionConfiguration structure](#aws-glue-api-table-optimizers-CompactionConfiguration "#aws-glue-api-table-optimizers-CompactionConfiguration")
- [IcebergCompactionConfiguration structure](#aws-glue-api-table-optimizers-IcebergCompactionConfiguration "#aws-glue-api-table-optimizers-IcebergCompactionConfiguration")
- [TableOptimizerRun structure](#aws-glue-api-table-optimizers-TableOptimizerRun "#aws-glue-api-table-optimizers-TableOptimizerRun")
- [BatchGetTableOptimizerEntry structure](#aws-glue-api-table-optimizers-BatchGetTableOptimizerEntry "#aws-glue-api-table-optimizers-BatchGetTableOptimizerEntry")
- [BatchTableOptimizer structure](#aws-glue-api-table-optimizers-BatchTableOptimizer "#aws-glue-api-table-optimizers-BatchTableOptimizer")
- [BatchGetTableOptimizerError structure](#aws-glue-api-table-optimizers-BatchGetTableOptimizerError "#aws-glue-api-table-optimizers-BatchGetTableOptimizerError")
- [RetentionConfiguration structure](#aws-glue-api-table-optimizers-RetentionConfiguration "#aws-glue-api-table-optimizers-RetentionConfiguration")
- [IcebergRetentionConfiguration structure](#aws-glue-api-table-optimizers-IcebergRetentionConfiguration "#aws-glue-api-table-optimizers-IcebergRetentionConfiguration")
- [OrphanFileDeletionConfiguration structure](#aws-glue-api-table-optimizers-OrphanFileDeletionConfiguration "#aws-glue-api-table-optimizers-OrphanFileDeletionConfiguration")
- [IcebergOrphanFileDeletionConfiguration structure](#aws-glue-api-table-optimizers-IcebergOrphanFileDeletionConfiguration "#aws-glue-api-table-optimizers-IcebergOrphanFileDeletionConfiguration")
- [CompactionMetrics structure](#aws-glue-api-table-optimizers-CompactionMetrics "#aws-glue-api-table-optimizers-CompactionMetrics")
- [RetentionMetrics structure](#aws-glue-api-table-optimizers-RetentionMetrics "#aws-glue-api-table-optimizers-RetentionMetrics")
- [OrphanFileDeletionMetrics structure](#aws-glue-api-table-optimizers-OrphanFileDeletionMetrics "#aws-glue-api-table-optimizers-OrphanFileDeletionMetrics")
- [IcebergCompactionMetrics structure](#aws-glue-api-table-optimizers-IcebergCompactionMetrics "#aws-glue-api-table-optimizers-IcebergCompactionMetrics")
- [IcebergRetentionMetrics structure](#aws-glue-api-table-optimizers-IcebergRetentionMetrics "#aws-glue-api-table-optimizers-IcebergRetentionMetrics")
- [IcebergOrphanFileDeletionMetrics structure](#aws-glue-api-table-optimizers-IcebergOrphanFileDeletionMetrics "#aws-glue-api-table-optimizers-IcebergOrphanFileDeletionMetrics")
- [RunMetrics structure](#aws-glue-api-table-optimizers-RunMetrics "#aws-glue-api-table-optimizers-RunMetrics")

## TableOptimizer structure

Contains details about an optimizer associated with a table.

###### Fields

- `type` – UTF-8 string (valid values: `compaction="COMPACTION"` | `retention="RETENTION"` | `orphan_file_deletion="ORPHAN_FILE_DELETION"`).

The type of table optimizer. The valid values are:

    + `compaction`: for managing compaction with a table optimizer.
    + `retention`: for managing the retention of snapshot with
     a table optimizer.
    + `orphan_file_deletion`: for managing the deletion of orphan
     files with a table optimizer.

- `configuration` – A [TableOptimizerConfiguration](#aws-glue-api-table-optimizers-TableOptimizerConfiguration "#aws-glue-api-table-optimizers-TableOptimizerConfiguration") object.

A `TableOptimizerConfiguration` object that was specified
when creating or updating a table optimizer.

- `lastRun` – A [TableOptimizerRun](#aws-glue-api-table-optimizers-TableOptimizerRun "#aws-glue-api-table-optimizers-TableOptimizerRun") object.

A `TableOptimizerRun` object representing the last run
of the table optimizer.

- `configurationSource` – UTF-8 string (valid values: `catalog="CATALOG"` | `table="TABLE"`).

Specifies the source of the optimizer configuration. This indicates
how the table optimizer was configured and which entity or service initiated
the configuration.

## TableOptimizerConfiguration structure

Contains details on the configuration of a table optimizer. You pass this
configuration when creating or updating a table optimizer.

###### Fields

- `roleArn` – UTF-8 string, not less than 20 or more than 2048 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A role passed by the caller which gives the service permission to update
the resources associated with the optimizer on the caller's behalf.

- `enabled` – Boolean.

Whether table optimization is enabled.

- `vpcConfiguration` – A [TableOptimizerVpcConfiguration](#aws-glue-api-table-optimizers-TableOptimizerVpcConfiguration "#aws-glue-api-table-optimizers-TableOptimizerVpcConfiguration") object.

A `TableOptimizerVpcConfiguration` object representing
the VPC configuration for a table optimizer.

This configuration is necessary to perform optimization on tables that
are in a customer VPC.

- `compactionConfiguration` – A [CompactionConfiguration](#aws-glue-api-table-optimizers-CompactionConfiguration "#aws-glue-api-table-optimizers-CompactionConfiguration") object.

The configuration for a compaction optimizer. This configuration defines
how data files in your table will be compacted to improve query performance and
reduce storage costs.

- `retentionConfiguration` – A [RetentionConfiguration](#aws-glue-api-table-optimizers-RetentionConfiguration "#aws-glue-api-table-optimizers-RetentionConfiguration") object.

The configuration for a snapshot retention optimizer.

- `orphanFileDeletionConfiguration` – An [OrphanFileDeletionConfiguration](#aws-glue-api-table-optimizers-OrphanFileDeletionConfiguration "#aws-glue-api-table-optimizers-OrphanFileDeletionConfiguration") object.

The configuration for an orphan file deletion optimizer.

## TableOptimizerVpcConfiguration structure

An object that describes the VPC configuration for a table optimizer.

This configuration is necessary to perform optimization on tables that
are in a customer VPC.

###### Fields

- `glueConnectionName` – UTF-8 string, at least 1 byte long.

The name of the AWS Glue connection used for the VPC for the table
optimizer.

## CompactionConfiguration structure

The configuration for a compaction optimizer. This configuration defines
how data files in your table will be compacted to improve query performance and
reduce storage costs.

###### Fields

- `icebergConfiguration` – An [IcebergCompactionConfiguration](#aws-glue-api-table-optimizers-IcebergCompactionConfiguration "#aws-glue-api-table-optimizers-IcebergCompactionConfiguration") object.

The configuration for an Iceberg compaction optimizer.

## IcebergCompactionConfiguration structure

The configuration for an Iceberg compaction optimizer. This configuration
defines parameters for optimizing the layout of data files in Iceberg tables.

###### Fields

- `strategy` – UTF-8 string (valid values: `binpack="BINPACK"` | `sort="SORT"` | `z-order="ZORDER"`).

The strategy to use for compaction. Valid values are:

    + `binpack`: Combines small files into larger files, typically
     targeting sizes over 100MB, while applying any pending deletes. This is the recommended
     compaction strategy for most use cases.
    + `sort`: Organizes data based on specified columns which
     are sorted hierarchically during compaction, improving query performance
     for filtered operations. This strategy is recommended when your queries frequently
     filter on specific columns. To use this strategy, you must first define a sort
     order in your Iceberg table properties using the `sort_order` table
     property.
    + `z-order`: Optimizes data organization by blending multiple
     attributes into a single scalar value that can be used for sorting, allowing efficient
     querying across multiple dimensions. This strategy is recommended when you
     need to query data across multiple dimensions simultaneously. To use this strategy,
     you must first define a sort order in your Iceberg table properties using the `sort_order`
     table property.

If an input is not provided, the default value 'binpack' will be used.

- `minInputFiles` – Number (integer).

The minimum number of data files that must be present in a partition before
compaction will actually compact files. This parameter helps control when compaction
is triggered, preventing unnecessary compaction operations on partitions
with few files. If an input is not provided, the default value 100 will be used.

- `deleteFileThreshold` – Number (integer).

The minimum number of deletes that must be present in a data file to make
it eligible for compaction. This parameter helps optimize compaction by focusing
on files that contain a significant number of delete operations, which can improve
query performance by removing deleted records. If an input is not provided, the
default value 1 will be used.

## TableOptimizerRun structure

Contains details for a table optimizer run.

###### Fields

- `eventType` – UTF-8 string (valid values: `starting="STARTING"` | `completed="COMPLETED"` | `failed="FAILED"` | `in_progress="IN_PROGRESS"`).

An event type representing the status of the table optimizer run.

- `startTimestamp` – Timestamp.

Represents the epoch timestamp at which the compaction job was started
within Lake Formation.

- `endTimestamp` – Timestamp.

Represents the epoch timestamp at which the compaction job ended.

- `metrics` – A [RunMetrics](#aws-glue-api-table-optimizers-RunMetrics "#aws-glue-api-table-optimizers-RunMetrics") object.

A `RunMetrics` object containing metrics for the optimizer
run.

This member is deprecated. See the individual metric members for compaction,
retention, and orphan file deletion.

- `error` – UTF-8 string.

An error that occured during the optimizer run.

- `compactionMetrics` – A [CompactionMetrics](#aws-glue-api-table-optimizers-CompactionMetrics "#aws-glue-api-table-optimizers-CompactionMetrics") object.

A `CompactionMetrics` object containing metrics for the
optimizer run.

- `compactionStrategy` – UTF-8 string (valid values: `binpack="BINPACK"` | `sort="SORT"` | `z-order="ZORDER"`).

The strategy used for the compaction run. Indicates which algorithm was
applied to determine how files were selected and combined during the compaction
process. Valid values are:

    + `binpack`: Combines small files into larger files, typically
     targeting sizes over 100MB, while applying any pending deletes. This is the recommended
     compaction strategy for most use cases.
    + `sort`: Organizes data based on specified columns which
     are sorted hierarchically during compaction, improving query performance
     for filtered operations. This strategy is recommended when your queries frequently
     filter on specific columns. To use this strategy, you must first define a sort
     order in your Iceberg table properties using the `sort_order` table
     property.
    + `z-order`: Optimizes data organization by blending multiple
     attributes into a single scalar value that can be used for sorting, allowing efficient
     querying across multiple dimensions. This strategy is recommended when you
     need to query data across multiple dimensions simultaneously. To use this strategy,
     you must first define a sort order in your Iceberg table properties using the `sort_order`
     table property.

- `retentionMetrics` – A [RetentionMetrics](#aws-glue-api-table-optimizers-RetentionMetrics "#aws-glue-api-table-optimizers-RetentionMetrics") object.

A `RetentionMetrics` object containing metrics for the
optimizer run.

- `orphanFileDeletionMetrics` – An [OrphanFileDeletionMetrics](#aws-glue-api-table-optimizers-OrphanFileDeletionMetrics "#aws-glue-api-table-optimizers-OrphanFileDeletionMetrics") object.

An `OrphanFileDeletionMetrics` object containing metrics
for the optimizer run.

## BatchGetTableOptimizerEntry structure

Represents a table optimizer to retrieve in the `BatchGetTableOptimizer`
operation.

###### Fields

- `catalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Catalog ID of the table.

- `databaseName` – UTF-8 string, at least 1 byte long.

The name of the database in the catalog in which the table resides.

- `tableName` – UTF-8 string, at least 1 byte long.

The name of the table.

- `type` – UTF-8 string (valid values: `compaction="COMPACTION"` | `retention="RETENTION"` | `orphan_file_deletion="ORPHAN_FILE_DELETION"`).

The type of table optimizer.

## BatchTableOptimizer structure

Contains details for one of the table optimizers returned by the `BatchGetTableOptimizer`
operation.

###### Fields

- `catalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Catalog ID of the table.

- `databaseName` – UTF-8 string, at least 1 byte long.

The name of the database in the catalog in which the table resides.

- `tableName` – UTF-8 string, at least 1 byte long.

The name of the table.

- `tableOptimizer` – A [TableOptimizer](#aws-glue-api-table-optimizers-TableOptimizer "#aws-glue-api-table-optimizers-TableOptimizer") object.

A `TableOptimizer` object that contains details on the configuration
and last run of a table optimizer.

## BatchGetTableOptimizerError structure

Contains details on one of the errors in the error list returned by the `BatchGetTableOptimizer`
operation.

###### Fields

- `error` – An [ErrorDetail](aws-glue-api-common.md#aws-glue-api-common-ErrorDetail "aws-glue-api-common.md#aws-glue-api-common-ErrorDetail") object.

An `ErrorDetail` object containing code and message details
about the error.

- `catalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Catalog ID of the table.

- `databaseName` – UTF-8 string, at least 1 byte long.

The name of the database in the catalog in which the table resides.

- `tableName` – UTF-8 string, at least 1 byte long.

The name of the table.

- `type` – UTF-8 string (valid values: `compaction="COMPACTION"` | `retention="RETENTION"` | `orphan_file_deletion="ORPHAN_FILE_DELETION"`).

The type of table optimizer.

## RetentionConfiguration structure

The configuration for a snapshot retention optimizer.

###### Fields

- `icebergConfiguration` – An [IcebergRetentionConfiguration](#aws-glue-api-table-optimizers-IcebergRetentionConfiguration "#aws-glue-api-table-optimizers-IcebergRetentionConfiguration") object.

The configuration for an Iceberg snapshot retention optimizer.

## IcebergRetentionConfiguration structure

The configuration for an Iceberg snapshot retention optimizer.

###### Fields

- `snapshotRetentionPeriodInDays` – Number (integer).

The number of days to retain the Iceberg snapshots. If an input is not provided,
the corresponding Iceberg table configuration field will be used or if not present,
the default value 5 will be used.

- `numberOfSnapshotsToRetain` – Number (integer).

The number of Iceberg snapshots to retain within the retention period.
If an input is not provided, the corresponding Iceberg table configuration field
will be used or if not present, the default value 1 will be used.

- `cleanExpiredFiles` – Boolean.

If set to false, snapshots are only deleted from table metadata, and the
underlying data and metadata files are not deleted.

- `runRateInHours` – Number (integer).

The interval in hours between retention job runs. This parameter controls
how frequently the retention optimizer will run to clean up expired snapshots.
The value must be between 3 and 168 hours (7 days). If an input is not provided, the
default value 24 will be used.

## OrphanFileDeletionConfiguration structure

The configuration for an orphan file deletion optimizer.

###### Fields

- `icebergConfiguration` – An [IcebergOrphanFileDeletionConfiguration](#aws-glue-api-table-optimizers-IcebergOrphanFileDeletionConfiguration "#aws-glue-api-table-optimizers-IcebergOrphanFileDeletionConfiguration") object.

The configuration for an Iceberg orphan file deletion optimizer.

## IcebergOrphanFileDeletionConfiguration structure

The configuration for an Iceberg orphan file deletion optimizer.

###### Fields

- `orphanFileRetentionPeriodInDays` – Number (integer).

The number of days that orphan files should be retained before file deletion.
If an input is not provided, the default value 3 will be used.

- `location` – UTF-8 string.

Specifies a directory in which to look for files (defaults to the table's
location). You may choose a sub-directory rather than the top-level table location.

- `runRateInHours` – Number (integer).

The interval in hours between orphan file deletion job runs. This parameter
controls how frequently the orphan file deletion optimizer will run to clean
up orphan files. The value must be between 3 and 168 hours (7 days). If an input is
not provided, the default value 24 will be used.

## CompactionMetrics structure

A structure that contains compaction metrics for the optimizer run.

###### Fields

- `IcebergMetrics` – An [IcebergCompactionMetrics](#aws-glue-api-table-optimizers-IcebergCompactionMetrics "#aws-glue-api-table-optimizers-IcebergCompactionMetrics") object.

A structure containing the Iceberg compaction metrics for the optimizer
run.

## RetentionMetrics structure

A structure that contains retention metrics for the optimizer run.

###### Fields

- `IcebergMetrics` – An [IcebergRetentionMetrics](#aws-glue-api-table-optimizers-IcebergRetentionMetrics "#aws-glue-api-table-optimizers-IcebergRetentionMetrics") object.

A structure containing the Iceberg retention metrics for the optimizer
run.

## OrphanFileDeletionMetrics structure

A structure that contains orphan file deletion metrics for the optimizer
run.

###### Fields

- `IcebergMetrics` – An [IcebergOrphanFileDeletionMetrics](#aws-glue-api-table-optimizers-IcebergOrphanFileDeletionMetrics "#aws-glue-api-table-optimizers-IcebergOrphanFileDeletionMetrics") object.

A structure containing the Iceberg orphan file deletion metrics for the
optimizer run.

## IcebergCompactionMetrics structure

Compaction metrics for Iceberg for the optimizer run.

###### Fields

- `DpuHours` – Number (double).

The number of DPU hours consumed by the job.

- `NumberOfDpus` – Number (Integer).

The number of DPUs consumed by the job, rounded up to the nearest whole number.

- `JobDurationInHour` – Number (double).

The duration of the job in hours.

## IcebergRetentionMetrics structure

Snapshot retention metrics for Iceberg for the optimizer run.

###### Fields

- `DpuHours` – Number (double).

The number of DPU hours consumed by the job.

- `NumberOfDpus` – Number (Integer).

The number of DPUs consumed by the job, rounded up to the nearest whole number.

- `JobDurationInHour` – Number (double).

The duration of the job in hours.

## IcebergOrphanFileDeletionMetrics structure

Orphan file deletion metrics for Iceberg for the optimizer run.

###### Fields

- `DpuHours` – Number (double).

The number of DPU hours consumed by the job.

- `NumberOfDpus` – Number (Integer).

The number of DPUs consumed by the job, rounded up to the nearest whole number.

- `JobDurationInHour` – Number (double).

The duration of the job in hours.

## RunMetrics structure

Metrics for the optimizer run.

This structure is deprecated. See the individual metric members for compaction,
retention, and orphan file deletion.

###### Fields

- `NumberOfBytesCompacted` – UTF-8 string.

The number of bytes removed by the compaction job run.

- `NumberOfFilesCompacted` – UTF-8 string.

The number of files removed by the compaction job run.

- `NumberOfDpus` – UTF-8 string.

The number of DPUs consumed by the job, rounded up to the nearest whole number.

- `JobDurationInHour` – UTF-8 string.

The duration of the job in hours.

## Operations

- [GetTableOptimizer action (Python: get_table_optimizer)](#aws-glue-api-table-optimizers-GetTableOptimizer "#aws-glue-api-table-optimizers-GetTableOptimizer")
- [BatchGetTableOptimizer action (Python: batch_get_table_optimizer)](#aws-glue-api-table-optimizers-BatchGetTableOptimizer "#aws-glue-api-table-optimizers-BatchGetTableOptimizer")
- [ListTableOptimizerRuns action (Python: list_table_optimizer_runs)](#aws-glue-api-table-optimizers-ListTableOptimizerRuns "#aws-glue-api-table-optimizers-ListTableOptimizerRuns")
- [CreateTableOptimizer action (Python: create_table_optimizer)](#aws-glue-api-table-optimizers-CreateTableOptimizer "#aws-glue-api-table-optimizers-CreateTableOptimizer")
- [DeleteTableOptimizer action (Python: delete_table_optimizer)](#aws-glue-api-table-optimizers-DeleteTableOptimizer "#aws-glue-api-table-optimizers-DeleteTableOptimizer")
- [UpdateTableOptimizer action (Python: update_table_optimizer)](#aws-glue-api-table-optimizers-UpdateTableOptimizer "#aws-glue-api-table-optimizers-UpdateTableOptimizer")

## GetTableOptimizer action (Python: get_table_optimizer)

Returns the configuration of all optimizers associated with a specified
table.

###### Request

- `CatalogId` – _Required:_ Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Catalog ID of the table.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database in the catalog in which the table resides.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table.

- `Type` – _Required:_ UTF-8 string (valid values: `compaction="COMPACTION"` | `retention="RETENTION"` | `orphan_file_deletion="ORPHAN_FILE_DELETION"`).

The type of table optimizer.

###### Response

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Catalog ID of the table.

- `DatabaseName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database in the catalog in which the table resides.

- `TableName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table.

- `TableOptimizer` – A [TableOptimizer](#aws-glue-api-table-optimizers-TableOptimizer "#aws-glue-api-table-optimizers-TableOptimizer") object.

The optimizer associated with the specified table.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `AccessDeniedException`
- `InternalServiceException`
- `ThrottlingException`

## BatchGetTableOptimizer action (Python: batch_get_table_optimizer)

Returns the configuration for the specified table optimizers.

###### Request

- `Entries` – _Required:_ An array of [BatchGetTableOptimizerEntry](#aws-glue-api-table-optimizers-BatchGetTableOptimizerEntry "#aws-glue-api-table-optimizers-BatchGetTableOptimizerEntry") objects.

A list of `BatchGetTableOptimizerEntry` objects specifying
the table optimizers to retrieve.

###### Response

- `TableOptimizers` – An array of [BatchTableOptimizer](#aws-glue-api-table-optimizers-BatchTableOptimizer "#aws-glue-api-table-optimizers-BatchTableOptimizer") objects.

A list of `BatchTableOptimizer` objects.

- `Failures` – An array of [BatchGetTableOptimizerError](#aws-glue-api-table-optimizers-BatchGetTableOptimizerError "#aws-glue-api-table-optimizers-BatchGetTableOptimizerError") objects.

A list of errors from the operation.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `AccessDeniedException`
- `InternalServiceException`
- `ThrottlingException`

## ListTableOptimizerRuns action (Python: list_table_optimizer_runs)

Lists the history of previous optimizer runs for a specific table.

###### Request

- `CatalogId` – _Required:_ Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Catalog ID of the table.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database in the catalog in which the table resides.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table.

- `Type` – _Required:_ UTF-8 string (valid values: `compaction="COMPACTION"` | `retention="RETENTION"` | `orphan_file_deletion="ORPHAN_FILE_DELETION"`).

The type of table optimizer.

- `MaxResults` – Number (integer).

The maximum number of optimizer runs to return on each call.

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation call.

###### Response

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Catalog ID of the table.

- `DatabaseName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database in the catalog in which the table resides.

- `TableName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table.

- `NextToken` – UTF-8 string.

A continuation token for paginating the returned list of optimizer runs,
returned if the current segment of the list is not the last.

- `TableOptimizerRuns` – An array of [TableOptimizerRun](#aws-glue-api-table-optimizers-TableOptimizerRun "#aws-glue-api-table-optimizers-TableOptimizerRun") objects.

A list of the optimizer runs associated with a table.

###### Errors

- `EntityNotFoundException`
- `AccessDeniedException`
- `InvalidInputException`
- `ValidationException`
- `InternalServiceException`
- `ThrottlingException`

## CreateTableOptimizer action (Python: create_table_optimizer)

Creates a new table optimizer for a specific function.

###### Request

- `CatalogId` – _Required:_ Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Catalog ID of the table.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database in the catalog in which the table resides.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table.

- `Type` – _Required:_ UTF-8 string (valid values: `compaction="COMPACTION"` | `retention="RETENTION"` | `orphan_file_deletion="ORPHAN_FILE_DELETION"`).

The type of table optimizer.

- `TableOptimizerConfiguration` – _Required:_ A [TableOptimizerConfiguration](#aws-glue-api-table-optimizers-TableOptimizerConfiguration "#aws-glue-api-table-optimizers-TableOptimizerConfiguration") object.

A `TableOptimizerConfiguration` object representing
the configuration of a table optimizer.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `ValidationException`
- `InvalidInputException`
- `AccessDeniedException`
- `AlreadyExistsException`
- `InternalServiceException`
- `ThrottlingException`

## DeleteTableOptimizer action (Python: delete_table_optimizer)

Deletes an optimizer and all associated metadata for a table. The optimization
will no longer be performed on the table.

###### Request

- `CatalogId` – _Required:_ Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Catalog ID of the table.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database in the catalog in which the table resides.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table.

- `Type` – _Required:_ UTF-8 string (valid values: `compaction="COMPACTION"` | `retention="RETENTION"` | `orphan_file_deletion="ORPHAN_FILE_DELETION"`).

The type of table optimizer.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `AccessDeniedException`
- `InternalServiceException`
- `ThrottlingException`

## UpdateTableOptimizer action (Python: update_table_optimizer)

Updates the configuration for an existing table optimizer.

###### Request

- `CatalogId` – _Required:_ Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Catalog ID of the table.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database in the catalog in which the table resides.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table.

- `Type` – _Required:_ UTF-8 string (valid values: `compaction="COMPACTION"` | `retention="RETENTION"` | `orphan_file_deletion="ORPHAN_FILE_DELETION"`).

The type of table optimizer.

- `TableOptimizerConfiguration` – _Required:_ A [TableOptimizerConfiguration](#aws-glue-api-table-optimizers-TableOptimizerConfiguration "#aws-glue-api-table-optimizers-TableOptimizerConfiguration") object.

A `TableOptimizerConfiguration` object representing
the configuration of a table optimizer.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `AccessDeniedException`
- `ValidationException`
- `InternalServiceException`
- `ThrottlingException`
- `ConcurrentModificationException`
