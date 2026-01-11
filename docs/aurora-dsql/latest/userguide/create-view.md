# `CREATE VIEW`

`CREATE VIEW` defines a new persistent view. Aurora DSQL does not support temporary views;
only permanent views are supported.

## Supported syntax

```
CREATE [ OR REPLACE ] [ RECURSIVE ] VIEW name [ ( column_name [, ...] ) ]
    [ WITH ( view_option_name [= view_option_value] [, ... ] ) ]
    AS query
    [ WITH [ CASCADED | LOCAL ] CHECK OPTION ]
```

## Description

`CREATE VIEW` defines a view of a query. The view is not physically
materialized. Instead, the query is run every time the view is referenced in a query.

`CREATE or REPLACE VIEW` is similar, but if a view of the same name already
exists, it is replaced. The new query must generate the same columns that were generated
by the existing view query (that is, the same column names in the same order and with the
same data types), but it may add additional columns to the end of the list. The
calculations giving rise to the output columns may be different.

If a schema name is given, such as `CREATE VIEW myschema.myview ...`) then
the view is created in the specified schema. Otherwise, it is created in the current
schema.

The name of the view must be distinct from the name of any other relation (table,
index, view) in the same schema.

## Parameters

`CREATE VIEW` supports various parameters to control the behavior of
automatically updatable views.

**`RECURSIVE`**

Creates a recursive view. The syntax: `CREATE RECURSIVE VIEW [ schema . ]
 view_name (column_names) AS SELECT ...;` is equivalent to `CREATE
 VIEW [ schema . ] view_name AS WITH RECURSIVE view_name (column_names) AS
 (SELECT ...) SELECT column_names FROM view_name;`.

A view column name list must be specified for a recursive view.

**`name`**

The name of the view to be created, which may be optionally schema-qualified.
A column name list must be specified for a recursive view.

**`column_name`**

An optional list of names to be used for columns of the view. If not given,
the column names are deduced from the query.

**`WITH ( view_option_name [= view_option_value] [, ... ] )`**

This clause specifies optional parameters for a view; the following parameters
are supported.

- `check_option (enum)` — This parameter may be either
  `local` or `cascaded`, and is equivalent to specifying
  `WITH [ CASCADED | LOCAL ] CHECK OPTION`.
- `security_barrier (boolean)`—This should be used if the
  view is intended to provide row-level security. Aurora DSQL does not currently
  support row-level security, but this option will still force the view's
  `WHERE` conditions (and any conditions using operators which are
  marked as `LEAKPROOF`) to be evaluated first.
- `security_invoker (boolean)`—This option causes the
  underlying base relations to be checked against the privileges of the user of
  the view rather than the view owner. See the notes below for full
  details.

All of the above options can be changed on existing views using `ALTER
 VIEW`.

**`query`**

A `SELECT` or `VALUES` command which will provide the
columns and rows of the view.

**`WITH [ CASCADED | LOCAL ] CHECK OPTION`**

This option controls the behavior of automatically updatable views. When this
option is specified, `INSERT` and `UPDATE` commands
on the view will be checked to ensure that new rows satisfy the
view-defining condition (that is, the new rows are checked to ensure that
they are visible through the view). If they are not, the update will be
rejected. If the `CHECK OPTION` is not specified,
`INSERT` and `UPDATE` commands on the view are
allowed to create rows that are not visible through the view.

`LOCAL`—New rows are only checked against the
conditions defined directly in the view itself. Any conditions defined on
underlying base views are not checked (unless they also specify the
`CHECK OPTION`).

`CASCADED`—New rows are checked against the
conditions of the view and all underlying base views. If the `CHECK
 OPTION` is specified, and neither `LOCAL` nor
`CASCADED` are specified, then `CASCADED` is
assumed.

###### Note

The `CHECK OPTION` may not be used with `RECURSIVE` views. The `CHECK OPTION` is only supported on views that are automatically updatable.

## Notes

Use the `DROP VIEW` statement to drop views.

The names and data types of the view's columns should be carefully considered. For
example, CREATE VIEW vista AS SELECT 'Hello World'; is not recommended because the
column name defaults to `?column?;`. Also, the column data type defaults to
`text`, which might not be what you wanted.

A better approach is to explicitly specify the column name and data type, such as:
`CREATE VIEW vista AS SELECT text 'Hello World' AS hello;`.

By default, access to the underlying base relations referenced in the view is determined by the permissions of the view owner. In some cases, this can be used to provide secure but restricted access to the underlying tables. However, not all views are secure against tampering.

- If the view has the `security_invoker` property set to true, access to the underlying base relations is determined by the permissions of the user executing the query, rather than the view owner. Thus, the user of a security invoker view must have the relevant permissions on the view and its underlying base relations.
- If any of the underlying base relations is a security invoker view, it will be treated as if it had been accessed directly from the original query. Thus, a security invoker view will always check its underlying base relations using the permissions of the current user, even if it is accessed from a view without the `security_invoker` property.
- Functions called in the view are treated the same as if they had been called directly from the query using the view. Therefore, the user of a view must have permissions to call all functions used by the view. Functions in the view are executed with the privileges of the user executing the query or the function owner, depending on whether the functions are defined as `SECURITY INVOKER` or `SECURITY DEFINER`.
- The user creating or replacing a view must have `USAGE` privileges on any schemas referred to in the view query, in order to look up the referenced objects in those schemas.
- When `CREATE OR REPLACE VIEW` is used on an existing view, only the view's defining `SELECT` rule, plus any `WITH ( ... )` parameters and its `CHECK OPTION` are changed. Other view properties, including ownership, permissions, and non-SELECT rules, remain unchanged. You must own the view to replace it (this includes being a member of the owning role).

## Updatable views

Simple views are automatically updatable: the system will allow `INSERT`, `UPDATE`, and `DELETE` statements to be used on the view in the same way as on a regular table. A view is automatically updatable if it satisfies all of the following conditions:

- The view must have exactly one entry in its `FROM` list, which must be a table or another updatable view.
- The view definition must not contain `WITH`, `DISTINCT`, `GROUP BY`, `HAVING`, `LIMIT`, or `OFFSET` clauses at the top level.
- The view definition must not contain set operations (`UNION`, `INTERSECT`, or `EXCEPT`) at the top level.
- The view's select list must not contain any aggregates, window functions, or set-returning functions.

An automatically updatable view may contain a mix of updatable and non-updatable columns. A column is updatable if it's a simple reference to an updatable column of the underlying base relation. Otherwise, the column is read-only, and an error occurs if an `INSERT` or `UPDATE` statement attempts to assign a value to it.

A more complex view that doesn't satisfy all these conditions is read-only by default: the system doesn't allow an insert, update, or delete on the view.

###### Note

The user performing the insert, update, or delete on the view must have the corresponding insert, update, or delete privilege on the view. By default, the view's owner must have the relevant privileges on the underlying base relations, while the user performing the update doesn't need any permissions on the underlying base relations. However, if the view has security_invoker set to true, the user performing the update, rather than the view owner, must have the relevant privileges on the underlying base relations.

## Examples

To create a view consisting of all comedy films.

```
CREATE VIEW comedies AS
    SELECT *
    FROM films
    WHERE kind = 'Comedy';
```

Create a view with `LOCAL CHECK OPTION`.

```
CREATE VIEW pg_comedies AS
    SELECT *
    FROM comedies
    WHERE classification = 'PG'
    WITH CASCADED CHECK OPTION;
```

Create a recursive view.

```
CREATE RECURSIVE VIEW public.nums_1_100 (n) AS
    VALUES (1)
UNION ALL
    SELECT n+1 FROM nums_1_100 WHERE n < 100;
```

## Compatibility

`CREATE OR REPLACE VIEW` is a PostgreSQL language extension. The `WITH ( ... )` clause is an extension as well, as are security barrier views and security invoker views. Aurora DSQL supports these language extensions.
