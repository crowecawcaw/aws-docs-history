# Case sensitivity differences for Oracle and PostgreSQL

Object name case sensitivity is different for Oracle and PostgreSQL. Oracle names aren’t case sensitive. PostgreSQL names are case sensitive.

By default, AWS SCT uses object name in lower-case for PostgreSQL. In most cases, you’ll want to use AWS DMS transformations to change schema, table, and column names to lower case.

To have an upper-case name, you must place the objects names within doubles quotes.

For example, to create a table named `EMPLOYEES` (upper-case) in PostgreSQL, you should use the following

```
CREATE TABLE "EMPLOYEES" (
  EMP_ID NUMERIC PRIMARY KEY,
  EMP_FULL_NAME VARCHAR(60) NOT NULL,
  AVG_SALARY NUMERIC NOT NULL);
```

The following command creates a table named employees (lower-case).

```
CREATE TABLE EMPLOYEES (
  EMP_ID NUMERIC PRIMARY KEY,
  EMP_FULL_NAME VARCHAR(60) NOT NULL,
  AVG_SALARY NUMERIC NOT NULL);
```

If you don’t use doubles quotes, PostgreSQL looks for object names in their lower-case form. For `CREATE` commands where you don’t use doubles quotes, PostgreSQL creates objects with lower-case names. Therefore, to create, query, or manipulate an upper-cased (or mixed) object names, use doubles quotes.
