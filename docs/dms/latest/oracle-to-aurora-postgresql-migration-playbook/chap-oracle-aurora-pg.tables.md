# Oracle virtual columns and PostgreSQL views and functions

With AWS DMS, you can replicate data from an Oracle database to a PostgreSQL database while creating PostgreSQL views and functions that mimic Oracle’s virtual columns. Oracle virtual columns let you create columns that derive values from other columns or expressions. PostgreSQL lacks a direct equivalent, but you can use views and functions to achieve similar functionality.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| ------------------------------- | ---------------------------------- | ------------------------- | --------------- |
| Four star feature compatibility | Five star automation level         | N/A                       | N/A             |

## Oracle usage

Oracle virtual columns appear as normal columns, but their values are calculated instead of being stored in the database. Virtual columns can’t be created based on other virtual columns and can only reference columns from the same table. When creating a virtual column, you can either explicitly specify the data type or let the database select the data type based on the expression.

You can use virtual columns with constraints, indexes, table partitioning, and foreign keys.

Functions in expressions must be deterministic at the time of table creation.

Virtual columns can’t be manipulated by DML operations.

You can use virtual columns in a `WHERE` clause and as part of DML commands.

When you create an index on a virtual column, Oracle creates a function-based index.

Virtual columns don’t support index-organized tables, external, objects, clusters, or temporary tables.

The output of a virtual column expression must be a scalar value.

The virtual column keywords `GENERATED ALWAYS AS` and `VIRTUAL` aren’t mandatory and are provided for clarity only.

```
COLUMN_NAME [datatype] [GENERATED ALWAYS] AS (expression) [VIRTUAL]
```

The keyword `AS` after the column name indicates the column is created as a virtual column.

A virtual column doesn’t need to be specified in an `INSERT` statement.

**Examples**

Create a table that includes two virtual columns.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMBER,
  FIRST_NAME VARCHAR2(20),
  LAST_NAME VARCHAR2(25),
  USER_NAME VARCHAR2(25),
  EMAIL AS (LOWER(USER_NAME) || '@aws.com'),
  HIRE_DATE DATE,
  BASE_SALARY NUMBER,
  SALES_COUNT NUMBER,
  FINAL_SALARY NUMBER GENERATED ALWAYS AS
    (CASE WHEN SALES_COUNT >= 10 THEN BASE_SALARY +
    (BASE_SALARY * (SALES_COUNT * 0.05))
    END)
  VIRTUAL);
```

Insert a new record into the table without specifying values for the virtual column.

```
INSERT INTO EMPLOYEES
  (EMPLOYEE_ID, FIRST_NAME, LAST_NAME,
    USER_NAME, HIRE_DATE,BASE_SALARY, SALES_COUNT)
  VALUES(1, 'John', 'Smith', 'jsmith',
    '17-JUN-2003', 5000, 21);
```

Select the email Virtual Column from the table.

```
SELECT email FROM EMPLOYEES;

EMAIL           FINAL_SALARY
jsmith@aws.com  10250
```

For more information, see [CREATE TABLE](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TABLE.html#GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6 "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TABLE.html#GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6") in the _Oracle documentation_.

## PostgreSQL usage

PostgreSQL doesn’t provide a feature that is directly equivalent to a Virtual Column in Oracle before version 12. However, there are workarounds to emulate similar functionality.

Starting with PostgreSQL 12, support for generated columns have been added. Generated columns can be either calculated from other columns values on the fly or calculated and stored. Generated columns are similar to Oracle virtual columns.

Alternatives for virtual columns for PostgreSQL before version 12:app-name:

- **Views** — Create a view using the function for the virtual column as part of the view syntax.
- **Function as a column** — Create a function that receives column values from table records (as parameters) and returns a modified value according to a specific expression. The function serves as a Virtual Column equivalent. You can create a PostgreSQL Expression Index (equivalent to Oracle function-based index) that is based on the function.

**Examples**

The email address for a user is calculated based on the USER_NAME column that is a physical property of the table.

Create a table that includes a `USER_NAME` column but doesn’t include an email address column.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMERIC PRIMARY KEY,
  FIRST_NAME VARCHAR(20),
  LAST_NAME VARCHAR(25),
  USER_NAME VARCHAR(25));
```

Create a PL/pgSQL function which receives the `USER_NAME` value and returns the full email address.

```
CREATE OR REPLACE FUNCTION USER_EMAIL(EMPLOYEES)
  RETURNS text AS $$
  SELECT (LOWER($1.USER_NAME) || '@aws.com')
  $$ STABLE LANGUAGE SQL;
```

Insert data to the table, including a value for `USER_NAME`. During insert, no reference to the `USER_EMAIL` function is made.

```
INSERT INTO EMPLOYEES
  (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, USER_NAME)
  VALUES(1, 'John', 'Smith', 'jsmith'),
  (2, 'Steven', 'King', 'sking');
```

Use the `USER_EMAIL` function as part of a `SELECT` statement.

```
SELECT EMPLOYEE_ID,
    FIRST_NAME,
    LAST_NAME,
    USER_NAME,
    USER_EMAIL(EMPLOYEES)
  FROM EMPLOYEES;

employee_id  first_name  last_name  user_name  user_email
1            John        Smith      jsmith     jsmith@aws.com
2            Steven      King       sking      sking@aws.com
```

Create a view that incorporates the `USER_EMAIL` function.

```
CREATE VIEW employees_function AS
SELECT EMPLOYEE_ID,
    FIRST_NAME,
    LAST_NAME,
    USER_NAME,
    USER_EMAIL(EMPLOYEES)
  FROM EMPLOYEES;
```

Create an expression-based index on the `USER_EMAIL` column for improved performance.

```
CREATE INDEX IDX_USER_EMAIL ON EMPLOYEES(USER_EMAIL(EMPLOYEES));
```

Verify the expression-based index with `EXPLAIN`.

```
SET enable_seqscan = OFF;

EXPLAIN
  SELECT * FROM EMPLOYEES
  WHERE USER_EMAIL(EMPLOYEES) = 'jsmith@aws.com';

QUERY PLAN
Index Scan using idx_user_email on employees (cost=0.13..8.14 rows=1 width=294)
Index Cond: ((lower((user_name)::text) || '@aws.com'::text) = 'jsmith@aws.com'::text)
```

### DML support

Using triggers, you can populate column values automatically as virtual columns. For this approach, create two PostgreSQL objects:

- Create a function containing the data modification logic based on table column data.
- Create a trigger to use the function and run it as part of the DML.

**Examples**

The following code examples show how to automatically populate the `FULL_NAME` column with the values using data from the `FIRST_NAME` and `LAST_NAME` columns.

Create the table.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMERIC PRIMARY KEY,
  FIRST_NAME VARCHAR(20),
  LAST_NAME VARCHAR(25),
  FULL_NAME VARCHAR(25));
```

Create a function to concatenate the `FIRST_NAME` and `LAST_NAME` columns.

```
CREATE OR REPLACE FUNCTION FUNC_USER_FULL_NAME ()
  RETURNS trigger as '
    BEGIN
    NEW.FULL_NAME = NEW.FIRST_NAME || '' '' || NEW.LAST_NAME;
    RETURN NEW;
    END;
' LANGUAGE plpgsql;
```

Create a trigger that uses the function created in the previous step. The function will run before an insert.

```
CREATE TRIGGER TRG_USER_FULL_NAME BEFORE INSERT OR UPDATE
  ON EMPLOYEES FOR EACH ROW
  EXECUTE PROCEDURE FUNC_USER_FULL_NAME();
```

Verify the functionality of the trigger.

```
INSERT INTO EMPLOYEES (EMPLOYEE_ID, FIRST_NAME, LAST_NAME)
  VALUES(1, 'John', 'Smith'),(2, 'Steven', 'King');

SELECT * FROM EMPLOYEES;

employee_id  first_name  last_name  full_name
1            John        Smith      John Smith
2            Steven      King       Steven King
```

Create an index based on the virtual `FULL_NAME` column.

```
CREATE INDEX IDX_USER_FULL_NAME ON EMPLOYEES(FULL_NAME);
```

Verify the expression-based index with `EXPLAIN`.

```
SET enable_seqscan = OFF;

EXPLAIN
  SELECT * FROM EMPLOYEES
  WHERE FULL_NAME = 'John Smith';

QUERY PLAN
Index Scan using idx_user_full_name on employees (cost=0.13..8.14 rows=1 width=226)
Index Cond: ((full_name)::text = 'John Smith'::text)
```

For more information, see [CREATE TRIGGER](https://www.postgresql.org/docs/13/sql-createtrigger.html "https://www.postgresql.org/docs/13/sql-createtrigger.html") in the _PostgreSQL documentation_.
