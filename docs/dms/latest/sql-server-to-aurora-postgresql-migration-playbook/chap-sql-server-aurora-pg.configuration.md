# Configuring session options

This topic provides reference information comparing session options and system variables between Microsoft SQL Server 2019 and Amazon Aurora PostgreSQL. You can understand how SQL Server’s session options translate to system variables, which is crucial for database administrators and developers migrating from SQL Server to Aurora PostgreSQL.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                                      |
| ------------------------------ | ---------------------------------- | ------------------------- | ------------------------------------------------------------------------------------ |
| Two star feature compatibility | N/A                                | N/A                       | `SET` options are significantly different, except for transaction isolation control. |

## SQL Server Usage

Session options in SQL Server is a collection of run-time settings that control certain aspects of how the server handles data for individual sessions. A session is the period between a login event and a disconnect event or an `exec sp_reset_connection` command for connection pooling.

Each session may have multiple run scopes, which are all the statements before the GO keyword used in SQL Server Management Studio scripts, or any set of commands sent as a single run batch by a client application. Each run scope may contain additional sub-scopes. For example, scripts calling stored procedures or functions.

You can set the global session options, which all run scopes use by default, using the `SET` T-SQL command. Server code modules such as stored procedures and functions may have their own run context settings, which are saved along with the code to guarantee the validity of results.

Developers can explicitly use `SET` commands to change the default settings for any session or for an run scope within the session. Typically, client applications send explicit `SET` commands upon connection initiation.

You can view the metadata for current sessions using the `sp_who_system` stored procedure and the `sysprocesses` system table.

###### Note

To change the default setting for SQL Server Management Studio, choose **Tools**, **Options**, **Query Execution**, **SQL Server**, **Advanced**.

### Syntax

Syntax for the `SET` command:

```
SET
Category Setting
Date and time    DATEFIRST | DATEFORMAT
Locking          DEADLOCK_PRIORITY | SET LOCK_TIMEOUT
Miscellaneous    CONCAT_NULL_YIELDS_NULL | CURSOR_CLOSE_ON_COMMIT | FIPS_FLAGGER | SET IDENTITY_INSERT | LANGUAGE | OFFSETS | QUOTED_IDENTIFIER
Query Execution  ARITHABORT | ARITHIGNORE | FMTONLY | NOCOUNT | NOEXEC | NUMERIC_ROUNDABORT | PARSEONLY | QUERY_GOVERNOR_COST_LIMIT | ROWCOUNT | TEXTSIZE
ANSI             ANSI_DEFAULTS | ANSI_NULL_DFLT_OFF | ANSI_NULL_DFLT_ON | ANSI_NULLS | ANSI_PADDING | ANSI_WARNINGS
Execution Stats  FORCEPLAN | SHOWPLAN_ALL | SHOWPLAN_TEXT | SHOWPLAN_XML | STATISTICS IO | STATISTICS XML | STATISTICS PROFILE | STATISTICS TIME
Transactions     IMPLICIT_TRANSACTIONS | REMOTE_PROC_TRANSACTIONS | TRANSACTION ISOLATION LEVEL | XACT_ABORT
```

For more information, see [SET Statements (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/set-statements-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/set-statements-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

### SET ROWCOUNT for DML Deprecated Setting

The SET ROWCOUNT for DML statements has been deprecated as of SQL Server 2008. For more information, see [Deprecated Database Engine Features in SQL Server 2008 R2](<https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143729(v=sql.105)> "https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143729(v=sql.105)") in the _SQL Server documentation_.

For SSQL Server version 2008 R2 and lower, you could limit the number of rows affected by `INSERT`, `UPDATE`, and `DELETE` operations using `SET ROWCOUNT`. For example, it is a common practice in SQL Server to batch large `DELETE` or `UPDATE` operations to avoid transaction logging issues.

The following example loops and deletes rows where `ForDelete` is set to 1, but only 5000 rows at a time in separate transactions (assuming the loop isn’t within an explicit transaction).

```
SET ROWCOUNT 5000;
WHILE @@ROWCOUNT > 0
BEGIN
  DELETE FROM MyTable
  WHERE ForDelete = 1;
END
```

Starting from SQL Server 2012, `SET ROWCOUNT` is ignored for `INSERT`, `UPDATE`, and `DELETE` statements. You can achieve the same functionality using `TOP`. You can convert `TOP` to the Aurora PostgreSQL
`LIMIT`.

For example, you can rewrite the preceding code as:

```
WHILE @@ROWCOUNT > 0
BEGIN
DELETE TOP (5000)
  FROM MyTable
  WHERE ForDelete = 1;
END
```

AWS Schema Conversion Tool can convert this syntax automatically.

### Examples

Use SET within a stored procedure.

```
CREATE PROCEDURE <ProcedureName>
AS
BEGIN
  <Some non-critical transaction code>
  SET TRANSACTION_ISOLATION_LEVEL SERIALIZABLE;
  SET XACT_ABORT ON;
  <Some critical transaction code>
END
```

Explicit `SET` commands affect their run scope and sub scopes. After the scope terminates and the procedure code exits, the calling scope resumes its original settings used before the calling the stored procedure.

For more information, see [SET Statements (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/set-statements-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/set-statements-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) supports hundreds of Server System Variables to control server behavior and the global and session levels.

PostgreSQL provides session-modifiable parameters that are configured using the `SET SESSION` command. Configuration of parameters using `SET SESSION` will only be applicable in the current session. To view the list of
parameters that can be set with `SET SESSION`, you can query `pg_settings`:

```
SELECT * FROM pg_settings where context = 'user';
```

Examples of commonly used session parameters:

- `client_encoding` configures the connected client character set.
- `force_parallel_mode` forces use of parallel query for the session.
- `lock_timeout` sets the maximum allowed duration of time to wait for a database lock to release.
- `search_path` sets the schema search order for object names that aren’t schema-qualified.
- `transaction_isolation` sets the current Transaction Isolation Level for the session.

You can view Aurora PostgreSQL variables using the PostgreSQL command line utility, Amazon Aurora database cluster parameters, Amazon Aurora database instance parameters, or SQL Server interface system variables.

### Converting from SQL Server 2008 SET ROWCOUNT for DML operations

The use of `SET ROWCOUNT` for DML operations is deprecated as of SQL Server 2008 R2. Code that uses the `SET ROWCOUNT` syntax can’t be converted automatically.

You can either rewrite the code to use `TOP` before running AWS SCT, or manually change it afterward.

Consider the example that is used to batch `DELETE` operations in SQL Server using `TOP`:

```
WHILE @@ROWCOUNT > 0
BEGIN
  DELETE TOP (5000)
  FROM MyTable
  WHERE ForDelete = 1;
END
```

You can rewrite the preceding example to use the Aurora PostgreSQL
`LIMIT` clause:

```
WHILE row_count() > 0 LOOP
  DELETE FROM num_test
  WHERE ctid IN (
  SELECT ctid
  FROM num_test
  LIMIT 10)
END LOOP;
```

### Examples

Change the time zone of the connected session.

```
SET SESSION DateStyle to POSTGRES, DMY;
SET

SELECT NOW();

now
Sat 09 Sep 11:03:43.597202 2017 UTC
(1 row)

SET SESSION DateStyle to ISO, MDY;
SET

SELECT NOW();

now
2017-09-09 11:04:01.3859+00
(1 row)
```

## Summary

The following table summarizes commonly used SQL Server session options and their corresponding Aurora PostgreSQL system variables.

| Category      | SQL Server                                                            | Aurora PostgreSQL                                                                                    |
| ------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Date and time | `DATEFIRST`                                                           | Use `DOW` in queries                                                                                 |
| Date and time | `DATEFORMAT`                                                          | `DateStyle`                                                                                          |
| Locking       | `LOCK_TIMEOUT`                                                        | `lock_timeout`                                                                                       |
| Transactions  | `IMPLICIT_TRANSACTIONS`                                               | `SET TRANSACTION`                                                                                    |
| Transactions  | `TRANSACTION ISOLATION LEVEL`                                         | `BEGIN TRANSACTION ISOLATION LEVEL`                                                                  |
| Query run     | `IDENTITY_INSERT`                                                     | See [Sequences and Identity](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md"). |
| Query run     | `LANGUAGE`                                                            | `lc_monetary`, `lc_numeric`, or `lc_time`                                                            |
| Query run     | `QUOTED_IDENTIFIER`                                                   | N/A                                                                                                  |
| Query run     | `NOCOUNT`                                                             | N/A and not needed                                                                                   |
| Run stats     | `SHOWPLAN_ALL`, `TEXT`, `XML`, `STATISTICS IO`, `PROFILE`, and `TIME` | See [Run Plans](chap-sql-server-aurora-pg.tuning.md "chap-sql-server-aurora-pg.tuning.md").          |
| Miscellaneous | `CONCAT_NULL_YIELDS_NULL`                                             | N/A                                                                                                  |
| Miscellaneous | `ROWCOUNT`                                                            | Use `LIMIT` within `SELECT`.                                                                         |

For more information, see [SET](https://www.postgresql.org/docs/13/sql-set.html "https://www.postgresql.org/docs/13/sql-set.html") in the _PostgreSQL documentation_.
