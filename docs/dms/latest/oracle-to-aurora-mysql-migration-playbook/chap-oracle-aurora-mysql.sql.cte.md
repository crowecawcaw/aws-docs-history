

# Oracle and MySQL Common Table Expressions
<a name="chap-oracle-aurora-mysql.sql.cte"></a>

The following sections provide details on defining and leveraging Common Table Expressions (CTEs) within AWS DMS to streamline database operations and enhance query performance.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Two star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-2.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  |  [Common Table Expressions](chap-oracle-aurora-mysql.tools.actioncode.md#chap-oracle-aurora-mysql.tools.actioncode.commontableexpressions)  | MySQL doesn’t support common table expressions. A workaround is available. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.sql.cte.oracle"></a>

CTEs provide a way to implement the logic of sequential code or to reuse code. You can define a named sub query and then use it multiple times in different parts of a query statement.

A CTE is implemented using a `WITH` clause, which is part of the ANSI SQL-99 standard and has existed in Oracle since version 9.2. CTE usage is similar to an inline view or a temporary table. Its main purpose is to reduce query statement repetition and make complex queries simpler to read and understand.

### Syntax
<a name="chap-oracle-aurora-mysql.sql.cte.oracle.syntax"></a>

```
WITH <subquery name> AS (<subquery code>)[...]
SELECT <Select list> FROM <subquery name>;
```

### Examples
<a name="chap-oracle-aurora-mysql.sql.cte.oracle.examples"></a>

The following example creates a sub query of the employee count for each department and then use the result set of the CTE in a query.

```
WITH DEPT_COUNT
(DEPARTMENT_ID, DEPT_COUNT) AS
(SELECT DEPARTMENT_ID, COUNT(*)
FROM EMPLOYEES
GROUP BY DEPARTMENT_ID)
SELECT E.FIRST_NAME ||' '|| E.LAST_NAME AS EMP_NAME,
D.DEPT_COUNT AS EMP_DEPT_COUNT
FROM EMPLOYEES E JOIN DEPT_COUNT D
USING (DEPARTMENT_ID)
ORDER BY 2;
```

## MySQL usage
<a name="chap-oracle-aurora-mysql.sql.cte.mysql"></a>

Aurora MySQL 5.7 doesn’t support common table expressions (CTE).

**Note**  
 Amazon Relational Database Service (Amazon RDS) for MySQL version 8 supports common table expressions both non-recursive and recursive. Common table expressions enable use of named temporary result sets implemented by permitting a `WITH` clause preceding `SELECT` statements and certain other statements. For more information, see [WITH (Common Table Expressions)](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/with.html). As of MySQL 8.0.19, the recursive `SELECT` part of a recursive common table expression (CTE) supports a `LIMIT` clause. `LIMIT` with `OFFSET` is also supported. For more information, see [Recursive Common Table Expressions](https://dev.mysql.com/doc/refman/8.0/en/with.html#common-table-expressions-recursive).

### Migration considerations
<a name="chap-oracle-aurora-mysql.sql.cte.mysql.considerations"></a>

As a workaround, use views or derived tables in place of non-recursive CTEs. Since non-recursive CTEs are more convenient for readability and code simplification, you can convert the code to use derived tables, which are a subquery in the parent query’s `FROM` clause. For example, replace the following CTE:

```
WITH TopCustomerOrders
( SELECT Customer, COUNT(*) AS NumOrders
    FROM Orders
    GROUP BY Customer
)
SELECT TOP 10 * FROM TopCustomerOrders ORDER BY NumOrders DESC;
```

With the following subquery:

```
SELECT *
FROM ( SELECT Customer, COUNT(*) AS NumOrders
    FROM Orders
    GROUP BY Customer ) AS TopCustomerOrders
ORDER BY NumOrders DESC
LIMIT 10 OFFSET 0;
```

When you use derived tables, make sure that the derived table definition is repeated if multiple instances are required for the query.

Converting the code for recursive CTEs is not straight forward, but you can achieve similar functionality using loops.

### Examples
<a name="chap-oracle-aurora-mysql.sql.cte.mysql.examples"></a>

 **Replacing non-recursive CTEs** 

Use a derived table to replace non-recursive CTE functionality as follows:

The following example creates and populates an `OrderItems` table.

```
CREATE TABLE OrderItems(
    OrderID INT NOT NULL, Item VARCHAR(20) NOT NULL,
    Quantity SMALLINT NOT NULL,
    PRIMARY (OrderID, Item));

INSERT INTO OrderItems (OrderID, Item, Quantity)
VALUES (1, 'M8 Bolt', 100), (2, 'M8 Nut', 100),
(3, 'M8 Washer', 200), (3, 'M6 Washer', 100);
```

Define a derived table for `TotalQty` of every order and then join to the `OrderItems` to obtain the relative quantity for each item.

```
SELECT O.OrderID, O.Item, O.Quantity, (O.Quantity / AO.TotalQty) * 100 AS PercentOfOrder
FROM OrderItems AS O
    INNER JOIN
    ( SELECT OrderID, SUM(Quantity) AS TotalQty
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
Stored procedure and function recursion in Aurora MySQL is turned off by default. You can set the server system variable `max_sp_recursion_depth` to a value of 1 or higher to turn on recursion. However, this approach is not recommended because it may increase contention for the thread stack space.

The following example creates and populates an Employees table.

```
CREATE TABLE Employees
( Employee VARCHAR(5) NOT NULL PRIMARY KEY,
    DirectManager VARCHAR(5) NULL);

INSERT INTO Employees (Employee, DirectManager)
VALUES ('John', 'Dave'), ('Jose', 'Dave'),
('Fred', 'John'), ('Dave', NULL);
```

The following example creates an `EmpHierarcy` table.

```
CREATE TABLE EmpHierarchy (LVL INT, Employee VARCHAR(5), Manager VARCHAR(5));
```

The following example creates a procedure that uses a loop to traverse the employee hierarchy.

```
CREATE PROCEDURE P()
BEGIN
DECLARE var_lvl INT;
DECLARE var_Employee VARCHAR(5);
SET var_lvl = 0;
SET var_Employee = (SELECT Employee FROM Employees WHERE DirectManager IS NULL);
INSERT INTO EmpHierarchy VALUES (var_lvl, var_Employee, NULL);
WHILE var_lvl <> -1
DO
INSERT INTO EmpHierarchy (LVL, Employee, Manager)
SELECT var_lvl + 1, Employee, DirectManager
FROM Employees
WHERE DirectManager IN (SELECT Employee FROM EmpHierarchy WHERE LVL = var_lvl);
IF NOT EXISTS (SELECT * FROM EmpHierarchy WHERE LVL = var_lvl + 1)
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

Level  Employee  Manager
0      Dave
1      John      Dave
1      Jose      Dave
2      Fred      John
```

## Summary
<a name="chap-oracle-aurora-mysql.sql.cte.summary"></a>


| Oracle | Aurora MySQL | Comments | 
| --- | --- | --- | 
| Non-recursive CTE | Derived table | For multiple instances of the same table, the derived table definition subquery must be repeated. | 
| Recursive CTE | Loop inside a stored procedure or stored function. |  | 

For more information, see [WITH (Common Table Expressions)](https://dev.mysql.com/doc/refman/8.0/en/with.html) in the *MySQL documentation*.