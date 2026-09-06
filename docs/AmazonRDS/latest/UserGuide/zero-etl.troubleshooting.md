

# Troubleshooting Amazon RDS zero-ETL integrations
<a name="zero-etl.troubleshooting"></a>

You can check the state of a zero-ETL integration by querying the [SVV\_INTEGRATION](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_INTEGRATION.html) system table in the analytics destination. If the `state` column has a value of `ErrorState`, it means something's wrong. For more information, see [Monitoring integrations using system tables for Amazon Redshift](zero-etl.describingmonitoring.md#zero-etl.monitoring).

Use the following information to troubleshoot common issues with Amazon RDS zero-ETL integrations.

**Important**  
Resync and refresh operations are not available for zero-ETL integrations with an Amazon SageMaker AI lakehouse. If there are issues with an integration, you must delete the integration and create a new integration. You can't refresh or resync an existing integration.

**Topics**
+ [I can't create a zero-ETL integration](#zero-etl.troubleshooting.creation)
+ [My integration is stuck in a state of `Syncing`](#zero-etl.troubleshooting.syncing)
+ [My tables aren't replicating to Amazon Redshift](#zero-etl.troubleshooting.primarykey)
+ [One or more of my Amazon Redshift tables requires a resync](#zero-etl.troubleshooting.resync)
+ [Integration failed issues for Amazon SageMaker AI lakehouse zero-ETL integrations](#zero-etl.troubleshooting.integration-issues)

## I can't create a zero-ETL integration
<a name="zero-etl.troubleshooting.creation"></a>

If you can't create a zero-ETL integration, make sure that the following are correct for your source database:
+ Your source database must be running a supported DB engine version. For a list of supported versions, see [Supported Regions and DB engines for Amazon RDS zero-ETL integrations](Concepts.RDS_Fea_Regions_DB-eng.Feature.ZeroETL.md).
+  You correctly configured DB parameters. If the required parameters are set incorrectly or not associated with the database, creation fails. See [Step 1: Create a custom DB parameter group](zero-etl.setting-up.md#zero-etl.parameters).

In addition, make sure the following are correct for your target data warehouse:
+ Case sensitivity is enabled. See [Turn on case sensitivity for your data warehouse](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.setting-up.html#zero-etl-setting-up.case-sensitivity).
+ You added the correct authorized principal and integration source. See [Configure authorization for your Amazon Redshift data warehouse](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.setting-up.html#zero-etl-using.redshift-iam).
+ The data warehouse is encrypted (if it's a provisioned cluster). See [Amazon Redshift database encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html).

## My integration is stuck in a state of `Syncing`
<a name="zero-etl.troubleshooting.syncing"></a>

Your integration might consistently show a status of `Syncing` if you change the value of one of the required DB parameters.

To fix this issue, check the values of the parameters in the parameter group associated with the source database, and make sure that they match the required values. For more information, see [Step 1: Create a custom DB parameter group](zero-etl.setting-up.md#zero-etl.parameters).

If you modify any parameters, make sure to reboot the database to apply the changes.

## My tables aren't replicating to Amazon Redshift
<a name="zero-etl.troubleshooting.primarykey"></a>

If you don't see one or more tables reflected in Amazon Redshift, you can run the following command to resynchronize them:

```
ALTER DATABASE {{dbname}} INTEGRATION REFRESH TABLES {{table1}}, {{table2}};
```

For more information, see [ALTER DATABASE](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_DATABASE.html) in the Amazon Redshift SQL reference.

Your data might not be replicating because one or more of your source tables doesn't have a primary key. The monitoring dashboard in Amazon Redshift displays the status of these tables as `Failed`, and the status of the overall zero-ETL integration changes to `Needs attention`. To resolve this issue, you can identify an existing key in your table that can become a primary key, or you can add a synthetic primary key. For detailed solutions, see [Handle tables without primary keys while creating Amazon Aurora MySQL or Amazon RDS for MySQL zero-ETL integrations with Amazon Redshift](https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-mysql-or-amazon-rds-for-mysql-zero-etl-integrations-with-amazon-redshift/). 

## One or more of my Amazon Redshift tables requires a resync
<a name="zero-etl.troubleshooting.resync"></a>

Running certain commands on your source database might require your tables to be resynchronized. In these cases, the [SVV\_INTEGRATION\_TABLE\_STATE](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_INTEGRATION_TABLE_STATE.html) system view shows a `table_state` of `ResyncRequired`, which means that the integration must completely reload data for that specific table from MySQL to Amazon Redshift.

When the table starts to resynchronize, it enters a state of `Syncing`. You don't need to take any manual action to resynchronize a table. While table data is resynchronizing, you can't access it in Amazon Redshift.

The following are some example operations that can put a table into a `ResyncRequired` state, and possible alternatives to consider.


| Operation | Example | Alternative | 
| --- | --- | --- | 
| Adding a column into a specific position  |  <pre>ALTER TABLE {{table_name}}<br />  ADD COLUMN {{column_name}} INTEGER<br />  NOT NULL first;</pre>  | Amazon Redshift doesn't support adding columns into specific positions using first or after keywords. If the order of columns in the target table isn't critical, add the column to the end of the table using a simpler command:<pre>ALTER TABLE {{table_name}}<br />  ADD COLUMN {{column_name}} {{column_type}};</pre> | 
| Adding a timestamp column with the default CURRENT\_TIMESTAMP |  <pre>ALTER TABLE {{table_name}}<br />  ADD COLUMN {{column_name}} TIMESTAMP<br />  NOT NULL DEFAULT CURRENT_TIMESTAMP;</pre>  | The CURRENT\_TIMESTAMP value for existing table rows is calculated by RDS for MySQL and can't be simulated in Amazon Redshift without full table data resynchronization. If possible, switch the default value to a literal constant like `2023-01-01 00:00:15` to avoid latency in table availability. | 
| Performing multiple column operations within a single command |  <pre>ALTER TABLE {{table_name}}<br />  ADD COLUMN {{column_1}},<br />  RENAME COLUMN {{column_2}} TO {{column_3}};</pre>  | Consider splitting the command into two separate operations, ADD and RENAME, which won't require resynchronization. | 

## Integration failed issues for Amazon SageMaker AI lakehouse zero-ETL integrations
<a name="zero-etl.troubleshooting.integration-issues"></a>

If you encounter issues with an existing zero-ETL integration with an Amazon SageMaker AI lakehouse, the only resolution is to delete the integration and create a new one. Unlike other AWS services, zero-ETL integrations do not support refresh or resync operations.

To resolve integration issues:

1. Delete the problematic zero-ETL integration using the console, CLI, or API.

1. Verify that the source database and target data warehouse configurations are correct.

1. Create a new zero-ETL integration with the same or updated configuration.

This process will result in a complete re-initialization of the data pipeline, which may take time depending on the size of your source database.