# Window functions for ANSI SQL

This topic provides reference information comparing window functions in Microsoft SQL Server and PostgreSQL, which is valuable for database migration projects. You can gain insights into the similarities and differences between these two database systems' analytical capabilities. The topic highlights the types of window functions available in SQL Server, including ranking, aggregate, and analytic functions, and compares them to PostgreSQL’s window function support.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| ------------------------------- | ---------------------------------- | ------------------------- | --------------- |
| Five star feature compatibility | Five star automation level         | N/A                       | N/A             |

## SQL Server Usage

Window functions use an `OVER` clause to define the window and frame for a data set to be processed. They are part of the ANSI standard and are typically compatible among various SQL dialects. However, most RDBMS don’t yet support the full ANSI specification.

Window functions are a relatively new, advanced, and efficient T-SQL programming tool. They are highly utilized by developers to solve numerous programming challenges.

SQL Server currently supports the following window functions:

- Ranking functions: `ROW_NUMBER`, `RANK`, `DENSE_RANK`, and `NTILE`.
- Aggregate functions: `AVG`, `MIN`, `MAX`, `SUM`, `COUNT`, `COUNT_BIG`, `VAR`, `STDEV`, `STDEVP`, `STRING_AGG`, `GROUPING`, `GROUPING_ID`, `VAR`, `VARP`, and `CHECKSUM_AGG`.
- Analytic functions: `LAG`, `LEAD`, `FIRST_Value`, `LAST_VALUE`, `PERCENT_RANK`, `PERCENTILE_CONT`, `PERCENTILE_DISC`, and `CUME_DIST`.
- Other functions: `NEXT_VALUE_FOR`. For more information, see [Sequences and Identity](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").

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

The following example creates and populates an OrderItems table.

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

The following example uses a window ranking function to rank items based on the ordered quantity.

```
SELECT Item,
  Quantity,
RANK() OVER(ORDER BY Quantity) AS QtyRank
FROM OrderItems;
```

The preceding example produces the following results.

```
Item            Quantity  QtyRank
M8 Bolt         100       1
M8 Nut          100       1
M8 Washer       200       3
M6 Locking Nut  300       4
```

The following example uses a partitioned window aggregate function to calculate the total quantity for each order. This statement doesn’t use a `GROUP BY` clause.

```
SELECT Item,
Quantity,
OrderID,
SUM(Quantity)
OVER (PARTITION BY OrderID) AS TotalOrderQty
FROM OrderItems;
```

The preceding example produces the following results.

```
Item            Quantity  QtyRank  TotalOrderQty
M8 Bolt         100       1        100
M8 Nut          100       2        100
M6 Locking Nut  300       3        500
M8 Washer       200       3        500
```

The following example uses an analytic `LEAD` function to get the next largest quantity for the order.

```
SELECT Item,
  Quantity,
  OrderID,
  LEAD(Quantity)
  OVER (PARTITION BY OrderID ORDER BY Quantity) AS NextQtyOrder
FROM OrderItems;
```

The preceding example produces the following results.

```
Item            Quantity  OrderID  NextQtyOrder
M8 Bolt         100       1        NULL
M8 Nut          100       2        NULL
M8 Washer       200       3        300
M6 Locking Nut  300       3        NULL
```

For more information, see [SELECT - OVER Clause (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/queries/select-over-clause-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/queries/select-over-clause-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

PostgreSQL refers to ANSI SQL analytical functions as window functions. They provide the same core functionality as SQL Server analytical functions. Window functions in PostgreSQL operate on a logical partition or window of the result set and return a value for rows in that window.

From a database migration perspective, you should examine PostgreSQL window functions by type and compare them with the equivalent SQL Server window functions to verify compatibility of syntax and output.

###### Note

Even if a PostgreSQL window function provides the same functionality of a specific SQL Server window function, the returned data type may be different and require application changes.

PostgreSQL provides support for two main types of window functions: aggregation functions and ranking functions.

### PostgreSQL Window Functions by Type

| Function type | Related functions                                                                                                                 |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Aggregate     | `avg`, `count`, `max`, `min`, `sum`, `string_agg`                                                                                 |
| Ranking       | `row_number`, `rank`, `dense_rank`, `percent_rank`, `cume_dist`, `ntile`, `lag`, `lead`, `first_value`, `last_value`, `nth_value` |

### PostgreSQL Window Functions

| PostgreSQL window function | Returned data type                                        | Compatible syntax |
| -------------------------- | --------------------------------------------------------- | ----------------- |
| Count                      | bigint                                                    | Yes               |
| Max                        | numeric, string, date/time, network or enum type          | Yes               |
| Min                        | numeric, string, date/time, network or enum type          | Yes               |
| Avg                        | numeric, double, otherwise same data type as the argument | Yes               |
| Sum                        | bigint, otherwise same data type as the argument          | Yes               |
| rank()                     | bigint                                                    | Yes               |
| row_number()               | bigint                                                    | Yes               |
| dense_rank()               | bigint                                                    | Yes               |
| percent_rank()             | double                                                    | Yes               |
| cume_dist()                | double                                                    | Yes               |
| ntile()                    | integer                                                   | Yes               |
| lag()                      | Same type as value                                        | Yes               |
| lead()                     | Same type as value                                        | Yes               |
| first_value()              | Same type as value                                        | Yes               |
| last_value()               | Same type as value                                        | Yes               |

### Examples

The following example uses he PostgreSQL `rank()` function.

```
SELECT department_id, last_name, salary, commission_pct,
RANK() OVER (PARTITION BY department_id
ORDER BY salary DESC, commission_pct) "Rank"
FROM employees WHERE department_id = 80;

DEPARTMENT_ID  LAST_NAME  SALARY    COMMISSION_PCT  Rank
80             Russell    14000.00  0.40            1
80             Partners   13500.00  0.30            2
80             Errazuriz  12000.00  0.30            3
```

The returned formatting for certain numeric data types is different.

The following example calculates the total salary for the department 80.

```
SELECT SUM(salary)
FROM employees WHERE department_id = 80;

SUM(SALARY)
39500.00
```

The following example creates and populates an OrderItems table.

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
INSERT INTO OrderItems (OrderID, Item, Quantity) VALUES
(1, 'M8 Bolt', 100),
(2, 'M8 Nut', 100),
(3, 'M8 Washer', 200),
(3, 'M6 Locking Nut', 300);
```

The following example uses a window ranking function to rank items based on the ordered quantity.

```
SELECT Item, Quantity, RANK()
  OVER(ORDER BY Quantity) AS QtyRank
FROM OrderItems;

Item            Quantity  QtyRank
M8 Bolt         100       1
M8 Nut          100       1
M8 Washer       200       3
M6 Locking Nut  300       4
```

The following example uses a partitioned window aggregate function to calculate the total quantity for each order. This statement doesn’t use a `GROUP BY` clause.

```
SELECT Item, Quantity, OrderID, SUM(Quantity)
  OVER (PARTITION BY OrderID) AS TotalOrderQty
FROM OrderItems;

Item            Quantity  OrderID  TotalOrderQty
M8 Bolt         100       1        100
M8 Nut          100       2        100
M6 Locking Nut  300       3        500
M8 Washer       200       3        500
```

The following example uses an analytic `LEAD` function to get the next largest quantity for the order.

```
SELECT Item, Quantity, OrderID, LEAD(Quantity)
  OVER (PARTITION BY OrderID ORDER BY Quantity) AS NextQtyOrder
FROM OrderItems;

Item            Quantity  OrderID  NextQtyOrder
M8 Bolt         100       1        NULL
M8 Nut          100       2        NULL
M8 Washer       200       3        300
M6 Locking Nut  300       3        NULL
```

For more information, see [Window Functions](https://www.postgresql.org/docs/13/tutorial-window.html "https://www.postgresql.org/docs/13/tutorial-window.html") in the _PostgreSQL documentation_.
