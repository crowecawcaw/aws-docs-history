

# Oracle procedures and functions and PostgreSQL stored procedures
<a name="chap-oracle-aurora-pg.sql.stored"></a>

With AWS DMS, you can migrate Oracle procedures and functions, as well as PostgreSQL stored procedures, to various target databases supported by the service. Oracle procedures and functions are reusable code blocks written in PL/SQL that perform specific tasks within an Oracle database. PostgreSQL stored procedures are similar reusable code blocks for PostgreSQL databases.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-3.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-4.png)  |  [Stored Procedures](chap-oracle-aurora-pg.tools.actioncode.md#chap-oracle-aurora-pg.tools.actioncode.procedures)  | Syntax and option differences | 

## Oracle usage
<a name="chap-oracle-aurora-pg.sql.stored.ora"></a>

PL/SQL is Oracle built-in database programming language providing several methods to store and run reusable business logic from within the database. Procedures and functions are reusable snippets of code created using the `CREATE PROCEDURE` and the `CREATE FUNCTION` statements.

Stored procedures and stored functions are PL/SQL units of code consisting of SQL and PL/SQL statements that solve specific problems or perform a set of related tasks.

 **Procedure** is used to perform database actions with PL/SQL.

 **Function** is used to perform a calculation and return a result.

### Privileges for creating procedures and functions
<a name="chap-oracle-aurora-pg.sql.stored.ora.privileges"></a>

To create procedures and functions in their own schema, Oracle database users need the `CREATE PROCEDURE` system privilege.

To create procedures or functions in other schemas, database users need the `CREATE ANY PROCEDURE` privilege.

To run a procedure or function, database users need the `EXECUTE` privilege.

### Package and package body
<a name="chap-oracle-aurora-pg.sql.stored.ora.package"></a>

In addition to stored procedures and functions, Oracle also provides packages to encapsulate related procedures, functions, and other program objects.

 **Package** declares and describes all the related PL/SQL elements.

 **Package Body** contains the executable code.

To run a stored procedure or function created inside a package, specify the package name and the stored procedure or function name.

```
EXEC PKG_EMP.CALCULTE_SAL('100');
```

 **Examples** 

Create an Oracle stored procedure using the `CREATE OR REPLACE PROCEDURE` statement. The optional `OR REPLACE` clause overwrites an existing stored procedure with the same name if it exists.

```
CREATE OR REPLACE PROCEDURE EMP_SAL_RAISE
(P_EMP_ID IN NUMBER, SAL_RAISE IN NUMBER)
AS
V_EMP_CURRENT_SAL NUMBER;
BEGIN
SELECT SALARY INTO V_EMP_CURRENT_SAL FROM EMPLOYEES WHERE EMPLOYEE_ID=P_EMP_ID;
UPDATE EMPLOYEES
SET SALARY=V_EMP_CURRENT_SAL+SAL_RAISE
WHERE EMPLOYEE_ID=P_EMP_ID;
DBMS_OUTPUT.PUT_LINE('New Salary For Employee ID: '||P_EMP_ID||' Is '||(V_EMP_CURRENT_
SAL+SAL_RAISE));
EXCEPTION WHEN OTHERS THEN
RAISE_APPLICATION_ERROR(-20001,'An error was encountered - '||SQLCODE||' -ERROR-
'||SQLERRM);
ROLLBACK;
COMMIT;
END;
/
-- Run
EXEC EMP_SAL_RAISE(200, 1000);
```

Create a function using the `CREATE OR REPLACE FUNCTION` statement.

```
CREATE OR REPLACE FUNCTION EMP_PERIOD_OF_SERVICE_YEAR
(P_EMP_ID NUMBER)
RETURN NUMBER
AS
V_PERIOD_OF_SERVICE_YEARS NUMBER;
BEGIN
SELECT EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM TO_DATE(HIRE_DATE)) INTO V_PERIOD_OF_SERVICE_YEARS
FROM EMPLOYEES
WHERE EMPLOYEE_ID=P_EMP_ID;
RETURN V_PERIOD_OF_SERVICE_YEARS;
END;
/

SELECT EMPLOYEE_ID,FIRST_NAME, EMP_PERIOD_OF_SERVICE_YEAR(EMPLOYEE_ID) AS PERIOD_OF_SERVICE_YEAR FROM EMPLOYEES;
EMPLOYEE_ID  FIRST_NAME  PERIOD_OF_SERVICE_YEAR
174          Ellen       13
166          Sundar      9
130          Mozhe       12
105          David       12
204          Hermann     15
116          Shelli      12
167          Amit        9
172          Elizabeth   10
```

Create a package using the `CREATE OR REPLACE PACKAGE` statement.

```
CREATE OR REPLACE PACKAGE PCK_CHINOOK_REPORTS
AS
PROCEDURE GET_ARTIST_BY_ALBUM(P_ARTIST_ID ALBUM.TITLE%TYPE);
PROCEDURE CUST_INVOICE_BY_YEAR_ANALYZE;
END;
```

Create a new package using the `CREATE OR REPLACE PACKAGE BODY` statement.

```
CREATE OR REPLACE PACKAGE BODY PCK_CHINOOK_REPORTS
AS
PROCEDURE GET_ARTIST_BY_ALBUM(P_ARTIST_ID ALBUM.TITLE%TYPE)
IS
V_ARTIST_NAME ARTIST.NAME%TYPE;
BEGIN
SELECT ART.NAME INTO V_ARTIST_NAME
FROM ALBUM ALB JOIN ARTIST ART USING(ARTISTID)
WHERE ALB.TITLE=P_ARTIST_ID;
DBMS_OUTPUT.PUT_LINE('ArtistName: '||V_ARTIST_NAME);
END;

PROCEDURE CUST_INVOICE_BY_YEAR_ANALYZE
AS
V_CUST_GENRES VARCHAR2(200);
BEGIN
FOR V IN(SELECT CUSTOMERID, CUSTNAME, LOW_YEAR, HIGH_YEAR, CUST_AVG FROM TMP_CUST_
INVOICE_ANALYSE)
LOOP
IF SUBSTR(V.LOW_YEAR, -4) > SUBSTR(V.HIGH_YEAR , -4) THEN
SELECT LISTAGG(GENRE, ',') WITHIN GROUP (ORDER BY GENRE) INTO V_CUST_GENRES FROM
(SELECT DISTINCT
FUNC_GENRE_BY_ID(TRC.GENREID) AS GENRE
FROM TMP_CUST_INVOICE_ANALYSE TMPTBL JOIN INVOICE INV USING(CUSTOMERID)
JOIN INVOICELINE INVLIN
ON INV.INVOICEID = INVLIN.INVOICEID
JOIN TRACK TRC
ON TRC.TRACKID = INVLIN.TRACKID
WHERE CUSTOMERID=V.CUSTOMERID);
DBMS_OUTPUT.PUT_LINE('Customer: '||UPPER(V.CUSTNAME)||' - Offer a Discount According
To Preferred Genres: '||UPPER(V_CUST_GENRES));
END IF;
END LOOP;
END;
END;

EXEC PCK_CHINOOK_REPORTS.GET_ARTIST_BY_ALBUM();
EXEC PCK_CHINOOK_REPORTS.CUST_INVOICE_BY_YEAR_ANALYZE;
```

The preceding examples demonstrate basic Oracle PL/SQL procedure and function capabilities. Oracle PL/SQL provides a large number of features and capabilities that aren’t within the scope of this document.

For more information, see [CREATE FUNCTION](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-FUNCTION.html#GUID-156AEDAC-ADD0-4E46-AA56-6D1F7CA63306) and [CREATE PROCEDURE](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-PROCEDURE.html#GUID-771879D8-BBFD-4D87-8A6C-290102142DA3) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.sql.stored.pg"></a>

PostgreSQL provides support for both stored procedures and stored functions using the `CREATE FUNCTION` statement. To emphasize, the procedural statements used by PostgreSQL support the `CREATE FUNCTION` statement only. The `CREATE PROCEDURE` statement isn’t compatible with this PostgreSQL version.

PL/pgSQL is the main database programming language used for migrating from Oracle PL/SQL code. PostgreSQL support additional programming languages, also available in Amazon Aurora PostgreSQL:
+ PL/pgSQL
+ PL/Tcl
+ PL/Perl.

Use the `show.rds.extensions` command to view all available extensions for Amazon Aurora.

 **Interchangeability between Oracle PL/SQL and PostgreSQL PL/pgSQL** 

PostgreSQL PL/pgSQL language is often considered the ideal candidate to migrate from Oracle PL/SQL code because many of the Oracle PL/SQL syntax elements are supported by PostgreSQL PL/pgSQL code.

For example, Oracle `CREATE OR REPLACE PROCEDURE` statement is supported by PostgreSQL PL/pgSQL. Many other PL/SQL syntax elements are also supported making PostgreSQL and PL/pgSQL natural alternatives when migrating from Oracle.

 **PostgreSQL create function privileges** 

To create a function, a user must have `USAGE` privilege on the language. When creating a function, a language parameter can be specified as shown in the examples.

 **Examples** 

Converting Oracle Stored Procedures and Functions to PostgreSQL PL/pgSQL.

Use the PostgreSQL `CREATE FUNCTION` command to create a new function named `FUNC_ALG`.

```
CREATE OR REPLACE FUNCTION FUNC_ALG(P_NUM NUMERIC)
RETURNS NUMERIC
AS $$
BEGIN
  RETURN P_NUM * 2;
END; $$
LANGUAGE PLPGSQL;
```

Using a `CREATE OR REPLACE` statement creates a new function, or replaces an existing function, with these limitations:
+ You can’t change the function name or argument types.
+ The statement doesn’t allow changing the existing function return type.
+ The user must own the function to replace it.
+  `INPUT` parameter (`P_NUM`) is implemented similarly to Oracle PL/SQL `INPUT` parameter.
+ Two dollar signs are used to prevent the need to use single-quoted string escape elements. With the two dollar signs, there is no need to use escape characters in the code when using single quotation marks ( ' ). The two dollar signs appear after the keyword `AS` and after the function keyword `END`.
+ Use the `LANGUAGE PLPGSQL` parameter to specify the language for the created function.

Convert the Oracle `EMP_SAL_RAISE` PL/SQL function to PostgreSQL PL/pgSQL.

```
CREATE OR REPLACE FUNCTION EMP_SAL_RAISE
(IN P_EMP_ID DOUBLE PRECISION,
IN SAL_RAISE DOUBLE PRECISION)
RETURNS VOID
AS $$
DECLARE
V_EMP_CURRENT_SAL DOUBLE PRECISION;
BEGIN
SELECT SALARY INTO STRICT V_EMP_CURRENT_SAL
FROM EMPLOYEES WHERE EMPLOYEE_ID = P_EMP_ID;

UPDATE EMPLOYEES SET SALARY = V_EMP_CURRENT_SAL +
SAL_RAISE WHERE EMPLOYEE_ID = P_EMP_ID;

RAISE DEBUG USING MESSAGE := CONCAT_WS('',
'NEW SALARY FOR EMPLOYEE ID: ', P_EMP_ID, 'IS ',
(V_EMP_CURRENT_SAL + SAL_RAISE));
EXCEPTION
WHEN OTHERS THEN
RAISE USING ERRCODE := '20001', MESSAGE :=
CONCAT_WS('', 'AN ERROR WAS ENCOUNTERED - ',
SQLSTATE, ' -ERROR-', SQLERRM);
END; $$
LANGUAGE PLPGSQL;
select emp_sal_raise(200, 1000);
```

Convert the Oracle `EMP_PERIOD_OF_SERVICE_YEAR` PL/SQL function to PostgreSQL PL/pgSQL.

```
CREATE OR REPLACE FUNCTION
EMP_PERIOD_OF_SERVICE_YEAR (IN P_EMP_ID DOUBLE PRECISION)
RETURNS DOUBLE PRECISION
AS $$
DECLARE
V_PERIOD_OF_SERVICE_YEARS DOUBLE PRECISION;
BEGIN
SELECT
EXTRACT (YEAR FROM NOW()) - EXTRACT (YEAR FROM (HIRE_DATE))
INTO STRICT V_PERIOD_OF_SERVICE_YEARS
FROM EMPLOYEES
WHERE EMPLOYEE_ID = P_EMP_ID;
RETURN V_PERIOD_OF_SERVICE_YEARS;
END; $$
LANGUAGE PLPGSQL;
SELECT EMPLOYEE_ID,FIRST_NAME,
EMP_PERIOD_OF_SERVICE_YEAR(EMPLOYEE_ID) AS
PERIOD_OF_SERVICE_YEAR
FROM EMPLOYEES;
```

### Oracle Packages and Package Bodies
<a name="chap-oracle-aurora-pg.sql.stored.pg.bodies"></a>

PostgreSQL doesn’t support Oracle packages and package bodies. All PL/SQL objects must be converted to PostgreSQL functions. The following examples describe how the Amazon Schema Conversion Tool (SCT) handles Oracle packages and package body names.

Oracle package name: `PCK_CHINOOK_REPORTS`. Oracle package body: `GET_ARTIST_BY_ALBUM`.

```
EXEC PCK_CHINOOK_REPORTS.GET_ARTIST_BY_ALBUM('');
```

The PostgreSQL code converted with AWS SCT uses the `$` sign to separate the package and the package name.

```
SELECT PCK_CHINOOK_REPORTS$GET_ARTIST_BY_ALBUM('');
```

 **Examples** 

Convert an Oracle package and package body to PostgreSQL PL/pgSQL.

In the following example, the Oracle package name is `PCK_CHINOOK_REPORTS`, and the Oracle package body is `GET_ARTIST_BY_ALBUM`.

```
CREATE OR REPLACE FUNCTION
  chinook."PCK_CHINOOK_REPORTS$GET_ARTIST_BY_ALBUM"
  (p_artist_id text)
  RETURNS void
  LANGUAGE plpgsql
  AS $function$
  DECLARE
    V_ARTIST_NAME CHINOOK.ARTIST.NAME%TYPE;
  BEGIN
    SELECT art.name INTO STRICT V_ARTIST_NAME
    FROM chinook.album AS alb
    JOIN chinook.artist AS art
    USING (artistid)
    WHERE alb.title = p_artist_id;
  RAISE DEBUG USING MESSAGE := CONCAT_WS('', 'ArtistName: ', V_ARTIST_NAME);
END;
$function$;

-- Procedures (Packages) Verification
set client_min_messages = 'debug';
-- Equivalent to Oracle SET SERVEROUTPUT ON
select chinook.pck_chinook_reports$get_artist_by_album(' Fireball');
```

In the following example, the Oracle package name is `PCK_CHINOOK_REPORTS`, and the Oracle package body is `CUST_INVOICE_BY_YEAR_ANALYZE`.

```
CREATE OR REPLACE FUNCTION chinook."pck_chinook_reports$cust_invoice_by_year_analyze" ()
RETURNS void
LANGUAGE plpgsql
AS $function$
DECLARE
  v_cust_genres CHARACTER VARYING(200);
  v RECORD;
BEGIN
  FOR v IN
  SELECT customerid, custname, low_year, high_year, cust_avg
  FROM chinook.tmp_cust_invoice_analyse
  LOOP
    IF SUBSTR(v.low_year, - 4) > SUBSTR(v.high_year, - 4) THEN
-- Altering Oracle LISTAGG Function With PostgreSQL STRING_AGG Function
      select string_agg(genre, ',') into v_cust_genres
      from (select distinct chinook.func_genre_by_id(trc.genreid) as genre
      from chinook.tmp_cust_invoice_analyse tmptbl
      join chinook.INVOICE inv using(customerid)
      join chinook.INVOICELINE invlin on inv.invoiceid = invlin.invoiceid
      join chinook.TRACK trc on trc.trackid = invlin.trackid
      where customerid=v.CUSTOMERID) a;

-- PostgreSQL Equivalent To Oracle DBMS_OUTPUT.PUT_LINE()\
    RAISE DEBUG USING MESSAGE := CONCAT_WS('', 'Customer: ',
    UPPER(v.custname), ' - Offer a Discount According To Preferred Genres: ', UPPER(v_
    cust_genres));
    END IF;
  END LOOP;
END;
$function$;

-- Running
SELECT chinook.pck_chinook_reports$cust_invoice_by_year_analyze();
```

New behavior in PostgreSQL version 10 for a set-returning function, used by the `LATERAL FROM` clause.

 **Previous** 

```
CREATE TABLE emps (id int, manager int);
INSERT INTO tab VALUES (23, 24), (52, 23), (21, 65);
SELECT x, generate_series(1,5) AS g FROM tab;
id |g
---|--
23 |1
23 |2
23 |3
23 |4
23 |5
52 |1
52 |2
52 |3
52 |4
52 |5
21 |1
21 |2
21 |3
21 |4
21 |5
```

 **New** 

```
SELECT id, g FROM emps, LATERAL generate_series(1,5) AS g;
id |g
---|--
23 |1
23 |2
23 |3
23 |4
23 |5
52 |1
52 |2
52 |3
52 |4
52 |5
21 |1
21 |2
21 |3
21 |4
21 |5
```

Here the planner could choose to put the set-return function on the outside of the nestloop join, since it has no actual lateral dependency on emps table.

For more information, see [CREATE FUNCTION](https://www.postgresql.org/docs/13/sql-createfunction.html), [PL/pgSQL — SQL Procedural Language](https://www.postgresql.org/docs/13/plpgsql.html), [https://www.postgresql.org/docs/13/xplang.html](https://www.postgresql.org/docs/13/xplang.html), and [Query Language (SQL) Functions](https://www.postgresql.org/docs/13/xfunc-sql.html) in the *PostgreSQL documentation*.