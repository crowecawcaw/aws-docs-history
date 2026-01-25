# Constraints for ANSI SQL

This topic provides reference information about SQL constraints in both Microsoft SQL Server and Amazon Aurora PostgreSQL. You can understand the similarities and differences in constraint implementation between these two database systems. The topic covers various types of constraints, including check, unique, primary key, and foreign key constraints, as well as cascaded referential actions and indexing requirements.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                            | Key differences                                                      |
| ------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Five star feature compatibility | Four star automation level         | [Constraints](chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.constraints "chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.constraints") | The `SET DEFAULT` option is missing. Check constraint with subquery. |

## SQL Server Usage

Column and table constraints are defined by the SQL standard and enforce relational data consistency. You can use four types of SQL constraints: check, unique, primary key, and foreign key.

### Check Constraints

Check constraints enforce domain integrity by limiting the data values stored in table columns. They are logical Boolean expressions that evaluate to one of the following three values: `TRUE`, `FALSE`, and `UNKNOWN`.

```
CHECK (<Logical Expression>)
```

###### Note

Check constraint expressions behave differently than predicates in other query clauses. For example, in a `WHERE` clause, a logical expression that evaluates to `UNKNOWN` is functionally equivalent to `FALSE` and the row is filtered out. For check constraints, an expression that evaluates to `UNKNOWN` is functionally equivalent to `TRUE` because the value is permitted by the constraint.

You can assign multiple check constraints to a column. Also, you can apply a single check constraint to multiple columns. In this case, it works as a table-level check constraint.

In ANSI SQL, check constraints can’t access other rows as part of the expression. In SQL Server, you can use user-defined functions in constraints to access other rows, tables, or databases.

### Unique Constraints

You can use unique constraints for all candidate keys. A candidate key is an attribute or a set of attributes or columns that uniquely identify each row in the relation (table data).

```
UNIQUE [CLUSTERED | NONCLUSTERED] (<Column List>)
```

Unique constraints guarantee that no rows with duplicate column values exist in a table.

A unique constraint can be simple or composite. Simple constraints are composed of a single column. Composite constraints are composed of multiple columns. A column may be a part of more than one constraint.

According to the ANSI SQL standard, you can have multiple rows with `NULL` values for unique constraints. However, in SQL Server, you can use a `NULL` value only for a single row. You can use a `NOT NULL` constraint in addition to a unique constraint to address this limitation.

To improve the efficiency, SQL Server creates a unique index to support unique constraints. Otherwise, every `INSERT` and `UPDATE` would require a full table scan to verify that the table doesn’t include duplicates. The default index type for unique constraints is non-clustered.

### Primary Key Constraints

A primary key is a candidate key serving as the unique identifier of a table row. Primary keys might consist of one or more columns. All columns that comprise a primary key must also have a `NOT NULL` constraint. Tables can have one primary key.

```
PRIMARY KEY [CLUSTERED | NONCLUSTERED] (<Column List>)
```

The default index type for primary keys is a clustered index.

### Foreign Key Constraints

Foreign key constraints enforce domain referential integrity. Similar to check constraints, foreign keys limit the values stored in a column or set of columns.

```
FOREIGN KEY (<Referencing Column List>)
REFERENCES <Referenced Table>(<Referenced Column List>)
```

Foreign keys reference columns in other tables, which must be either primary keys or have unique constraints. The set of values that you can use for the referencing table is the set of values that exist in the referenced table.

Although the columns referenced in the parent table are indexed because they have either a primary key or unique constraint, no indexes are automatically created for the referencing columns in the child table. A best practice is to create appropriate indexes to support joins and constraint enforcement.

Foreign key constraints impose DML limitations for the referencing child and parent tables. The purpose of a constraint is to guarantee that no orphan rows, which don’t have corresponding matching values in the parent table exist in the referencing table. The constraint limits `INSERT` and `UPDATE` to the child table and `UPDATE` and `DELETE` to the parent table. For example, you can’t delete an order having associated order items.

Foreign keys support Cascading Referential Integrity (CRI). You can use CRI to enforce constraints and define action paths for DML statements that violate the constraints. There are four CRI options:

- **NO ACTION**. When the constraint is violated due to a DML operation, an error is raised and the operation is rolled back.
- **CASCADE**. Values in a child table are updated with values from the parent table when they are updated or deleted along with the parent.
- **SET NULL**. All columns that are part of the foreign key are set to NULL when the parent is deleted or updated.
- **SET DEFAULT**. All columns that are part of the foreign key are set to their DEFAULT value when the parent is deleted or updated.

You can customize these actions independently of others in the same constraint. For example, a cascading constraint may have `CASCADE` for `UPDATE`, but `NO ACTION` for `DELETE`.

### Examples

Create a composite non-clustered primary key.

```
CREATE TABLE MyTable
(
Col1 INT NOT NULL,
Col2 INT NOT NULL,
Col3 VARCHAR(20) NULL,
CONSTRAINT PK_MyTable
PRIMARY KEY NONCLUSTERED (Col1, Col2)
);
```

Create a table-level check constraint.

```
CREATE TABLE MyTable
(
Col1 INT NOT NULL,
Col2 INT NOT NULL,
Col3 VARCHAR(20) NULL,
CONSTRAINT PK_MyTable
PRIMARY KEY NONCLUSTERED (Col1, Col2),
CONSTRAINT CK_MyTableCol1Col2
CHECK (Col2 >= Col1)
);
```

Create a simple non-null unique constraint.

```
CREATE TABLE MyTable
(
Col1 INT NOT NULL,
Col2 INT NOT NULL,
Col3 VARCHAR(20) NULL,
CONSTRAINT PK_MyTable
PRIMARY KEY NONCLUSTERED (Col1, Col2),
CONSTRAINT UQ_Col2Col3
UNIQUE (Col2, Col3)
);
```

Create a foreign key with multiple cascade actions.

```
CREATE TABLE MyParentTable
(
Col1 INT NOT NULL,
Col2 INT NOT NULL,
Col3 VARCHAR(20) NULL,
CONSTRAINT PK_MyTable
PRIMARY KEY NONCLUSTERED (Col1, Col2)
);
```

```
CREATE TABLE MyChildTable
(
Col1 INT NOT NULL PRIMARY KEY,
Col2 INT NOT NULL,
Col3 INT NOT NULL,
CONSTRAINT FK_MyChildTable_MyParentTable
FOREIGN KEY (Col2, Col3)
REFERENCES MyParentTable (Col1, Col2)
ON DELETE NO ACTION
ON UPDATE CASCADE
);
```

For more information, see [Unique Constraints and Check Constraints](https://docs.microsoft.com/en-us/sql/relational-databases/tables/unique-constraints-and-check-constraints?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/tables/unique-constraints-and-check-constraints?view=sql-server-ver15") and [Primary and Foreign Key Constraints](https://docs.microsoft.com/en-us/sql/relational-databases/tables/primary-and-foreign-key-constraints?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/tables/primary-and-foreign-key-constraints?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

PostgreSQL supports the following types of table constraints:

- `PRIMARY KEY`.
- `FOREIGN KEY`.
- `UNIQUE`.
- `NOT NULL`.
- `EXCLUDE` (unique to PostgreSQL).

Similar to constraint declaration in SQL Server, you can create constraints inline or out-of-line when you specify table columns in PostgreSQL.

You can specify PostgreSQL constraints using `CREATE TABLE` or `ALTER TABLE`. Constraints on views aren’t supported.

Make sure that you have the `CREATE` and `ALTER` privileges on the table for which you create constraints. For foreign key constraints, make sure that you have the `REFERENCES` privilege.

### Primary Key Constraints

- Uniquely identify each row and can’t contain NULL values.
- Use the same ANSI SQL syntax as SQL Server.
- You can create primary key constraints on a single column or on multiple columns (composite primary keys) as the only primary key in a table.
- Creating a primary key constraint automatically creates a unique B-Tree index on the column or group of columns marked as the primary key of the table.
- You can generate constraint names automatically by PostgreSQL or explicitly specified during constraint creation.

Create an inline primary key constraint with a system-generated constraint name.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMERIC PRIMARY KEY,
  FIRST_NAME VARCHAR(20),
  LAST_NAME VARCHAR(25),
  EMAIL VARCHAR(25));
```

Create an inline primary key constraint with a user-specified constraint name.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMERIC CONSTRAINT PK_EMP_ID PRIMARY KEY,
  FIRST_NAME VARCHAR(20),
  LAST_NAME VARCHAR(25),
  EMAIL VARCHAR(25));
```

Create an out-of-line primary key constraint.

```
CREATE
```

```
CREATE TABLE EMPLOYEES(
  EMPLOYEE_ID NUMERIC,
  FIRST_NAME VARCHAR(20),
  LAST_NAME VARCHAR(25),
  EMAIL VARCHAR(25)),
  CONSTRAINT PK_EMP_ID PRIMARY KEY (EMPLOYEE_ID));
```

Add a primary key constraint to an existing table.

```
ALTER TABLE SYSTEM_EVENTS
  ADD CONSTRAINT PK_EMP_ID PRIMARY KEY (EVENT_CODE, EVENT_TIME);
```

Drop the primary key.

```
ALTER TABLE SYSTEM_EVENTS DROP CONSTRAINT PK_EMP_ID;
```

### Foreign Key Constraints

- Enforce referential integrity in the database. Values in specific columns or a group of columns must match the values from another table or column.
- Creating a foreign key constraint in PostgreSQL uses the same ANSI SQL syntax as SQL Server.
- You can create foreign key constraints in-line or out-of-line during table creation.
- Use the `REFERENCES` clause to specify the table referenced by the foreign key constraint.
- When specifying `REFERENCES` in the absence of a column list in the referenced table, the primary key of the referenced table is used as the referenced column or columns.
- A table can have multiple foreign key constraints.
- Use the ON DELETE clause to handle foreign key parent record deletions such as cascading deletes.
- Foreign key constraint names are generated automatically by the database or specified explicitly during constraint creation.

### ON DELETE Clause

PostgreSQL provides three main options to handle cases where data is deleted from the parent table and a child table is referenced by a FOREIGN KEY constraint. By default, without specifying any additional options, PostgreSQL uses the NO ACTION method and raises an error if the referencing rows still exist when the constraint is verified.

- `ON DELETE CASCADE`. Any dependent foreign key values in the child table are removed along with the referenced values from the parent table.
- `ON DELETE RESTRICT`. Prevents the deletion of referenced values from the parent table and the deletion of dependent foreign key values in the child table.
- `ON DELETE NO ACTION`. Performs no action (the default). The fundamental difference between `RESTRICT` and `NO ACTION` is that `NO ACTION` allows the check to be postponed until later in the transaction; `RESTRICT` doesn’t.

### ON UPDATE Clause

Handling updates on `FOREIGN KEY` columns is also available using the `ON UPDATE` clause, which shares the same options as the `ON DELETE` clause:

- `ON UPDATE CASCADE`.
- `ON UPDATE RESTRICT`.
- `ON UPDATE NO ACTION`.

Create an inline foreign key with a user-specified constraint name.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMERIC PRIMARY KEY,
  FIRST_NAME VARCHAR(20),
  LAST_NAME VARCHAR(25),
  EMAIL VARCHAR(25),
  DEPARTMENT_ID NUMERIC REFERENCES DEPARTMENTS(DEPARTMENT_ID));
```

Create an out-of-line foreign key constraint with a system-generated constraint name.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMERIC PRIMARY KEY,
  FIRST_NAME VARCHAR(20),
  LAST_NAME VARCHAR(25),
  EMAIL VARCHAR(25),
  DEPARTMENT_ID NUMERIC,
  CONSTRAINT FK_FEP_ID
  FOREIGN KEY(DEPARTMENT_ID) REFERENCES DEPARTMENTS(DEPARTMENT_ID));
```

Create a foreign key using the `ON DELETE CASCADE` clause.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMERIC PRIMARY KEY,
  FIRST_NAME VARCHAR(20),
  LAST_NAME VARCHAR(25),
  EMAIL VARCHAR(25),
  DEPARTMENT_ID NUMERIC,
  CONSTRAINT FK_FEP_ID
  FOREIGN KEY(DEPARTMENT_ID) REFERENCES DEPARTMENTS(DEPARTMENT_ID)
  ON DELETE CASCADE);
```

Add a foreign key to an existing table.

```
ALTER TABLE EMPLOYEES ADD CONSTRAINT FK_DEPT
  FOREIGN KEY (department_id)
  REFERENCES DEPARTMENTS (department_id) NOT VALID;

ALTER TABLE EMPLOYEES VALIDATE CONSTRAINT FK_DEPT;
```

### ON UPDATE Clause

- Ensure that values in a column, or a group of columns, are unique across the entire table.
- PostgreSQL unique constraint syntax is ANSI SQL compatible.
- Automatically creates a B-Tree index on the respective column, or a group of columns, when creating a `UNIQUE` constraint.
- If duplicate values exist in the column, for which you create the unique constraint, the operation fails and returns an error message.
- Unique constraints in PostgreSQL accept multiple NULL values. This behavior is similar to SQL Server.
- You can use system-generated or explicitly specified naming for unique constraints.

Create an inline unique constraint ensuring uniqueness of values in the email column.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMERIC PRIMARY KEY,
  FIRST_NAME VARCHAR(20),
  LAST_NAME VARCHAR(25),
  EMAIL VARCHAR(25) CONSTRAINT UNIQ_EMP_EMAIL UNIQUE,
  DEPARTMENT_ID NUMERIC);
```

### CHECK Constraints

- Enforce that values in a column satisfy a specific requirement.
- Check constraints in PostgreSQL use the same ANSI SQL syntax as SQL Server.
- Can only be defined using a Boolean data type to evaluate the values of a column.
- Check constraints naming can be system-generated or explicitly specified by the user during constraint creation.

Check constraints are using Boolean data type, therefore you can’t use subqueries in the check constraint. To use this feature, you can create a Boolean function that will check the query results and return `TRUE` or `FALSE` values accordingly.

### NOT NULL Constraints

- Enforce that a column can’t accept NULL values. This behavior is different from the default column behavior in PostgreSQL where columns can accept NULL values.
- `NOT NULL` constraints can only be defined inline during table creation.
- You can explicitly specify names for `NOT NULL` constraints when used with a `CHECK` constraint.

Define two not null constraints on the `FIRST_NAME` and `LAST_NAME` columns. Define a check constraint with an explicitly user-specified name to enforce not null behavior on the `EMAIL` column.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMERIC PRIMARY KEY,
  FIRST_NAME VARCHAR(20) NOT NULL,
  LAST_NAME VARCHAR(25) NOT NULL,
  EMAIL VARCHAR(25) CONSTRAINT CHK_EMAIL
    CHECK(EMAIL IS NOT NULL));
```

### SET Constraints Syntax

```
SET CONSTRAINTS { ALL | name [, ...] } { DEFERRED | IMMEDIATE }
```

PostgreSQL provides controls for certain aspects of constraint behavior:

- `DEFERRABLE` | `NOT DEFERRABLE`. Using the PostgreSQL `SET CONSTRAINTS` statement. You can define constraints as:
  - `DEFERRABLE`. Allows you to use the `SET CONSTRAINTS` statement to set the behavior of constraint checking within the current transaction until transaction commit.
  - `IMMEDIATE`. Constraints are enforced only at the end of each statement. Note that each constraint has its own `IMMEDIATE` or `DEFERRED` mode.
  - `NOT DEFERRABLE`: This statement always runs as `IMMEDIATE` and isn’t affected by the `SET CONSTRAINTS` command.

- `VALIDATE CONSTRAINT` | `NOT VALID`.
  - `VALIDATE CONSTRAINT`. Validates foreign key or check constraints only that were previously created as `NOT VALID`. This action performs a validation check by scanning the table to ensure all records satisfy the constraint definition.
  - `NOT VALID`. You can use this type only for foreign key or check constraints. When specified, new records aren’t validated with the creation of the constraint. Only when the `VALIDATE CONSTRAINT` state is applied is the constraint state enforced on all records.

### Using Existing Indexes During Constraint Creation

PostgreSQL can add a new primary key or unique constraints based on an existing unique index. PostgreSQL includes all index columns in the constraint. When you create constraints using this method, the index is owned by the constraint. If you delete the constraint, then PostgreSQL deletes the index.

Use an existing unique index to create a primary key constraint.

```
CREATE UNIQUE INDEX IDX_EMP_ID ON EMPLOYEES(EMPLOYEE_ID);

ALTER TABLE EMPLOYEES
  ADD CONSTRAINT PK_CON_UNIQ PRIMARY KEY USING INDEX IDX_EMP_ID;
```

## Summary

The following table identifies similarities, differences, and key migration considerations.

| Feature                         | SQL Server                                | Aurora PostgreSQL                      |
| ------------------------------- | ----------------------------------------- | -------------------------------------- |
| Check constraints               | CHECK                                     | CHECK                                  |
| Unique constraints              | UNIQUE                                    | UNIQUE                                 |
| Primary key constraints         | PRIMARY KEY                               | PRIMARY KEY                            |
| Foreign key constraints         | FOREIGN KEY                               | FOREIGN KEY                            |
| Cascaded referential actions    | NO ACTION, CASCADE, SET NULL, SET DEFAULT | RESTRICT, CASCADE, SET NULL, NO ACTION |
| Indexing of referencing columns | Not required                              | N/A                                    |
| Indexing of referenced columns  | PRIMARY KEY or UNIQUE                     | PRIMARY KEY or UNIQUE                  |

For more information, see [Constraints](https://www.postgresql.org/docs/13/ddl-constraints.html "https://www.postgresql.org/docs/13/ddl-constraints.html"), [SET CONSTRAINTS](https://www.postgresql.org/docs/13/sql-set-constraints.html "https://www.postgresql.org/docs/13/sql-set-constraints.html"), and [ALTER TABLE](https://www.postgresql.org/docs/13/sql-altertable.html "https://www.postgresql.org/docs/13/sql-altertable.html") in the _PostgreSQL documentation_.
