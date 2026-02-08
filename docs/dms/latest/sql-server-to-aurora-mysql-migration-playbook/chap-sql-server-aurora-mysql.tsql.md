# DELETE and UPDATE FROM for T-SQL

This topic provides reference information about the differences in SQL syntax and functionality between Microsoft SQL Server 2019 and Amazon Aurora MySQL, specifically regarding DELETE and UPDATE statements with joins. You can use this information to understand how to adapt your existing SQL Server queries when migrating to Aurora MySQL.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences            |
| ------------------------------- | ---------------------------------- | ------------------------- | -------------------------- |
| Four star feature compatibility | Four star automation level         | N/A                       | Rewrite to use subqueries. |

## SQL Server Usage

SQL Server supports an extension to the ANSI standard that allows using an additional `FROM` clause in `UPDATE` and `DELETE` statements.

You can use this additional `FROM` clause to limit the number of modified rows by joining the table being updated, or deleted from, to one or more other tables. This functionality is similar to using a `WHERE` clause with a derived table subquery. For `UPDATE`, you can use this syntax to set multiple column values simultaneously without repeating the subquery for every column.

However, these statements can introduce logical inconsistencies if a row in an updated table is matched to more than one row in a joined table. The current implementation chooses an arbitrary value from the set of potential values and is non deterministic.

### Syntax

```
UPDATE <Table Name>
SET <Column Name> = <Expression> ,...
FROM <Table Source>
WHERE <Filter Predicate>;
```

```
DELETE FROM <Table Name>
FROM <Table Source>
WHERE <Filter Predicate>;
```

### Examples

Delete customers with no orders.

```
CREATE TABLE Customers
(
    Customer VARCHAR(20) PRIMARY KEY
);
```

```
INSERT INTO Customers
VALUES
('John'),
('Jim'),
('Jack')
```

```
CREATE TABLE Orders
(
    OrderID INT NOT NULL PRIMARY KEY,
    Customer VARCHAR(20) NOT NULL,
    OrderDate DATE NOT NULL
);
```

```
INSERT INTO Orders (OrderID, Customer, OrderDate)
VALUES
(1, 'Jim', '20180401'),
(2, 'Jack', '20180402');
```

```
DELETE FROM Customers
FROM Customers AS C
    LEFT OUTER JOIN
    Orders AS O
    ON O.Customer = C.Customer
WHERE O.OrderID IS NULL;
```

```
SELECT *
FROM Customers;
```

For the preceding examples, the result looks as shown following.

```
Customer

Jim
Jack
```

Update multiple columns in `Orders` based on the values in `OrderCorrections`.

```
CREATE TABLE OrderCorrections
(
    OrderID INT NOT NULL PRIMARY KEY,
    Customer VARCHAR(20) NOT NULL,
    OrderDate DATE NOT NULL
);
```

```
INSERT INTO OrderCorrections
VALUES (1, 'Jack', '20180324');
```

```
UPDATE O
SET Customer = OC.Customer,
    OrderDate = OC.OrderDate
FROM Orders AS O
    INNER JOIN
    OrderCorrections AS OC
    ON O.OrderID = OD.OrderID;
```

```
SELECT *
FROM Orders;
```

For the preceding example, the result looks as shown following.

```
Customer  OrderDate
Jack      2018-03-24
Jack      2018-04-02
```

For more information, see [UPDATE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/queries/update-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/queries/update-transact-sql?view=sql-server-ver15"), [DELETE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/delete-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/delete-transact-sql?view=sql-server-ver15"), and [FROM clause plus JOIN, APPLY, PIVOT (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/queries/from-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/queries/from-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) doesn’t support `DELETE` and `UPDATE FROM` syntax.

### Migration Considerations

You can easily rewrite the `DELETE` and `UPDATE FROM` statements as subqueries.

For `DELETE`, place the subqueries in the `WHERE` clause.

For `UPDATE`, place the subqueries either in the `WHERE` or `SET` clause.

###### Note

When rewriting `UPDATE FROM` queries, include a `WHERE` clause to limit which rows are updated even if the SQL Server version (where the rows were limited by the join condition) did not have one.

For `DELETE` statements, the workaround is simple and, in most cases, easier to read and understand.

For `UPDATE` statements, the workaround involves repeating the correlated subquery for each column being set.

Although this approach makes the code longer and harder to read, it does solve the logical challenges associated with updates having multiple matched rows in the joined tables.

In the current implementation, the SQL Server engine silently chooses an arbitrary value if more than one value exists for the same row.

When you rewrite the statement to use a correlated subquery, such as in the following example, if more than one value is returned from the sub query, a SQL error will be raised: `SQL Error [1242] [21000]: Subquery returns more than 1 row`.

Consult the documentation for the Aurora MySQL
`UPDATE` statement as there are significant processing differences from SQL Server. For example:

- In Aurora MySQL, you can update multiple tables in a single `UPDATE` statement.
- `UPDATE` expressions are evaluated in order from left to right. This behavior differs from SQL Server and the ANSI standard, which require an all-at-once evaluation.

For example, in the statement `UPDATE Table SET Col1 = Col1 + 1, Col2 = Col1`, `Col2` is set to the new value of `Col1`. The end result is `Col1 = Col2`.

### Examples

Delete customers with no orders.

```
CREATE TABLE Customers
(
    Customer VARCHAR(20) PRIMARY KEY
);
```

```
INSERT INTO Customers
VALUES
('John'),
('Jim'),
('Jack')
```

```
CREATE TABLE Orders
(
    OrderID INT NOT NULL PRIMARY KEY,
    Customer VARCHAR(20) NOT NULL,
    OrderDate DATE NOT NULL
);
```

```
INSERT INTO Orders (OrderID, Customer, OrderDate)
VALUES
(1, 'Jim', '20180401'),
(2, 'Jack', '20180402');
```

```
DELETE FROM Customers
WHERE Customer NOT IN (
    SELECT Customer
    FROM Orders
);
```

```
SELECT *
FROM Customers;
```

For the preceding example, the result looks as shown following.

```
Customer

Jim
Jack
```

Update multiple columns in `Orders` based on the values in `OrderCorrections`.

```
CREATE TABLE OrderCorrections
(
    OrderID INT NOT NULL PRIMARY KEY,
    Customer VARCHAR(20) NOT NULL,
    OrderDate DATE NOT NULL
);
```

```
INSERT INTO OrderCorrections
VALUES (1, 'Jack', '20180324');
```

```
UPDATE Orders
SET Customer = (
    SELECT Customer
    FROM OrderCorrections AS OC
    WHERE Orders.OrderID = OC.OrderID
),
OrderDate = (
    SELECT OrderDate
    FROM OrderCorrections AS OC
    WHERE Orders.OrderID = OC.OrderID
IN (
    SELECT OrderID
    FROM OrderCorrections
);
```

```
SELECT *
FROM Orders;
```

For the preceding example, the result looks as shown following.

```
Customer  OrderDate
Jack      2018-03-24
Jack      2018-04-02
```

## Summary

The following table identifies similarities, differences, and key migration considerations.

| Feature                  | SQL Server            | Aurora MySQL | Comments                                                                                                |
| ------------------------ | --------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
| Join as part of `DELETE` | `DELETE FROM …​ FROM` | N/A          | Rewrite to use the `WHERE` clause with a subquery.                                                      |
| Join as part of `UPDATE` | `UPDATE …​ FROM`      | N/A          | Rewrite to use correlated subquery in the `SET` clause and add the `WHERE` clause to limit updates set. |

For more information, see [UPDATE Statement](https://dev.mysql.com/doc/refman/5.7/en/update.html "https://dev.mysql.com/doc/refman/5.7/en/update.html") and [DELETE Statement](https://dev.mysql.com/doc/refman/5.7/en/delete.html "https://dev.mysql.com/doc/refman/5.7/en/delete.html") in the _MySQL documentation_.
