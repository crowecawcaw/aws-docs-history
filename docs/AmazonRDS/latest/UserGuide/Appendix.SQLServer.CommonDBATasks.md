# Using SQL Server Agent for Amazon RDS

With Amazon RDS, you can use SQL Server Agent on a DB instance running Microsoft SQL Server Enterprise Edition, Standard Edition, or Web
Edition. SQL Server Agent is a Microsoft Windows service that runs scheduled administrative tasks that are called jobs. You can
use SQL Server Agent to run T-SQL jobs to rebuild indexes, run corruption checks, and aggregate data in a SQL Server DB
instance.

When you create a SQL Server DB instance, the master user is enrolled in the `SQLAgentUserRole` role.

SQL Server Agent can run a job on a schedule, in response to a specific event, or on demand. For more information, see [SQL Server Agent](http://msdn.microsoft.com/en-us/library/ms189237 "http://msdn.microsoft.com/en-us/library/ms189237") in the Microsoft documentation.

###### Note

Avoid scheduling jobs to run during the maintenance and backup windows for your DB instance. The maintenance and backup
processes that are launched by AWS could interrupt a job or cause it to be canceled.

In Multi-AZ deployments, SQL Server Agent jobs are replicated from the primary host to the secondary host when the job
replication feature is turned on. For more information, see [Turning on SQL Server Agent job replication](#SQLServerAgent.Replicate "#SQLServerAgent.Replicate").

Multi-AZ deployments have a limit of 10,000 SQL Server Agent jobs. If you need a higher limit, request an increase by
contacting Support. Open the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") page, sign in if necessary, and
choose **Create case**. Choose **Service limit increase**. Complete and submit the
form.

To view the history of an individual SQL Server Agent job in SQL Server Management Studio (SSMS), open Object Explorer, right-click
the job, and then choose **View History**.

Because SQL Server Agent is running on a managed host in a DB instance, some actions aren't supported:

- Running replication jobs and running command-line scripts by using ActiveX, Windows command shell, or Windows
  PowerShell aren't supported.
- You can't manually start, stop, or restart SQL Server Agent.
- Email notifications through SQL Server Agent aren't available from a DB instance.
- SQL Server Agent alerts and operators aren't supported.
- Using SQL Server Agent to create backups isn't supported. Use Amazon RDS to back up your DB instance.
- Currently, RDS for SQL Server does not support the use SQL Server Agent tokens.

## Turning on SQL Server Agent job replication

You can turn on SQL Server Agent job replication by using the following stored procedure:

```
EXECUTE msdb.dbo.rds_set_system_database_sync_objects @object_types = 'SQLAgentJob';
```

You can run the stored procedure on all SQL Server versions supported by Amazon RDS for SQL Server. Jobs in the following categories are
replicated:

- [Uncategorized (Local)]
- [Uncategorized (Multi-Server)]
- [Uncategorized]
- Data Collector
- Database Engine Tuning Advisor
- Database Maintenance
- Full-Text

Only jobs that use T-SQL job steps are replicated. Jobs with step types such as SQL Server Integration Services (SSIS),
SQL Server Reporting Services (SSRS), Replication, and PowerShell aren't replicated. Jobs that use Database Mail and
server-level objects aren't replicated.

###### Important

The primary host is the source of truth for replication. Before turning on job replication, make sure that your SQL
Server Agent jobs are on the primary. If you don't do this, it could lead to the deletion of your SQL Server Agent jobs
if you turn on the feature when newer jobs are on the secondary host.

You can use the following function to confirm whether replication is turned on.

```
SELECT * from msdb.dbo.rds_fn_get_system_database_sync_objects();
```

The T-SQL query returns the following if SQL Server Agent jobs are replicating. If they're not replicating, it
returns nothing for `object_class`.

![SQL Server Agent jobs are replicating](images/SQLAgentJob.png)

You can use the following function to find the last time objects were synchronized in UTC time.

```
SELECT * from msdb.dbo.rds_fn_server_object_last_sync_time();
```

For example, suppose that you modify a SQL Server Agent job at 01:00. You expect
the most recent synchronization time to be after 01:00, indicating that
synchronization has taken place.

After synchronization, the values returned for `date_created` and `date_modified` on the secondary node are expected to match.

![Last time server objects were synchronized was 01:21:23](images/SQLAgentJob_last_sync_time.png)

If you are also using `tempdb` replication, you can enable replication for both SQL Agent jobs and the `tempdb`
configuration by providing them in the `@object_type` parameter:

```
EXECUTE msdb.dbo.rds_set_system_database_sync_objects @object_types = 'SQLAgentJob,TempDbFile';
```

For more information on `tempdb` replication, see [TempDB configuration for Multi-AZ deployments](SQLServer.TempDB.md "SQLServer.TempDB.md").
