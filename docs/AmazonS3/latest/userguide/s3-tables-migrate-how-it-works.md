

# How to migrate a table to S3 Tables
<a name="s3-tables-migrate-how-it-works"></a>

S3 Tables migration creates an Apache Iceberg table from an existing AWS Glue Data Catalog Apache Hive table that's stored as Apache Parquet. The migration job validates, transforms, and optimizes your data. Your source data remains available throughout the migration.

When you start a migration, the migration job automatically creates a read-only destination table in S3 Tables, and manages it for the duration of the migration. The table remains read-only until you complete the migration so that a later sync doesn't overwrite your changes. You can delete the destination table at any time.

For more information, see the following topics.

**Topics**
+ [Start, Sync, and Complete](#s3-tables-migrate-lifecycle)
+ [What you can do during a migration](#s3-tables-migrate-during)
+ [How data is migrated](#s3-tables-migrate-how-data)
+ [Migration policy](#s3-tables-migrate-migration-policies)
+ [Partitioning](#s3-tables-migrate-partitioning)
+ [Data type mappings for table migration](s3-tables-migrate-data-type-mappings.md)
+ [Migration reports and statistics](s3-tables-migrate-reports.md)

## Start, Sync, and Complete
<a name="s3-tables-migrate-lifecycle"></a>

![The three steps of a table migration: Start, which creates a new destination table and migrates the source data; Sync, which catches up the changes in the source and can be repeated as needed; and Complete, which makes the table read-write for your engines.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/images/s3-tables-migrate-lifecycle.png)


You migrate a table in three steps:

1. **Start** – `StartTableMigration` creates a new destination table with the specified table name from the defined source table and copies the source data. You can optionally set additional configurations such as schema, compression codec, and migration policy.

1. **Sync** – `SyncTableMigration` copies only the objects and partitions that changed since the previous start or sync, even if the change is only within part of a partition. Sync is an optional step, and you can sync as many times as you need. You also use sync to resume a failed or cancelled migration.

1. **Complete** – `CompleteTableMigration` enables writes on the destination table in addition to reads, and turns on table maintenance. After you complete a migration, no further migration operations are permitted.

Only one start or sync operation can run on a destination table at a time. If a start or sync fails or is cancelled, see [Data from failed or cancelled migrations](s3-tables-migrate-running.md#s3-tables-migrate-failed-data).

## What you can do during a migration
<a name="s3-tables-migrate-during"></a>

You do not have to alter the workloads running on your source table before or during the migration. You can read, write, and delete objects in your source table. In the destination table, you can query the data and delete the table at any time during the migration. Queries return the data that the migration job has committed so far. Writes, file compaction, and unreferenced file removal are disabled until you complete the migration. Snapshot management remains enabled and uses the snapshot management settings that you specify when you start the migration. Throughout the process, you retain control of the source and destination tables, including the ability to delete them or revoke permissions, though doing so can cause the migration job to fail.

## How data is migrated
<a name="s3-tables-migrate-how-data"></a>

Each start and sync moves through two states: planning and migrating. `GetTableMigration` reports the current state, such as `planning`, `migrating`, or `succeeded`. To check the current state, call `GetTableMigration`. For a description of every state, see [Migration states](s3-tables-migrate-running.md#s3-tables-migrate-states).
+ **Planning state**: The migration job validates your request and identifies every source object in the source table. The outputs of the planning state are a table compatibility report and an object compatibility report, which list any issues that were detected. For more information, see [Migration reports](s3-tables-migrate-reports.md#s3-tables-migrate-reports-overview). You have the option to review the reports before any data is migrated. To review the reports before any data is copied, set `reviewMigrationPlan` to `true` when you start or sync. The migration then waits in the `pendingReview` state until you approve or cancel it.
+ **Migrating state**: If `reviewMigrationPlan` is `false` or once you've approved the migration plan, the migration moves to the migrating state. In this state, the migration job reads each planned object, applies your migration policy, converts data types, recompresses and compacts the data, and commits it to the destination table. Each commit adds an Iceberg snapshot. At the end of the migrating state, the migration job writes an object migration report.

## Migration policy
<a name="s3-tables-migrate-migration-policies"></a>

The migration policy determines how migration handles differences between your source data and the destination and governs data conversion rules. You set this in `dataMigration.migrationPolicies` when you call `StartTableMigration`, and subsequent sync operations use the same policy. The migration policy has two settings that control how migration handles mismatches, and cannot be changed once set. Both default to `fail`.
+ `unmatchedSourceFieldsPolicy` controls source columns that aren't in the destination schema. Set it to `fail` (default) to fail the source object (the data file holding the unmatched column), which fails the migration, or `drop` to leave out the column.
+ `incompatibleValuesPolicy` controls optional (or nullable) columns that can't be converted to their destination data type. Set it to `fail` (default) to fail the migration job, or `setNull` to write the destination column as null instead.


| `unmatchedSourceFieldsPolicy` | `incompatibleValuesPolicy` | Source column that isn't in the destination | Incompatible column or value | 
| --- | --- | --- | --- | 
| fail (default) | fail (default) | Fails | Fails | 
| fail | setNull | Fails | Written as null | 
| drop | fail | Dropped (not migrated) | Fails | 
| drop | setNull | Dropped (not migrated) | Written as null | 

A source column is required only if the destination schema marks the matching destination column as required. To specify a schema, see [Setting up table migration](s3-tables-migrate-setting-up.md).

The object migration report lists the objects that failed and the columns that were dropped or written as null. If any object fails, the migration job ends in the `failed` state. Failed jobs will not migrate all the data in the source table. For more information, see [Troubleshooting](s3-tables-migrate-running.md#s3-tables-migrate-troubleshooting).

### Migration policy example
<a name="s3-tables-migrate-policies-example"></a>

Your AWS Glue table `orders` has the columns `order_id` (`bigint`) and `quantity` (`int`), and you let migration infer the schema.


**Orders Tables**  

| Column | AWS Glue data type | 
| --- | --- | 
| order\_id | bigint | 
| quantity | int | 

`file-a.parquet` has an extra column, `audit`. `file-b.parquet` stores `quantity` as `bigint`, which is incompatible with `int`. The mismatch is handled as follows based on your migration policy.


| `unmatchedSourceFieldsPolicy` | `incompatibleValuesPolicy` | `file-a.parquet` (extra column) | `file-b.parquet` (`bigint` in an `int` column) | 
| --- | --- | --- | --- | 
| fail | fail | Fails | Fails | 
| fail | setNull | Fails | Migrates, with quantity written as null for this object | 
| drop | fail | Migrates without the audit column | Fails | 
| drop | setNull | Migrates without the audit column | Migrates, with quantity written as null for this object | 

## Partitioning
<a name="s3-tables-migrate-partitioning"></a>

Migration keeps your source table's partitioning. The migration job copies the objects under each partition location that's registered in AWS Glue, including objects in subdirectories. For an unpartitioned table, migration copies the objects directly under the table location. For partition requirements and limits, see [Considerations and limitations](s3-tables-migrate-setting-up.md#s3-tables-migrate-considerations).