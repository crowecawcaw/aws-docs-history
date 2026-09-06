

# Oracle and PostgreSQL user-defined functions
<a name="chap-oracle-aurora-pg.sql.udfs"></a>

With AWS DMS, you can migrate user-defined functions (UDFs) from Oracle and PostgreSQL databases to compatible target databases. UDFs are custom functions written in programming languages like PL/SQL or SQL that extend the functionality of the database management system.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-3.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-4.png)  |  [Stored Procedures](chap-oracle-aurora-pg.tools.actioncode.md#chap-oracle-aurora-pg.tools.actioncode.procedures)  | Syntax and option differences. | 

## Oracle usage
<a name="chap-oracle-aurora-pg.sql.udfs.ora"></a>

You can create an Oracle user-defined function (UDF) using PL/SQL, Java, or C. UDFs are useful for providing functionality not available in SQL or SQL built-in functions. They can appear in SQL statements wherever built-in SQL functions can appear.

You can use UDFs in the following cases:
+ To return a single value from a `SELECT` statement (scalar function).
+ While performing DML operations.
+ In `WHERE`, `GROUP BY`, `ORDER BY`, `HAVING`, `CONNECT BY`, and `START WITH` clauses.

 **Examples** 

Create a simple Oracle UDF with arguments for employee `HIRE_DATE` and `SALARY` as `INPUT` parameters and calculate the overall salary over the employee’s years of service for the company.

```
CREATE OR REPLACE FUNCTION TOTAL_EMP_SAL_BY_YEARS
(p_hire_date DATE, p_current_sal NUMBER)
RETURN NUMBER
AS
v_years_of_service NUMBER;
v_total_sal_by_years NUMBER;
BEGIN
SELECT EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM to_date(p_hire_date))
INTO v_years_of_service FROM dual;
v_total_sal_by_years:=p_current_sal*v_years_of_service;
RETURN v_total_sal_by_years;
END;
/
-- Verifying
SELECT EMPLOYEE_ID, FIRST_NAME, TOTAL_EMP_SAL_BY_YEARS(HIRE_DATE, SALARY)AS TOTAL_
SALARY
FROM EMPLOYEES;

EMPLOYEE_ID FIRST_NAME TOTAL_SALARY
100         Steven     364000
101         Neena      204000
102         Lex        272000
103         Alexander  99000
104         Bruce      60000
105         David      57600
…
```

For more information, see [CREATE FUNCTION](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-FUNCTION.html#GUID-156AEDAC-ADD0-4E46-AA56-6D1F7CA63306) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.sql.udfs.pg"></a>

PostgreSQL supports the creation of user-defined functions using the `CREATE FUNCTION` statement. The PostgreSQL extended SQL language, PL/pgSQL, is the primary language to use while migrating from Oracle PL/SQL user-defined functions.

To create a function, a user needs the `USAGE` privilege on the language.

 **Examples** 

Convert the Oracle user-defined function from the previous Oracle section to a PostgreSQL PL/pgSQL function.

```
CREATE OR REPLACE FUNCTION total_emp_sal_by_years
(P_HIRE_DATE DATE, P_CURRENT_SAL NUMERIC)
RETURNS NUMERIC
AS
$BODY$
DECLARE
V_YEARS_OF_SERVICE NUMERIC;
V_TOTAL_SAL_BY_YEARS NUMERIC;
BEGIN
SELECT EXTRACT(YEAR FROM NOW()) - EXTRACT(YEAR FROM (P_HIRE_DATE)) INTO V_YEARS_OF_SERVICE;
V_TOTAL_SAL_BY_YEARS:=P_CURRENT_SAL*V_YEARS_OF_SERVICE;
RETURN V_TOTAL_SAL_BY_YEARS;
END;
$BODY$
LANGUAGE PLPGSQL;

SELECT EMPLOYEE_ID, FIRST_NAME, TOTAL_EMP_SAL_BY_YEARS(HIRE_DATE, SALARY)AS TOTAL_SALARY
FROM EMPLOYEES;

employee_id  first_name  total_salary
100          Steven      364000.00
101          Neena       204000.00
102          Lex         272000.00
103          Alexander   99000.00
104          Bruce       60000.00
105          David       57600.00
106          Valli       52800.00
107          Diana       42000.00
…
```

For more information, see [User-Defined Functions](https://www.postgresql.org/docs/13/xfunc.html) and [CREATE FUNCTION](https://www.postgresql.org/docs/13/sql-createfunction.html) in the *PostgreSQL documentation*, and [What is the AWS Schema Conversion Tool?](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) in the *user guide*.