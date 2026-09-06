

# User-defined types for T-SQL
<a name="chap-sql-server-aurora-mysql.tsql.udt"></a>

This topic provides reference information about user-defined types and table-valued parameters in Microsoft SQL Server and their compatibility with Amazon Aurora MySQL. It explains the differences in feature support between SQL Server and Aurora MySQL, highlighting that Aurora MySQL does not currently support user-defined types or table-valued parameters.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  |  ![Three star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-automation-3.png)  |  [User-Defined Types](chap-sql-server-aurora-mysql.tools.actioncode.md#chap-sql-server-aurora-mysql.tools.actioncode.udt)  | Replace scalar UDT with base types. Rewrite stored procedures that use table-type input parameters to use strings with CSV, XML, or JSON, or to process row-by-row. For more information, see [Stored Procedures](chap-sql-server-aurora-mysql.tsql.storedprocedures.md). | 

## SQL Server Usage
<a name="chap-sql-server-aurora-mysql.tsql.udt.sqlserver"></a>

SQL Server user-defined types provide a mechanism for encapsulating custom data types and for adding NULL constraints.

SQL Server also supports table-valued user-defined types, which you can use to pass a set of values to a stored procedure.

User defined types can also be associated to CLR code assemblies. Beginning with SQL Server 2014, memory-optimized types support memory optimized tables and code.

**Note**  
If your code uses custom rules bound to data types, Microsoft recommends discontinuing use of this deprecated feature.

All user-defined types are based on an existing system data types. They allow developers to reuse the definition, making the code and schema more readable.

### Syntax
<a name="chap-sql-server-aurora-mysql.tsql.udt.sqlserver.syntax"></a>

The simplified syntax for the `CREATE TYPE` statement.

```
CREATE TYPE <type name> {
FROM <base type> [ NULL | NOT NULL ] | AS TABLE (<Table Definition>)}
```

### Examples
<a name="chap-sql-server-aurora-mysql.tsql.udt.sqlserver.examples"></a>

 **User-defined types** 

Create a `ZipCodeScalar` user-defined type.

```
CREATE TYPE ZipCode
FROM CHAR(5)
NOT NULL
```

Use the `ZipCodetype` in a table.

```
CREATE TABLE UserLocations
(UserID INT NOT NULL PRIMARY KEY, ZipCode ZipCode);
```

```
INSERT INTO [UserLocations] ([UserID],[ZipCode]) VALUES (1, '94324');
INSERT INTO [UserLocations] ([UserID],[ZipCode]) VALUES (2, NULL);
```

For the preceding example, the following error message appears. It indicates that NULL values for `ZipCodeare` aren’t allowed.

```
Msg 515, Level 16, State 2, Line 78
Cannot insert the value NULL into column 'ZipCode', table 'tempdb.dbo.UserLocations';
column doesn't allow nulls. INSERT fails.
The statement has been terminated.
```

 **Table-valued types** 

The following example demonstrates how to create and use a table valued types to pass a set of values to a stored procedure.

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

Create a table valued type for the `OrderItems` table.

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

Create the `InsertOrderItems` procedure. Note that the entire set of rows from the table valued parameter is handled with one statement.

```
CREATE PROCEDURE InsertOrderItems
@OrderItems AS OrderItems READONLY
AS
BEGIN
    INSERT INTO OrderItems(OrderID, Item, Quantity)
    SELECT OrderID,
        Item,
        Quantity
    FROM @OrderItems;
END
```

Instantiate the `OrderItems` type, insert the values, and pass it to a stored procedure.

```
DECLARE @OrderItems AS OrderItems;
```

```
INSERT INTO @OrderItems ([OrderID], [Item], [Quantity])
VALUES
(1, 'M8 Bolt', 100),
(1, 'M8 Nut', 100),
(1, M8 Washer, 200);

EXECUTE [InsertOrderItems] @OrderItems = @OrderItems;

(3 rows affected)
```

Select all rows from the `OrderItems` table.

```
SELECT * FROM OrderItems;

OrderID  Item       Quantity
1        M8 Bolt    100
1        M8 Nut     100
1        M8 Washer  200
```

For more information, see [CREATE TYPE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-type-transact-sql?view=sql-server-ver15) in the *SQL Server documentation*.

## MySQL Usage
<a name="chap-sql-server-aurora-mysql.tsql.udt.mysql"></a>

 Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) 5.7 doesn’t support user defined types and user defined table valued parameters.

The current documentation doesn’t indicate these features will be supported in Aurora MySQL version 8.

### Migration Considerations
<a name="chap-sql-server-aurora-mysql.tsql.udt.mysql.considerations"></a>

For scalar user-defined types, replace the type name with base type and optional NULL constraints.

For table-valued user-defined types used as stored procedure parameters, the workaround is more complicated.

Common solutions include using either temporary tables to hold the data or passing large string parameters containing the data in CSV, XML, JSON (or any other convenient format) and then writing code to parse these values in a stored procedure. Alternatively, if the logic doesn’t require access to the entire set of changes, and for small data sets, it is easier to call the stored procedure in a loop and pass the columns as standard parameters, row by row.

Memory-optimized engines aren’t yet supported in Aurora MySQL. You must convert memory optimized tables to disk based tables.

### Examples
<a name="chap-sql-server-aurora-mysql.tsql.udt.mysql.examples"></a>

 **Replacing a user-defined type** 

Replace the `ZipCode` user-defined type with a base type.

```
CREATE TABLE UserLocations
(
    UserID INT NOT NULL
    PRIMARY KEY,
    /*ZipCode*/ CHAR(5) NOT NULL
);
```

 **Replacing a table-valued stored procedure parameter** 

The following steps describe how to replace a table-valued parameter with a source table and a `LOOP` cursor.

Create an `OrderItems` table.

```
CREATE TABLE OrderItems
(
    OrderID INT NOT NULL,
    Item VARCHAR(20) NOT NULL,
    Quantity SMALLINT NOT NULL,
    PRIMARY KEY(OrderID, Item)
);
```

Create and populate the `SourceTable`.

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

Create a procedure to loop through the `SourceTable` and insert rows.

**Note**  
There are syntax differences from T-SQL for both the `CREATE PROCEDURE` and the `CURSOR` declaration and use. For more information, see [Stored Procedures](chap-sql-server-aurora-mysql.tsql.storedprocedures.md) and [Cursors](chap-sql-server-aurora-mysql.tsql.cursors.md).

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
        FOR NOT FOUND
        SET done = TRUE;
    OPEN ItemCursor;
    CursorStart: LOOP
    FETCH NEXT FROM ItemCursor
        INTO var_OrderID, var_Item, var_Quantity;
    IF Done
        THEN LEAVE CursorStart;
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
<a name="chap-sql-server-aurora-mysql.tsql.udt.summary"></a>


| SQL Server |  Aurora MySQL  | Comments | 
| --- | --- | --- | 
| Table-valued parameters | Not supported | Use either temporary tables, or CSV, XML, JSON string parameters and parse the data. Alternatively, rewrite the stored procedure to accept the data one row at a time and process the data in a loop. | 
| Memory-optimized table-valued user-defined types | Not supported | Not supported. | 

For more information, see [Cursors](https://dev.mysql.com/doc/refman/5.7/en/cursors.html) in the *MySQL documentation*.