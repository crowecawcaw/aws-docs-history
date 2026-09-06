

# Using a Microsoft SQL Server database as a target for AWS Database Migration Service
<a name="CHAP_Target.SQLServer"></a>

You can migrate data to Microsoft SQL Server databases using AWS DMS. With an SQL Server database as a target, you can migrate data from either another SQL Server database or one of the other supported databases.

For information about versions of SQL Server that AWS DMS supports as a target, see [Targets for AWS DMS](CHAP_Introduction.Targets.md). 

AWS DMS supports the on-premises and Amazon RDS editions of Enterprise, Standard, Workgroup, and Developer.

For additional details on working with AWS DMS and SQL Server target databases, see the following.

**Topics**
+ [Limitations on using SQL Server as a target for AWS Database Migration Service](#CHAP_Target.SQLServer.Limitations)
+ [Security requirements when using SQL Server as a target for AWS Database Migration Service](#CHAP_Target.SQLServer.Security)
+ [Endpoint settings when using SQL Server as a target for AWS DMS](#CHAP_Target.SQLServer.ConnectionAttrib)
+ [Target data types for Microsoft SQL Server](#CHAP_Target.SQLServer.DataTypes)

## Limitations on using SQL Server as a target for AWS Database Migration Service
<a name="CHAP_Target.SQLServer.Limitations"></a>

The following limitations apply when using a SQL Server database as a target for AWS DMS:
+ When you manually create a SQL Server target table with a computed column, full load replication is not supported when using the BCP bulk-copy utility. To use full load replication, disable BCP loading by setting the extra connection attribute (ECA) `'useBCPFullLoad=false'` on the endpoint. For information about setting ECAs on endpoints, see [Creating source and target endpoints](CHAP_Endpoints.Creating.md). For more information on working with BCP, see the [Microsoft SQL Server documentation](https://docs.microsoft.com/en-us/sql/relational-databases/import-export/import-and-export-bulk-data-by-using-the-bcp-utility-sql-server).
+ When replicating tables with SQL Server spatial data types (GEOMETRY and GEOGRAPHY), AWS DMS replaces any spatial reference identifier (SRID) that you might have inserted with the default SRID. The default SRID is 0 for GEOMETRY and 4326 for GEOGRAPHY.
+ Temporal tables are not supported. Migrating temporal tables may work with a replication-only task in transactional apply mode if those tables are manually created on the target.
+ Currently, `boolean` data types in a PostgreSQL source are migrated to a SQLServer target as the `bit` data type with inconsistent values. 

  As a workaround, do the following:
  + Precreate the table with a `VARCHAR(1)` data type for the column (or let AWS DMS create the table). Then have downstream processing treat an "F" as False and a "T" as True.
  + To avoid having to change downstream processing, add a transformation rule to the task to change the "F" values to "0" and "T" values to 1, and store them as the SQL server bit datatype.
+ AWS DMS doesn't support change processing to set column nullability (using the `ALTER COLUMN [SET|DROP] NOT NULL` clause with `ALTER TABLE` statements).
+ Windows Authentication isn't supported.

## Security requirements when using SQL Server as a target for AWS Database Migration Service
<a name="CHAP_Target.SQLServer.Security"></a>

The following describes the security requirements for using AWS DMS with a Microsoft SQL Server target:
+ The AWS DMS user account must have at least the `db_owner` user role on the SQL Server database that you are connecting to.
+ A SQL Server system administrator must provide this permission to all AWS DMS user accounts.

## Endpoint settings when using SQL Server as a target for AWS DMS
<a name="CHAP_Target.SQLServer.ConnectionAttrib"></a>

You can use endpoint settings to configure your SQL Server target database similar to using extra connection attributes. You specify the settings when you create the target endpoint using the AWS DMS console, or by using the `create-endpoint` command in the [AWS CLI](https://docs.aws.amazon.com/cli/latest/reference/dms/index.html), with the `--microsoft-sql-server-settings '{"{{EndpointSetting"}}: {{"value"}}, {{...}}}'` JSON syntax.

The following table shows the endpoint settings that you can use with SQL Server as a target.


| Name | Description | 
| --- | --- | 
| `ControlTablesFileGroup` | Specify a filegroup for the AWS DMS internal tables. When the replication task starts, all the internal AWS DMS control tables (awsdms\_ apply\_exception, awsdms\_apply, awsdms\_changes) are created on the specified filegroup. <br />Default value: n/a <br />Valid values: String <br />Example: `--microsoft-sql-server-settings '{"ControlTablesFileGroup": "filegroup1"}'`<br />The following is an example of a command for creating a filegroup.<pre>ALTER DATABASE replicate ADD FILEGROUP Test1FG1; <br />GO ALTER DATABASE replicate <br />  ADD FILE (        <br />    NAME = test1dat5,        <br />    FILENAME = 'C:\temp\DATA\t1dat5.ndf',        <br />    SIZE = 5MB,        <br />    MAXSIZE = 100MB,        <br />    FILEGROWTH = 5MB    <br />  )    <br />TO FILEGROUP Test1FG1;    <br />GO<br />                                </pre> | 
| `ConnectionTimeout` | Use this extra connection attribute (ECA) to set the endpoint connection timeout for the SQL Server instance, in seconds. The default value is 10 seconds. ECA Example: `ConnectionTimeout=30`. | 
| `ExecuteTimeout` | Use this extra connection attribute (ECA) to set the client statement timeout for the SQL Server instance, in seconds. The default value is 60 seconds. <br />Example: `'{"ExecuteTimeout": 100}'` | 
| `UseBCPFullLoad` | Use this to attribute to transfer data for full-load operations using BCP. When the target table contains an identity column that does not exist in the source table, you must disable the **use BCP for loading table** option. <br />Default value: true <br />Valid values: true/false <br />Example: `--microsoft-sql-server-settings '{"UseBCPFullLoad": false}'` | 

## Target data types for Microsoft SQL Server
<a name="CHAP_Target.SQLServer.DataTypes"></a>

The following table shows the Microsoft SQL Server target data types that are supported when using AWS DMS and the default mapping from AWS DMS data types. For additional information about AWS DMS data types, see [Data types for AWS Database Migration Service](CHAP_Reference.DataTypes.md).


|  AWS DMS data type  |  SQL Server data type  | 
| --- | --- | 
| BOOLEAN | TINYINT | 
| BYTES | VARBINARY(length) | 
| DATE | For SQL Server 2008 and higher, use DATE.<br />For earlier versions, if the scale is 3 or less use DATETIME. In all other cases, use VARCHAR (37). | 
| TIME | For SQL Server 2008 and higher, use DATETIME2 (%d).<br />For earlier versions, if the scale is 3 or less use DATETIME. In all other cases, use VARCHAR (37). | 
| DATETIME | For SQL Server 2008 and higher, use DATETIME2 (scale). <br />For earlier versions, if the scale is 3 or less use DATETIME. In all other cases, use VARCHAR (37). | 
| INT1 | SMALLINT | 
| INT2 | SMALLINT | 
| INT4 | INT | 
| INT8 | BIGINT | 
| NUMERIC | NUMERIC (p,s) | 
| REAL4 | REAL | 
| REAL8 | FLOAT | 
| STRING | If the column is a date or time column, then do the following: +  For SQL Server 2008 and higher, use DATETIME2. <br />+  For earlier versions, if the scale is 3 or less use DATETIME. In all other cases, use VARCHAR (37). <br />If the column is not a date or time column, use VARCHAR (length). | 
| UINT1 | TINYINT | 
| UINT2 | SMALLINT | 
| UINT4 | INT | 
| UINT8 | BIGINT | 
| WSTRING | NVARCHAR (length) | 
| BLOB | VARBINARY(max)<br />IMAGE<br />To use this data type with AWS DMS, you must enable the use of BLOBs for a specific task. AWS DMS supports BLOB data types only in tables that include a primary key. | 
| CLOB | VARCHAR(max)<br />To use this data type with AWS DMS, you must enable the use of CLOBs for a specific task. During change data capture (CDC), AWS DMS supports CLOB data types only in tables that include a primary key. | 
| NCLOB | NVARCHAR(max)<br />To use this data type with AWS DMS, you must enable the use of NCLOBs for a specific task. During CDC, AWS DMS supports NCLOB data types only in tables that include a primary key. | 