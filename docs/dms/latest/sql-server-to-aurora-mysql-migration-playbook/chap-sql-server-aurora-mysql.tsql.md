# User-defined functions for T-SQL

This topic provides reference content comparing user-defined functions (UDFs) in Microsoft SQL Server 2019 and Amazon Aurora MySQL. It explains the capabilities, limitations, and key differences between UDFs in these two database systems. You’ll learn about the types of UDFs supported, their behavior, and important considerations when migrating from SQL Server to Aurora MySQL.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                                   | Key differences                                                                                                     |
| ------------------------------ | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Two star feature compatibility | Three star automation level        | [User-Defined Functions](chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.udf "chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.udf") | Scalar functions only, rewrite inline TVF as views or derived tables, and multi-statement TVF as stored procedures. |

## SQL Server Usage

User-defined functions (UDF) are code objects that accept input parameters and return either a scalar value or a set consisting of rows and columns.

SQL Server UDFs can be implemented using T-SQL or Common Language Runtime (CLR) code.

###### Note

This section doesn’t cover CLR code objects.

Function invocations can’t have any lasting impact on the database. They must be contained and can only modify objects and data local to their scope (for example, data in local variables). Functions aren’t allowed to modify data or the structure of a database.

Functions may be deterministic or non-deterministic. Deterministic functions always return the same result when you run them with the same data. Non-deterministic functions may return different results each time they run. For example, a function that returns the current date or time.

SQL Server supports three types of T-SQL UDFs: scalar functions, table-valued functions, and multi-statement table-valued functions.

SQL Server 2019 adds scalar user-defined functions inlining. Inlining transforms functions into relational expressions and embeds them in the calling SQL query. This transformation improves the performance of workloads that take advantage of scalar UDFs. Scalar UDF inlining facilitates cost-based optimization of operations inside UDFs. The results are efficient, set-oriented, and parallel instead of inefficient, iterative, serial run plans. For more information, see [Scalar UDF Inlining](https://docs.microsoft.com/en-us/sql/relational-databases/user-defined-functions/scalar-udf-inlining?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/user-defined-functions/scalar-udf-inlining?view=sql-server-ver15") in the _SQL Server documentation_.

### Scalar User-Defined Functions

Scalar UDFs accept zero or more parameters and return a scalar value. You can use scalar UDFs in T-SQL expressions.

**Syntax**

```
CREATE FUNCTION <Function Name> ([{<Parameter Name> [AS] <Data Type> [= <Default Value>] [READONLY]} [,...n]])
RETURNS <Return Data Type>
[AS]
BEGIN
<Function Body Code>
RETURN <Scalar Expression>
END[;]
```

**Examples**

Create a scalar function to change the first character of a string to upper case.

```
CREATE FUNCTION dbo.UpperCaseFirstChar (@String VARCHAR(20))
RETURNS VARCHAR(20)
AS
BEGIN
RETURN UPPER(LEFT(@String, 1)) + LOWER(SUBSTRING(@String, 2, 19))
END;
```

```
SELECT dbo.UpperCaseFirstChar ('mIxEdCasE');

Mixedcase
```

### User-Defined Table-Valued Functions

Inline table-valued UDFs are similar to views or a Common Table Expressions (CTE) with the added benefit of parameters. They can be used in `FROM` clauses as subqueries and can be joined to other source table rows using the `APPLY` and `OUTER APPLY` operators. In-line table valued UDFs have many associated internal optimizer optimizations due to their simple, view-like characteristics.

**Syntax**

```
CREATE FUNCTION <Function Name> ([{<Parameter Name> [AS] <Data Type> [= <Default
Value>] [READONLY]} [,...n]])
RETURNS TABLE
[AS]
RETURN (<SELECT Query>)[;]
```

**Examples**

Create a table valued function to aggregate employee orders.

```
CREATE TABLE Orders
(
    OrderID INT NOT NULL PRIMARY KEY,
    EmployeeID INT NOT NULL,
    OrderDate DATETIME NOT NULL
);
```

```
INSERT INTO Orders (OrderID, EmployeeID, OrderDate)
VALUES
(1, 1, '20180101 13:00:05'),
(2, 1, '20180201 11:33:12'),
(3, 2, '20180112 10:22:35');
```

```
CREATE FUNCTION dbo.EmployeeMonthlyOrders
(@EmployeeID INT)
RETURNS TABLE AS
RETURN
(
SELECT EmployeeID,
    YEAR(OrderDate) AS OrderYear,
    MONTH(OrderDate) AS OrderMonth,
    COUNT(*) AS NumOrders
FROM Orders AS O
WHERE EmployeeID = @EmployeeID
GROUP BY EmployeeID,
    YEAR(OrderDate),
    MONTH(OrderDate)
);
```

```
SELECT *
FROM dbo.EmployeeMonthlyOrders (1)

EmployeeID  OrderYear  OrderMonth  NumOrders
1           2018       1           1
1           2018       2           1
```

### Multi-Statement User-Defined Table-Valued Functions

Multi-statement table valued UDFs, like inline UDFs, are also similar to views or CTEs, with the added benefit of allowing parameters. They can be used in FROM clauses as sub queries and can be joined to other source table rows using the `APPLY` and `OUTER APPLY` operators.

The difference between multi-statement UDFs and the inline UDFs is that multi-statement UDFs aren’t restricted to a single `SELECT` statement. They can consist of multiple statements including logic implemented with flow control, complex data processing, security checks, and so on.

The downside of using multi-statement UDFs is that there are far less optimizations possible and performance may suffer.

**Syntax**

```
CREATE FUNCTION <Function Name> ([{<Parameter Name> [AS] <Data Type> [= <Default
Value>] [READONLY]} [,...n]])
RETURNS <@Return Variable> TABLE <Table Definition>
[AS]
BEGIN
<Function Body Code>
RETURN
END[;]
```

For more information, see [CREATE FUNCTION (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-function-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/create-function-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) supports the creation of user-defined scalar functions only. There is no support for table-valued functions.

Unlike SQL Server, Aurora MySQL enables routines to read and write data using `INSERT`, `UPDATE`, and `DELETE`. It also allows DDL statements such as `CREATE` and `DROP`. Aurora MySQL doesn’t permit stored functions to contain explicit SQL transaction statements such as `COMMIT` and `ROLLBACK`.

In Aurora MySQL, you can explicitly specify several options with the `CREATE FUNCTION` statement. These characteristics are saved with the function definition and are viewable with the `SHOW CREATE FUNCTION` statement.

- The `DETERMINISTIC` option must be explicitly stated. Otherwise, the engine assumes it is not deterministic.

###### Note

The MySQL engine doesn’t check the validity of the deterministic property declaration. If you wrongly specify a function as `DETERMINISTIC` when in fact it is not, unexpected results and errors may occur.

- `CONTAINS SQL` indicates the function code doesn’t contain statements that read or modify data.
- `READS SQL DATA` indicates the function code contains statements that read data (for example, `SELECT`) but not statements that modify data (for example, `INSERT`, `DELETE`, or `UPDATE`).
- `MODIFIES SQL DATA` indicates the function code contains statements that may modify data.

###### Note

The preceding options are advisory only. The server doesn’t constrain the function code based on the declaration. This feature is useful in assisting code management.

### Syntax

```
CREATE FUNCTION <Function Name> ([<Function Parameter>[,...]])
RETURNS <Returned Data Type> [characteristic ...]
<Function Code Body>
```

```
characteristic:
COMMENT '<Comment>' | LANGUAGE SQL | [NOT] DETERMINISTIC
| { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
| SQL SECURITY { DEFINER | INVOKER }
```

### Migration Considerations

For scalar functions, migration should be straight forward as far as the function syntax is concerned. Note that rules in Aurora MySQL regarding functions are much more lenient than SQL Server.

A function in Aurora MySQL may modify data and schema. Function determinism must be explicitly stated, unlike SQL Server that infers it from the code. Additional properties can be stated for a function, but most are advisory only and have no functional impact.

Also note that the AS keyword, which is mandatory in SQL Server before the function’s code body, is not valid Aurora MySQL syntax and must be removed.

Table-valued functions will be harder to migrate. For most in-line table valued functions, a simple path may consist of migrating to using views, and letting the calling code handle parameters.

Complex multi-statement table valued functions will require rewrite as a stored procedure, which may in turn write the data to a temporary or standard table for further processing.

### Examples

Create a scalar function to change the first character of string to upper case.

```
CREATE FUNCTION UpperCaseFirstChar (String VARCHAR(20))
RETURNS VARCHAR(20)
BEGIN
RETURN CONCAT(UPPER(LEFT(String, 1)) , LOWER(SUBSTRING(String, 2, 19)));
END
```

```
SELECT UpperCaseFirstChar ('mIxEdCasE');
```

```
Mixedcase
```

## Summary

The following table identifies similarities, differences, and key migration considerations.

| SQL Server user-defined function feature | Migrate to Aurora MySQL    | Comment                                                                                                                   |
| ---------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Scalar UDF                               | Scalar UDF                 | Use `CREATE FUNCTION` with similar syntax, remove the `AS` keyword.                                                       |
| Inline table-valued UDF                  | N/A                        | Use views and replace parameters with `WHERE` filter predicates.                                                          |
| Multi-statement table-valued UDF         | N/A                        | Use stored procedures to populate tables and read from the table directly.                                                |
| UDF determinism implicit                 | Explicit declaration       | Use the `DETERMINISTIC` characteristic explicitly to denote a deterministic function, which enables engine optimizations. |
| UDF boundaries local only                | Can change data and schema | UDF rules are more lenient, avoid unexpected changes from function invocation.                                            |

For more information, see [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html "https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html") and [CREATE FUNCTION Statement for Loadable Functions](https://dev.mysql.com/doc/refman/5.7/en/create-function-loadable.html "https://dev.mysql.com/doc/refman/5.7/en/create-function-loadable.html") in the _MySQL documentation_.
