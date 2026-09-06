

# Flow control for T-SQL
<a name="chap-sql-server-aurora-pg.tsql.flowcontrol"></a>

This topic provides reference information comparing flow control constructs between Microsoft SQL Server and Amazon Aurora PostgreSQL. You can use this information to understand the similarities and differences in flow control mechanisms when migrating from SQL Server to Aurora PostgreSQL. The topic outlines various flow control commands available in both systems, highlighting where direct equivalents exist and suggesting alternatives where they don’t.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Four star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-compatibility-4.png)  |  ![Three star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-automation-3.png)  |  [Flow Control](chap-sql-server-aurora-pg.tools.actioncode.md#chap-sql-server-aurora-pg.tools.actioncode.flowcontrol)  | PostgreSQL doesn’t support `GOTO` and `WAITFOR TIME`. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-pg.tsql.flowcontrol.sqlserver"></a>

Although SQL Server is a mostly declarative language, it does support flow control commands, which provide run time dynamic changes in script run paths.

Before SQL/PSM was introduced in SQL:1999, the ANSI standard didn’t include flow control constructs. Therefore, there are significant syntax differences among RDBMS engines.

SQL Server provides the following flow control keywords.
+  `BEGIN…​ END` — Define boundaries for a block of commands that are run together.
+  `RETURN` — Exit a server code module (stored procedure, function, and so on) and return control to the calling scope. You can use `RETURN <value>` to return an `INT` value to the calling scope.
+  `BREAK` — Exit `WHILE` loop run.
+  `THROW` — Raise errors and potentially return control to the calling stack.
+  `CONTINUE` — Restart a `WHILE` loop.
+  `TRY…​ CATCH` — Error handling. For more information, see [Error Handling](chap-sql-server-aurora-pg.tsql.errorhandling.md).
+  `GOTO label` — Moves the run point to the location of the specified label.
+  `WAITFOR` — Delay.
+  `IF…​ ELSE` — Conditional flow control.
+  `WHILE <condition>` — Continue looping while <condition> returns TRUE.

**Note**  
WHILE loops are commonly used with cursors and use the system variable `@@FETCH_STATUS` to determine when to exit. For more information, see [Cursors](chap-sql-server-aurora-pg.tsql.cursors.md).

### Examples
<a name="chap-sql-server-aurora-pg.tsql.flowcontrol.sqlserver.examples"></a>

The following example demonstrates a solution for running different processes based on the number of items in an order.

Create and populate an OrderItems table.

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

For more information, see [Control-of-Flow](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/control-of-flow?view=sql-serverver15) in the *SQL Server documentation*.

## PostgreSQL Usage
<a name="chap-sql-server-aurora-pg.tsql.flowcontrol.pg"></a>

 Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) provides the following flow control constructs:
+  `BEGIN…​ END` — Define boundaries for a block of commands that are run together.
+  `CASE` — Run a set of commands based on a predicate (not to be confused with CASE expressions).
+  `IF…​ ELSE` — Perform conditional flow control.
+  `ITERATE` — Restart a `LOOP` or `WHILE` statement.
+  `LEAVE` — Exit a server code module such as stored procedure, function, and so on and return control to the calling scope.
+  `LOOP` — Loop indefinitely.
+  `REPEAT…​ UNTIL` — Loop until the predicate is true.
+  `RETURN` — Terminate the run of the current scope and return to the calling scope.
+  `WHILE` — Continue looping while the condition returns TRUE.

### Examples
<a name="chap-sql-server-aurora-pg.tsql.flowcontrol.pg.examples"></a>

The following example demonstrates a solution for running different logic based on the number of items in an order. It provides the same functionality as the example for SQL Server flow control. However, unlike the SQL Server example ran as a batch script, Aurora PostgreSQL variables can only be used in stored routines such as procedures and functions.

Create and populate an OrderItems table.

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

Create a procedure to declare a cursor and loop through the order items.

```
CREATE OR REPLACE FUNCTION P()
  RETURNS numeric
  LANGUAGE plpgsql
AS $function$
DECLARE
  done int default false;
  var_OrderID int;
  var_NumItems int;
  OrderItemCursor CURSOR FOR SELECT OrderID, SUM(Quantity) AS NumItems
  FROM OrderItems
  GROUP BY OrderID
  ORDER BY OrderID;

  BEGIN
    OPEN OrderItemCursor;
    LOOP
      fetch from OrderItemCursor INTO var_OrderID, var_NumItems;
    EXIT WHEN NOT FOUND;
    IF var_NumItems > 100 THEN
      RAISE NOTICE 'EXECUTING LogLargeOrder - %s',var_OrderID;
      RAISE NOTICE 'Num Items: %s', var_NumItems;
    ELSE
      RAISE NOTICE 'EXECUTING LogSmallOrder - %s',var_OrderID;
      RAISE NOTICE 'Num Items: %s', var_NumItems;
    END IF;
    END LOOP;
done = TRUE;
CLOSE OrderItemCursor;
END; $function$
```

## Summary
<a name="chap-sql-server-aurora-pg.tsql.flowcontrol.summary"></a>

While there are some syntax differences between SQL Server and Aurora PostgreSQL flow control statements, most rewrites should be straightforward. The following table summarizes the differences and identifies how to modify T-SQL code to support similar functionality in Aurora PostgreSQL PL/pgSQL.


| Command | SQL Server |  Aurora PostgreSQL  | 
| --- | --- | --- | 
|  `BEGIN…​END`  | Define command block boundaries. | Define command block boundaries. | 
|  `RETURN`  | Exit the current scope and return to caller. Supported for both scripts and stored code such as procedures and functions. | Exit a stored function and return to caller. | 
|  `BREAK`  | Exit `WHILE` loop run |  `EXIT WHEN`  | 
|  `THROW`  | Raise errors and potentially return control to the calling stack. | Raise errors and potentially return control to the calling stack. | 
|  `TRY…​CATCH`  | Error handling. | Error handling. For more information, see [Error Handling](chap-sql-server-aurora-pg.tsql.errorhandling.md). | 
|  `GOTO`  | Move run to a specified label | Consider rewriting the flow logic using either `CASE` statements or nested stored procedures. You can use nested stored procedures to circumvent this limitation by separating code sections and encapsulating them in sub-procedures. Use `IF <condition> EXEC <stored procedure>` instead of `GOTO`. | 
|  `WAITFOR`  | Delay |  `pg_sleep`. For more information, see [Date/Time Functions and Operators](https://www.postgresql.org/docs/13/static/functions-datetime.html) in the *PostgreSQL documentation*. | 
|  `IF…​ ELSE`  | Conditional flow control. | Conditional flow control. | 
|  `WHILE`  | Continue running while condition is true. | Continue running while condition is true. | 

For more information, see [Control Structures](https://www.postgresql.org/docs/13/plpgsql-control-structures.html) in the *PostgreSQL documentation*.