

# Roll back to the previous KCL version
<a name="kcl-migration-rollback"></a>

This topic explains the steps to roll back your KCL 3.5.x consumer to the previous version. The rollback process depends on which migration phase your application is currently in.

**Important**  
The KCL Migration Tool is only required when rolling back from Phase 2 (`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X`) to Phase 1 (`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X_PHASE1`). If your application is still in Phase 1, you can roll back to your previous KCL version by redeploying your previous code without running the tool.

## Roll back from Phase 1 to the previous KCL version
<a name="kcl-migration-rollback-phase1"></a>

If your application is in Phase 1 (`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X_PHASE1`), you can roll back to your previous KCL version by redeploying your previous code. Phase 1 is backward compatible with previous KCL versions and does not create any migration-specific entries in the lease table. No migration tool is needed.

To roll back from Phase 1:

1. Redeploy the code with your previous KCL version to all workers.

## Roll back from Phase 2 to Phase 1
<a name="kcl-migration-rollback-phase2"></a>

If your application is in Phase 2 (`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X`), you must use the KCL Migration Tool to roll back to Phase 1. This is a two-step process:

1. Run the [KCL Migration Tool](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py).

1. Redeploy the code with Phase 1 configuration (optional).

**Important**  
You cannot roll back two levels (from Phase 2 to Phase 1 and then to the previous KCL version). The KCL Migration Tool only handles the Phase 2 to Phase 1 rollback.

**Note**  
The KCL Migration Tool does not delete non-lease entries from the lease table. These entries are not backward compatible with previous KCL versions, which is why a two-level rollback from Phase 2 directly to a previous KCL version is not possible.

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
python3 ./KclMigrationTool.py --region <region> --mode rollback [--application_name <applicationName>] [--lease_table_name <leaseTableName>]
```

**Parameters**
+ --region: Replace `<region>` with your AWS Region.
+ --application\_name: This parameter is required if you're using the default name for your lease table. If you have specified a custom name for the lease table, you can omit this parameter. Replace `<applicationName>` with your actual KCL application name. The tool uses this name to derive the default table name if a custom name is not provided.
+ --lease\_table\_name (optional): This parameter is needed when you have set a custom name for the lease table in your KCL configuration. If you're using the default table name, you can omit this parameter. Replace `<leaseTableName>` with the custom table name you specified for your lease table.

## Step 2: Redeploy the code with Phase 1 configuration (optional)
<a name="kcl-migration-rollback-redeploy"></a>

After running the KCL Migration Tool for a rollback from Phase 2 to Phase 1, you'll see one of these messages:
+ **Message 1:** "Rollback completed. Your application was running Phase 2 (2x compatible) functionality. Please rollback to Phase 1 by deploying your KCL 3.5.x application with the Phase 1 configuration."
  + **Required action: **Your workers were running in Phase 2 (2x compatible) mode. Redeploy your KCL 3.5.x application with Phase 1 configuration (`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X_PHASE1`) to your workers.
+ **Message 2: **"Rollback completed. Your KCL application was running Phase 2 (3x) functionality and has been rolled back to Phase 2 (2x compatible) mode. If you don't see mitigation after a short period of time, please rollback to Phase 1 by deploying your KCL 3.5.x application with the Phase 1 configuration."
  + **Required action: **Your workers were running in Phase 2 (3x) mode and the KCL Migration Tool rolled them back to Phase 2 (2x compatible) mode. If the issue is resolved, you don't need to redeploy. If the issue persists, redeploy your KCL 3.5.x application with Phase 1 configuration (`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X_PHASE1`) to your workers.