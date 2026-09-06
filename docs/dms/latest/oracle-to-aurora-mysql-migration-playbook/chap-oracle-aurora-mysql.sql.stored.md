

# Oracle procedures and functions and MySQL stored procedures
<a name="chap-oracle-aurora-mysql.sql.stored"></a>

By migrating procedures, functions, and stored procedures, you can preserve existing business logic and functionality in the new database. The following sections provide detailed steps for migrating these database objects using AWS DMS, ensuring a smooth transition while maintaining data integrity and application compatibility.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-4.png)  |  [Stored Procedures](chap-oracle-aurora-mysql.tools.actioncode.md#chap-oracle-aurora-mysql.tools.actioncode.storedprocedures)  | Syntax and option differences. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.sql.stored.oracle"></a>

PL/SQL is Oracle built-in database programming language providing several methods to store and run reusable business logic from within the database. Procedures and functions are reusable snippets of code created using the `CREATE PROCEDURE` and the `CREATE FUNCTION` statements.

Stored procedures and stored functions are PL/SQL units of code consisting of SQL and PL/SQL statements that solve specific problems or perform a set of related tasks.

 **Procedure** is used to perform database actions with PL/SQL.

 **Function** is used to perform a calculation and return a result.

### Privileges for creating procedures and functions
<a name="chap-oracle-aurora-mysql.sql.stored.oracle.privileges"></a>

To create procedures and functions in their own schema, Oracle database users need the `CREATE PROCEDURE` system privilege.

To create procedures or functions in other schemas, database users need the `CREATE ANY PROCEDURE` privilege.

To run a procedure or function, database users need the `EXECUTE` privilege.

### Package and package body
<a name="chap-oracle-aurora-mysql.sql.stored.oracle.package"></a>

In addition to stored procedures and functions, Oracle also provides packages to encapsulate related procedures, functions, and other program objects.

 **Package** declares and describes all the related PL/SQL elements.

 **Package body** contains the executable code.

To run a stored procedure or function created inside a package, specify the package name and the stored procedure or function name.

```
EXEC PKG_EMP.CALCULTE_SAL('100');
```

### Examples
<a name="chap-oracle-aurora-mysql.sql.stored.oracle.examples"></a>

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

## MySQL usage
<a name="chap-oracle-aurora-mysql.sql.stored.mysql"></a>

Aurora MySQL Stored Procedures provide similar functionality to Oracle stored procedures. As with Oracle, Aurora MySQL supports security execution context. It also supports input, output, and bi-directional parameters.

Stored procedures are typically used for:
+  **Code reuse** — Stored procedures provide a convenient code encapsulation and reuse mechanism for multiple applications, potentially written in various languages, requiring the same database operations.
+  **Security management** — By allowing access to base tables only through stored procedures, administrators can manage auditing and access permissions. This approach minimizes dependencies between application code and database code. Administrators can use stored procedures to process business rules and to perform auditing and logging.
+  **Performance improvements** — Full SQL query text does not need to be transferred from the client to the database.

**Note**  
Aurora MySQL stored procedures, triggers, and user-defined functions are collectively referred to as Stored Routines. When binary logging is enabled, MySQL `SUPER` privilege is required to run stored routines. However, you can run stored routines with binary logging enabled without `SUPER` privilege by setting `thelog_bin_trust_function_creators` parameter to true for the DB parameter group for your MySQL instance.

Aurora MySQL permits stored routines to contain control flow, DML, DDL, and transaction management statements including `START TRANSACTION`, `COMMIT`, and `ROLLBACK`.

### Syntax
<a name="chap-oracle-aurora-mysql.sql.stored.mysql.syntax"></a>

```
CREATE [DEFINER = { user | CURRENT_USER }] PROCEDURE sp_name ([proc_parameter[,...]])
[characteristic ...]
routine_body

proc_parameter: [ IN | OUT | INOUT ] param_name type

characteristic: COMMENT 'string' | LANGUAGE SQL | [NOT] DETERMINISTIC | { CONTAINS SQL
| NO SQL | READS SQL DATA | MODIFIES SQL DATA } | SQL SECURITY { DEFINER | INVOKER }
```

### Examples
<a name="chap-oracle-aurora-mysql.sql.stored.mysql.examples"></a>

The following example demonstrates using a `LOOP` cursor with a source table to replace table valued parameters.

Create an `OrderItems` table.

```
CREATE TABLE OrderItems(
  OrderID INT NOT NULL,
  Item VARCHAR(20) NOT NULL,
  Quantity SMALLINT NOT NULL,
  PRIMARY KEY(OrderID, Item));
```

Create and populate `SourceTable` as a temporary data store for incoming rows.

```
CREATE TABLE SourceTable (
  OrderID INT,
  Item VARCHAR(20),
  Quantity SMALLINT,
  PRIMARY KEY (OrderID, Item));

INSERT INTO SourceTable (
  OrderID, Item, Quantity)
  VALUES (1, 'M8 Bolt', 100),
  (2, 'M8 Nut', 100),
  (3, 'M8 Washer', 200);
```

Create a procedure to loop through all rows in `SourceTable` and insert them into the `OrderItems` table.

```
CREATE PROCEDURE LoopItems()
BEGIN
  DECLARE done INT DEFAULT FALSE;
  DECLARE var_OrderID INT;
  DECLARE var_Item VARCHAR(20);
  DECLARE var_Quantity SMALLINT;
  DECLARE ItemCursor CURSOR FOR SELECT OrderID, Item, Quantity FROM SourceTable;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  OPEN ItemCursor;
  CursorStart: LOOP
  FETCH NEXT FROM ItemCursor INTO var_OrderID, var_Item, var_Quantity;
  IF Done THEN LEAVE CursorStart;
  END IF;
    INSERT INTO OrderItems (OrderID, Item, Quantity)
    VALUES (var_OrderID, var_Item, var_Quantity);
  END LOOP;
  CLOSE ItemCursor;
END;
```

Call the stored procedure.

```
CALL LoopItems();
```

Select all rows from the `OrderItems` table.

```
SELECT * FROM OrderItems;

OrderID  Item       Quantity
1        M8 Bolt    100
2        M8 Nut     100
3        M8 Washer  200
```

## Summary
<a name="chap-oracle-aurora-mysql.sql.stored.summary"></a>

The following table summarizes the differences between Aurora MySQL stored procedures and Oracle stored procedures.


|  | Oracle | Aurora MySQL | Workaround | 
| --- | --- | --- | --- | 
| General `CREATE` syntax differences |  <pre>CREATE PROCEDURE<br /><Procedure Name><br />Parameter1 <Type>, ...n<br />AS <Body></pre>  |  <pre>CREATE PROCEDURE<br /><Procedure Name><br />(Parameter1 <Type>,...n)<br /><Body></pre>  | Rewrite stored procedure creation scripts to use `PROCEDURE` instead of `PROC`. Rewrite stored procedure creation scripts to omit the `AS` keyword. | 
| Security context |  <pre>{ AUTHID }<br />{ CURRENT_USER | DEFINER}</pre>  | <pre>DEFINER = 'user' |<br />CURRENT_USER</pre>in conjunction with<pre>SQL SECURITY {<br />DEFINER | INVOKER }</pre> | For stored procedures that use an explicit user name, rewrite the code from `EXECUTE AS 'user'` to `DEFINER = 'user'` and `SQL SECURITY DEFINER`.<br />For stored procedures that use the `CALLER` option, rewrite the code to include `SQL SECURITY INVOKER`.<br />For stored procedures that use the `SELF` option, rewrite the code to `DEFINER = CURRENT_USER` and `SQL SECURITY DEFINER`. | 
| Parameter direction |  `IN` and `OUT`, by default `OUT` can be used as `IN` as well. |  `IN`, `OUT`, and `INOUT`  |  | 

For more information, see [Stored Procedures and Functions](https://dev.mysql.com/doc/refman/5.7/en/faqs-stored-procs.html) and [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html) in the *MySQL documentation*.