

# Oracle EXECUTE IMMEDIATE and PostgreSQL EXECUTE and PREPARE
<a name="chap-oracle-aurora-pg.sql.immediate"></a>

With AWS DMS, you can run dynamic SQL statements and prepared statements on source and target databases during a database migration. Oracle’s `EXECUTE IMMEDIATE` statement evaluates a string literal containing SQL statements at runtime. PostgreSQL’s `EXECUTE` statement executes a previously prepared statement, while `PREPARE` creates a prepared statement from a string literal.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Four star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-4.png)  |  ![Two star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-2.png)  | N/A | N/A | 

## Oracle usage
<a name="chap-oracle-aurora-pg.sql.immediate.ora"></a>

You can use Oracle `EXECUTE IMMEDIATE` statement to parse and run a dynamic SQL statement or an anonymous PL/SQL block. It also supports bind variables.

 **Examples** 

Run a dynamic SQL statement from within a PL/SQL procedure:

1. Create a PL/SQL procedure named `raise_sal`.

1. Define a SQL statement with a dynamic value for the column name included in the `WHERE` statement.

1. Use the `EXECUTE IMMEDIATE` command supplying the two bind variables to be used as part of the `SELECT` statement: `amount` and `col_val`.

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

1. Run the DDL operation from within an `EXECUTE IMMEDIATE` command.

   ```
   EXECUTE IMMEDIATE 'CREATE TABLE link_emp (idemp1 NUMBER, idemp2 NUMBER)';
   EXECUTE IMMEDIATE 'ALTER SESSION SET SQL_TRACE TRUE';
   ```

1. Run an anonymous block with bind variables using `EXECUTE IMMEDIATE`.

   ```
   EXECUTE IMMEDIATE 'BEGIN raise_sal (:col_val, :col_name, :amount); END;'
     USING 134, 'EMPLOYEE_ID', 10;
   ```

For more information, see [EXECUTE IMMEDIATE Statement](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/EXECUTE-IMMEDIATE-statement.html#GUID-C3245A95-B85B-4280-A01F-12307B108DC8) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.sql.immediate.pg"></a>

The PostgreSQL `EXECUTE` command prepares and runs commands dynamically. The `EXECUTE` command can also run DDL statements and retrieve data using SQL commands. Similar to Oracle, you can use the PostgreSQL `EXECUTE` command with bind variables.

 **Examples** 

Execute a SQL SELECT query with the table name as a dynamic variable using bind variables. This query returns the number of employees under a manager with a specific ID.

```
DO $$DECLARE
Tabname varchar(30) := 'employees';
num integer := 1;
cnt integer;
BEGIN
EXECUTE format('SELECT count(*) FROM %I WHERE manager = $1', tabname)
INTO cnt USING num;
RAISE NOTICE 'Count is % int table %', cnt, tabname;
END$$;
;
```

Run a DML command with no variables and then with variables.

```
DO $$DECLARE
BEGIN
EXECUTE 'INSERT INTO numbers (a) VALUES (1)';
EXECUTE format('INSERT INTO numbers (a) VALUES (%s)', 42);
END$$;
;
```

**Note**  
 `%s` formats the argument value as a simple string. A null value is treated as an empty string.  
 `%I` treats the argument value as an SQL identifier and double-quoting it if necessary. It is an error for the value to be null.

Run a DDL command.

```
DO $$DECLARE
BEGIN
EXECUTE 'CREATE TABLE numbers (num integer)';
END$$;
;
```

For more information, see [String Functions and Operators](https://www.postgresql.org/docs/13/functions-string.html) in the *PostgreSQL documentation*.

Using a `PREPARE` statement can improve performance for reusable SQL statements.

The `PREPARE` command can receive a `SELECT`, `INSERT`, `UPDATE`, `DELETE`, or `VALUES` statement and parse it with a user-specified qualifying name so you can use the `EXECUTE` command later without the need to re-parse the SQL statement on each run.
+ When using `PREPARE` to create a prepared statement, it will be viable for the scope of the current session.
+ If you run a DDL command on a database object referenced by the prepared SQL statement, the next `EXECUTE` command requires a hard parse of the SQL statement.

 **Example** 

Use `PREPARE` and `EXECUTE` commands together.

1. The SQL command is prepared with a user-specified qualifying name.

1. The SQL command runs several times, without the need for re-parsing.

```
PREPARE numplan (int, text, bool) AS
INSERT INTO numbers VALUES($1, $2, $3);

EXECUTE numplan(100, 'New number 100', 't');
EXECUTE numplan(101, 'New number 101', 't');
EXECUTE numplan(102, 'New number 102', 'f');
EXECUTE numplan(103, 'New number 103', 't');
```

## Summary
<a name="chap-oracle-aurora-pg.sql.immediate.summary"></a>


| Functionality | Oracle EXECUTE IMMEDIATE | PostgreSQL EXECUTE | 
| --- | --- | --- | 
| Execute SQL with results and bind variables |  <pre>EXECUTE IMMEDIATE 'select salary<br />from employees WHERE ' || col_name ||<br />' = :1' INTO amount USING col_val;</pre>  |  <pre>EXECUTE format('select salary from employees<br />WHERE %I = $1', col_name) INTO<br />amount USING col_val;</pre>  | 
| Execute DML with variables and bind variables |  <pre>EXECUTE IMMEDIATE 'UPDATE<br />employees SET salary = salary + :1<br />WHERE ' || col_name || ' = :2'<br />USING amount, col_val;</pre>  |  <pre>EXECUTE format('UPDATE employees<br />SET salary = salary + $1 WHERE %I = $2',<br />col_name) USING amount, col_val;</pre>  | 
| Execute DDL |  <pre>EXECUTE IMMEDIATE 'CREATE<br />TABLE link_emp (idemp1 NUMBER,<br />idemp2 NUMBER)';</pre>  |  <pre>EXECUTE 'CREATE TABLE link_emp<br />(idemp1 integer, idemp2 integer)';</pre>  | 
| Execute anonymous block |  <pre>EXECUTE IMMEDIATE 'BEGIN<br />DBMS_OUTPUT.PUT_LINE<br />("Anonymous Block"); END;';</pre>  |  <pre>DO $$DECLARE<br />BEGIN ... END$$;</pre>  | 

For more information, see [Basic Statements](https://www.postgresql.org/docs/13/plpgsql-statements.html) in the *PostgreSQL documentation*.