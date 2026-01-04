# GROUP BY for ANSI SQL

This topic provides reference information about migrating from Microsoft SQL Server 2019 to Amazon Aurora PostgreSQL, focusing on GROUP BY, CUBE, ROLLUP, and GROUPING SETS functionalities. You can use this guide to understand the similarities and differences between these database systems when working with aggregate functions and grouping operations.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| ------------------------------- | ---------------------------------- | ------------------------- | --------------- |
| Five star feature compatibility | Five star automation level         | N/A                       | N/A             |

## SQL Server Usage

`GROUP BY` is an ANSI SQL query clause used to group individual rows that have passed the `WHERE` filter clause into groups to be passed on to the `HAVING` filter and then to the `SELECT` list. This grouping supports the use of aggregate functions such as `SUM`, `MAX`, `AVG`, and others.

### Syntax

ANSI compliant `GROUP BY` Syntax.

```
GROUP BY
[ROLLUP | CUBE]
<Column Expression> ...n
[GROUPING SETS (<Grouping Set>)...n
```

Backward compatibility syntax.

```
GROUP BY
  [ ALL ] <Column Expression> ...n
  [ WITH CUBE | ROLLUP ]
```

The basic ANSI syntax for GROUP BY supports multiple grouping expressions, the `CUBE` and `ROLLUP` keywords, and the `GROUPING SETS` clause; all used to add super-aggregate rows to the output.

Up to SQL Server 2008 R2, the database engine supported a legacy, proprietary syntax (not ANSI Compliant) using the `WITH CUBE` and `WITH ROLLUP` clauses. These clauses added super-aggregates to the output.

Also, up to SQL Server 2008 R2, SQL Server supported the `GROUP BY ALL` syntax, which was used to create an empty group for rows that failed the WHERE clause.

SQL Server supports the following aggregate functions: `AVG`, `CHECKSUM_AGG`, `COUNT`, `COUNT_BIG`, `GROUPING`, `GROUPING_ID`, `STDEV`, `STDEVP`, `STRING_AGG`, `SUM`, `MIN`, `MAX`, `VAR`, `VARP`.

### Examples

**Legacy CUBE and ROLLUP Syntax**

```
CREATE TABLE Orders
(
  OrderID INT IDENTITY(1,1) NOT NULL
  PRIMARY KEY,
  Customer VARCHAR(20) NOT NULL,
  OrderDate DATE NOT NULL
);
```

```
INSERT INTO Orders(Customer, OrderDate)
VALUES ('John', '20180501'), ('John', '20180502'), ('John', '20180503'),
  ('Jim', '20180501'), ('Jim', '20180503'), ('Jim', '20180504')
```

```
SELECT Customer,
  OrderDate,
  COUNT(*) AS NumOrders
FROM Orders AS O
GROUP BY Customer, OrderDate
WITH ROLLUP
```

The preceding example produces the following results.

```
Customer  OrderDate   NumOrders
Jim       2018-05-01  1
Jim       2018-05-03  1
Jim       2018-05-04  1
Jim       NULL        3
John      2018-05-01  1
John      2018-05-02  1
John      2018-05-03  1
John      NULL        3
NULL      NULL        6
```

The rows with NULL were added as a result of the `WITH ROLLUP` clause and contain super aggregates for the following:

- All orders for Jim and John regardless of OrderDate.
- A super aggregated for all customers and all dates.

Using `CUBE` instead of `ROLLUP` adds super aggregates in all possible combinations, not only in `GROUP BY` expression order.

```
SELECT Customer,
  OrderDate,
  COUNT(*) AS NumOrders
FROM Orders AS O
GROUP BY Customer, OrderDate
WITH CUBE
```

The preceding example produces the following results.

```
Customer  OrderDate   NumOrders
Jim       2018-05-01  1
John      2018-05-01  1
NULL      2018-05-01  2
John      2018-05-02  1
NULL      2018-05-02  1
Jim       2018-05-03  1
John      2018-05-03  1
NULL      2018-05-03  2
Jim       2018-05-04  1
NULL      2018-05-04  1
NULL      NULL        6
Jim       NULL        3
John      NULL        3
```

Four additional rows were added by the `CUBE`. They provide super aggregates for every date for all customers that were not part of the `ROLLUP` results in the preceding example.

**Legacy GROUP BY ALL**

Use the Orders table from the previous example.

```
SELECT Customer, OrderDate, COUNT(*) AS NumOrders
FROM Orders AS O
WHERE OrderDate <= '20180503'
GROUP BY ALL Customer, OrderDate
```

The preceding example produces the following results.

```
Customer  OrderDate   NumOrders
Jim       2018-05-01  1
John      2018-05-01  1
John      2018-05-02  1
Jim       2018-05-03  1
John      2018-05-03  1
Jim       2018-05-04  0
Warning: Null value is eliminated by an aggregate or other SET operation.
```

The last row failed the WHERE clause and was returned as an empty group as indicated by the warning for the empty `COUNT(*) = 0`.

**Use GROUPING SETS**

The following query uses the ANSI compliant `GROUPING SETS` syntax to provide all possible aggregate combinations for the Orders table, similar to the result of the `CUBE` syntax. This syntax requires specifying each dimension that needs to be aggregated.

```
SELECT Customer, OrderDate, COUNT(*) AS NumOrders
FROM Orders AS O
GROUP BY GROUPING SETS (
  (Customer, OrderDate),
  (Customer),
  (OrderDate),
  ()
)
```

The preceding example produces the following results.

```
Customer  OrderDate   NumOrders
Jim       2018-05-01  1
John      2018-05-01  1
NULL      2018-05-01  2
John      2018-05-02  1
NULL      2018-05-02  1
Jim       2018-05-03  1
John      2018-05-03  1
NULL      2018-05-03  2
Jim       2018-05-04  1
NULL      2018-05-04  1
NULL      NULL        6
Jim       NULL        3
John      NULL        3
```

For more information, see [Aggregate Functions (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/functions/aggregate-functions-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/functions/aggregate-functions-transact-sql?view=sql-server-ver15") and [SELECT - GROUP BY- Transact-SQL](https://docs.microsoft.com/en-us/sql/t-sql/queries/select-group-by-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/queries/select-group-by-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) supports the basic ANSI syntax for `GROUP BY` and also supports `GROUPING SETS CUBE`, and `ROLLUP`.

In Aurora PostgreSQL, you can use `ROLLUP` and `ORDER BY` clauses in the same query, but the syntax is different from SQL Server. There is no `WITH` clause in the statement.

```
SELECT Customer, OrderDate, COUNT(*) AS NumOrders
FROM Orders AS O
GROUP BY ROLLUP (Customer, OrderDate)
```

The main difference is the need to move from writing the column to `GROUP BY` after the `ROLLUP`.

For the `CUBE` option, it’s the same change.

```
SELECT Customer, OrderDate, COUNT(*) AS NumOrders
FROM Orders AS O
GROUP BY CUBE (Customer, OrderDate);
```

For the `GROUPING SET`, use the following query.

```
SELECT Customer, OrderDate, COUNT(*) AS NumOrders
FROM Orders AS O
GROUP BY GROUPING SETS (
  (Customer, OrderDate),
  (Customer),
  (OrderDate),
  ()
);
```

For more information, see [Table Expressions](https://www.postgresql.org/docs/13/queries-table-expressions.html "https://www.postgresql.org/docs/13/queries-table-expressions.html") in the _PostgreSQL documentation_.

### Syntax

```
SELECT <Select List>
FROM <Table Source>
WHERE <Row Filter>
GROUP BY
  [ROLLUP | CUBE | GROUPING SETS]
<Column Name> | <Expression> | <Position>
```

### Migration Considerations

The `GROUP BY` functionality exists except for the `ALL` option.

Convert every query to use the column name after the `GROUP BY` option, such as `CUBE`, `ROLLUP`, or `CUBE`.

### Examples

Rewrite SQL Server `WITH CUBE` modifier for migration.

```
CREATE TABLE Orders
(
  OrderID serial NOT NULL
  PRIMARY KEY,
  Customer VARCHAR(20) NOT NULL,
  OrderDate DATE NOT NULL
);
```

```
INSERT INTO Orders(Customer, OrderDate)
VALUES ('John', '20180501'), ('John', '20180502'), ('John', '20180503'),
  ('Jim', '20180501'), ('Jim', '20180503'), ('Jim', '20180504');
```

```
SELECT Customer, OrderDate, COUNT(*) AS NumOrders
FROM Orders AS O
GROUP BY CUBE (Customer, OrderDate);
```

The preceding example produces the following results.

```
Customer  OrderDate   NumOrders
Jim       2018-05-01  1
Jim       2018-05-03  1
Jim       2018-05-04  1
Jim       NULL        3
John      2018-05-01  1
John      2018-05-02  1
John      2018-05-03  1
John      NULL        3
NULL      NULL        6
NULL      2018-05-01  2
NULL      2018-05-02  1
NULL      2018-05-03  2
NULL      2018-05-04  1
```

Rewrite SQL Server `GROUP BY ALL` for migration.

```
SELECT Customer, OrderDate, COUNT(*) AS NumOrders
FROM Orders AS O
WHERE OrderDate <= '20180503'
GROUP BY Customer, OrderDate
UNION ALL -- Add the empty groups
SELECT DISTINCT Customer, OrderDate, 0
FROM Orders AS O
WHERE OrderDate > '20180503';
```

The preceding example produces the following results.

```
Customer  OrderDate   NumOrders
Jim       2018-05-01  1
Jim       2018-05-03  1
John      2018-05-01  1
John      2018-05-02  1
John      2018-05-03  1
Jim       2018-05-04  0
```

## Summary

The following table shows similarities, differences, and key migration considerations.

| SQL Server feature                        | Aurora PostgreSQL feature                     | Comments                                                                                                    |
| ----------------------------------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `MAX`, `MIN`, `AVG`, `COUNT`, `COUNT_BIG` | `MAX`, `MIN`, `AVG`, `COUNT`                  | In Aurora PostgreSQL, `COUNT` returns a `BIGINT` and is compatible with SQL Server `COUNT` and `COUNT_BIG`. |
| `CHECKSUM_AGG`                            | N/A                                           | Use a loop to calculate checksums.                                                                          |
| `GROUPING`, `GROUPING_ID`                 | `GROUPING`                                    | Reconsider the query logic to avoid having NULL groups that are ambiguous with the super aggregates.        |
| `STDEV`, `STDEVP`, `VAR`, `VARP`          | `STDDEV`, `STDDEV_POP`, `VARIANCE`, `VAR_POP` | Rewrite keywords only.                                                                                      |
| `STRING_AGG`                              | `STRING_AGG`                                  |                                                                                                             |
| `WITH ROLLUP`                             | `ROLLUP`                                      | Remove `WITH` and change the columns names to be after the `ROLLUP` keyword.                                |
| `WITH CUBE`                               | `CUBE`                                        | Remove `WITH` and change the columns names to be after the `CUBE` keyword.                                  |
| `GROUPING SETS`                           | `GROUPING SETS`                               |                                                                                                             |

For more information, see [Aggregate Functions](https://www.postgresql.org/docs/10/functions-aggregate.html "https://www.postgresql.org/docs/10/functions-aggregate.html") in the _PostgreSQL documentation_.
