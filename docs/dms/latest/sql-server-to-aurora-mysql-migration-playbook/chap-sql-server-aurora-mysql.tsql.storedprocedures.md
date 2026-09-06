

# Stored procedures for T-SQL
<a name="chap-sql-server-aurora-mysql.tsql.storedprocedures"></a>

This topic provides reference content comparing stored procedures in Microsoft SQL Server 2019 and Amazon Aurora MySQL. You can understand the key differences and similarities between these two database systems' implementations of stored procedures.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-automation-4.png)  |  [Stored Procedures](chap-sql-server-aurora-mysql.tools.actioncode.md#chap-sql-server-aurora-mysql.tools.actioncode.storedprocedures)  | No support for table-valued parameters. Syntax and option differences. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-mysql.tsql.storedprocedures.sqlserver"></a>

Stored procedures are encapsulated, persisted code modules you can run using the `EXECUTE` T-SQL statement. They may have multiple input and output parameters. Table-valued user-defined types can be used as input parameters. IN is the default direction for parameters, but `OUT` must be explicitly specified. You can specify parameters as both `IN` and `OUT`.

In SQL Server, you can run stored procedures in any security context using the `EXECUTE AS` option. They can be explicitly recompiled for every run using the RECOMPILE option and can be encrypted in the database using the `ENCRYPTION` option to prevent unauthorized access to the source code.

SQL Server provides a unique feature that allows you to use a stored procedure as an input to an `INSERT` statement. When you use this feature, only the first row in the data set returned by the stored procedure is evaluated.

As part of the stored procedure syntax, SQL Server supports a default output integer parameter that can be specified along with the `RETURN` command, for example, `RETURN -1`. It’s typically used to signal status or error to the calling scope, which can use the syntax `EXEC @Parameter = <Stored Procedure Name>` to retrieve the `RETURN` value, without explicitly stating it as part of the parameter list.

### Syntax
<a name="chap-sql-server-aurora-mysql.tsql.storedprocedures.sqlserver.syntax"></a>

```
CREATE [ OR ALTER ] { PROC | PROCEDURE } <Procedure Name>
[<Parameter List>
[ WITH [ ENCRYPTION ]|[ RECOMPILE ]|[ EXECUTE AS ...]]
AS {
[ BEGIN ]
<SQL Code Body>
[RETURN [<Integer Value>]]
[ END ] }[;]
```

### Creating and Running a Stored Procedure
<a name="chap-sql-server-aurora-mysql.tsql.storedprocedures.sqlserver.create"></a>

Create a simple parameterized stored procedure to validate the basic format of an email.

```
CREATE PROCEDURE ValidateEmail
@Email VARCHAR(128), @IsValid BIT = 0 OUT
AS
BEGIN
IF @Email LIKE N'%@%'
    SET @IsValid = 1
ELSE
    SET @IsValid = 0
RETURN
END;
```

Run the procedure.

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

Create a stored procedure that uses `RETURN` to pass the application an error value.

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

### Using a Table-Valued Input Parameter
<a name="chap-sql-server-aurora-mysql.tsql.storedprocedures.sqlserver.tablevalued"></a>

Create and populate the `OrderItems` table.

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

Create a table-valued type for the `OrderItem` table-valued parameter.

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

Create a procedure to process order items.

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

Instantiate and populate the table valued variable and pass the data set to the stored procedure.

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
<a name="chap-sql-server-aurora-mysql.tsql.storedprocedures.sqlserver.insert"></a>

```
INSERT INTO <MyTable>
EXECUTE <MyStoredProcedure>;
```

For more information, see [CREATE PROCEDURE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-procedure-transact-sql?view=sql-server-ver15) in the *SQL Server documentation*.

## MySQL Usage
<a name="chap-sql-server-aurora-mysql.tsql.storedprocedures.mysql"></a>

 Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) stored procedures provide similar functionality to SQL Server stored procedures.

As with SQL Server, Aurora MySQL supports security run context. It also supports input, output, and bi-directional parameters.

Stored procedures are typically used for: \* **Code reuse** — Stored procedures offer a convenient code encapsulation and reuse mechanism for multiple applications, potentially written in various languages, requiring the same database operations. \* **Security management** — By allowing access to base tables only through stored procedures, administrators can manage auditing and access permissions. This approach minimizes dependencies between application code and database code. Administrators can use stored procedures to process business rules and to perform auditing and logging. \* **Performance improvements** — Full SQL query text doesn’t need to be transferred from the client to the database.

Stored procedures, triggers, and user-defined functions in Aurora MySQL are collectively referred to as *stored routines*. When binary logging is enabled, MySQL `SUPER` privilege is required to run stored routines. However, you can run stored routines with binary logging enabled without `SUPER` privilege by setting `thelog_bin_trust_function_creators` parameter to true for the DB parameter group for your MySQL instance.

 Aurora MySQL permits stored routines to contain control flow, DML, DDL, and transaction management statements including `START TRANSACTION`, `COMMIT`, and `ROLLBACK`.

### Syntax
<a name="chap-sql-server-aurora-mysql.tsql.storedprocedures.mysql.syntax"></a>

```
CREATE [DEFINER = { user | CURRENT_USER }] PROCEDURE sp_name
([ IN | OUT | INOUT ] <Parameter> <Parameter Data Type> ... )
COMMENT 'string' |
LANGUAGE SQL |
[NOT] DETERMINISTIC |
{ CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA } |
SQL SECURITY { DEFINER | INVOKER }
<Stored Procedure Code Body>
```

### Examples
<a name="chap-sql-server-aurora-mysql.tsql.storedprocedures.mysql.examples"></a>

Replace RETURN value parameter with standard OUTPUT parameters.

```
CREATE PROCEDURE ProcessImportBatch()
IN @BatchID INT, OUT @ErrorNumber INT
BEGIN
    CALL Step1 (@BatchID)
    CALL Step2 (@BatchID)
    CALL Step3 (@BatchID)
IF error_count > 1
    SET @ErrorNumber = -1 -- indicate special condition
END
```

Use a `LOOP` cursor with a source table to replace table valued parameters.

Create the `OrderItems` table.

```
CREATE TABLE OrderItems
(
    OrderID INT NOT NULL,
    Item VARCHAR(20) NOT NULL,
    Quantity SMALLINT NOT NULL,
    PRIMARY KEY(OrderID, Item)
);
```

Create and populate `SourceTable` as a temporary data store for incoming rows.

```
CREATE TABLE SourceTable
(
    OrderID INT,
    Item VARCHAR(20),
    Quantity SMALLINT,
    PRIMARY KEY (OrderID, Item)
);
```

```
INSERT INTO SourceTable (OrderID, Item, Quantity)
VALUES
(1, 'M8 Bolt', 100),
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
    DECLARE ItemCursor CURSOR
        FOR SELECT OrderID,
            Item,
            Quantity
        FROM SourceTable;
    DECLARE CONTINUE HANDLER
        FOR NOT FOUND SET done = TRUE;
    OPEN ItemCursor;
    CursorStart: LOOP
    FETCH NEXT FROM ItemCursor
        INTO var_OrderID, var_Item, var_Quantity;
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

Select all rows from the OrderItems table.

```
SELECT * FROM OrderItems;
```

For the preceding example, the result looks as shown following.

```
OrderID  Item       Quantity
1        M8 Bolt    100
2        M8 Nut     100
3        M8 Washer  200
```

## Summary
<a name="chap-sql-server-aurora-mysql.tsql.storedprocedures.summary"></a>

The following table summarizes the differences between MySQL Stored Procedures and SQL Server Stored Procedures.


| Feature | SQL Server |  Aurora MySQL  | Workaround | 
| --- | --- | --- | --- | 
| General `CREATE` syntax differences |  <pre>CREATE PROC|PROCEDURE<br /><Procedure Name><br />@Parameter1 <Type>,<br />...n<br />AS<br /><Body></pre>  |  <pre>CREATE PROCEDURE<br /><Procedure Name><br />(Parameter1<br /><Type>,...n)<br /><Body></pre>  | Rewrite stored procedure creation scripts to use `PROCEDURE` instead of `PROC`.<br />Rewrite stored procedure creation scripts to omit the `AS` keyword.<br />Rewrite stored procedure parameters to not use the `@` symbol in parameter names. Add parentheses around the parameter declaration.<br />Rewrite stored procedure parameter direction `OUTPUT` to `OUT` or `INOUT` for bidirectional parameters. `IN` is the parameter direction for both MySQL and SQL Server. | 
| Security context |  <pre>{ EXEC | EXECUTE } AS<br />{ CALLER | SELF | OWNER |<br />'user_name' }</pre>  | <pre>DEFINER = 'user' |<br />CURRENT_USER</pre>in conjunction with<pre>SQL SECURITY {<br />DEFINER | INVOKER }</pre> | For stored procedures that use an explicit user name, rewrite the code from `EXECUTE AS 'user'` to `DEFINER = 'user'` and `SQL SECURITY DEFINER`.<br />For stored procedures that use the `CALLER` option, rewrite the code to include `SQL SECURITY INVOKER`.<br />For stored procedures that use the `SELF` option, rewrite the code to `DEFINER = CURRENT_USER` and `SQL SECURITY DEFINER`.<br />Unlike SQL Server, `OWNER`s can’t be specified and must be explicitly named. | 
| Encryption | Use the `WITH ENCRYPTION` option. | Not supported in Aurora MySQL. |  | 
| Parameter direction |  `IN` and `OUT\|OUTPUT`, by default `OUT` can be used as `IN` as well. |  `IN`, `OUT`, and `INOUT`  | Although the functionality of these parameters is the same for SQL Server and MySQL, make sure that you rewrite the code for syntax compliance.<br />Use `OUT` instead of `OUTPUT`.<br />Use `INOUT` instead of `OUT` for bidirectional parameters. | 
| Recompile | Use the `WITH RECOMPILE` option. | Not supported in Aurora MySQL. |  | 
| Table-valued parameters | Use declared table type user-defined parameters. | Not supported in Aurora MySQL. | See the preceding example for a workaround. | 
|  `INSERT…​ EXEC`  | Use the output of the stored procedure as input to an `INSERT` statement. | Not supported in Aurora MySQL. | Use tables to hold the data or pass string parameters formatted as CSV, XML, JSON (or any other convenient format) and then parse the parameters before the `INSERT` statement. | 
| Additional restrictions | Use `BULK INSERT` to load data from text file. | The LOAD DATA statement isn’t allowed in stored procedures. |  | 
|  `RETURN` value |  `RETURN <Integer Value>`  | Not supported. | Use a standard `OUTPUT` parameter instead. | 

For more information, see [Stored Procedures and Functions](https://dev.mysql.com/doc/refman/5.7/en/faqs-stored-procs.html) and [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html) in the *MySQL documentation*.