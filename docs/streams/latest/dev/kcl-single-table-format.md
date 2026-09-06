

# Single table format for KCL
<a name="kcl-single-table-format"></a>

Starting with KCL 3.5, you can consolidate all DynamoDB metadata into a single lease table using the **single table format**. By default, KCL 3.x creates three DynamoDB tables for each application: the lease table, the worker metrics table, and the coordinator state table. The single table format reduces these three tables to one, which helps you avoid DynamoDB account-level table limits.

## How single table format works
<a name="kcl-single-table-how-it-works"></a>

In single table format, KCL stores worker metrics and coordinator state entries in the lease table alongside lease entries. Each item includes an `entityType` attribute that distinguishes between the different record types.

Worker metrics and coordinator state items use the same primary key structure as the lease table but include a distinct `entityType` value. This attribute allows KCL to identify each item's purpose during table scans.

Each component of KCL filters out the entries it requires for its business logic based on the `entityType` attribute. For example, the Lease Assignment Manager (LAM) filters for lease and worker metrics entries to perform lease assignment.

## Configure single table format
<a name="kcl-single-table-config"></a>

How you enable single table format depends on your current KCL version:
+ **If you are on KCL 2.x:** Follow the updated migration guide to upgrade to KCL 3.5. Single table format is used by default for new migrations from 2.x to 3.5.
+ **If you are on KCL 3.0–3.4:** You must perform a two-phase deployment to migrate to single table format. See the following configuration and migration steps.

For existing KCL 3.x customers, set the `migrateAllEntitiesToLeaseTable` configuration option in `CoordinatorConfig`. This option controls whether KCL stores all metadata entity types in the lease table.


**Configuration values for `migrateAllEntitiesToLeaseTable`**  

| Value | Default | Effect | 
| --- | --- | --- | 
| false | Yes | KCL uses separate tables for worker metrics and coordinator state. The application code supports single table format but does not activate it. | 
| true | No | KCL begins writing worker metrics and coordinator state data into the lease table. Set this value on the Phase 2 deployment after the `TableMigrationStatus` reaches `DEPLOYED` and you have baked for no regressions. | 

Migrating from KCL 3.x to single table format requires a two-phase deployment:

1. **Phase 1:** Deploy the updated KCL 3.5 code with `migrateAllEntitiesToLeaseTable` set to `false` (the default). This installs the new code that supports single table format but does not activate the migration.

1. **Phase 2:** After all workers run the new code and the `TableMigrationStatus` reaches `DEPLOYED`, and you have verified that there are no regressions, deploy again with `migrateAllEntitiesToLeaseTable` set to `true` to begin the migration.

## Migration states
<a name="kcl-single-table-states"></a>

The `TableMigrationStateMachine` manages the transition from multi-table format to single table format. KCL tracks the current migration state in a separate coordinator state entry called `TableMigration3.5` in the coordinator state table. For the complete list of states, transitions, and descriptions, see [KCL single table migration states](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/src/main/java/software/amazon/kinesis/coordinator/migration/TableMigrationStatus.java).


**Single table format migration states**  

| State | Description | Transition condition | 
| --- | --- | --- | 
| INIT | Initial state. All workers are emitting the minimum support code in worker metric stats. Workers continue to emit worker metrics into the legacy table and read worker metrics and coordinator state from both the legacy and lease tables. Functionally, there is no difference between INIT and DEPLOYED. | All workers emit the minimum support code steadily for the bake time. The application is ready to move to Phase 2 deployment. | 
| DEPLOYED | All workers have been deployed with the new code (Phase 1 complete). The application supports single table format but has not activated it. | Phase 2 deployment begins with `migrateAllEntitiesToLeaseTable` set to `true`. | 
| PENDING | All workers run the new code. KCL migrates data from the worker metrics and coordinator state tables into the lease table. | A 24-hour default bake time elapses after migration completes. | 
| COMPLETE | Migration is complete. KCL uses the lease table exclusively for all reads and writes. The old worker metrics and coordinator state tables are no longer used. | Terminal state. No further transitions occur. | 

For detailed information about each state, transition conditions, and the complete state machine behavior, see [KCL single table migration state machine](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/src/main/java/software/amazon/kinesis/coordinator/migration/TableMigrationStatus.java).

**Note**  
The default bake time between the PENDING and COMPLETE states is 24 hours, but you can configure it up to one week. During this period, KCL uses the lease table for all reads and writes but does not delete the old tables. You must manually delete the old worker metrics and coordinator state tables after you confirm the migration is successful. KCL does not delete these tables automatically.

## Migration metrics
<a name="kcl-single-table-metrics"></a>

With KCL, you can monitor the progress and health of the single table migration using CloudWatch metrics. Use these metrics to confirm that workers have adopted the new code and to track the migration as it moves through its states. You can also detect DynamoDB read, write, or delete faults during the migration. The following tables group the metrics by the KCL operation (metric dimension) that emits them and by when each metric is emitted.

The elected leader worker continuously emits the following metrics, regardless of whether a migration is in progress:


**Metrics emitted by the leader at all times**  

| Operation | Metric | Unit | Description | 
| --- | --- | --- | --- | 
| `TableMigration` | `StatusOrdinal` | None | Ordinal of the current DynamoDB migration status: `0` = UNKNOWN, `1` = INIT, `2` = DEPLOYED, `3` = PENDING, `4` = COMPLETE. | 
| `WorkerMetrics` | `FleetMinSupportCode` | None | Minimum support code across all lease-owning workers in the fleet. | 

The elected leader worker emits the following metrics only while a migration is in progress:


**Metrics emitted by the leader during migration**  

| Operation | Metric | Unit | Description | 
| --- | --- | --- | --- | 
| `TableMigration` | `Phase1Worker` | Count | Number of workers that support operating with a single DynamoDB table but have not yet migrated to using the single table. | 
| `TableMigration` | `Phase2Worker` | Count | Number of workers that have migrated to writing to the single table. These workers might still read from multiple tables until the table migration completes. | 
| `TableMigration` | `PrePhase1Worker` | Count | Number of workers on a version prior to 3.5 that cannot support operating on a single DynamoDB table. | 
| `TableMigration` | `WriteFault` | Count | `1` on a DynamoDB write failure, `0` on success. | 
| `TableMigration` | `DeleteFault` | Count | `1` on a DynamoDB delete failure, `0` on success. | 
| `TableMigration` | `CompletionFault` | Count | `1` when the transactional write of the `COMPLETE` status fails, `0` on success. | 
| `TableMigrationAsyncMove` | `Success` | Count | `1` on a successful transactional move of CoordinatorState entries, `0` on failure. | 
| `TableMigrationAsyncMove` | `Time` | Milliseconds | Duration of the async move operation. | 
| `TableMigrationAsyncMove` | `BatchCount` | Count | Number of batches that were successfully moved. | 

All workers emit the following metrics while a migration is in progress:


**Metrics emitted by all workers during migration**  

| Operation | Metric | Unit | Description | 
| --- | --- | --- | --- | 
| `TableMigration` | `ReadFault` | Count | `1` on failure to read the `TableMigrationState` from DynamoDB, `0` on success. | 
| `TableMigration` | `Time` | Milliseconds | Duration of the state machine run. | 
| `TableMigrationInitialize` | `Success` | Count | `1` on a successful initialize, `0` on failure. | 
| `TableMigrationInitialize` | `Time` | Milliseconds | Duration of the initialize operation. | 

Use these metrics to decide when to advance the migration. When `StatusOrdinal` is consistently `2` (DEPLOYED) and `PrePhase1Worker` is `0`, all workers support the single table format, and you can move to phase 2 of the table migration deployment. After `StatusOrdinal` reaches `4` (COMPLETE), you can safely delete the legacy tables.

## Rollback considerations
<a name="kcl-single-table-rollback"></a>

Rollback support depends on the current `TableMigrationStatus`:
+ **During Phase 1** (`TableMigrationStatus` is `DEPLOYED` or not yet set): You can safely roll back to the previous version. The new code runs in a backward-compatible mode and no data has been written to non-lease entries in the lease table.
+ **During Phase 2** (`TableMigrationStatus` is `DEPLOYED` or `PENDING`): You can roll back to Phase 1. Workers revert to using the legacy tables (multi-table format) for worker metrics and coordinator state. The migration is undone.
+ **After COMPLETE state**: Rollback is not supported. KCL only uses the lease table for all entities. Even if the code rolls back to Phase 1, the worker continues using the lease table for all entities and the configuration is ignored.

**Warning**  
After the migration reaches the COMPLETE state, the application operates exclusively in single table mode. The `migrateAllEntitiesToLeaseTable` configuration is ignored, and KCL does not revert to using separate tables. Make sure the bake time before moving to COMPLETE is sufficient, because after that even a code rollback does not switch back to multiple tables.

## Best practices
<a name="kcl-single-table-best-practices"></a>

Follow these best practices when you adopt single table format:
+ After Phase 1 deployment, verify that the coordinator state entry `TableMigration3.5` reaches `DEPLOYED` status. Ensure there are no regressions before proceeding to Phase 2.
+ Monitor the `TableMigrationStatus` in the `TableMigration3.5` coordinator state entry to track progress through the DEPLOYED, PENDING, and COMPLETE states. The status is stored in the coordinator state table as a separate entry (not in the lease table) until the migration reaches COMPLETE.
+ Make sure the bake time before moving to COMPLETE is sufficient, because after that even a code rollback does not switch back to multiple tables. The application functions only in single table mode.
+ After the migration reaches COMPLETE, manually delete the old worker metrics and coordinator state tables. KCL does not delete these tables automatically—it only stops using them.
+ If you have configured `CoordinatorConfig.coordinatorStateTableConfig` or `LeaseManagementConfig.workerUtilizationAwareAssignmentConfig.workerMetricsTableConfig`, you can remove these configurations after migration completes. These configurations are deprecated in KCL 3.5 and later.