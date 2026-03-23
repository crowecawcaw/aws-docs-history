# CREATE TABLE AS SELECT statement

With AWS DMS, you can create a new table in a target database by selecting data from one or more tables in a source database using the Oracle and PostgreSQL `CREATE TABLE AS SELECT` statement. This statement defines a new table by querying data from existing tables, providing a way to replicate table structures and data from a source to a target database.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| ------------------------------- | ---------------------------------- | ------------------------- | --------------- |
| Five star feature compatibility | Five star automation level         | N/A                       | N/A             |

## Oracle usage

The Create Table As Select (CTAS) statement creates a new table based on an existing table. It copies the table DDL definitions (column names and column datatypes) and data to a new table. The new table is populated from the columns specified in the `SELECT` statement, or all columns if you use `SELECT * FROM`. You can filter specific data using the `WHERE` and `AND` statements. Additionally, you can create a new table having a different structure using joins, `GROUP BY`, and `ORDER BY`.

**Examples**

Create a table based on an existing table and include data from all columns.

```
CREATE TABLE EMPS
AS
SELECT * FROM EMPLOYEES;
```

Create a table based on an existing table with select columns.

```
CREATE TABLE EMPS
AS
SELECT EMPLOYEE_ID, FIRST_NAME, SALARY FROM EMPLOYEES
ORDER BY 3 DESC
```

For more information, see [CREATE TABLE](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TABLE.html#GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6 "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TABLE.html#GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6") in the _Oracle documentation_.

## PostgreSQL usage

PostgreSQL conforms to the ANSI/SQL standard for CTAS functionality and is compatible with an Oracle CTAS statement. For PostgreSQL, the following CTAS standard elements are optional:

- The standard requires parentheses around the `SELECT` statement; PostgreSQL doesn’t.
- The standard requires the `WITH [ NO ] DATA` clause; PostgreSQL doesn’t.

**PostgreSQL CTAS synopsis**

```
CREATE
[ [ GLOBAL | LOCAL ] { TEMPORARY | TEMP } | UNLOGGED ] TABLE [ IF NOT EXISTS ] table_name
[ (column_name [, ...] ) ]
[ WITH ( storage_parameter [= value] [, ... ] ) |
WITH OIDS | WITHOUT OIDS ]
[ ON COMMIT { PRESERVE ROWS | DELETE ROWS | DROP } ]
[ TABLESPACE tablespace_name ]
AS query
[ WITH [ NO ] DATA ]
```

**Examples**

PostgreSQL CTAS.

```
pg_CREATE TABLE EMPS AS SELECT * FROM EMPLOYEES;
pg_CREATE TABLE EMPS AS
SELECT EMPLOYEE_ID, FIRST_NAME, SALARY FROM EMPLOYEES ORDER BY 3 DESC;
```

PostgreSQL CTAS with no data.

```
pg_CREATE TABLE EMPS AS SELECT * FROM EMPLOYEES WITH NO DATA;
```

For more information, see [CREATE TABLES](https://www.postgresql.org/docs/13/sql-createtableas.html "https://www.postgresql.org/docs/13/sql-createtableas.html") in the _PostgreSQL documentation_.
