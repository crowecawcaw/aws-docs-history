# Roll back to the previous KCL

version

This topic explains the steps to roll back your consumer back to the previous version.
When you need to roll back, there is a two-step process:

1. Run the [KCL Migration Tool](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py "https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py").
2. Redeploy previous KCL version code (optional).

## Step 1: Run the KCL Migration

Tool

When you need to roll back to the previous KCL version, you must run the
KCL Migration Tool. The KCL Migration Tool does two important
tasks:

- It removes a metadata table called worker metrics table and global
  secondary index on the lease table in DynamoDB. These two artifacts are
  created by KCL 3.x but are not needed when you roll back to the
  previous version.
- It makes all workers run in a mode compatible with KCL 2.x and start using the load
  balancing algorithm used in previous KCL versions. If you have
  issues with the new load balancing algorithm in KCL 3.x, this will
  mitigate the issue immediately.

###### Important

The coordinator state table in DynamoDB must exist and must not be deleted during
the migration, rollback, and rollforward process.

###### Note

It's important that all workers in your consumer application use the same load
balancing algorithm at a given time. The KCL Migration Tool makes sure
that all workers in your KCL 3.x consumer application switch to the
KCL 2.x compatible mode so that all workers run the same load balancing
algorithm during the rolling depayment back to your previous KCL
version.

You can download the [KCL Migration Tool](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py "https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py") in the scripts directory of the [KCL GitHub
repository](https://github.com/awslabs/amazon-kinesis-client/tree/master "https://github.com/awslabs/amazon-kinesis-client/tree/master"). The script can be run from any of your workers or any host
which has the required permissions to write to the coordinator state table, delete
the worker metrics table, and update the lease table. You can refer to [IAM permissions required for KCL
consumer applications](kcl-iam-permissions.md "kcl-iam-permissions.md") for required
IAM permission to run the script. You must run the script only once per
KCL application. You can run the KCL Migration Tool with the
following command:

```
python3 ./KclMigrationTool.py --region <region> --mode rollback [--application_name <applicationName>] [--lease_table_name <leaseTableName>] [--coordinator_state_table_name <coordinatorStateTableName>] [--worker_metrics_table_name <workerMetricsTableName>]
```

**Parameters**

- --region: Replace `<region>` with your AWS Region.
- --application_name: This parameter is required if you're using default
  names for your DynamoDB metadata tables (lease table, coordinator state table,
  and worker metrics table). If you have specified custom names for these
  tables, you can omit this parameter. Replace
  `<applicationName>` with your actual KCL
  application name. The tool uses this name to derive the default table names
  if custom names are not provided.
- --lease_table_name (optional): This parameter is needed when you have set
  a custom name for the lease table in your KCL configuration. If
  you're using the default table name, you can omit this parameter. Replace
  `leaseTableName` with the custom table name you specified for
  your lease table.
- --coordinator_state_table_name (optional): This parameter is needed when
  you have set a custom name for the coordinator state table in your
  KCL configuration. If you're using the default table name, you can
  omit this parameter. Replace `<coordinatorStateTableName>`
  with the custom table name you specified for your coordinator state table.
- --worker_metrics_table_name (optional): This parameter is needed when you
  have set a custom name for the worker metrics table in your KCL
  configuration. If you're using the default table name, you can omit this
  parameter. Replace `<workerMetricsTableName>` with the custom
  table name you specified for your worker metrics table.

## Step 2: Redeploy the code with the

previous KCL version (optional)

After running the KCL Migration Tool for a rollback, you'll see one of
these messages:

- **Message 1:** “Rollback completed. Your
  KCL application was running the KCL 2.x compatible mode.
  If you don't see mitigation of any regression, please rollback to your
  previous application binaries by deploying the code with your previous
  KCL version.”
  - **Required action:** This means that
    your workers were running in the KCL 2.x compatible mode.
    If the issue persists, redeploy the code with the previous
    KCL version to your workers.

- **Message 2:** “Rollback completed. Your
  KCL application was running the KCL 3.x functionality
  mode. Rollback to the previous application binaries is not necessary, unless
  you don’t see any mitigation for the issue within 5 minutes. If you still
  have an issue, please rollback to your previous application binaries by
  deploying the code with your previous KCL version.”
  - **Required action:** This means that
    your workers were running in KCL 3.x mode and the
    KCL Migration Tool switched all workers to KCL 2.x
    compatible mode. If the issue is resolved, you don't need to
    redeploy the code with the previous KCL version. If the
    issue persists, redeploy the code with the previous KCL
    version to your workers.
