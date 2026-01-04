# Oracle and PostgreSQL temporary tables

With AWS DMS, you can efficiently migrate data between Oracle and PostgreSQL databases while leveraging temporary tables. Temporary tables are database objects that store data temporarily, existing only for the duration of a session or transaction. These tables are useful when you need to store intermediate results during complex queries or data transformations.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                      | Key differences                                                                                                                                  |
| -------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Three star feature compatibility | Three star automation level        | [Creating Tables](chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.tables "chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.tables") | PostgreSQL doesn’t support GLOBAL temporary table. PostgreSQL can’t read from multiple sessions. PostgreSQL drops tables after the session ends. |

## Oracle usage

In Oracle, you can create temporary tables for storing data that exists only for the duration of a session or transaction.

Use the `CREATE GLOBAL TEMPORARY TABLE` statement to create a temporary table. This type of table has a persistent DDL structure, but not persistent data. It doesn’t generate redo during DML. Two of the primary use-cases for temporary tables include:

- Processing many rows as part of a batch operation while requiring staging tables to store intermediate results.
- Storing data required only for the duration of a specific session. When the session ends, the session data is cleared.

When using temporary tables, the data is visible only to the session that inserts the data into the table.

Oracle 18c introduces private temporary tables which are temporary tables that are only available during session or transaction. After session or transaction ends they are automatically dropped.

### Oracle global temporary tables

Global temporary tables store data in the Oracle temporary tablespace.

DDL operations on a temporary table are permitted including `ALTER TABLE`, `DROP TABLE`, and `CREATE INDEX`.

Temporary tables can’t be partitioned, clustered, or created as index-organized tables. Also, they don’t support parallel `UPDATE`, `DELETE`, and `MERGE`.

Foreign key constraints can’t be created on temporary tables.

Processing DML operations on a temporary table doesn’t generate redo data. However, undo data for the rows and redo data for the undo sata itself are generated.

Indexes can be created for a temporary table. They are treated as temporary indexes. Temporary tables also support triggers.

Temporary tables can’t be named after an existing table object and can’t be dropped while containing records, even from another session.

### Session-specific and transaction-specific temporary table syntax

Use `ON COMMIT` to specifies whether the temporary table data persists for the duration of a transaction or a session.

Use `PRESERVE ROWS` when the session ends, all data is truncated but persists beyond the end of the transaction.

Use `DELETE ROWS` to truncate data after each commit. This is the default behavior.

### Oracle 12c temporary table enhancements

**Global temporary table statistics**

Prior to Oracle 12c, statistics on temporary tables were common to all sessions. Oracle 12c introduces sessionspecific statistics for temporary tables. Statistics can be configured using the `DBMS_STATS` preference `GLOBAL_TEMP_TABLE_STATS`, which can be set to `SHARED` or `SESSION`.

**Global temporary table undo**

Performing DML operations on a temporary table doesn’t generate Redo data, but does generate undo data that eventually, by itself, generates redo records. Oracle 12c provides an option to store the temporary undo data in the temporary tablespace itself. This feature is configured using the `temp_undo_enabled` parameter with the options `TRUE` or `FALSE`.

For more information, see [TEMP_UNDO_ENABLED](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/TEMP_UNDO_ENABLED.html#GUID-E2A01A84-2D63-401F-B64E-C96B18C5DCA6 "https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/TEMP_UNDO_ENABLED.html#GUID-E2A01A84-2D63-401F-B64E-C96B18C5DCA6") in the _Oracle documentation_.

**Examples**

Create an Oracle global temporary table (with `ON COMMIT PRESERVE ROWS`).

```
CREATE GLOBAL TEMPORARY TABLE EMP_TEMP (
  EMP_ID NUMBER PRIMARY KEY,
  EMP_FULL_NAME VARCHAR2(60) NOT NULL,
  AVG_SALARY NUMERIC NOT NULL)
  ON COMMIT PRESERVE ROWS;

CREATE INDEX IDX_EMP_TEMP_FN ON EMP_TEMP(EMP_FULL_NAME);

INSERT INTO EMP_TEMP VALUES(1, 'John Smith', '5000');

COMMIT;

SELECT * FROM SCT.EMP_TEMP;

EMP_ID EMP_FULL_NAME AVG_SALARY
1      John Smith    5000
```

Create an Oracle global temporary table (with `ON COMMIT DELETE ROWS`).

```
CREATE GLOBAL TEMPORARY TABLE EMP_TEMP (
  EMP_ID NUMBER PRIMARY KEY,
  EMP_FULL_NAME VARCHAR2(60) NOT NULL,
  AVG_SALARY NUMERIC NOT NULL)
  ON COMMIT DELETE ROWS;

INSERT INTO EMP_TEMP VALUES(1, 'John Smith', '5000');

COMMIT;

SELECT * FROM SCT.EMP_TEMP;
```

For more information, see [CREATE TABLE](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/TEMP_UNDO_ENABLED.html#GUID-E2A01A84-2D63-401F-B64E-C96B18C5DCA6 "https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/TEMP_UNDO_ENABLED.html#GUID-E2A01A84-2D63-401F-B64E-C96B18C5DCA6") in the _Oracle documentation_.

## PostgreSQL usage

PostgreSQL temporary tables share many similarities with Oracle global temporary tables.

From a syntax perspective, PostgreSQL temporary tables are referred to as temporary tables without global definition. The implementation is mostly identical.

Starting from PostgreSQL 10, partition tables can also be temporary tables.

In terms of differences, Oracle stores the temporary table structure (DDL) for repeated use — even after a database restart — but doesn’t store rows persistently. PostgreSQL implements temporary tables differently: the table structure (DDL) isn’t stored in the database. When a session ends, the temporary table is dropped.

- **Session-specific** — In PostgreSQL, every session is required to create its own Temporary Tables. Each session can create its own “private” Temporary Tables, using identical table names.
- **LOCAL / GLOBAL syntax** — PostgreSQL temporary tables don’t support cross-session data access. PostgreSQL doesn’t distinguish between “GLOBAL” and “LOCAL” temporary tables. The use of these keywords is permitted in PostgreSQL, but they have no effect because PostgreSQL creates temporary tables as local and session-isolated tables.

###### Note

Use of the GLOBAL keyword is deprecated.

- In the Oracle Database, the default behavior when the `ON COMMIT` clause is omitted is `ON COMMIT DELETE ROWS`. In PostgreSQL, the default is `ON COMMIT PRESERVE ROWS`.

### PostgreSQL temporary tables ON COMMIT clause

The `ON COMMIT` clause specifies the state of the data as it persists for the duration of a transaction or a session.

- `PRESERVE ROWS` — The PostgreSQL default. When a session ends, all data is truncated but persists beyond the end of thetransaction.
- `DELETE ROWS` — The data is truncated after each commit.

**Examples**

Create a use a temporary table, with `ON COMMIT PRESERVE ROWS`.

```
CREATE GLOBAL TEMPORARY TABLE EMP_TEMP (
  EMP_ID NUMERIC PRIMARY KEY,
  EMP_FULL_NAME VARCHAR(60) NOT NULL,
  AVG_SALARY NUMERIC NOT NULL)
  ON COMMIT PRESERVE ROWS;

CREATE INDEX IDX_EMP_TEMP_FN ON EMP_TEMP(EMP_FULL_NAME);

INSERT INTO EMP_TEMP VALUES(1, 'John Smith', '5000');

COMMIT;

SELECT * FROM SCT.EMP_TEMP;

emp_id  emp_full_name  avg_salary
1       John Smith     5000

DROP TABLE EMP_TEMP;
```

Create and use a Temporary Table, with `ON COMMIT DELETE ROWS`.

```
CREATE GLOBAL TEMPORARY TABLE EMP_TEMP (
  EMP_ID NUMERIC PRIMARY KEY,
  EMP_FULL_NAME VARCHAR(60) NOT NULL,
  AVG_SALARY NUMERIC NOT NULL)
  ON COMMIT DELETE ROWS;

INSERT INTO EMP_TEMP VALUES(1, 'John Smith', '5000');

COMMIT;

SELECT * FROM SCT.EMP_TEMP;
emp_id  emp_full_name  avg_salary
(0 rows)

DROP TABLE EMP_TEMP;
DROP TABLE
```

## Summary

| Feature                                                                           | Oracle                        | Aurora PostgreSQL                      |
| --------------------------------------------------------------------------------- | ----------------------------- | -------------------------------------- |
| Semantic                                                                          | Global Temporary Table        | Temporary Table / Temp Table           |
| Create table                                                                      | CREATE GLOBAL TEMPORARY…      | CREATE TEMPORARY… or CREATE TEMP…      |
| Accessible from multiple sessions                                                 | Yes                           | No                                     |
| Temp table DDL persist after session end / database restart usermanaged datafiles | Yes                           | No (dropped at the end of the session) |
| Create index support                                                              | Yes                           | Yes                                    |
| Foreign key support                                                               | Yes                           | Yes                                    |
| ON COMMIT default                                                                 | COMMIT DELETE ROWS            | ON COMMIT PRESERVE ROWS                |
| ON COMMIT PRESERVE ROWS                                                           | Yes                           | Yes                                    |
| ON COMMIT DELETE ROWS                                                             | Yes                           | Yes                                    |
| Alter table support                                                               | Yes                           | Yes                                    |
| Gather statistics                                                                 | dbms_stats.gather_table_stats | ANALYZE                                |
| Oracle 12c GLOBAL_TEMP_TABLE_STATS                                                | dbms_stats.set_table_prefs    | ANALYZE                                |

For more information, see [CREATE TABLE](https://www.postgresql.org/docs/13/sql-createtable.html "https://www.postgresql.org/docs/13/sql-createtable.html") in the _PostgreSQL documentation_.
