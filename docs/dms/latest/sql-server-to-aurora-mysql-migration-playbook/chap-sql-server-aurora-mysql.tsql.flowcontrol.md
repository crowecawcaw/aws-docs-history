

# Flow control for T-SQL
<a name="chap-sql-server-aurora-mysql.tsql.flowcontrol"></a>

This topic provides reference information about flow control in SQL Server and Amazon Aurora MySQL, comparing their respective capabilities and syntax differences. You can use this guide to understand how to adapt your existing SQL Server flow control statements when migrating to Aurora MySQL.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Four star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-compatibility-4.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-automation-4.png)  |  [Flow Control](chap-sql-server-aurora-mysql.tools.actioncode.md#chap-sql-server-aurora-mysql.tools.actioncode.flowcontrol)  | Syntax and option differences, similar functionality. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-mysql.tsql.flowcontrol.sqlserver"></a>

Although SQL is a mostly declarative language, it does support flow control commands, which provide run time dynamic changes in script run paths.

**Note**  
Before SQL/PSM was introduced in SQL:1999, the ANSI standard did not include flow control constructs. Therefore, there are significant syntax differences among RDBMS engines.

SQL Server provides the following flow control keywords.
+  `BEGIN…​ END` — Define boundaries for a block of commands that run together.
+  `RETURN` — Exit a server code module such as stored procedure, function, and so on and return control to the calling scope. You can use `RETURN <value>` to return an `INT` value to the calling scope.
+  `BREAK` — Exit `WHILE` loop run.
+  `THROW` — Raise errors and potentially return control to the calling stack.
+  `CONTINUE` — Restart a `WHILE` loop.
+  `TRY…​ CATCH` — Error handling. For more information, see [Error Handling](chap-sql-server-aurora-mysql.tsql.errorhandling.md).
+  `GOTO label` — Moves the run point to the location of the specified label.
+  `WAITFOR` — Delay.
+  `IF…​ ELSE` — Conditional flow control.
+  `WHILE <condition>` — Continue looping while `<condition>` returns `TRUE`.
**Note**  
 `WHILE` loops are commonly used with cursors and use the system variable `@@FETCH_STATUS` to determine when to exit. For more information, see [Cursors](chap-sql-server-aurora-mysql.tsql.cursors.md).

For more information, see [Error Handling](chap-sql-server-aurora-mysql.tsql.errorhandling.md).

### Examples
<a name="chap-sql-server-aurora-mysql.tsql.flowcontrol.sqlserver.examples"></a>

Create and populate the `OrderItems` table.

```
CREATE TABLE OrderItems
(
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
(3, 'M8 Washer', 200);
```

 **WAITFOR** 

Use `WAITFOR` to introduce a one minute delay between background batches purging old data.

```
SET ROWCOUNT 1000;
WHILE @@ROWCOUNT > 0;
BEGIN;
    DELETE FROM OrderItems
    WHERE OrderDate < '19900101';
    WAITFOR DELAY '00:01:00';
END;
```

 **GOTO** 

Use `GOTO` to skip a code section based on an input parameter in a stored procedure.

```
CREATE PROCEDURE ProcessOrderItems
@OrderID INT, @Item VARCHAR(20), @Quantity INT, @UpdateInventory BIT
AS
BEGIN
        INSERT INTO OrderItems (OrderID, Item, Quantity)
        SELECT @OrderID, @item, @Quantity
    IF @UpdateInventory = 0
        GOTO Finish
    UPDATE Inventory
    SET Stock = Stock - @Quantity
    WHERE Item = @Item
    /* Additional Inventory Processing */
finish:
/* Generate Results Log*/
END
```

 **Dynamic Procedure Run Path** 

The following example demonstrates a solution for running different processes based on the number of items in an order.

Declare a cursor for looping through all OrderItems and calculating the total quantity for each order.

```
DECLARE OrderItemCursor CURSOR FAST_FORWARD
FOR
SELECT OrderID,
    SUM(Quantity) AS NumItems
FROM OrderItems
GROUP BY OrderID
ORDER BY OrderID;
DECLARE @OrderID INT, @NumItems INT;

-- Instantiate the cursor and loop through all orders.
OPEN OrderItemCursor;

FETCH NEXT FROM OrderItemCursor
INTO @OrderID, @NumItems

WHILE @@Fetch_Status = 0
BEGIN;

IF @NumItems > 100
    PRINT 'EXECUTING LogLargeOrder - '
    + CAST(@OrderID AS VARCHAR(5))
    + ' ' + CAST(@NumItems AS VARCHAR(5));
ELSE
    PRINT 'EXECUTING LogSmallOrder - '
    + CAST(@OrderID AS VARCHAR(5))
    + ' ' + CAST(@NumItems AS VARCHAR(5));

FETCH NEXT FROM OrderItemCursor
INTO @OrderID, @NumItems;
END;

-- Close and deallocate the cursor.
CLOSE OrderItemCursor;
DEALLOCATE OrderItemCursor;
```

For the preceding example, the result looks as shown following.

```
EXECUTING LogSmallOrder - 1 100
EXECUTING LogSmallOrder - 2 100
EXECUTING LogLargeOrder - 3 200
```

For more information, see [Control-of-Flow](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/control-of-flow?view=sql-server-ver15) in the *SQL Server documentation*.

## MySQL Usage
<a name="chap-sql-server-aurora-mysql.tsql.flowcontrol.mysql"></a>

 Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) provides the following flow control constructs:
+  `BEGIN…​ END` — Define boundaries for a block of commands that are ran together.
+  `CASE` — Run a set of commands based on a predicate (not to be confused with `CASE` expressions).
+  `IF…​ ELSE` — Conditional flow control.
+  `ITERATE` — Restart a `LOOP`, `REPEAT`, and `WHILE` statement.
+  `LEAVE` — Exit a server code module such as stored procedure, function, and so on, and return control to the calling scope.
+  `LOOP` — Loop indefinitely.
+  `REPEAT…​ UNTIL` — Loop until the predicate is true.
+  `RETURN` — Terminate the run of the current scope and return to the calling scope.
+  `WHILE` — Continue looping while the condition returns `TRUE`.
+  `SLEEP` — Pause the run for a specified number of seconds.

### Examples
<a name="chap-sql-server-aurora-mysql.tsql.flowcontrol.mysql.examples"></a>

Create and populate the `OrderItems` table.

```
CREATE TABLE OrderItems
(
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
(3, 'M8 Washer', 200);
```

Rewrite of SQL Server `WAITFOR` delay using `SLEEP`.

```
CREATE PROCEDURE P()
BEGIN
    DECLARE RR INT;
    SET RR = (
        SELECT COUNT(*)
        FROM OrderItems
        WHERE OrderDate < '19900101'
        );
    WHILE RR > 0 DO
    DELETE FROM OrderItems
    WHERE OrderDate < '19900101';
        DO SLEEP (60);
    SET RR = (
        SELECT COUNT(*)
        FROM OrderItems
        WHERE OrderDate < '19900101'
        );
    END WHILE;
END;
```

Rewrite of SQL Server `GOTO` using nested blocks.

```
CREATE PROCEDURE ProcessOrderItems
(Var_OrderID INT, Var_Item VARCHAR(20), Var_Quantity INT, UpdateInventory BIT)
BEGIN
        INSERT INTO OrderItems (OrderID, Item, Quantity)
        VALUES(Var_OrderID, Var_Item, Var_Quantity)
    IF @UpdateInventory = 1
    BEGIN
        UPDATE Inventory
        SET Stock = Stock - @Quantity
        WHERE Item = @Item
        /* Additional Inventory Processing...*/
    END
/* Generate Results Log */
END
```

 **Dynamic Procedure Run Path** 

The following example demonstrates a solution for running different processes based on the number of items in an order.

This example provides the same functionality as the example for SQL Server flow control. However, unlike the SQL Server example which you run as a batch script, Aurora MySQL variables can only be used in stored routines such as procedures and functions.

Create a procedure to declare a cursor and loop through the order items.

```
CREATE PROCEDURE P()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE var_OrderID INT;
    DECLARE var_NumItems INT;

    DECLARE OrderItemCursor CURSOR FOR
    SELECT OrderID,
        SUM(Quantity) AS NumItems
    FROM OrderItems
    GROUP BY OrderID
    ORDER BY OrderID;

    DECLARE CONTINUE HANDLER
    FOR NOT FOUND SET done = TRUE;

    OPEN OrderItemCursor;

    CursorStart: LOOP
    FETCH NEXT FROM OrderItemCursor
        INTO var_OrderID, var_NumItems;
    IF done
        THEN LEAVE CursorStart;
    END IF;
    IF var_NumItems > 100
        THEN SELECT CONCAT('EXECUTING LogLargeOrder - ', CAST(var_OrderID AS VARCHAR(5)),' Num Items: ', CAST(var_ NumItems AS VARCHAR(5)))
    ELSE SELECT CONCAT('EXECUTING LogSmallOrder - ', CAST(var_OrderID AS VARCHAR(5)),     ' Num Items: ', CAST(var_NumItems AS VARCHAR(5)))
    END IF;
END LOOP;

CLOSE OrderItemCursor;

END;
```

## Summary
<a name="chap-sql-server-aurora-mysql.tsql.flowcontrol.summary"></a>

While there are some syntax differences between SQL Server and Aurora MySQL flow control statements, most rewrites should be straightforward. The following table summarizes the differences and identifies how to modify T-SQL code to support similar functionality in Aurora MySQL.


| Feature | SQL Server |  Aurora MySQL  | Workaround | 
| --- | --- | --- | --- | 
|  `BEGIN…​ END`  | Define command block boundaries. | Define command block boundaries. | Compatible. | 
|  `RETURN`  | Exit the current scope and return to caller.<br />Supported for both scripts and stored code such as procedures and functions. | Exit a stored function and return to caller. | For Aurora MySQL, `RETURN` is valid only in stored or user-defined functions. It isn’t used in stored procedures, triggers, or events.<br />Rewrite the T-SQL code using the `LEAVE` keyword.<br />The `RETURN` statement can return a value in both products. However, `LEAVE` doesn’t support return parameters. Rewrite the code to use output parameters.<br />You can’t `RETURN` in Aurora MySQL for scripts that aren’t part of a stored routine. | 
|  `BREAK`  | Exit the `WHILE` loop run. | Not supported. | Rewrite the logic to explicitly set a value that will render the `WHILE` condition `FALSE`. For example, `WHILE a<100 AND control = 1`. Explicitly `SET control = 0`, and use `ITERATE` to return to the beginning of the loop. | 
|  `THROW`  | Raise errors and potentially return control to the calling stack. | Errors are handled by `HANDLER` objects. | For more information, see [Error Handling](chap-sql-server-aurora-mysql.tsql.errorhandling.md). | 
|  `TRY - CATCH`  | Error handling | Errors are handled by `HANDLER` objects. | For more information, see [Error Handling](chap-sql-server-aurora-mysql.tsql.errorhandling.md). | 
|  `GOTO`  | Move run to specified label. | Not supported. | Consider rewriting the flow logic using either `CASE` statements or nested stored procedures. You can use nested stored procedures to circumvent this limitation by separating code sections and encapsulating them in sub-procedures. Use `IF <condition> CALL <stored procedure>` in place of `GOTO`. | 
|  `WAITFOR`  | Delay. | Not supported. | Replace `WAITFOR` with Aurora MySQL `SLEEP`. `SLEEP` is less flexible than `WAITFOR` and only supports delays specified in seconds. Rewrite the code using `SLEEP` to replace `WAITFOR DELAY` and convert the units to seconds.<br /> `WAITFOR TIME` isn’t supported in Aurora MySQL. You can calculate the difference in seconds between the desired time and current time using date and rime functions and use the result to dynamically generate the `SLEEP` statement. Alternatively, consider using `CREATE EVENT` with a predefined schedule. | 
|  `IF…​ ELSE`  | Conditional flow control. | Conditional flow control. | The functionality is compatible, but the syntax differs. SQL Server uses `IF <condition> <statement> ELSE <statement>`. Aurora MySQL uses `IF <condition> THEN <statement> ELSE <statement> ENDIF`.<br />Rewrite T-SQL code to add the mandatory `THEN` and `ENDIF` keywords. | 
|  `WHILE`  | Continue running while condition is `TRUE`. | Continue running while condition is `TRUE`. | The functionality is compatible, but the syntax differs. SQL Server uses `WHILE <condition> BEGIN…​END`, Aurora MySQL uses `WHILE <condition> DO…​ END WHILE`. Aurora MySQL doesn’t require a `BEGIN…​END` block.<br />Rewrite T-SQL code to use the Aurora MySQL keywords. | 

For more information, see [Flow Control Statements](https://dev.mysql.com/doc/refman/5.7/en/flow-control-statements.html) in the *MySQL documentation*.