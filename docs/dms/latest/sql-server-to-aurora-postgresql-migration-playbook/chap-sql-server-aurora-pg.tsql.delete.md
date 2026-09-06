

# Delete and update from for T-SQL
<a name="chap-sql-server-aurora-pg.tsql.delete"></a>

This topic provides reference information about feature compatibility between Microsoft SQL Server 2019 and Amazon Aurora PostgreSQL, specifically focusing on DELETE and UPDATE statements with JOINs. You can understand the differences in syntax and functionality when migrating from SQL Server to Aurora PostgreSQL. The topic highlights that while SQL Server supports an extended syntax for DELETE and UPDATE statements with additional FROM clauses, Aurora PostgreSQL has limitations in this area.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-compatibility-3.png)  |  ![Three star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-automation-3.png)  | N/A | PostgreSQL doesn’t support `DELETE …​ FROM from_list`. Rewrite to use subqueries. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-pg.tsql.delete.sqlserver"></a>

SQL Server supports an extension to the ANSI standard that allows using an additional `FROM` clause in `UPDATE` and `DELETE` statements.

You can use this additional `FROM` clause to limit the number of modified rows by joining the table being updated, or deleted from, to one or more other tables. This functionality is similar to using a WHERE clause with a derived table sub-query. For `UPDATE`, you can use this syntax to set multiple column values simultaneously without repeating the sub-query for every column.

However, these statements can introduce logical inconsistencies if a row in an updated table is matched to more than one row in a joined table. The current implementation chooses an arbitrary value from the set of potential values and is non-deterministic.

### Syntax
<a name="chap-sql-server-aurora-pg.tsql.delete.sqlserver.syntax"></a>

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
<a name="chap-sql-server-aurora-pg.tsql.delete.sqlserver.examples"></a>

The following example deletes customers with no orders.

```
CREATE TABLE Customers
(
  Customer VARCHAR(20) PRIMARY KEY
);
```

```
INSERT INTO Customers VALUES
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
INSERT INTO Orders (OrderID, Customer, OrderDate) VALUES
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

```
Customer
Jim
Jack
```

The following example updates multiple columns in Orders based on the values in OrderCorrections.

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
  ON O.OrderID = OC.OrderID;
```

```
SELECT *
FROM Orders;
```

```
Customer  OrderDate
Jack      2018-03-24
Jack      2018-04-02
```

For more information, see [UPDATE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/queries/update-transact-sql?view=sql-server-ver15), [DELETE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/delete-transact-sql?view=sql-server-ver15), and [FROM clause plus JOIN, APPLY, PIVOT (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/queries/from-transact-sql?view=sql-server-ver15) in the *SQL Server documentation*.

## PostgreSQL Usage
<a name="chap-sql-server-aurora-pg.tsql.delete.pg"></a>

 Aurora PostgreSQL doesn’t support the `DELETE..FROM` syntax, but it support the `UPDATE FROM` syntax.

### Syntax
<a name="chap-sql-server-aurora-pg.tsql.delete.pg.syntax"></a>

```
[ WITH [ RECURSIVE ] with_query [, ...] ]
UPDATE [ ONLY ] table_name [ * ] [ [ AS ] alias ]
  SET { column_name = { expression | DEFAULT } |
    ( column_name [, ...] ) = ( { expression | DEFAULT } [, ...] ) |
    ( column_name [, ...] ) = ( sub-SELECT )
  } [, ...]
  [ FROM from_list ]
  [ WHERE condition | WHERE CURRENT OF cursor_name ]
  [ RETURNING * | output_expression [ [ AS ] output_name ] [, ...] ]
```

### Migration Considerations
<a name="chap-sql-server-aurora-pg.tsql.delete.pg.considerations"></a>

You can rewrite the `DELETE` statements as subqueries. Place the subqueries in the WHERE clause. This workaround is simple and, in most cases, easier to read and understand.

### Examples
<a name="chap-sql-server-aurora-pg.tsql.delete.pg.examples"></a>

The following example deletes customers with no orders.

```
CREATE TABLE Customers
(
  Customer VARCHAR(20) PRIMARY KEY
);

INSERT INTO Customers
VALUES
('John'),
('Jim'),
('Jack')

CREATE TABLE Orders
(
  OrderID INT NOT NULL PRIMARY KEY,
  Customer VARCHAR(20) NOT NULL,
  OrderDate DATE NOT NULL
);

INSERT INTO Orders (OrderID, Customer, OrderDate)
VALUES
(1, 'Jim', '20180401'),
(2, 'Jack', '20180402');

DELETE FROM Customers
WHERE Customer NOT IN (
  SELECT Customer
  FROM Orders
);

SELECT * FROM Customers;

Customer
Jim
Jack
```

The following example updates multiple columns in Orders based on the values in OrderCorrections

```
CREATE TABLE OrderCorrections
(
  OrderID INT NOT NULL PRIMARY KEY,
  Customer VARCHAR(20) NOT NULL,
  OrderDate DATE NOT NULL
);

INSERT INTO OrderCorrections
VALUES (1, 'Jack', '20180324');

UPDATE orders
SET Customer = OC.Customer,
  OrderDate = OC.OrderDate
FROM Orders AS O
  INNER JOIN
  OrderCorrections AS OC
  ON O.OrderID = OC.OrderID;

SELECT *
FROM Orders;

Customer  OrderDate
Jack      2018-03-24
Jack      2018-04-02
```

## Summary
<a name="chap-sql-server-aurora-pg.tsql.delete.summary"></a>

The following table identifies similarities, differences, and key migration considerations.


| Feature | SQL Server |  Aurora PostgreSQL  | 
| --- | --- | --- | 
| Join as part of `DELETE`  |  `DELETE FROM …​ FROM`  | Not available. Rewrite to use WHERE clause with a sub-query. | 
| Join as part of `UPDATE`  |  `UPDATE …​ FROM`  |  `UPDATE …​ FROM`  | 

For more information, see [DELETE](https://www.postgresql.org/docs/13/sql-delete.html) and [UPDATE](https://www.postgresql.org/docs/13/sql-update.html) in the *PostgreSQL documentation*.