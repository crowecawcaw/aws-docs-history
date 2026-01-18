# Oracle DBMS_REDEFINITION and MySQL tables and triggers

The following sections provide detailed guidance on leveraging the Oracle `DBMS_REDEFINITION` and MySQL tables and triggers features during database migration using AWS DMS.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                            |
| ------------------------------ | ---------------------------------- | ------------------------- | ------------------------------------------ |
| Two star feature compatibility | No automation                      | N/A                       | MySQL doesn’t support `DBMS_REDEFINITION`. |

## Oracle usage

The Oracle `DBMS_REDEFINITION` package can be used to reorganize tables while they perform DML operations. Use this package to reclaim space due to a high watermark or to change the table’s DDL.

Oracle uses materialized views to track changes on the master table and then applies those changes in refresh synchronization.

### Examples

Run online redefinition.

- `DBMS_REDEFINITION.CAN_REDEF_TABLE` — Determines if the table can be redefined.
- `DBMS_REDEFINITION.START_REDEF_TABLE` — Start the online redefinition.
- `DBMS_REDEFINITION.SYNC_INTERIM_TABLE` — Synchronize tables with interim data.
- `DBMS_REDEFINITION.FINISH_REDEF_TABLE` — Complete redefinition.

```
EXEC DBMS_REDEFINITION.CAN_REDEF_TABLE('HR', 'EMPLOYEES');
CREATE TABLE employees2 AS SELECT * FROM employees WHERE 1=2;

EXEC DBMS_REDEFINITION.START_REDEF_TABLE
  ('HR','EMPLOYEES','EMPLOYEES2','*');

EXEC DBMS_REDEFINITION.SYNC_INTERIM_TABLE
  ('HR', 'EMPLOYEES', 'EMPLOYEES2');

ALTER TABLE employees2 ADD
  (CONSTRAINT emp_pk2 PRIMARY KEY (empno) USING INDEX);

EXEC DBMS_REDEFINITION.FINISH_REDEF_TABLE
  ('HR', 'EMPLOYEES', 'EMPLOYEES2');

DROP TABLE employees2;
```

For more information, see [DBMS_REDEFINITION](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_REDEFINITION.html#GUID-2BA796C4-8B4D-49B4-8A35-4C6F789CD374 "https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_REDEFINITION.html#GUID-2BA796C4-8B4D-49B4-8A35-4C6F789CD374") in the _Oracle documentation_.

## MySQL usage

MySQL has no equivalent to Oracle for automatically rebuilding tables or syncing between two tables. However, you can sync data from one table to another using CREATE TABLE AS SELECT or mysqldump. After the table is copied, the delta rows can be copied using triggers. Once the application is ready to use the new table, it is synced.

If a table has sequence columns, the last value in the sequence is retained when the table is copied.

For more information, see [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html "https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html"), [CREATE TABLE …​ SELECT Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table-select.html "https://dev.mysql.com/doc/refman/5.7/en/create-table-select.html"), and [mysqldump — A Database Backup Program](https://dev.mysql.com/doc/refman/5.7/en/mysqldump.html "https://dev.mysql.com/doc/refman/5.7/en/mysqldump.html") in the _MySQL documentation_.
