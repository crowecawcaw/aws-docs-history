# Top fetch for T-SQL

This topic provides reference information about feature compatibility between Microsoft SQL Server 2019 and Amazon Aurora PostgreSQL, specifically focusing on result set limiting and paging. You can understand how SQL Server’s TOP and FETCH clauses compare to PostgreSQL’s LIMIT and OFFSET functionality. The topic explains the differences in syntax and capabilities, helping you navigate the transition from SQL Server to Aurora PostgreSQL.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                  | Key differences                 |
| ------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------- |
| Four star feature compatibility | Four star automation level         | [TOP and FETCH](chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.fetch "chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.fetch") | PostgreSQL doesn’t support TOP. |

## SQL Server Usage

SQL Server supports two options for limiting and paging result sets returned to the client. `TOP` is a legacy, proprietary T-SQL keyword that is still supported due to its wide usage. The ANSI compliant syntax of `FETCH` and `OFFSET` were introduced in SQL Server 2012 and are recommended for paginating results sets.

### TOP

The `TOP (n)` operator is used in the `SELECT` list and limits the number of rows returned to the client based on the `ORDER BY` clause.

###### Note

When `TOP` is used with no `ORDER BY` clause, the query is non-deterministic and may return any rows up to the number specified by the `TOP` operator.

You can use `TOP (n)` with two modifier options:

- `TOP (n) PERCENT` is used to designate a percentage of the rows to be returned instead of a fixed maximal row number `limit (n)`. When you use `PERCENT`, `n` can be any value from 1-100.
- `TOP (n) WITH TIES` is used to allow overriding the n maximal number or percentage of rows specified in case there are additional rows with the same ordering values as the last row.

If you use `TOP (n)` without `WITH TIES` and there are additional rows that have the same ordering value as the last row in the group of n rows, the query is also non-deterministic because the last row may be any of the rows that share the same ordering value.

### Syntax

```
ORDER BY <Ordering Expression> [ ASC | DESC ] [ ,...n ]
OFFSET <Offset Expression> { ROW | ROWS }
[FETCH { FIRST | NEXT } <Page Size Expression> { ROW | ROWS } ONLY ]
```

### Examples

The following example creates the OrderItems table.

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

The following example retrieves the 3 most ordered items by quantity.

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

For the preceding example, the result looks as shown following.

```
OrderID  Item            Quantity
3        M6 Locking Nut  300
3        M8 Washer       200
2        M8 Nut          100
```

The following example includes rows with ties.

```
SELECT TOP (3) WITH TIES *
FROM OrderItems
ORDER BY Quantity DESC;
```

For the preceding example, the result looks as shown following.

```
OrderID  Item            Quantity
3        M6 Locking Nut  300
3        M8 Washer       200
2        M8 Nut          100
1        M8 Bolt         100
```

The following example retrieves half the rows based on quantity.

```
SELECT TOP (50) PERCENT *
FROM OrderItems
ORDER BY Quantity DESC;
```

For the preceding example, the result looks as shown following.

```
OrderID  Item            Quantity
3        M6 Locking Nut  300
3        M8 Washer       200
```

For more information, see [SELECT - ORDER BY Clause (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/queries/select-order-by-clause-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/queries/select-order-by-clause-transact-sql?view=sql-server-ver15") and [TOP (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/queries/top-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/queries/top-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) supports the non-ANSI compliant but popular with other engines `LIMIT…​ OFFSET` operator for paging results sets.

The `LIMIT` clause limits the number of rows returned and doesn’t require an `ORDER BY` clause, although that would make the query non-deterministic.

The `OFFSET` clause is zero-based, similar to SQL Server and used for pagination. `OFFSET 0` is the same as omitting the `OFFSET` clause, as is `OFFSET` with a NULL argument.

### Syntax

```
SELECT select_list
  FROM table_expression
  [ ORDER BY ... ]
  [ LIMIT { number | ALL } ] [ OFFSET number ]
```

### Migration Considerations

You can use the `LIMIT…​ OFFSET` syntax to replace the functionality of `TOP(n)` and `FETCH…​ OFFSET` in SQL Server. It is automatically converted by the AWS Schema Conversion Tool (AWS SCT) except for the `WITH TIES` and `PERCENT` modifiers.

To replace the `PERCENT` option, first calculate how many rows the query returns and then calculate the fixed number of rows to be returned based on that number.

###### Note

Because this technique involves added complexity and accessing the table twice, consider changing the logic to use a fixed number instead of percentage.

To replace the `WITH TIES` option, rewrite the logic to add another query that checks for the existence of additional rows that have the same ordering value as the last row returned from the `LIMIT` clause.

###### Note

Because this technique introduces significant added complexity and three accesses to the source table, consider changing the logic to introduce a tie-breaker into the `ORDER BY` clause.

### Examples

The following example creates the OrderItems table.

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

The following example retrieves the three most ordered items by quantity.

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
1        M8 Bolt         100
```

The following example includes rows with ties.

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

The following example retrieves half the rows based on quantity.

```
CREATE or replace FUNCTION getOrdersPct(int) RETURNS SETOF OrderItems AS $$
SELECT * FROM OrderItems
ORDER BY Quantity desc LIMIT (SELECT COUNT(*)*$1/100 FROM OrderItems) OFFSET 0;
$$ LANGUAGE SQL;
```

```
SELECT * from getOrdersPct(50);
or
SELECT getOrdersPct(50);

OrderID  Item            Quantity
3        M6 Locking Nut  300
3        M8 Washer       200
```

## Summary

| SQL Server          | Aurora PostgreSQL | Comments                    |
| ------------------- | ----------------- | --------------------------- |
| `TOP (n)`           | `LIMIT n`         |                             |
| `TOP (n) WITH TIES` | Not supported     | See examples for workaround |
| `TOP (n) PERCENT`   | Not supported     | See examples for workaround |
| `OFFSET…​ FETCH`    | `LIMIT…​ OFFSET`  |                             |

For more information, see [LIMIT and OFFSET](https://www.postgresql.org/docs/13/queries-limit.html "https://www.postgresql.org/docs/13/queries-limit.html") in the _PostgreSQL documentation_.
