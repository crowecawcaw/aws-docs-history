# Oracle EXECUTE IMMEDIATE and MySQL EXECUTE and PREPARE statements

With AWS DMS, you can migrate databases between different database platforms, including Oracle and MySQL, by leveraging features, such as Oracle’s `EXECUTE IMMEDIATE` statement and MySQL’s `EXECUTE` and `PREPARE` statements.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                          | Key differences                                                                                                                                               |
| ------------------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Four star feature compatibility | Two star automation level          | [EXECUTE IMMEDIATE](chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.immediate "chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.immediate") | Make sure that you use the `PREPARE` command in MySQL. MySQL doesn’t support running SQL with results and bind variables or anonymous blocks using `EXECUTE`. |

## Oracle usage

You can use Oracle `EXECUTE IMMEDIATE` statement to parse and run a dynamic SQL statement or an anonymous PL/SQL block. It also supports bind variables.

### Examples

Run a dynamic SQL statement from within a PL/SQL procedure:

1. Create a PL/SQL procedure named `raise_sal`.
2. Define a SQL statement with a dynamic value for the column name included in the `WHERE` statement.
3. Use the `EXECUTE IMMEDIATE` command supplying the two bind variables to be used as part of the `SELECT` statement: `amount` and `col_val`.

```
CREATE OR REPLACE PROCEDURE raise_sal (col_val NUMBER,
emp_col VARCHAR2, amount NUMBER) IS
  col_name VARCHAR2(30);
  sql_stmt VARCHAR2(350);
BEGIN
  -- determine if a valid column name has been given as input
  SELECT COLUMN_NAME INTO col_name FROM USER_TAB_COLS
  WHERE TABLE_NAME = 'EMPLOYEES' AND COLUMN_NAME = emp_col;

  -- define the SQL statment (with bind variables)
  sql_stmt := 'UPDATE employees SET salary = salary + :1 WHERE ' ||
  col_name || ' = :2';

  -- Run the command
  EXECUTE IMMEDIATE sql_stmt USING amount, col_val;
END raise_sal;
/
```

4. Run the DDL operation from within an `EXECUTE IMMEDIATE` command.

```
EXECUTE IMMEDIATE 'CREATE TABLE link_emp (idemp1 NUMBER, idemp2 NUMBER)';
EXECUTE IMMEDIATE 'ALTER SESSION SET SQL_TRACE TRUE';
```

5. Run an anonymous block with bind variables using `EXECUTE IMMEDIATE`.

```
EXECUTE IMMEDIATE 'BEGIN raise_sal (:col_val, :col_name, :amount); END;'
  USING 134, 'EMPLOYEE_ID', 10;
```

For more information, see [EXECUTE IMMEDIATE Statement](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/EXECUTE-IMMEDIATE-statement.html#GUID-C3245A95-B85B-4280-A01F-12307B108DC8 "https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/EXECUTE-IMMEDIATE-statement.html#GUID-C3245A95-B85B-4280-A01F-12307B108DC8") in the _Oracle documentation_.

## MySQL usage

The `EXECUTE` command in MySQL runs commands that were prepared by the `PREPARE` command. It can also run DDL statements and retrieve data using SQL commands. Similar to Oracle, you can use the MySQL `EXECUTE` command with bind variables.

The `PREPARE` command can receive a `SELECT`, `INSERT`, `UPDATE`, `DELETE`, or `VALUES` statement and parse it with a user-specified qualifying name so that you can use the `EXECUTE` command later without the need to re-parse the SQL statement for each run.

- Statement names are not case-sensitive. A Statement name is either a string literal or a user variable containing the text of the SQL statement.
- If a prepared statement with the given name already exists, it is deallocated implicitly before the new statement is prepared.
- The scope of a prepared statement is the session in which it is created.

### Examples

Run a SQL `SELECT` query with the table name as a dynamic variable using bind variables. This query returns the number of employees under a manager with a specific ID.

```
PREPARE stmt1 FROM 'SELECT count(*) FROM employees WHERE ID=?';
SET @man_id = 3;
EXECUTE stmt1 USING @a;

count(*)
2
```

Run a DML command with no variables and then with variables.

```
PREPARE stmt1 FROM 'INSERT INTO numbers (a) VALUES (1)';
EXECUTE stmt1;

PREPARE stmt1 FROM 'INSERT INTO numbers (a) VALUES (?)';
SET @man_id = 3;
EXECUTE stmt1 USING @a;
```

Run a DDL command.

```
PREPARE stmt1 FROM 'CREATE TABLE numbers (num integer)';
EXECUTE stmt1;
```

## Summary

| Functionality                             | Oracle EXECUTE IMMEDIATE                                                                  | MySQL EXECUTE and PREPARE                                                                                     |
| ----------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------- | --- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Run SQL with results and bind variables   | ```<br>EXECUTE IMMEDIATE 'select salary<br>from employees WHERE '                         |                                                                                                               | col_name |     | <br>' = :1' INTO amount USING col_val;<br>``` | N/A                                                                                                                                        |
| Run DML with variables and bind variables | ```<br>EXECUTE IMMEDIATE 'UPDATE<br>employees SET salary = salary + :1<br>WHERE '         |                                                                                                               | col_name |     | ' = :2'<br>USING amount, col_val;<br>```      | `<br>PREPARE stmt1 FROM 'UPDATE<br>employees SET salary = salary + ?<br>WHERE ? = ?'<br>EXECUTE stmt1 USING @amount,@<br>col,@colval;<br>` |
| Run DDL                                   | `<br>EXECUTE IMMEDIATE 'CREATE<br>TABLE link_emp (idemp1 NUMBER,<br>idemp2 NUMBER)';<br>` | `<br>PREPARE stmt1 FROM 'CREATE<br>TABLE link_emp (idemp1 INTEGER,<br>idemp2 INTEGER)'<br>EXECUTE stmt1;<br>` |
| Run an anonymous block                    | `<br>EXECUTE IMMEDIATE 'BEGIN<br>DBMS_OUTPUT.PUT_LINE<br>("Anonymous Block"); END;';<br>` | N/A                                                                                                           |

For more information, see [EXECUTE Statement](https://dev.mysql.com/doc/refman/5.7/en/execute.html "https://dev.mysql.com/doc/refman/5.7/en/execute.html") and [PREPARE Statement](https://dev.mysql.com/doc/refman/5.7/en/prepare.html "https://dev.mysql.com/doc/refman/5.7/en/prepare.html") in the _MySQL documentation_.
