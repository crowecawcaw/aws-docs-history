# Roll forward to Phase 2 KCL 3.5.x+ after a rollback

This topic explains how to roll forward your consumer application to KCL 3.5.x+
after a rollback. When you need to roll forward, you must complete a two-step process:

1. Run the [KCL Migration Tool](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py "https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py") on the GitHub website.
2. Deploy the Phase 2 code.

## Step 1: Run the KCL Migration Tool

Run the KCL Migration Tool with the following command to roll forward to
KCL 3.5.x+:

```
python3 ./KclMigrationTool.py --region `region` --mode rollforward [--application_name `applicationName`] [--lease_table_name `leaseTableName`]
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

After you run the migration tool in roll-forward mode, KCL creates the
following DynamoDB resource required for KCL 3.5.x+:

- A Global Secondary Index on the lease table

###### Note

KCL 3.5.x+ does not create separate worker metrics or coordinator
state tables during migration. All metadata is stored in the lease table.

## Step 2: Deploy the code with Phase 2 configuration

After running the KCL Migration Tool for a roll forward, deploy your code
with KCL 3.5.x+ Phase 2 configuration
(`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X`) to your workers. To complete your migration, see [Step 8: Complete the migration](../../../streams/latest/dev/kcl-migration-from-2-3.md#kcl-migration-from-2-3-finish "../../../streams/latest/dev/kcl-migration-from-2-3.md#kcl-migration-from-2-3-finish").
