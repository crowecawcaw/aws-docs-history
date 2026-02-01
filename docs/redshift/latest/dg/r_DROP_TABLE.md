Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DROP TABLE

Removes a table from a database.

If you are trying to empty a table of rows, without removing the table, use the DELETE
or TRUNCATE command.

DROP TABLE removes constraints that exist on the target table. Multiple tables can be
removed with a single DROP TABLE command.

DROP TABLE with an external table can't be run inside a transaction (BEGIN … END).
For more information about transactions, see [Isolation levels in Amazon Redshift](c_serial_isolation.md "c_serial_isolation.md").

To find an example where the DROP privilege is granted to a group, see GRANT [Examples](r_GRANT-examples.md "r_GRANT-examples.md").

## Required privileges

Following are required privileges for DROP TABLE:

- Superuser
- Users with the DROP TABLE privilege
- Table owner with the USAGE privilege on the schema

## Syntax

```
DROP TABLE [ IF EXISTS ] *name* [, ...] [ CASCADE | RESTRICT ]
```

## Parameters

IF EXISTS

Clause that indicates that if the specified table doesn’t exist, the command
should make no changes and return a message that the table doesn't exist,
rather than terminating with an error.

This clause is useful when scripting, so the script doesn’t fail if DROP
TABLE runs against a nonexistent table.

_name_

Name of the table to drop.

CASCADE

Clause that indicates to automatically drop objects that depend on the
table, such as views.

To create a view that isn't dependent on other database objects, such
as views and tables, include the WITH NO SCHEMA BINDING clause in the view
definition. For more information, see [CREATE VIEW](r_CREATE_VIEW.md "r_CREATE_VIEW.md").

RESTRICT

Clause that indicates not to drop the table if any objects depend on it.
This action is the default.

## Examples

**Dropping a table with no dependencies**

The following example creates and drops a table called FEEDBACK that has no
dependencies:

```
create table feedback(a int);

drop table feedback;
```

If a table contains columns that are referenced by views or other tables, Amazon Redshift
displays a message such as the following.

```
Invalid operation: cannot drop table feedback because other objects depend on it
```

**Dropping two tables simultaneously**

The following command set creates a FEEDBACK table and a BUYERS table and then drops
both tables with a single command:

```
create table feedback(a int);

create table buyers(a int);

drop table feedback, buyers;

```

**Dropping a table with a dependency**

The following steps show how to drop a table called FEEDBACK using the CASCADE
switch.

First, create a simple table called FEEDBACK using the CREATE TABLE command:

```
create table feedback(a int);
```

Next, use the CREATE VIEW command to create a view called FEEDBACK_VIEW that relies
on the table FEEDBACK:

```
create view feedback_view as select * from feedback;
```

The following example drops the table FEEDBACK and also drops the view
FEEDBACK_VIEW, because FEEDBACK_VIEW is dependent on the table FEEDBACK:

```
drop table feedback cascade;
```

**Viewing the dependencies for a table**

To return the dependencies for your table, use the following example. Replace
`my_schema` and `my_table` with
your own schema and table.

```
`SELECT dependent_ns.nspname as dependent_schema
, dependent_view.relname as dependent_view
, source_ns.nspname as source_schema
, source_table.relname as source_table
, pg_attribute.attname as column_name
FROM pg_depend
JOIN pg_rewrite ON pg_depend.objid = pg_rewrite.oid
JOIN pg_class as dependent_view ON pg_rewrite.ev_class = dependent_view.oid
JOIN pg_class as source_table ON pg_depend.refobjid = source_table.oid
JOIN pg_attribute ON pg_depend.refobjid = pg_attribute.attrelid
 AND pg_depend.refobjsubid = pg_attribute.attnum
JOIN pg_namespace dependent_ns ON dependent_ns.oid = dependent_view.relnamespace
JOIN pg_namespace source_ns ON source_ns.oid = source_table.relnamespace
WHERE
source_ns.nspname = 'my_schema'
AND source_table.relname = 'my_table'
AND pg_attribute.attnum > 0
ORDER BY 1,2
LIMIT 10;`
```

To drop `my_table` and its dependencies, use the following
example. This example also returns all dependencies for the table that has been
dropped.

```
`DROP TABLE my_table CASCADE;

SELECT dependent_ns.nspname as dependent_schema
, dependent_view.relname as dependent_view
, source_ns.nspname as source_schema
, source_table.relname as source_table
, pg_attribute.attname as column_name
FROM pg_depend
JOIN pg_rewrite ON pg_depend.objid = pg_rewrite.oid
JOIN pg_class as dependent_view ON pg_rewrite.ev_class = dependent_view.oid
JOIN pg_class as source_table ON pg_depend.refobjid = source_table.oid
JOIN pg_attribute ON pg_depend.refobjid = pg_attribute.attrelid
 AND pg_depend.refobjsubid = pg_attribute.attnum
JOIN pg_namespace dependent_ns ON dependent_ns.oid = dependent_view.relnamespace
JOIN pg_namespace source_ns ON source_ns.oid = source_table.relnamespace
WHERE
source_ns.nspname = 'my_schema'
AND source_table.relname = 'my_table'
AND pg_attribute.attnum > 0
ORDER BY 1,2
LIMIT 10;`

`+------------------+----------------+---------------+--------------+-------------+
| dependent_schema | dependent_view | source_schema | source_table | column_name |
+------------------+----------------+---------------+--------------+-------------+`
```

**Dropping a table Using IF EXISTS**

The following example either drops the FEEDBACK table if it exists, or does nothing
and returns a message if it doesn't:

```
drop table if exists feedback;
```
