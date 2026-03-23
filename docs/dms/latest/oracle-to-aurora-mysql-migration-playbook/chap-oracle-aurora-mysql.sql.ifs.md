# Oracle and MySQL INSERT FROM SELECT statement

The following sections provide details on running the `INSERT FROM SELECT` statement, including syntax examples and best practices for efficient data transfer.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                         |
| ------------------------------- | ---------------------------------- | ------------------------- | ------------------------------------------------------- |
| Four star feature compatibility | Four star automation level         | N/A                       | MySQL doesn’t support `ERROR LOG` and subquery options. |

## Oracle usage

You can insert multiple records into a table from another table using the `INSERT FROM SELECT` statement, which is a derivative of the basic `INSERT` statement. The column ordering and data types must match between the target and the source tables.

### Examples

Simple `INSERT FROM SELECT` (explicit).

```
INSERT INTO EMPS (EMPLOYEE_ID, FIRST_NAME, SALARY, DEPARTMENT_ID) SELECT EMPLOYEE_ID,
FIRST_NAME, SALARY, DEPARTMENT_ID
FROM EMPLOYEES
WHERE SALARY > 10000;
```

Simple `INSERT FROM SELECT` (implicit).

```
INSERT INTO EMPS
SELECT EMPLOYEE_ID, FIRST_NAME, SALARY, DEPARTMENT_ID
FROM EMPLOYEES
WHERE SALARY > 10000;
```

This example produces the same result as the preceding example but uses a subquery in the `DML_table_expression_clause`.

```
INSERT INTO
(SELECT EMPLOYEE_ID, FIRST_NAME, SALARY, DEPARTMENT_ID FROM EMPS)
VALUES (120, 'Kenny', 10000, 90);
```

Log errors with the Oracle `error_logging_clause`.

```
ALTER TABLE EMPS ADD CONSTRAINT PK_EMP_ID PRIMARY KEY(employee_id);
EXECUTE DBMS_ERRLOG.CREATE_ERROR_LOG('EMPS', 'ERRLOG');
INSERT INTO EMPS
SELECT EMPLOYEE_ID, FIRST_NAME, SALARY, DEPARTMENT_ID
FROM EMPLOYEES
WHERE SALARY > 10000
LOG ERRORS INTO errlog ('Cannot Perform Insert') REJECT LIMIT 100;
0 rows inserted
```

When inserting an existing `EMPLOYEE ID` into the `EMPS` table, the insert doesn’t fail because the invalid records are redirected to the `ERRLOG` table.

For more information, see [INSERT](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/INSERT.html#GUID-903F8043-0254-4EE9-ACC1-CB8AC0AF3423 "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/INSERT.html#GUID-903F8043-0254-4EE9-ACC1-CB8AC0AF3423") in the _Oracle documentation_.

## MySQL usage

MySQL is compatible with the Oracle `INSERT FROM SELECT` syntax except for a few features specific to Oracle. For example, the `conditional_insert_clause (ALL | FIRST | ELSE)`. MySQL doesn’t support the Oracle `error_logging_clause` feature. Generally, you can use `ON DUPLICATE KEY UPDATE` to handle duplicate rows.

### Syntax

```
INSERT [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE]
  [INTO] tbl_name
  [PARTITION (partition_name [, partition_name] ...)]
  [(col_name [, col_name] ...)]
  SELECT ...
  [ON DUPLICATE KEY UPDATE assignment_list]

value:
  {expr | DEFAULT}

assignment:
  col_name = value

assignment_list:
  assignment [, assignment] ...
```

### Examples

Simple `INSERT FROM SELECT` (explicit).

```
INSERT INTO EMPS (EMPLOYEE_ID, FIRST_NAME, SALARY, DEPARTMENT_ID)
SELECT EMPLOYEE_ID, FIRST_NAME, SALARY, DEPARTMENT_ID
FROM EMPLOYEES
WHERE SALARY > 10000;
```

Simple `INSERT FROM SELECT` (implicit).

```
INSERT INTO EMPS
SELECT EMPLOYEE_ID, FIRST_NAME, SALARY, DEPARTMENT_ID
FROM EMPLOYEES
WHERE SALARY > 10000;
```

The following example isn’t compatible with MySQL.

```
INSERT INTO
(SELECT EMPLOYEE_ID, FIRST_NAME, SALARY, DEPARTMENT_ID FROM EMPS)
VALUES (120, 'Kenny', 10000, 90);
```

The following example demonstrates using the `ON DUPLICATE KEY UPDATE` clause to update specific columns when a `UNIQUE` violation occurs.

```
INSERT INTO EMPS
SELECT * from EMPLOYEES
  where EMPLOYEE_ID > 10
ON DUPLICATE KEY UPDATE
EMPS.FIRST_NAME=EMPLOYEES.FIRST_NAME,
EMPS.SALARY=EMPLOYEES.SALARY;
```

For more information, see [INSERT …​ SELECT Statement](https://dev.mysql.com/doc/refman/8.0/en/insert-select.html "https://dev.mysql.com/doc/refman/8.0/en/insert-select.html") in the _MySQL documentation_.
