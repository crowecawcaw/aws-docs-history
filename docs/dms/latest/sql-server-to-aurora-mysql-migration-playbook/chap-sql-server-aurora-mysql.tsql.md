# SQL Server TOP and FETCH and MySQL LIMIT for T-SQL

This topic provides reference information about feature compatibility between Microsoft SQL Server 2019 and Amazon Aurora MySQL, specifically focusing on result set limiting and paging techniques. You can understand how the TOP and FETCH clauses in SQL Server correspond to the LIMIT and OFFSET clauses in Aurora MySQL.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                                    | Key differences                                                                         |
| ------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| Four star feature compatibility | Four star automation level         | [TOP and FETCH](chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.topfetch "chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.topfetch") | Syntax rewrite, very similar functionality. Convert `PERCENT` and `TIES` to subqueries. |

## SQL Server Usage

SQL Server supports two options for limiting and paging result sets returned to the client. `TOP` is a legacy, proprietary T-SQL keyword that is still supported due to its wide usage. The ANSI compliant syntax of `FETCH` and `OFFSET` were introduced in SQL Server 2012 and are recommended for paginating results sets.

### TOP

The `TOP (n)` operator is used in the `SELECT` list and limits the number of rows returned to the client based on the `ORDER BY` clause.

###### Note

When you use TOP with no `ORDER BY` clause, the query is non-deterministic and may return any rows up to the number specified by the `TOP` operator.

You can use `TOP (n)` used with two modifier options:

- `TOP (n) PERCENT` is used to designate a percentage of the rows to be returned instead of a fixed maximal row number limit (n). When using PERCENT, n can be any value from 1-100.
- `TOP (n) WITH TIES` is used to allow overriding the n maximal number (or percentage) of rows specified in case there are additional rows with the same ordering values as the last row.

###### Note

If `TOP (n)` is used without `WITH TIES` and there are additional rows that have the same ordering value as the last row in the group of n rows, the query is also non-deterministic because the last row may be any of the rows that share the same ordering value.

**Syntax**

```
SELECT TOP (<Limit Expression>) [PERCENT] [ WITH TIES ] <Select Expressions List>
FROM...
```

### OFFSET…​ FETCH

`OFFSET…​ FETCH` as part of the `ORDER BY` clause is the ANSI compatible syntax for limiting and paginating result sets. It allows specification of the starting position and limits the number of rows returned, which enables easy pagination of result sets.

Similar to `TOP`, `OFFSET…​ FETCH` relies on the presentation order defined by the `ORDER BY` clause. Unlike `TOP`, it is part of the `ORDER BY` clause and can’t be used without it.

###### Note

Queries using `FETCH…​ OFFSET` can still be non-deterministic if there is more than one row that has the same ordering value as the last row.

**Syntax**

```
ORDER BY <Ordering Expression> [ ASC | DESC ] [ ,...n ]
OFFSET <Offset Expression> { ROW | ROWS }
[FETCH { FIRST | NEXT } <Page Size Expression> { ROW | ROWS } ONLY ]
```

**Examples**

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

```
INSERT INTO OrderItems (OrderID, Item, Quantity)
VALUES
(1, 'M8 Bolt', 100),
(2, 'M8 Nut', 100),
(3, 'M8 Washer', 200),
(3, 'M6 Locking Nut', 300);
```

Retrieve the three most ordered items by quantity.

```
-- Using TOP
SELECT TOP (3) *
FROM OrderItems
ORDER BY Quantity DESC;

-- USING FETCH
SELECT *
FROM OrderItems
ORDER BY Quantity DESC
OFFSET 0 ROWS FETCH NEXT 3 ROWS ONLY;
```

```
OrderID  Item            Quantity
3        M6 Locking Nut  300
3        M8 Washer       200
2        M8 Nut          100
```

Include rows with ties.

```
SELECT TOP (3) WITH TIES *
FROM OrderItems
ORDER BY Quantity DESC;
```

```
OrderID  Item            Quantity
3        M6 Locking Nut  300
3        M8 Washer       200
2        M8 Nut          100
1        M8 Bolt         100
```

Retrieve half of the rows based on quantity.

```
SELECT TOP (50) PERCENT *
FROM OrderItems
ORDER BY Quantity DESC;
```

```
OrderID  Item            Quantity
3        M6 Locking Nut  300
3        M8 Washer       200
```

For more information, see [SELECT - ORDER BY Clause (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/queries/select-order-by-clause-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/queries/select-order-by-clause-transact-sql?view=sql-server-ver15") and [TOP (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/queries/top-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/queries/top-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) supports the non-ANSI compliant but popular with other database engines `LIMIT…​ OFFSET` operator for paging results sets.

The `LIMIT` clause limits the number of rows returned and doesn’t require an `ORDER BY` clause, although that would make the query non-deterministic.

The `OFFSET` clause is zero-based, similar to SQL Server and used for pagination.

### Migration Considerations

`LIMIT…​ OFFSET` syntax can be used to replace the functionality of both `TOP(n)` and `FETCH…​ OFFSET` in SQL Server. It is automatically converted by the AWS Schema Conversion Tool (AWS SCT except for the `WITH TIES` and `PERCENT` modifiers.

To replace the `PERCENT` option, first calculate how many rows the query returns and then calculate the fixed number of rows to be returned based on that number.

###### Note

Because this technique involves added complexity and accessing the table twice, consider changing the logic to use a fixed number instead of percentage.

To replace the `WITH TIES` option, rewrite the logic to add another query that checks for the existence of additional rows that have the same ordering value as the last row returned from the `LIMIT` clause.

###### Note

Because this technique introduces significant added complexity and three accesses to the source table, consider changing the logic to introduce a tie-breaker into the `ORDER BY` clause.

### Examples

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

```
INSERT INTO OrderItems (OrderID, Item, Quantity)
VALUES
(1, 'M8 Bolt', 100),
(2, 'M8 Nut', 100),
(3, 'M8 Washer', 200),
(3, 'M6 Locking Nut', 300);
```

Retrieve the three most ordered items by quantity.

```
SELECT *
FROM OrderItems
ORDER BY Quantity DESC
LIMIT 3 OFFSET 0;
```

For the preceding example, the result looks as shown following.

```
OrderID  Item            Quantity
3        M6 Locking Nut  300
3        M8 Washer       200
2        M8 Nut          100
```

Include rows with ties.

```
SELECT *
FROM
(
    SELECT *
    FROM OrderItems
    ORDER BY Quantity DESC
    LIMIT 3 OFFSET 0
) AS X
UNION
SELECT *
FROM OrderItems
WHERE Quantity = (
    SELECT Quantity
    FROM OrderItems
    ORDER BY Quantity DESC
    LIMIT 1 OFFSET 2
)
ORDER BY Quantity DESC
```

For the preceding example, the result looks as shown following.

```
OrderID  Item            Quantity
3        M6 Locking Nut  300
3        M8 Washer       200
2        M8 Nut          100
1        M8 Bolt         100
```

Retrieve half of the rows based on quantity.

```
CREATE PROCEDURE P(Percent INT)
BEGIN
DECLARE N INT;
SELECT COUNT(*) * Percent / 100 FROM OrderItems INTO N;
SELECT *
FROM OrderItems
ORDER BY Quantity DESC
LIMIT N OFFSET 0;
END
```

```
CALL P(50);
```

For the preceding example, the result looks as shown following.

```
OrderID  Item            Quantity
3        M6 Locking Nut  300
3        M8 Washer       200
```

## Summary

| SQL Server          | Aurora MySQL     | Comments                         |
| ------------------- | ---------------- | -------------------------------- |
| `TOP (n)`           | `LIMIT n`        |                                  |
| `TOP (n) WITH TIES` | Not supported    | See examples for the workaround. |
| `TOP (n) PERCENT`   | Not supported    | See examples for the workaround. |
| `OFFSET…​ FETCH`    | `LIMIT…​ OFFSET` |                                  |

For more information, see [SELECT Statement](https://dev.mysql.com/doc/refman/5.7/en/select.html "https://dev.mysql.com/doc/refman/5.7/en/select.html") and [LIMIT Query Optimization](https://dev.mysql.com/doc/refman/5.7/en/limit-optimization.html "https://dev.mysql.com/doc/refman/5.7/en/limit-optimization.html") in the _MySQL documentation_.
