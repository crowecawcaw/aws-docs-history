

# Common table expressions for ANSI SQL
<a name="chap-sql-server-aurora-mysql.sql.cte"></a>

This topic provides reference information about Common Table Expressions (CTEs) and their compatibility between Microsoft SQL Server 2019 and Amazon Aurora MySQL. You can understand the differences in CTE support between these database systems, which is crucial when migrating from SQL Server to Aurora MySQL.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Two star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-compatibility-2.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  |  [Common Table Expressions](chap-sql-server-aurora-mysql.tools.actioncode.md#chap-sql-server-aurora-mysql.tools.actioncode.commontableexpressions)  | Rewrite non-recursive CTE to use views and derived tables. Redesign recursive CTE code. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-mysql.sql.cte.sqlserver"></a>

Common Table Expressions (CTE), which have been a part of the ANSI standard since SQL:1999, simplify queries and make them more readable by defining a temporary view, or derived table, that a subsequent query can reference. SQL Server CTEs can be the target of DML modification statements and have similar restrictions as updateable views.

SQL Server CTEs provide recursive functionality in accordance with the ANSI 99 standard. Recursive CTEs can reference themselves and re-run queries until the data set is exhausted, or the maximum number of iterations is exceeded.

### Simplified CTE Syntax
<a name="chap-sql-server-aurora-mysql.sql.cte.sqlserver.simplified"></a>

```
WITH <CTE NAME>
AS
(
SELECT ....
)
SELECT ...
FROM CTE
```

### Recursive CTE syntax
<a name="chap-sql-server-aurora-mysql.sql.cte.sqlserver.recursive"></a>

```
WITH <CTE NAME>
AS (
<Anchor SELECT query>
UNION ALL
<Recursive SELECT query with reference to <CTE NAME>>
)
SELECT ... FROM <CTE NAME>...
```

### Examples
<a name="chap-sql-server-aurora-mysql.sql.cte.sqlserver.examples"></a>

Create and populate an `OrderItems` table.

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
(3, 'M6 Washer', 100);
```

Define a CTE to calculate the total quantity in every order and then join to the `OrderItems` table to obtain the relative quantity for each item.

```
WITH AggregatedOrders
AS
(
    SELECT OrderID, SUM(Quantity) AS TotalQty
    FROM OrderItems
    GROUP BY OrderID
)
SELECT O.OrderID, O.Item, O.Quantity,
    (O.Quantity / AO.TotalQty) * 100 AS PercentOfOrder
FROM OrderItems AS O
    INNER JOIN
    AggregatedOrders AS AO
    ON O.OrderID = AO.OrderID;
```

For the preceding example, the result looks as shown following.

```
OrderID  Item       Quantity  PercentOfOrder
1        M8 Bolt    100       100.0000000000
2        M8 Nut     100       100.0000000000
3        M8 Washer  100       33.3333333300
3        M6 Washer  200       66.6666666600
```

Using a recursive CTE, create and populate the `Employees` table with the `DirectManager` for each employee.

```
CREATE TABLE Employees
(
    Employee VARCHAR(5) NOT NULL PRIMARY KEY,
    DirectManager VARCHAR(5) NULL
);
```

```
INSERT INTO Employees(Employee, DirectManager)
VALUES
('John', 'Dave'),
('Jose', 'Dave'),
('Fred', 'John'),
('Dave', NULL);
```

Use a recursive CTE to display the employee-management hierarchy.

```
WITH EmpHierarchyCTE AS
(
-- Anchor query retrieves the top manager
SELECT 0 AS LVL,
    Employee,
    DirectManager
FROM Employees AS E
WHERE DirectManager IS NULL
UNION ALL
-- Recursive query gets all Employees managed by the previous level
SELECT LVL + 1 AS LVL,
    E.Employee,
    E.DirectManager
FROM EmpHierarchyCTE AS EH
INNER JOIN
Employees AS E
ON E.DirectManager = EH.Employee
)
SELECT *
FROM EmpHierarchyCTE;
```

For the preceding example, the result looks as shown following.

```
LVL  Employee  DirectManager
0    Dave      NULL
1    John      Dave
1    Jose      Dave
2    Fred      John
```

For more information, see [Recursive Queries Using Common Table Expressions](https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms186243(v=sql.105)) in the *SQL Server documentation*.

## MySQL Usage
<a name="chap-sql-server-aurora-mysql.sql.cte.mysql"></a>

 Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) 5.7 doesn’t support Common Table Expressions (CTE).

**Note**  
 Amazon Relational Database Service (Amazon RDS) for MySQL 8 supports common table expressions both nonrecursive and recursive. Common table expressions enable use of named temporary result sets implemented by permitting a `WITH` clause preceding `SELECT` statements and certain other statements. As of MySQL 8.0.19, the recursive `SELECT` part of a recursive common table expression supports a `LIMIT` clause. `LIMIT` with `OFFSET` is also supported. For more information, see [Recursive Common Table Expressions](https://dev.mysql.com/doc/refman/8.0/en/with.html#common-table-expressions-recursive) in the *MySQL documentation*.

### Migration Considerations
<a name="chap-sql-server-aurora-mysql.sql.cte.mysql.considerations"></a>

As a workaround, use views or derived tables in place of non-recursive CTEs.

Since non-recursive CTEs are more convenient for readability and code simplification, You can convert the code to use derived tables, which are a subquery in the parent query’s `FROM` clause. For example, replace the following CTE:

```
WITH TopCustomerOrders
(
    SELECT Customer,
    COUNT(*) AS NumOrders
    FROM Orders
    GROUP BY Customer
)
SELECT TOP 10 *
FROM TopCustomerOrders
ORDER BY NumOrders DESC;
```

With the following subquery:

```
SELECT *
FROM (
    SELECT Customer,
    COUNT(*) AS NumOrders
    FROM Orders
    GROUP BY Customer
) AS TopCustomerOrders
ORDER BY NumOrders DESC
LIMIT 10 OFFSET 0;
```

When using derived tables, the derived table definition must be repeated if multiple instances are required for the query.

Converting the code for recursive CTEs isn’t straight forward, but you can achieve similar functionality using loops.

### Examples
<a name="chap-sql-server-aurora-mysql.sql.cte.mysql.examples"></a>

 **Replacing non-recursive CTEs** 

Use a derived table to replace non-recursive CTE functionality as shown following.

Create and populate an `OrderItems` table.

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
(3, 'M6 Washer', 100);
```

Define a derived table for `TotalQty` of every order and then join to the `OrderItems` to obtain the relative quantity for each item.

```
SELECT O.OrderID,
    O.Item,
    O.Quantity,
    (O.Quantity / AO.TotalQty) * 100 AS PercentOfOrder
FROM OrderItems AS O
    INNER JOIN
    (
        SELECT OrderID,
        SUM(Quantity) AS TotalQty
        FROM OrderItems
        GROUP BY OrderID
    ) AS AO
    ON O.OrderID = AO.OrderID;
```

For the preceding example, the result looks as shown following.

```
OrderID  Item       Quantity  PercentOfOrder
1        M8 Bolt    100       100.0000000000
2        M8 Nut     100       100.0000000000
3        M8 Washer  100       33.3333333300
3        M6 Washer  200       66.6666666600
```

 **Replacing recursive CTEs** 

Use recursive SQL code in stored procedures and SQL loops to replace a recursive CTEs.

**Note**  
Stored procedure and function recursion in Aurora MySQL is turned off by default. You can set the server system variable `max_sp_recursion_depth` to a value of 1 or higher to enable recursion. However, this approach isn’t recommended because it may increase contention for the thread stack space.

Create and populate an `Employees` table.

```
CREATE TABLE Employees
(
    Employee VARCHAR(5) NOT NULL PRIMARY KEY,
    DirectManager VARCHAR(5) NULL
);
```

```
INSERT INTO Employees (Employee, DirectManager)
VALUES
('John', 'Dave'),
('Jose', 'Dave'),
('Fred', 'John'),
('Dave', NULL);
```

Create an `EmpHierarchy` table.

```
CREATE TABLE EmpHierarchy
(
    LVL INT,
    Employee VARCHAR(5),
    Manager VARCHAR(5)
);
```

Create a procedure that uses a loop to traverse the employee hierarchy. For more information, see [Stored Procedures](chap-sql-server-aurora-mysql.tsql.storedprocedures.md) and [Flow Control](chap-sql-server-aurora-mysql.tsql.flowcontrol.md).

```
CREATE PROCEDURE P()
BEGIN
DECLARE var_lvl INT;
DECLARE var_Employee VARCHAR(5);
SET var_lvl = 0;
SET var_Employee = (
    SELECT Employee
    FROM Employees |
    WHERE DirectManager IS NULL
);
INSERT INTO EmpHierarchy
VALUES (var_lvl, var_Employee, NULL);
WHILE var_lvl <> -1
DO
INSERT INTO EmpHierarchy (LVL, Employee, Manager)
SELECT var_lvl + 1,
    Employee,
    DirectManager
FROM Employees
WHERE DirectManager IN (
    SELECT Employee
    FROM EmpHierarchy
    WHERE LVL = var_lvl
);
IF NOT EXISTS (
    SELECT *
    FROM EmpHierarchy
    WHERE LVL = var_lvl + 1
)
THEN SET var_lvl = -1;
ELSE SET var_lvl = var_lvl + 1;
END IF;
END WHILE;
END;
```

Run the procedure.

```
CALL P()
```

Select all records from the `EmpHierarchy` table.

```
SELECT * FROM EmpHierarchy;
```

```
Level  Employee  Manager
0      Dave
1      John      Dave
1      Jose      Dave
2      Fred      John
```

## Summary
<a name="chap-sql-server-aurora-mysql.sql.cte.summary"></a>


| SQL Server |  Aurora MySQL  | Comments | 
| --- | --- | --- | 
| Non recursive CTE | Derived table | For multiple instances of the same table, the derived table definition subquery must be repeated. | 
| Recursive CTE | Loop inside a stored procedure or stored function. |  | 

For more information, see [WITH (Common Table Expressions)](https://dev.mysql.com/doc/refman/8.0/en/with.html) in the *MySQL documentation*.