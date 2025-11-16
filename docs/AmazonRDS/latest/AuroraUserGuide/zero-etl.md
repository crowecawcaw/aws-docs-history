# Troubleshooting Aurora zero-ETL integrations

You can check the state of a zero-ETL integration by querying the [SVV_INTEGRATION](../../../redshift/latest/dg/r_SVV_INTEGRATION.md "../../../redshift/latest/dg/r_SVV_INTEGRATION.md") system table in the
analytics destination. If the `state` column has a value of
`ErrorState`, it means something's wrong. For more information, see [Monitoring integrations using system tables for Amazon Redshift](zero-etl.md#zero-etl.monitoring "zero-etl.md#zero-etl.monitoring").

Use the following information to troubleshoot common issues with Aurora
zero-ETL integrations.

###### Important

Resync and refresh operations are not available for zero-ETL integrations with an
Amazon SageMaker AI lakehouse. If there are issues with an
integration, you must delete the integration and create a new integration. You can't
refresh or resync an existing integration.

###### Topics

- [I can't create a
  zero-ETL integration](#zero-etl.troubleshooting.creation "#zero-etl.troubleshooting.creation")
- [My integration is stuck in a state
  of Syncing](#zero-etl.troubleshooting.syncing "#zero-etl.troubleshooting.syncing")
- [My tables aren't replicating
  to Amazon Redshift](#zero-etl.troubleshooting.primarykey "#zero-etl.troubleshooting.primarykey")
- [One or more of my Amazon Redshift tables
  requires a resync](#zero-etl.troubleshooting.resync "#zero-etl.troubleshooting.resync")
- [Integration failed
  issues for Amazon SageMaker AI lakehouse zero-ETL integrations](#zero-etl.troubleshooting.integration-issues "#zero-etl.troubleshooting.integration-issues")
- [DDL changes are in Amazon Redshift before the
  DDL transaction is complete for Aurora PostgreSQL](#zero-etl.troubleshooting.ddl "#zero-etl.troubleshooting.ddl")

## I can't create a

zero-ETL integration

If you can't create a zero-ETL integration, make sure that the following are correct for
your source database:

- Your source database must be running a supported DB engine version. For a
  list of supported versions, see [Supported
  Regions and Aurora DB engines for zero-ETL integrations](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").
- You correctly configured DB parameters. If the required parameters are
  set incorrectly or not associated with the database, creation fails. See
  [Step 1: Create a custom DB cluster parameter group](zero-etl.md#zero-etl.parameters "zero-etl.md#zero-etl.parameters").

In addition, make sure the following are correct for your target data
warehouse:

- Case sensitivity is enabled. See [Turn on case sensitivity for your data warehouse](../../../redshift/latest/mgmt/zero-etl-using.md#zero-etl-setting-up.case-sensitivity "../../../redshift/latest/mgmt/zero-etl-using.md#zero-etl-setting-up.case-sensitivity").
- You added the correct authorized principal and integration source. See
  [Configure authorization for your Amazon Redshift data
  warehouse](../../../redshift/latest/mgmt/zero-etl-using.md#zero-etl-using.redshift-iam "../../../redshift/latest/mgmt/zero-etl-using.md#zero-etl-using.redshift-iam").
- The data warehouse is encrypted (if it's a provisioned cluster). See
  [Amazon Redshift database
  encryption](../../../redshift/latest/mgmt/working-with-db-encryption.md "../../../redshift/latest/mgmt/working-with-db-encryption.md").

## My integration is stuck in a state

of `Syncing`

Your integration might consistently show a status of `Syncing` if you
change the value of one of the required DB parameters.

To fix this issue, check the values of the parameters in the parameter group
associated with the source DB cluster, and make sure that they match the required
values. For more information, see [Step 1: Create a custom DB cluster parameter group](zero-etl.md#zero-etl.parameters "zero-etl.md#zero-etl.parameters").

If you modify any parameters, make sure to reboot the DB cluster
to apply the changes.

## My tables aren't replicating

to Amazon Redshift

If you don't see one or more tables reflected in Amazon Redshift, you can run the following
command to resynchronize them:

```
ALTER DATABASE `dbname` INTEGRATION REFRESH TABLES `table1`, `table2`;
```

For more information, see [ALTER
DATABASE](../../../redshift/latest/dg/r_ALTER_DATABASE.md "../../../redshift/latest/dg/r_ALTER_DATABASE.md") in the Amazon Redshift SQL reference.

Your data might not be replicating because one or more of your source tables
doesn't have a primary key. The monitoring dashboard in Amazon Redshift displays the status of
these tables as `Failed`, and the status of the overall zero-ETL integration
changes to `Needs attention`. To resolve this issue, you can identify an
existing key in your table that can become a primary key, or you can add a synthetic
primary key. For detailed solutions, see
the following resources:

- [Handle tables without primary keys while creating Amazon Aurora MySQL
  or Amazon RDS for MySQL zero-ETL integrations with Amazon
  Redshift](https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-mysql-or-amazon-rds-for-mysql-zero-etl-integrations-with-amazon-redshift/ "https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-mysql-or-amazon-rds-for-mysql-zero-etl-integrations-with-amazon-redshift/")
- [Handle tables without primary keys while creating Amazon Aurora
  PostgreSQL zero-ETL integrations with Amazon Redshift](https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-postgresql-zero-etl-integrations-with-amazon-redshift/ "https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-postgresql-zero-etl-integrations-with-amazon-redshift/")

## One or more of my Amazon Redshift tables

requires a resync

Running certain commands on your source database might require your tables to be
resynchronized. In these cases, the [SVV_INTEGRATION_TABLE_STATE](../../../redshift/latest/dg/r_SVV_INTEGRATION_TABLE_STATE.md "../../../redshift/latest/dg/r_SVV_INTEGRATION_TABLE_STATE.md") system view shows a
`table_state` of `ResyncRequired`, which means that the
integration must completely reload data for that specific table from MySQL to
Amazon Redshift.

When the table starts to resynchronize, it enters a state of `Syncing`.
You don't need to take any manual action to resynchronize a table. While table data
is resynchronizing, you can't access it in Amazon Redshift.

The following are some example operations that can put a table into a
`ResyncRequired` state, and possible alternatives to consider.

| Operation                                                         | Example                                                                                                           | Alternative                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Adding a column into a specific position                          | ``<br>ALTER TABLE `table_name`<br>ADD COLUMN `column_name` INTEGER<br>NOT NULL first;<br>``                       | Amazon Redshift doesn't support adding columns into specific positions using<br>`first` or `after` keywords. If the order<br>of columns in the target table isn't critical, add the column to the<br>end of the table using a simpler<br>command:<br>``<br>ALTER TABLE `table_name`<br>ADD COLUMN `column_name` `column_type`;<br>`` |
| Adding a timestamp column with the default<br>`CURRENT_TIMESTAMP` | ``<br>ALTER TABLE `table_name`<br>ADD COLUMN `column_name` TIMESTAMP<br>NOT NULL DEFAULT CURRENT_TIMESTAMP;<br>`` | The `CURRENT_TIMESTAMP` value for existing table rows<br>is calculated by Aurora MySQL and can't be simulated in Amazon Redshift without full<br>table data resynchronization. If possible, switch the default<br>value to a literal constant like `2023-01-01<br>00:00:15` to avoid latency in table<br>availability.               |
| Performing multiple column operations within a single<br>command  | ``<br>ALTER TABLE `table_name`<br>ADD COLUMN `column_1`,<br>RENAME COLUMN `column_2` TO `column_3`;<br>``         | Consider splitting the command into two separate operations,<br>`ADD` and `RENAME`, which won't require<br>resynchronization.                                                                                                                                                                                                        |

## Integration failed

issues for Amazon SageMaker AI lakehouse zero-ETL integrations

If you encounter issues with an existing zero-ETL integration with an Amazon SageMaker AI lakehouse, the only resolution is to delete the integration
and create a new one. Unlike other AWS services, zero-ETL integrations do not support
refresh or resync operations.

To resolve integration issues:

1. Delete the problematic zero-ETL integration using the console, CLI, or
   API.
2. Verify that the source database and target data warehouse configurations
   are correct.
3. Create a new zero-ETL integration with the same or updated configuration.

This process will result in a complete re-initialization of the data pipeline,
which may take time depending on the size of your source database.

## DDL changes are in Amazon Redshift before the

DDL transaction is complete for Aurora PostgreSQL

DDL changes can appear in Amazon Redshift before a DDL operation finishes in Aurora PostgreSQL
zero-ETL integrations. For more information, see [DDL operations for Aurora PostgreSQL](zero-etl.md#zero-etl.ddl-postgres "zero-etl.md#zero-etl.ddl-postgres").
