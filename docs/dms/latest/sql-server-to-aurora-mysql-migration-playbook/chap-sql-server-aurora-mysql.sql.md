# GROUP BY for ANSI SQL

This topic provides reference content comparing the GROUP BY functionality in Microsoft SQL Server 2019 and Amazon Aurora MySQL. It explores the similarities and differences in syntax, supported features, and aggregate functions between the two database systems.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                             | Key differences                                                                                                                              |
| ------------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Four star feature compatibility | Four star automation level         | [GROUP BY](chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.groupby "chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.groupby") | Basic syntax compatible. Advanced options such as `ALL`, `CUBE`, `GROUPING SETS` will require rewrites to use multiple queries with `UNION`. |

## SQL Server Usage

`GROUP BY` is an ANSI SQL query clause used to group individual rows that have passed the `WHERE` filter clause into groups to be passed on to the `HAVING` filter and then to the `SELECT` list. This grouping supports the use of aggregate functions such as `SUM`, `MAX`, `AVG` and others.

### Syntax

ANSI compliant `GROUP BY` syntax:

```
GROUP BY
[ROLLUP | CUBE]
<Column Expression> ...n
[GROUPING SETS (<Grouping Set>)...n
```

Backward compatibility syntax:

```
GROUP BY
    [ ALL ] <Column Expression> ...n
    [ WITH CUBE | ROLLUP ]
```

The basic ANSI syntax for `GROUP BY` supports multiple grouping expressions, the `CUBE` and ROLLUP keywords, and the `GROUPING SETS` clause; all used to add super-aggregate rows to the output.

Up to SQL Server 2008 R2, the database engine supported a legacy, proprietary, and not ANSI-compliant syntax using the `WITH CUBE` and `WITH ROLLUP` clauses. These clauses added super-aggregates to the output.

Also, up to SQL Server 2008 R2, SQL Server supported the `GROUP BY ALL` syntax, which was used to create an empty group for rows that failed the `WHERE` clause.

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

The rows with NULL values were added as a result of the `WITH ROLLUP` clause and contain super aggregates for the following:

- All orders for Jim and John regardless of `OrderDate`.
- A super aggregated for all customers and all dates.

Using `CUBE` instead of `ROLLUP` adds super aggregates in all possible combinations, not only in group by expression order.

```
SELECT Customer,
    OrderDate,
    COUNT(*) AS NumOrders
FROM Orders AS O
GROUP BY Customer, OrderDate
WITH CUBE
```

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

The additional four rows where the value for Customer is set to NULL, were added by `CUBE`. These rows provide super aggregates for every date for all customers that were not part of the `ROLLUP` results.

**Legacy GROUP BY ALL**

Use the Orders table from the preceding example.

```
SELECT Customer,
    OrderDate,
    COUNT(*) AS NumOrders
FROM Orders AS O
WHERE OrderDate <= '20180503'
GROUP BY ALL Customer, OrderDate
```

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

The last row for 2018-05-04 failed the `WHERE` clause and was returned as an empty group as indicated by the warning for the empty `COUNT(*) = 0`.

**Use GROUPING SETS**

The following query uses the ANSI compliant `GROUPING SETS` syntax to provide all possible aggregate combinations for the `Orders` table, similar to the result of the `CUBE` syntax. This syntax requires specifying each dimension that needs to be aggregated.

```
SELECT Customer,
    OrderDate,
    COUNT(*) AS NumOrders
FROM Orders AS O
GROUP BY GROUPING SETS (
    (Customer, OrderDate),
    (Customer),
    (OrderDate),
    ()
    )
```

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

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) supports only the basic ANSI syntax for `GROUP BY` and doesn’t support `GROUPING SETS` or the standard `GROUP BY CUBE` and `GROUP BY ROLLUP`. Aurora MySQL supports the `WITH ROLLUP` non-ANSI syntax like SQL Server, but not the `CUBE` option.

Aurora MySQL supports a wider range of aggregate functions than SQL Server: `AVG`, `BIT_AND`, `BIT_OR`, `BIT_XOR`, `COUNT`, `GROUP_CONCAT`, `JSON_ARRAYAGG`, `JSON_OBJECTAGG`, `MAX`, `MIN`, `STD`, `STDDEV`, `STDDEV_POP`, `STDDEV_SAMP`, `SUM`, `VAR_POP`, `VAR_SAMP`, `VARIANCE`.

The bitwise aggregates and the JSON aggregates not available in SQL Server may prove to be very useful in many scenarios. For more information, see [MySQL Handling of GROUP BY](https://dev.mysql.com/doc/refman/5.7/en/group-by-handling.html "https://dev.mysql.com/doc/refman/5.7/en/group-by-handling.html") in the _MySQL documentation_.

Unlike SQL Server, in Aurora MySQL you can’t use `ROLLUP` and `ORDER BY` clauses in the same query. As a workaround, encapsulate the `ROLLUP` query as a derived table and add the `ORDER BY` clause to the outer query.

```
SELECT *
FROM (
    SELECT Customer,
        OrderDate,
        COUNT(*) AS NumOrders
    FROM Orders AS O
    GROUP BY Customer, OrderDate
    WITH ROLLUP
)
ORDER BY OrderDate, Customer;
```

Additionally, rows produced by `ROLLUP` can’t be referenced in a `WHERE` clause or in a `FROM` clause as a join condition because the super aggregates are added late in the processing phase.

Even more problematic is the lack of a function equivalent to the `GROUPING_ID` function in SQL Server, which can be used to distinguish super aggregate rows from the base groups. Unfortunately, it is currently not possible to distinguish rows that have NULLs due to being super aggregates from rows where the NULL is from the base set.

Until SQL92, column expressions not appearing in the `GROUP BY` list were not allowed in the `HAVING`, `SELECT`, and `ORDER BY` clauses. This limitation still applies in SQL Server today. For example, the following query isn’t legal in SQL Serve since a customer group may contain multiple order dates.

```
SELECT Customer,
    OrderDate,
    COUNT(*) AS NumOrders
FROM Orders AS O
GROUP BY Customer
```

However, in some cases, when the columns that don’t appear in the GROUP BY clause are functionally dependent on the `GROUP BY` columns, it does make sense to allow it and ANSI SQL optional feature T301 does allow it. Aurora MySQL can detect such functional dependencies and allows such queries to run.

###### Note

To use non-aggregate columns in the `HAVING`, `SELECT`, and `ORDER BY` clauses, turn on the `ONLY_FULL_GROUP_BY` SQL mode.

### Syntax

```
SELECT <Select List>
FROM <Table Source>
WHERE <Row Filter>
GROUP BY <Column Name> | <Expression> | <Position>
    [ASC | DESC], ...
    [WITH ROLLUP]]
```

### Migration Considerations

For most aggregate queries that use only grouping expressions without modifiers, the migration should be straightforward. Even the `WITH ROLLUP` syntax is supported as is in Aurora MySQL. For more complicated aggregates such as `CUBE` and `GROUPING SETS`, a rewrite to include all sub-aggregate queries as `UNION ALL` sets is required.

Because Aurora MySQL supports a wider range of aggregate functions, the migration shouldn’t present major challenges. Some minor syntax changes, for example replacing `STDEVP` with `STDDEV_POP`, can be performed automatically by the AWS Schema Conversion Tool (AWS SCT. Some may need manual intervention such as rewriting the `STRING_AGG` syntax to `GROUP_CONCAT`. Also consider using Aurora MySQL additional aggregate functions for query optimizations.

If you plan to keep using the `WITH ROLLUP` groupings, you must consider how to handle NULLS since Aurora MySQL doesn’t support an equivalent function to `GROUPING_ID` in SQL Server.

### Examples

Rewrite SQL Server WITH CUBE modifier for migration.

```
CREATE TABLE Orders
(
    OrderID INT NOT NULL AUTO_INCREMENT
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
UNION ALL -- Add the super aggregate rows for each OrderDate
SELECT NULL,
    OrderDate,
    COUNT(*) AS NumOrders
FROM Orders AS O
GROUP BY OrderDate
```

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
SELECT Customer,
    OrderDate,
    COUNT(*) AS NumOrders
FROM Orders AS O
WHERE OrderDate <= '20180503'
GROUP BY Customer, OrderDate
UNION ALL -- Add the empty groups
SELECT DISTINCT Customer,
    OrderDate,
    NULL
FROM Orders AS O
WHERE OrderDate > '20180503';
```

```
Customer  OrderDate   NumOrders
Jim       2018-05-01  1
Jim       2018-05-03  1
John      2018-05-01  1
John      2018-05-02  1
John      2018-05-03  1
Jim       2018-05-04  NULL
```

## Summary

Table of similarities, differences, and key migration considerations.

| SQL Server feature                        | Aurora MySQL feature                                    | Comments                                                                                                     |
| ----------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `MAX`, `MIN`, `AVG`, `COUNT`, `COUNT_BIG` | `MAX`, `MIN`, `AVG`, `COUNT`                            | In Aurora MySQL, `COUNT` returns a `BIGINT` and is compatible with `COUNT` and `COUNT_BIG` in SQL Server.    |
| `CHECKSUM_AGG`                            | N/A                                                     | Use a loop to calculate checksums.                                                                           |
| `GROUPING`, `GROUPING_ID`                 | N/A                                                     | Reconsider query logic to avoid having NULL groups that are ambiguous with the super aggregates.             |
| `STDEV`, `STDEVP`, `VAR`, `VARP`          | `STDDEV`, `STDDEV_POP`, `VARIANCE`, `VAR_POP`           | Rewrite keywords only.                                                                                       |
| `STRING_AGG`                              | `GROUP_CONCAT`                                          | Rewrite syntax.                                                                                              |
| `WITH ROLLUP`                             | `WITH ROLLUP`                                           | Compatible                                                                                                   |
| `WITH CUBE`                               | N/A                                                     | Rewrite using UNION ALL.                                                                                     |
| `ANSI CUBE` / `ROLLUP`                    | N/A                                                     | Rewrite using `WITH ROLLUP` and using `UNION ALL` queries.                                                   |
| `GROUPING SETS`                           | N/A                                                     | Rewrite using `UNION ALL` queries.                                                                           |
| N/A                                       | Non-aggregate columns in `HAVING`, `SELECT`, `ORDER BY` | Requires to turn off the `ONLY_FULL_GROUP_BY` SQL mode. Functional dependencies are evaluated by the engine. |

For more information, see [MySQL Handling of GROUP BY](https://dev.mysql.com/doc/refman/5.7/en/group-by-handling.html "https://dev.mysql.com/doc/refman/5.7/en/group-by-handling.html") in the _MySQL documentation_.
