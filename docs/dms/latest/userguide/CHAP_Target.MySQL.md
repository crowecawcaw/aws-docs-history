

# Using a MySQL-compatible database as a target for AWS Database Migration Service
<a name="CHAP_Target.MySQL"></a>

You can migrate data to any MySQL-compatible database using AWS DMS, from any of the source data engines that AWS DMS supports. If you are migrating to an on-premises MySQL-compatible database, then AWS DMS requires that your source engine reside within the AWS ecosystem. The engine can be on an AWS-managed service such as Amazon RDS, Amazon Aurora, or Amazon S3. Or the engine can be on a self-managed database on Amazon EC2. 

You can use SSL to encrypt connections between your MySQL-compatible endpoint and the replication instance. For more information on using SSL with a MySQL-compatible endpoint, see [Using SSL with AWS Database Migration Service](CHAP_Security.SSL.md). 

For information about versions of MySQL that AWS DMS supports as a target, see [Targets for AWS DMS](CHAP_Introduction.Targets.md).

You can use the following MySQL-compatible databases as targets for AWS DMS:
+ MySQL Community Edition
+ MySQL Standard Edition
+ MySQL Enterprise Edition
+ MySQL Cluster Carrier Grade Edition
+ MariaDB Community Edition
+ MariaDB Enterprise Edition
+ MariaDB Column Store
+ Amazon Aurora MySQL

**Note**  
Regardless of the source storage engine (MyISAM, MEMORY, and so on), AWS DMS creates a MySQL-compatible target table as an InnoDB table by default.   
If you need a table in a storage engine other than InnoDB, you can manually create the table on the MySQL-compatible target and migrate the table using the **Do nothing** option. For more information, see [Full-load task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.FullLoad.md).

For additional details on working with a MySQL-compatible database as a target for AWS DMS, see the following sections. 

**Topics**
+ [Using any MySQL-compatible database as a target for AWS Database Migration Service](#CHAP_Target.MySQL.Prerequisites)
+ [Considerations for Aurora MySQL 8.4 targets](#CHAP_Target.MySQL.AuroraMySQL84)
+ [Limitations on using a MySQL-compatible database as a target for AWS Database Migration Service](#CHAP_Target.MySQL.Limitations)
+ [Endpoint settings when using a MySQL-compatible database as a target for AWS DMS](#CHAP_Target.MySQL.ConnectionAttrib)
+ [Target data types for MySQL](#CHAP_Target.MySQL.DataTypes)

## Using any MySQL-compatible database as a target for AWS Database Migration Service
<a name="CHAP_Target.MySQL.Prerequisites"></a>

Before you begin to work with a MySQL-compatible database as a target for AWS DMS, make sure that you have completed the following prerequisites:
+ Provide a user account to AWS DMS that has read/write privileges to the MySQL-compatible database. To create the necessary privileges, run the following commands.

  ```
  CREATE USER '<user acct>'@'%' IDENTIFIED BY '<user password>';
  GRANT ALTER, CREATE, DROP, INDEX, INSERT, UPDATE, DELETE, SELECT, CREATE TEMPORARY TABLES  ON <schema>.* TO 
  '<user acct>'@'%';
  GRANT ALL PRIVILEGES ON awsdms_control.* TO '<user acct>'@'%';
  ```
+ During the full-load migration phase, you must disable foreign keys on your target tables. To disable foreign key checks on a MySQL-compatible database during a full load, you can add the following command to the **Extra connection attributes** section of the AWS DMS console for your target endpoint.

  ```
  Initstmt=SET FOREIGN_KEY_CHECKS=0;
  ```
+ Set the database parameter `local_infile = 1` to enable AWS DMS to load data into the target database.
+ Grant the following privileges if you use MySQL-specific premigration assessments.

  ```
  grant select on mysql.user to <dms_user>;
  grant select on mysql.db to <dms_user>;
  grant select on mysql.tables_priv to <dms_user>;
  grant select on mysql.role_edges to <dms_user>  #only for MySQL version 8.0.11 and higher
  ```

## Considerations for Aurora MySQL 8.4 targets
<a name="CHAP_Target.MySQL.AuroraMySQL84"></a>

Aurora MySQL 8.4 introduces security changes that may affect AWS DMS target endpoint connectivity. Review the following before upgrading your Aurora MySQL target to version 8.4.

**TLS enforcement**

Aurora MySQL 8.4 sets `require_secure_transport` to `ON` by default, meaning all connections must use TLS. If your AWS DMS target endpoint connects to Aurora MySQL 8.4 and the SSL mode is set to **none**, connections will be rejected. If your endpoint SSL mode is set to **none**, you will receive the following error: `MySQL Error 3159 (HY000): Connections using insecure transport are prohibited while --require_secure_transport=ON`. Set the endpoint SSL mode to **verify-ca** or **verify-full**. Both modes require a CA certificate. Alternatively, set `require_secure_transport` to `OFF` in your Aurora cluster parameter group to allow unencrypted connections.

**Note**  
Aurora MySQL 8.4 only supports GCM cipher suites for TLS 1.2. All CBC-mode ciphers have been removed. AWS DMS uses TLS 1.2 for MySQL and Aurora MySQL endpoints and will auto-negotiate a supported GCM cipher. If you have custom cipher configurations, verify they include one of the following supported ciphers: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-ECDSA-AES128-GCM-SHA256, or ECDHE-ECDSA-AES256-GCM-SHA384.

**Note**  
AWS DMS does not support TLS 1.3 for MySQL endpoints. This does not affect connectivity to Aurora MySQL 8.4, as Aurora MySQL 8.4 continues to support TLS 1.2.

**Authentication (Aurora MySQL and RDS for MySQL 8.4)**

Aurora MySQL 8.4 replaces the `default_authentication_plugin` parameter with `authentication_policy`, which defaults to `*:caching_sha2_password`. Existing database users retain their current authentication plugin after the upgrade. If you create new AWS DMS endpoint users after upgrading, they will use `caching_sha2_password` by default unless you set `authentication_policy` to `*:mysql_native_password` in your cluster parameter group.

**Master user password reset**

After upgrading to Aurora MySQL 8.4, resetting the master user password via the AWS Management Console, CLI, or through Secrets Manager rotation sets the master user’s authentication plugin to the default defined by the `authentication_policy` parameter. If `authentication_policy` is set to its default value (`*:caching_sha2_password`), the master user’s authentication plugin changes from `mysql_native_password` to `caching_sha2_password` upon the next password reset.

If your AWS DMS target endpoint uses the master user account, verify connectivity after any password reset. To avoid authentication plugin changes, either:
+ Set `authentication_policy` to `*:mysql_native_password` in your cluster parameter group before resetting the password, or
+ Create a dedicated AWS DMS endpoint user with an explicitly specified authentication plugin (recommended). For example: `CREATE USER 'dms_user'@'%' IDENTIFIED WITH mysql_native_password BY 'password';`

For more information about Aurora MySQL 8.4 security changes, see [Security with Amazon Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Security.html) and [Password management with Amazon Aurora and Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html) in the *Amazon Aurora User Guide*. For information about authentication plugin known issues, see [Authentication plugin](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.KnownIssuesAndLimitations.html#MySQL.Concepts.KnownIssuesAndLimitations.authentication-plugin) in the *Amazon RDS User Guide*.

## Limitations on using a MySQL-compatible database as a target for AWS Database Migration Service
<a name="CHAP_Target.MySQL.Limitations"></a>

When using a MySQL database as a target, AWS DMS doesn't support the following:
+ The data definition language (DDL) statements TRUNCATE PARTITION, DROP TABLE, and RENAME TABLE.
+ Using an `ALTER TABLE {{table_name}} ADD COLUMN {{column_name}}` statement to add columns to the beginning or the middle of a table.
+ When loading data to a MySQL-compatible target in a full load task, AWS DMS doesn't report errors caused by constraints in the task logs, which can cause duplicate key errors or mismatches with the number of records. This is caused by the way MySQL handles local data with the `LOAD DATA` command. Be sure to do the following during the full load phase: 
  + Disable constraints
  + Use AWS DMS validation to make sure the data is consistent.
+ When you update a column's value to its existing value, MySQL-compatible databases return a `0 rows affected` warning. Although this behavior isn't technically an error, it is different from how the situation is handled by other database engines. For example, Oracle performs an update of one row. For MySQL-compatible databases, AWS DMS generates an entry in the awsdms\_apply\_exceptions control table and logs the following warning.

  ```
  Some changes from the source database had no impact when applied to
  the target database. See awsdms_apply_exceptions table for details.
  ```
+ Aurora Serverless is available as a target for Amazon Aurora version 2, compatible with MySQL version 5.7. (Select Aurora MySQL version 2.07.1 to be able to use Aurora Serverless with MySQL 5.7 compatibility.) For more information about Aurora Serverless, see [Using Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html) in the *Amazon Aurora User Guide*.
+ AWS DMS does not support using a reader endpoint for Aurora or Amazon RDS, unless the instances are in writable mode, that is, the `read_only` and `innodb_read_only` parameters are set to `0` or `OFF`. For more information about using Amazon RDS and Aurora as targets, see the following:
  +  [ Determining which DB instance you are connected to](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.html#AuroraMySQL.BestPractices.DeterminePrimaryInstanceConnection) 
  +  [ Updating read replicas with MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MySQL.Replication.ReadReplicas.html#USER_MySQL.Replication.ReadReplicas.Updates) 
+ When replicating TIME datatype, fractional part of time value is not replicated.
+ When replicating TIME datatype with Extra Connection Attribute `loadUsingCSV=false`, the time value is capped to range `[00:00:00, 23:59:59]`.

## Endpoint settings when using a MySQL-compatible database as a target for AWS DMS
<a name="CHAP_Target.MySQL.ConnectionAttrib"></a>

You can use endpoint settings to configure your MySQL-compatible target database similar to using extra connection attributes. You specify the settings when you create the target endpoint using the AWS DMS console, or by using the `create-endpoint` command in the [AWS CLI](https://docs.aws.amazon.com/cli/latest/reference/dms/index.html), with the `--my-sql-settings '{"{{EndpointSetting"}}: {{"value"}}, {{...}}}'` JSON syntax.

The following table shows the endpoint settings that you can use with MySQL as a target.


| Name | Description | 
| --- | --- | 
| `ConnectionTimeout` | Use this extra connection attribute (ECA) to set the endpoint connection timeout for the MySQL instance, in seconds. The default value is 10 seconds. ECA Example: `ConnectionTimeout=30`. | 
| ` TargetDbType` | Specifies where to migrate source tables on the target, either to a single database or multiple databases. If you specify `SPECIFIC_DATABASE`, you need to specify the database name, either when using the AWS CLI or the AWS Management Console.<br />Default value: `MULTIPLE_DATABASES`<br />Valid values: {`SPECIFIC_DATABASE`, `MULTIPLE_DATABASES`} <br />Example: `--my-sql-settings '{"TargetDbType": "MULTIPLE_DATABASES"}'` | 
| `ParallelLoadThreads` | Improves performance when loading data into the MySQL-compatible target database. Specifies how many threads to use to load the data into the MySQL-compatible target database. Setting a large number of threads can have an adverse effect on database performance, because a separate connection is required for each thread. <br />Default value: 1 <br />Valid values: 1–5 <br />Example: `--my-sql-settings '{"ParallelLoadThreads": 1}'` | 
| `AfterConnectScript` | Specifies a script to run immediately after AWS DMS connects to the endpoint.<br />For example, you can specify that the MySQL-compatible target should translate received statements into the latin1 character set, which is the default compiled-in character set of the database. This parameter typically improves performance when converting from UTF8 clients.<br />Example: `--my-sql-settings '{"AfterConnectScript": "SET character_set_connection='latin1'"}'` | 
| `MaxFileSize` | Specifies the maximum size (in KB) of any .csv file used to transfer data to a MySQL-compatible database.<br />Default value: 32,768 KB (32 MB)<br />Valid values: 1–1,048,576<br />`--my-sql-settings '{"MaxFileSize": 512}'` | 

You can also use extra connection attributes to configure your MySQL-compatible target database.

The following table shows the extra connection attributes that you can use with MySQL as a target.


| Name | Description | 
| --- | --- | 
| `Initstmt=SET FOREIGN_KEY_CHECKS=0;` | Disables foreign key checks.<br />Example: `--extra-connection-attributes "Initstmt=SET FOREIGN_KEY_CHECKS=0;"` | 
| `Initstmt=SET time_zone` | Specifies the time zone for the target MySQL-compatible database. <br />Default value: UTC <br />Valid values: The time zone names available in the target MySQL database.<br />Example: `--extra-connection-attributes "Initstmt=SET time_zone={{US/Pacific}};"` | 

Alternatively, you can use the `AfterConnectScript` parameter of the `--my-sql-settings` command to disable foreign key checks and specify the time zone for your database.

## Target data types for MySQL
<a name="CHAP_Target.MySQL.DataTypes"></a>

The following table shows the MySQL database target data types that are supported when using AWS DMS and the default mapping from AWS DMS data types.

For additional information about AWS DMS data types, see [Data types for AWS Database Migration Service](CHAP_Reference.DataTypes.md).


|  AWS DMS data types  |  MySQL data types  | 
| --- | --- | 
| BOOLEAN | BOOLEAN | 
| BYTES | If the length is from 1 through 65,535, then use VARBINARY (length). <br />If the length is from 65,536 through 2,147,483,647, then use LONGLOB. | 
| DATE | DATE | 
| TIME | TIME | 
| TIMESTAMP | "If scale is => 0 and =< 6, then: DATETIME (Scale)<br />If scale is => 7 and =< 9, then: VARCHAR (37)" | 
| INT1 | TINYINT | 
| INT2 | SMALLINT | 
| INT4 | INTEGER | 
| INT8 | BIGINT | 
| NUMERIC | DECIMAL (p,s) | 
| REAL4 | FLOAT | 
| REAL8 | DOUBLE PRECISION | 
| STRING | If the length is from 1 through 21,845, then use VARCHAR (length).<br />If the length is from 21,846 through 2,147,483,647, then use LONGTEXT. | 
| UINT1 | UNSIGNED TINYINT | 
| UINT2 | UNSIGNED SMALLINT | 
| UINT4 | UNSIGNED INTEGER | 
| UINT8 | UNSIGNED BIGINT | 
| WSTRING | If the length is from 1 through 32,767, then use VARCHAR (length). <br />If the length is from 32,768 through 2,147,483,647, then use LONGTEXT. | 
| BLOB | If the length is from 1 through 65,535, then use BLOB.<br />If the length is from 65,536 through 2,147,483,647, then use LONGBLOB.<br />If the length is 0, then use LONGBLOB (full LOB support). | 
| NCLOB | If the length is from 1 through 65,535, then use TEXT.<br />If the length is from 65,536 through 2,147,483,647, then use LONGTEXT with ucs2 for CHARACTER SET.<br />If the length is 0, then use LONGTEXT (full LOB support) with ucs2 for CHARACTER SET. | 
| CLOB | If the length is from 1 through 65,535, then use TEXT.<br />If the length is from 65,536 through 2147483647, then use LONGTEXT.<br />If the length is 0, then use LONGTEXT (full LOB support). | 