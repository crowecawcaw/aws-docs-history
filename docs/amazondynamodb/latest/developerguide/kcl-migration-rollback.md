# Roll back to the previous KCL version

This topic explains how to roll back your KCL 3.5.x+ consumer application to
KCL 1.x. The rollback process depends on which migration phase your application
is currently in.

## Roll back from Phase 1 to KCL 1.x

If your application is in Phase 1
(`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X_PHASE1`), you can roll back
to KCL 1.x by redeploying your previous code. Phase 1 is
backward compatible with KCL 1.x and does not create any
migration-specific entries in the lease table. No migration tool is needed. To roll back
from Phase 1, redeploy the code with your KCL 1.x version to all workers.

###### Important

Phase 2 (`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X`) is a breaking change
for rollback. Once your application enters Phase 2, non-lease entries
(`WORKER_METRIC_STATS` and `Migration3.0`) are written to the lease
table that are not backward compatible with KCL 1.x. This permanently prevents a direct
rollback to KCL 1.x. We strongly recommend baking your application in Phase 1 for
an extended period to validate stability before proceeding to Phase 2.

## Roll back from Phase 2 to Phase 1

If your application is in Phase 2
(`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X`), you must use the
[KCL Migration Tool](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py "https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py") on the GitHub website to roll back to Phase 1
(`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X_PHASE1`). This is a two-step
process:

1. Run the [KCL Migration Tool](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py "https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py") on the GitHub website.
2. Redeploy the code with Phase 1 configuration (optional).

###### Important

You cannot roll back two levels (from Phase 2 to Phase 1 and then to
KCL 1.x). The KCL Migration Tool only handles
the Phase 2 to Phase 1 rollback. The tool does not delete non-lease entries from the
lease table. These entries are not backward compatible with KCL 1.x,
which is why a two-level rollback from Phase 2 directly to KCL 1.x is not
possible.

## Step 1: Run the KCL Migration Tool

When you need to roll back from Phase 2
(`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X`) to Phase 1
(`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X_PHASE1`), run the
KCL Migration Tool. The tool performs the following tasks:

- It removes the Global Secondary Index (LeaseOwnerToLeaseKeyIndex) on the
  lease table in DynamoDB. This index is created by KCL 3.5.x+ but is
  not needed when you roll back to Phase 1.
- It makes all workers run in a mode compatible with KCL 1.x and
  start using the load balancing algorithm used in previous KCL
  versions. If you have issues with the new load balancing algorithm in
  KCL 3.5.x+, this mitigates the issue immediately.

###### Important

The coordinator state entry (`Migration3.0`) in the lease table
must not be deleted during the migration, rollback, and rollforward process.

###### Note

All workers in your consumer application must use the same load balancing
algorithm at a given time. The KCL Migration Tool makes sure that all
workers in your KCL 3.5.x+ consumer application switch to the
KCL 1.x compatible mode so that all workers run the same load balancing
algorithm during the rolling deployment back to Phase 1.

You can download the [KCL Migration Tool](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py "https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py") in the scripts directory of the [KCL GitHub
repository](https://github.com/awslabs/amazon-kinesis-client/tree/master "https://github.com/awslabs/amazon-kinesis-client/tree/master"). Run the script from any of your workers or any host that has
the required permissions to write to and update the lease table. Ensure the
appropriate [IAM
permissions](../../../streams/latest/dev/kcl-iam-permissions.md "../../../streams/latest/dev/kcl-iam-permissions.md") are configured for KCL consumer applications. You must run the script only once per
KCL application. Run the KCL Migration Tool with the following
command:

```
python3 ./KclMigrationTool.py --region `region` --mode rollback [--application_name `applicationName`] [--lease_table_name `leaseTableName`]
```

### Parameters

`--region`

Replace `region` with your AWS Region.

`--application_name`

This parameter is required if you're using the default
name for your lease table. If you have specified a custom name for the lease
table, you can omit this parameter. Replace
`applicationName` with your actual KCL application name.
The tool uses this name to derive the default table name
if a custom name is not provided.

`--lease_table_name`

This parameter is needed when you have set a custom name for the lease table in your KCL configuration. If you're using the default table name, you can omit this parameter. Replace `leaseTableName` with the custom table name you specified for your lease table.

## Step 2: Redeploy the code with Phase 1 configuration (optional)

After running the KCL Migration Tool for a rollback from Phase 2 to
Phase 1, you'll see one of these messages:

Message 1

"Rollback completed. Your application was running Phase 2 (2x compatible) functionality. Please
rollback to Phase 1 by deploying your KCL 3.5.x application with the
Phase 1 configuration."

**Required action:** Your workers
were running in KCL 1.x compatible mode (Phase 2 had not yet auto-transitioned to
full 3.x load balancing). Redeploy your
KCL 3.5.x+ application with Phase 1 configuration
(`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X_PHASE1`) to
your workers.

Message 2

"Rollback completed. Your KCL application was running Phase 2 (3x) functionality and has been rolled
back to Phase 2 (2x compatible) mode. If you don't see mitigation after a
short period of time, please rollback to Phase 1 by deploying your KCL
3.5.x application with the Phase 1 configuration."

**Required action:** Your workers
had auto-transitioned to full KCL 3.x load balancing and the KCL Migration
Tool switched them back to KCL 1.x compatible mode.
If the issue is resolved, you don't need to redeploy. If the issue persists,
redeploy your KCL 3.5.x+ application with Phase 1
configuration
(`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X_PHASE1`) to
your workers.
