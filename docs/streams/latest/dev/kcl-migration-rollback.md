

# Roll back to the previous KCL version
<a name="kcl-migration-rollback"></a>

This topic explains the steps to roll back your KCL 3.5.x consumer to the previous version. The rollback process depends on which migration phase your application is currently in.

**Important**  
The KCL Migration Tool is required when rolling back from Phase 2 (`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X`) to Phase 1 (`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X_PHASE1`). The tool is also required to roll back from Phase 1 to your previous KCL version (KCL 2.x). This applies when your lease table still contains migration-specific entries from an earlier Phase 2 deployment. If your application entered Phase 1 directly and has not started Phase 2, you can roll back to your previous KCL version by redeploying your previous code without running the tool.

## Roll back from Phase 1 to the previous KCL version
<a name="kcl-migration-rollback-phase1"></a>

If your application entered Phase 1 (`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X_PHASE1`) directly as part of a migration from KCL 2.x and has not yet started Phase 2, you can roll back to your previous KCL version by redeploying your previous code. Phase 1 is backward compatible with previous KCL versions and does not create any migration-specific entries in the lease table. No migration tool is needed.

To roll back from Phase 1:

1. Redeploy the code with your previous KCL version to all workers.

**Note**  
You cannot roll back directly from Phase 2 to your previous KCL version (KCL 2.x). You must roll back in sequence:  
Roll back from Phase 2 to Phase 1 (run the tool, then redeploy the Phase 1 code). See [Roll back from Phase 2 to Phase 1](#kcl-migration-rollback-phase2).
Roll back from Phase 1 to KCL 2.x (run the tool, then redeploy your previous code). See [Roll back from Phase 1 to KCL 2.x](#kcl-migration-rollback-to-v2).
You might redeploy the Phase 1 code for either of two reasons: to continue rolling back to KCL 2.x, or because running the tool alone did not mitigate the issue and you want to fully return to Phase 1.

## Roll back from Phase 2 to Phase 1
<a name="kcl-migration-rollback-phase2"></a>

If your application is in Phase 2 (`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X`), you must use the KCL Migration Tool to roll back to Phase 1. This is a two-step process:

1. Run the [KCL Migration Tool](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py).

1. Redeploy the code with Phase 1 configuration (optional).

**Note**  
The KCL Migration Tool handles only the Phase 2 to Phase 1 rollback. To reach your previous KCL version (KCL 2.x) from Phase 2, first roll back to Phase 1 using the steps in this section, and then follow [Roll back from Phase 1 to KCL 2.x](#kcl-migration-rollback-to-v2) to run the tool in `rollback-to-v2` mode and delete the non-lease entries before you redeploy your previous code.

## Step 1: Run the KCL Migration Tool
<a name="kcl-migration-rollback-tool"></a>

When you need to roll back from Phase 2 (`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X`) to Phase 1, run the KCL Migration Tool. The tool performs the following tasks:
+ It removes the Global Secondary Index (LeaseOwnerToLeaseKeyIndex) on the lease table in DynamoDB. This index is created by KCL 3.5.x but is not needed when you roll back to Phase 1.
+ It makes all workers run in a mode compatible with KCL 2.x and start using the load balancing algorithm used in previous KCL versions. If you have issues with the new load balancing algorithm in KCL 3.5.x, this mitigates the issue immediately.

**Important**  
The coordinator state entry (`Migration3.0`) in the lease table must not be deleted during the migration, rollback, and rollforward process.

**Note**  
All workers in your consumer application must use the same load balancing algorithm at a given time. The KCL Migration Tool makes sure that all workers in your KCL 3.5.x consumer application switch to the KCL 2.x compatible mode so that all workers run the same load balancing algorithm during the rolling deployment back to Phase 1.

You can download the [KCL Migration Tool](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py) in the scripts directory of the [KCL GitHub repository](https://github.com/awslabs/amazon-kinesis-client/tree/master). Run the script from any of your workers or any host that has the required permissions to write to and update the lease table. You can refer to [IAM permissions required for KCL consumer applications](kcl-iam-permissions.md) for required IAM permissions to run the script. You must run the script only once per KCL application. Run the KCL Migration Tool with the following command:

```
python3 ./KclMigrationTool.py --region <region> --mode rollback-to-phase1 [--application_name <applicationName>] [--lease_table_name <leaseTableName>]
```

**Parameters**
+ --region: Replace `<region>` with your AWS Region.
+ --application\_name: This parameter is required if you're using the default name for your lease table. If you have specified a custom name for the lease table, you can omit this parameter. Replace `<applicationName>` with your actual KCL application name. The tool uses this name to derive the default table name if a custom name is not provided.
+ --lease\_table\_name (optional): This parameter is needed when you have set a custom name for the lease table in your KCL configuration. If you're using the default table name, you can omit this parameter. Replace `<leaseTableName>` with the custom table name you specified for your lease table.

## Step 2: Redeploy the code with Phase 1 configuration (optional)
<a name="kcl-migration-rollback-redeploy"></a>

After running the KCL Migration Tool for a rollback from Phase 2 to Phase 1, you'll see one of these messages:

**Note**  
Redeploying the Phase 1 configuration is optional if you rolled back to mitigate an issue and intend to stay on KCL 3.5.x (you can later roll forward to Phase 2 without redeploying). It is required if you intend to continue rolling back to KCL 2.x, because the `rollback-to-v2` step requires all workers to be running the Phase 1 configuration first.
+ **Message 1:** "Rollback completed. Your application was running Phase 2 (2x compatible) functionality. Please rollback to Phase 1 by deploying your KCL 3.5.x application with the Phase 1 configuration."
  + **Required action: **Your workers were running in Phase 2 (2x compatible) mode. Redeploy your KCL 3.5.x application with Phase 1 configuration (`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X_PHASE1`) to your workers.
+ **Message 2: **"Rollback completed. Your KCL application was running Phase 2 (3x) functionality and has been rolled back to Phase 2 (2x compatible) mode. If you don't see mitigation after a short period of time, please rollback to Phase 1 by deploying your KCL 3.5.x application with the Phase 1 configuration."
  + **Required action: **Your workers were running in Phase 2 (3x) mode and the KCL Migration Tool rolled them back to Phase 2 (2x compatible) mode. If the issue is resolved, you don't need to redeploy. If the issue persists, redeploy your KCL 3.5.x application with Phase 1 configuration (`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X_PHASE1`) to your workers.

## Roll back from Phase 1 to KCL 2.x
<a name="kcl-migration-rollback-to-v2"></a>

This section describes how to roll back from Phase 1 to your previous KCL version (KCL 2.x) when your application has been in Phase 2. This is the second step of the sequence described in [Roll back from Phase 1 to the previous KCL version](#kcl-migration-rollback-phase1): first roll back from Phase 2 to Phase 1, and then complete the steps in this section. After all workers are running Phase 1, run the KCL Migration Tool in `rollback-to-v2` mode to clean up the non-lease entries, and then redeploy your previous code.

**Important**  
Rolling back to your previous code without this step will stall the application, because the previous code cannot handle the non-lease entries in the lease table.

**Important**  
Before you run the tool in `rollback-to-v2` mode, confirm that the Phase 2 to Phase 1 rollback is complete: all workers in your fleet have finished the Phase 1 code rollback deployment with `CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X_PHASE1` and no Phase 2 workers remain. The tool proceeds only when `MigrationState.ClientVersion` is already `CLIENT_VERSION_2X`, which indicates that the Phase 2 to Phase 1 rollback has run. Verify this using your CI/CD system.

To roll back from Phase 1 to your previous KCL version (KCL 2.x):

1. Run the [KCL Migration Tool](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py) in `rollback-to-v2` mode. You can run the script from any of your workers or any host that has the required permissions to write to and update the lease table. Because this mode deletes the non-lease entries from the lease table, the host must have delete permissions (`DeleteItem`) on the lease table. For the required IAM permissions, see [IAM permissions required for KCL consumer applications](kcl-iam-permissions.md).

   ```
   python3 ./KclMigrationTool.py --region <region> --mode rollback-to-v2 [--application_name <applicationName>] [--lease_table_name <leaseTableName>]
   ```

   **Parameters**
   + --region: Replace `<region>` with your AWS Region.
   + --application\_name: This parameter is required if you're using the default name for your lease table. If you have specified a custom name for the lease table, you can omit this parameter. Replace `<applicationName>` with your actual KCL application name. The tool uses this name to derive the default table name if a custom name is not provided.
   + (Optional) --lease\_table\_name: Use this parameter when you have set a custom name for the lease table in your KCL configuration. If you're using the default table name, you can omit this parameter. Replace `<leaseTableName>` with the custom table name you specified for your lease table.

1. The tool scans the lease table for non-lease entities and lists the entries that it will delete from the lease table, such as the client version migration entry (`Migration3.0`) and worker metric statistics entries. Review the listed entries.

1. When the tool prompts you, type the following confirmation string exactly to acknowledge that the Phase 1 code rollback is complete:

   ```
   Code rollback to CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X_PHASE1 completed
   ```

1. When the tool prompts you to confirm the deletion, type `yes`. The tool permanently deletes the listed non-lease entities from the lease table.

1. After the tool reports that the lease table is clean for the KCL 2.x rollback, redeploy the code with your previous KCL version (KCL 2.x) to all workers.

**Important**  
After the tool deletes the non-lease entities, a later roll forward to Phase 2 requires a fresh migration from Phase 1. When you're ready to migrate to KCL 3.5.x again, deploy with the Phase 1 configuration (`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X_PHASE1`), allow the Phase 1 deployment to bake for your confidence interval, and then deploy with the Phase 2 configuration (`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X`). No tool is needed for either of these deployments.