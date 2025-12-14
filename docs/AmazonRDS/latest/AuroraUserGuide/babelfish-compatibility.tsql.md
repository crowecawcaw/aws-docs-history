# Unsupported

functionalities in Babelfish

In the following table and lists, you can find functionality that isn't currently
supported in Babelfish. Updates to Babelfish are included in Aurora PostgreSQL
versions. For more information, see the [_Release Notes for Aurora PostgreSQL_](../AuroraPostgreSQLReleaseNotes/Welcome.md "../AuroraPostgreSQLReleaseNotes/Welcome.md").

###### Topics

- [Functionality that isn't currently supported](#babelfish-compatibility.tsql.limitations-unsupported-table "#babelfish-compatibility.tsql.limitations-unsupported-table")
- [Settings
  that aren't supported](#babelfish-compatibility.tsql.limitations-unsupported-list8 "#babelfish-compatibility.tsql.limitations-unsupported-list8")
- [Commands
  that aren't supported](#babelfish-compatibility.tsql.limitations-unsupported-list1 "#babelfish-compatibility.tsql.limitations-unsupported-list1")
- [Column
  names or attributes that aren't supported](#babelfish-compatibility.tsql.limitations-unsupported-list7 "#babelfish-compatibility.tsql.limitations-unsupported-list7")
- [Data types
  that aren't supported](#babelfish-compatibility.tsql.limitations-unsupported-list9 "#babelfish-compatibility.tsql.limitations-unsupported-list9")
- [Object
  types that aren't supported](#babelfish-compatibility.tsql.limitations-unsupported-list3 "#babelfish-compatibility.tsql.limitations-unsupported-list3")
- [Functions
  that aren't supported](#babelfish-compatibility.tsql.limitations-unsupported-list4 "#babelfish-compatibility.tsql.limitations-unsupported-list4")
- [Syntax that
  isn't supported](#babelfish-compatibility.tsql.limitations-unsupported-list5 "#babelfish-compatibility.tsql.limitations-unsupported-list5")

## Functionality that isn't currently supported

In the table you can find information about certain functionality that isn't
currently supported.

| Functionality or syntax                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Assembly modules and SQL Common Language Runtime (CLR)<br>routines          | Functionality related to assembly modules and CLR routines<br>isn't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Column attributes                                                           | ROWGUIDCOL, SPARSE, FILESTREAM, and MASKED aren't<br>supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Contained databases                                                         | Contained databases with logins authenticated at the database<br>level rather than at the server level aren't<br>supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Cross-database DDL                                                          | Performing DDL statements that reference or operate on objects across<br>multiple databases isn't yet supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Cursors (updatable)                                                         | Updatable cursors aren't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Cursors (global)                                                            | GLOBAL cursors aren't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Cursor (fetch behaviors)                                                    | The following cursor fetch behaviors aren't supported:<br>FETCH PRIOR, FIRST, LAST, ABSOLUTE, abd RELATIVE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Cursor-typed output parameters                                              | Cursor-typed variables and parameters aren't supported for<br>output parameters (an error is raised).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Cursor options                                                              | SCROLL, KEYSET, DYNAMIC, FAST_FORWARD, SCROLL_LOCKS,<br>OPTIMISTIC, TYPE_WARNING, and FOR UPDATE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Data encryption                                                             | Data encryption isn't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Data-tier applications (DAC)                                                | Data-tier applications (DAC) import or export operations with<br>DAC package (.dacpac) or DAC backup (.bacpac) files aren't<br>supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DBCC commands                                                               | Microsoft SQL Server Database Console Commands (DBCC)<br>aren't supported. DBCC CHECKIDENT is supported in<br>Babelfish 3.4.0 and higher releases.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DROP IF EXISTS                                                              | This syntax isn't supported for USER and SCHEMA objects.<br>It's supported for the objects TABLE, VIEW, PROCEDURE, FUNCTION, and<br>DATABASE.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Encryption                                                                  | Built-in functions and statements don't support<br>encryption.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ENCRYPT_CLIENT_CERT connections                                             | Client certificate connections aren't<br>supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| EXECUTE AS statement                                                        | This statement isn't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| EXECUTE AS SELF clause                                                      | This clause isn't supported in functions, procedures, or<br>triggers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| EXECUTE AS USER clause                                                      | This clause isn't supported in functions, procedures, or<br>triggers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Foreign key constraints referencing database<br>name                        | Foreign key constraints that reference the database name<br>aren't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| FORMAT                                                                      | User-defined types aren't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Function declarations with greater than 100<br>parameters                   | Function declarations that contain more than 100 parameters<br>aren't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Function calls that include DEFAULT as a parameter<br>value                 | DEFAULT isn't a supported parameter value for a function<br>call. DEFAULT as a parameter value for a function call is supported<br>from Babelfish 3.4.0 and higher releases.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Functions, externally defined                                               | External functions, including SQL CLR functions, aren't<br>supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Global temporary tables (tables with names that start with<br>##)           | Global temporary tables aren't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Graph functionality                                                         | All SQL graph functionality isn't<br>supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| General Extended stored procedures                                          | System stored procedures that provide an interface from an<br>instance of SQL Server to external programs, for various maintenance<br>activities aren't supported. This includes `xp_cmdshell`<br>and other system stored procedures. For more information, see [General Extended stored procedures](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/general-extended-stored-procedures-transact-sql?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/general-extended-stored-procedures-transact-sql?view=sql-server-ver16"). |
| Identifiers (variables or parameters) with multiple leading @<br>characters | Identifiers that start with more than one leading<br>`@` aren't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Identifiers, table or column names that contain @ or ]]<br>characters       | Table or column names that contain an `@` sign or<br>square brackets aren't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Inline indexes                                                              | Inline indexes aren't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Invoking a procedure whose name is in a variable                            | Using a variable as a procedure name isn't<br>supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Materialized views                                                          | Materialized views aren't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| NOT FOR REPLICATION clause                                                  | This syntax is accepted and ignored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ODBC escape functions                                                       | ODBC escape functions aren't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Procedure calls that includes DEFAULT as a parameter<br>value               | DEFAULT isn't a supported parameter value. DEFAULT as a<br>parameter value for a function call is supported from<br>Babelfish 3.4.0 and higher releases.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Procedure declarations with more than 100<br>parameters                     | Declarations with more than 100 parameters aren't<br>supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Procedures, externally defined                                              | Externally defined procedures, including SQL CLR procedures,<br>aren't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Procedure versioning                                                        | Procedure versioning isn't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Procedures WITH RECOMPILE                                                   | WITH RECOMPILE (when used in conjunction with the DECLARE and<br>EXECUTE statements) isn't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Remote object references                                                    | Executing stored procedures against Babelfish linked<br>servers isn’t supported. Four-part object names work only for<br>reading and doesn’t work for modifying the remote table. An UPDATE<br>can reference a remote table in the FROM clause without modifying<br>it. For more information, see [Babelfish supports linked servers](babelfish-postgres-linkedservers.md "babelfish-postgres-linkedservers.md").                                                                                                                                                                                                            |
| Row-level security                                                          | Row-level security with CREATE SECURITY POLICY and inline<br>table-valued functions isn't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Service broker functionality                                                | Service broker functionality isn't<br>supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| SESSIONPROPERTY                                                             | Unsupported properties: ANSI_NULLS, ANSI_PADDING,<br>ANSI_WARNINGS, ARITHABORT, CONCAT_NULL_YIELDS_NULL, and<br>NUMERIC_ROUNDABORT                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| SET LANGUAGE                                                                | This syntax isn't supported with any value other than<br>`english` or `us_english`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| SP_CONFIGURE                                                                | This system stored procedure isn't<br>supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| SQL keyword `SPARSE`                                                        | The keyword SPARSE is accepted and ignored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Table value constructor syntax (FROM clause)                                | The unsupported syntax is for a derived table constructed with<br>the FROM clause.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Temporal tables                                                             | Temporal tables aren't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Temporary procedures aren't dropped<br>automatically                        | This functionality isn't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Triggers, externally defined                                                | These triggers aren't supported, including SQL Common<br>Language Runtime (CLR).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Without SCHEMABINDING clause                                                | Creating a view without SCHEMABINDING isn't supported, but the<br>view is created as if WITH SCHEMABINDING was specified. Using<br>SCHEMABINDING when creating functions, procedures, triggers is<br>silently ignored.                                                                                                                                                                                                                                                                                                                                                                                                       |

## Settings

that aren't supported

The following settings aren't supported:

- SET ANSI_NULL_DFLT_OFF ON
- SET ANSI_NULL_DFLT_ON OFF
- SET ANSI_PADDING OFF
- SET ANSI_WARNINGS OFF
- SET ARITHABORT OFF
- SET ARITHIGNORE ON
- SET CURSOR_CLOSE_ON_COMMIT ON
- SET NUMERIC_ROUNDABORT ON
- SET PARSEONLY ON (command doesn't work as expected)
- SET FMTONLY ON (command doesn't work as expected. It suppresses only the
  execution of SELECT statements but not others.)

## Commands

that aren't supported

Certain functionality for the following commands isn't supported:

- ADD SIGNATURE
- ALTER DATABASE, ALTER DATABASE SET
- BACKUP/RESTORE DATABASE/LOG
- BACPAC and DACPAC FILES RESTORE
- CREATE, ALTER, DROP AUTHORIZATION. ALTER AUTHORIZATION is supported for
  database objects.
- CREATE, ALTER, DROP AVAILABILITY GROUP
- CREATE, ALTER, DROP BROKER PRIORITY
- CREATE, ALTER, DROP COLUMN ENCRYPTION KEY
- CREATE, ALTER, DROP DATABASE ENCRYPTION KEY
- CREATE, ALTER, DROP, BACKUP CERTIFICATE
- CREATE AGGREGATE
- CREATE CONTRACT
- CHECKPOINT

## Column

names or attributes that aren't supported

The following column names aren't supported:

- $IDENTITY
- $ROWGUID
- IDENTITYCOL

## Data types

that aren't supported

The following data types aren't supported:

- HIERARCHYID

## Object

types that aren't supported

The following object types aren't supported:

- COLUMN MASTER KEY
- CREATE, ALTER EXTERNAL DATA SOURCE
- CREATE, ALTER, DROP DATABASE AUDIT SPECIFICATION
- CREATE, ALTER, DROP EXTERNAL LIBRARY
- CREATE, ALTER, DROP SERVER AUDIT
- CREATE, ALTER, DROP SERVER AUDIT SPECIFICATION
- CREATE, ALTER, DROP, OPEN/CLOSE SYMMETRIC KEY
- CREATE, DROP DEFAULT
- CREDENTIAL
- CRYPTOGRAPHIC PROVIDER
- DIAGNOSTIC SESSION
- Indexed views
- SERVICE MASTER KEY
- SYNONYM

## Functions

that aren't supported

The following built-in functions aren't supported:

###### Aggregate functions

- APPROX_COUNT_DISTINCT
- CHECKSUM_AGG
- GROUPING_ID
- STRING_AGG using the WITHIN GROUP clause

###### Cryptographic functions

- CERTENCODED function
- CERTID function
- CERTPROPERTY function

###### Metadata functions

- COLUMNPROPERTY
- TYPEPROPERTY
- SERVERPROPERTY function – The following properties aren't
  supported:
  - BuildClrVersion
  - ComparisonStyle
  - ComputerNamePhysicalNetBIOS
  - HadrManagerStatus
  - InstanceDefaultDataPath
  - InstanceDefaultLogPath
  - IsClustered
  - IsHadrEnabled
  - LCID
  - NumLicenses
  - ProcessID
  - ProductBuild
  - ProductBuildType
  - ProductUpdateReference
  - ResourceLastUpdateDateTime
  - ResourceVersion
  - ServerName
  - SqlCharSet
  - SqlCharSetName
  - SqlSortOrder
  - SqlSortOrderName
  - FilestreamShareName
  - FilestreamConfiguredLevel
  - FilestreamEffectiveLevel

###### Security functions

- CERTPRIVATEKEY
- LOGINPROPERTY

###### Statements, operators, other functions

- EVENTDATA function
- GET_TRANSMISSION_STATUS
- OPENXML

## Syntax that

isn't supported

The following syntax isn't supported:

- ALTER DATABASE
- ALTER DATABASE SCOPED CONFIGURATION
- ALTER DATABASE SCOPED CREDENTIAL
- ALTER DATABASE SET HADR
- ALTER INDEX
- ALTER PARTITION FUNCTION
- ALTER PARTITION SCHEME
- ALTER SCHEMA
- ALTER SERVER CONFIGURATION
- ALTER SERVICE, BACKUP/RESTORE SERVICE MASTER KEY clause
- BEGIN CONVERSATION TIMER
- BEGIN DISTRIBUTED TRANSACTION
- BEGIN DIALOG CONVERSATION
- BULK INSERT
- CREATE COLUMNSTORE INDEX
- CREATE EXTERNAL FILE FORMAT
- CREATE EXTERNAL TABLE
- CREATE, ALTER, DROP APPLICATION ROLE
- CREATE, ALTER, DROP ASSEMBLY
- CREATE, ALTER, DROP ASYMMETRIC KEY
- CREATE, ALTER, DROP CREDENTIAL
- CREATE, ALTER, DROP CRYPTOGRAPHIC PROVIDER
- CREATE, ALTER, DROP ENDPOINT
- CREATE, ALTER, DROP EVENT SESSION
- CREATE, ALTER, DROP EXTERNAL LANGUAGE
- CREATE, ALTER, DROP EXTERNAL RESOURCE POOL
- CREATE, ALTER, DROP FULLTEXT CATALOG
- CREATE, ALTER, DROP FULLTEXT INDEX
- CREATE, ALTER, DROP FULLTEXT STOPLIST
- CREATE, ALTER, DROP MESSAGE TYPE
- CREATE, ALTER, DROP, OPEN/CLOSE, BACKUP/RESTORE MASTER KEY
- CREATE, ALTER, DROP QUEUE
- CREATE, ALTER, DROP RESOURCE GOVERNOR
- CREATE, ALTER, DROP RESOURCE POOL
- CREATE, ALTER, DROP ROUTE
- CREATE, ALTER, DROP SEARCH PROPERTY LIST
- CREATE, ALTER, DROP SECURITY POLICY
- CREATE, ALTER, DROP SELECTIVE XML INDEX clause
- CREATE, ALTER, DROP SERVICE
- CREATE, ALTER, DROP SPATIAL INDEX
- CREATE, ALTER, DROP TYPE
- CREATE, ALTER, DROP XML INDEX
- CREATE, ALTER, DROP XML SCHEMA COLLECTION
- CREATE/DROP RULE
- CREATE, DROP WORKLOAD CLASSIFIER
- CREATE, ALTER, DROP WORKLOAD GROUP
- ALTER TRIGGER
- CREATE TABLE... GRANT clause
- CREATE TABLE... IDENTITY clause
- CREATE USER – This syntax isn't supported. The PostgreSQL
  statement CREATE USER doesn't create a user that is equivalent to the SQL
  Server CREATE USER syntax. For more information, see [T-SQL differences in
  Babelfish](babelfish-compatibility.tsql.md "babelfish-compatibility.tsql.md").
- DENY
- END, MOVE CONVERSATION
- EXECUTE with AS LOGIN or AT option
- GET CONVERSATION GROUP
- GROUP BY ALL clause
- GROUP BY CUBE clause
- GROUP BY ROLLUP clause
- INSERT... DEFAULT VALUES
- MERGE
- READTEXT
- REVERT
- SELECT TOP x PERCENT WHERE x <> 100
- SELECT TOP... WITH TIES
- SELECT... FOR BROWSE
- SELECT... FOR XML AUTO
- SELECT... FOR XML EXPLICIT
- SELECT... FOR XML PATH
- SEND
- SET DATEFORMAT
- SET DEADLOCK_PRIORITY
- SET FMTONLY
- SET FORCEPLAN
- SET NUMERIC_ROUNDABORT ON
- SET OFFSETS
- SET REMOTE_PROC_TRANSACTIONS
- SET SHOWPLAN_TEXT
- SET SHOWPLAN_XML
- SET STATISTICS
- SET STATISTICS PROFILE
- SET STATISTICS TIME
- SET STATISTICS XML
- SHUTDOWN statement
- UPDATE STATISTICS
- UPDATETEXT
- Using EXECUTE to call a SQL function
- VIEW... CHECK OPTION clause
- VIEW... VIEW_METADATA clause
- WAITFOR DELAY
- WAITFOR TIME
- WAITFOR, RECEIVE
- WITH XMLNAMESPACES construct
- WRITETEXT
- XPATH expressions
