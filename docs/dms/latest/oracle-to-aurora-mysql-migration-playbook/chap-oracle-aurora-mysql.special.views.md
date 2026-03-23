# Oracle and MySQL views

With AWS DMS, you can create and work with database views in Oracle and MySQL databases. A view is a virtual table that derives its data from one or more underlying tables or views. Views provide a way to present a subset of data from one or more tables, combining data from different tables, or adding additional data transformations.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| ------------------------------- | ---------------------------------- | ------------------------- | --------------- |
| Four star feature compatibility | Four star automation level         |                           | N/A             |

## Oracle usage

Database views store a named SQL query in the Oracle Data Dictionary with a predefined structure. A view doesn’t store actual data and may be considered a virtual table or a logical table based on the data from one or more physical database tables.

### Privileges

Make sure that the user has the `CREATE VIEW` privilege to create a view in their own schema.

Make sure that the user has the `CREATE ANY VIEW` privilege to create a view in any schema.

Make sure that the owner of the view has all the necessary privileges on the source tables or views on which the view is based (`SELECT` or `DML` privileges).

### CREATE (OR REPLACE) VIEW Statements

- `CREATE VIEW` creates a new view.
- `CREATE OR REPLACE` overwrites an existing view and modifies the view definition without having to manually drop and recreate the original view, and without deleting the previously granted privileges.

### Oracle common view parameters

| Oracle view parameter    | Description                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `CREATE OR REPLACE`      | Recreate an existing view (if one exists) or create a new view.                                              |
| `FORCE`                  | Create the view regardless of the existence of the source tables or views and regardless of view privileges. |
| `VISIBLE` or `INVISIBLE` | Specify if a column based on the view is visible or invisible.                                               |
| `WITH READ ONLY`         | Disable DML commands.                                                                                        |
| `WITH CHECK OPTION`      | Specifies the level of enforcement when performing DML commands on the view.                                 |

### Examples

Views are classified as either simple or complex.

A _simple view_ is a view having a single source table with no aggregate functions. DML operations can be performed on simple views and affect the base table(s). The following example creates and updates a simple View.

```
CREATE OR REPLACE VIEW VW_EMP
AS
SELECT EMPLOYEE_ID, LAST_NAME, EMAIL, SALARY
FROM EMPLOYEES
WHERE DEPARTMENT_ID BETWEEN 100 AND 130;
UPDATE VW_EMP
SET EMAIL=EMAIL||'.org'
WHERE EMPLOYEE_ID=110;

1 row updated.
```

A _complex view_ is a view with several source tables or views containing joins, aggregate (group) functions, or an order by clause. Performing DML operations on complex views can’t be done directly, but `INSTEAD OF` triggers can be used as a workaround. The following example creates and updates a complex view.

```
CREATE OR REPLACE VIEW VW_DEP
AS
SELECT B.DEPARTMENT_NAME, COUNT(A.EMPLOYEE_ID) AS CNT
FROM EMPLOYEES A JOIN DEPARTMENTS B USING(DEPARTMENT_ID)
GROUP BY B.DEPARTMENT_NAME;
UPDATE VW_DEP
SET CNT=CNT +1
WHERE DEPARTMENT_NAME=90;

ORA-01732: data manipulation operation not legal on this view
```

For more information, see [CREATE VIEW](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-VIEW.html#GUID-61D2D2B4-DACC-4C7C-89EB-7E50D9594D30 "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-VIEW.html#GUID-61D2D2B4-DACC-4C7C-89EB-7E50D9594D30") in the _Oracle documentation_.

## MySQL usage

Similar to Oracle, Aurora MySQL views consist of a `SELECT` statement that references base tables and other views.

Aurora MySQL views are created using the `CREATE VIEW` statement. The `SELECT` statement comprising the definition of the view is evaluated only when the view is created and is not affected by subsequent changes to the underlying base tables.

Aurora MySQL views have the following restrictions:

- A view can’t reference system variables or user-defined variables.
- When used within a stored procedure or function, the `SELECT` statement can’t reference parameters or local variables.
- A view can’t reference prepared statement parameters.
- Make sure that all objects referenced by a view exist when the view is created. If an underlying table or view is later dropped, invoking the view results in an error.
- Views can’t reference `TEMPORARY` tables.
- `TEMPORARY` views aren’t supported.
- Views don’t support triggers.
- Aliases are limited to a maximum length of 64 characters and not the typical 256 maximum alias length.

Aurora MySQL provides additional properties that aren’t available in Oracle:

- The `ALGORITHM` clause is a fixed hint that affects the way the MySQL query processor handles the view physical evaluation operator. The MERGE algorithm uses a dynamic approach where the definition of the view is merged to the outer query. The `TEMPTABLE` algorithm materializes the view data internally. For more information, see [View Processing Algorithms](https://dev.mysql.com/doc/refman/5.7/en/view-algorithms.html "https://dev.mysql.com/doc/refman/5.7/en/view-algorithms.html") in the _MySQL documentation_.
- You can use the `DEFINER` and `SQL SECURITY` clauses can be used to specify a specific security context for checking view permissions at run time.

Similar to Oracle, Aurora MySQL supports updatable views and the ANSI standard `CHECK OPTION` to limit inserts and updates to rows referenced by the view.

You can use the `LOCAL` and `CASCADED` keywords to determine the scope of violation checks. When you use the `LOCAL` keyword, the `CHECK OPTION` is evaluated only for the view being created. The `CASCADED` option causes evaluation of referenced views. The default option is `CASCADED`.

In general, only views having a one-to-one relationship between the source rows and the exposed rows are updatable. Adding the following constructs prevents modification of data:

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

Make sure that your view has unique column names. Column aliases are derived from the base tables or explicitly specified in the `SELECT` statement of column definition list. `ORDER BY` is permitted in Aurora MySQL, but ignored if the outer query has an `ORDER BY` clause.

A view in Aurora MySQL can invoke functions, which in turn may introduce a change to the database.

Aurora MySQL assesses data access privileges as follows:

- Make sure that the user creating a view has all required privileges to use the top-level objects referenced by the view. For example, for a view referencing table columns, the user must have privilege for each column in the select list of the view definition.
- If the view definition references a stored function, only the privileges needed to invoke the function are checked. The privileges required at run time can be checked only at run time because different invocations may use different execution paths within the function code.
- Make sure that the user referencing a view has the appropriate `SELECT`, `INSERT`, `UPDATE`, or `DELETE` privileges, as with a normal table.
- When a view is referenced, privileges for all objects accessed by the view are evaluated using the privileges for the view `DEFINER` account, or the invoker, depending on whether `SQL SECURITY` is set to `DEFINER` or `INVOKER`.
- When a view invocation triggers the execution of a stored function, privileges are checked for statements executed within the function based on the function’s `SQL SECURITY` setting. For functions where the security is set to `DEFINER`, the function executes with the privileges of the `DEFINER` account. For functions where it is set to `INVOKER`, the function executes with the privileges determined by the view’s `SQL SECURITY` setting as described above.

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

### Examples

The following example creates and populate the `Invoices` table.

```
CREATE TABLE Invoices(
InvoiceID INT NOT NULL PRIMARY KEY,
Customer VARCHAR(20) NOT NULL,
TotalAmount DECIMAL(9,2) NOT NULL);

INSERT INTO Invoices (InvoiceID,Customer,TotalAmount)
VALUES (1, 'John', 1400.23), (2, 'Jeff', 245.00), (3, 'James', 677.22);
```

The following example creates the `TotalSales` view.

```
CREATE VIEW TotalSales
AS
SELECT Customer, SUM(TotalAmount) AS CustomerTotalAmount
GROUP BY Customer;
```

The following example invokes the view.

```
SELECT * FROM TotalSales
ORDER BY CustomerTotalAmount DESC;

Customer  CustomerTotalAmount
John      1400.23
James     677.22
Jeff      245.00
```

For more information, see [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html "https://dev.mysql.com/doc/refman/5.7/en/create-view.html"), [Restrictions on Views](https://dev.mysql.com/doc/refman/5.7/en/view-restrictions.html "https://dev.mysql.com/doc/refman/5.7/en/view-restrictions.html"), and [Updatable and Insertable Views](https://dev.mysql.com/doc/refman/5.7/en/view-updatability.html "https://dev.mysql.com/doc/refman/5.7/en/view-updatability.html") in the _MySQL documentation_.
