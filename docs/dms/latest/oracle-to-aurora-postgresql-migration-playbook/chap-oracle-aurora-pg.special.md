# Oracle and PostgreSQL views

With AWS DMS, you can create database views on source and target databases to simplify data access and transformation during migration. Views are virtual tables that derive their data from one or more underlying base tables or views. They provide a logical representation of data without duplicating or moving the base data.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                          | Key differences |
| ------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| Four star feature compatibility | Four star automation level         | [Views](chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.views "chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.views") | N/A             |

## Oracle usage

Database Views store a named SQL query in the Oracle Data Dictionary with a predefined structure. A view doesn’t store actual data and may be considered a virtual table or a logical table based on the data from one or more physical database tables.

**Privileges**

A user needs the `CREATE VIEW` privilege to create a view in their own schema. A user needs the `CREATE ANY VIEW` privilege to create a view in any schema.

The owner of a needs all the necessary privileges on the source tables or views on which the view is based (`SELECT` or `DML` privileges).

**CREATE (OR REPLACE) VIEW statements**

- `CREATE VIEW` creates a new view.
- `CREATE OR REPLACE` overwrites an existing view and modifies the view definition without having to manually drop and recreate the original view, and without deleting the previously granted privileges.

**Oracle common view parameters**

| Oracle view parameter    | Description                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `CREATE OR REPLACE`      | Recreate an existing view (if one exists) or create a new view.                                              |
| `FORCE`                  | Create the view regardless of the existence of the source tables or views and regardless of view privileges. |
| `VISIBLE` or `INVISIBLE` | Specify if a column based on the view is visible or invisible.                                               |
| `WITH READ ONLY`         | Disable DML commands.                                                                                        |
| `WITH CHECK OPTION`      | Specifies the level of enforcement when performing DML commands on the view.                                 |

**Examples**

Views are classified as either simple or complex.

A simple view is a view having a single source table with no aggregate functions. DML operations can be performed on simple views and affect the base table(s). The following example creates and updates a simple View.

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

A complex view is a view with several source tables or views containing joins, aggregate (group) functions, or an order by clause. Performing DML operations on complex views can’t be done directly, but `INSTEAD OF` triggers can be used as a workaround. The following example creates and updates a complex view.

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

## PostgreSQL usage

PostgreSQL views share functionality with Oracle views. Creating a view defines a stored query based on one or more physical database tables which runs every time the view is accessed.

Views with `INSTEAD INSERT` triggers can be used with `COPY` command, with this synopsis.

```
COPY view FROM source;
```

Starting with PostgreSQL 13 it is now possible to rename view columns using `ALTER VIEW` command, this will help the DBA to avoid dropping and recreating the view in order to change a column name.

The following syntax was added to the `ALTER VIEW`:

```
ALTER VIEW [ IF EXISTS ] name RENAME [ COLUMN ] column_name TO new_column_name
```

Prior to PostgreSQL 13 the capability was there but in order to change the view’s column name the DBA had to use the `ALTER TABLE` command.

**PostgreSQL View Synopsis**

```
CREATE [ OR REPLACE ] [ TEMP | TEMPORARY ] [ RECURSIVE ] VIEW name [ (
column_name [, ...] ) ]
[ WITH ( view_option_name [= view_option_value] [, ... ] ) ]
AS query
[ WITH [ CASCADED | LOCAL ] CHECK OPTION ]
```

**PostgreSQL view privileges**

A Role or user must be granted `SELECT` and `DML` privileges on the base tables or views in order to create a view.

For more information, see [GRANT](https://www.postgresql.org/docs/10/sql-grant.html "https://www.postgresql.org/docs/10/sql-grant.html") in the _PostgreSQL documentation_.

**PostgreSQL view parameters**

- `CREATE [OR REPLACE] VIEW` — Similar to the Oracle syntax. When you re-create an existing view, the new view must have the same column structure as generated by the original view (column names, column order and data types). As such, it is sometimes preferable to drop the view and use the `CREATE VIEW` statement instead.

```
CREATE [OR REPLACE] VIEW VW_NAME AS SELECT COLUMNS FROM TABLE(s) [WHERE CONDITIONS];
DROP VIEW [IF EXISTS] VW_NAME;
```

The `IF EXISTS` parameter is optional.

- `WITH [ CASCADED | LOCAL ] CHECK OPTION` — DML `INSERT` and `UPDATE` operations are verified against the view-based tables to ensure that new rows satisfy the original structure conditions or the view-defining condition. If a conflict is detected, the DML operation fails.

`CHECK OPTION` can be `LOCAL` or `CASCADED`. `LOCAL` verifies against the view without a hierarchical check. `CASCADED` verifies all underlying base views using a hierarchical check.

**Executing DML commands on views**

PostgreSQL simple views are automatically updatable. Unlike Oracle views, no restrictions exist when performing DML operations against views. An updatable view may contain a combination of updatable and non-updatable columns. A column is updatable if it references an updatable column of the underlying base table. If not, the column is read-only and an error is raised if an `INSERT` or `UPDATE` statement is attempted on the column.

**Examples**

Creating and updating a view without the `CHECK OPTION` parameter.

```
CREATE OR REPLACE VIEW VW_DEP AS
SELECT DEPARTMENT_ID, DEPARTMENT_NAME,
MANAGER_ID, LOCATION_ID FROM DEPARTMENTS
WHERE LOCATION_ID=1700;

view VW_DEP created.

UPDATE VW_DEP SET LOCATION_ID=1600;

21 rows updated.
```

Creating and updating a view with the `LOCAL CHECK OPTION` parameter.

```
CREATE OR REPLACE VIEW VW_DEP AS
SELECT DEPARTMENT_ID, DEPARTMENT_NAME,
MANAGER_ID, LOCATION_ID FROM DEPARTMENTS
WHERE LOCATION_ID=1700 WITH LOCAL CHECK OPTION;

view VW_DEP created.

UPDATE VW_DEP SET LOCATION_ID=1600;

SQL Error: ERROR: new row violates check option for view "vw_dep"
```

For more information, see [Views](https://www.postgresql.org/docs/13/tutorial-views.html "https://www.postgresql.org/docs/13/tutorial-views.html") and [CREATE VIEW](https://www.postgresql.org/docs/13/sql-createview.html "https://www.postgresql.org/docs/13/sql-createview.html") in the _PostgreSQL documentation_.
