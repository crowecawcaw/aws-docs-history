# Using a Microsoft SQL Server database as a

source for AWS DMS

Migrate data from one or many Microsoft SQL Server databases using AWS DMS. With a SQL
Server database as a source, you can migrate data to another SQL Server database, or to
one of the other AWS DMS supported databases.

For information about versions of SQL
Server that AWS DMS supports as a source, see [Sources for AWS DMS](CHAP_Introduction.md "CHAP_Introduction.md").

The source SQL Server database can be installed on any computer in your network. A SQL
Server account with appropriate access privileges to the source database for the type of
task you chose is required for use with AWS DMS. For more information, see
[Permissions for SQL Server
tasks](#CHAP_Source.SQLServer.Permissions "#CHAP_Source.SQLServer.Permissions").

AWS DMS supports migrating data from named instances of SQL Server. You can use the
following notation in the server name when you create the source endpoint.

```
IPAddress\InstanceName
```

For example, the following is a correct source endpoint server name. Here, the first
part of the name is the IP address of the server, and the second part is the SQL Server
instance name (in this example, SQLTest).

```
10.0.0.25\SQLTest
```

Also, obtain the port number that your named instance of SQL Server listens on, and
use it to configure your AWS DMS source endpoint.

###### Note

Port 1433 is the default for Microsoft SQL Server. But dynamic ports that change
each time SQL Server is started, and specific static port numbers used to connect to
SQL Server through a firewall are also often used. So, you want to know the actual
port number of your named instance of SQL Server when you create the AWS DMS source
endpoint.

You can use SSL to encrypt connections between your SQL Server endpoint and the
replication instance. For more information on using SSL with a SQL Server endpoint, see
[Using SSL with AWS Database Migration Service](CHAP_Security.md "CHAP_Security.md").

You can use CDC for ongoing migration from a SQL Server database. For information
about configuring your source SQL server database for CDC, see
[Capturing data changes for ongoing replication from SQL Server](CHAP_Source.SQLServer.md "CHAP_Source.SQLServer.md").

For additional details on working with SQL Server source databases and AWS DMS, see the
following.

###### Topics

- [Limitations on using SQL Server
  as a source for AWS DMS](#CHAP_Source.SQLServer.Limitations "#CHAP_Source.SQLServer.Limitations")
- [Permissions for SQL Server
  tasks](#CHAP_Source.SQLServer.Permissions "#CHAP_Source.SQLServer.Permissions")
- [Prerequisites for using ongoing
  replication (CDC) from a SQL Server source](#CHAP_Source.SQLServer.Prerequisites "#CHAP_Source.SQLServer.Prerequisites")
- [Supported compression
  methods for SQL Server](#CHAP_Source.SQLServer.Compression "#CHAP_Source.SQLServer.Compression")
- [Working with self-managed SQL Server AlwaysOn
  availability groups](#CHAP_Source.SQLServer.AlwaysOn "#CHAP_Source.SQLServer.AlwaysOn")
- [Endpoint settings
  when using SQL Server as a source for AWS DMS](#CHAP_Source.SQLServer.ConnectionAttrib "#CHAP_Source.SQLServer.ConnectionAttrib")
- [Source data types for SQL
  Server](#CHAP_Source.SQLServer.DataTypes "#CHAP_Source.SQLServer.DataTypes")
- [Capturing data changes for ongoing replication from SQL Server](CHAP_Source.SQLServer.md "CHAP_Source.SQLServer.md")

## Limitations on using SQL Server

as a source for AWS DMS

The following limitations apply when using a SQL Server database as a source for
AWS DMS:

- The identity property for a column isn't migrated to a target
  database column.
- The SQL Server endpoint doesn't support the use of tables with sparse
  columns.
- Windows Authentication isn't supported.
- Changes to computed fields in a SQL Server aren't replicated.
- Temporal tables aren't supported.
- SQL Server partition switching isn't supported.
- When using the WRITETEXT and UPDATETEXT utilities, AWS DMS doesn't
  capture events applied on the source database.
- The following data manipulation language (DML) pattern isn't
  supported.

```
SELECT * INTO `new_table` FROM `existing_table`
```

- When using SQL Server as a source, column-level encryption isn't
  supported.
- AWS DMS doesn't support server level audits on SQL Server 2008 or SQL
  Server 2008 R2 as sources. This is because of a known issue with SQL Server
  2008 and 2008 R2. For example, running the following command causes AWS DMS to
  fail.

```
USE [master]
GO
ALTER SERVER AUDIT [my_audit_test-20140710] WITH (STATE=on)
GO
```

- Geometry and Geography columns are not supported in full lob mode when
  using SQL Server as a source. Instead, use limited lob mode or set the
  `InlineLobMaxSize` task setting to use inline lob mode.
- When using a Microsoft SQL Server source database in a replication task,
  the SQL Server Replication Publisher definitions aren't removed if you
  remove the task. A Microsoft SQL Server system administrator must delete
  those definitions from Microsoft SQL Server.
- Migrating data from schema-bound and non-schema-bound views is supported for full-load only tasks.
- Renaming tables using sp_rename isn't supported (for example,
  `sp_rename 'Sales.SalesRegion', 'SalesReg;)`
- Renaming columns using sp_rename isn't supported (for example,
  `sp_rename 'Sales.Sales.Region', 'RegID', 'COLUMN';`)
- AWS DMS doesn't support change processing to set and unset column
  default values (using the `ALTER COLUMN SET DEFAULT` clause with `ALTER TABLE`
  statements).
- AWS DMS doesn't support change processing to set column nullability
  (using the `ALTER COLUMN [SET|DROP] NOT NULL` clause with `ALTER TABLE`
  statements).
- With SQL Server 2012 and SQL Server 2014, when using DMS replication with Availability Groups,
  the distribution database can't be placed in an availability group. SQL 2016 supports placing the
  distribution database into an availability group, except for distribution databases used in merge, bidirectional,
  or peer-to-peer replication topologies.
- For partitioned tables, AWS DMS doesn't support different data compression settings
  for each partition.
- When inserting a value into SQL Server spatial data types (GEOGRAPHY and
  GEOMETRY), you can either ignore the spatial reference system identifier
  (SRID) property or specify a different number. When replicating tables with
  spatial data types, AWS DMS replaces the SRID with the default SRID (0 for
  GEOMETRY and 4326 for GEOGRAPHY).
- If your database isn't configured for MS-REPLICATION or MS-CDC, you
  can still capture tables that do not have a Primary Key, but only
  INSERT/DELETE DML events are captured. UPDATE and TRUNCATE TABLE events are
  ignored.
- Columnstore indexes aren't supported.
- Memory-optimized tables (using In-Memory OLTP) aren't
  supported.
- When replicating a table with a primary key that consists of multiple
  columns, updating the primary key columns during full load isn't
  supported.
- Delayed durability isn't supported.
- The `readBackupOnly=true` endpoint setting (extra connection
  attribute) doesn't work on RDS for SQL Server source instances because of the way RDS
  performs backups.
- `EXCLUSIVE_AUTOMATIC_TRUNCATION` doesn’t work on Amazon RDS SQL
  Server source instances because RDS users don't have access to run the
  SQL Server stored procedure, `sp_repldone`.
- AWS DMS doesn't capture truncate commands.
- AWS DMS doesn't support replication from databases with accelerated database
  recovery (ADR) turned on.
- AWS DMS doesn't support capturing data definition language (DDL) and data
  manipulation language (DML) statements within a single transaction.
- AWS DMS doesn't support the replication of data-tier application
  packages (DACPAC).
- UPDATE statements that involve primary keys or unique indexes and update
  multiple data rows, can cause conflicts when you apply changes to the target
  database. This might happen, for example, when the target database applies
  updates as INSERT and DELETE statements instead of a single UPDATE statement.
  With the batch optimized apply mode, the table might be ignored. With the
  transactional apply mode, the UPDATE operation might result in constraint
  violations. To avoid this issue, reload the relevant table. Alternatively,
  locate the problematic records in the Apply Exceptions control table
  (`dmslogs.awsdms_apply_exceptions`) and edit them manually
  in the target database. For more information, see [Change processing tuning settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md").
- AWS DMS doesn't support the replication of tables and schemas, where
  the name includes a special character from the following set.

`\\ -- \n \" \b \r ' \t ;`

- Data masking isn't supported. AWS DMS migrates masked data
  without masking.
- AWS DMS replicates up to 32,767 tables with primary keys and up to 1,000
  columns for each table. This is because AWS DMS creates a SQL Server replication
  article for each replicated table, and SQL Server replication articles have
  these limitations.
- When using Change Data Capture (CDC), you must define all columns that make up a unique index
  as `NOT NULL`. If this requirement is not met, SQL Server system error 22838 will result.
- You may lose events if SQL Server archives from the active transaction log to the backup log, or truncates
  them from the active transaction log.

The following limitations apply when accessing the backup transaction logs:

- Encrypted backups aren't supported.
- Backups stored at a URL or on Windows Azure aren't supported.
- AWS DMS doe snot support direct processing of transaction log backups at the
  file level from alternative shared folders.
- For Cloud SQL Server sources other than Amazon RDS for Microsoft SQL Server, AWS DMS supports ongoing replication (CDC)
  with the active transaction log only. You can't use the backup
  log with CDC. You may lose events if SQL server archives them from the active transaction log to the backup log, or truncates
  them from the active transaction log before DMS can read it.
- For Amazon RDS for Microsoft SQL Server sources, AWS DMS 3.5.2 and below supports ongoing replication (CDC) with the
  active transaction log only, because DMS can’t access the backup log with CDC.
  You may lose events if RDS for SQL Server archives them from the active transaction log to
  the backup log, or truncate them from the active transaction log before DMS can
  read it. This limitation does not apply to AWS DMS version 3.5.3 and above.
- AWS DMS does not support CDC for Amazon RDS Proxy for SQL Server as a
  source.
- If the SQL Server source becomes unavailable during a full load task, AWS DMS
  might mark the task as completed after multiple reconnection attempts, even
  though the data migration remains incomplete. In this scenario, the target
  tables contain only the records migrated before the connection loss, potentially
  creating data inconsistencies between the source and target systems. To ensure
  data completeness, you must either restart the full load task entirely or reload
  the specific tables affected by the connection interruption.

## Permissions for SQL Server

tasks

###### Topics

- [Permissions for full load only
  tasks](#CHAP_Source.SQLServer.Permissions.FullLoad "#CHAP_Source.SQLServer.Permissions.FullLoad")
- [Permissions for tasks with ongoing replication](#CHAP_Source.SQLServer.Permissions.Ongoing "#CHAP_Source.SQLServer.Permissions.Ongoing")

### Permissions for full load only

tasks

The following permissions are required to perform full load only tasks. Note that
AWS DMS does not create the `dms_user` login. For information about
creating a login for SQL Server, see [Create a database user](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/create-a-database-user?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/create-a-database-user?view=sql-server-ver16") topic in _Microsoft's
documentation_.

```
USE db_name;

                CREATE USER dms_user FOR LOGIN dms_user;
                ALTER ROLE [db_datareader] ADD MEMBER dms_user;
                GRANT VIEW DATABASE STATE to dms_user;
                GRANT VIEW DEFINITION to dms_user;

                USE master;

                GRANT VIEW SERVER STATE TO dms_user;
```

### Permissions for tasks with ongoing replication

Self-managed SQL Server instances can be configured for ongoing replication using DMS with or without
using the `sysadmin` role. For SQL Server instances, where you can't grant the `sysadmin` role,
ensure that the DMS user has the privileges described as follows.

###### Set up permissions for ongoing replication from a self-managed SQL Server database

1. Create a new SQL Server account with password authentication using SQL Server Management Studio (SSMS)
   or as described previously in [Permissions for full load only
   tasks](#CHAP_Source.SQLServer.Permissions.FullLoad "#CHAP_Source.SQLServer.Permissions.FullLoad"), for example, `self_managed_user`.
2. Run the following `GRANT` commands:

```
GRANT VIEW SERVER STATE TO `self_managed_user`;

USE msdb;
    GRANT SELECT ON msdb.dbo.backupset TO `self_managed_user`;
    GRANT SELECT ON msdb.dbo.backupmediafamily TO `self_managed_user`;
    GRANT SELECT ON msdb.dbo.backupfile TO `self_managed_user`;

USE db_name;
    CREATE USER `self_managed_user` FOR LOGIN `self_managed_user`;
    ALTER ROLE [db_owner] ADD MEMBER `self_managed_user`;
    GRANT VIEW DEFINITION to `self_managed_user`;
```

3. In addition to the preceding permissions, the user needs one of the following:
   - The user must be a member of the `sysadmin` fixed server role
   - Configurations and permissions as described in [Setting up ongoing replication
     on a SQL Server in an availability group environment: Without sysadmin role](CHAP_Source.SQLServer.md#CHAP_SupportScripts.SQLServer.ag "CHAP_Source.SQLServer.md#CHAP_SupportScripts.SQLServer.ag") or
     [Setting up ongoing replication
     on a standalone SQL Server: Without sysadmin role](CHAP_Source.SQLServer.md#CHAP_SupportScripts.SQLServer.standalone "CHAP_Source.SQLServer.md#CHAP_SupportScripts.SQLServer.standalone"),
     depending on your source configuration.

#### Set up permissions for ongoing replication

from a cloud SQL Server database

A cloud-hosted SQL server instance is an instance running on Amazon RDS for Microsoft SQL Server, an Azure SQL Managed Instance,
or any other managed cloud SQL Server instance supported by DMS.

Create a new SQL Server account with password authentication using SQL Server Management Studio (SSMS) or
as described previously in [Permissions for full load only
tasks](#CHAP_Source.SQLServer.Permissions.FullLoad "#CHAP_Source.SQLServer.Permissions.FullLoad"), for example, `rds_user`.

Run the following grant commands.

```
GRANT VIEW SERVER STATE TO rds_user;
```

For Amazon RDS for Microsoft SQL Server sources, DMS version 3.5.3 and above support reading from transaction
log backups. To ensure that DMS is able to access the log backups, in addition to the above,
either grant `master` user privileges, or the following privileges on an RDS SQL Server source:

```

USE msdb;
    GRANT EXEC ON msdb.dbo.rds_dms_tlog_download TO rds_user;
    GRANT EXEC ON msdb.dbo.rds_dms_tlog_read TO rds_user;
    GRANT EXEC ON msdb.dbo.rds_dms_tlog_list_current_lsn TO rds_user;
    GRANT EXEC ON msdb.dbo.rds_task_status TO rds_user;

USE db_name;
    CREATE USER rds_user FOR LOGIN rds_user;
    ALTER ROLE [db_owner] ADD MEMBER rds_user;
    GRANT VIEW DEFINITION to rds_user;
```

For Amazon Azure SQL Managed Instances grant the following privileges:

```
GRANT SELECT ON msdb.dbo.backupset TO rds_user;
GRANT SELECT ON msdb.dbo.backupmediafamily TO rds_user;
GRANT SELECT ON msdb.dbo.backupfile TO rds_user;
```

## Prerequisites for using ongoing

replication (CDC) from a SQL Server source

You can use ongoing replication (change data capture, or CDC) for a self-managed
SQL Server database on-premises or on Amazon EC2, or a cloud database such as Amazon RDS or a
Microsoft Azure SQL managed instance.

The following requirements apply specifically when using ongoing replication with
a SQL Server database as a source for AWS DMS:

- SQL Server must be configured for full backups, and you must perform a
  backup before beginning to replicate data.
- The recovery model must be set to **Bulk logged** or
  **Full**.
- SQL Server backup to multiple disks isn't supported. If the backup is
  defined to write the database backup to multiple files over different disks,
  AWS DMS can't read the data and the AWS DMS task fails.
- For self-managed SQL Server sources, SQL Server Replication Publisher
  definitions for the source used in a DMS CDC task aren't removed when
  you remove the task. A SQL Server system administrator must delete these
  definitions from SQL Server for self-managed sources.
- During CDC, AWS DMS needs to look up SQL Server transaction log backups to
  read changes. AWS DMS doesn't support SQL Server transaction log backups
  created using third-party backup software that*aren't* in native format. To support transaction log
  backups that _are_ in native format and
  created using third-party backup software, add the
  `use3rdPartyBackupDevice=Y` connection attribute to the
  source endpoint.
- For self-managed SQL Server sources, be aware that SQL Server doesn't
  capture changes on newly created tables until they've been published.
  When tables are added to a SQL Server source, AWS DMS manages creating the
  publication. However, this process might take several minutes. Operations
  made to newly created tables during this delay aren't captured or
  replicated to the target.
- AWS DMS change data capture requires full transaction logging to be turned on in SQL
  Server. To turn on full transaction logging in SQL Server, either enable MS-REPLICATION
  or CHANGE DATA CAPTURE (CDC).
- SQL Server _tlog_ entries won't be marked for re-use until the MS CDC
  capture job processes those changes.
- CDC operations aren't supported on memory-optimized tables. This
  limitation applies to SQL Server 2014 (when the feature was first
  introduced) and higher.
- AWS DMS change data capture requires a distribution database by default on Amazon EC2 or On-Prem SQL server as source.
  So, ensure that you have activated the distributor while configuring MS replication for tables with primary keys.

## Supported compression

methods for SQL Server

Note the following about support for SQL Server compression methods in AWS DMS:

- AWS DMS supports Row/Page compression in SQL Server version 2008 and later.
- AWS DMS doesn't support the Vardecimal storage format.
- AWS DMS doesn't support sparse columns and columnar structure compression.

## Working with self-managed SQL Server AlwaysOn

availability groups

SQL Server Always On availability groups provide high availability and disaster
recovery as an enterprise-level alternative to database mirroring.

In AWS DMS, you can migrate changes from a single primary or secondary availability
group replica.

### Working with the primary availability group

replica

###### To use the primary availability group as a source in AWS DMS, do the following:

1. Turn on the distribution option for all SQL Server instances in your
   availability replicas. For more information, see [Setting up ongoing replication
   on a self-managed SQL Server](CHAP_Source.SQLServer.md#CHAP_Source.SQLServer.CDC.MSCDC "CHAP_Source.SQLServer.md#CHAP_Source.SQLServer.CDC.MSCDC").
2. In the AWS DMS console, open the SQL Server source database settings. For
   **Server Name**, specify the Domain Name Service (DNS)
   name or IP address that was configured for your availability group listener.

When you start an AWS DMS task for the first time, it might take longer than usual
to start. This slowness occurs because the creation of the table articles is being
duplicated by the availability group server.

### Working with a secondary availability

group replica

###### To use a secondary availability group as a source in AWS DMS, do the

following:

1. Use the same credentials for connecting to individual replicas as those used by the AWS DMS source endpoint user.
2. Ensure that your AWS DMS replication instance can resolve DNS names for
   all existing replicas, and connect to them. You can use the following SQL
   query to get DNS names for all of your replicas.

```
select ar.replica_server_name, ar.endpoint_url from sys.availability_replicas ar
JOIN sys.availability_databases_cluster adc
ON adc.group_id = ar.group_id AND adc.database_name = '<source_database_name>';
```

3. When you create the source endpoint, specify the DNS name of the
   availability group listener for the endpoint's **Server
   name** or for the endpoint secret's **Server
   address**. For more information about availability group
   listeners, see [What is an availability group listener?](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/availability-group-listener-overview?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/availability-group-listener-overview?view=sql-server-ver15") in the SQL Server documentation.

You can use either a public DNS server or an on-premises DNS server to
resolve the availability group listener, the primary replica, and the
secondary replicas. To use an on-premises DNS server, configure the
Amazon Route 53 Resolver. For more information, see [Using your own on-premises name server](CHAP_BestPractices.md#CHAP_BestPractices.Rte53DNSResolver "CHAP_BestPractices.md#CHAP_BestPractices.Rte53DNSResolver"). 4. Add the following extra connection attributes to your source endpoint.

| Extra connection attribute             | Value      | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `applicationIntent`                    | `ReadOnly` | Without this ODBC setting, the replication task is<br>routed to the primary availability group replica. For more<br>information, see [SQL Server Native Client Support for High<br>Availability, Disaster Recovery](https://docs.microsoft.com/en-us/sql/relational-databases/native-client/features/sql-server-native-client-support-for-high-availability-disaster-recovery?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/native-client/features/sql-server-native-client-support-for-high-availability-disaster-recovery?view=sql-server-ver15") in the SQL Server documentation. |
| `multiSubnetFailover`                  | `yes`      | For more information, see [SQL Server Native Client Support for High<br>Availability, Disaster Recovery](https://docs.microsoft.com/en-us/sql/relational-databases/native-client/features/sql-server-native-client-support-for-high-availability-disaster-recovery?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/native-client/features/sql-server-native-client-support-for-high-availability-disaster-recovery?view=sql-server-ver15") in the SQL Server<br>documentation.                                                                                                         |
| `alwaysOnSharedSynchedBackupIsEnabled` | `false`    | For more information, see [Endpoint settings<br>when using SQL Server as a source for AWS DMS](#CHAP_Source.SQLServer.ConnectionAttrib "#CHAP_Source.SQLServer.ConnectionAttrib").                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `activateSafeguard`                    | `false`    | For more information, see [Limitations](#CHAP_Source.SQLServer.AlwaysOn.Secondary.limitations "#CHAP_Source.SQLServer.AlwaysOn.Secondary.limitations") following.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `setUpMsCdcForTables`                  | `false`    | For more information, see [Limitations](#CHAP_Source.SQLServer.AlwaysOn.Secondary.limitations "#CHAP_Source.SQLServer.AlwaysOn.Secondary.limitations") following.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

5. Enable the distribution option on all replicas in your availability group. Add all nodes to
   the distributors list. For more information, see [To set up distribution](CHAP_Source.SQLServer.md#CHAP_Source.SQLServer.CDC.MSCDC.Setup "CHAP_Source.SQLServer.md#CHAP_Source.SQLServer.CDC.MSCDC.Setup").
6. Run the following query on the primary read-write replica to enable publication of your
   database. You run this query only once for your database.

```
sp_replicationdboption @dbname = N'<source DB name>', @optname = N'publish', @value = N'true';
```

#### Limitations

Following are limitations for working with a secondary availability group
replica:

- AWS DMS doesn't support Safeguard when using a read-only availability group replica as a source.
  For more information, see [Endpoint settings
  when using SQL Server as a source for AWS DMS](#CHAP_Source.SQLServer.ConnectionAttrib "#CHAP_Source.SQLServer.ConnectionAttrib").
- AWS DMS doesn't support the `setUpMsCdcForTables` extra connection attribute when
  using a read-only availability group replica as a source. For more
  information, see [Endpoint settings
  when using SQL Server as a source for AWS DMS](#CHAP_Source.SQLServer.ConnectionAttrib "#CHAP_Source.SQLServer.ConnectionAttrib").
- AWS DMS can use a self-managed secondary availability group replica as a source database for
  ongoing replication (change data capture, or CDC) starting from version 3.4.7.
  Cloud SQL Server Multi-AZ read replicas are not supported.
  If you use previous versions of AWS DMS, make sure that you use the primary
  availability group replica as a source database for CDC.

#### Failover to other nodes

If you set the `ApplicationIntent` extra connection attribute
for your endpoint to `ReadOnly`, your AWS DMS task connects to the
read-only node with the highest read-only routing priority. It then fails over
to other read-only nodes in your availability group when the highest priority
read-only node is unavailable. If you don't set `ApplicationIntent`,
your AWS DMS task only connects to the primary (read/write) node in your
availability group.

## Endpoint settings

when using SQL Server as a source for AWS DMS

You can use endpoint settings to configure your SQL Server source database similar to using
extra connection attributes. You specify the settings when you create the source
endpoint using the AWS DMS console, or by using the `create-endpoint` command in the
[AWS CLI](../../../cli/latest/reference/dms/index.md "../../../cli/latest/reference/dms/index.md"), with the
`--microsoft-sql-server-settings '{"`EndpointSetting"`:
 `"value"`, `...`}'` JSON syntax.

The following table shows the endpoint settings that you can use with
SQL Server as a source.

| Name                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ActivateSafeguard`                    | This attribute turns Safeguard on or off. For information<br>about Safeguard, see `SafeguardPolicy` following.<br>Default value:<br>`true`<br>Valid values: {`false`,<br>`true`}<br>Example: `'{"ActivateSafeguard": true}'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `AlwaysOnSharedSynchedBackupIsEnabled` | This attribute adjusts the behavior of AWS DMS when migrating<br>from an SQL Server source database that is hosted as part of an<br>Always On availability group cluster.<br>AWS DMS has enhanced support for SQL Server source databases<br>that are configured to run in an Always On cluster. In this case,<br>AWS DMS attempts to track if transaction backups are happening from<br>nodes in the Always On cluster other than the node where the source<br>database instance is hosted. At migration task start-up, AWS DMS tries<br>to connect to each node in the cluster, but fails if it can't<br>connect to any one of the nodes.<br>If you need AWS DMS to poll all the nodes in the Always On<br>cluster for transaction backups, set this attribute to<br>`false`.<br>Default value: `true`<br>Valid values: `true` or `false`<br>Example: `'{"AlwaysOnSharedSynchedBackupIsEnabled": false}'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `"ApplicationIntent": "readonly"`      | This ODBC driver attribute setting causes SQL Server to route your replication task to the<br>highest priority read-only node. Without this setting, SQL Server<br>routes your replication task to the primary read-write node.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `ConnectionTimeout`                    | Use this extra connection attribute (ECA) to set the endpoint<br>connection timeout for the SQL Server instance, in seconds. The<br>default value is 10 seconds. ECA Example:<br>`ConnectionTimeout=30`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `EnableNonSysadminWrapper`             | Use this endpoint setting when you are setting up ongoing replication on a standalone<br>SQL server without a sysadmin user. This parameter is supported on AWS DMS version 3.4.7<br>and higher. For information about setting up ongoing replication<br>on a standalone SQL server, see [Capturing data changes for ongoing replication from SQL Server](CHAP_Source.SQLServer.md "CHAP_Source.SQLServer.md").<br>Default value:<br>`false`<br>Valid values: `true`, `false`<br>Example: `'{"EnableNonSysadminWrapper": true}'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `ExecuteTimeout`                       | Use this extra connection attribute (ECA) to set the client statement timeout for the<br>SQL Server instance, in seconds. The default value is 60<br>seconds.<br>Example: `'{"ExecuteTimeout": 100}'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `FatalOnSimpleModel`                   | When set to `true`, this setting generates a fatal error when SQL Server database<br>recovery model is set to `simple`.<br>Default value: `false`<br>Valid values: `true` or `false`<br>Example: `'{"FatalOnSimpleModel": true}'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `ForceLobLookup`                       | Forces LOB lookup on inline LOB.<br>Default value:<br>`false`<br>Valid values: `true`, `false`<br>Example: `'{"ForceLobLookup": false}'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `"MultiSubnetFailover": "Yes"`         | This ODBC driver attribute helps DMS to connect to the new primary in case of an Availability<br>Group failover. This attribute is designed for situations<br>when the connection is broken or the listener IP<br>address is incorrect. In these situations, AWS DMS attempts<br>to connect to all IP addresses associated with the Availability<br>Group listener.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `ReadBackupOnly`                       | Use of this attribute requires \*_sysadmin_<br>• privileges. When this<br>attribute is set to `true`, during ongoing replication<br>AWS DMS reads changes only from transaction log backups and<br>doesn't read from the active transaction log file. Setting this<br>parameter to `true` enables you to control active<br>transaction log file growth during full load and ongoing replication<br>tasks. However, it can add some source latency to ongoing<br>replication.<br>Valid values: `true` or `true`. The<br>default is `false`.<br>Example: `'{"ReadBackupOnly": true}'`<br>NoteThis parameter does not work on Amazon RDS SQL Server source<br>instances because of the way RDS performs backups.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `SafeguardPolicy`                      | For optimal performance, AWS DMS tries to capture all unread<br>changes from the active transaction log (TLOG). However,<br>sometimes due to truncation, the active TLOG might not contain<br>all the unread changes. When this occurs, AWS DMS accesses the<br>log backup to capture the missing changes. To minimize the need<br>to access the log backup, AWS DMS prevents truncation using one of<br>the following methods:<br>1. `RELY_ON_SQL_SERVER_REPLICATION_AGENT`<br>(**Start transactions in the database)**:<br>This is the default for AWS DMS.<br>When you use this setting, AWS DMS<br>requires that the SQL Server Log Reader Agent be running, so that<br>AWS DMS can move transactions that are marked for replication from the<br>active TLOG. Note that if the Log Reader Agent is not running,<br>the active TLOG can become full, causing the source database to switch<br>to read-only mode until you can resolve the issue. If<br>you need to enable Microsoft Replication in your database for a purpose<br>other than AWS DMS,<br>then you must choose this setting.<br>When you use this setting, AWS DMS minimizes log backup reads by creating<br>a table called `awsdms_truncation_safeguard` and prevents TLOG<br>truncation by mimicking an open transaction in the database. This keeps the database<br>from truncating events and moving them to the backup log for five minutes (by default).<br>Make sure that the table is not included in any maintenance plan, as it may cause the<br>maintenance job to fail. You can safely delete the table if there are no tasks configured<br>with the `Start Transactions` database option.<br>2. `EXCLUSIVE_AUTOMATIC_TRUNCATION` **(Exclusively use `sp_repldone`<br>with a single task)**: When you use this setting, AWS DMS has full control of the replication agent<br>process that marks log entries as `ready for truncation` using `sp_repldone`.<br>With this setting, AWS DMS doesn't use a dummy transaction as with the<br>`RELY_ON_SQL_SERVER_REPLICATION_AGENT` (default) setting. You can only use this setting<br>when MS Replication is not used for any other purpose other than AWS DMS on the source database.<br>Also, when using this setting, only one AWS DMS task can access the database.<br>If you need to run parallel AWS DMS tasks against the same database, use `RELY_ON_SQL_SERVER_REPLICATION_AGENT`.<br>• This setting requires that the Log Reader Agent be stopped in the database. If the Log Reader<br>Agent is running when the task starts, the AWS DMS task will force it to stop. Alternatively, you can<br>stop the Log Reader Agent manually before starting the task.<br>• When using this method with MS-CDC, you should stop and disable the **MS-CDC capture**<br>and **MS-CDC cleanup\*<br>• jobs.<br>• You can't use this setting when the **Microsoft SQL Server Migration\*\* job<br>runs on a remote Distributor machine, because AWS DMS doesn't have access to the remote machine.<br>• `EXCLUSIVE_AUTOMATIC_TRUNCATION` doesn't work on Amazon RDS for SQL Server source instances<br>because Amazon RDS users don't have access to run the `sp_repldone` stored procedure.<br>• If you set `SafeguardPolicy` to `EXCLUSIVE_AUTOMATIC_TRUNCATION` without<br>using the sysadmin role, you must grant permissions on the `dbo.syscategories` and<br>`dbo.sysjobs` objects to the `dmsuser` user.<br>Default value:<br>`RELY_ON_SQL_SERVER_REPLICATION_AGENT`<br>Valid values: {`EXCLUSIVE_AUTOMATIC_TRUNCATION`,<br>`RELY_ON_SQL_SERVER_REPLICATION_AGENT`}<br>Example: `'{"SafeguardPolicy": "EXCLUSIVE_AUTOMATIC_TRUNCATION"}'` |
| `SetUpMsCdcForTables`                  | This attribute turns on MS-CDC for the source database and for tables in<br>the task mapping that don't have MS-Replication enabled. Setting this value to<br>`true` runs the `sp_cdc_enable_db` stored procedure on the source<br>database, and runs the `sp_cdc_enable_table` stored procedure on each table<br>in the task that doesn't have MS-Replication enabled in the source database.<br>For more information<br>about turning on distribution, see [Setting up ongoing replication<br>on a self-managed SQL Server](CHAP_Source.SQLServer.md#CHAP_Source.SQLServer.CDC.MSCDC "CHAP_Source.SQLServer.md#CHAP_Source.SQLServer.CDC.MSCDC").<br>Valid values: {`true`,<br>`false`}<br>Example: `'{"SetUpMsCdcForTables": true}'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `TlogAccessMode`                       | Indicates the mode used to fetch CDC data.<br>Default value:<br>`PreferTlog`<br>Valid values: `BackupOnly`,<br>`PreferBackup`, `PreferTlog`, `TlogOnly`<br>Example: `'{"TlogAccessMode": "PreferTlog"}'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `Use3rdPartyBackupDevice`              | When this attribute is set to `Y`, AWS DMS<br>processes third-party transaction log backups if they are<br>created in native format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Source data types for SQL

Server

Data migration that uses SQL Server as a source for AWS DMS supports most SQL Server
data types. The following table shows the SQL Server source data types that are
supported when using AWS DMS and the default mapping from AWS DMS data types.

For information on how to view the data type that is mapped in the target, see the
section for the target endpoint you are using.

For additional information about AWS DMS data types, see [Data types for AWS Database Migration Service](CHAP_Reference.md "CHAP_Reference.md").

| SQL Server data types                  | AWS DMS data types                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BIGINT                                 | INT8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| BIT                                    | BOOLEAN                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DECIMAL                                | NUMERIC                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| INT                                    | INT4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| MONEY                                  | NUMERIC                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| NUMERIC (p,s)                          | NUMERIC                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| SMALLINT                               | INT2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| SMALLMONEY                             | NUMERIC                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| TINYINT                                | UINT1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| REAL                                   | REAL4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| FLOAT                                  | REAL8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| DATETIME                               | DATETIME                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DATETIME2 (SQL Server 2008 and higher) | DATETIME                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| SMALLDATETIME                          | DATETIME                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DATE                                   | DATE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| TIME                                   | TIME                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| DATETIMEOFFSET                         | WSTRING                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| CHAR                                   | STRING                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| VARCHAR                                | STRING                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| VARCHAR (max)                          | CLOB<br>TEXT<br>To use this data type with AWS DMS, you must enable the use of<br>CLOB data types for a specific task.<br>For SQL Server tables, AWS DMS updates LOB columns in the target<br>even for UPDATE statements that don't change the value of<br>the LOB column in SQL Server.<br>During CDC, AWS DMS supports CLOB data types only in tables that<br>include a primary key.                                                                                                                                                        |
| NCHAR                                  | WSTRING                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| NVARCHAR (length)                      | WSTRING                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| NVARCHAR (max)                         | NCLOB<br>NTEXT<br>To use this data type with AWS DMS, you must enable the use of<br>SupportLobs for a specific task. For more information about<br>enabling Lob support, see [Setting LOB support for source databases in<br>an AWS DMS task](CHAP_Tasks.md "CHAP_Tasks.md").<br>For SQL Server tables, AWS DMS updates LOB columns in the target<br>even for UPDATE statements that don't change the value of<br>the LOB column in SQL Server.<br>During CDC, AWS DMS supports CLOB data types only in tables that<br>include a primary key. |
| BINARY                                 | BYTES                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| VARBINARY                              | BYTES                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| VARBINARY (max)                        | BLOB<br>IMAGE<br>For SQL Server tables, AWS DMS updates LOB columns in the target<br>even for UPDATE statements that don't change the value of<br>the LOB column in SQL Server.<br>To use this data type with AWS DMS, you must enable the use of<br>BLOB data types for a specific task.<br>AWS DMS supports BLOB data types only in tables that include a<br>primary key.                                                                                                                                                                   |
| TIMESTAMP                              | BYTES                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| UNIQUEIDENTIFIER                       | STRING                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| HIERARCHYID                            | Use HIERARCHYID when replicating to a SQL Server target<br>endpoint.<br>Use WSTRING (250) when replicating to all other target<br>endpoints.                                                                                                                                                                                                                                                                                                                                                                                                  |
| XML                                    | NCLOB<br>For SQL Server tables, AWS DMS updates LOB columns in the target<br>even for UPDATE statements that don't change the value of<br>the LOB column in SQL Server.<br>To use this data type with AWS DMS, you must enable the use of<br>NCLOB data types for a specific task.<br>During CDC, AWS DMS supports NCLOB data types only in tables<br>that include a primary key.                                                                                                                                                             |
| GEOMETRY                               | Use GEOMETRY when replicating to target endpoints that support<br>this data type.<br>Use CLOB when replicating to target endpoints that don't<br>support this data type.                                                                                                                                                                                                                                                                                                                                                                      |
| GEOGRAPHY                              | Use GEOGRAPHY when replicating to target endpoints that<br>support this data type.<br>Use CLOB when replicating to target endpoints that don't<br>support this data type.                                                                                                                                                                                                                                                                                                                                                                     |

AWS DMS doesn't support tables that include fields with the following data
types.

- CURSOR
- SQL_VARIANT
- TABLE

###### Note

User-defined data types are supported according to their base type. For
example, a user-defined data type based on DATETIME is handled as a DATETIME
data type.
