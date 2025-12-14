# TempDB configuration for Multi-AZ deployments

If your RDS for SQL Server DB instance is in a Multi-AZ Deployment using Database Mirroring (DBM) or Always On Availability Groups (AGs), keep in mind the following
considerations for using the `tempdb` database.

You can't replicate `tempdb` data from your primary DB instance to your secondary DB instance. When you fail over to
a secondary DB instance, `tempdb` on that secondary DB instance will be empty.

You can synchronize the configuration of the `tempdb` database options, including its file sizing and autogrowth settings,
from your primary DB instance to your secondary DB instance. Synchronizing the `tempDB` configuration is supported on all RDS for SQL Server versions.
You can turn on automatic synchronization of the `tempdb` configuration by using the following stored procedure:

```
EXECUTE msdb.dbo.rds_set_system_database_sync_objects @object_types = 'TempDbFile';
```

###### Important

Before using the `rds_set_system_database_sync_objects` stored procedure, ensure you've set your preferred `tempdb` configuration
on your primary DB instance, rather than on your secondary DB instance. If you made the configuration change on your secondary DB instance, your preferred
`tempdb` configuration could be deleted when you turn on automatic synchronization.

You can use the following function to confirm whether automatic synchronization of the `tempdb` configuration is turned on:

```
SELECT * from msdb.dbo.rds_fn_get_system_database_sync_objects();
```

When automatic synchronization of the `tempdb` configuration is turned on, there will be a return value for the `object_class` field. When
it's turned off, no value is returned.

You can use the following function to find the last time objects were synchronized, in UTC time:

```
SELECT * from msdb.dbo.rds_fn_server_object_last_sync_time();
```

For example, if you modified the `tempdb` configuration at 01:00 and then run the `rds_fn_server_object_last_sync_time` function,
the value returned for `last_sync_time` should be after 01:00, indicating that an automatic synchronization occurred.

If you are also using SQL Server Agent job replication, you can enable replication for both SQL Agent jobs and the `tempdb`
configuration by providing them in the `@object_type` parameter:

```
EXECUTE msdb.dbo.rds_set_system_database_sync_objects @object_types = 'SQLAgentJob,TempDbFile';
```

For more information on SQL Server Agent job replication, see [Turning on SQL Server Agent job replication](Appendix.SQLServer.CommonDBATasks.md#SQLServerAgent.Replicate "Appendix.SQLServer.CommonDBATasks.md#SQLServerAgent.Replicate").

As an alternative to using the `rds_set_system_database_sync_objects` stored procedure to ensure that `tempdb` configuration changes
are automatically synchronized, you can use one of the following manual methods:

###### Note

We recommend turning on automatic synchronization of the `tempdb` configuration by using the `rds_set_system_database_sync_objects` stored procedure.
Using automatic synchronization prevents the need to perform these manual tasks each time you change your `tempdb` configuration.

- First modify your DB instance and turn Multi-AZ off, then modify tempdb, and finally turn
  Multi-AZ back on. This method doesn't involve any downtime.

For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

- First modify `tempdb` in the original primary instance, then fail over
  manually, and finally modify `tempdb` in the new primary instance.
  This method involves downtime.

For more information, see [Rebooting a DB instance](USER_RebootInstance.md "USER_RebootInstance.md").
