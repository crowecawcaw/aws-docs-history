

# Cursors for T-SQL
<a name="chap-sql-server-aurora-mysql.tsql.cursors"></a>

This topic provides reference information about cursor compatibility between Microsoft SQL Server 2019 and Amazon Aurora MySQL. You can understand the differences in cursor support and functionality when migrating from SQL Server to Aurora MySQL.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  |  ![Three star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-automation-3.png)  |  [Cursors](chap-sql-server-aurora-mysql.tools.actioncode.md#chap-sql-server-aurora-mysql.tools.actioncode.cursors)  |  Aurora MySQL supports only static, forward only, read-only cursors. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-mysql.tsql.cursors.sqlserver"></a>

A *set* is a fundamental concept of the relation data model, from which SQL is derived. SQL is a declarative language that operates on whole sets, unlike most procedural languages that operate on individual data elements. A single invocation of a SQL statement can return a whole set or modify millions of rows.

Many developers are accustomed to using procedural or imperative approaches to develop solutions that are difficult to implement using set-based querying techniques. Also, operating on row data sequentially may be a more appropriate approach is certain situations.

Cursors provide an alternative mechanism for operating on result sets. Instead of receiving a table object containing rows of data, applications can use cursors to access the data sequentially, row-by-row. Cursors provide the following capabilities:
+ Positioning the cursor at specific rows of the result set using absolute or relative offsets.
+ Retrieving a row, or a block of rows, from the current cursor position.
+ Modifying data at the current cursor position.
+ Isolating data modifications by concurrent transactions that affect the cursor’s result.
+ T-SQL statements can use cursors in scripts, stored procedures, and triggers.

### Syntax
<a name="chap-sql-server-aurora-mysql.tsql.cursors.sqlserver.syntax"></a>

```
DECLARE <Cursor Name>
CURSOR [LOCAL | GLOBAL]
    [FORWARD_ONLY | SCROLL]
    [STATIC | KEYSET | DYNAMIC | FAST_FORWARD]
    [ READ_ONLY | SCROLL_LOCKS | OPTIMISTIC]
    [TYPE_WARNING]
    FOR <SELECT statement>
    [ FOR UPDATE [ OF <Column List>]][;]
```

```
FETCH [NEXT | PRIOR | FIRST | LAST | ABSOLUTE <Value> | RELATIVE <Value>]
FROM <Cursor Name> INTO <Variable List>;
```

### Examples
<a name="chap-sql-server-aurora-mysql.tsql.cursors.sqlserver.examples"></a>

The following example processes data in a cursor.

```
DECLARE MyCursor CURSOR FOR
    SELECT *
    FROM Table1 AS T1
        INNER JOIN
        Table2 AS T2
        ON T1.Col1 = T2.Col1;
    OPEN MyCursor;
    DECLARE @VarCursor1 VARCHAR(20);
    FETCH NEXT
        FROM MyCursor INTO @VarCursor1;

    WHILE @@FETCH_STATUS = 0
    BEGIN
        EXEC MyPRocessingProcedure
            @InputParameter = @VarCursor1;
        FETCH NEXT
            FROM product_cursor INTO @VarCursor1;
    END

    CLOSE MyCursor;
    DEALLOCATE MyCursor ;
```

For more information, see [SQL Server Cursors](https://docs.microsoft.com/en-us/sql/relational-databases/cursors?view=sql-server-ver15) and [Cursors (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/cursors-transact-sql?view=sql-server-ver15) in the *SQL Server documentation*.

## MySQL Usage
<a name="chap-sql-server-aurora-mysql.tsql.cursors.mysql"></a>

 Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) supports cursors only within stored routines, functions and stored procedures.

Unlike SQL Server, which offers an array of cursor types, Aurora MySQL cursors have the following characteristics:
+  **Asensitive** — The server can choose to either make a copy of its result table or to access the source data as the cursor progresses.
+  **Read-only** — Cursors aren’t updatable.
+  **Nonscrollable** — Cursors can only be traversed in one direction and can’t skip rows. The only supported cursor advance operation is `FETCH NEXT`.

In Aurora MySQL, cursor declarations appear before handler declarations and after variable and condition declarations.

Similar to SQL Server, you can declare cursors with the `DECLARE CURSOR` statement. To open a cursor, use the `OPEN` statement. To fetch a cursor, use the `FETCH` statement. You can close the cursor with the `CLOSE` statement.

**Note**  
 Aurora MySQL doesn’t have a `DEALLOCATE` statement because you don’t need it.

### DECLARE Cursor
<a name="chap-sql-server-aurora-mysql.tsql.cursors.mysql.declare"></a>

```
DECLARE <Cursor Name> CURSOR
FOR <Cursor SELECT Statement>
```

The `DECLARE CURSOR` statement instantiates a cursor object and associates it with a `SELECT` statement. This `SELECT` is then used to retrieve the cursor rows.

To fetch the rows, use the `FETCH` statement. As mentioned before, Aurora MySQL supports only `FETCH NEXT`. Make sure that the number of output variables specified in the `FETCH` statement matches the number of columns retrieved by the cursor.

 Aurora MySQL cursors have additional characteristics:
+  `SELECT INTO` isn’t allowed in a cursor.
+ Stored routing can have multiple cursor declarations, but every cursor declared in a given code block must have a unique name.
+ Cursors can be nested.

### OPEN Cursor
<a name="chap-sql-server-aurora-mysql.tsql.cursors.mysql.open"></a>

```
OPEN <Cursor Name>;
```

The `OPEN` command populates the cursor with the data, either dynamically or in a temporary table, and readies the first row for consumption by the `FETCH` statement.

### FETCH Cursor
<a name="chap-sql-server-aurora-mysql.tsql.cursors.mysql.fetch"></a>

```
FETCH [[NEXT] FROM] <Cursor Name>
INTO <Variable 1> [,<Variable n>]
```

The `FETCH` statement retrieves the current pointer row, assigns the column values to the variables listed in the `FETCH` statement, and advances the cursor pointer by one row. If the row isn’t available, meaning the cursor has been exhausted, Aurora MySQL raises a no data condition with the `SQLSTATE` value set to `0200000`.

To catch this condition, or the alternative `NOT FOUND` condition, create a condition handler. For more information, see [Error Handling](chap-sql-server-aurora-mysql.tsql.errorhandling.md).

**Note**  
Carefully plan your error handling flow. The same condition might be raised by other `SELECT` statements or other cursors than the one you intended. Place operations within `BEGIN-END` blocks to associate each cursor with its own handler.

### CLOSE Cursor
<a name="chap-sql-server-aurora-mysql.tsql.cursors.mysql.close"></a>

```
CLOSE <Cursor Name>;
```

The `CLOSE` statement closes an open cursor. If the cursor with the specified name doesn’t exist, Aurora MySQL raises an error. If a cursor isn’t explicitly closed, Aurora MySQL closes it automatically at the end of the `BEGIN …​ END` block in which it was declared.

### Migration Considerations
<a name="chap-sql-server-aurora-mysql.tsql.cursors.mysql.considerations"></a>

The Aurora MySQL Cursors framework is much simpler than SQL Server and provides only the basic types. If your code relies on advanced cursor features, these will need to be rewritten.

However, most applications use forward only, read only cursors, and those will be easy to migrate.

If your application uses cursors in ad-hoc batches, move the code to a stored procedure or a function.

### Examples
<a name="chap-sql-server-aurora-mysql.tsql.cursors.mysql.examples"></a>

The following examples use a cursor to iterate over source rows and merges into the `OrderItems` table.

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

Create and populate the `SourceTable` table.

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

Create a procedure to loop through `SourceTable` and insert rows.

**Note**  
There are syntax differences between T-SQL for the `CREATE PROCEDURE` and the `CURSOR` declaration. For more information, see [Stored Procedures](chap-sql-server-aurora-mysql.tsql.storedprocedures.md).

```
CREATE PROCEDURE LoopItems()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE var_OrderID INT;
    DECLARE var_Item VARCHAR(20);
    DECLARE var_Quantity SMALLINT;
    DECLARE ItemCursor CURSOR
    FOR
        SELECT OrderID,
            Item,
            Quantity
        FROM SourceTable;
    DECLARE CONTINUE HANDLER
        FOR NOT FOUND
        SET done = TRUE;
    OPEN ItemCursor;
    CursorStart: LOOP
    FETCH NEXT
        FROM ItemCursor
        INTO var_OrderID,
            var_Item,
            var_Quantity;
    IF Done
        THEN LEAVE CursorStart;
    END IF;
        INSERT INTO OrderItems (OrderID, Item, Quantity)
        VALUES (var_OrderID, var_Item, var_Quantity);
    END LOOP;
    CLOSE ItemCursor;
END;
```

Run the stored procedure.

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
<a name="chap-sql-server-aurora-mysql.tsql.cursors.summary"></a>


| Feature | SQL Server |  Aurora MySQL  | Comments | 
| --- | --- | --- | --- | 
| Cursor options |  `[FORWARD_ONLY \| SCROLL]` <br /> `[STATIC \| KEYSET \| DYNAMIC \| FAST_FORWARD]` <br /> `[READ_ONLY \| SCROLL_LOCKS \| OPTIMISTIC]`  |  |  | 
| Updateable cursors |  `DECLARE CURSOR…​ FOR UPDATE`  | Not supported |  | 
| Declaration |  `DECLARE CURSOR`  |  `DECLARE CURSOR`  | No options for `DECLARE CURSOR` in Aurora MySQL. | 
| Open | OPEN | OPEN |  | 
| Fetch |  `FETCH NEXT \| PRIOR \| FIRST \| LAST \| ABSOLUTE \| RELATIVE`  |  `FETCH NEXT`  |  | 
| Close | CLOSE | CLOSE |  | 
| Deallocate | DEALLOCATE | N/A | Not required because the `CLOSE` statement deallocates the cursor | 
| Cursor end condition |  `@@FETCH_STATUS` system variable | Event Handler | Event handlers aren’t specific to a cursor. For more information, see [Error Handling](chap-sql-server-aurora-mysql.tsql.errorhandling.md). | 

For more information, see [Cursors](https://dev.mysql.com/doc/refman/5.7/en/cursors.html) in the *MySQL documentation*.