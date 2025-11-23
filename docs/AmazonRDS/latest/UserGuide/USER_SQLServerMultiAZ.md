# Multi-AZ deployments for Amazon RDS for Microsoft SQL Server

Multi-AZ deployments provide increased availability, data durability, and fault tolerance for DB instances. In the event of planned
database maintenance or unplanned service disruption, Amazon RDS automatically fails over to the up-to-date secondary DB instance. This
functionality lets database operations resume quickly without manual intervention. The primary and standby instances use the same
endpoint, whose physical network address transitions to the secondary replica as part of the failover process. You don't have to
reconfigure your application when a failover occurs.

Amazon RDS supports Multi-AZ deployments for Microsoft SQL Server by using either SQL Server
Database Mirroring (DBM), Always On Availability Groups (AGs), or block level replication. Amazon RDS monitors and maintains the health
of your Multi-AZ deployment. If problems occur, RDS automatically repairs unhealthy DB
instances, reestablishes synchronization, and initiates failovers. Failover only occurs if
the standby and primary are fully in sync. You don't have to manage anything.

When you set up SQL Server Multi-AZ, RDS automatically configures all databases on the
instance to use DBM, AGs, or block level replication. Amazon RDS handles the primary, the witness, and the secondary DB
instance for you when you configure DBM or AGs. For block level replication, RDS handles the primary and the secondary DB instances.
Because configuration is automatic, RDS selects DBM, Always On AGs, or block level replication based
on the version of SQL Server that you deploy.

Amazon RDS supports Multi-AZ with Always On AGs for the following SQL Server versions and
editions:

- SQL Server 2022:
  - Standard Edition
  - Enterprise Edition

- SQL Server 2019:
  - Standard Edition 15.00.4073.23 and higher
  - Enterprise Edition

- SQL Server 2017:
  - Standard Edition 14.00.3401.7 and higher
  - Enterprise Edition 14.00.3049.1 and higher

- SQL Server 2016: Enterprise Edition 13.00.5216.0 and higher
  Amazon RDS supports Multi-AZ with DBM for the following SQL Server versions and editions, except for the versions noted previously:

- SQL Server 2019: Standard Edition 15.00.4043.16
- SQL Server 2017: Standard and Enterprise Editions
- SQL Server 2016: Standard and Enterprise Editions
  Amazon RDS supports Multi-AZ with block level replication for SQL Server 2022 Web Edition 16.00.4215.2 and above.

###### Note

Only new DB instances created with 16.00.4215.2 or higher support Multi-AZ deployments with block level replication.
The following restrictions apply for existing SQL Server 2022 Web Edition instances:

- For existing instances on version 16.00.4215.2, you must restore a snapshot to
  a new instance with the same or higher minor version to enable block level replication.
- SQL Server 2022 Web instances with an older minor version can
  be upgraded to minor version 16.00.4215.2 or higher to enable block level replication.
  You can use the following SQL query to determine whether your SQL Server DB instance is
  Single-AZ, Multi-AZ with DBM, or Multi-AZ with Always On AGs.
  This query does not apply for Multi-AZ deployments on SQL Server Web Edition.

```
SELECT CASE WHEN dm.mirroring_state_desc IS NOT NULL THEN 'Multi-AZ (Mirroring)'
    WHEN dhdrs.group_database_id IS NOT NULL THEN 'Multi-AZ (AlwaysOn)'
    ELSE 'Single-AZ'
    END 'high_availability'
FROM sys.databases sd
LEFT JOIN sys.database_mirroring dm ON sd.database_id = dm.database_id
LEFT JOIN sys.dm_hadr_database_replica_states dhdrs ON sd.database_id = dhdrs.database_id AND dhdrs.is_local = 1
WHERE DB_NAME(sd.database_id) = 'rdsadmin';
```

The output resembles the following:

```
high_availability
Multi-AZ (AlwaysOn)
```

## Adding Multi-AZ to a Microsoft SQL Server

DB instance

When you create a new SQL Server DB instance using the AWS Management Console, you can add Multi-AZ with Database Mirroring (DBM), Always On
AGs or block level replication. You do so by choosing **Yes (Mirroring / Always On / Block Level Replication)** from **Multi-AZ deployment**. For
more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

When you modify an existing SQL Server DB instance using the console, you can add Multi-AZ with DBM, AGs, or block level replication by choosing
**Yes (Mirroring / Always On / Block Level Replication)** from **Multi-AZ deployment** on the **Modify DB
instance** page. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

###### Note

If your DB instance is running Database Mirroring (DBM)—not Always On Availability
Groups (AGs)—you might need to disable in-memory optimization before you add
Multi-AZ. Disable in-memory optimization with DBM before you add Multi-AZ if your DB
instance runs SQL Server 2016 or 2017 Enterprise Edition and has in-memory
optimization enabled.

If your DB instance is running AGs or block level replication for SQL Server Web Editions, it doesn't require this step.

## Removing Multi-AZ from a Microsoft SQL Server

DB instance

When you modify an existing SQL Server DB instance using the AWS Management Console, you can remove
Multi-AZ with DBM, AGs, or block level replication. You can do this by choosing **No (Mirroring / Always
On / Block Level Replication)** from **Multi-AZ deployment** on the **Modify
DB instance** page. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
