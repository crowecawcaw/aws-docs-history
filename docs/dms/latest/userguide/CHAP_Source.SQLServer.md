# Capturing data changes for ongoing replication from SQL Server

This topic describes how to set up CDC replication on a SQL Server source.

###### Topics

- [Capturing data changes for self-managed
  SQL Server on-premises or on Amazon EC2](#CHAP_Source.SQLServer.CDC.Selfmanaged "#CHAP_Source.SQLServer.CDC.Selfmanaged")
- [Setting up ongoing replication
  on a cloud SQL Server DB instance](#CHAP_Source.SQLServer.Configuration "#CHAP_Source.SQLServer.Configuration")

## Capturing data changes for self-managed

SQL Server on-premises or on Amazon EC2

To capture changes from a source Microsoft SQL Server database, make sure that the database
is configured for full backups. Configure the database either in full recovery mode
or bulk-logged mode.

For a self-managed SQL Server source, AWS DMS uses the following:

**MS-Replication**

To capture changes for tables with primary keys. You can configure
this automatically by giving sysadmin privileges to the AWS DMS endpoint
user on the source SQL Server instance. Or you can follow the steps in
this section to prepare the source and use a user that doesn't have
sysadmin privileges for the AWS DMS endpoint.

**MS-CDC**

To capture changes for tables without primary keys. Enable MS-CDC at
the database level and for all of the tables individually.

When setting up a SQL Server database for ongoing replication (CDC), you can do
one of the following:

- Set up ongoing replication using the sysadmin role.
- Set up ongoing replication to not use the sysadmin role.

###### Note

You can use the following script to find all table without a primary or a unique
key:

```
USE [DBname]
SELECT SCHEMA_NAME(schema_id) AS schema_name, name AS table_name
FROM sys.tables
WHERE OBJECTPROPERTY(object_id, 'TableHasPrimaryKey') = 0
        AND  OBJECTPROPERTY(object_id, 'TableHasUniqueCnst') = 0
ORDER BY schema_name, table_name;
```

### Setting up ongoing replication

on a self-managed SQL Server

This section contains information about setting up ongoing replication on a self-managed
SQL server with or without using the sysadmin role.

###### Topics

- [Setting up ongoing replication
  on a self-managed SQL Server: Using sysadmin role](#CHAP_Source.SQLServer.CDC.MSCDC.Sysadmin "#CHAP_Source.SQLServer.CDC.MSCDC.Sysadmin")
- [Setting up ongoing replication
  on a standalone SQL Server: Without sysadmin role](#CHAP_SupportScripts.SQLServer.standalone "#CHAP_SupportScripts.SQLServer.standalone")
- [Setting up ongoing replication
  on a SQL Server in an availability group environment: Without sysadmin role](#CHAP_SupportScripts.SQLServer.ag "#CHAP_SupportScripts.SQLServer.ag")

#### Setting up ongoing replication

on a self-managed SQL Server: Using sysadmin role

AWS DMS ongoing replication for SQL Server uses native SQL Server replication
for tables with primary keys, and change data capture (CDC) for tables without
primary keys.

Before setting up ongoing replication, see [Prerequisites for using ongoing
replication (CDC) from a SQL Server source](CHAP_Source.md#CHAP_Source.SQLServer.Prerequisites "CHAP_Source.md#CHAP_Source.SQLServer.Prerequisites").

For tables with primary keys, AWS DMS can generally configure the required
artifacts on the source. However, for SQL Server source instances that are
self-managed, make sure to first configure the SQL Server distribution manually.
After you do so, AWS DMS source users with sysadmin permission can automatically
create the publication for tables with primary keys.

To check if distribution has already been configured, run the following
command.

```
sp_get_distributor
```

If the result is `NULL` for column distribution, distribution
isn't configured. You can use the following procedure to set up
distribution.

###### To set up distribution

1. Connect to your SQL Server source database using the SQL Server
   Management Studio (SSMS) tool.
2. Open the context (right-click) menu for the **Replication** folder, and choose **Configure Distribution**. The Configure Distribution
   wizard appears.
3. Follow the wizard to enter the default values and create the
   distribution.

###### To set up CDC

AWS DMS version 3.4.7 and greater can set up MS CDC for your database and
all of your tables automatically if you aren't using a read-only replica.
To use this feature, set the `SetUpMsCdcForTables` ECA to true. For information
about ECAs, see [Endpoint settings](CHAP_Source.md#CHAP_Source.SQLServer.ConnectionAttrib "CHAP_Source.md#CHAP_Source.SQLServer.ConnectionAttrib").

For versions of AWS DMS earlier than 3.4.7, or for a read-only replica as a source, perform the following steps:

1. For tables without primary keys, set up MS-CDC for the database. To do so, use
   an account that has the sysadmin role assigned to it, and run the following
   command.

```
use [DBname]
EXEC sys.sp_cdc_enable_db
```

2. Next, set up MS-CDC for each of the source tables. For each table with unique
   keys but no primary key, run the following query to set up MS-CDC.

```
exec sys.sp_cdc_enable_table
@source_schema = N'schema_name',
@source_name = N'table_name',
@index_name = N'unique_index_name',
@role_name = NULL,
@supports_net_changes = 1
GO
```

3. For each table with no primary key or no unique keys, run the following query
   to set up MS-CDC.

```
exec sys.sp_cdc_enable_table
@source_schema = N'schema_name',
@source_name = N'table_name',
@role_name = NULL
GO
```

For more information on setting up MS-CDC for specific tables, see the [SQL Server
documentation](https://msdn.microsoft.com/en-us/library/cc627369.aspx "https://msdn.microsoft.com/en-us/library/cc627369.aspx").

#### Setting up ongoing replication

on a standalone SQL Server: Without sysadmin role

This section describes how to set up ongoing replication for a standalone SQL Server database source that
doesn't require the user account to have sysadmin privileges.

###### Note

After running the steps in this section, the non-sysadmin DMS user will have permissions
to do the following:

- Read changes from the online transactions log file
- Disk access to read changes from transactional log backup files
- Add or alter the publication which DMS uses
- Add articles to the publication

1. Set up Microsoft SQL Server for Replication as described in
   [Capturing data changes for ongoing replication from SQL Server](CHAP_Source.SQLServer.md "CHAP_Source.SQLServer.md").
2. Enable MS-REPLICATION on the source database. This can either be done manually or by running the task once as a sysadmin user.
3. Create the `awsdms` schema on the source database using the following script:

```
use master
go
create schema awsdms
go


-- Create the table valued function [awsdms].[split_partition_list] on the Master database, as follows:
USE [master]
GO

set ansi_nulls on
go

set quoted_identifier on
go

if (object_id('[awsdms].[split_partition_list]','TF')) is not null

drop function [awsdms].[split_partition_list];

go

create function [awsdms].[split_partition_list]

(

@plist varchar(8000), --A delimited list of partitions

@dlm nvarchar(1) --Delimiting character

)

returns @partitionsTable table --Table holding the BIGINT values of the string fragments

(

pid bigint primary key

)

as

begin

declare @partition_id bigint;

declare @dlm_pos integer;

declare @dlm_len integer;

set @dlm_len = len(@dlm);

while (charindex(@dlm,@plist)>0)

begin

set @dlm_pos = charindex(@dlm,@plist);

set @partition_id = cast( ltrim(rtrim(substring(@plist,1,@dlm_pos-1))) as bigint);

insert into @partitionsTable (pid) values (@partition_id)

set @plist = substring(@plist,@dlm_pos+@dlm_len,len(@plist));

end

set @partition_id = cast (ltrim(rtrim(@plist)) as bigint);

insert into @partitionsTable (pid) values ( @partition_id );

return

end

GO
```

4. Create the `[awsdms].[rtm_dump_dblog]` procedure on the Master database
   using the following script:

```
use [MASTER]

go

if (object_id('[awsdms].[rtm_dump_dblog]','P')) is not null drop procedure [awsdms].[rtm_dump_dblog];
go


set ansi_nulls on
go

set quoted_identifier on
GO



CREATE procedure [awsdms].[rtm_dump_dblog]

(

@start_lsn varchar(32),

@seqno integer,

@filename varchar(260),

@partition_list varchar(8000), -- A comma delimited list: P1,P2,... Pn

@programmed_filtering integer,

@minPartition bigint,

@maxPartition bigint

)

as begin

declare @start_lsn_cmp varchar(32); -- Stands against the GT comparator

SET NOCOUNT ON -- – Disable "rows affected display"

set @start_lsn_cmp = @start_lsn;

if (@start_lsn_cmp) is null

set @start_lsn_cmp = '00000000:00000000:0000';

if (@partition_list is null)

begin

RAISERROR ('Null partition list waspassed',16,1);

return

end

if (@start_lsn) is not null

set @start_lsn = '0x'+@start_lsn;

if (@programmed_filtering=0)



SELECT

[Current LSN],

[operation],

[Context],

[Transaction ID],

[Transaction Name],

[Begin Time],

[End Time],

[Flag Bits],

[PartitionID],

[Page ID],

[Slot ID],

[RowLog Contents 0],

[Log Record],

[RowLog Contents 1]

FROM

fn_dump_dblog (

@start_lsn, NULL, N'DISK', @seqno, @filename,

default, default, default, default, default, default, default,

default, default, default, default, default, default, default,

default, default, default, default, default, default, default,

default, default, default, default, default, default, default,

default, default, default, default, default, default, default,

default, default, default, default, default, default, default,

default, default, default, default, default, default, default,

default, default, default, default, default, default, default,

default, default, default, default, default, default, default)

where [Current LSN] collate SQL_Latin1_General_CP1_CI_AS > @start_lsn_cmp collate SQL_Latin1_General_CP1_CI_AS

and

(

( [operation] in ('LOP_BEGIN_XACT','LOP_COMMIT_XACT','LOP_ABORT_XACT') )

or

( [operation] in ('LOP_INSERT_ROWS','LOP_DELETE_ROWS','LOP_MODIFY_ROW')

and

( ( [context] in ('LCX_HEAP','LCX_CLUSTERED','LCX_MARK_AS_GHOST') ) or ([context] = 'LCX_TEXT_MIX' and (datalength([RowLog Contents 0]) in (0,1))))

and [PartitionID] in ( select * from master.awsdms.split_partition_list (@partition_list,','))

)

or

([operation] = 'LOP_HOBT_DDL')

)


else


SELECT

[Current LSN],

[operation],

[Context],

[Transaction ID],

[Transaction Name],

[Begin Time],

[End Time],

[Flag Bits],

[PartitionID],

[Page ID],

[Slot ID],

[RowLog Contents 0],

[Log Record],

[RowLog Contents 1] -- After Image

FROM

fn_dump_dblog (

@start_lsn, NULL, N'DISK', @seqno, @filename,

default, default, default, default, default, default, default,

default, default, default, default, default, default, default,

default, default, default, default, default, default, default,

default, default, default, default, default, default, default,

default, default, default, default, default, default, default,

default, default, default, default, default, default, default,

default, default, default, default, default, default, default,

default, default, default, default, default, default, default,

default, default, default, default, default, default, default)

where [Current LSN] collate SQL_Latin1_General_CP1_CI_AS > @start_lsn_cmp collate SQL_Latin1_General_CP1_CI_AS

and

(

( [operation] in ('LOP_BEGIN_XACT','LOP_COMMIT_XACT','LOP_ABORT_XACT') )

or

( [operation] in ('LOP_INSERT_ROWS','LOP_DELETE_ROWS','LOP_MODIFY_ROW')

and

( ( [context] in ('LCX_HEAP','LCX_CLUSTERED','LCX_MARK_AS_GHOST') ) or ([context] = 'LCX_TEXT_MIX' and (datalength([RowLog Contents 0]) in (0,1))))

and ([PartitionID] is not null) and ([PartitionID] >= @minPartition and [PartitionID]<=@maxPartition)

)

or

([operation] = 'LOP_HOBT_DDL')

)



SET NOCOUNT OFF -- Re-enable "rows affected display"

end

GO
```

5. Create the certificate on the Master database using the following script:

```
Use [master]
Go

CREATE CERTIFICATE [awsdms_rtm_dump_dblog_cert] ENCRYPTION BY PASSWORD = N'@5trongpassword'

WITH SUBJECT = N'Certificate for FN_DUMP_DBLOG Permissions';
```

6. Create the login from the certificate using the following script:

```
Use [master]
Go

CREATE LOGIN awsdms_rtm_dump_dblog_login FROM CERTIFICATE [awsdms_rtm_dump_dblog_cert];
```

7. Add the login to the sysadmin server role using the following script:

```
ALTER SERVER ROLE [sysadmin] ADD MEMBER [awsdms_rtm_dump_dblog_login];
```

8. Add the signature to [master].[awsdms].[rtm\_dump\_dblog] using the certificate, using
   the following script:

```
Use [master]
GO
ADD SIGNATURE
TO [master].[awsdms].[rtm_dump_dblog] BY CERTIFICATE [awsdms_rtm_dump_dblog_cert] WITH PASSWORD = '@5trongpassword';
```

###### Note

If you recreate the stored procedure, you need to add the signature again. 9. Create the [awsdms].[rtm\_position\_1st\_timestamp] on the Master database using the following
script:

```
use [master]
    if object_id('[awsdms].[rtm_position_1st_timestamp]','P') is not null
    DROP PROCEDURE [awsdms].[rtm_position_1st_timestamp];
    go
    create procedure [awsdms].[rtm_position_1st_timestamp]
    (
    @dbname                sysname,      -- Database name
    @seqno                 integer,      -- Backup set sequence/position number within file
    @filename              varchar(260), -- The backup filename
    @1stTimeStamp          varchar(40)   -- The timestamp to position by
    )
    as begin

    SET NOCOUNT ON       -- Disable "rows affected display"

    declare @firstMatching table
    (
    cLsn varchar(32),
    bTim datetime
    )

    declare @sql nvarchar(4000)
    declare @nl                       char(2)
    declare @tb                       char(2)
    declare @fnameVar                 nvarchar(254) = 'NULL'

    set @nl  = char(10); -- New line
    set @tb  = char(9)   -- Tab separator

    if (@filename is not null)
    set @fnameVar = ''''+@filename +''''

    set @sql='use ['+@dbname+'];'+@nl+
    'select top 1 [Current LSN],[Begin Time]'+@nl+
    'FROM fn_dump_dblog (NULL, NULL, NULL, '+ cast(@seqno as varchar(10))+','+ @fnameVar+','+@nl+
    @tb+'default, default, default, default, default, default, default,'+@nl+
    @tb+'default, default, default, default, default, default, default,'+@nl+
    @tb+'default, default, default, default, default, default, default,'+@nl+
    @tb+'default, default, default, default, default, default, default,'+@nl+
    @tb+'default, default, default, default, default, default, default,'+@nl+
    @tb+'default, default, default, default, default, default, default,'+@nl+
    @tb+'default, default, default, default, default, default, default,'+@nl+
    @tb+'default, default, default, default, default, default, default,'+@nl+
    @tb+'default, default, default, default, default, default, default)'+@nl+
    'where operation=''LOP_BEGIN_XACT''' +@nl+
    'and [Begin Time]>= cast('+''''+@1stTimeStamp+''''+' as datetime)'+@nl

    --print @sql
    delete from  @firstMatching
    insert into @firstMatching  exec sp_executesql @sql    -- Get them all

    select top 1 cLsn as [matching LSN],convert(varchar,bTim,121) as [matching Timestamp] from @firstMatching;

    SET NOCOUNT OFF      -- Re-enable "rows affected display"

    end
    GO
```

10. Create the certificate on the Master database using the following script:

```
Use [master]
Go
CREATE CERTIFICATE [awsdms_rtm_position_1st_timestamp_cert]
ENCRYPTION BY PASSWORD = '@5trongpassword'
WITH SUBJECT = N'Certificate for FN_POSITION_1st_TIMESTAMP Permissions';
```

11. Create the login from the certificate using the following script:

```
Use [master]
Go
CREATE LOGIN awsdms_rtm_position_1st_timestamp_login FROM CERTIFICATE [awsdms_rtm_position_1st_timestamp_cert];
```

12. Add the login to the sysadmin role using the following script:

```
ALTER SERVER ROLE [sysadmin] ADD MEMBER [awsdms_rtm_position_1st_timestamp_login];
```

13. Add the signature to [master].[awsdms].[rtm\_position\_1st\_timestamp] using the certificate,
    using the following script:

```
Use [master]
    GO
    ADD SIGNATURE
    TO [master].[awsdms].[rtm_position_1st_timestamp]
    BY CERTIFICATE [awsdms_rtm_position_1st_timestamp_cert]
    WITH PASSWORD = '@5trongpassword';
```

14. Grant the DMS user execute access to the new stored procedure using the following script:

```
use master
go
GRANT execute on [awsdms].[rtm_position_1st_timestamp] to dms_user;
```

15. Create a user with the following permissions and roles in each of the following databases:

###### Note

You should create the dmsnosysadmin user account with the same SID on each replica. The following
SQL query can help verify the dmsnosysadmin account SID value on each replica. For more information about
creating a user, see
[CREATE USER (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-user-transact-sql "https://learn.microsoft.com/en-us/sql/t-sql/statements/create-user-transact-sql") in the
[Microsoft SQL server documentation](https://learn.microsoft.com/en-us/sql/ "https://learn.microsoft.com/en-us/sql/").
For more information about creating SQL user accounts for Azure SQL database, see
[Active geo-replication](https://learn.microsoft.com/en-us/azure/azure-sql/database/active-geo-replication-overview "https://learn.microsoft.com/en-us/azure/azure-sql/database/active-geo-replication-overview") .

```
use master
go
grant select on sys.fn_dblog to [DMS_user]
grant view any definition to [DMS_user]
grant view server state to [DMS_user]--(should be granted to the login).
grant execute on sp_repldone to [DMS_user]
grant execute on sp_replincrementlsn to [DMS_user]
grant execute on sp_addpublication to [DMS_user]
grant execute on sp_addarticle to [DMS_user]
grant execute on sp_articlefilter to [DMS_user]
grant select on [awsdms].[split_partition_list] to [DMS_user]
grant execute on [awsdms].[rtm_dump_dblog] to [DMS_user]
```

```
use msdb
go
grant select on msdb.dbo.backupset to `self_managed_user`
grant select on msdb.dbo.backupmediafamily to `self_managed_user`
grant select on msdb.dbo.backupfile to `self_managed_user`
```

Run the following script on the source database:

```
use Source_DB
    Go
    EXEC sp_addrolemember N'db_owner', N'DMS_user'
```

16. Lastly, add an Extra Connection Attribute (ECA) to the source SQL Server endpoint:

```
enableNonSysadminWrapper=true;
```

#### Setting up ongoing replication

on a SQL Server in an availability group environment: Without sysadmin role

This section describes how to set up ongoing replication for a SQL Server database source
in an availability group environment that
doesn't require the user account to have sysadmin privileges.

###### Note

After running the steps in this section, the non-sysadmin DMS user will have permissions
to do the following:

- Read changes from the online transactions log file
- Disk access to read changes from transactional log backup files
- Add or alter the publication which DMS uses
- Add articles to the publication

###### To set up ongoing replication without using the sysadmin user in an Availability Group environment

1. Set up Microsoft SQL Server for Replication as described in
   [Capturing data changes for ongoing replication from SQL Server](CHAP_Source.SQLServer.md "CHAP_Source.SQLServer.md").
2. Enable MS-REPLICATION on the source database. This can either be done manually or by running
   the task once using a sysadmin user.

###### Note

You should either configure the MS-REPLICATION distributor as local or in a way that allows
access to non-sysadmin users via the associated linked server. 3. If the **Exclusively use sp_repldone within a single task** endpoint option is
enabled, stop the MS-REPLICATION Log Reader job. 4. Perform the following steps on each replica:

    1. Create the `[awsdms]`[awsdms] schema in the master database:



    ```
    CREATE SCHEMA [awsdms]
    ```
    2. Create the `[awsdms].[split_partition_list]` table valued function on the Master database:



    ```
    USE [master]
    GO

    SET ansi_nulls on
    GO

    SET quoted_identifier on
    GO

    IF (object_id('[awsdms].[split_partition_list]','TF')) is not null
      DROP FUNCTION [awsdms].[split_partition_list];
    GO

    CREATE FUNCTION [awsdms].[split_partition_list]
    (
      @plist varchar(8000),    --A delimited list of partitions
      @dlm nvarchar(1)    --Delimiting character
    )
    RETURNS @partitionsTable table --Table holding the BIGINT values of the string fragments
    (
      pid bigint primary key
    )
    AS
    BEGIN
      DECLARE @partition_id bigint;
      DECLARE @dlm_pos integer;
      DECLARE @dlm_len integer;
      SET @dlm_len = len(@dlm);
      WHILE (charindex(@dlm,@plist)>0)
      BEGIN
        SET @dlm_pos = charindex(@dlm,@plist);
        SET @partition_id = cast( ltrim(rtrim(substring(@plist,1,@dlm_pos-1))) as bigint);
        INSERT into @partitionsTable (pid) values (@partition_id)
        SET @plist = substring(@plist,@dlm_pos+@dlm_len,len(@plist));
      END
      SET @partition_id = cast (ltrim(rtrim(@plist)) as bigint);
      INSERT into @partitionsTable (pid) values (  @partition_id  );
      RETURN
    END
    GO
    ```
    3. Create the `[awsdms].[rtm_dump_dblog]` procedure on the Master database:



    ```
    USE [MASTER]
    GO

    IF (object_id('[awsdms].[rtm_dump_dblog]','P')) is not null
      DROP PROCEDURE [awsdms].[rtm_dump_dblog];
    GO

    SET ansi_nulls on
    GO

    SET quoted_identifier on
    GO

    CREATE PROCEDURE [awsdms].[rtm_dump_dblog]
    (
      @start_lsn            varchar(32),
      @seqno                integer,
      @filename             varchar(260),
      @partition_list       varchar(8000), -- A comma delimited list: P1,P2,... Pn
      @programmed_filtering integer,
      @minPartition         bigint,
      @maxPartition         bigint
    )
    AS
    BEGIN

      DECLARE @start_lsn_cmp varchar(32); -- Stands against the GT comparator

      SET NOCOUNT ON  -- Disable "rows affected display"

      SET @start_lsn_cmp = @start_lsn;
      IF (@start_lsn_cmp) is null
        SET @start_lsn_cmp = '00000000:00000000:0000';

      IF (@partition_list is null)
        BEGIN
          RAISERROR ('Null partition list was passed',16,1);
          return
          --set @partition_list = '0,';    -- A dummy which is never matched
        END

      IF (@start_lsn) is not null
        SET @start_lsn = '0x'+@start_lsn;

      IF (@programmed_filtering=0)
        SELECT
          [Current LSN],
          [operation],
          [Context],
          [Transaction ID],
          [Transaction Name],
          [Begin Time],
          [End Time],
          [Flag Bits],
          [PartitionID],
          [Page ID],
          [Slot ID],
          [RowLog Contents 0],
          [Log Record],
          [RowLog Contents 1] -- After Image
        FROM
          fn_dump_dblog (
            @start_lsn, NULL, N'DISK', @seqno, @filename,
            default, default, default, default, default, default, default,
            default, default, default, default, default, default, default,
            default, default, default, default, default, default, default,
            default, default, default, default, default, default, default,
            default, default, default, default, default, default, default,
            default, default, default, default, default, default, default,
            default, default, default, default, default, default, default,
            default, default, default, default, default, default, default,
            default, default, default, default, default, default, default)
        WHERE
          [Current LSN] collate SQL_Latin1_General_CP1_CI_AS > @start_lsn_cmp collate SQL_Latin1_General_CP1_CI_AS -- This aims for implementing FN_DBLOG based on GT comparator.
          AND
          (
            (  [operation] in ('LOP_BEGIN_XACT','LOP_COMMIT_XACT','LOP_ABORT_XACT') )
            OR
            (  [operation] in ('LOP_INSERT_ROWS','LOP_DELETE_ROWS','LOP_MODIFY_ROW')
              AND
              ( ( [context]   in ('LCX_HEAP','LCX_CLUSTERED','LCX_MARK_AS_GHOST') ) or ([context] = 'LCX_TEXT_MIX') )
              AND
              [PartitionID] in ( select * from master.awsdms.split_partition_list (@partition_list,','))
            )
          OR
          ([operation] = 'LOP_HOBT_DDL')
        )
        ELSE
          SELECT
            [Current LSN],
            [operation],
            [Context],
            [Transaction ID],
            [Transaction Name],
            [Begin Time],
            [End Time],
            [Flag Bits],
            [PartitionID],
            [Page ID],
            [Slot ID],
            [RowLog Contents 0],
            [Log Record],
            [RowLog Contents 1] -- After Image
          FROM
            fn_dump_dblog (
              @start_lsn, NULL, N'DISK', @seqno, @filename,
              default, default, default, default, default, default, default,
              default, default, default, default, default, default, default,
              default, default, default, default, default, default, default,
              default, default, default, default, default, default, default,
              default, default, default, default, default, default, default,
              default, default, default, default, default, default, default,
              default, default, default, default, default, default, default,
              default, default, default, default, default, default, default,
              default, default, default, default, default, default, default)
          WHERE [Current LSN] collate SQL_Latin1_General_CP1_CI_AS > @start_lsn_cmp collate SQL_Latin1_General_CP1_CI_AS -- This aims for implementing FN_DBLOG based on GT comparator.
          AND
          (
            (  [operation] in ('LOP_BEGIN_XACT','LOP_COMMIT_XACT','LOP_ABORT_XACT') )
            OR
            (  [operation] in ('LOP_INSERT_ROWS','LOP_DELETE_ROWS','LOP_MODIFY_ROW')
              AND
              ( ( [context]   in ('LCX_HEAP','LCX_CLUSTERED','LCX_MARK_AS_GHOST') ) or ([context] = 'LCX_TEXT_MIX') )
              AND ([PartitionID] is not null) and ([PartitionID] >= @minPartition and [PartitionID]<=@maxPartition)
            )
            OR
            ([operation] = 'LOP_HOBT_DDL')
          )
          SET NOCOUNT OFF -- Re-enable "rows affected display"
    END
    GO
    ```
    4. Create a certificate on the Master Database:



    ```
    USE [master]
    GO
    CREATE CERTIFICATE [awsdms_rtm_dump_dblog_cert]
      ENCRYPTION BY PASSWORD = N'@hardpassword1'
      WITH SUBJECT = N'Certificate for FN_DUMP_DBLOG Permissions'
    ```
    5. Create a login from the certificate:



    ```
    USE [master]
    GO
    CREATE LOGIN awsdms_rtm_dump_dblog_login FROM CERTIFICATE
      [awsdms_rtm_dump_dblog_cert];
    ```
    6. Add the login to the sysadmin server role:



    ```
    ALTER SERVER ROLE [sysadmin] ADD MEMBER [awsdms_rtm_dump_dblog_login];
    ```
    7. Add the signature to the [master].[awsdms].[rtm\_dump\_dblog] procedure using the certificate:



    ```
    USE [master]
    GO

    ADD SIGNATURE
      TO [master].[awsdms].[rtm_dump_dblog]
      BY CERTIFICATE [awsdms_rtm_dump_dblog_cert]
      WITH PASSWORD = '@hardpassword1';
    ```

    ###### Note

    If you recreate the stored procedure, you need to add the signature again.
    8. Create the `[awsdms].[rtm_position_1st_timestamp]` procedure on the Master database:



    ```
    USE [master]
    IF object_id('[awsdms].[rtm_position_1st_timestamp]','P') is not null
      DROP PROCEDURE [awsdms].[rtm_position_1st_timestamp];
    GO
    CREATE PROCEDURE [awsdms].[rtm_position_1st_timestamp]
    (
      @dbname                sysname,      -- Database name
      @seqno                 integer,      -- Backup set sequence/position number within file
      @filename              varchar(260), -- The backup filename
      @1stTimeStamp          varchar(40)   -- The timestamp to position by
    )
    AS
    BEGIN
      SET NOCOUNT ON       -- Disable "rows affected display"

      DECLARE @firstMatching table
      (
        cLsn varchar(32),
        bTim datetime
      )
      DECLARE @sql nvarchar(4000)
      DECLARE @nl                       char(2)
      DECLARE @tb                       char(2)
      DECLARE @fnameVar                 sysname = 'NULL'

      SET @nl  = char(10); -- New line
      SET @tb  = char(9)   -- Tab separator

      IF (@filename is not null)
        SET @fnameVar = ''''+@filename +''''
      SET @filename = ''''+@filename +''''
      SET @sql='use ['+@dbname+'];'+@nl+
        'SELECT TOP 1 [Current LSN],[Begin Time]'+@nl+
        'FROM fn_dump_dblog (NULL, NULL, NULL, '+ cast(@seqno as varchar(10))+','+ @filename +','+@nl+
        @tb+'default, default, default, default, default, default, default,'+@nl+
        @tb+'default, default, default, default, default, default, default,'+@nl+
        @tb+'default, default, default, default, default, default, default,'+@nl+
        @tb+'default, default, default, default, default, default, default,'+@nl+
        @tb+'default, default, default, default, default, default, default,'+@nl+
        @tb+'default, default, default, default, default, default, default,'+@nl+
        @tb+'default, default, default, default, default, default, default,'+@nl+
        @tb+'default, default, default, default, default, default, default,'+@nl+
        @tb+'default, default, default, default, default, default, default)'+@nl+
        'WHERE operation=''LOP_BEGIN_XACT''' +@nl+
        'AND [Begin Time]>= cast('+''''+@1stTimeStamp+''''+' as datetime)'+@nl

        --print @sql
        DELETE FROM @firstMatching
        INSERT INTO @firstMatching  exec sp_executesql @sql    -- Get them all
        SELECT TOP 1 cLsn as [matching LSN],convert(varchar,bTim,121) AS[matching Timestamp] FROM @firstMatching;

        SET NOCOUNT OFF      -- Re-enable "rows affected display"

    END
    GO
    ```
    9. Create a certificate on the Master database:



    ```
    USE [master]
    GO
    CREATE CERTIFICATE [awsdms_rtm_position_1st_timestamp_cert]
      ENCRYPTION BY PASSWORD = N'@hardpassword1'
      WITH SUBJECT = N'Certificate for FN_POSITION_1st_TIMESTAMP Permissions';
    ```
    10. Create a login from the certificate:



    ```
    USE [master]
    GO
    CREATE LOGIN awsdms_rtm_position_1st_timestamp_login FROM CERTIFICATE
      [awsdms_rtm_position_1st_timestamp_cert];
    ```
    11. Add the login to the sysadmin server role:



    ```
    ALTER SERVER ROLE [sysadmin] ADD MEMBER [awsdms_rtm_position_1st_timestamp_login];
    ```
    12. Add the signature to the `[master].[awsdms].[rtm_position_1st_timestamp]` procedure
     using the certificate:



    ```
    USE [master]
    GO
    ADD SIGNATURE
      TO [master].[awsdms].[rtm_position_1st_timestamp]
      BY CERTIFICATE [awsdms_rtm_position_1st_timestamp_cert]
      WITH PASSWORD = '@hardpassword1';
    ```

    ###### Note

    If you recreate the stored procedure, you need to add the signature again.
    13. Create a user with the following permissions/roles in each of the following databases:


    ###### Note

    You should create the dmsnosysadmin user account with the same SID on each replica. The following
     SQL query can help verify the dmsnosysadmin account SID value on each replica. For more information about
     creating a user, see
     [CREATE USER (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-user-transact-sql "https://learn.microsoft.com/en-us/sql/t-sql/statements/create-user-transact-sql")  in the
     [Microsoft SQL server documentation](https://learn.microsoft.com/en-us/sql/ "https://learn.microsoft.com/en-us/sql/").
     For more information about creating SQL user accounts for Azure SQL database, see
     [Active geo-replication](https://learn.microsoft.com/en-us/azure/azure-sql/database/active-geo-replication-overview "https://learn.microsoft.com/en-us/azure/azure-sql/database/active-geo-replication-overview") .



    ```
    SELECT @@servername servername, name, sid, create_date, modify_date
      FROM sys.server_principals
      WHERE name = 'dmsnosysadmin';
    ```
    14. Grant permissions on the master database on each replica:



    ```
    USE master
    GO

    GRANT select on sys.fn_dblog to dmsnosysadmin;
    GRANT view any definition to dmsnosysadmin;
    GRANT view server state to dmsnosysadmin -- (should be granted to the login).
    GRANT execute on sp_repldone to dmsnosysadmin;
    GRANT execute on sp_replincrementlsn to dmsnosysadmin;
    GRANT execute on sp_addpublication to dmsnosysadmin;
    GRANT execute on sp_addarticle to dmsnosysadmin;
    GRANT execute on sp_articlefilter to dmsnosysadmin;
    GRANT select on [awsdms].[split_partition_list] to dmsnosysadmin;
    GRANT execute on [awsdms].[rtm_dump_dblog] to dmsnosysadmin;
    GRANT execute on [awsdms].[rtm_position_1st_timestamp] to dmsnosysadmin;
    ```
    15. Grant permissions on the msdb database on each replica:



    ```
    USE msdb
    GO
    GRANT select on msdb.dbo.backupset TO `self_managed_user`
    GRANT select on msdb.dbo.backupmediafamily TO `self_managed_user`
    GRANT select on msdb.dbo.backupfile TO `self_managed_user`
    ```
    16. Add the `db_owner` role to `dmsnosysadmin` on
     the source database. Because the database is synchronized, you can add the role on
     the primary replica only.



    ```
    use <source DB>
    GO
    EXEC sp_addrolemember N'db_owner', N'dmsnosysadmin'
    ```

## Setting up ongoing replication

on a cloud SQL Server DB instance

This section describes how to set up CDC on a cloud-hosted SQL Server database instance.
A cloud-hosted SQL server instance is an instance running on Amazon RDS for SQL Server, an Azure SQL Manged Instance,
or any other managed cloud SQL Server instance. For information about limitations for ongoing replication for
each database type, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

Before setting up ongoing replication, see [Prerequisites for using ongoing
replication (CDC) from a SQL Server source](CHAP_Source.md#CHAP_Source.SQLServer.Prerequisites "CHAP_Source.md#CHAP_Source.SQLServer.Prerequisites").

Unlike self-managed Microsoft SQL Server sources, Amazon RDS for SQL Server doesn't support
MS-Replication. Therefore, AWS DMS needs to use MS-CDC for tables with or without
primary keys.

Amazon RDS doesn't grant sysadmin privileges for setting replication artifacts
that AWS DMS uses for ongoing changes in a source SQL Server instance. Make sure to
turn on MS-CDC for the Amazon RDS instance (using master user privileges) as in the
following procedure.

###### To turn on MS-CDC for a cloud SQL Server DB instance

1. Run one of the following queries at the database level.

For an RDS for SQL Server DB instance, use this query.

```
exec msdb.dbo.rds_cdc_enable_db '`DB_name`'
```

For an Azure SQL managed DB instance, use this query.

```
USE `DB_name`
GO
EXEC sys.sp_cdc_enable_db
GO
```

2. For each table with a primary key, run the following query to turn on
   MS-CDC.

```
exec sys.sp_cdc_enable_table
@source_schema = N'schema_name',
@source_name = N'table_name',
@role_name = NULL,
@supports_net_changes = 1
GO
```

For each table with unique keys but no primary key, run the following
query to turn on MS-CDC.

```
exec sys.sp_cdc_enable_table
@source_schema = N'schema_name',
@source_name = N'table_name',
@index_name = N'unique_index_name',
@role_name = NULL,
@supports_net_changes = 1
GO
```

For each table with no primary key nor unique keys, run the following
query to turn on MS-CDC.

```
exec sys.sp_cdc_enable_table
@source_schema = N'schema_name',
@source_name = N'table_name',
@role_name = NULL
GO
```

3. Set the retention period:
   - For RDS for SQL Server instances that are replicating using DMS version 3.5.3 and above,
     make sure that the retention period is set to the default value of 5 seconds. If you’re upgrading or moving from DMS 3.5.2 and
     below to DMS 3.5.3 and above, change the polling interval value after the tasks are running
     on the new or upgraded instance. The following script sets the retention period to 5 seconds:

   ```
   use *dbname*
   EXEC sys.sp_cdc_change_job @job_type = 'capture' ,@pollinginterval = 5
   exec sp_cdc_stop_job 'capture'
   exec sp_cdc_start_job 'capture'
   ```

   - The parameter `@pollinginterval` is measured in seconds with a
     recommended value set to 86399. This means that the transaction log retains
     changes for 86,399 seconds (one day) when `@pollinginterval =
86399`. The procedure `exec sp_cdc_start_job 'capture'`
     initiates the settings.

   ###### Note

   With some versions of SQL Server, if the value of
   `pollinginterval` is set to more than 3599 seconds, the
   value resets to the default five seconds. When this happens, T-Log
   entries are purged before AWS DMS can read them. To determine which SQL
   Server versions are affected by this known issue, see [this Microsoft KB article](https://support.microsoft.com/en-us/topic/kb4459220-fix-incorrect-results-occur-when-you-convert-pollinginterval-parameter-from-seconds-to-hours-in-sys-sp-cdc-scan-in-sql-server-dac8aefe-b60b-7745-f987-582dda2cfa78 "https://support.microsoft.com/en-us/topic/kb4459220-fix-incorrect-results-occur-when-you-convert-pollinginterval-parameter-from-seconds-to-hours-in-sys-sp-cdc-scan-in-sql-server-dac8aefe-b60b-7745-f987-582dda2cfa78").

   If you are using Amazon RDS with Multi-AZ, make sure that you also set your
   secondary to have the right values in case of failover.

   ```
   exec rdsadmin..rds_set_configuration 'cdc_capture_pollinginterval' , <5 or preferred value>

   ```

###### To maintain the retention period when an AWS DMS replication task is stopped for more than one hour

###### Note

The following steps aren’t needed for a RDS for SQL Server source replicating using DMS 3.5.3 and above.

1. Stop the job truncating the transaction logs by using the following
   command.

```
exec sp_cdc_stop_job 'capture'
```

2. Find your task on the AWS DMS console and resume the task.
3. Choose the **Monitoring** tab, and check the
   `CDCLatencySource` metric.
4. After the `CDCLatencySource` metric equals 0 (zero) and stays
   there, restart the job truncating the transaction logs using the following
   command.

```
exec sp_cdc_start_job 'capture'
```

Remember to start the job that truncates SQL Server transaction logs.
Otherwise, storage on your SQL Server instance might fill up.

### Recommended settings

when using RDS for SQL Server as a source for AWS DMS

#### For AWS DMS 3.5.3 and above

###### Note

The initial release of the RDS for SQL Server log backup feature is enabled by default for endpoints that
you created or modified after the release of DMS version 3.5.3. To use this feature for existing endpoints,
modify the endpoint without making any changes.

AWS DMS version 3.5.3 introduces support for reading from log backups. DMS primarily relies on reading from
the active transaction logs to replicate events. If a transaction is backed up before DMS can read it from
the active log, the task accesses the RDS backups on-demand and reads from the subsequent backup logs until
it catches up to the active transaction log. To ensure that DMS has access to log backups, set the RDS
automated backup retention period to at least one day. For information about setting the automated
backup retention period, see [Backup retention period](../../../AmazonRDS/latest/UserGuide/USER_ManagingAutomatedBackups.md#USER_WorkingWithAutomatedBackups.BackupRetention "../../../AmazonRDS/latest/UserGuide/USER_ManagingAutomatedBackups.md#USER_WorkingWithAutomatedBackups.BackupRetention") in the _Amazon RDS User Guide_.

A DMS task accessing log backups utilizes storage on the RDS instance. Note that the task only accesses the log backups
needed for replication. Amazon RDS removes these downloaded backups in a couple of hours. This removal doesn't
affect the Amazon RDS backups retained in Amazon S3, or Amazon RDS `RESTORE DATABASE` functionality. It is advisable to
allocate additional storage on your RDS for SQL Server source if you intend to replicate using DMS. One way to
estimate the amount of storage needed is to identify the backup from which DMS will start or resume
replicating from, and add up the file sizes of all the subsequent backups using the RDS `tlog backup`
metadata function. For more information about the `tlog backup` function, see
[Listing available transaction log backups](../../../AmazonRDS/latest/UserGuide/USER.SQLServer.AddlFeat.md#USER.SQLServer.AddlFeat.TransactionLogAccess.Listing "../../../AmazonRDS/latest/UserGuide/USER.SQLServer.AddlFeat.md#USER.SQLServer.AddlFeat.TransactionLogAccess.Listing") in the _Amazon RDS User Guide_.

Alternately, you may choose to enable storage autoscaling and/ or trigger storage scaling
based on the CloudWatch `FreeStorageSpace` metric for your Amazon RDS instance.

We strongly recommend that you don’t start or resume from a point too far back in the transaction log backups,
as it might lead to storage on your SQL Server instance filling up. In such cases, it is advisable to start
a full load. Replicating from the transaction log backup is slower than reading from the active transaction logs.
For more information, see [Transaction log
backup processing for RDS for SQL Server](CHAP_Troubleshooting_Latency_Source_SQLServer.md#CHAP_Troubleshooting_Latency_Source_SQLServer_backup "CHAP_Troubleshooting_Latency_Source_SQLServer.md#CHAP_Troubleshooting_Latency_Source_SQLServer_backup").

Note that accessing the log backups requires additional privileges. For more information, see
as detailed in [Set up permissions for ongoing replication
from a cloud SQL Server database](CHAP_Source.md#CHAP_Source.SQLServer.Permissions.Cloud "CHAP_Source.md#CHAP_Source.SQLServer.Permissions.Cloud")
Make sure that you grant these privileges before the task starts replicating.

#### For AWS DMS 3.5.2 and below

When you work with Amazon RDS for SQL Server as a source, the MS-CDC capture job relies on the parameters
`maxscans` and `maxtrans`. These parameters govern the maximum
number of scans that the MS-CDC capture does on the transaction log and the number of
transactions that are processed for each scan.

For databases, where a number of transactions is greater than
`maxtrans*maxscans`, increasing the `polling_interval` value
can cause an accumulation of active transaction log records. In turn, this accumulation
can lead to an increase in the size of the transaction log.

Note that AWS DMS does not rely on the MS-CDC capture job. The MS-CDC capture job marks
the transaction log entries as having been processed. This allows the transaction log backup
job to remove the entries from the transaction log.

We recommend that you monitor the size of the transaction log and the success of the MS-CDC jobs. If
the MS-CDC jobs fail, the transaction log could grow excessively and cause AWS DMS replication failures.
You can monitor MS-CDC capture job errors using the `sys.dm_cdc_errors` dynamic management view
in the source database. You can monitor the transaction log size using the `DBCC SQLPERF(LOGSPACE)`
management command.

###### To address the transaction log increase that is caused by MS-CDC

1. Check the `Log Space Used %` for the database AWS DMS is replicating from and validate that it increases continuously.

```
DBCC SQLPERF(LOGSPACE)
```

2. Identify what is blocking the transaction log backup process.

```
Select log_reuse_wait, log_reuse_wait_desc, name from sys.databases where name = db_name();
```

If the `log_reuse_wait_desc` value equals `REPLICATION`,
the log backup retention is caused by the latency in MS-CDC. 3. Increase the number of events processed by the capture job by increasing the
`maxtrans` and `maxscans` parameter values.

```
EXEC sys.sp_cdc_change_job @job_type = 'capture' ,@maxtrans = 5000, @maxscans = 20
exec sp_cdc_stop_job 'capture'
exec sp_cdc_start_job 'capture'
```

To address this issue, set the values of `maxscans` and
`maxtrans` so that `maxtrans*maxscans` is equal to the average
number of events generated for tables that AWS DMS replicates from the source database for
each day.

If you set these parameters higher than the recommended value, the capture jobs process all events
in the transaction logs. If you set these parameters below the recommended value, MS-CDC latency
increases and your transaction log grows.

Identifying appropriate values for `maxscans` and `maxtrans` can
be difficult because changes in workload produce varying number of events. In this case,
we recommend that you set up monitoring on MS-CDC latency. For more information, see
[Monitor the process](https://docs.microsoft.com/en-us/sql/relational-databases/track-changes/administer-and-monitor-change-data-capture-sql-server?view=sql-server-ver15#Monitor "https://docs.microsoft.com/en-us/sql/relational-databases/track-changes/administer-and-monitor-change-data-capture-sql-server?view=sql-server-ver15#Monitor") in SQL Server documentation. Then configure
`maxtrans` and `maxscans` dynamically based on the monitoring
results.

If the AWS DMS task is unable to find the log sequence numbers (LSNs) needed to resume or continue the task, the task may fail and require a complete reload.

###### Note

When using AWS DMS to replicate data from an RDS for SQL Server source, you may encounter errors
when trying to resume replication after a stop-start event of the Amazon RDS instance. This is
due to the SQL Server Agent process restarting the capture job process when it restarts after the
stop-start event. This bypasses the MS-CDC polling interval.

Because of this, on databases with transaction volumes lower than the MS-CDC capture
job processing, this can cause data to be processed or marked as replicated and backed up
before AWS DMS can resume from where it stopped, resulting in the following error:

```
[SOURCE_CAPTURE ]E: Failed to access LSN '0000dbd9:0006f9ad:0003' in the backup log sets since BACKUP/LOG-s are not available. [1020465] (sqlserver_endpoint_capture.c:764)
```

To mitigate this issue, set the `maxtrans` and `maxscans` values as
recommended prior.
