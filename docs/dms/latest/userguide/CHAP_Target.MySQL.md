# Using a MySQL-compatible database as a target for AWS Database Migration Service

You can migrate data to any MySQL-compatible database using AWS DMS, from any of the
source data engines that AWS DMS supports. If you are migrating to an on-premises
MySQL-compatible database, then AWS DMS requires that your source engine reside within the
AWS ecosystem. The engine can be on an AWS-managed service such as Amazon RDS, Amazon
Aurora, or Amazon S3. Or the engine can be on a self-managed database on Amazon EC2.

You can use SSL to encrypt connections between your MySQL-compatible endpoint and the
replication instance. For more information on using SSL with a MySQL-compatible
endpoint, see [Using SSL with AWS Database Migration Service](CHAP_Security.SSL.md "CHAP_Security.SSL.md").

For information about versions
of MySQL that AWS DMS supports as a target, see [Targets for AWS DMS](CHAP_Introduction.Targets.md "CHAP_Introduction.Targets.md").

You can use the following MySQL-compatible databases as targets for AWS DMS:

- MySQL Community Edition
- MySQL Standard Edition
- MySQL Enterprise Edition
- MySQL Cluster Carrier Grade Edition
- MariaDB Community Edition
- MariaDB Enterprise Edition
- MariaDB Column Store
- Amazon Aurora MySQL

###### Note

Regardless of the source storage engine (MyISAM, MEMORY, and so on), AWS DMS
creates a MySQL-compatible target table as an InnoDB table by default.

If you need a table in a storage engine other than InnoDB, you can manually create
the table on the MySQL-compatible target and migrate the table using the
**Do nothing** option. For more information, see [Full-load task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.FullLoad.md "CHAP_Tasks.CustomizingTasks.TaskSettings.FullLoad.md").

For additional details on working with a MySQL-compatible database as a target for
AWS DMS, see the following sections.

###### Topics

- [Using any MySQL-compatible database as a target for AWS Database Migration Service](#CHAP_Target.MySQL.Prerequisites "#CHAP_Target.MySQL.Prerequisites")
- [Limitations on using a MySQL-compatible database as a target for AWS Database Migration Service](#CHAP_Target.MySQL.Limitations "#CHAP_Target.MySQL.Limitations")
- [Endpoint settings when using a MySQL-compatible database as a target for AWS DMS](#CHAP_Target.MySQL.ConnectionAttrib "#CHAP_Target.MySQL.ConnectionAttrib")
- [Target data types for MySQL](#CHAP_Target.MySQL.DataTypes "#CHAP_Target.MySQL.DataTypes")

## Using any MySQL-compatible database as a target for AWS Database Migration Service

Before you begin to work with a MySQL-compatible database as a target for
AWS DMS, make sure that you have completed the following prerequisites:

- Provide a user account to AWS DMS that has read/write privileges to the
  MySQL-compatible database. To create the necessary privileges, run the
  following commands.

```

CREATE USER '<user acct>'@'%' IDENTIFIED BY '<user password>';
GRANT ALTER, CREATE, DROP, INDEX, INSERT, UPDATE, DELETE, SELECT, CREATE TEMPORARY TABLES  ON <schema>.* TO
'<user acct>'@'%';
GRANT ALL PRIVILEGES ON awsdms_control.* TO '<user acct>'@'%';

```

- During the full-load migration phase, you must disable foreign keys on
  your target tables. To disable foreign key checks on a MySQL-compatible database
  during a full load, you can add the following command to the **Extra
  connection attributes** section of the AWS DMS console for your target
  endpoint.

```
Initstmt=SET FOREIGN_KEY_CHECKS=0;
```

- Set the database parameter `local_infile = 1` to enable AWS DMS
  to load data into the target database.
- Grant the following privileges if you use MySQL-specific premigration assessments.

```
grant select on mysql.user to <dms_user>;
grant select on mysql.db to <dms_user>;
grant select on mysql.tables_priv to <dms_user>;
grant select on mysql.role_edges to <dms_user>  #only for MySQL version 8.0.11 and higher
```

## Limitations on using a MySQL-compatible database as a target for AWS Database Migration Service

When using a MySQL database as a target, AWS DMS doesn't support the
following:

- The data definition language (DDL) statements TRUNCATE PARTITION, DROP
  TABLE, and RENAME TABLE.
- Using an `ALTER TABLE `table_name`ADD
COLUMN`column_name`` statement to add
  columns to the beginning or the middle of a table.
- When loading data to a MySQL-compatible target in a full load task, AWS DMS doesn't
  report errors caused by constraints in the task logs, which can cause duplicate key errors
  or mismatches with the number of records. This is caused by the way MySQL handles local
  data with the `LOAD DATA` command. Be sure to do the following during the full load phase:
  - Disable constraints
  - Use AWS DMS validation to make sure the data is consistent.

- When you update a column's value to its existing value, MySQL-compatible
  databases return a `0 rows affected` warning. Although this
  behavior isn't technically an error, it is different from how the
  situation is handled by other database engines. For example, Oracle performs
  an update of one row. For MySQL-compatible databases, AWS DMS generates an
  entry in the awsdms_apply_exceptions control table and logs the following
  warning.

```

Some changes from the source database had no impact when applied to
the target database. See awsdms_apply_exceptions table for details.

```

- Aurora Serverless is available as a target for Amazon Aurora version
  2, compatible with MySQL version 5.7. (Select Aurora MySQL version 2.07.1 to
  be able to use Aurora Serverless with MySQL 5.7 compatibility.) For more
  information about Aurora Serverless, see [Using
  Aurora Serverless v2](../../../AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.md "../../../AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.md") in the
  _Amazon Aurora User Guide_.
- AWS DMS does not support using a reader endpoint for Aurora or Amazon RDS, unless the instances are in
  writable mode, that is, the `read_only` and
  `innodb_read_only` parameters are set to `0` or
  `OFF`. For more information about using Amazon RDS and Aurora as
  targets, see the following:
  - [Determining which DB instance you are connected to](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.md#AuroraMySQL.BestPractices.DeterminePrimaryInstanceConnection "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.md#AuroraMySQL.BestPractices.DeterminePrimaryInstanceConnection")
  - [Updating read replicas with MySQL](../../../AmazonRDS/latest/UserGuide/USER_MySQL.Replication.ReadReplicas.md#USER_MySQL.Replication.ReadReplicas.Updates "../../../AmazonRDS/latest/UserGuide/USER_MySQL.Replication.ReadReplicas.md#USER_MySQL.Replication.ReadReplicas.Updates")

- When replicating TIME datatype, fractional part of time value is not
  replicated.
- When replicating TIME datatype with Extra Connection Attribute
  `loadUsingCSV=false`, the time value is capped to range
  `[00:00:00, 23:59:59]`.

## Endpoint settings when using a MySQL-compatible database as a target for AWS DMS

You can use endpoint settings to configure your MySQL-compatible target database similar to using
extra connection attributes. You specify the settings when you create the target
endpoint using the AWS DMS console, or by using the `create-endpoint` command in the
[AWS CLI](../../../cli/latest/reference/dms/index.md "../../../cli/latest/reference/dms/index.md"), with the
`--my-sql-settings '{"`EndpointSetting"`:
 `"value"`, `...`}'` JSON syntax.

The following table shows the endpoint settings that you can use with
MySQL as a target.

| Name                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ConnectionTimeout`   | Use this extra connection attribute (ECA) to set the endpoint<br>connection timeout for the MySQL instance, in seconds. The default<br>value is 10 seconds. ECA Example:<br>`ConnectionTimeout=30`.                                                                                                                                                                                                                                                                                     |
| `TargetDbType`        | Specifies where to migrate source tables on the target, either to<br>a single database or multiple databases. If you specify<br>`SPECIFIC_DATABASE`, you need to specify the database<br>name, either when using the AWS CLI or the AWS Management Console.<br>Default value: `MULTIPLE_DATABASES`<br>Valid values: {`SPECIFIC_DATABASE`,<br>`MULTIPLE_DATABASES`}<br>Example: `--my-sql-settings '{"TargetDbType":<br>"MULTIPLE_DATABASES"}'`                                          |
| `ParallelLoadThreads` | Improves performance when loading data into<br>the MySQL-compatible target database. Specifies how many threads<br>to use to load the data into the MySQL-compatible target<br>database. Setting a large number of threads can have an adverse<br>effect on database performance, because a separate connection is<br>required for each thread.<br>Default value: 1<br>Valid values: 1–5<br>Example: `--my-sql-settings '{"ParallelLoadThreads":<br>1}'`                                |
| `AfterConnectScript`  | Specifies a script to run immediately after AWS DMS<br>connects to the endpoint.<br>For example, you can specify that the MySQL-compatible target<br>should translate received statements into the latin1 character<br>set, which is the default compiled-in character set of the<br>database. This parameter typically improves performance when<br>converting from UTF8 clients.<br>Example: `--my-sql-settings '{"AfterConnectScript": "SET<br>character_set_connection='latin1'"}'` |
| `MaxFileSize`         | Specifies the maximum size (in KB) of any .csv file used to<br>transfer data to a MySQL-compatible database.<br>Default value: 32,768 KB (32 MB)<br>Valid values: 1–1,048,576<br>`--my-sql-settings '{"MaxFileSize": 512}'`                                                                                                                                                                                                                                                             |

You can also use extra connection attributes to configure your MySQL-compatible target database.

The following table shows the extra connection attributes that you can use with MySQL as a target.

| Name                                 | Description                                                                                                                                                                                                                                                |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Initstmt=SET FOREIGN_KEY_CHECKS=0;` | Disables foreign key checks.<br>Example: `--extra-connection-attributes "Initstmt=SET FOREIGN_KEY_CHECKS=0;"`                                                                                                                                              |
| `Initstmt=SET time_zone`             | Specifies the time zone for the target<br>MySQL-compatible database.<br>Default value: UTC<br>Valid values: The time zone names available in the target MySQL database.<br>Example: `--extra-connection-attributes "Initstmt=SET time_zone=`US/Pacific`;"` |

Alternatively, you can use the `AfterConnectScript` parameter
of the `--my-sql-settings` command to disable foreign key checks
and specify the time zone for your database.

## Target data types for MySQL

The following table shows the MySQL database target data types that are supported
when using AWS DMS and the default mapping from AWS DMS data types.

For additional information about AWS DMS data types, see [Data types for AWS Database Migration Service](CHAP_Reference.DataTypes.md "CHAP_Reference.DataTypes.md").

| AWS DMS data types | MySQL data types                                                                                                                                                                                                                                            |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BOOLEAN            | BOOLEAN                                                                                                                                                                                                                                                     |
| BYTES              | If the length is from 1 through 65,535, then use VARBINARY<br>(length).<br>If the length is from 65,536 through 2,147,483,647, then use<br>LONGLOB.                                                                                                         |
| DATE               | DATE                                                                                                                                                                                                                                                        |
| TIME               | TIME                                                                                                                                                                                                                                                        |
| TIMESTAMP          | "If scale is => 0 and =< 6, then: DATETIME<br>(Scale)<br>If scale is => 7 and =< 9, then: VARCHAR (37)"                                                                                                                                                     |
| INT1               | TINYINT                                                                                                                                                                                                                                                     |
| INT2               | SMALLINT                                                                                                                                                                                                                                                    |
| INT4               | INTEGER                                                                                                                                                                                                                                                     |
| INT8               | BIGINT                                                                                                                                                                                                                                                      |
| NUMERIC            | DECIMAL (p,s)                                                                                                                                                                                                                                               |
| REAL4              | FLOAT                                                                                                                                                                                                                                                       |
| REAL8              | DOUBLE PRECISION                                                                                                                                                                                                                                            |
| STRING             | If the length is from 1 through 21,845, then use VARCHAR<br>(length).<br>If the length is from 21,846 through 2,147,483,647, then use<br>LONGTEXT.                                                                                                          |
| UINT1              | UNSIGNED TINYINT                                                                                                                                                                                                                                            |
| UINT2              | UNSIGNED SMALLINT                                                                                                                                                                                                                                           |
| UINT4              | UNSIGNED INTEGER                                                                                                                                                                                                                                            |
| UINT8              | UNSIGNED BIGINT                                                                                                                                                                                                                                             |
| WSTRING            | If the length is from 1 through 32,767, then use VARCHAR<br>(length).<br>If the length is from 32,768 through 2,147,483,647, then use<br>LONGTEXT.                                                                                                          |
| BLOB               | If the length is from 1 through 65,535, then use BLOB.<br>If the length is from 65,536 through 2,147,483,647, then use<br>LONGBLOB.<br>If the length is 0, then use LONGBLOB (full LOB<br>support).                                                         |
| NCLOB              | If the length is from 1 through 65,535, then use TEXT.<br>If the length is from 65,536 through 2,147,483,647, then use<br>LONGTEXT with ucs2 for CHARACTER SET.<br>If the length is 0, then use LONGTEXT (full LOB support) with<br>ucs2 for CHARACTER SET. |
| CLOB               | If the length is from 1 through 65,535, then use TEXT.<br>If the length is from 65,536 through 2147483647, then use<br>LONGTEXT.<br>If the length is 0, then use LONGTEXT (full LOB<br>support).                                                            |
