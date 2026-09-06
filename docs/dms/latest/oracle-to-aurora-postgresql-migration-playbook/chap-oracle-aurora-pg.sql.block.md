

# Oracle anonymous block and PostgreSQL DO
<a name="chap-oracle-aurora-pg.sql.block"></a>

With AWS DMS, you can run PL/SQL anonymous blocks and PostgreSQL `DO` commands to perform custom database code operations during a database migration. An Oracle anonymous block is an unattached, unnamed PL/SQL code block that can contain SQL queries and PL/SQL statements. A PostgreSQL `DO` command runs an anonymous code block containing procedural language statements.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Four star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-4.png)  |  ![Three star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-3.png)  |  [Stored Procedures](chap-oracle-aurora-pg.tools.actioncode.md#chap-oracle-aurora-pg.tools.actioncode.procedures)  | Different syntax may require code rewrite. | 

## Oracle usage
<a name="chap-oracle-aurora-pg.sql.block.ora"></a>

Oracle PL/SQL is a procedural extension of SQL. The PL/SQL program structure divides the code into blocks distinguished by the following keywords: `DECLARE`, `BEGIN`, `EXCEPTION`, and `END`.

An unnamed PL/SQL code block (code not stored in the database as a procedure, function, or package) is known as an anonymous block. An anonymous block serves as the basic unit of Oracle PL/SQL and contains the following code sections:
+  **The declarative section** (optional) — Contains variables (names, data types, and initial values).
+  **The executable section** (mandatory) — Contains executable statements (each block structure must contain at least one executable PL/SQL statement).
+  **The exception-handling section** (optional) — Contains elements for handling exceptions or errors in the code.

 **Examples** 

Simple structure of an Oracle anonymous block.

```
SET SERVEROUTPUT ON;
BEGIN
DBMS_OUTPUT.PUT_LINE('hello world');
END;
/

hello world
PL/SQL procedure successfully completed.
```

Oracle PL/SQL Anonymous blocks can contain advanced code elements such as functions, cursors, dynamic SQL, and conditional logic. The following anonymous block uses a cursor, conditional logic, and exception-handling.

```
SET SERVEROUTPUT ON;
DECLARE
v_sal_chk        NUMBER;
v_emp_work_years NUMBER;
v_sql_cmd        VARCHAR2(2000);
BEGIN
FOR v IN (SELECT EMPLOYEE_ID, FIRST_NAME||' '||LAST_NAME AS
EMP_NAME, HIRE_DATE, SALARY FROM EMPLOYEES)
LOOP
v_emp_work_years:=EXTRACT(YEAR FROM SYSDATE) - EXTRACT (YEAR FROM v.hire_date);
IF v_emp_work_years>=10 and v.salary <= 6000 then
DBMS_OUTPUT.PUT_LINE('Consider a Bonus for: '||v.emp_name);
END IF;
END LOOP;
EXCEPTION WHEN OTHERS THEN
DBMS_OUTPUT.PUT_LINE('CODE ERR: '||sqlerrm);
END;
/
```

The preceding example calculates the number of years each employee has worked based on the `HIRE_DATE` column of the `EMPLOYEES` table. If the employee has worked for ten or more years and has a salary of $6000 or less, the system prints the message “Consider a Bonus for: <employee name>”.

For more information, see [Overview of PL/SQL](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/overview.html#GUID-2FBCFBBE-6B42-4DB8-83F3-55B63B75B1EB) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.sql.block.pg"></a>

PostgreSQL supports capabilities similar to Oracle anonymous blocks. In PostgreSQL, you can run PL/pgSQL code that isn’t stored in the database as an independent code segment using a PL/pgSQL `DO` statement.

PL/pgSQL is a PostgreSQL extension to the ANSI SQL and has many similar elements to Oracle PL/SQL. PostgreSQL `DO` uses a similar code structure to an Oracle anonymous block
+  **The declarative section** (optional).
+  **The executable section** (mandatory).
+  **The exception-handling section** (optional).

 **Examples** 

PostgreSQL DO simple structure.

```
SET CLIENT_MIN_MESSAGES = 'debug';
-- Equivalent To Oracle SET SERVEROUTPUT ON

DO $$
  BEGIN
    RAISE DEBUG USING MESSAGE := 'hello world';
  END $$;

DEBUG: hello world
DO
```

The PostgreSQL PL/pgSQL `DO` statement supports the use of advanced code elements such as functions, cursors, dynamic SQL, and conditional logic.

The following example is a more complex PL/pgSQL DO code structure converted from Oracle “employee bonus” PL/SQL anonymous block example presented in the previous section:

```
DO $$
  DECLARE
    v_sal_chk DOUBLE PRECISION;
    v_emp_work_years DOUBLE PRECISION;
    v_sql_cmd CHARACTER VARYING(2000);
    v RECORD;
  BEGIN
  FOR v IN
  SELECT employee_id, CONCAT_WS('', first_name, ' ', last_name) AS emp_name, hire_date, salary FROM employees
  LOOP
    v_emp_work_years := EXTRACT (YEAR FROM now()) - EXTRACT (YEAR FROM v.hire_date);
  IF v_emp_work_years >= 10 AND v.salary <= 6000 THEN
    RAISE DEBUG USING MESSAGE := CONCAT_WS('', 'Consider a Salary Raise for: ',v.emp_name);
  END IF;
END LOOP;
EXCEPTION
  WHEN others THEN
    RAISE DEBUG USING MESSAGE := CONCAT_WS('', 'CODE ERR: ',SQLERRM);
  END $$;
```

For more information, see [DO](https://www.postgresql.org/docs/13/sql-do.html) in the *PostgreSQL documentation*.