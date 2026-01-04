# Views for ANSI SQL

This topic provides reference information about views in Microsoft SQL Server and Amazon Aurora MySQL, comparing their features and usage. You can use this content to understand the similarities and differences between views in these two database systems, which is valuable for planning and executing migrations from SQL Server to Aurora MySQL.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                                                 |
| ------------------------------- | ---------------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------- |
| Four star feature compatibility | Four star automation level         | N/A                       | Minor syntax and handling differences. Indexes, triggers, and temporary views aren’t supported. |

## SQL Server Usage

Views are schema objects that provide stored definitions for virtual tables. Similar to tables, views are data sets with uniquely named columns and rows. With the exception of indexed views, view objects don’t store data. They consist only of a query definition and are reevaluated for each invocation.

Views are used as abstraction layers and security filters for the underlying tables. They can `JOIN` and `UNION` data from multiple source tables and use aggregates, window functions, and other SQL features as long as the result is a semi-proper set with uniquely identifiable columns and no order to the rows. You can use distributed views to query other databases and data sources using linked servers.

As an abstraction layer, a view can decouple application code from the database schema. The underlying tables can be changed without the need to modify the application code, as long as the expected results of the view don’t change. You can use this approach to provide backward compatible views of data.

As a security mechanism, a view can screen and filter source table data. You can perform permission management at the view level without explicit permissions to the base objects, provided the ownership chain is maintained.

For more information, see [Overview of SQL Server Security](https://docs.microsoft.com/en-us/previous-versions/dotnet/framework/data/adonet/sql/overview-of-sql-server-security?view=sql-server-ver15 "https://docs.microsoft.com/en-us/previous-versions/dotnet/framework/data/adonet/sql/overview-of-sql-server-security?view=sql-server-ver15") in the _SQL Server documentation_.

View definitions are evaluated when they are created and aren’t affected by subsequent changes to the underlying tables.

For example, a view that uses `SELECT *` doesn’t display columns that were added later to the base table. Similarly, if a column was dropped from the base table, invoking the view results in an error. Use the `SCHEMABINDING` option to prevent changes to base objects.

### Modifying Data Through Views

Updatable views can both `SELECT` and modify data. For a view to be updatable, the following conditions must be met:

- The DML targets only one base table.
- Columns being modified must be directly referenced from the underlying base tables. Computed columns, set operators, functions, aggregates, or any other expressions aren’t permitted.
- If a view is created with the `CHECK OPTION`, rows being updated can’t be filtered out of the view definition as the result of the update.

### Special View Types

SQL Server also provides three types of special views:

- **Indexed views** (also known as materialized views or persisted views) are standard views that have been evaluated and persisted in a unique clustered index, much like a normal clustered primary key table. Each time the source data changes, SQL Server re-evaluates the indexed views automatically and updates the indexed view. Indexed views are typically used as a means to optimize performance by pre-processing operators such as aggregations, joins, and others. Queries needing this pre-processing don’t have to wait for it to be reevaluated on every query run.
- **Partitioned views** are views that rejoin horizontally partitioned data sets from multiple underlying tables, each containing only a subset of the data. The view uses a UNION ALL query where the underlying tables can reside locally or in other databases (or even other servers). These types of views are called Distributed Partitioned Views (DPV).
- **System views** are used to access server and object meta data. SQL Server also supports a set of standard `INFORMATION_SCHEMA` views for accessing object meta data.

### Syntax

```
CREATE [OR ALTER] VIEW [<Schema Name>.] <View Name> [(<Column Aliases> ])]
[WITH [ENCRYPTION][SCHEMABINDING][VIEW_METADATA]]
AS <SELECT Query>
[WITH CHECK OPTION][;]
```

### Examples

Create a view that aggregates items for each customer.

```
CREATE TABLE Orders
(
    OrderID INT NOT NULL PRIMARY KEY,
    OrderDate DATETIME NOT NULL
    DEFAULT GETDATE()
);
```

```
CREATE TABLE OrderItems
(
    OrderID INT NOT NULL
        REFERENCES Orders(OrderID),
    Item VARCHAR(20) NOT NULL,
    Quantity SMALLINT NOT NULL,
    PRIMARY KEY(OrderID, Item)
);
```

```
CREATE VIEW SalesView
AS
SELECT O.Customer,
    OI.Product,
    SUM(CAST(OI.Quantity AS BIGINT)) AS TotalItemsBought
FROM Orders AS O
    INNER JOIN
    OrderItems AS OI
        ON O.OrderID = OI.OrderID;
```

Create an indexed view that pre-aggregates items for each customer.

```
CREATE VIEW SalesViewIndexed
AS
SELECT O.Customer,
    OI.Product,
    SUM_BIG(OI.Quantity) AS TotalItemsBought
FROM Orders AS O
    INNER JOIN
    OrderItems AS OI
        ON O.OrderID = OI.OrderID;
```

```
CREATE UNIQUE CLUSTERED INDEX IDX_SalesView
ON SalesViewIndexed (Customer, Product);
```

Create a partitioned view.

```
CREATE VIEW dbo.PartitioneView
WITH SCHEMABINDING
AS
SELECT *
FROM Table1
UNION ALL
SELECT *
FROM Table2
UNION ALL
SELECT *
FROM Table3
```

For more information, see [Views](https://docs.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/views/views?view=sql-server-ver15"), [Modify Data Through a View](https://docs.microsoft.com/en-us/sql/relational-databases/views/modify-data-through-a-view?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/views/modify-data-through-a-view?view=sql-server-ver15"), and [CREATE VIEW (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-view-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/create-view-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Similar to SQL Server, Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) views consist of a `SELECT` statement that can references base tables and other views.

Aurora MySQL views are created using the `CREATE VIEW` statement. The `SELECT` statement comprising the definition of the view is evaluated only when the view is created and isn’t affected by subsequent changes to the underlying base tables.

Aurora MySQL views have the following restrictions:

- A view can’t reference system variables or user-defined variables.
- When used within a stored procedure or function, the `SELECT` statement can’t reference parameters or local variables.
- A view can’t reference prepared statement parameters.
- All objects referenced by a view must exist when the view is created. If an underlying table or view is later dropped, invoking the view results in an error.
- Views can’t reference `TEMPORARY` tables.
- `TEMPORARY` views aren’t supported.
- Views don’t support triggers.
- Aliases are limited to a maximum length of 64 characters (not the typical 256 maximum alias length).

Aurora MySQL provides additional properties not available in SQL Server:

- The `ALGORITHM` clause is a fixed hint that affects the way the MySQL query processor handles the view physical evaluation operator.

The MERGE algorithm uses a dynamic approach where the definition of the view is merged to the outer query.

The TEMPTABLE algorithm materializes the view data internally. For more information, see [View Processing Algorithms](https://dev.mysql.com/doc/refman/5.7/en/view-algorithms.html "https://dev.mysql.com/doc/refman/5.7/en/view-algorithms.html") in the _MySQL documentation_.

- The `DEFINER` and `SQL SECURITY` clauses can be used to specify a specific security context for checking view permissions at run time.

Similar to SQL Server, Aurora MySQL supports updatable views and the ANSI standard `CHECK OPTION` to limit inserts and updates to rows referenced by the view.

The `LOCAL` and `CASCADED` keywords are used to determine the scope of violation checks. When using the `LOCAL` keyword, the `CHECK OPTION` is evaluated only for the view being created. `CASCADED` causes evaluation of referenced views. The default is `CASCADED`.

In general, only views having a one-to-one relationship between the source rows and the exposed rows are updatable.

Adding the following constructs prevents modification of data:

- Aggregate functions.
- `DISTINCT`.
- `GROUP BY`.
- `HAVING`.
- `UNION` or `UNION ALL`.
- Subquery in the select list.
- Certain joins.
- Reference to a non-updatable view.
- Subquery in the `WHERE` clause that refers to a table in the `FROM` clause.
- `ALGORITHM = TEMPTABLE`.
- Multiple references to any column of a base table.

A view must have unique column names. Column aliases are derived from the base tables or explicitly specified in the `SELECT` statement of column definition list. `ORDER BY` is permitted in Aurora MySQL, but ignored if the outer query has an `ORDER BY` clause.

Aurora MySQL assesses data access privileges as follows:

- The user creating a view must have all required privileges to use the top-level objects referenced by the view.

For example, for a view referencing table columns, the user must have privilege for each column in any clause of the view definition.

- If the view definition references a stored function, only the privileges needed to invoke the function are checked. The privileges required at run time can be checked only at run time because different invocations may use different run paths within the function code.
- The user referencing a view must have appropriate `SELECT`, `INSERT`, `UPDATE`, or `DELETE` privileges, as with a normal table.
- When a view is referenced, privileges for all objects accessed by the view are evaluated using the privileges for the view `DEFINER` account, or the invoker, depending on whether `SQL SECURITY` is set to `DEFINER` or `INVOKER`.
- When a view invocation triggers the call of a stored function, privileges are checked for statements that run within the function based on the function’s `SQL SECURITY` setting. For functions where the security is set to `DEFINER`, the function runs with the privileges of the `DEFINER` account. For functions where it is set to `INVOKER`, the function runs with the privileges determined by the view’s `SQL SECURITY` setting as described before.

### Syntax

```
CREATE [OR REPLACE]
    [ALGORITHM = {UNDEFINED | MERGE | TEMPTABLE}]
    [DEFINER = { <User> | CURRENT_USER }]
    [SQL SECURITY { DEFINER | INVOKER }]
    VIEW <View Name> [(<Column List>)]
    AS <SELECT Statement>
    [WITH [CASCADED | LOCAL] CHECK OPTION];
```

### Migration Considerations

The basic syntax for views is very similar to SQL Server and is ANSI compliant. Code migration should be straightforward.

Aurora MySQL doesn’t support triggers on views. In SQL Server, `INSTEAD OF` triggers are supported. For more information, see [Triggers](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

In Aurora MySQL, `ORDER BY` is permitted in a view definition. It is ignored if the outer `SELECT` has its own `ORDER BY`. This behavior is different than SQL Server where `ORDER BY` is allowed only for `TOP` filtering. The actual order of the rows isn’t guaranteed.

Security context is explicit in Aurora MySQL, which isn’t supported in SQL Server. Use security contexts to work around the lack of ownership-chain permission paths.

Unlike SQL Server, a view in Aurora MySQL can invoke functions, which in turn may introduce a change to the database. For more information, see [User-Defined Functions](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

The `WITH CHECK` option in Aurora MySQL can be scoped to `LOCAL` or `CASCADED`. The `CASCADED` causes the `CHECK` option to be evaluated for nested views referenced in the parent.

Indexed views aren’t supported in Aurora MySQL. Consider using application maintained tables instead. Change application code to reference those tables instead of the base table.

### Examples

Create and populate the `Invoices` table.

```
CREATE TABLE Invoices(
InvoiceID INT NOT NULL PRIMARY KEY,
Customer VARCHAR(20) NOT NULL,
TotalAmount DECIMAL(9,2) NOT NULL);

INSERT INTO Invoices (InvoiceID,Customer,TotalAmount)
VALUES
(1, 'John', 1400.23),
(2, 'Jeff', 245.00),
(3, 'James', 677.22);
```

Create the `TotalSales` view.

```
CREATE VIEW TotalSales
AS
SELECT Customer,
    SUM(TotalAmount) AS CustomerTotalAmount
GROUP BY Customer;
```

Invoke the view.

```
SELECT * FROM TotalSales
ORDER BY CustomerTotalAmount DESC;

Customer  CustomerTotalAmount
John      1400.23
James     677.22
Jeff      245.00
```

## Summary

| Feature                  | SQL Server                      | Aurora MySQL | Comments                                                                                                                                          |
| ------------------------ | ------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Indexed views            | Supported                       | N/A          |                                                                                                                                                   |
| Partitioned views        | Supported                       | N/A          | You can create partitioned views in the same way as SQL Server, they won’t benefit from the internal optimizations such as partition elimination. |
| Updateable views         | Supported                       | Supported    |                                                                                                                                                   |
| Prevent schema conflicts | `SCHEMABINDING` option          |              |                                                                                                                                                   |
| Triggers on views        | `INSTEAD OF`                    | N/A          | For more information, see [Triggers](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").                                |
| Temporary views          | `CREATE VIEW #View…​`           | N/A          |                                                                                                                                                   |
| Refresh view definition  | `sp_refreshview` / `ALTER VIEW` | `ALTER VIEW` |                                                                                                                                                   |

For more information, see [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html "https://dev.mysql.com/doc/refman/5.7/en/create-view.html"), [Restrictions on Views](https://dev.mysql.com/doc/refman/5.7/en/view-restrictions.html "https://dev.mysql.com/doc/refman/5.7/en/view-restrictions.html"), and [Updatable and Insertable Views](https://dev.mysql.com/doc/refman/5.7/en/view-updatability.html "https://dev.mysql.com/doc/refman/5.7/en/view-updatability.html") in the _MySQL documentation_.
