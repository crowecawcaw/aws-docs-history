# Maintenance plans

This topic provides reference information comparing database maintenance tasks between Microsoft SQL Server and Amazon Aurora PostgreSQL. You can understand the key differences in how these two database systems handle common maintenance operations such as backups, index management, statistics updates, and consistency checks.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                              |
| -------------------------------- | ---------------------------------- | ------------------------- | ---------------------------------------------------------------------------- |
| Three star feature compatibility | N/A                                | N/A                       | Backups using the Amazon RDS services. Table maintenance using SQL commands. |

## SQL Server Usage

A _maintenance plan_ is a set of automated tasks used to optimize a database, performs regular backups, and ensure it is free of inconsistencies. Maintenance plans are implemented as SQL Server Integration Services (SSIS) packages and are run by SQL Server Agent jobs. You can run them manually or automatically at scheduled time intervals.

SQL Server provides a variety of pre-configured maintenance tasks. You can create custom tasks using TSQL scripts or operating system batch files.

Maintenance plans are typically used for the following tasks:

- Backing up database and transaction log files.
- Performing cleanup of database backup files in accordance with retention policies.
- Performing database consistency checks.
- Rebuilding or reorganizing indexes.
- Decreasing data file size by removing empty pages (shrink a database).
- Updating statistics to help the query optimizer obtain updated data distributions.
- Running SQL Server Agent jobs for custom actions.
- Running a T-SQL task.

Maintenance plans can include tasks for operator notifications and history or maintenance cleanup. They can also generate reports and output the contents to a text file or the maintenance plan tables in the `msdb` database.

You can create and manage maintenance plans using the maintenance plan wizard in SQL Server Management Studio, Maintenance Plan Design Surface (provides enhanced functionality over the wizard), Management Studio Object Explorer, and T-SQL system stored procedures.

For more information, see [SQL Server Agent and PostgreSQL Scheduled Lambda](chap-sql-server-aurora-pg.management.md "chap-sql-server-aurora-pg.management.md").

### Deprecated DBCC Index and Table Maintenance Commands

The DBCC DBREINDEX, INDEXDEFRAG, and SHOWCONTIG commands have been deprecated as of SQL Server 2008R2. For more information, see [Deprecated Database Engine Features in SQL Server 2008 R2](<https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143729(v=sql.105)> "https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143729(v=sql.105)") in the _SQL Server documentation_.

In place of the deprecated DBCC, SQL Server provides newer syntax alternatives as detailed in the following table.

| Deprecated DBCC command | Use instead                      |
| ----------------------- | -------------------------------- |
| `DBCC DBREINDEX`        | `ALTER INDEX …​ REBUILD`         |
| `DBCC INDEXDEFRAG`      | `ALTER INDEX …​ REORGANIZE`      |
| `DBCC SHOWCONTIG`       | `sys.dm_db_index_physical_stats` |

For the Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) alternatives to these maintenance commands, see [Aurora PostgreSQL Maintenance Plans](#chap-sql-server-aurora-pg.management.maintenanceplans.pg "#chap-sql-server-aurora-pg.management.maintenanceplans.pg").

### Examples

Enable Agent XPs, which are disabled by default.

```
EXEC [sys].[sp_configure] @configname = 'show advanced options', @configvalue = 1 RECONFIGURE ;
```

```
EXEC [sys].[sp_configure] @configname = 'agent xps', @configvalue = 1 RECONFIGURE;
```

Create a T-SQL maintenance plan for a single index rebuild.

```
USE msdb;
```

Add the Index Maintenance `IDX1` job to SQL Server Agent.

```
EXEC dbo.sp_add_job @job_name = N'Index Maintenance IDX1', @enabled = 1, @description = N'Optimize IDX1 for INSERT' ;
```

Add the T-SQL job step `Rebuild IDX1 to 50 percent fill`.

```
EXEC dbo.sp_add_jobstep @job_name = N'Index Maintenance IDX1', @step_name = N'Rebuild IDX1 to 50 percent fill', @subsystem = N'TSQL',
@command = N'Use MyDatabase; ALTER INDEX IDX1 ON Shcema.Table REBUILD WITH ( FILL_FACTOR = 50), @retry_attempts = 5, @retry_interval = 5;
```

Add a schedule to run every day at 01:00 AM.

```
EXEC dbo.sp_add_schedule @schedule_name = N'Daily0100', @freq_type = 4, @freq_interval = 1, @active_start_time = 010000;
```

Associate the schedule `Daily0100` with the job index maintenance `IDX1`.

```
EXEC sp_attach_schedule @job_name = N'Index Maintenance IDX1' @schedule_name = N'Daily0100' ;
```

For more information, see [Maintenance Plans](https://docs.microsoft.com/en-us/sql/relational-databases/maintenance-plans/maintenance-plans?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/maintenance-plans/maintenance-plans?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

Amazon Relational Database Service (Amazon RDS) performs automated database backups by creating storage volume snapshots that back up entire instances, not individual databases.

Amazon RDS creates snapshots during the backup window for individual database instances and retains snapshots in accordance with the backup retention period. You can use the snapshots to restore a database to any point in time within the backup retention period.

###### Note

The state of a database instance must be ACTIVE for automated backups to occur.

You can backup database instances manually by creating an explicit database snapshot. Use the AWS console, the AWS CLI, or the AWS API to take manual snapshots.

### Examples

**Create a manual database snapshot using the Amazon RDS console**

1. In the AWS console, choose **RDS**, and then choose **Databases**.
2. Choose your Aurora PostgreSQL instance, and for **Instance actions** choose **Take snapshot**.

![Take snapshot](images/pb-sql-server-aurora-pg-take-snapshot.png)

**Restore a snapshot using the Amazon RDS console**

1. In the AWS console, choose **RDS**, and then choose **Snapshots**.
2. Choose the snapshot to restore, and for **Actions** choose **Restore snapshot**.

This action creates a new instance. 3. Enter the required configuration options in the wizard for creating a new Amazon Aurora database instance. Choose **Restore DB Instance**.

You can also restore a database instance to a point-in-time. For more information, see [Backup and Restore](chap-sql-server-aurora-pg.hadr.md "chap-sql-server-aurora-pg.hadr.md").

For all other tasks, use a third-party or a custom application scheduler.

**Rebuild and reorganize a table**

Aurora PostgreSQL supports the `VACUUM`, `ANALYZE`, and `REINDEX` commands, which are similar to the `REORGANIZE` option of SQL Server indexes.

```
VACUUM MyTable;
ANALYZE MyTable;
REINDEX TABLE MyTable;
```

- `VACUUM` reclaims storage.
- `ANALYZE` collects statistics.
- `REINDEX` recreates all indexes.

For more information, see [ANALYZE](https://www.postgresql.org/docs/13/sql-analyze.html "https://www.postgresql.org/docs/13/sql-analyze.html"), [VACUUM](https://www.postgresql.org/docs/13/sql-vacuum.html "https://www.postgresql.org/docs/13/sql-vacuum.html"), and [REINDEX](https://www.postgresql.org/docs/13/sql-reindex.html "https://www.postgresql.org/docs/13/sql-reindex.html") in the _PostgreSQL documentation_.

**Convert deprecated DBCC index and table maintenance commands**

| Deprecated DBCC command | Aurora PostgreSQL equivalent                           |
| ----------------------- | ------------------------------------------------------ |
| `DBCC DBREINDEX`        | `REINDEX INDEX` or `REINDEX TABLE`                     |
| `DBCC INDEXDEFRAG`      | `VACUUM table_name` or `VACUUM table_name column_name` |

**Update statistics to help the query optimizer get updated data distribution**

For more information, see [SQL Server Managing Statistics and PostgreSQL Table Statistics](chap-sql-server-aurora-pg.tuning.md "chap-sql-server-aurora-pg.tuning.md").

## Summary

The following table summarizes the key tasks that use SQL Server maintenance plans and a comparable Aurora PostgreSQL solutions.

| Task                                                                        | SQL Server                                 | Aurora PostgreSQL                          |
| --------------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------ |
| Rebuild or reorganize indexes                                               | `ALTER INDEX` or `ALTER TABLE`             | `REINDEX INDEX` or `REINDEX TABLE`         |
| Decrease data file size by removing empty pages                             | `DBCC SHRINKDATABASE` or `DBCC SHRINKFILE` | `VACUUM`                                   |
| Update statistics to help the query optimizer get updated data distribution | `UPDATE STATISTICS` or `sp_updatestats`    | `ANALYZE`                                  |
| Perform database consistency checks                                         | `DBCC CHECKDB` or `DBCC CHECKTABLE`        | N/A                                        |
| Back up the database and transaction log files                              | `BACKUP DATABASE` or `BACKUP LOG`          | Automatically (for example, using AWS CLI) |
| Run SQL Server Agent jobs for custom actions                                | `sp_start_job` or `scheduled`              | N/A                                        |

For more information, see [Working with backups](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md") in the _PostgreSQL documentation_.
