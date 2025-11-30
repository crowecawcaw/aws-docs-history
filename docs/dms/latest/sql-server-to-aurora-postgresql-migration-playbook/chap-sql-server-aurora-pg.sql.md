# Case sensitivity differences for ANSI SQL

This topic provides reference information on handling object name case sensitivity when migrating from Microsoft SQL Server 2019 to Amazon Aurora PostgreSQL. You can use this information to ensure proper naming conventions and avoid potential conflicts during the migration process.

Object name case sensitivity might be different for SQL Server and PostgreSQL. By default, SQL Server names are case insensitive. However, you can create a case sensitive SQL Server database by changing the `COLLATION` property. In PostgreSQL, object names are case insensitive.

By default, the AWS Schema Conversion Tool (AWS SCT) uses object names in lowercase for PostgreSQL. If your source code includes objects with identical names in different case, make sure that you keep unique names in your converted code. You can enclose object names in double quotation marks or change the names manually.

In addition to this, you can use AWS Database Migration Service transformation actions to change schema, table, and column names to lowercase. For more information, see [Transformation rules and actions](../userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md "../userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md").

To use an uppercase name, enclose object names with double quotation marks. The following code example shows how to create the `EMPLOYEES` table in uppercase.

```
CREATE TABLE "EMPLOYEES" (
  EMP_ID NUMERIC PRIMARY KEY,
  EMP_FULL_NAME VARCHAR(60) NOT NULL,
  AVG_SALARY NUMERIC NOT NULL);
```

The following PostgreSQL command creates the `employees` table in lowercase.

```
CREATE TABLE EMPLOYEES (
  EMP_ID NUMERIC PRIMARY KEY,
  EMP_FULL_NAME VARCHAR(60) NOT NULL,
  AVG_SALARY NUMERIC NOT NULL);
```

If you don’t use double quotation marks, then PostgreSQL creates objects with lowercase names. To create, query, or manage PostgreSQL database objects with names in uppercase or mixed case, use double quotation marks.
