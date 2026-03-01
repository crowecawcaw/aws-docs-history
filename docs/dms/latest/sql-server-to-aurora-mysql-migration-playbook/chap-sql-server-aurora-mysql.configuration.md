# Configuring session options

This topic provides reference information about session options and system variables in SQL Server and Amazon Aurora MySQL. You can use this content to understand the differences and similarities between how these two database systems handle runtime settings that control server behavior.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                                    |
| ------------------------------ | ---------------------------------- | ------------------------- | ---------------------------------------------------------------------------------- |
| Two star feature compatibility | N/A                                | N/A                       | SET options are significantly different, except for transaction isolation control. |

## SQL Server Usage

Session options in SQL Server is a collection of run-time settings that control certain aspects of how the server handles data for individual sessions. A session is the period between a login event and a disconnect event or the `exec sp_reset_connection` command for connection pooling.

Each session may have multiple run scopes, which are all the statements before the `GO` keyword used in SQL Server management Studio scripts, or any set of commands sent as a single run batch by a client application. Each run scope may contain additional sub-scopes. For example, scripts calling stored procedures or functions.

You can set the global session options, which all run scopes use by default, using the `SET` T-SQL command. Server code modules such as stored procedures and functions may have their own run context settings,
which are saved along with the code to guarantee the validity of results.

Developers can explicitly use `SET` commands to change the default settings for any session or for an run scope within the session. Typically, client applications send explicit `SET` commands upon connection initiation.

You can view the metadata for current sessions using the `sp_who_system` stored procedure and the `sysprocesses` system table.

###### Note

To change the default setting for SQL Server Management Studio, choose **Tools**, **Options**, **Query Execution**, **SQL Server**, **Advanced**.

### Syntax

The following example includes categories and settings for the `SET` command:

```
SET
Date and time
DATEFIRST | DATEFORMAT
Locking
DEADLOCK_PRIORITY | SET LOCK_TIMEOUT
Miscellaneous
CONCAT_NULL_YIELDS_NULL | CURSOR_CLOSE_ON_COMMIT | FIPS_FLAGGER |
SET IDENTITY_INSERT | LANGUAGE | OFFSETS | QUOTED_IDENTIFIER
Query Execution
ARITHABORT | ARITHIGNORE | FMTONLY | NOCOUNT | NOEXEC |
NUMERIC_ROUNDABORT | PARSEONLY | QUERY_GOVERNOR_COST_LIMIT |
ROWCOUNT | TEXTSIZE | ANSI ANSI_DEFAULTS | ANSI_NULL_DFLT_OFF |
ANSI_NULL_DFLT_ON | ANSI_NULLS | ANSI_PADDING |  ANSI_WARNINGS
Execution Stats
FORCEPLAN | SHOWPLAN_ALL | SHOWPLAN_TEXT | SHOWPLAN_XML | STATISTICS IO |
STATISTICS XML | STATISTICS PROFILE | STATISTICS TIME
Transactions
IMPLICIT_TRANSACTIONS | REMOTE_PROC_TRANSACTIONS |
TRANSACTION ISOLATION LEVEL | XACT_ABORT
```

For more information, see [SET Statements (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/set-statements-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/set-statements-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

### SET ROWCOUNT for DML Deprecated Setting

The SET ROWCOUNT for DML statements has been deprecated as of SQL Server 2008.

Up to and including SQL Server 2008 R2, you could limit the number of rows affected by `INSERT`, `UPDATE`, and `DELETE` operations using `SET ROWCOUNT`. For example, it is a common practice in SQL Server to batch large `DELETE` or `UPDATE` operations to avoid transaction logging issues. The following example loops and deletes rows having `ForDelete` set to 1, but only 5000 rows at a time in separate transactions (assuming the loop isn’t within an explicit transaction).

```
SET ROWCOUNT 5000;
WHILE @@ROWCOUNT > 0
BEGIN
    DELETE FROM MyTable
    WHERE ForDelete = 1;
END
```

Starting with SQL Server 2012, `SET ROWCOUNT` is ignored for `INSERT`, `UPDATE` and `DELETE` statements.

You can achieve the same functionality using `TOP`, which can be converted to `LIMIT` in Aurora MySQL. For example, you can rewrite the preceding example as shown following:

```
WHILE @@ROWCOUNT > 0
BEGIN
    DELETE TOP (5000)
    FROM MyTable
    WHERE ForDelete = 1;
END
```

AWS Schema Conversion Tool (AWS SCT automatically converts this example to Aurora MySQL.

### Examples

Use `SET` within a stored procedure.

```
CREATE PROCEDURE <ProcedureName>
AS
BEGIN
    <Some non critical transaction code>
    SET TRANSACTION_ISOLATION_LEVEL SERIALIZABLE;
    SET XACT_ABORT ON;
    <Some critical transaction code>
END
```

###### Note

Explicit `SET` commands affect their run scope and sub scopes. After the scope terminates and the procedure code exits, the calling scope resumes its original settings used before the calling the stored procedure.

For more information, see [SET Statements (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/set-statements-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/set-statements-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) supports hundreds of Server System Variables to control server behavior and the global and session levels.

Use the `SHOW VARIABLES` command to view a list of all variables.

```
SHOW SESSION VARIABLES;
-- 532 rows returned
```

###### Note

Aurora MySQL 5.7 provides additional variables that don’t exist in MySQL 5.7 standalone installations. These variables are prefixed with Amazon Aurora or AWS.

You can view Aurora MySQL variables using the MySQL command line utility, Aurora database cluster parameters, Aurora database instance parameters, or SQL interface system variables.

To view all sessions, use the `SHOW PROCESSLIST` command or the `information_schema PROCESSLIST` view, which displays information such as session current status, default database, host name, and application name.

###### Note

Unlike standalone installations of MySQL, Amazon Aurora doesn’t provide access to the configuration file containing system variable defaults. Cluster-level parameters are managed in database cluster parameter groups and instance-level parameters are managed in database parameter groups. In Aurora MySQL, some parameters from the full base set of standalone MySQL installations can’t be modified and others were removed. See Server Options for a walkthrough of creating a custom parameter group.

### Converting from SQL Server 2008 SET ROWCOUNT for DML operations

The use of `SET ROWCOUNT` for DML operations is deprecated as of SQL Server 2008 R2. Code that uses the `SET ROWCOUNT` syntax can’t be converted automatically. You can either rewrite to use `TOP` before running AWS SCT, or manually change it afterward.

The following example runs batch `DELETE` operations in SQL Server using `TOP`:

```
WHILE @@ROWCOUNT > 0
BEGIN
    DELETE TOP (5000)
    FROM MyTable
    WHERE ForDelete = 1;
END
```

You can rewrite the preceding example to use the `LIMIT` clause in Aurora MySQL.

```
WHILE row_count() > 0
DO
    DELETE
    FROM MyTable
    WHERE ForDelete = 1
    LIMIT 5000;
END WHILE;
```

### Examples

View the metadata for all processes.

```
SELECT *
FROM information_schema.PROCESSLIST;
```

```
SHOW PROCESSLIST;
```

Use the `SET` command to change session isolation level and SQL mode.

```
SET sql_mode = 'ANSI_QUOTES';
SET SESSION TRANSACTION ISOLATION LEVEL 'READ-COMMITTED';
```

Set isolation level using a system variable.

```
SET SESSION tx_isolation = 'READ-COMMITTED'
```

The `SET SESSION` command is the equivalent to the `SET` command in T-SQL.

However, there are far more configurable parameters in Aurora MySQL than in SQL Server.

## Summary

The following table summarizes commonly used SQL Server session options and their corresponding Aurora MySQL system variables.

| Category      | SQL Server                                                                         | Aurora MySQL                                                                                                                                                        | Comments                                                                                                                                                                                                                                                                                                               |
| ------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Date and time | `DATEFIRST`<br>`DATEFORMAT`                                                        | `default_week_format`<br>`date_format` (deprecated)                                                                                                                 | `default_week_format` operates different than `DATEFIRST`. You can use only Sunday and Monday as the start of the week. It also controls what is considered week one of the year and whether returned `WEEK` value is zero<br>• based, or one-based. There is no alternative to the deprecated `date_format` variable. |
| Locking       | `LOCK_TIMEOUT`                                                                     | `lock_wait_timeout`                                                                                                                                                 | Set in database parameter groups.                                                                                                                                                                                                                                                                                      |
| ANSI          | `ANSI_NULLS`<br>`ANSI_PADDING`                                                     | N/A<br>`PAD_CHAR_TO_FULL_LENGTH`                                                                                                                                    | Set with the sql_mode system variable.                                                                                                                                                                                                                                                                                 |
| Transactions  | `IMPLICIT_TRANSACTIONS`<br>`TRANSACTION ISOLATION LEVEL`                           | `autocommit`<br>`SET SESSION TRANSACTION ISOLATION LEVEL`                                                                                                           | The default for Aurora MySQL, as in SQL server, is to commit automatically. Syntax is compatible except the addition of the `SESSION` keyword.                                                                                                                                                                         |
| Query run     | `IDENTITY_INSERT`<br>`LANGUAGE`<br>`QUOTED_IDENTIFIER`<br>`NOCOUNT`                | See [Identity and Sequences](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md")<br>`lc_time_names`<br>`ANSI_QUOTES`<br>N/A and not needed | `lc_time_names` are set in a database parameter group. `lc_messages` isn’t supported in Aurora MySQL. `ANSI_QUOTES` is a value for the `sql_mode` parameter. Aurora MySQL doesn’t add row count information<br>to the errors collection.                                                                               |
| Runtime stats | `SHOWPLAN_ALL`, `TEXT`, and `XML`<br>`STATISTICS IO`, `XML`, `PROFILE`, and `TIME` | See [Run Plans](chap-sql-server-aurora-mysql.tuning.md "chap-sql-server-aurora-mysql.tuning.md")                                                                    |                                                                                                                                                                                                                                                                                                                        |
| Miscellaneous | `CONCAT_NULL_YIELDS_NULL`<br>`ROWCOUNT`                                            | N/A<br>`sql_select_limit`                                                                                                                                           | Aurora MySQL always returns NULL for any NULL concatenation operation. `sql_select_limit` only affects `SELECT` statements unlike `ROWCOUNT`, which also affects all DML.                                                                                                                                              |

For more information, see [Server System Variables](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html "https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html") in the _MySQL documentation_.
