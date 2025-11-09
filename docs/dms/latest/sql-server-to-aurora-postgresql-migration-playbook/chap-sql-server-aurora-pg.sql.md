# Table JOIN for ANSI SQL

This topic provides reference information about join operations in SQL Server and their compatibility with Amazon Aurora PostgreSQL. You can understand how different types of joins, such as INNER JOIN, OUTER JOIN, CROSS JOIN, and APPLY operations, are supported or need to be rewritten when migrating from SQL Server to Aurora PostgreSQL.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                             |
| ------------------------------- | ---------------------------------- | ------------------------- | --------------------------------------------------------------------------- |
| Four star feature compatibility | Four star automation level         | N/A                       | `OUTER JOIN` with commas. `CROSS APPLY` and `OUTER APPLY` aren’t supported. |

## SQL Server Usage

### ANSI JOIN

SQL Server supports the standard ANSI join types.

- `<Set A> CROSS JOIN <Set B>`. Results in a Cartesian product of the two sets. Every `JOIN` starts as a Cartesian product.
- `<Set A> INNER JOIN <Set B> ON <Join Condition>`. Filters the Cartesian product to only the rows where the join predicate evaluates to `TRUE`.
- `<Set A> LEFT OUTER JOIN <Set B> ON <Join Condition>`. Adds to the `INNER JOIN` all the rows from the reserved left set with NULL for all the columns that come from the right set.
- `<Set A> RIGHT OUTER JOIN <Set B> ON <Join Condition>` Adds to the `INNER JOIN` all the rows from the reserved right set with NULL for all the columns that come from the left set.
- `<Set A> FULL OUTER JOIN <Set B> ON <Join Condition>`. Designates both sets as reserved and adds non-matching rows from both, similar to a `LEFT OUTER JOIN` and a `RIGHT OUTER JOIN`.

### APPLY

SQL Server also supports the `APPLY` operator, which is somewhat similar to a join. However, `APPLY` operators enable the creation of a correlation between `<Set A>` and `<Set B>` such that `<Set B>` may consist of a sub query, a `VALUES` row value constructor, or a table valued function that is evaluated for each row of `<Set A>` where the `<Set B>` query can reference columns from the current row in `<Set A>`. This functionality isn’t possible with any type of standard `JOIN` operator.

There are two `APPLY` types:

- `<Set A> CROSS APPLY <Set B>`. Similar to a `CROSS JOIN` in the sense that every row from `<Set A>` is matched with every row from `<Set B>`.
- `<Set A> OUTER APPLY <Set B>`. Similar to a `LEFT OUTER JOIN` in the sense that rows from `<Set A>` are returned even if the sub query for `<Set B>` produces an empty set. In that case, NULL is assigned to all columns of `<Set B>`.

### ANSI SQL 89 JOIN

Up until version 2008R2, SQL Server also supported the old-style `JOIN` syntax including `LEFT` and `RIGHT OUTER JOIN`.

The ANSI syntax for a `CROSS JOIN` operator was to list the sets in the `FROM` clause using commas as separators.

```
SELECT * FROM Table1,
  Table2,
  Table3...
```

To perform an `INNER JOIN`, you only needed to add the `JOIN` predicate as part of the `WHERE` clause.

```
SELECT * FROM Table1,
  Table2
WHERE Table1.Column1 = Table2.Column1
```

Although the ANSI standard didn’t specify outer joins at the time, most RDBMS supported them in one way or another. T-SQL supported outer joins by adding an asterisk to the left or the right of equality sign of the join predicate to designate the reserved table.

```
SELECT * FROM Table1,
  Table2
WHERE Table1.Column1 *= Table2.Column1
```

To perform a `FULL OUTER JOIN`, asterisks were placed on both sides of the equality sign of the join predicate.

As of SQL Server 2008R2, outer joins using this syntax have been deprecated. For more information, see [Deprecated Database Engine Features in SQL Server 2008 R2](<https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143729(v=sql.105)?redirectedfrom=MSDN> "https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143729(v=sql.105)?redirectedfrom=MSDN") in the _SQL Server documentation_.

###### Note

Even though `INNER JOIN` using the ANSI SQL 89 syntax is still supported, they are highly discouraged due to being notorious for introducing hard-to-catch programming bugs.

### Syntax

**CROSS JOIN**

```
FROM <Table Source 1>
  CROSS JOIN
  <Table Source 2>
```

```
-- ANSI 89
FROM <Table Source 1>,
  <Table Source 2>
```

**INNER / OUTER JOIN**

```
FROM <Table Source 1>
  [ { INNER | { { LEFT | RIGHT | FULL } [ OUTER ] } }] JOIN
  <Table Source 2>
  ON <JOIN Predicate>
```

```
-- ANSI 89
FROM <Table Source 1>,
  <Table Source 2>
WHERE <Join Predicate>
<Join Predicate>:: <Table Source 1 Expression> | = | *= | =* | *=* <Table Source 2 Expression>
```

**APPLY**

```
FROM <Table Source 1>
  { CROSS | OUTER } APPLY
  <Table Source 2>
<Table Source 2>:: <SELECT sub-query> | <Table Valued UDF> | <VALUES clause>
```

### Examples

Create the Orders and Items tables.

```
CREATE TABLE Items
(
  Item VARCHAR(20) NOT NULL
  PRIMARY KEY
  Category VARCHAR(20) NOT NULL,
  Material VARCHAR(20) NOT NULL
);
```

```
INSERT INTO Items (Item, Category, Material)
VALUES
('M8 Bolt', 'Metric Bolts', 'Stainless Steel'),
('M8 Nut', 'Metric Nuts', 'Stainless Steel'),
('M8 Washer', 'Metric Washers', 'Stainless Steel'),
('3/8" Bolt', 'Imperial Bolts', 'Brass')
```

```
CREATE TABLE OrderItems
(
  OrderID INT NOT NULL,
  Item VARCHAR(20) NOT NULL
  REFERENCES Items(Item),
  Quantity SMALLINT NOT NULL,
  PRIMARY KEY(OrderID, Item)
);
```

```
INSERT INTO OrderItems (OrderID, Item, Quantity)
VALUES
(1, 'M8 Bolt', 100),
(2, 'M8 Nut', 100),
(3, 'M8 Washer', 200)
```

**INNER JOIN**

```
SELECT *
FROM Items AS I
  INNER JOIN
  OrderItems AS OI
  ON I.Item = OI.Item;
-- ANSI SQL 89
SELECT *
FROM Items AS I,
  OrderItems AS OI
WHERE I.Item = OI.Item;
```

**LEFT OUTER JOIN**

Find Items that were never ordered.

```
SELECT I.Item
FROM Items AS I
  LEFT OUTER JOIN
  OrderItems AS OI
  ON I.Item = OI.Item
WHERE OI.OrderID IS NULL;

-- ANSI SQL 89
SELECT Item
FROM
(
  SELECT I.Item, O.OrderID
  FROM Items AS I,
    OrderItems AS OI
  WHERE I.Item *= OI.Item
) AS LeftJoined
WHERE LeftJoined.OrderID IS NULL;
```

**FULL OUTER JOIN**

```
CREATE TABLE T1(Col1 INT, COl2 CHAR(2));
CREATE TABLE T2(Col1 INT, COl2 CHAR(2));

INSERT INTO T1 (Col1, Col2)
VALUES (1, 'A'), (2,'B');

INSERT INTO T2 (Col1, Col2)
VALUES (2,'BB'), (3,'CC');

SELECT *
FROM T1
  FULL OUTER JOIN
  T2
  ON T1.Col1 = T2.Col1;
```

The preceding example produces the following results.

```
Col1  COl2  Col1  COl2
1     A     NULL  NULL
2     B     2     BB
NULL  NULL  3     CC
```

For more information, see [FROM clause plus JOIN, APPLY, PIVOT (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/queries/from-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/queries/from-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) supports all types of joins in the same way as SQL Server.

- `<Set A> CROSS JOIN <Set B>`. Results in a Cartesian product of the two sets. Every `JOIN` starts as a Cartesian product.
- `<Set A> INNER JOIN <Set B> ON <Join Condition>`. Filters the Cartesian product to only the rows where the join predicate evaluates to `TRUE`.
- `<Set A> LEFT OUTER JOIN <Set B> ON <Join Condition>`. Adds to the `INNER JOIN` all the rows from the reserved left set with NULL for all the columns that come from the right set.
- `<Set A> RIGHT OUTER JOIN <Set B> ON <Join Condition>` Adds to the `INNER JOIN` all the rows from the reserved right set with NULL for all the columns that come from the left set.
- `<Set A> FULL OUTER JOIN <Set B> ON <Join Condition>`. Designates both sets as reserved and adds non-matching rows from both, similar to a `LEFT OUTER JOIN` and a `RIGHT OUTER JOIN`.

PostgreSQL doesn’t support `APPLY` options. You can replace them with `INNER JOIN LATERAL` and `LEFT JOIN LATERAL`.

### Syntax

```
FROM
    <Table Source 1> CROSS JOIN <Table Source 2>
  | <Table Source 1> INNER JOIN <Table Source 2>
    ON <Join Predicate>
  | <Table Source 1> {LEFT|RIGHT|FULL} [OUTER] JOIN <Table Source 2>
    ON <Join Predicate>
```

### Migration Considerations

For most `JOIN` statements, the syntax should be equivalent and no rewrites should be needed. Find the differences following.

- ANSI SQL 89 isn’t supported.
- `FULL OUTER JOIN` and `OUTER JOIN` using the pre-ANSI SQL 92 syntax aren’t supported, but you can use workarounds.
- `CROSS APPLY` and `OUTER APPLY` aren’t supported. You can rewrite these statements using `INNER JOIN LATERAL` and `LEFT JOIN LATERAL`.

### Examples

Create the Orders and Items tables.

```
CREATE TABLE Items
(
  Item VARCHAR(20) NOT NULL
  PRIMARY KEY
  Category VARCHAR(20) NOT NULL,
  Material VARCHAR(20) NOT NULL
);
```

```
INSERT INTO Items (Item, Category, Material)
VALUES
('M8 Bolt', 'Metric Bolts', 'Stainless Steel'),
('M8 Nut', 'Metric Nuts', 'Stainless Steel'),
('M8 Washer', 'Metric Washers', 'Stainless Steel'),
('3/8" Bolt', 'Imperial Bolts', 'Brass')
```

```
CREATE TABLE OrderItems
(
  OrderID INT NOT NULL,
  Item VARCHAR(20) NOT NULL
  REFERENCES Items(Item),
  Quantity SMALLINT NOT NULL,
  PRIMARY KEY(OrderID, Item)
);
```

```
INSERT INTO OrderItems (OrderID, Item, Quantity)
VALUES
(1, 'M8 Bolt', 100),
(2, 'M8 Nut', 100),
(3, 'M8 Washer', 200)
```

**INNER JOIN**

```
SELECT *
FROM Items AS I
  INNER JOIN
  OrderItems AS OI
  ON I.Item = OI.Item;
```

**LEFT OUTER JOIN**

Find Items that were never ordered.

```
SELECT Item
FROM Items AS I
  LEFT OUTER JOIN
  OrderItems AS OI
  ON I.Item = OI.Item
WHERE OI.OrderID IS NULL;
```

**FULL OUTER JOIN**

```
CREATE TABLE T1(Col1 INT, COl2 CHAR(2));
CREATE TABLE T2(Col1 INT, COl2 CHAR(2));

INSERT INTO T1 (Col1, Col2)
VALUES (1, 'A'), (2,'B');

INSERT INTO T2 (Col1, Col2)
VALUES (2,'BB'), (3,'CC');

SELECT *
FROM T1
FULL OUTER JOIN
T2
ON T1.Col1 = T2.Col1;
```

The preceding example produces the following results.

```
Col1  COl2  Col1  COl2
1     A     NULL  NULL
2     B     2     BB
NULL  NULL  3     CC
```

## Summary

The following table shows similarities, differences, and key migration considerations.

| SQL Server feature                       | Aurora PostgreSQL feature | Comments                                       |
| ---------------------------------------- | ------------------------- | ---------------------------------------------- |
| `INNER JOIN` with `ON` clause or commas. | Supported.                |                                                |
| `OUTER JOIN` with `ON` clause.           | Supported.                |                                                |
| `OUTER JOIN` with commas.                | Not supported.            | Requires T-SQL rewrite post SQL Server 2008R2. |
| `CROSS JOIN` or using commas.            | Supported.                |                                                |
| `CROSS APPLY` and `OUTER APPLY`.         | Not supported.            | Rewrite required.                              |

For more information, see [Controlling the Planner with Explicit JOIN Clauses](https://www.postgresql.org/docs/13/explicit-joins.html "https://www.postgresql.org/docs/13/explicit-joins.html") and [Joins Between Tables](https://www.postgresql.org/docs/13/tutorial-join.html "https://www.postgresql.org/docs/13/tutorial-join.html") in the _PostgreSQL documentation_.
