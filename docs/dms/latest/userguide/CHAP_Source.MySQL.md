

# Using a MySQL-compatible database as a source for AWS DMS
<a name="CHAP_Source.MySQL"></a>

You can migrate data from any MySQL-compatible database (MySQL, MariaDB, or Amazon Aurora MySQL) using AWS Database Migration Service. 

For information about versions of MySQL that AWS DMS supports as a source, see [Sources for AWS DMS](CHAP_Introduction.Sources.md). 

You can use SSL to encrypt connections between your MySQL-compatible endpoint and the replication instance. For more information on using SSL with a MySQL-compatible endpoint, see [Using SSL with AWS Database Migration Service](CHAP_Security.SSL.md).

In the following sections, the term "self-managed" applies to any database that is installed either on-premises or on Amazon EC2. The term "AWS-managed" applies to any database on Amazon RDS, Amazon Aurora, or Amazon S3.

For additional details on working with MySQL-compatible databases and AWS DMS, see the following sections.

**Topics**
+ [Migrating from MySQL to MySQL using AWS DMS](#CHAP_Source.MySQL.Homogeneous)
+ [Using any MySQL-compatible database as a source for AWS DMS](#CHAP_Source.MySQL.Prerequisites)
+ [Using a self-managed MySQL-compatible database as a source for AWS DMS](#CHAP_Source.MySQL.CustomerManaged)
+ [Using an AWS-managed MySQL-compatible database as a source for AWS DMS](#CHAP_Source.MySQL.AmazonManaged)
+ [Considerations for Aurora MySQL 8.4 sources](#CHAP_Source.MySQL.AuroraMySQL84)
+ [Limitations on using a MySQL database as a source for AWS DMS](#CHAP_Source.MySQL.Limitations)
+ [Support for XA transactions](#CHAP_Source.MySQL.XA)
+ [Endpoint settings when using MySQL as a source for AWS DMS](#CHAP_Source.MySQL.ConnectionAttrib)
+ [Source data types for MySQL](#CHAP_Source.MySQL.DataTypes)

**Note**  
When configuring AWS Database Migration Service (AWS DMS) mapping rules, it is important to avoid using wildcards (%) for database or schema names. Instead, you must explicitly specify only the user-created databases that need to be migrated. Using a wildcard character includes all databases in the migration process, including system databases which are not required on the target instance. Since the MySQL Amazon RDS master user lacks the necessary permissions to import data into target system databases, attempting to migrate these system databases fails.

## Migrating from MySQL to MySQL using AWS DMS
<a name="CHAP_Source.MySQL.Homogeneous"></a>

For a heterogeneous migration, where you are migrating from a database engine other than MySQL to a MySQL database, AWS DMS is almost always the best migration tool to use. But for a homogeneous migration, where you are migrating from a MySQL database to a MySQL database, we recommend that you use a homogeneous data migrations migration project. homogeneous data migrations uses native database tools to provide an improved data migration performance and accuracy when compared to AWS DMS.

## Using any MySQL-compatible database as a source for AWS DMS
<a name="CHAP_Source.MySQL.Prerequisites"></a>

Before you begin to work with a MySQL database as a source for AWS DMS, make sure that you have the following prerequisites. These prerequisites apply to either self-managed or AWS-managed sources.

You must have an account for AWS DMS that has the Replication Admin role. The role needs the following privileges:
+ **REPLICATION CLIENT** – This privilege is required for CDC tasks only. In other words, full-load-only tasks don't require this privilege. 
**Note**  
For MariaDB version 10.5.2\+, you can use BINLOG MONITOR – it is a replacement for REPLICATION CLIENT.
+ **REPLICATION SLAVE** – This privilege is required for CDC tasks only. In other words, full-load-only tasks don't require this privilege.
+ **SUPER** – This privilege is required only in MySQL versions before 5.6.6.

The AWS DMS user must also have SELECT privileges for the source tables designated for replication.

Grant the following privileges if you use MySQL-specific premigration assessments:

```
grant select on mysql.user to <dms_user>;
grant select on mysql.db to <dms_user>;
grant select on mysql.tables_priv to <dms_user>;
grant select on mysql.role_edges to <dms_user>  #only for MySQL version 8.0.11 and higher
grant select on performance_schema.replication_connection_status to <dms_user>;  #Required for primary instance validation - MySQL version 5.7 and higher only
```

If you're using an RDS source and plan to run MySQL-specific premigration assessments, add the following permission:

```
grant select on mysql.rds_configuration to <dms_user>;  #Required for binary log retention check
```

If parameter `BatchEnable` is `true` it is required to grant:

```
grant create temporary tables on `<schema>`.* to <dms_user>;
```

## Using a self-managed MySQL-compatible database as a source for AWS DMS
<a name="CHAP_Source.MySQL.CustomerManaged"></a>

You can use the following self-managed MySQL-compatible databases as sources for AWS DMS:
+ MySQL Community Edition
+ MySQL Standard Edition
+ MySQL Enterprise Edition
+ MySQL Cluster Carrier Grade Edition
+ MariaDB Community Edition
+ MariaDB Enterprise Edition
+ MariaDB Column Store

To use CDC, make sure to enable binary logging. To enable binary logging, the following parameters must be configured in MySQL's `my.ini` (Windows) or `my.cnf` (UNIX) file.


| Parameter | Value | 
| --- | --- | 
| `server_id` | Set this parameter to a value of 1 or greater. | 
| `log-bin` | Set the path to the binary log file, such as `log-bin=E:\MySql_Logs\BinLog`. Don't include the file extension. | 
| `binlog_format` | Set this parameter to `ROW`. We recommend this setting during replication because in certain cases when `binlog_format` is set to `STATEMENT`, it can cause inconsistency when replicating data to the target. The database engine also writes similar inconsistent data to the target when `binlog_format` is set to `MIXED`, because the database engine automatically switches to `STATEMENT`-based logging which can result in writing inconsistent data on the target database. | 
| `expire_logs_days`<br />or<br />`binlog_expire_logs_seconds` | *The expire\_logs\_days parameter is deprecated since MySQL 8.0 and removed in MySQL 8.4.* For more information, see [Server and Status Variables and Options Added, Deprecated, or Removed in MySQL 8.4 since 8.0](https://dev.mysql.com/doc/refman/8.4/en/added-deprecated-removed.html#optvars-removed).<br />Use the `expire_logs_days` parameter for MySQL 5.x. We recommend that you set this parameter to `1` or greater, see [Binary Logging Options and Variables](https://dev.mysql.com/doc/refman/5.7/en/replication-options-binary-log.html#sysvar_expire_logs_days).<br />Use the `binlog_expire_logs_seconds` parameter for MySQL 8.0 and later. We recommend that you set this parameter to a value of `86400` seconds (1 day) or greater. See [Binary Logging Options and Variables](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_expire_logs_seconds). | 
| `binlog_checksum` | Set this parameter to `NONE` for DMS version 3.4.7 or prior. | 
| `binlog_row_image` | Set this parameter to `FULL`. | 
| `log_slave_updates` | Set this parameter to `TRUE` if you are using a MySQL or MariaDB read-replica as a source. | 

If you are using a MySQL or MariaDB read-replica as a source for a DMS migration task using **Migrate existing data and replicate ongoing changes** mode, there is a possibility of data loss. DMS won't write a transaction during either full load or CDC under the following conditions:
+ The transaction had been committed to the primary instance before the DMS task started.
+ The transaction hadn't been committed to the replica until after the DMS task started, due to lag between the primary instance and the replica.

The longer the lag between the primary instance and the replica, the greater potential there is for data loss.

If your source uses the NDB (clustered) database engine, the following parameters must be configured to enable CDC on tables that use that storage engine. Add these changes in MySQL's `my.ini` (Windows) or `my.cnf` (UNIX) file.


| Parameter | Value | 
| --- | --- | 
| `ndb_log_bin` | Set this parameter to `ON`. This value ensures that changes in clustered tables are logged to the binary log. | 
| `ndb_log_update_as_write` | Set this parameter to `OFF`. This value prevents writing UPDATE statements as INSERT statements in the binary log. | 
| `ndb_log_updated_only` | Set this parameter to `OFF`. This value ensures that the binary log contains the entire row and not just the changed columns. | 

## Using an AWS-managed MySQL-compatible database as a source for AWS DMS
<a name="CHAP_Source.MySQL.AmazonManaged"></a>

You can use the following AWS-managed MySQL-compatible databases as sources for AWS DMS:
+ MySQL Community Edition
+ MariaDB Community Edition
+ Amazon Aurora MySQL-Compatible Edition

When using an AWS-managed MySQL-compatible database as a source for AWS DMS, make sure that you have the following prerequisites for CDC:
+ To enable binary logs for RDS for MySQL and for RDS for MariaDB, enable automatic backups at the instance level. To enable binary logs for an Aurora MySQL cluster, change the variable `binlog_format` in the parameter group.

  For more information about setting up automatic backups, see [Working with automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html) in the *Amazon RDS User Guide*.

  For more information about setting up binary logging for an Amazon RDS for MySQL database, see [ Setting the binary logging format](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MySQL.BinaryFormat.html) in the *Amazon RDS User Guide*. 

  For more information about setting up binary logging for an Aurora MySQL cluster, see [ How do I turn on binary logging for my Amazon Aurora MySQL cluster?](https://aws.amazon.com/premiumsupport/knowledge-center/enable-binary-logging-aurora/). 
+ If you plan to use CDC, turn on binary logging. For more information on setting up binary logging for an Amazon RDS for MySQL database, see [Setting the binary logging format](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MySQL.BinaryFormat.html) in the *Amazon RDS User Guide*.
+ Ensure that the binary logs are available to AWS DMS. Because AWS-managed MySQL-compatible databases purge the binary logs as soon as possible, you should increase the length of time that the logs remain available. For example, to increase log retention to 24 hours, run the following command. 

  ```
   call mysql.rds_set_configuration('binlog retention hours', 24);
  ```
+ Set the `binlog_format` parameter to `"ROW"`.
**Note**  
On MySQL or MariaDB, `binlog_format` is a dynamic parameter, so you don't have to reboot to make the new value take effect. However, the new value will only apply to new sessions. If you switch the `binlog_format` to `ROW` for replication purposes, your database can still create subsequent binary logs using the `MIXED` format, if those sessions started before you changed the value. This may prevent AWS DMS from properly capturing all changes on the source database. When you change the `binlog_format` setting on a MariaDB or MySQL database, be sure to restart the database to close all existing sessions, or restart any application performing DML (Data Manipulation Language) operations. Forcing your database to restart all sessions after changing the `binlog_format` parameter to `ROW` will ensure that your database writes all subsequent source database changes using the correct format, so that AWS DMS can properly capture those changes.
+ Set the `binlog_row_image` parameter to `"Full"`. 
+ Set the `binlog_checksum` parameter to `"NONE"` for DMS version 3.4.7 or prior. For more information about setting parameters in Amazon RDS MySQL, see [Working with automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html) in the *Amazon RDS User Guide*.
+ If you are using an Amazon RDS MySQL or Amazon RDS MariaDB read replica as a source, enable backups on the read replica, and ensure the `log_slave_updates` parameter is set to `TRUE`.

For more information about Aurora MySQL 8.4 security changes, see [Security with Amazon Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Security.html) and [Password management with Amazon Aurora and Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html) in the *Amazon Aurora User Guide*.

## Considerations for Aurora MySQL 8.4 sources
<a name="CHAP_Source.MySQL.AuroraMySQL84"></a>

Aurora MySQL 8.4 introduces security changes that may affect AWS DMS source endpoint connectivity. Review the following before upgrading your Aurora MySQL source to version 8.4.

**TLS enforcement**

Aurora MySQL 8.4 sets `require_secure_transport` to `ON` by default, meaning all connections must use TLS. If your AWS DMS source endpoint connects to Aurora MySQL 8.4 and the SSL mode is set to **none**, connections will be rejected. If your endpoint SSL mode is set to **none**, you will receive the following error: `MySQL Error 3159 (HY000): Connections using insecure transport are prohibited while --require_secure_transport=ON`. Set the endpoint SSL mode to **verify-ca** or **verify-full**. Both modes require a CA certificate. Alternatively, set `require_secure_transport` to `OFF` in your Aurora cluster parameter group to allow unencrypted connections.

**Note**  
Aurora MySQL 8.4 only supports GCM cipher suites for TLS 1.2. All CBC-mode ciphers have been removed. AWS DMS uses TLS 1.2 for MySQL and Aurora MySQL endpoints and will auto-negotiate a supported GCM cipher. If you have custom cipher configurations, verify they include one of the following supported ciphers: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-ECDSA-AES128-GCM-SHA256, or ECDHE-ECDSA-AES256-GCM-SHA384.

**Note**  
AWS DMS does not support TLS 1.3 for MySQL endpoints. This does not affect connectivity to Aurora MySQL 8.4, as Aurora MySQL 8.4 continues to support TLS 1.2.

**Authentication (Aurora MySQL and RDS for MySQL 8.4)**

Aurora MySQL 8.4 replaces the `default_authentication_plugin` parameter with `authentication_policy`, which defaults to `*:caching_sha2_password`. Existing database users retain their current authentication plugin after the upgrade. If you create new AWS DMS endpoint users after upgrading, they will use `caching_sha2_password` by default unless you set `authentication_policy` to `*:mysql_native_password` in your cluster parameter group.

**Master user password reset**

After upgrading to Aurora MySQL 8.4, resetting the master user password via the AWS Management Console, CLI, or through Secrets Manager rotation sets the master user’s authentication plugin to the default defined by the `authentication_policy` parameter. If `authentication_policy` is set to its default value (`*:caching_sha2_password`), the master user’s authentication plugin changes from `mysql_native_password` to `caching_sha2_password` upon the next password reset.

If your AWS DMS source endpoint uses the master user account, verify connectivity after any password reset. To avoid authentication plugin changes, either:
+ Set `authentication_policy` to `*:mysql_native_password` in your cluster parameter group before resetting the password, or
+ Create a dedicated AWS DMS endpoint user with an explicitly specified authentication plugin (recommended). For example: `CREATE USER 'dms_user'@'%' IDENTIFIED WITH mysql_native_password BY 'password';`

## Limitations on using a MySQL database as a source for AWS DMS
<a name="CHAP_Source.MySQL.Limitations"></a>

When using a MySQL database as a source, consider the following:
+  Change data capture (CDC) isn't supported for Amazon RDS MySQL 5.5 or lower. For Amazon RDS MySQL, you must use version 5.6, 5.7, or 8.0 to enable CDC. CDC is supported for self-managed MySQL 5.5 sources. 
+ For CDC, `CREATE TABLE`, `ADD COLUMN`, and `DROP COLUMN` changing the column data type, and `renaming a column` are supported. However, `DROP TABLE`, `RENAME TABLE`, and updates made to other attributes, such as column default value, column nullability, character set and so on, are not supported.
+  For partitioned tables on the source, when you set **Target table preparation mode** to **Drop tables on target**, AWS DMS creates a simple table without any partitions on the MySQL target. To migrate partitioned tables to a partitioned table on the target, precreate the partitioned tables on the target MySQL database.
+  Using an `ALTER TABLE {{table_name}} ADD COLUMN {{column_name}}` statement to add columns to the beginning (FIRST) or the middle of a table (AFTER) isn't supported for relational targets. Columns are always added to the end of the table. When the target is Amazon S3 or Amazon Kinesis Data Streams, adding columns using FIRST or AFTER is supported.
+ CDC isn't supported when a table name contains uppercase and lowercase characters, and the source engine is hosted on an operating system with case-insensitive file names. An example is Microsoft Windows or OS X using HFS\+.
+ You can use Aurora MySQL-Compatible Edition Serverless v1 for full load, but you can't use it for CDC. This is because you can't enable the prerequisites for MySQL. For more information, see [ Parameter groups and Aurora Serverless v1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.how-it-works.html#aurora-serverless.parameter-groups). 

  Aurora MySQL-Compatible Edition Serverless v2 supports CDC.
+  The AUTO\_INCREMENT attribute on a column isn't migrated to a target database column.
+  Capturing changes when the binary logs aren't stored on standard block storage isn't supported. For example, CDC does not work when the binary logs are stored on Amazon S3.
+  AWS DMS creates target tables with the InnoDB storage engine by default. If you need to use a storage engine other than InnoDB, you must manually create the table and migrate to it using [do nothing](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html) mode.
+ You can't use Aurora MySQL replicas as a source for AWS DMS unless your DMS migration task mode is **Migrate existing data**—full load only.
+  If the MySQL-compatible source is stopped during full load, the AWS DMS task does not stop with an error. The task ends successfully, but the target might be out of sync with the source. If this happens, either restart the task or reload the affected tables.
+  Indexes created on a portion of a column value aren't migrated. For example, the index CREATE INDEX first\_ten\_chars ON customer (name(10)) isn't created on the target.
+ In some cases, the task is configured to not replicate LOBs ("SupportLobs" is false in task settings or **Don't include LOB columns** is chosen in the task console). In these cases, AWS DMS does not migrate any MEDIUMBLOB, LONGBLOB, MEDIUMTEXT, and LONGTEXT columns to the target.

  BLOB, TINYBLOB, TEXT, and TINYTEXT columns aren't affected and are migrated to the target.
+ Temporal data tables or system—versioned tables are not supported on MariaDB source and target databases.
+ If migrating between two Amazon RDS Aurora MySQL clusters, the RDS Aurora MySQL source endpoint must be a read/write instance, not a replica instance. 
+ AWS DMS currently does not support views migration for MariaDB.
+ AWS DMS does not support DDL changes for partitioned tables for MySQL. To skip table suspension for partition DDL changes during CDC, set `skipTableSuspensionForPartitionDdl` to `true`.
+ AWS DMS only supports XA transactions in version 3.5.0 and higher. Previous versions do not support XA transactions. AWS DMS does not support XA transactions in MariaDB version 10.6 or higher For more information, see [Support for XA transactions](#CHAP_Source.MySQL.XA) following.
+ AWS DMS does not use GTIDs for replication, even if the source data contains them. 
+ AWS DMS does not support Aurora MySQL enhanced binary log.
+ AWS DMS does not support binary log transaction compression.
+ AWS DMS does not propagate ON DELETE CASCADE and ON UPDATE CASCADE events for MySQL databases using the InnoDB storage engine. For these events, MySQL does not generate binlog events to reflect the cascaded operations on the child tables. Consequently, AWS DMS can't replicate the corresponding changes to the child tables. For more information, see [Indexes, Foreign Keys, or Cascade Updates or Deletes Not Migrated](CHAP_Troubleshooting.md#CHAP_Troubleshooting.MySQL.FKsAndIndexes).
+ AWS DMS does not capture changes to computed (`VIRTUAL` and `GENERATED ALWAYS`) columns. To work around this limitation, do the following:
  + Pre-create the target table in the target database, and create the AWS DMS task with the `DO_NOTHING` or `TRUNCATE_BEFORE_LOAD` full-load task setting.
  + Add a transformation rule to remove the computed column from the task scope. For information about transformation rules, see [Transformation rules and actions](CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Transformations.md).
+ Due to internal MySQL limitation, AWS DMS can process BINLOGs no larger than 4GB size. BINLOGs larger than 4GB may result in DMS task failures or other unpredictable behavior. You must reduce the size of transactions to avoid BINLOGs larger than 4GB.
+ AWS DMS does not support back-ticks (```) or single quotes (`'`) in schema, table, and column names.
+ AWS DMS does not migrate data from invisible columns in your source database. To include these columns in your migration scope, use the ALTER TABLE statement to make these columns visible.

## Support for XA transactions
<a name="CHAP_Source.MySQL.XA"></a>

An Extended Architecture (XA) transaction is a transaction that can be used to group a series of operations from multiple transactional resources into a single, reliable global transaction. An XA transaction uses a two-phase commit protocol. In general, capturing changes while there are open XA transactions might lead to loss of data. If your database does not use XA transactions, you can ignore this permission and the configuration `IgnoreOpenXaTransactionsCheck` by using the default value `TRUE`. To start replicating from a source that has XA transactions, do the following:
+ Ensure that the AWS DMS endpoint user has the following permission:

  ```
  grant XA_RECOVER_ADMIN on *.* to 'userName'@'%';
  ```
+ Set the endpoint setting `IgnoreOpenXaTransactionsCheck` to `false`.

**Note**  
AWS DMS doesn’t support XA transactions on MariaDB Source DB version 10.6 or higher.

## Endpoint settings when using MySQL as a source for AWS DMS
<a name="CHAP_Source.MySQL.ConnectionAttrib"></a>

You can use endpoint settings to configure your MySQL source database similar to using extra connection attributes. You specify the settings when you create the source endpoint using the AWS DMS console, or by using the `create-endpoint` command in the [AWS CLI](https://docs.aws.amazon.com/cli/latest/reference/dms/index.html), with the `--my-sql-settings '{"{{EndpointSetting"}}: {{"value"}}, {{...}}}'` JSON syntax.

The following table shows the endpoint settings that you can use with MySQL as a source.


| Name | Description | 
| --- | --- | 
| `ConnectionTimeout` | Use this extra connection attribute (ECA) to set the endpoint connection timeout for the MySQL instance, in seconds. The default value is 10 seconds. ECA Example: `ConnectionTimeout=30`. | 
| EventsPollInterval | Specifies how often to check the binary log for new changes/events when the database is idle. <br />Default value: 5 <br />Valid values: 1–60 <br />Example: `--my-sql-settings '{"EventsPollInterval": 5}'`<br />In the example, AWS DMS checks for changes in the binary logs every five seconds. | 
| ExecuteTimeout | For AWS DMS versions 3.4.7 and higher, sets the client statement timeout for a MySQL source endpoint, in seconds.<br />Default value: 60 <br />Example: `--my-sql-settings '{"ExecuteTimeout": 1500}'` | 
| ServerTimezone | Specifies the time zone for the source MySQL database.<br />Example: `--my-sql-settings '{"ServerTimezone": "{{US/Pacific}}"}'` | 
| AfterConnectScript | Specifies a script to run immediately after AWS DMS connects to the endpoint. The migration task continues running regardless if the SQL statement succeeds or fails. <br />Valid values: One or more valid SQL statements, set off by a semicolon. <br />Example: `--my-sql-settings '{"AfterConnectScript": "ALTER SESSION SET CURRENT_SCHEMA=system"}'` | 
|  CleanSourceMetadataOnMismatch  | Cleans and recreates table metadata information on the replication instance when a mismatch occurs. For example, in a situation where running an alter DDL on the table could result in different information about the table cached in the replication instance. Boolean.<br />Default value: `false`<br />Example: `--my-sql-settings '{"CleanSourceMetadataOnMismatch": false}'` | 
|  skipTableSuspensionForPartitionDdl  | AWS DMS does not support DDL changes for partitioned tables for MySQL. For AWS DMS versions 3.4.6 and higher, setting this to `true` skips table suspension for partition DDL changes during CDC. AWS DMS ignores partitioned-table-related DDL, and continues to process further binary log changes. <br />Default value: `false`<br />Example: `--my-sql-settings '{"skipTableSuspensionForPartitionDdl": true}'` | 
|  IgnoreOpenXaTransactionsCheck  | For AWS DMS versions 3.5.0 and higher, specifies whether tasks should ignore open XA transactions while starting. Set this to `false` if your source has XA transactions.<br />Default value: `true`<br />Example: `--my-sql-settings '{"IgnoreOpenXaTransactionsCheck": false}'` | 

## Source data types for MySQL
<a name="CHAP_Source.MySQL.DataTypes"></a>

The following table shows the MySQL database source data types that are supported when using AWS DMS and the default mapping from AWS DMS data types.

For information on how to view the data type that is mapped in the target, see the section for the target endpoint you are using.

For additional information about AWS DMS data types, see [Data types for AWS Database Migration Service](CHAP_Reference.DataTypes.md).


|  MySQL data types  |  AWS DMS data types  | 
| --- | --- | 
| INT | INT4 | 
| BIGINT | INT8 | 
| MEDIUMINT | INT4 | 
| TINYINT | INT1 | 
| SMALLINT | INT2 | 
| UNSIGNED TINYINT | UINT1 | 
| UNSIGNED SMALLINT | UINT2 | 
| UNSIGNED MEDIUMINT | UINT4 | 
| UNSIGNED INT | UINT4 | 
| UNSIGNED BIGINT | UINT8 | 
| DECIMAL(10) | NUMERIC (10,0) | 
| BINARY | BYTES(1) | 
| BIT | BOOLEAN | 
| BIT(64) | BYTES(8) | 
| BLOB | BYTES(65535) | 
| LONGBLOB | BLOB | 
| MEDIUMBLOB | BLOB | 
| TINYBLOB | BYTES(255) | 
| DATE | DATE | 
| DATETIME | DATETIME<br />DATETIME without a parenthetical value is replicated without milliseconds. DATETIME with a parenthetical value of 1 to 5 (such as `DATETIME(5)`) is replicated with milliseconds.<br />When replicating a DATETIME column, the time remains the same on the target. It is not converted to UTC. | 
| TIME | STRING | 
| TIMESTAMP | DATETIME<br />When replicating a TIMESTAMP column, the time is converted to UTC on the target. | 
| YEAR | INT2 | 
| DOUBLE | REAL8 | 
| FLOAT | REAL(DOUBLE)<br />If the FLOAT values are not in the range following, use a transformation to map FLOAT to STRING. For more information about transformations, see [Transformation rules and actions](CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Transformations.md).<br />The supported FLOAT range is -1.79E\+308 to -2.23E-308, 0, and 2.23E-308 to 1.79E\+308 | 
| VARCHAR (45) | WSTRING (45) | 
| VARCHAR (2000) | WSTRING (2000) | 
| VARCHAR (4000) | WSTRING (4000) | 
| VARBINARY (4000) | BYTES (4000) | 
| VARBINARY (2000) | BYTES (2000) | 
| CHAR | WSTRING | 
| TEXT | WSTRING | 
| LONGTEXT | NCLOB | 
| MEDIUMTEXT | NCLOB | 
| TINYTEXT | WSTRING(255) | 
| GEOMETRY | BLOB | 
| POINT | BLOB | 
| LINESTRING | BLOB | 
| POLYGON | BLOB | 
| MULTIPOINT | BLOB | 
| MULTILINESTRING | BLOB | 
| MULTIPOLYGON | BLOB | 
| GEOMETRYCOLLECTION | BLOB | 
| ENUM | WSTRING ({{length}})<br />Here, {{length}} is the length of the longest value in the ENUM. | 
| SET | WSTRING ({{length}})<br />Here, {{length}} is the total length of all values in the SET, including commas. | 
| JSON | CLOB | 

**Note**  
In some cases, you might specify the DATETIME and TIMESTAMP data types with a "zero" value (that is, 0000-00-00). If so, make sure that the target database in the replication task supports "zero" values for the DATETIME and TIMESTAMP data types. Otherwise, these values are recorded as null on the target.