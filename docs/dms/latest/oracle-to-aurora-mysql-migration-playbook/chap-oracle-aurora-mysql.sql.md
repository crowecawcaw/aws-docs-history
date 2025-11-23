# Oracle and MySQL CREATE TABLE AS SELECT statement

With AWS DMS, you can create a new table in a target database by selecting data from one or more tables in a source database using the Oracle and MySQL `CREATE TABLE AS SELECT` statement. This statement defines a new table by querying data from existing tables, providing a way to replicate table structures and data from a source to a target database.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| ------------------------------- | ---------------------------------- | ------------------------- | --------------- |
| Five star feature compatibility | Five star automation level         | N/A                       | N/A             |

## Oracle usage

The Create Table As Select (CTAS) statement creates a new table based on an existing table. It copies the table DDL definitions (column names and column datatypes) and data to a new table. The new table is populated from the columns specified in the `SELECT` statement, or all columns if you use `SELECT * FROM`. You can filter specific data using the `WHERE` and `AND` statements. Additionally, you can create a new table having a different structure using joins, `GROUP BY`, and `ORDER BY`.

### Examples

The following example creates a table based on an existing table and include data from all columns.

```
CREATE TABLE EMPS
AS
SELECT * FROM EMPLOYEES;
```

The following example creates a table based on an existing table with select columns.

```
CREATE TABLE EMPS
AS
SELECT EMPLOYEE_ID, FIRST_NAME, SALARY FROM EMPLOYEES
ORDER BY 3 DESC
```

For more information, see [CREATE TABLE](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TABLE.html#GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6 "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TABLE.html#GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6") in the _Oracle documentation_.

## MySQL usage

MySQL conforms to the ANSI/SQL standard for CTAS functionality and is compatible with an Oracle CTAS statement. For MySQL, the following CTAS standard elements are optional:

- The standard requires parentheses around the `SELECT` statement; MySQL doesn’t.
- The standard requires the `WITH [ NO ] DATA` clause; MySQL doesn’t.

### Examples

The following example creates a table based on an existing table and include data from all columns.

```
CREATE TABLE EMPS AS SELECT * FROM EMPLOYEES;
```

The following example creates a table based on an existing table with select columns.

```
CREATE TABLE EMPS AS SELECT EMPLOYEE_ID, FIRST_NAME, SALARY FROM EMPLOYEES ORDER BY 3
DESC;
```
