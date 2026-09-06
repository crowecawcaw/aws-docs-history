

# Migrate from KCL 3.x to single table format
<a name="kcl-migration-from-3-3-5"></a>

If you run KCL 3.x with all three DynamoDB metadata tables (lease table, worker metrics table, and coordinator state table), you can migrate to single table format to consolidate all metadata into the lease table.

**Prerequisites**
+ Your application runs KCL 3.x with all three metadata tables.
+ Your application is stable and all workers are healthy.
+ Your application has finished the KCL 3.x migration and does not configure `CoordinatorConfig.clientVersionConfig`. Do not perform the table migration and the client version migration from 2.x to 3.x at the same time.

**To migrate from KCL 3.x to single table format, follow the two-phase deployment process**  


1. **Phase 1:** Update your project dependency to KCL 3.5 or later. Deploy with `migrateAllEntitiesToLeaseTable` set to `false` (the default). This deployment installs the new code that supports single table format but does not activate the migration.

1. Wait for the deployment to complete on all workers. Monitor the `TableMigration3.5` coordinator state entry until the `TableMigrationStatus` reaches `DEPLOYED`. Verify that there are no regressions and allow sufficient bake time.

1. **Phase 2:** Deploy again with `migrateAllEntitiesToLeaseTable` set to `true`. This deployment begins the migration to single table format.

1. Monitor the `TableMigrationStatus`. The leader worker advances the state through DEPLOYED, PENDING, and COMPLETE.

1. After the status reaches COMPLETE, verify that there are no regressions and allow additional bake time to make sure no rollbacks are necessary.

1. Manually delete the old worker metrics and coordinator state tables. KCL does not delete these tables automatically—it only stops using them. If you have configured `CoordinatorConfig.coordinatorStateTableConfig` or `LeaseManagementConfig.workerUtilizationAwareAssignmentConfig.workerMetricsTableConfig`, you can remove these configurations as they are deprecated.

**Important**  
Do not roll back your application after the migration reaches the COMPLETE state. After COMPLETE, the application operates exclusively in single table mode. Even a code rollback to Phase 1 does not switch back to multiple tables— the configuration is ignored and the application continues using only the lease table.

For details on migration states and rollback options, see [Single table format for KCL](kcl-single-table-format.md).