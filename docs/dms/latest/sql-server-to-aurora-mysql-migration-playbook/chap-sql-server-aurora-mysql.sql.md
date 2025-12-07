# Table JOIN for ANSI SQL

This topic provides reference content comparing table join functionality between Microsoft SQL Server 2019 and Amazon Aurora MySQL. You can understand the similarities and differences in join syntax and support between these two database systems.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                                      | Key differences                                                                                          |
| ------------------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Four star feature compatibility | Four star automation level         | [Table Joins](chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.tablejoins "chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.tablejoins") | Basic syntax compatible. `FULL OUTER`, `APPLY`, and `ANSI SQL 89` outer joins will need to be rewritten. |

## SQL Server Usage

SQL Server supports the standard ANSI join types:

- `<Set A> CROSS JOIN <Set B>` — Results in a Cartesian product of the two sets. Every `JOIN` starts as a Cartesian product.
- `<Set A> INNER JOIN <Set B> ON <Join Condition>` — Filters the cartesian product to only the rows where the join predicate evaluates to `TRUE`.
- `<Set A> LEFT OUTER JOIN <Set B> ON <Join Condition>` — Adds to the `INNER JOIN` all the rows from the reserved left set with NULL for all the columns that come from the right set.
- `<Set A> RIGHT OUTER JOIN <Set B> ON <Join Condition>` — Adds to the `INNER JOIN` all the rows from the reserved right set with NULL for all the columns that come from the left set.
- `<Set A> FULL OUTER JOIN <Set B> ON <Join Condition>` — Designates both sets as reserved and adds non matching rows from both, similar to a `LEFT OUTER JOIN` and a `RIGHT OUTER JOIN`.

### APPLY

SQL Server also supports the `APPLY` operator, which is somewhat similar to a join. However, `APPLY` operators enable the creation of a correlation between `<Set A>` and `<Set B>` such as that `<Set B>` may consist of a subquery, a `VALUES` row value constructor, or a table valued function that is evaluated for each row of `<Set A>` where the `<Set B>` query can reference columns from the current row in `<Set A>`. This functionality isn’t possible with any type of standard `JOIN` operator.

There are two `APPLY` types:

- `<Set A> CROSS APPLY <Set B>` — Similar to a `CROSS JOIN` in the sense that every row from `<Set A>` is matched with every row from `<Set B>`.
- `<Set A> OUTER APPLY <Set B>` — Similar to a `LEFT OUTER JOIN` in the sense that rows from `<Set A>` are returned even if the sub query for `<Set B>` produces an empty set. In that case, NULL is assigned to all columns of `<Set B>`.

### ANSI SQL 89 JOIN Syntax

Up until SQL Server version 2008 R2, SQL Server also supported the old style `JOIN` syntax including `LEFT` and` RIGHT OUTER JOIN`.

The ANSI syntax for a `CROSS JOIN` operator was to list the sets in the `FROM` clause using commas as separators. Consider the following example:

```
SELECT *
FROM Table1,
    Table2,
    Table3...
```

To perform an `INNER JOIN`, you only needed to add the `JOIN` predicate as part of the `WHERE` clause. Consider the following example:

```
SELECT *
FROM Table1,
    Table2
WHERE Table1.Column1 = Table2.Column1
```

Although the ANSI standard didn’t specify outer joins at the time, most RDBMS supported them in one way or another. T-SQL supported outer joins by adding an asterisk to the left or the right of equality sign of the join predicate to designate the reserved table. Consider the following example:

```
SELECT *
FROM Table1,
    Table2
WHERE Table1.Column1 *= Table2.Column1
```

To perform a `FULL OUTER JOIN`, asterisks were placed on both sides of the equality sign of the join predicate.

As of SQL Server 2008R2, outer joins using this syntax have been deprecated. For more information, see [Deprecated Database Engine Features in SQL Server 2008 R2](<https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143729(v=sql.105)> "https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143729(v=sql.105)") in the _SQL Server documentation_.

###### Note

Even though inner joins using the ANSI SQL 89 syntax are still supported, they are highly discouraged due to being notorious for introducing hard to catch programming bugs.

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

Create the `Orders` and `Items` tables.

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
SELECT Item
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

```
Result:
Col1  COl2  Col1  COl2
1     A     NULL  NULL
2     B     2     BB
NULL NULL 3 CC
```

For more information, see [FROM clause plus JOIN, APPLY, PIVOT (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/queries/from-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/queries/from-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) supports the following types of joins in the same way as SQL Server, except for `FULL OUTER JOIN`:

- `<Set A> CROSS JOIN <Set B>` — Results in a Cartesian product of the two sets. Every `JOIN` starts as a Cartesian product.
- `<Set A> INNER JOIN <Set B> ON <Join Condition>` — Filters the Cartesian product to only the rows where the join predicate evaluates to `TRUE`.
- `<Set A> LEFT OUTER JOIN <Set B> ON <Join Condition>` — Adds to the `INNER JOIN` all the rows from the reserved left set with NULL for all the columns that come from the right set.
- `<Set A> RIGHT OUTER JOIN <Set B> ON <Join Condition>` — Adds to the `INNER JOIN` all the rows from the reserved right set with NULL for all the columns that come from the left set.

In addition, Aurora MySQL supports the following join types not supported by SQL Server:

- `<Set A> NATURAL [INNER | LEFT OUTER | RIGHT OUTER ] JOIN <Set B>` — Implicitly assumes that the join predicate consists of all columns with the same name from `<Set A>` and `<Set B>`.
- `<Set A> STRAIGHT_JOIN <Set B>` — Forces `<Set A>` to be read before `<Set B>` and is used as an optimizer hint.

Aurora MySQL also supports the `USING` clause as an alternative to the `ON` clause. The `USING` clause consists of a list of comma separated columns that must appear in both tables. The join predicate is the equivalent of an `AND` logical operator for equality predicates of each column. For example, the following two joins are equivalent:

```
FROM Table1
    INNER JOIN
    Table2
    ON Table1.Column1 = Table2.column1;
```

```
FROM Table1
    INNER JOIN
    Table2
    USING (Column1);
```

If `Column1` is the only column with a common name between `Table1` and `Table2`, the following statement is also equivalent:

```
FROM Table1
    NATURAL JOIN
    Table2
```

###### Note

Aurora MySQL supports the ANSI SQL 89 syntax for joins using commas in the `FROM` clause, but only for inner joins.

###### Note

Aurora MySQL supports neither `APPLY` nor the equivalent `LATERAL JOIN` used by some other database engines.

### Syntax

```
FROM
    <Table Source 1> CROSS JOIN <Table Source 2>
    | <Table Source 1> INNER JOIN <Table Source 2>
        ON <Join Predicate> | USING (Equality Comparison Column List)
    | <Table Source 1> {LEFT|RIGHT} [OUTER] JOIN <Table Source 2>
        ON <Join Predicate> | USING (Equality Comparison Column List)
    | <Table Source 1> NATURAL [INNER | {LEFT|RIGHT} [OUTER]] JOIN <Table Source 2>
    | <Table Source 1> STRAIGHT_JOIN <Table Source 2>
    | <Table Source 1> STRAIGHT_JOIN <Table Source 2>
        ON <Join Predicate>
```

### Migration Considerations

For most joins, the syntax should be equivalent and no rewrites should be needed.

- `CROSS JOIN` using either ANSI SQL 89 or ANSI SQL 92 syntax.
- `INNER JOIN` using either ANSI SQL 89 or ANSI SQL 92 syntax.
- `OUTER JOIN` using the ANSI SQL 92 syntax only.

`FULL OUTER JOIN` and `OUTER JOIN` using the pre-ANSI SQL 92 syntax aren’t supported, but they can be easily worked around.

`CROSS APPLY` and `OUTER APPLY` aren’t supported and need to be rewritten.

### Examples

Create the `Orders` and `Items` tables.

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

**INNER JOIN and OUTER JOIN**

```
SELECT *
FROM Items AS I
    INNER JOIN
    OrderItems AS OI
    ON I.Item = OI.Item;

-- ANSI SQL 89
SELECT *
FROM Items AS I,
    Orders AS O
WHERE I.Item = OI.Item;
```

**LEFT OUTER JOIN**

```
SELECT Item
FROM Items AS I
    LEFT OUTER JOIN
    OrderItems AS OI
    ON I.Item = OI.Item
WHERE OI.OrderID IS NULL;
```

**Rewrite for FULL OUTER JOIN**

```
CREATE TABLE T1(Col1 INT, COl2 CHAR(2));
CREATE TABLE T2(Col1 INT, COl2 CHAR(2));

INSERT INTO T1 (Col1, Col2)
VALUES (1, 'A'), (2,'B');

INSERT INTO T2 (Col1, Col2)
VALUES (2,'BB'), (3,'CC');

SELECT *
FROM T1
    LEFT OUTER JOIN
    T2
    ON T1.Col1 = T2.Col1
UNION ALL
SELECT NULL, NULL, Col1, Col2
FROM T2
WHERE Col1 NOT IN (SELECT Col1 FROM T1);
```

```
Result:
Col1  COl2  Col1  COl2
1     A     NULL  NULL
2     B     2     BB
NULL  NULL  3     CC
```

## Summary

Table of similarities, differences, and key migration considerations.

| SQL Server                              | Aurora MySQL    | Comments                                                                 |
| --------------------------------------- | --------------- | ------------------------------------------------------------------------ |
| `INNER JOIN` with `ON` clause or commas | Supported       |                                                                          |
| `OUTER JOIN` with `ON` clause           | Supported       |                                                                          |
| `OUTER JOIN` with commas                | Not supported   | Requires T-SQL rewrite post SQL Server 2008 R2.                          |
| `CROSS JOIN` or using commas            | Supported       |                                                                          |
| `CROSS APPLY` and `OUTER APPLY`         | Not Supported   | Rewrite required.                                                        |
| Not Supported                           | `NATURAL JOIN`  | Not recommended, may cause unexpected issues if table structure changes. |
| Not Supported                           | `STRAIGHT_JOIN` |                                                                          |
| Not Supported                           | `USING` clause  |                                                                          |

For more information, see [JOIN Clause](https://dev.mysql.com/doc/refman/5.7/en/join.html "https://dev.mysql.com/doc/refman/5.7/en/join.html") in the _MySQL documentation_.
