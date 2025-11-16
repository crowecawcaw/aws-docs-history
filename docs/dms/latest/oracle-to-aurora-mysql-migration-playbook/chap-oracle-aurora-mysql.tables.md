# Oracle and MySQL table constraints

With AWS DMS, you can enforce data integrity rules on tables in Oracle and MySQL databases during migration. Table constraints are database objects that define rules for the data in a table. They prevent invalid data from being entered into the database and maintain consistency across related tables. The following sections will provide details on supported constraint types, configuration options, and best practices for managing table constraints during database migration using AWS DMS.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                        | Key differences                                                                                                       |
| ------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| Four star feature compatibility | Four star automation level         | [Constraints](chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.constraints "chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.constraints") | MySQL doesn’t support `REF`, `ENABLE`, `DEFERRABLE`, and `DISABLE`. Also, MySQL doesn’t support constraints on views. |

## Oracle usage

Oracle provides six types of constraints to enforce data integrity on table columns. Constraints ensure data inserted into tables is controlled and satisfies logical requirements.

### Oracle integrity constraint types

- **Primary key** — Enforces that row values in a specific column are unique and not null.
- **Foreign key** — Enforces that values in the current table exist in the referenced table.
- **Unique** — Prevents data duplication on a column, or combination of columns, and allows one null value.
- **Check** — Enforces that values comply with a specific condition.
- **Not null** — Enforces that null values can’t be inserted into a specific column.
- **REF** — References an object in another object type or in a relational table.

### Oracle constraint creation

You can create new constraints in two ways.

- **Inline** — Defines a constraint as part of a table column declaration.

```
CREATE TABLE EMPLOYEES (
  EMP_ID NUMBER PRIMARY KEY,…);
```

- **Out-of-line** — Defines a constraint as part of the table DDL during table creation.

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

### Privileges

You need privileges on the table where constrains are created and, in case of foreign key constraints, you need the `REFERENCES` privilege on the referenced table.

### PRIMARY KEY constraints

A unique identifier for each record in a database table can appear only once and can’t contain `NULL` values. A table can only have one primary key.

When you create a primary key constraint inline, you can specify only the `PRIMARY KEY` keyword. When you create the constraint out-of-line, you must specify one column or a combination of columns.

Creating a new primary key constraint also implicitly creates a unique index on the primary key column if no index already exists. When dropping a primary key constraint, the system-generated index is also dropped. If a user defined index was used, the index isn’t dropped.

- Primary keys can’t be created on columns defined with the following data types: `LOB`, `LONG`, `LONG RAW`, `VARRAY`, `NESTED TABLE`, `BFILE`, `REF`, `TIMESTAMP WITH TIME ZONE`.

You can use the `TIMESTAMP WITH LOCAL TIME ZONE` data type as a primary key.

- Primary keys can be created from multiple columns (composite PK). They are limited to a total of 32 columns.
- Defining the same column as both a primary key and as a unique constraint isn’t allowed.

#### Examples

Create an inline primary key using a system-generated primary key constraint name.

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

#### Limitations

Foreign keys can’t be created on columns defined with the following data types: `LOB`, `LONG`, `LONG RAW`, `VARRAY`, `NESTED TABLE`, `BFILE`, `REF`, `TIMESTAMP WITH TIME ZONE`.

Composite foreign key constraints comprised from multiple columns can’t have more than 32 columns.

Foreign key constraints can’t be created in a `CREATE TABLE` statement with a subquery clause.

A referenced primary key or unique constraint on a parent table must be created before the foreign key creation command.

### ON DELETE clause

The `ON DELETE` clause specifies the effect of deleting values from a parent table on the referenced records of a child table. If the `ON DELETE` clause isn’t specified, Oracle doesn’t allow deletion of referenced key values in a parent table that has dependent rows in the child table.

- `ON DELETE CASCADE` — Dependent foreign key values in a child table are removed along with the referenced values from the parent table.
- `ON DELETE NULL` — Dependent foreign key values in a child table are updated to NULL.

### Examples

Create an inline foreign key with a user-defined constraint name.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMBER PRIMARY KEY,
  FIRST_NAME VARCHAR2(20),
  LAST_NAME VARCHAR2(25),
  EMAIL VARCHAR2(25) ,
  DEPARTMENT_ID REFERENCES DEPARTMENTS(DEPARTMENT_ID));
```

Create an out-of-line foreign key with a system-generated constraint name.

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

#### Limitations

A unique constraint can’t be created on columns defined with the following data types: `LOB`, `LONG`, `LONG RAW`, `VARRAY`, `NESTED TABLE`, `BFILE`, `REF`, `TIMESTAMP WITH TIME ZONE`.

A unique constraint comprised from multiple columns can’t have more than 32 columns.

Primary key and unique constraints can’t be created on the same column or columns.

#### Example

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

When you create a check constraint as inline, it can only be defined on a specific column. When using the out-of-line method, the check constraint can be defined on multiple columns.

#### Limitations

Check constraints can’t perform validation on columns of other tables.

Check constraints can’t be used with functions that aren’t deterministic (for example, `CURRENT_DATE`).

Check constraints can’t be used with user-defined functions.

Check constrains can’t be used with pseudo columns such as: `CURRVAL`, `NEXTVAL`, `LEVEL`, or `ROWNUM`.

#### Example

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

### NOT NULL constraints

A `NOT NULL` constraint prevents a column from containing any null values. To enable the `NOT NULL` constraint, make sure that you specify the `NOT NULL` keyword during table creation (inline only). Permitting null values is the default if `NOT NULL` isn’t specified.

#### Example

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMBER PRIMARY KEY,
  FIRST_NAME VARCHAR2(20) NOT NULL,
  LAST_NAME VARCHAR2(25) NOT NULL,
  EMAIL VARCHAR2(25),
  DEPARTMENT_ID NUMBER);
```

### Referential constraints

Referential constraints define a relationship between a column of type `REF` and the object it references. The `REF` constraint can be created both inline and out-of-line. Both methods permit defining a scope constraint, a row identifier constraint, or a referential integrity constraint based on the `REF` column.

#### Examples

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

#### Examples

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

#### Example

Create a unique constraint based on an existing index.

```
CREATE UNIQUE INDEX IDX_EMP_ID ON EMPLOYEES(EMPLOYEE_ID);

ALTER TABLE EMPLOYEES
  ADD CONSTRAINT PK_CON_UNIQ
  PRIMARY KEY(EMPLOYEE_ID) USING INDEX IDX_EMP_ID;
```

For more information, see [CREATE TABLE](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TABLE.html#GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6 "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TABLE.html#GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6") in the _Oracle documentation_.

## MySQL usage

MySQL supports the following types of table constraints:

- PRIMARY KEY
- FOREIGN KEY
- UNIQUE
- NOT NULL
- ENUM (unique to MySQL)
- SET (unique to MySQL)

###### Note

MySQL doesn’t support Oracle `REF` constraint.

Similar to constraint declaration in Oracle, in MySQL you can create constraints in-line or out-of-line when you specify table columns.

You can specify MySQL constraints using `CREATE` or `ALTER TABLE`. Views aren’t supported.

You need privileges on the table in which constrains are created. For foreign key constraints, you need the `REFERENCES` privilege.

### Primary key constraints

Primary key constraints uniquely identify each record and can’t contain a NULL value.

Primary key constraint marks the column on which the table’s heap is sorted (in the InnoDB storage engine, like Oracle IOT).

Primary key constraint uses the same ANSI SQL syntax as Oracle.

You can create a primary key constraint on a single column, or on multiple columns (composite primary keys), as the only `PRIMARY KEY` in a table.

Primary key constraint creates a unique B-tree index automatically on the column, or group of columns, marked as the primary key of the table.

Constraint names can be generated automatically by MySQL. If a name is explicitly specified during constraint creation, the constraint name is `PRIMARY`.

#### Examples

Create an inline primary key constraint with a system-generated constraint name.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMERIC PRIMARY KEY,
  FIRST_NAME VARCHAR(20),
  LAST_NAME VARCHAR(25),
  EMAIL VARCHAR(25));
```

Create an out-of-line primary key constraint. For both examples, the constraint name is `PRIMARY`.

```
CREATE TABLE EMPLOYEES(
    EMPLOYEE_ID NUMERIC,
    FIRST_NAME VARCHAR(20),
    LAST_NAME VARCHAR(25),
    EMAIL VARCHAR(25),
    CONSTRAINT PK_EMP_ID PRIMARY KEY (EMPLOYEE_ID));

or

CREATE TABLE EMPLOYEES(
    EMPLOYEE_ID NUMERIC,
    FIRST_NAME VARCHAR(20),
    LAST_NAME VARCHAR(25)
    EMAIL VARCHAR(25),
    CONSTRAINT PRIMARY KEY (EMPLOYEE_ID));
```

Add a primary key constraint to an existing table.

```
ALTER TABLE SYSTEM_EVENTS
    ADD CONSTRAINT PK_EMP_ID PRIMARY KEY (EVENT_CODE, EVENT_TIME);

or

ALTER TABLE SYSTEM_EVENTS
    ADD CONSTRAINT PRIMARY KEY (EVENT_CODE, EVENT_TIME);

or

ALTER TABLE SYSTEM_EVENTS
    ADD PRIMARY KEY (EVENT_CODE, EVENT_TIME);
```

Drop the primary key.

```
ALTER TABLE SYSTEM_EVENTS DROP PRIMARY KEY;
```

### Foreign key constraints

Important notes about foreign key constraints:

- Enforces referential integrity in the database. Values in specific columns or group of columns must match the values from another table or column.
- Creating a `FOREIGN KEY` constraint in MySQL uses the same ANSI SQL syntax as Oracle.
- Can be created only out-of-line during table creation.
- Use the `REFERENCES` clause to specify the table referenced by the foreign key constraint.
- A table can have multiple `FOREIGN KEY` constraints to describe its relationships with other tables.
- Use the `ON DELETE` clause to handle cases of `FOREIGN KEY` parent records deletions such as cascading deletes.
- Use the `ON UPDATE` clause to handle cases of `FOREIGN KEY` parent records updates such as cascading updates.
- Foreign key constraint names are generated automatically by the database or specified explicitly during constraint creation.

### ON DELETE clause

MySQL provides four options to handle cases where data is deleted from the parent table and a child table is referenced by a `FOREIGN KEY` constraint. By default, without specifying any additional options, MySQL uses the `NO ACTION` method and raises an error if the referencing rows still exist when the constraint is verified.

- `ON DELETE CASCADE` — Removes any dependent foreign key values in the child table along with the referenced values from the parent table.
- `ON DELETE RESTRICT` — Prevents the deletion of referenced values from the parent table and the deletion of dependent foreign key values in the child table.
- `ON DELETE NO ACTION` — Prevents the deletion of referenced values from the parent table and the deletion of dependent foreign key values in the child table (the same as `RESTRICT`).
- `ON DELETE SET NULL` — Deletes the row from the parent table and sets the foreign key column, or columns in the child table, to NULL. If you specify a `SET NULL` action, ensure you have not declared the columns in the child table as `NOT NULL`.

### ON UPDATE clause

Handle updates on `FOREIGN KEY` columns is also available using the `ON UPDATE` clause, which shares the same options as the `ON DELETE` clause:

- `ON UPDATE CASCADE`
- `ON UPDATE RESTRICT`
- `ON UPDATE NO ACTION`

###### Note

Oracle doesn’t provide an `ON UPDATE` clause.

#### Examples

Create an out-of-line foreign key constraint with a system-generated constraint name.

```
CREATE TABLE EMPLOYEES (
    EMPLOYEE_ID NUMERIC PRIMARY KEY,
    FIRST_NAME VARCHAR(20),
    LAST_NAME VARCHAR(25),
    EMAIL VARCHAR(25),
    DEPARTMENT_ID NUMERIC,
    CONSTRAINT FK_FEP_ID FOREIGN KEY(DEPARTMENT_ID)
        REFERENCES DEPARTMENTS(DEPARTMENT_ID));
```

Create a foreign key using the `ON DELETE CASCADE` clause.

```
CREATE TABLE EMPLOYEES (
    EMPLOYEE_ID NUMERIC PRIMARY KEY,
    FIRST_NAME VARCHAR(20),
    LAST_NAME VARCHAR(25),
    EMAIL VARCHAR(25),
    DEPARTMENT_ID NUMERIC,
    CONSTRAINT FK_FEP_ID FOREIGN KEY(DEPARTMENT_ID)
    REFERENCES DEPARTMENTS(DEPARTMENT_ID) ON DELETE CASCADE);
```

Add a foreign key to an existing table.

```
ALTER TABLE EMPLOYEES
    ADD CONSTRAINT FK_FEP_ID
    FOREIGN KEY(DEPARTMENT_ID)
    REFERENCES DEPARTMENTS(DEPARTMENT_ID);
```

### UNIQUE constraints

Important notes about unique constraints:

- Ensures that a value in a column, or a group of columns, is unique across the entire table.
- MySQL `UNIQUE` constraint syntax is ANSI SQL compatible.
- Automatically creates a B-tree index on the respective column, or a group of columns, when creating a UNIQUE constraint.
- If duplicate values exist in the column(s) on which the constraint was defined during `UNIQUE` constraint creation, the `UNIQUE` constraint creation fails and returns an error message.
- `UNIQUE` constraints in MySQL accept multiple NULL values, similar to Oracle.
- `UNIQUE` constraint naming can be system-generated or explicitly specified.

#### Example

Create an inline unique constraint ensuring uniqueness of values in the email column.

```
CREATE TABLE EMPLOYEES (
    EMPLOYEE_ID NUMERIC PRIMARY KEY,
    FIRST_NAME VARCHAR(20),
    LAST_NAME VARCHAR(25),
    EMAIL VARCHAR(25) UNIQUE,
    DEPARTMENT_ID NUMERIC);
```

### Disable integration check

In MySQL, you don’t have an option to `DISABLE` the integration check, but there is a session variable for disabling checks at the session level.

The following example turns on integration checks in the session.

```
SET FOREIGN_KEY_CHECKS=1;
```

The following example turns off integration checks in the session.

```
SET FOREIGN_KEY_CHECKS=0;
```

### Unique MySQL constraints

- `ENUM` — The value must be one of the values listed in the column definition or the internal numeric equivalent. The value can’t be the error value. That is, 0 or the empty string. For a column defined as `ENUM ('a','b','c')`, the values such as `''`, `'d'`, or `'ax'` are not valid and are rejected.
- `SET` — The value must be the empty string or a value consisting only of the values listed in the column definition separated by commas. For a column defined as `SET('a','b','c')`, values such as `'d'` or `'a,b,c,d'` are not valid and are rejected.

### Summary

| Oracle constraint or parameter | MySQL constraint or parameter                                                                |
| ------------------------------ | -------------------------------------------------------------------------------------------- |
| `PRIMARY KEY`                  | `PRIMARY KEY`                                                                                |
| `NOT NULL`                     | `FOREIGN KEY`                                                                                |
| `UNIQUE`                       | `UNIQUE`                                                                                     |
| `CHECK`                        | Not supported, in some cases you can use `ENUM` and `SET`. Can be implemented with triggers. |
| `NOT NULL`                     | `NOT NULL`                                                                                   |
| `REF`                          | Not supported                                                                                |
| `DEFERRABLE`                   | Not supported as keyword, you can use the `FOREIGN_KEY_CHECKS` parameter.                    |
| `NOT DEFERRABLE`               | Not supported as keyword, you can use the `FOREIGN_KEY_CHECKS` parameter.                    |
| `SET CONSTRAINTS`              | Not supported as keyword, you can use the `FOREIGN_KEY_CHECKS` parameter.                    |
| `INITIALLY IMMEDIATE`          | Default, not supported as keyword.                                                           |
| `INITIALLY DEFERRED`           | Not supported                                                                                |
| `ENABLE`                       | Default, not supported as keyword.                                                           |
| `DISBALE`                      | Not supported as keyword, you can use the `FOREIGN_KEY_CHECKS` parameter.                    |
| `ENABLE VALIDATE`              | Default, not supported as keyword                                                            |
| `ENABLE NOVALIDATE`            | Not supported                                                                                |
| `DISABLE VALIDATE`             | Not supported                                                                                |
| `DISABLE NOVALIDATE`           | Default, not supported as keyword                                                            |
| `USING_INDEX_CLAUSE`           | Not supported                                                                                |
| View constraints               | Not supported                                                                                |
| Metadata: `DBA_CONSTRAINTS`    | Metadata: `TABLE_CONSTRAINTS`.                                                               |

For more information, see
[How MySQL Deals with Constraints](https://dev.mysql.com/doc/refman/5.7/en/constraints.html "https://dev.mysql.com/doc/refman/5.7/en/constraints.html"), and [FOREIGN KEY Constraints](https://dev.mysql.com/doc/refman/5.7/en/create-table-foreign-keys.html "https://dev.mysql.com/doc/refman/5.7/en/create-table-foreign-keys.html") in the _MySQL documentation_.
