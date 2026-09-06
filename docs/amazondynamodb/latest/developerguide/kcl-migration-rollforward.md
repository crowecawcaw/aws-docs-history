

# Roll forward to Phase 2 KCL 3.5.x\+ after a rollback
<a name="kcl-migration-rollforward"></a>

This topic explains how to roll forward your consumer application to KCL 3.5.x\+ after a rollback. When you need to roll forward, you must complete a two-step process:

1. Run the [KCL Migration Tool](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py) on the GitHub website.

1. Deploy the Phase 2 code.

## Step 1: Run the KCL Migration Tool
<a name="kcl-migration-rollforward-step1"></a>

Run the KCL Migration Tool with the following command to roll forward to KCL 3.5.x\+:

```
python3 ./KclMigrationTool.py --region {{region}} --mode rollforward [--application_name {{applicationName}}] [--lease_table_name {{leaseTableName}}]
```

### Parameters
<a name="kcl-migration-rollforward-parameters"></a>

`--region`  
Replace {{region}} with your AWS Region.

`--application_name`  
This parameter is required if you're using the default name for your lease table. If you have specified a custom name for the lease table, you can omit this parameter. Replace {{applicationName}} with your actual KCL application name. The tool uses this name to derive the default table name if a custom name is not provided.

`--lease_table_name`  
This parameter is needed when you have set a custom name for the lease table in your KCL configuration. If you're using the default table name, you can omit this parameter. Replace {{leaseTableName}} with the custom table name you specified for your lease table.

After you run the migration tool in roll-forward mode, KCL creates the following DynamoDB resource required for KCL 3.5.x\+:
+ A Global Secondary Index on the lease table

**Note**  
KCL 3.5.x\+ does not create separate worker metrics or coordinator state tables during migration. All metadata is stored in the lease table.

## Step 2: Deploy the code with Phase 2 configuration
<a name="kcl-migration-rollforward-step2"></a>

After running the KCL Migration Tool for a roll forward, deploy your code with KCL 3.5.x\+ Phase 2 configuration (`CLIENT_VERSION_CONFIG_COMPATIBLE_WITH_2X`) to your workers. To complete your migration, see [Step 8: Complete the migration](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration-from-2-3.html#kcl-migration-from-2-3-finish).