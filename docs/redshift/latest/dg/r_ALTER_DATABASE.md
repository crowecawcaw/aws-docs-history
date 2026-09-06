

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ALTER DATABASE
<a name="r_ALTER_DATABASE"></a>

Changes the attributes of a database.

## Required privileges
<a name="r_ALTER_DATABASE-privileges"></a>

To use ALTER DATABASE, one of the following privileges is required..
+ Superuser
+ Users with the ALTER DATABASE privilege
+ Database owner

## Syntax
<a name="r_ALTER_DATABASE-synopsis"></a>

```
ALTER DATABASE database_name
{ 
  RENAME TO new_name
  | OWNER TO new_owner
  | [ CONNECTION LIMIT { limit | UNLIMITED } ]
    [ COLLATE { CASE_SENSITIVE | CS | CASE_INSENSITIVE | CI } ]
    [ ISOLATION LEVEL { SNAPSHOT | SERIALIZABLE } ]
| INTEGRATION
 { 
  REFRESH { { ALL | INERROR | REMEDIABLE } TABLES [ IN SCHEMA schema [, ...] ] | TABLE schema.table [, ...] }
   | SET 
     [ QUERY_ALL_STATES [=] { TRUE | FALSE } ] 
     [ ACCEPTINVCHARS [=] { TRUE | FALSE } ] 
     [ REFRESH_INTERVAL <interval> ]
     [ TRUNCATECOLUMNS [=] { TRUE | FALSE } ]
     [ HISTORY_MODE [=] {TRUE | FALSE} [ FOR { {ALL} TABLES [IN SCHEMA schema [, ...] ] | TABLE schema.table [, ...] } ] ]
     [ AUTO_REMEDIATION [=] { TRUE | FALSE } ]
 }
}
```

## Parameters
<a name="r_ALTER_DATABASE-parameters"></a>

 *database\_name*   
Name of the database to alter. Typically, you alter a database that you are not currently connected to; in any case, the changes take effect only in subsequent sessions. You can change the owner of the current database, but you can't rename it:  

```
alter database tickit rename to newtickit;
ERROR:  current database may not be renamed
```

RENAME TO   
Renames the specified database. For more information about valid names, see [Names and identifiers](r_names.md). You can't rename the dev, padb\_harvest, template0, template1, or sys:internal databases, and you can't rename the current database. Only the database owner or a [superuser](r_superusers.md#def_superusers) can rename a database; non-superuser owners must also have the CREATEDB privilege.

 *new\_name*   
New database name.

OWNER TO   
Changes the owner of the specified database. You can change the owner of the current database or some other database. Only a superuser can change the owner.

 *new\_owner*   
New database owner. The new owner must be an existing database user with write privileges. For more information about user privileges, see [GRANT](r_GRANT.md).

CONNECTION LIMIT { *limit* \| UNLIMITED }   
The maximum number of database connections users are permitted to have open concurrently. The limit is not enforced for superusers. Use the UNLIMITED keyword to permit the maximum number of concurrent connections. A limit on the number of connections for each user might also apply. For more information, see [CREATE USER](r_CREATE_USER.md). The default is UNLIMITED. To view current connections, query the [STV\_SESSIONS](r_STV_SESSIONS.md) system view.  
If both user and database connection limits apply, an unused connection slot must be available that is within both limits when a user attempts to connect.

COLLATE { CASE\_SENSITIVE \| CS \| CASE\_INSENSITIVE \| CI }  
A clause that specifies whether string search or comparison is case-sensitive or case-insensitive.   
You can change the case sensitivity of the current database even if it's empty.  
You must have ALTER permission for the current database to change case sensitivity. Superusers or database owners with the CREATE DATABASE permission can also change database case sensitivity.  
CASE\_SENSITIVE and CS are interchangeable and yield the same results. Similarly, CASE\_INSENSITIVE and CI are interchangeable and yield the same results.  
To check the current collation of a database, use the [DB\_COLLATION](r_DB_COLLATION.md) function.

ISOLATION LEVEL { SNAPSHOT \| SERIALIZABLE }  
A clause that specifies the isolation level used when queries run against a database. For more information on isolation levels, see [Isolation levels in Amazon Redshift](c_serial_isolation.md).  
+ SNAPSHOT isolation – provides an isolation level with protection against update and delete conflicts. 
+ SERIALIZABLE isolation – provides full serializability for concurrent transactions.
Consider the following items when altering the isolation level of a database:  
+ You must have the superuser or CREATE DATABASE privilege to the current database to change the database isolation level.
+ You can't alter the isolation level of the `dev` database. 
+ You can't alter the isolation level within a transaction block.
+ The alter isolation level command fails if other users are connected to the database.
+ The alter isolation level command can alter the isolation level settings of the current session.

INTEGRATION  
Alter a zero-ETL integration database.

REFRESH {{ ALL \| INERROR \| REMEDIABLE } TABLES [IN SCHEMA *schema* [, ...]] \| TABLE *schema.table* [, ...]}  
A clause that specifies which tables Amazon Redshift refreshes. You can target all tables, tables with errors, or tables affected by duplicate rows. The refresh fully replicates the tables from the source database.  
`REMEDIABLE` targets tables in the `Synced` state that have been affected by duplicate rows. You can inspect which tables are affected by querying [SVV\_INTEGRATION\_TABLE\_STATE](r_SVV_INTEGRATION_TABLE_STATE.md).  
For more information, see [Zero-ETL integrations](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.html) in the *Amazon Redshift Management Guide*. For more information about integration states, see [SVV\_INTEGRATION\_TABLE\_STATE](r_SVV_INTEGRATION_TABLE_STATE.md) and [SVV\_INTEGRATION](r_SVV_INTEGRATION.md).

QUERY\_ALL\_STATES [=] { TRUE \| FALSE }  
The QUERY\_ALL\_STATES clause sets whether zero-ETL integration tables can be queried in all states (`Synced`, `Failed`, `ResyncRequired`, and `ResyncInitiated`). By default, a zero-ETL integration table can only be queried in `Synced` state.

ACCEPTINVCHARS [=] { TRUE \| FALSE }  
The ACCEPTINVCHARS clause sets whether zero-ETL integration tables continue with ingestion when invalid characters are detected for the VARCHAR data type. When invalid characters are encountered, the invalid character is replaced with a default `?` character.

REFRESH\_INTERVAL <interval>  
The REFRESH\_INTERVAL clause sets the approximate time interval, in seconds, that Amazon Redshift waits after a refresh cycle completes to start the next one. Each cycle refreshes data from the zero-ETL integration source to the target database, applying all accumulated changes since the end of the previous cycle. A value of 0 starts the next cycle as soon as the previous one finishes (near-real-time replication). A higher value spaces cycles further apart, reducing refresh overhead at the cost of immediate data freshness. Amazon Redshift waits between cycles only when ingestion has caught up; when changes accumulate faster than they can be applied, cycles run with no wait.  
The `interval` can be set to 0–432,000 seconds (5 days) for zero-ETL integrations whose source type is Aurora MySQL, Aurora PostgreSQL, or the supported RDS engines, and the default is 0. For Amazon DynamoDB zero-ETL integrations, the `interval` can be set to 900–432,000 seconds (15 minutes–5 days), and the default is 900 seconds (15 minutes); 0 is not supported.  
For write-intensive integrations other than DynamoDB that generate a high volume of changes, set REFRESH\_INTERVAL to a small non-zero value (for example, 60–120 seconds). Grouping more changes into each cycle reduces the overall compute overhead of replication.
For more information about creating databases with zero-ETL integrations, see [Creating destination databases in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.creating-db.html) in the *Amazon Redshift Management Guide*.

TRUNCATECOLUMNS [=] { TRUE \| FALSE }  
The TRUNCATECOLUMNS clause sets whether zero-ETL integration tables continue with ingestion when the values for the VARCHAR column or SUPER column attributes are beyond the limit. When `TRUE`, the values are truncated to fit into the column and the values of overflowing JSON attributes are truncated to fit into the SUPER column.

HISTORY\_MODE [=] {TRUE \| FALSE} [ FOR { {ALL} TABLES [IN SCHEMA schema [, ...]] \| TABLE schema.table [, ...]} ]  
A clause that specifies whether Amazon Redshift will set history mode for all tables or tables in the specified schema that participate in zero-ETL integration. This option is only applicable for databases created for zero-ETL integration.  
The HISTORY\_MODE clause can be set to `TRUE` or `FALSE`. The default is `FALSE`. Switching history mode on and off is only applicable to tables that are in the `Synced` state. For information about HISTORY\_MODE, see [History mode](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-history-mode.html) in the *Amazon Redshift Management Guide*.

AUTO\_REMEDIATION [=] { TRUE \| FALSE }  
Specifies whether Amazon Redshift automatically resynchronizes tables that are affected by duplicate rows. When set to `TRUE`, Amazon Redshift marks affected tables for resynchronization without requiring manual intervention. The default is `FALSE`.  
You can monitor which tables have been flagged by querying [SVV\_INTEGRATION\_TABLE\_STATE](r_SVV_INTEGRATION_TABLE_STATE.md). The current setting is visible in the `auto_remediation` column of [SVV\_INTEGRATION](r_SVV_INTEGRATION.md).

## Usage notes
<a name="r_ALTER_DATABASE-usage-notes"></a>

ALTER DATABASE commands apply to subsequent sessions not current sessions. You must reconnect to the altered database to see the effect of the change.

## Examples
<a name="r_ALTER_DATABASE-examples"></a>

The following example renames a database named TICKIT\_SANDBOX to TICKIT\_TEST: 

```
alter database tickit_sandbox rename to tickit_test;
```

The following example changes the owner of the TICKIT database (the current database) to DWUSER: 

```
alter database tickit owner to dwuser;
```

The following example changes the database case sensitivity of the sampledb database:

```
ALTER DATABASE sampledb COLLATE CASE_INSENSITIVE;
```

The following example alters a database named **sampledb** with SNAPSHOT isolation level.

```
ALTER DATABASE sampledb ISOLATION LEVEL SNAPSHOT;
```

The following example refreshes the tables **schema1.sample\_table1** and **schema2.sample\_table2** in the database **sample\_integration\_db** in your zero-ETL integration.

```
ALTER DATABASE sample_integration_db INTEGRATION REFRESH TABLE schema1.sample_table1, schema2.sample_table2;
```

The following example refreshes all synced and failed tables within your zero-ETL integration.

```
ALTER DATABASE sample_integration_db INTEGRATION REFRESH ALL tables;
```

The following example sets the refresh interval for zero-ETL integrations to 600 seconds..

```
ALTER DATABASE sample_integration_db INTEGRATION SET REFRESH_INTERVAL 600;
```

The following example refreshes all tables that are in the `ErrorState` in the schema **sample\_schema**.

```
ALTER DATABASE sample_integration_db INTEGRATION REFRESH INERROR TABLES in SCHEMA sample_schema;
```

The following example switches history mode on for table `myschema.table1`.

```
ALTER DATABASE sample_integration_db INTEGRATION SET HISTORY_MODE = true FOR TABLE myschema.table1
```

The following example switches history mode on for all tables in `myschema`. 

```
ALTER DATABASE sample_integration_db INTEGRATION SET HISTORY_MODE = true for ALL TABLES IN SCHEMA myschema
```

The following example enables automatic remediation of duplicate rows for a zero-ETL integration database.

```
ALTER DATABASE sample_integration_db INTEGRATION SET AUTO_REMEDIATION = true;
```

The following example refreshes all tables affected by duplicate rows in the zero-ETL integration database.

```
ALTER DATABASE sample_integration_db INTEGRATION REFRESH REMEDIABLE TABLES;
```

The following example refreshes tables affected by duplicate rows in the schema `myschema`.

```
ALTER DATABASE sample_integration_db INTEGRATION REFRESH REMEDIABLE TABLES IN SCHEMA myschema;
```