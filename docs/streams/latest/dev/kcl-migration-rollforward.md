# Roll forward to KCL 3.x after a

rollback

This topic explains the steps to roll forward your consumer back to KCL 3.x
after a rollback. When you need to roll forward, you must go through a two-step process:

1. Run the [KCL Migration Tool](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py "https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py").
2. Deploy the code with KCL 3.x.

## Step 1: Run the KCL Migration

Tool

Run the KCL Migration Tool. KCL Migration Tool with the
following command to roll forward to KCL 3.x:

```
python3 ./KclMigrationTool.py --region <region> --mode rollforward [--application_name <applicationName>] [--coordinator_state_table_name <coordinatorStateTableName>]
```

**Parameters**

- --region: Replace `<region>` with your AWS Region.
- --application_name: This parameter is required if you're using default
  names for your coordinator state table. If you have specified custom names
  for the coordinator state table, you can omit this parameter. Replace
  `<applicationName>` with your actual KCL
  application name. The tool uses this name to derive the default table names
  if custom names are not provided.
- --coordinator_state_table_name (optional): This parameter is needed when
  you have set a custom name for the coordinator state table in your
  KCL configuration. If you're using the default table name, you can
  omit this parameter. Replace `<coordinatorStateTableName>`
  with the custom table name you specified for your coordinator state table.

After you run the migration tool in roll-forward mode, KCL creates the
following DynamoDB resources required for KCL 3.x:

- A Global Secondary Index on the lease table
- A worker metrics table

## Step 2: Deploy the code with

KCL 3.x

After running the KCL Migration Tool for a roll forward, deploy your code
with KCL 3.x to your workers. Follow [Step 8: Complete the
migration](kcl-migration-from-2-3.md#kcl-migration-from-2-3-finish "kcl-migration-from-2-3.md#kcl-migration-from-2-3-finish")
to complete your migration.
