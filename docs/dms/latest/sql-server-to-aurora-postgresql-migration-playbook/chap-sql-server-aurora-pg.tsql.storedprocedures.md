

# Stored procedures for T-SQL
<a name="chap-sql-server-aurora-pg.tsql.storedprocedures"></a>

This topic provides reference information about the compatibility and differences between stored procedures in Microsoft SQL Server 2019 and Amazon Aurora PostgreSQL. You can use this guide to understand the key distinctions in syntax, security contexts, parameter handling, and supported features when migrating stored procedures from SQL Server to Aurora PostgreSQL.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-compatibility-3.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-automation-4.png)  |  [Stored Procedures](chap-sql-server-aurora-pg.tools.actioncode.md#chap-sql-server-aurora-pg.tools.actioncode.storedprocedures)  | Syntax and option differences. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-pg.tsql.storedprocedures.sqlserver"></a>

Stored procedures are encapsulated, persisted code modules that you can run using the `EXECUTE` T-SQL statement. They may have multiple input (`IN`) and output (`OUT`) parameters. Table-valued user-defined types can be used as input parameters. `IN` is the default direction for parameters, but `OUT` must be explicitly specified. You can specify parameters as both `IN` and `OUT`.

SQL Server allows you to run stored procedures in any security context using the `EXECUTE AS` option. You can explicitly recompile them for every run using the `RECOMPILE` option. You can encrypt them in the database using the `ENCRYPTION` option to prevent unauthorized access to the source code.

SQL Server provides a unique feature that allows you to use a stored procedure as an input to an INSERT statement. When using this feature, only the first row in the data set returned by the stored procedure is evaluated.

### Syntax
<a name="chap-sql-server-aurora-pg.tsql.storedprocedures.sqlserver.syntax"></a>

```
CREATE [ OR ALTER ] { PROC | PROCEDURE } <Procedure Name>
[<Parameter List>
[ WITH [ ENCRYPTION ]|[ RECOMPILE ]|[ EXECUTE AS ...]]
AS {
[ BEGIN ]
<SQL Code Body>
[ END ] }[;]
```

### Examples
<a name="chap-sql-server-aurora-pg.tsql.storedprocedures.sqlserver.examples"></a>

 **Create and run a stored procedure** 

The following example creates a simple parameterized stored procedure to validate the basic format of an email.

```
CREATE PROCEDURE ValidateEmail
@Email VARCHAR(128), @IsValid BIT = 0 OUT
AS
BEGIN
IF @Email LIKE N'%@%' SET @IsValid = 1
ELSE SET @IsValid = 0
RETURN @IsValid
END;
```

The following example runs this stored procedure.

```
DECLARE @IsValid BIT
EXECUTE [ValidateEmail]
@Email = 'X@y.com', @IsValid = @IsValid OUT;
SELECT @IsValid;

-- Returns 1
```

```
EXECUTE [ValidateEmail]
@Email = 'Xy.com', @IsValid = @IsValid OUT;
SELECT @IsValid;

-- Returns 0
```

The following example creates a stored procedure that uses `RETURN` to pass an error value to the application.

```
CREATE PROCEDURE ProcessImportBatch
@BatchID INT
AS
BEGIN
BEGIN TRY
EXECUTE Step1 @BatchID
EXECUTE Step2 @BatchID
EXECUTE Step3 @BatchID
END TRY
BEGIN CATCH
IF ERROR_NUMBER() = 235
RETURN -1 -- indicate special condition
ELSE
THROW -- handle error normally
END CATCH
END
```

 **Using a table-valued input parameter** 

The following example creates and populates an OrderItems table.

```
CREATE TABLE OrderItems(
OrderID INT NOT NULL,
Item VARCHAR(20) NOT NULL,
Quantity SMALLINT NOT NULL,
PRIMARY KEY(OrderID, Item)
);
```

```
INSERT INTO OrderItems (OrderID, Item, Quantity)
VALUES
(1, 'M8 Bolt', 100),
(2, 'M8 Nut', 100),
(3, 'M8 Washer', 200),
(3, 'M6 Washer', 100);
```

The following example creates a table-valued type for the `OrderItem` table-valued parameter.

```
CREATE TYPE OrderItems
AS TABLE
(
  OrderID INT NOT NULL,
  Item VARCHAR(20) NOT NULL,
  Quantity SMALLINT NOT NULL,
  PRIMARY KEY(OrderID, Item)
);
```

The following example creates a procedure to process order items.

```
CREATE PROCEDURE InsertOrderItems
@OrderItems AS OrderItems READONLY
AS
BEGIN
  INSERT INTO OrderItems(OrderID, Item, Quantity)
  SELECT OrderID,
    Item,
    Quantity
  FROM @OrderItems
END;
```

The following example populates the table-valued variable and passes the data set to the stored procedure.

```
DECLARE @OrderItems AS OrderItems;

INSERT INTO @OrderItems ([OrderID], [Item], [Quantity])
VALUES
(1, 'M8 Bolt', 100),
(1, 'M8 Nut', 100),
(1, M8 Washer, 200);

EXECUTE [InsertOrderItems]
@OrderItems = @OrderItems;

(3 rows affected)
   Item       Quantity
1  M8 Bolt    100
2  M8 Nut     100
3  M8 Washer  200
```

### INSERT…​ EXEC Syntax
<a name="chap-sql-server-aurora-pg.tsql.storedprocedures.sqlserver.insertsyntax"></a>

```
INSERT INTO <MyTable>
EXECUTE <MyStoredProcedure>;
```

For more information, see [CREATE PROCEDURE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-procedure-transact-sql?view=sql-server-ver15) in the *SQL Server documentation*.

## PostgreSQL Usage
<a name="chap-sql-server-aurora-pg.tsql.storedprocedures.pg"></a>

PostgreSQL version 10 provides support for both stored procedures and stored functions using the `CREATE FUNCTION` statement. To emphasize, only the `CREATE FUNCTION` is supported by the procedural statements used by PostgreSQL version 10. The `CREATE PROCEDURE` statement isn’t supported.

PL/pgSQL is the main database programming language used for migrating from SQL Server T-SQL code. PostgreSQL supports these additional programming languages, also available in Amazon Aurora PostgreSQL:
+ PL/pgSQL
+ PL/Tcl
+ PL/Perl

Use the `show.rds.extensions` command to view all available Amazon Aurora extensions.

### PostgreSQL Create Function Privileges
<a name="chap-sql-server-aurora-pg.tsql.storedprocedures.pg.privileges"></a>

To create a function, make sure that a user has the `USAGE` privilege on the language. When you create a function, you can specify a language parameter as shown in the following examples.

### Examples
<a name="chap-sql-server-aurora-pg.tsql.storedprocedures.pg.examples"></a>

The following example creates a new FUNC\_ALG function.

```
CREATE OR REPLACE FUNCTION FUNC_ALG(P_NUM NUMERIC)
RETURNS NUMERIC
AS $$
BEGIN
  RETURN P_NUM * 2;
END; $$
LANGUAGE PLPGSQL;
```

The `CREATE OR REPLACE` statement creates a new function or replaces an existing function with these limitations:
+ You can’t change the function name or argument types.
+ The statement doesn’t allow changing the existing function return type.
+ The user must own the function to replace it.
+ The `P_NUM` INPUT parameter is implemented similar to SQL Server T-SQL INPUT parameter.
+ The double dollar signs alleviate the need to use single-quoted string escape elements. With the double dollar sign, there is no need to use escape characters in the code when using single quotation marks. The double dollar sign appears after the keyword `AS` and after the function keyword `END`.
+ Use the `LANGUAGE PLPGSQL` parameter to specify the language for the created function.

The following example creates a function with PostgreSQL PL/pgSQL.

```
CREATE OR REPLACE FUNCTION EMP_SAL_RAISE
(IN P_EMP_ID DOUBLE PRECISION, IN SAL_RAISE DOUBLE PRECISION)
RETURNS VOID
AS $$
DECLARE
V_EMP_CURRENT_SAL DOUBLE PRECISION;
BEGIN
SELECT SALARY INTO STRICT V_EMP_CURRENT_SAL
FROM EMPLOYEES WHERE EMPLOYEE_ID = P_EMP_ID;

UPDATE EMPLOYEES SET SALARY = V_EMP_CURRENT_SAL + SAL_RAISE WHERE EMPLOYEE_ID = P_EMP_ID;

RAISE DEBUG USING MESSAGE := CONCAT_WS('', 'NEW SALARY FOR EMPLOYEE ID: ', P_EMP_ID, '
IS ', (V_EMP_CURRENT_SAL + SAL_RAISE));
EXCEPTION
WHEN OTHERS THEN
RAISE USING ERRCODE := '20001', MESSAGE := CONCAT_WS('', 'AN ERROR WAS ENCOUNTERED -', SQLSTATE, ' -ERROR-', SQLERRM);
END; $$
LANGUAGE PLPGSQL;

select emp_sal_raise(200, 1000);
```

In the preceding example, you can replace the `RAISE` command with `RETURN` to inform the application that an error occurred.

The following example creates a function with PostgreSQL PL/pgSQL.

```
CREATE OR REPLACE FUNCTION EMP_PERIOD_OF_SERVICE_YEAR (IN P_EMP_ID DOUBLE PRECISION)
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

SELECT EMPLOYEE_ID,FIRST_NAME, EMP_PERIOD_OF_SERVICE_YEAR(EMPLOYEE_ID) AS
PERIOD_OF_SERVICE_YEAR
FROM EMPLOYEES;
```

There is a new behavior in PostgreSQL version 10 for a set-returning function, used by `LATERAL FROM` clause.

 **PostgreSQL version 9.6 and lower** 

```
CREATE TABLE emps (id int, manager int);
INSERT INTO tab VALUES (23, 24), (52, 23), (21, 65);
SELECT x, generate_series(1,5) AS g FROM tab;

id  g
23  1
23  2
23  3
23  4
23  5
52  1
52  2
52  3
52  4
52  5
21  1
21  2
21  3
21  4
21  5
```

 **PostgreSQL version 10 and higher** 

```
SELECT id, g FROM emps, LATERAL generate_series(1,5) AS g;

id  g
23  1
23  2
23  3
23  4
23  5
52  1
52  2
52  3
52  4
52  5
21  1
21  2
21  3
21  4
21  5
```

In the preceding example, you can put the set-return function on the outside of the nested loop join because it has no actual lateral dependency on `emps` table.

## Summary
<a name="chap-sql-server-aurora-pg.tsql.storedprocedures.summary"></a>

The following table summarizes the differences between stored procedures in SQL Server and PostgreSQL.


| Feature | SQL Server |  Aurora PostgreSQL  | Workaround | 
| --- | --- | --- | --- | 
| General CREATE syntax differences |  <pre>CREATE PROC|PROCEDURE<br /><Procedure Name><br />@Parameter1 <Type>, ...n<br />AS<br /><Body></pre>  |  <pre>CREATE [ OR REPLACE] FUNCTION<br /><Function Name> (Parameter1 <Type>, ...n)<br />AS $$<br /><body></pre>  | Rewrite stored procedure creation scripts to use `FUNCTION` instead of `PROC` or `PROCEDURE`.<br />Rewrite stored procedure creation scripts to omit the `AS $$` pattern.<br />Rewrite stored procedure parameters to not use the `@` symbol in parameter names. Add parentheses around the parameter declaration. | 
| Security context |  <pre>{ EXEC | EXECUTE } AS<br />{ CALLER | SELF | OWNER<br />| 'user_name' }</pre>  |  <pre>SECURITY INVOKER | SECURITY DEFINER</pre>  | For stored procedures that use an explicit user name, rewrite the code from `EXECUTE AS user` to `SECURITY DEFINER` and recreate the functions with this user.<br />For stored procedures that use the `CALLER` option, rewrite the code to include `SECURITY INVOKER`.<br />For stored procedures that use the `SELF` option, rewrite the code to `SECURITY DEFINER`. | 
| Encryption | Use the `WITH ENCRYPTION` option. | Not supported in Aurora PostgreSQL. |  | 
| Parameter direction |  `IN` and `OUT\|OUTPUT`, by default `OUT` can be used as `IN` as well. |  `IN`, `OUT`, `INOUT`, or `VARIADIC`  | Although the functionality of these parameters is the same for SQL Server and PostgreSQL, rewrite the code for syntax compliance.<br />Use `OUT` instead of `OUTPUT`.<br />Use `INOUT` instead of `OUT` for bidirectional parameters. | 
| Recompile | Use the `WITH RECOMPILE` option. | Not supported in Aurora PostgreSQL. |  | 
| Table-valued parameters | Use declared table type user-defined parameters. | Use declared table type user-defined parameters. |  | 
| Additional restrictions | Use `BULK INSERT` to load data from text file. | Not supported in Aurora PostgreSQL. |  | 

For more information, see [CREATE FUNCTION](https://www.postgresql.org/docs/13/sql-createfunction.html), [PL/pgSQL — SQL Procedural Language](https://www.postgresql.org/docs/13/plpgsql.html), [Procedural Languages](https://www.postgresql.org/docs/13/xplang.html), and [Query Language (SQL) Functions](https://www.postgresql.org/docs/13/xfunc-sql.html) in the *PostgreSQL documentation*.