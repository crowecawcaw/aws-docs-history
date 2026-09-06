

# PIVOT and UNPIVOT for T-SQL
<a name="chap-sql-server-aurora-mysql.tsql.pivot"></a>

This topic provides reference content on migrating from Microsoft SQL Server 2019 to Amazon Aurora MySQL, specifically focusing on the PIVOT and UNPIVOT operators. You can use this guidance to understand the compatibility differences between these database systems and learn how to adapt your SQL queries.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  |  [PIVOT and UNPIVOT](chap-sql-server-aurora-mysql.tools.actioncode.md#chap-sql-server-aurora-mysql.tools.actioncode.pivot)  | Straightforward rewrite to use traditional SQL syntax. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-mysql.tsql.pivot.sqlserver"></a>

 `PIVOT` and `UNPIVOT` are relational operations used to transform a set by rotating rows into columns and columns into rows.

### PIVOT
<a name="chap-sql-server-aurora-mysql.tsql.pivot.sqlserver.pivot"></a>

The `PIVOT` operator consists of several clauses and implied expressions.

The *Anchor* column is the column that isn’t be pivoted and results in a single row for each unique value, similar to `GROUP BY`.

The pivoted columns are derived from the `PIVOT` clause and are the row values transformed into columns. The values for these columns are derived from the source column defined in the `PIVOT` clause.

#### Syntax
<a name="chap-sql-server-aurora-mysql.tsql.pivot.sqlserver.pivot.syntax"></a>

```
SELECT <Anchor column>,
    [Pivoted Column 1] AS <Alias>,
    [Pivoted column 2] AS <Alias>
    ...n
FROM
    (<SELECT Statement of Set to be Pivoted>)
    AS <Set Alias>
PIVOT
(
    <Aggregate Function>(<Aggregated Column>)
FOR
[<Column With the Values for the Pivoted Columns Names>]
    IN ( [Pivoted Column 1], [Pivoted column 2] ...)
) AS <Pivot Table Alias>;
```

#### PIVOT Examples
<a name="chap-sql-server-aurora-mysql.tsql.pivot.sqlserver.pivot.examples"></a>

Create and populate the `Orders` table.

```
CREATE TABLE Orders
(
    OrderID INT NOT NULL
    IDENTITY(1,1) PRIMARY KEY,
    OrderDate DATE NOT NULL,
    Customer VARCHAR(20) NOT NULL
);
```

```
INSERT INTO Orders (OrderDate, Customer)
VALUES
('20180101', 'John'),
('20180201', 'Mitch'),
('20180102', 'John'),
('20180104', 'Kevin'),
('20180104', 'Larry'),
('20180104', 'Kevin'),
('20180104', 'Kevin');
```

Create a simple `PIVOT` for the number of orders for each day. Days of month from 5 to 31 are omitted for example simplicity.

```
SELECT 'Number of Orders Per Day' AS DayOfMonth,
    [1], [2], [3], [4] /*...[31]*/
FROM (
    SELECT OrderID,
        DAY(OrderDate) AS OrderDay
    FROM Orders
) AS SourceSet
PIVOT
(
    COUNT(OrderID)
    FOR OrderDay IN ([1], [2], [3], [4] /*...[31]*/)
) AS PivotSet;
```

For the preceding example, the result looks as shown following.

```
DayOfMonth                     1  2  3  4  /*...[31]*/
Number of Orders for Each Day  2  1  0  4
```

**Note**  
The result set is now oriented in rows and columns. The first column is the description of the columns to follow.

 `PIVOT` for number of orders for each day for each customer.

```
SELECT Customer,
    [1], [2], [3], [4] /*...[31]*/
FROM (
    SELECT OrderID,
        Customer,
        DAY(OrderDate) AS OrderDay
    FROM Orders
    ) AS SourceSet
PIVOT
(
    COUNT(OrderID)
    FOR OrderDay IN ([1], [2], [3], [4] /*...[31]*/)
) AS PivotSet;
```

```
Customer  1  2  3  4
John      1  1  0  0
Kevin     0  0  0  3
Larry     0  0  0  1
Mitch     1  0  0  0
```

### UNPIVOT
<a name="chap-sql-server-aurora-mysql.tsql.pivot.sqlserver.unpivot"></a>

 `UNPIVOT` is similar to `PIVOT` in reverse, but spreads existing column values into rows.

The source set is similar to the result of the `PIVOT` with values pertaining to particular entities listed in columns.

Because the result set has more rows than the source, aggregations aren’t required.

It is less commonly used than `PIVOT` because most data in relational databases have attributes in columns; not the other way around.

#### UNPIVOT Examples
<a name="chap-sql-server-aurora-mysql.tsql.pivot.sqlserver.unpivot.examples"></a>

Create an populate the pivot-like `EmployeeSales` table. In real life, this is most likely a view or a set from an external source.

```
CREATE TABLE EmployeeSales
(
    SaleDate DATE NOT NULL PRIMARY KEY,
    John INT,
    Kevin INT,
    Mary INT
);
```

```
INSERT INTO EmployeeSales
VALUES
('20180101', 150, 0, 300),
('20180102', 0, 0, 0),
('20180103', 250, 50, 0),
('20180104', 500, 400, 100);
```

Unpivot employee sales for each date into individual rows for each employee.

```
SELECT SaleDate,
    Employee,
    SaleAmount
FROM
(
    SELECT SaleDate, John, Kevin, Mary
    FROM EmployeeSales
) AS SourceSet
UNPIVOT (
    SaleAmount
    FOR Employee IN (John, Kevin, Mary)
)AS UnpivotSet;
```

```
SaleDate    Employee  SaleAmount
2018-01-01  John      150
2018-01-01  Kevin     0
2018-01-01  Mary      300
2018-01-02  John      0
2018-01-02  Kevin     0
2018-01-02  Mary      0
2018-01-03  John      250
2018-01-03  Kevin     50
2018-01-03  Mary      0
2018-01-04  John      500
2018-01-04  Kevin     400
2018-01-04  Mary      100
```

For more information, see [FROM - Using PIVOT and UNPIVOT](https://docs.microsoft.com/en-us/sql/t-sql/queries/from-using-pivot-and-unpivot?vieww=%20sql-server-ver15&view=sql-server-ver15) in the *SQL Server documentation*.

## MySQL Usage
<a name="chap-sql-server-aurora-mysql.tsql.pivot.mysql"></a>

 Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) doesn’t support the `PIVOT` and `UNPIVOT` relational operators.

Functionality of both operators can be rewritten to use standard SQL syntax, as shown in the following examples.

### PIVOT Examples
<a name="chap-sql-server-aurora-mysql.tsql.pivot.mysql.pivotexamples"></a>

Create and populate the `Orders` table.

```
CREATE TABLE Orders
(
    OrderID INT
    AUTO_INCREMENT NOT NULL PRIMARY KEY,
    OrderDate DATE NOT NULL,
    Customer VARCHAR(20) NOT NULL
);
```

```
INSERT INTO Orders (OrderDate, Customer)
VALUES
('20180101', 'John'),
('20180201', 'Mitch'),
('20180102', 'John'),
('20180104', 'Kevin'),
('20180104', 'Larry'),
('20180104', 'Kevin'),
('20180104', 'Kevin');
```

Create a simple `PIVOT` for the number of orders for each day. Days of month from 5 to 31 are omitted for example simplicity.

```
SELECT 'Number of Orders Per Day' AS DayOfMonth,
    COUNT(CASE WHEN DAY(OrderDate) = 1 THEN 'OrderDate' ELSE NULL END) AS '1',
    COUNT(CASE WHEN DAY(OrderDate) = 2 THEN 'OrderDate' ELSE NULL END) AS '2',
    COUNT(CASE WHEN DAY(OrderDate) = 3 THEN 'OrderDate' ELSE NULL END) AS '3',
    COUNT(CASE WHEN DAY(OrderDate) = 4 THEN 'OrderDate' ELSE NULL END) AS '4' /*...[31]*/
FROM Orders AS O;
```

For the preceding example, the result looks as shown following.

```
DayOfMonth                     1  2  3  4  /*...[31]*/
Number of Orders for Each Day  2  1  0  4
```

 `PIVOT` for number of orders for each day for each customer.

```
SELECT Customer,
    COUNT(CASE WHEN DAY(OrderDate) = 1 THEN 'OrderDate' ELSE NULL END) AS '1',
    COUNT(CASE WHEN DAY(OrderDate) = 2 THEN 'OrderDate' ELSE NULL END) AS '2',
    COUNT(CASE WHEN DAY(OrderDate) = 3 THEN 'OrderDate' ELSE NULL END) AS '3',
    COUNT(CASE WHEN DAY(OrderDate) = 4 THEN 'OrderDate' ELSE NULL END) AS '4' /*...[31]*/
FROM Orders AS O
GROUP BY Customer;
```

```
Customer  1  2  3  4
John      1  1  0  0
Kevin     0  0  0  3
Larry     0  0  0  1
Mitch     1  0  0  0
```

### UNPIVOT Examples
<a name="chap-sql-server-aurora-mysql.tsql.pivot.mysql.examples"></a>

Create an populate the pivot-like `EmployeeSales` table. In real life, this is most likely a view or a set from an external source.

```
CREATE TABLE EmplyeeSales
(
    SaleDate DATE NOT NULL PRIMARY KEY,
    John INT,
    Kevin INT,
    Mary INT
);
```

```
INSERT INTO EmplyeeSales
VALUES
('20180101', 150, 0, 300),
('20180102', 0, 0, 0),
('20180103', 250, 50, 0),
('20180104', 500, 400, 100);
```

Unpivot employee sales for each date into individual rows for each employee.

```
SELECT SaleDate,
    Employee,
    SaleAmount
FROM
(
    SELECT SaleDate,
        Employee,
        CASE
            WHEN Employee = 'John' THEN John
            WHEN Employee = 'Kevin' THEN Kevin
            WHEN Employee = 'Mary' THEN Mary
        END AS SaleAmount
    FROM EmployeeSales
    CROSS JOIN
    (
        SELECT 'John' AS Employee
        UNION ALL
        SELECT 'Kevin'
        UNION ALL
        SELECT 'Mary'
    ) AS Employees
) AS UnpivotedSet;
```

```
SaleDate    Employee  SaleAmount
2018-01-01  John      150
2018-01-01  Kevin     0
2018-01-01  Mary      300
2018-01-02  John      0
2018-01-02  Kevin     0
2018-01-02  Mary      0
2018-01-03  John      250
2018-01-03  Kevin     50
2018-01-03  Mary      0
2018-01-04  John      500
2018-01-04  Kevin     400
2018-01-04  Mary      100
```

For more information, see [MySQL/Pivot table](https://en.wikibooks.org/wiki/MySQL/Pivot_table) in the *MySQL documentation*.