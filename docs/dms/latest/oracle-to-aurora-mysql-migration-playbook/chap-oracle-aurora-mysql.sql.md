# Oracle anonymous block and MySQL transactions or procedures

With AWS DMS, you can run Oracle anonymous blocks and MySQL transactions or procedures to modify data or perform complex operations during a database migration. An Oracle anonymous block is a set of procedural statements that perform transaction control, data manipulation, or control flow operations. A MySQL transaction groups multiple SQL statements into a single logical unit of work, while procedures are reusable code objects containing SQL statements.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                            |
| ------------------------------- | ---------------------------------- | ------------------------- | ------------------------------------------ |
| Four star feature compatibility | N/A                                | N/A                       | Different syntax may require code rewrite. |

## Oracle usage

Oracle PL/SQL is a procedural extension of SQL. The PL/SQL program structure divides the code into blocks distinguished by the following keywords: `DECLARE`, `BEGIN`, `EXCEPTION`, and `END`.

An unnamed PL/SQL code block (code not stored in the database as a procedure, function, or package) is known as an anonymous block. An anonymous block serves as the basic unit of Oracle PL/SQL and contains the following code sections:

- **The declarative section** (optional) — Contains variables (names, data types, and initial values).
- **The executable section** (mandatory) — Contains executable statements (each block structure must contain at least one executable PL/SQL statement).
- **The exception-handling section** (optional) — Contains elements for handling exceptions or errors in the code.

### Examples

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

For more information, see [Overview of PL/SQL](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/overview.html#GUID-2FBCFBBE-6B42-4DB8-83F3-55B63B75B1EB "https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/overview.html#GUID-2FBCFBBE-6B42-4DB8-83F3-55B63B75B1EB") in the _Oracle documentation_.

## MySQL usage

You can achieve the similar functionality to Oracle Anonymous Blocks by using the Aurora MySQL `START TRANSACTION` command or a stored procedure.

For more information, see [Stored Procedures](chap-oracle-aurora-mysql.sql.md "chap-oracle-aurora-mysql.sql.md") and [Oracle Transaction Model and MySQL Transactions](chap-oracle-aurora-mysql.sql.md "chap-oracle-aurora-mysql.sql.md").
