# Window functions for ANSI SQL

This topic provides reference information about window functions in Microsoft SQL Server and their compatibility with Amazon Aurora MySQL. You can understand the differences in support for window functions between SQL Server and Aurora MySQL, which is crucial for planning database migrations.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                                                     | Key differences                                         |
| ------------------------------ | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Two star feature compatibility | No automation                      | [Window Functions](chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.windowfunctions "chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.windowfunctions") | Rewrite window functions to use alternative SQL syntax. |

## SQL Server Usage

Window functions use an `OVER` clause to define the window and frame for a data set to be processed. They are part of the ANSI standard and are typically compatible among various SQL dialects. However, most database engines don’t yet support the full ANSI specification.

Window functions are a relatively new, advanced, and efficient T-SQL programming tool. They are highly utilized by developers to solve numerous programming challenges.

SQL Server currently supports the following window functions:

| Window function category | Examples                                                                                                                                               |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Ranking functions        | `ROW_NUMBER`, `RANK`, `DENSE_RANK`, and `NTILE`                                                                                                        |
| Aggregate functions      | `AVG`, `MIN`, `MAX`, `SUM`, `COUNT`, `COUNT_BIG`, `VAR`, `STDEV`, `STDEVP`, `STRING_AGG`, `GROUPING`, `GROUPING_ID`, `VAR`, `VARP`, and `CHECKSUM_AGG` |
| Analytic functions       | `LAG`, `LEAD`, `FIRST_Value`, `LAST_VALUE`, `PERCENT_RANK`, `PERCENTILE_CONT`, `PERCENTILE_DISC`, and `CUME_DIST`                                      |
| Other functions          | `NEXT_VALUE_FOR`. For more information, see [Identity and Sequences](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").     |

### Syntax

```
<Function()>
OVER
(
[ <PARTITION BY clause> ]
[ <ORDER BY clause> ]
[ <ROW or RANGE clause> ]
)
```

### Examples

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
(3, 'M8 Washer', 200),
(3, 'M6 Locking Nut', 300);
```

Use a window ranking function to rank items based on the ordered quantity.

```
SELECT Item,
    Quantity,
    RANK() OVER(ORDER BY Quantity) AS QtyRank
FROM OrderItems;
```

```
Item            Quantity  QtyRank
M8 Bolt         100       1
M8 Nut          100       1
M8 Washer       200       3
M6 Locking Nut  300       4
```

Use a partitioned window aggregate function to calculate the total quantity for each order (without using a `GROUP BY` clause).

```
SELECT Item,
    Quantity,
    OrderID,
    SUM(Quantity)
    OVER (PARTITION BY OrderID) AS TotalOrderQty
FROM OrderItems;
```

```
Item            Quantity  OrderID  TotalOrderQty
M8 Bolt         100       1        100
M8 Nut          100       2        100
M6 Locking Nut  300       3        500
M8 Washer       200       3        500
```

Use an analytic `LEAD` function to get the next largest quantity for the order.

```
SELECT Item,
    Quantity,
    OrderID,
    LEAD(Quantity)
    OVER (PARTITION BY OrderID ORDER BY Quantity) AS NextQtyOrder
FROM OrderItems;
```

```
Item            Quantity  OrderID  NextQtyOrder
M8 Bolt         100       1        NULL
M8 Nut          100       2        NULL
M8 Washer       200       3        300
M6 Locking Nut  300       3        NULL
```

For more information, see [SELECT - OVER Clause (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/queries/select-over-clause-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/queries/select-over-clause-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Aurora MySQL version 5.7 doesn’t support Window functions.

###### Note

Amazon Relational Database Service (Amazon RDS) for MySQL 8 supports window functions that for each row from a query perform a calculation using rows related to that row. These include functions such as `RANK()`, `LAG()`, and `NTILE()`. In addition, several existing aggregate functions now can be used as window functions, for example, `SUM()` and `AVG()`. For more information, see [Window Functions](https://dev.mysql.com/doc/refman/8.0/en/window-functions.html "https://dev.mysql.com/doc/refman/8.0/en/window-functions.html") in the _MySQL documentation_.

### Migration Considerations

As a temporary workaround, rewrite the code to remove the use of Window functions, and revert to using more traditional SQL code solutions.

In most cases, you can find an equivalent SQL query, although it may be less optimal in terms of performance, simplicity, and readability.

See the following examples for migrating Window functions to code that uses correlated subqueries.

###### Note

You may want to archive the original code and then reuse it in the future when Aurora MySQL is upgraded to version 8. The documentation for version 8 indicates the Window function syntax is ANSI compliant and will be compatible with SQL Server T-SQL syntax.

For more information, see [Window Functions](https://dev.mysql.com/doc/refman/8.0/en/window-functions.html "https://dev.mysql.com/doc/refman/8.0/en/window-functions.html") in the _MySQL documentation_.

### Examples

The following examples demonstrate ANSI SQL compliant subquery solutions as replacements for the two example queries from the previous SQL Server section.

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
(3, 'M8 Washer', 200),
(3, 'M6 Locking Nut', 300);
```

Rank items based on ordered quantity. The following example is a workaround for the window ranking function.

```
SELECT Item,
Quantity,
(
    SELECT COUNT(*)
    FROM OrderItems AS OI2
    WHERE OI.Quantity > OI2.Quantity) + 1
    AS QtyRank
FROM OrderItems AS OI;
```

```
Item            Quantity  QtyRank
M8 Bolt         100       1
M8 Nut          100       1
M6 Locking Nut  300       4
M8 Washer       200       3
```

Calculate the grand total. The following example is a workaround for a partitioned Window aggregate function.

```
SELECT Item,
Quantity,
OrderID,
(
    SELECT SUM(Quantity)
    FROM OrderItems AS OI2
    WHERE OI2.OrderID = OI.OrderID)
    AS TotalOrderQty
FROM OrderItems AS OI;
```

```
Item            Quantity  OrderID  TotalOrderQty
M8 Bolt         100       1        100
M8 Nut          100       2        100
M6 Locking Nut  300       3        500
M8 Washer       200       3        500
```

Get the next largest quantity for the order. The following example is a workaround for the `LEAD` analytical function.

```
SELECT Item,
Quantity,
OrderID,
(
    SELECT Quantity
    FROM OrderItems AS OI2
    WHERE OI.OrderID = OI2.OrderID
        AND
        OI2.Quantity > OI.Quantity
    ORDER BY Quantity
        LIMIT 1
    )
    AS NextQtyOrder
FROM OrderItems AS OI
```

```
Item            Quantity  OrderID  NextQtyOrder
M8 Bolt         100       1        [NULL]
M8 Nut          100       2        [NULL]
M6 Locking Nut  300       3        [NULL]
M8 Washer       200       3        300
```

## Summary

| SQL Server                          | Aurora MySQL       | Comments                                                                       |
| ----------------------------------- | ------------------ | ------------------------------------------------------------------------------ |
| Window functions and `OVER` clause. | Not supported yet. | Convert code to use traditional SQL techniques such as correlated sub queries. |

For more information, see [Window Function Descriptions](https://dev.mysql.com/doc/refman/8.0/en/window-function-descriptions.html "https://dev.mysql.com/doc/refman/8.0/en/window-function-descriptions.html") in the _MySQL documentation_.
