

# Common table expressions for ANSI SQL
<a name="chap-sql-server-aurora-pg.sql.cte"></a>

This topic provides reference information about Common Table Expressions (CTEs) in both SQL Server and PostgreSQL. It explains that CTEs are part of the ANSI SQL standard and are used to simplify queries and improve readability by defining temporary views or derived tables. The topic highlights the similarities between SQL Server and PostgreSQL implementations of CTEs, including their support for recursive functionality.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Five star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-compatibility-5.png)  |  ![Five star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-automation-5.png)  | N/A | Use `RECURSIVE` keyword for recursive CTE queries. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-pg.sql.cte.sqlserver"></a>

Common Table Expressions (CTE) are part of the ANSI standard since SQL:1999, simplify queries and make them more readable by defining a temporary view, or derived table, that a subsequent query can reference. You can use SQL Server CTEs as the target of DML modification statements. They have similar restrictions as updateable views.

SQL Server CTEs provide recursive functionality in accordance with the ANSI 99 standard. Recursive CTEs can reference themselves and re-run queries until the data set is exhausted, or the maximum number of iterations is exceeded.

### CTE Syntax
<a name="chap-sql-server-aurora-pg.sql.cte.sqlserver.syntax"></a>

```
WITH <CTE NAME>
AS
(
SELECT ....
)
SELECT ...
FROM CTE
```

### Recursive CTE Syntax
<a name="chap-sql-server-aurora-pg.sql.cte.sqlserver.recursivesyntax"></a>

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
<a name="chap-sql-server-aurora-pg.sql.cte.sqlserver.examples"></a>

Create and populate an OrderItems table.

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

Define a CTE to calculate the total quantity in every order and then join to the OrderItems table to obtain the relative quantity for each item.

```
WITH AggregatedOrders
AS
( SELECT OrderID, SUM(Quantity) AS TotalQty
FROM OrderItems
GROUP BY OrderID
)
SELECT O.OrderID, O.Item,
O.Quantity,
(O.Quantity / AO.TotalQty) * 100 AS PercentOfOrder
FROM OrderItems AS O
INNER JOIN
AggregatedOrders AS AO
ON O.OrderID = AO.OrderID;
```

The preceding example produces the following results.

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

The preceding example produces the following results.

```
LVL  Employee  DirectManager
0    Dave      NULL
1    John      Dave
1    Jose      Dave
2    Fred      John
```

For more information, see [Recursive Queries Using Common Table Expressions](https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms186243(v=sql.105)?redirectedfrom=MSDN) in the *SQL Server documentation*.

## PostgreSQL Usage
<a name="chap-sql-server-aurora-pg.sql.cte.pg"></a>

PostgreSQL conforms to the ANSI SQL-99 standard and implementing CTEs in PostgreSQL is similar to SQL Server.

CTE is also known as `WITH` query. This type of query helps you to simplify long queries, it is similar to defining temporary tables that exist only for the running of the query. The statement in a WITH clause can be a `SELECT`, `INSERT`, `UPDATE`, or `DELETE`, and the `WITH` clause itself is attached to a primary statement that can also be a `SELECT`, `INSERT`, `UPDATE`, or `DELETE`.

### CTE Syntax
<a name="chap-sql-server-aurora-pg.sql.cte.pg.syntax"></a>

```
WITH <CTE NAME>
AS
(
SELECT OR DML
)
SELECT OR DML
Recursive CTE
```

### Recursive CTE Syntax
<a name="chap-sql-server-aurora-pg.sql.cte.pg.recursivesyntax"></a>

```
WITH RECURSIVE <CTE NAME>
AS (
<Anchor SELECT query>
UNION ALL
<Recursive SELECT query with reference to <CTE NAME>>
)
SELECT OR DML
```

### Examples
<a name="chap-sql-server-aurora-pg.sql.cte.pg.examples"></a>

Create and populate an OrderItems table.

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

Create a CTE.

```
WITH DEPT_COUNT
  (DEPARTMENT_ID, DEPT_COUNT) AS (
    SELECT DEPARTMENT_ID, COUNT(*) FROM EMPLOYEES GROUP BY DEPARTMENT_ID)
    SELECT E.FIRST_NAME ||' '|| E.LAST_NAME AS EMP_NAME,
    D.DEPT_COUNT AS EMP_DEPT_COUNT
    FROM EMPLOYEES E JOIN DEPT_COUNT D USING (DEPARTMENT_ID) ORDER BY 2;
```

PostgreSQL provides an additional feature when using a CTE as a recursive modifier. The following example uses a recursive WITH clause to access its own result set.

```
WITH RECURSIVE t(n) AS (
  VALUES (0)
  UNION ALL
  SELECT n+1 FROM t WHERE n < 5)
  SELECT * FROM t;

WITH RECURSIVE t(n) AS (
VALUES (0)
UNION ALL
SELECT n+1 FROM t WHERE n < 5)

SELECT * FROM t;

n
0
...
5
```

Note that using the SQL Server example will get undesired results.

Define a CTE to calculate the total quantity in every order and then join to the OrderItems table to obtain the relative quantity for each item.

```
WITH AggregatedOrders
AS
( SELECT OrderID, SUM(Quantity) AS TotalQty
  FROM OrderItems
  GROUP BY OrderID
)
SELECT O.OrderID, O.Item,
  O.Quantity,
    (O.Quantity / AO.TotalQty) * 100 AS PercentOfOrder
FROM OrderItems AS O
  INNER JOIN
  AggregatedOrders AS AO
  ON O.OrderID = AO.OrderID;
```

The preceding example produces the following results.

```
OrderID  Item       Quantity  PercentOfOrder
1        M8 Bolt    100       100
2        M8 Nut     100       100
3        M8 Washer  100       0
3        M6 Washer  200       0
```

This is because when you divide `INT` by `INT`, you get a round result. If you use another data type such as `DECIMAL`, there will be no problem. To fix the current issue, cast the columns using `::decimal`.

```
AS
( SELECT OrderID, SUM(Quantity) AS TotalQty
  FROM OrderItems
  GROUP BY OrderID
)
SELECT O.OrderID, O.Item,
  O.Quantity,
  trunc((O.Quantity::decimal / AO.TotalQty::decimal)*100,2) AS PercentOfOrder
  FROM OrderItems AS O
  INNER JOIN
  AggregatedOrders AS AO
  ON O.OrderID = AO.OrderID;
```

The preceding example produces the following results.

```
OrderID  Item       Quantity  PercentOfOrder
1        M8 Bolt    100       100
2        M8 Nut     100       100
3        M8 Washer  100       33.33
3        M6 Washer  200       66.66
```

Unlike in SQL Server, for `RECURSIVE WITH` query, use the `RECURSIVE` keyword in PostgreSQL.

Use a recursive CTE to display the employee-management hierarchy.

```
WITH RECURSIVE EmpHierarchyCTE AS
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

The preceding example produces the following results.

```
LVL  Employee  DirectManager
0    Dave
1    John      Dave
1    Jose      Dave
2    Fred      John
```

For more information, see [WITH Queries (Common Table Expressions)](https://www.postgresql.org/docs/13/queries-with.html) in the *PostgreSQL documentation*.