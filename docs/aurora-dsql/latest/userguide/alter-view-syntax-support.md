# `ALTER VIEW`

The `ALTER VIEW` statement allows changing various properties of an existing view, and Aurora DSQL supports all the PostgreSQL syntax for this command.

## Supported syntax

```
ALTER VIEW [ IF EXISTS ] name ALTER [ COLUMN ] column_name SET DEFAULT expression
ALTER VIEW [ IF EXISTS ] name ALTER [ COLUMN ] column_name DROP DEFAULT
ALTER VIEW [ IF EXISTS ] name OWNER TO { new_owner | CURRENT_ROLE | CURRENT_USER | SESSION_USER }
ALTER VIEW [ IF EXISTS ] name RENAME [ COLUMN ] column_name TO new_column_name
ALTER VIEW [ IF EXISTS ] name RENAME TO new_name
ALTER VIEW [ IF EXISTS ] name SET SCHEMA new_schema
ALTER VIEW [ IF EXISTS ] name SET ( view_option_name [= view_option_value] [, ... ] )
ALTER VIEW [ IF EXISTS ] name RESET ( view_option_name [, ... ] )
```

## Description

`ALTER VIEW` changes various auxiliary properties of a view. (If you want
to modify the view's defining query, use `CREATE OR REPLACE VIEW`.) You must
own the view to use `ALTER VIEW`. To change a view's schema, you must also
have `CREATE` privilege on the new schema. To alter the owner, you must be
able to `SET ROLE` to the new owning role, and that role must have
`CREATE` privilege on the view's schema.

## Parameters

**`name`**

The name (optionally schema-qualified) of an existing view.

**`column_name`**

Name of an existing column, or new name for an existing column.

**`IF EXISTS`**

Don't throw an error if the view doesn't exist. A notice is issued in this case.

**`SET/DROP DEFAULT`**

These forms set or remove the default value for a column. The default value for a view column is substituted into any `INSERT` or `UPDATE` command where the target is the view.

**`new_owner`**

The user name of the new owner of the view.

**`new_name`**

The new name for the view.

**`new_schema`**

The new schema for the view.

**`SET ( view_option_name [= view_option_value] [, ... ] )`**

Sets a view option. The following are supported options:

- `check_option (enum)` - Changes the check option of the view. The value must be `local` or `cascaded`.
- `security_barrier (boolean)` - Changes the security-barrier property of the view.
- `security_invoker (boolean)` - Changes the security-invoker property of the view.

**`RESET ( view_option_name [, ... ] )`**

Resets a view option to its default value.

## Examples

Renaming the view `foo` to `bar`:

```
ALTER VIEW foo RENAME TO bar;
```

Attaching a default column value to an updatable view:

```
CREATE TABLE base_table (id int, ts timestamptz);
CREATE VIEW a_view AS SELECT * FROM base_table;
ALTER VIEW a_view ALTER COLUMN ts SET DEFAULT now();
INSERT INTO base_table(id) VALUES(1);  -- ts will receive a NULL
INSERT INTO a_view(id) VALUES(2);  -- ts will receive the current time
```

## Compatibility

`ALTER VIEW` is a PostgreSQL extension of the SQL standard that Aurora DSQL supports.
