# Oracle and PostgreSQL table constraints

With AWS DMS, you can migrate data from source databases while applying table constraints to enforce data integrity on the target PostgreSQL or Oracle databases. Table constraints define rules for the data in a table, such as restricting null values, ensuring unique entries, or specifying conditions for accepted values.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                      | Key differences                                                                                                   |
| ------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| Four star feature compatibility | Four star automation level         | [Creating Tables](chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.tables "chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.tables") | PostgreSQL doesn’t support `REF`, `ENABLE`, and `DISABLE`. Also, PostgreSQL doesn’t support constraints on views. |

## Oracle usage

Oracle provides six types of constraints to enforce data integrity on table columns. Constraints ensure data inserted into tables is controlled and satisfies logical requirements.

### Oracle integrity constraint types

- **Primary Key** — Enforces that row values in a specific column are unique and not null.
- **Foreign Key** — Enforces that values in the current table exist in the referenced table.
- **Unique** — Prevents data duplication on a column, or combination of columns, and allows one null value.
- **Check** — Enforces that values comply with a specific condition.
- **Not Null** — Enforces that null values can’t be inserted into a specific column.
- **REF** — References an object in another object type or in a relational table.

### Oracle constraint creation

You can create new constraints in two ways.

1. **Inline** — Defines a constraint as part of a table column declaration.

```
CREATE TABLE EMPLOYEES (
  EMP_ID NUMBER PRIMARY KEY,…);
```

2. **Out-of-line** — Defines a constraint as part of the table DDL during table creation.

```
CREATE TABLE EMPLOYEES (EMP_ID NUMBER,…,
  CONSTRAINT PK_EMP_ID PRIMARY KEY(EMP_ID));
```

###### Note

Declare NOT NULL constraints using the inline method.

Use the following syntax to specify Oracle constraints:

- `CREATE / ALTER TABLE`
- `CREATE / ALTER VIEW`

###### Note

Views have only a primary key, foreign key, and unique constraints.

**Privileges**

You need privileges on the table where constrains are created and, in case of foreign key constraints, you need the `REFERENCES` privilege on the referenced table.

### PRIMARY KEY constraints

A unique identifier for each record in a database table can appear only once and can’t contain NULL values. A table can only have one primary key.

When creating a primary key constraint inline, you can specify only the `PRIMARY KEY` keyword. When you create the constraint out-of-line, you must specify one column or a combination of columns.

Creating a new primary key constraint also implicitly creates a unique index on the primary key column if no index already exists. When dropping a primary key constraint, the system-generated index is also dropped. If a user defined index was used, the index isn’t dropped.

- Primary keys can’t be created on columns defined with the following data types: `LOB`, `LONG`, `LONG RAW`, `VARRAY`, `NESTED TABLE`, `BFILE`, `REF`, `TIMESTAMP WITH TIME ZONE`.

The TIMESTAMP WITH LOCAL TIME ZONE data type is allowed as a primary key.

- Primary keys can be created from multiple columns (composite PK). They are limited to a total of 32 columns.
- Defining the same column as both a primary key and as a unique constraint isn’t allowed.

**Examples**

Create an Inline primary key using a system-generated primary key constraint name.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMBER PRIMARY KEY,
  FIRST_NAME VARCHAR2(20),
  LAST_NAME VARCHAR2(25),
  EMAIL VARCHAR2(25));
```

Create an inline primary key using a user-specified primary key constraint name.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMBER CONSTRAINT PK_EMP_ID PRIMARY KEY,
  FIRST_NAME VARCHAR2(20),
  LAST_NAME VARCHAR2(25),
  EMAIL VARCHAR2(25));
```

Create an out-of-line primary key.

```
CREATE TABLE EMPLOYEES(
  EMPLOYEE_ID NUMBER,
  FIRST_NAME VARCHAR2(20),
  LAST_NAME VARCHAR2(25),
  EMAIL VARCHAR2(25));
  CONSTRAINT PK_EMP_ID PRIMARY KEY (EMPLOYEE_ID));
```

Add a primary key to an existing table.

```
ALTER TABLE SYSTEM_EVENTS
  ADD CONSTRAINT PK_EMP_ID PRIMARY KEY (EVENT_CODE, EVENT_TIME);
```

### FOREIGN KEY constraints

Foreign key constraints identify the relationship between column records defined with a foreign key constraint and a referenced primary key or a unique column. The main purpose of a foreign key is to enforce that the values in table A also exist in table B as referenced by the foreign key.

A referenced table is known as a parent table. The table on which the foreign key was created is known as a child table. Foreign keys created in child tables generally reference a primary key constraint in a parent table.

**Limitations**

Foreign keys can’t be created on columns defined with the following data types: `LOB`, `LONG`, `LONG RAW`, `VARRAY`, `NESTED TABLE`, `BFILE`, `REF`, `TIMESTAMP WITH TIME ZONE`.

Composite Foreign key constraints comprised from multiple columns can’t have more than 32 columns.

Foreign key constraints can’t be created in a `CREATE TABLE` statement with a subquery clause.

A referenced primary key or unique constraint on a parent table must be created before the foreign key creation command.

**ON DELETE clause**

The `ON DELETE` clause specifies the effect of deleting values from a parent table on the referenced records of a child table. If the `ON DELETE` clause isn’t specified, Oracle doesn’t allow deletion of referenced key values in a parent table that has dependent rows in the child table.

- `ON DELETE CASCADE` — Dependent foreign key values in a child table are removed along with the referenced values from the parent table.
- `ON DELETE NULL` — Dependent foreign key values in a child table are updated to NULL.

**Examples**

Create an inline foreign key with a user-defined constraint name.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMBER PRIMARY KEY,
  FIRST_NAME VARCHAR2(20),
  LAST_NAME VARCHAR2(25),
  EMAIL VARCHAR2(25) ,
  DEPARTMENT_ID REFERENCES DEPARTMENTS(DEPARTMENT_ID));
```

Create an Out-Of-Line foreign key with a system-generated constraint name.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMBER PRIMARY KEY,
  FIRST_NAME VARCHAR2(20),
  LAST_NAME VARCHAR2(25),
  EMAIL VARCHAR2(25),
  DEPARTMENT_ID NUMBER,
  CONSTRAINT FK_FEP_ID
  FOREIGN KEY(DEPARTMENT_ID) REFERENCES DEPARTMENTS(DEPARTMENT_ID));
```

Create a foreign key using the `ON DELETE CASCADE` clause.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMBER PRIMARY KEY,
  FIRST_NAME VARCHAR2(20),
  LAST_NAME VARCHAR2(25),
  EMAIL VARCHAR2(25),
  DEPARTMENT_ID NUMBER,
  CONSTRAINT FK_FEP_ID
  FOREIGN KEY(DEPARTMENT_ID) REFERENCES DEPARTMENTS(DEPARTMENT_ID)
  ON DELETE CASCADE);
```

Add a foreign key to an existing table.

```
ALTER TABLE EMPLOYEES
  ADD CONSTRAINT FK_FEP_ID
  FOREIGN KEY(DEPARTMENT_ID) REFERENCES DEPARTMENTS(DEPARTMENT_ID);
```

### UNIQUE constraints

A unique constraint is similar to a primary key constraint. It specifies that the values in a single column, or combination of columns, must be unique and can’t repeat in multiple rows.

The main difference from primary key constraint is that a unique constraint can contain NULL values. NULL values in multiple rows are also supported provided the combination of values is unique.

**Limitations**

A unique constraint can’t be created on columns defined with the following data types: `LOB`, `LONG`, `LONG RAW`, `VARRAY`, `NESTED TABLE`, `BFILE`, `REF`, `TIMESTAMP WITH TIME ZONE`.

A unique constraint comprised from multiple columns can’t have more than 32 columns.

Primary key and unique constraints can’t be created on the same column or columns.

**Example**

Create an inline unique Constraint.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMBER PRIMARY KEY,
  FIRST_NAME VARCHAR2(20),
  LAST_NAME VARCHAR2(25),
  EMAIL VARCHAR2(25) CONSTRAINT UNIQ_EMP_EMAIL UNIQUE,
  DEPARTMENT_ID NUMBER);
```

### Check constraints

Check constraints are used to validate values in specific columns that meet specific criteria or conditions. For example, you can use a check constraint on an `EMPLOYEE_EMAIL` column to validate that each record has an @aws.com suffix. If a record fails the check validation, an error is raised and the record isn’t inserted.

Using a check constraint can help transfer some of the logical integrity validation from the application to the database.

When creating a check constraint as inline, it can only be defined on a specific column. When using the out-of-line method, the check constraint can be defined on multiple columns.

**Limitations**

Check constraints can’t perform validation on columns of other tables.

Check constraints can’t be used with functions that aren’t deterministic (e.g. `CURRENT_DATE`).

Check constraints can’t be used with user-defined functions.

Check constrains can’t be used with pseudo columns such as: `CURRVAL`, `NEXTVAL`, `LEVEL`, or `ROWNUM`.

**Example**

Create an inline check constraint that uses a regular expression to validate the email suffix of inserted rows contains @aws.com.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMBER PRIMARY KEY,
  FIRST_NAME VARCHAR2(20),
  LAST_NAME VARCHAR2(25),
  EMAIL VARCHAR2(25)
  CHECK(REGEXP_LIKE (EMAIL, '^[A-Za-z]+@aws.com?{1,3}$')),
  DEPARTMENT_ID NUMBER);
```

### Not Null constraints

A Not Null constraint prevents a column from containing any null values. In order to enable the not null constraint, the keywords `NOT NULL` must be specified during table creation (inline only). Permitting null values is the default if `NOT NULL` isn’t specified.

**Example**

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMBER PRIMARY KEY,
  FIRST_NAME VARCHAR2(20) NOT NULL,
  LAST_NAME VARCHAR2(25) NOT NULL,
  EMAIL VARCHAR2(25),
  DEPARTMENT_ID NUMBER);
```

### REF constraints

REF constraints define a relationship between a column of type REF and the object it references. The REF constraint can be created both inline and out-of-line. Both methods permit defining a scope constraint, a rowid constraint, or a referential integrity constraint based on the REF column.

**Examples**

Create a new Oracle type object.

```
CREATE TYPE DEP_TYPE AS OBJECT (
  DEP_NAME VARCHAR2(60),
  DEP_ADDRESS VARCHAR2(300));
```

Create a table based on the previously created type object.

```
CREATE TABLE DEPARTMENTS_OBJ_T OF DEP_TYPE;
```

Create the `EMPLOYEES` table with a reference to the previously created `DEPARTMENTS` table that is based on the `DEP_TYPE` object:

```
CREATE TABLE EMPLOYEES (
  EMP_NAME VARCHAR2(60),
  EMP_EMAIL VARCHAR2(60),
  EMP_DEPT REF DEPARTMENT_TYP REFERENCES DEPARTMENTS_OBJ_T);
```

### Special constraint states

Oracle provides granular control of database constraint enforcement. For example, you can disable constraints temporarily while making modifications to table data.

Constraint states can be defined using the `CREATE TABLE` or `ALTER TABLE` statements. The following constraint states are supported:

- `DEFERRABLE` — Enables the use of the `SET CONSTRAINT` clause in subsequent transactions until a `COMMIT` statement is submitted.
- `NOT DEFERRABLE` — Disables the use of the `SET CONSTRAINT` clause.
- `INITIALLY IMMEDIATE` — Checks the constraint at the end of each subsequent SQL statement (this state is the default).
- `INITIALLY DEFERRED` — Checks the constraint at the end of subsequent transactions.
- `VALIDATE` or `NO VALIDATE` — These parameters depend on whether the constraint is `ENABLED` or `DISABLED`.
- `ENABLE` or `DISABLE` — Specifies if the constraint should be enforced after creation (`ENABLE` by default). Several options are available when using `ENABLE` or `DISABLE`:
  - `ENABLE VALIDATE` — Enforces that the constraint applies to all existing and new data.
  - `ENABLE NOVALIDATE` — Only new data complies with the constraint.
  - `DISABLE VALIDATE` — A valid constraint is created in disabled mode with no index.
  - `DISABLE NOVALIDATE` — The constraint is created in disabled mode without validation of new or existing data.

**Examples**

Create a unique constraint with a state of `DEFERRABLE`.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMBER PRIMARY KEY,
  FIRST_NAME VARCHAR2(20),
  LAST_NAME VARCHAR2(25),
  EMAIL VARCHAR2(25) CONSTRAINT UNIQ_EMP_EMAIL UNIQUE DEFERRABLE,
  DEPARTMENT_ID NUMBER);
```

Modify the state of the constraint to `ENABLE NOVALIDATE`.

```
ALTER TABLE EMPLOYEES
  ADD CONSTRAINT CHK_EMP_NAME CHECK(FIRST_NAME LIKE 'a%')
  ENABLE NOVALIDATE;
```

### Using existing indexes to enforce constraint integrity

Primary key and unique constraints can be created based on an existing index to enforce the constraint integrity instead of implicitly creating a new index during constraint creation.

**Example**

Create a unique constraint based on an existing index.

```
CREATE UNIQUE INDEX IDX_EMP_ID ON EMPLOYEES(EMPLOYEE_ID);

ALTER TABLE EMPLOYEES
  ADD CONSTRAINT PK_CON_UNIQ
  PRIMARY KEY(EMPLOYEE_ID) USING INDEX IDX_EMP_ID;
```

For more information, see [CREATE TABLE](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TABLE.html#GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6 "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TABLE.html#GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6") in the _Oracle documentation_.

## PostgreSQL usage

PostgreSQL supports the following types of table constraints:

- PRIMARY KEY
- FOREIGN KEY
- UNIQUE
- NOT NULL
- EXCLUDE (unique to PostgreSQL)

###### Note

PostgreSQL doesn’t support Oracle `REF` constraint.

Similar to constraint declaration in Oracle, in PostgreSQL you can create constraints in-line or out-of-line when you specify table columns.

You can specify PostgreSQL constraints using `CREATE` or `ALTER TABLE`. Views aren’t supported.

You need privileges on the table in which constrains are created. For foreign key constraints, you need the `REFERENCES` privilege.

### Primary key constraints

Primary key constraints uniquely identify each record and can’t contain a NULL value. You can use the same ANSI SQL syntax as Oracle.

You can create primary key constraints on a single column or on multiple columns (composite primary keys) as the only `PRIMARY KEY` in a table.

Create a `PRIMARY KEY` constraint creates a unique B-Tree index automatically on the column or group of columns marked as the primary key of the table.

Constraint names can be generated automatically by PostgreSQL or explicitly specified during constraint creation.

**Examples**

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
CREATE TABLE EMPLOYEES(
  EMPLOYEE_ID NUMERIC,
  FIRST_NAME VARCHAR(20),
  LAST_NAME VARCHAR(25),
  EMAIL VARCHAR(25));
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

### Foreign key constraints

Foreign key constraints enforces referential integrity in the database. Values in specific columns or group of columns must match the values from another table (or column).

To create a `FOREIGN KEY` constraint in PostgreSQL, use the same ANSI SQL syntax as in Oracle. You can create a foreign key constraint in-line or out-of-line during table creation.

Use the `REFERENCES` clause to specify the table referenced by the foreign key constraint. When you specify `REFERENCES` in absence of a column list in the referenced table, the `PRIMARY KEY` of the referenced table is used as the referenced column or columns.

A table can have multiple `FOREIGN KEY` constraints to describe its relationships with other tables.

Use the `ON DELETE` clause to handle cases of `FOREIGN KEY` parent records deletions (such as cascading deletes).

Foreign key constraint names are generated automatically by the database or specified explicitly during constraint creation.

### Foreign key and the ON DELETE clause

PostgreSQL provides three main options to handle cases where data is deleted from the parent table and a child table is referenced by a `FOREIGN KEY` constraint. By default, without specifying any additional options, PostgreSQL will use the `NO ACTION` method and raise an error if the referencing rows still exist when the constraint is verified.

- `ON DELETE CASCADE` — Any dependent foreign key values in the child table are removed along with the referenced values from the parent table.
- `ON DELETE RESTRICT` — Prevents the deletion of referenced values from the parent table and the deletion of dependent foreign key values in the child table.
- `ON DELETE NO ACTION` — Performs no action (the default action). The fundamental difference between `RESTRICT` and `NO ACTION` is that `NO ACTION` allows the check to be postponed until later in the transaction; `RESTRICT` doesn’t.

### Foreign key and the ON UPDATE clause

Handling updates on `FOREIGN KEY` columns is also available using the `ON UPDATE` clause, which shares the same options as the `ON DELETE` clause:

- `ON UPDATE CASCADE`
- `ON UPDATE RESTRICT`
- `ON UPDATE NO ACTION`

###### Note

Oracle doesn’t provide an `ON UPDATE` clause.

**Examples**

Create an inline foreign key with a user-specified constraint name.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMERIC PRIMARY KEY,
  FIRST_NAME VARCHAR(20),
  LAST_NAME VARCHAR(25),
  EMAIL VARCHAR(25),
  DEPARTMENT_ID NUMERIC REFERENCES DEPARTMENTS(DEPARTMENT_ID));
```

PostgreSQL foreign key columns must have a specified data type while Oracle doesn’t.

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
ALTER TABLE EMPLOYEES
  ADD CONSTRAINT FK_FEP_ID
    FOREIGN KEY(DEPARTMENT_ID)
    REFERENCES DEPARTMENTS(DEPARTMENT_ID);
```

### UNIQUE constraints

`UNIQUE` constraints ensures that a value in a column, or a group of columns, is unique across the entire table. PostgreSQL `UNIQUE` constraint syntax is ANSI SQL compatible.

PostgreSQL automatically creates a B-Tree index on the respective column, or a group of columns, when creating a `UNIQUE` constraint.

If duplicate values exist in the column(s) on which the constraint was defined during `UNIQUE` constraint creation, the `UNIQUE` constraint creation fails, returning an error message.

`UNIQUE` constraints in PostgreSQL will accept multiple NULL values (similar to Oracle). `UNIQUE` constraint naming can be system-generated or explicitly specified.

**Example**

Create an inline unique constraint ensuring uniqueness of values in the email column.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMERIC PRIMARY KEY,
  FIRST_NAME VARCHAR(20),
  LAST_NAME VARCHAR(25),
  EMAIL VARCHAR(25) CONSTRAINT UNIQ_EMP_EMAIL UNIQUE,
  DEPARTMENT_ID NUMERIC);
```

### CHECK constraints

`CHECK` constraints enforce that values in a column satisfy a specific requirement. `CHECK` constraints in PostgreSQL use the same ANSI SQL syntax as Oracle.

You can only define `CHECK` constraints using a Boolean data type to evaluate the values of a column.

`CHECK` constraints naming can be system-generated or explicitly specified by the user during constraint creation.

**Example**

Create an inline `CHECK` constraint, using a regular expression, to enforce that the email column contains email addresses with the @aws.com suffix.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMERIC PRIMARY KEY,
  FIRST_NAME VARCHAR(20),
  LAST_NAME VARCHAR(25),
  EMAIL VARCHAR(25) CHECK(EMAIL ~ '(^[A-Za-z]+@aws.com$)'),
  DEPARTMENT_ID NUMERIC);
```

### NOT NULL constraints

`NOT NULL` constraints enforce that a column can’t accept NULL values. This behavior is different from the default column behavior in PostgreSQL where columns can accept NULL values. `NOT NULL` constraints can only be defined inline, during table creation (similar to Oracle).

`NOT NULL` constraints in PostgreSQL use the same ANSI SQL syntax as Oracle. You can explicitly specify names for `NOT NULL` constraints when used with a CHECK constraint.

**Example**

Define two not null constraints on the `FIRST_NAME` and `LAST_NAME` columns. Define a check constraint (with an explicitly user-specified name) to enforce not null behavior on the `EMAIL` column.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMERIC PRIMARY KEY,
  FIRST_NAME VARCHAR(20) NOT NULL,
  LAST_NAME VARCHAR(25) NOT NULL,
  EMAIL VARCHAR(25) CONSTRAINT CHK_EMAIL
  CHECK(EMAIL IS NOT NULL));
```

### Constraint states

Similarly to Oracle, PostgreSQL provides controls for certain aspects of constraint behavior. Using the PostgreSQL `SET CONSTRAINTS` statement, constraints can be defined as.

- `DEFERRABLE` — Allows you to use the `SET CONSTRAINTS` statement to set the behavior of constraint checking within the current transaction until transaction commit.
- `IMMEDIATE` — Constraints are enforced only at the end of each statement. Each constraint has its own `IMMEDIATE` or `DEFERRED` mode (same as Oracle)
- `NOT DEFERRABLE` — This statement always runs as `IMMEDIATE` and isn’t affected by the `SET CONSTRAINTS` command.

**PostgreSQL SET CONSTRAINTS Synopsis**

```
SET CONSTRAINTS { ALL | name [, ...] } { DEFERRED | IMMEDIATE }
```

- `VALIDATE CONSTRAINT` — Validates foreign key or check constraints (only) that were previously created as NOT VALID. This action performs a validation check by scanning the table to ensure that all records satisfy the constraint definition.
- `NOT VALID` — Can be used only for foreign key or check constraints. When specified, new records aren’t validated with the creation of the constraint. Only when the `VALIDATE CONSTRAINT` state is applied does the constraint state is enforced on all records.

**Example**

```
ALTER TABLE EMPLOYEES ADD CONSTRAINT FK_DEPT
  FOREIGN KEY (department_id)
  REFERENCES DEPARTMENTS (department_id) NOT VALID;

ALTER TABLE EMPLOYEES VALIDATE CONSTRAINT FK_DEPT;
```

**Using Existing Indexes During Constraint Creation**

PostgreSQL can add a new primary key or unique constraints based on an existing unique index. All the index columns are included in the constraint. When creating constraints using this method, the index is owned by the constraint. When dropping the constraint, the index is also dropped.

**Example**

Use an existing unique index to create a primary key constraint.

```
CREATE UNIQUE INDEX IDX_EMP_ID ON EMPLOYEES(EMPLOYEE_ID);

ALTER TABLE EMPLOYEES
  ADD CONSTRAINT PK_CON_UNIQ PRIMARY KEY USING INDEX IDX_EMP_ID;
```

### Summary

| Oracle constraint or parameter | PostgreSQL constraint or parameter                  |
| ------------------------------ | --------------------------------------------------- |
| PRIMARY KEY                    | PRIMARY KEY                                         |
| FOREIGN KEY                    | FOREIGN KEY                                         |
| UNIQUE                         | UNIQUE                                              |
| CHECK                          | CHECK                                               |
| NOT NULL                       | NOT NULL                                            |
| REF                            | Not Supported                                       |
| DEFERRABLE                     | DEFERRABLE                                          |
| NOT DEFERRABLE                 | NOT DEFERRABLE                                      |
| SET CONSTRAINTS                | SET CONSTRAINTS                                     |
| INITIALLY IMMEDIATE            | INITIALLY IMMEDIATE                                 |
| INITIALLY DEFERRED             | INITIALLY DEFERRED                                  |
| ENABLE                         | Default, not supported as keyword                   |
| DISBALE                        | Not supported as keyword, NOT VALID can use instead |
| ENABLE VALIDATE                | Default, not supported as keyword                   |
| ENABLE NOVALIDATE              | NOT VALID                                           |
| DISABLE VALIDATE               | Not supported                                       |
| DISABLE NOVALIDATE             | Not supported                                       |
| USING_INDEX_CLAUSE             | table_constraint_using_index                        |
| View Constraints               | Not supported                                       |
| Metadata: DBA_CONSTRAINTS      | Metadata: PG_CONSTRAINT                             |

For more information, see
[Constraints](https://www.postgresql.org/docs/13/ddl-constraints.html "https://www.postgresql.org/docs/13/ddl-constraints.html"), [SET CONSTRAINTS](https://www.postgresql.org/docs/13/sql-set-constraints.html "https://www.postgresql.org/docs/13/sql-set-constraints.html"), and [ALTER TABLE](https://www.postgresql.org/docs/13/sql-altertable.html "https://www.postgresql.org/docs/13/sql-altertable.html") in the _PostgreSQL documentation_.
