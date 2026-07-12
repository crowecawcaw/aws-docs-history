# `ALTER TABLE`

`ALTER TABLE` changes the definition of a table.

## Supported syntax

```
ALTER TABLE [ IF EXISTS ] [ ONLY ] name [ * ]
    action [, ... ]
ALTER TABLE [ IF EXISTS ] [ ONLY ] name [ * ]
    RENAME [ COLUMN ] column_name TO new_column_name
ALTER TABLE [ IF EXISTS ] [ ONLY ] name [ * ]
    RENAME CONSTRAINT constraint_name TO new_constraint_name
ALTER TABLE [ IF EXISTS ] name
    RENAME TO new_name
ALTER TABLE [ IF EXISTS ] name
    SET SCHEMA new_schema

where action is one of:

    ADD [ COLUMN ] [ IF NOT EXISTS ] column_name data_type [ STORAGE { PLAIN | EXTERNAL | EXTENDED | MAIN | DEFAULT } ]
    ALTER [ COLUMN ] column_name SET DEFAULT expression
    ALTER [ COLUMN ] column_name DROP DEFAULT
    ALTER [ COLUMN ] column_name DROP NOT NULL
    ALTER [ COLUMN ] column_name DROP EXPRESSION [ IF EXISTS ]
    ALTER [ COLUMN ] column_name ADD GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY [ ( sequence_options ) ]
    ALTER [ COLUMN ] column_name { SET GENERATED { ALWAYS | BY DEFAULT } | SET sequence_option | RESTART [ [ WITH ] restart ] } [...]
    ALTER [ COLUMN ] column_name DROP IDENTITY [ IF EXISTS ]
    ALTER [ COLUMN ] column_name SET STORAGE { PLAIN | EXTERNAL | EXTENDED | MAIN | DEFAULT }
    ADD table_constraint_using_index
    DROP CONSTRAINT [ IF EXISTS ] constraint_name [ RESTRICT | CASCADE ]
    OWNER TO { new_owner | CURRENT_ROLE | CURRENT_USER | SESSION_USER }

and table_constraint_using_index is:

    [ CONSTRAINT constraint_name ]
    UNIQUE USING INDEX index_name
```

## Description

**`ADD [ COLUMN ] [ IF NOT EXISTS ]`**

This form adds a new column to the table, using the same syntax as
[CREATE TABLE](create-table-syntax-support.md "create-table-syntax-support.md"). If `IF NOT EXISTS` is
specified and a column already exists with this name, no error is thrown.

**`SET`/`DROP DEFAULT`**

These forms set or remove the default value for a column (where removal is
equivalent to setting the default value to NULL). The new default value will only
apply in subsequent `INSERT` or `UPDATE` commands; it does not
cause rows already in the table to change.

**`DROP NOT NULL`**

This form changes a column to allow null values.

**`DROP EXPRESSION [ IF EXISTS ]`**

This form turns a stored generated column into a normal base column. Existing data
in the columns is retained, but future changes will no longer apply the generation
expression. If `DROP EXPRESSION IF EXISTS` is specified and the column is
not a generated column, no error is thrown. In this case a notice is issued
instead.

**`ADD GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY`**
**`SET GENERATED { ALWAYS | BY DEFAULT }`**
**`DROP IDENTITY [ IF EXISTS ]`**

These forms change whether a column is an identity column or change the generation
attribute of an existing identity column. See
[CREATE TABLE](create-table-syntax-support.md "create-table-syntax-support.md") for details. Like `SET
 DEFAULT`, these forms only affect the behavior of subsequent `INSERT`
and `UPDATE` commands; they do not cause rows already in the table to
change.

The `sequence_option` is an option supported by
[ALTER SEQUENCE](alter-sequence-syntax-support.md "alter-sequence-syntax-support.md") such as `INCREMENT BY`.
These forms alter the sequence that underlies an existing identity column.

###### Note

Amazon Aurora DSQL requires an explicit `CACHE` value when using
`ADD GENERATED AS IDENTITY`. Additionally, identity columns are only
supported on `bigint` columns.

When using identity columns, the cache value should be
carefully considered. For more information, see the Important callout on the [CREATE SEQUENCE](create-sequence-syntax-support.md "create-sequence-syntax-support.md") page.

For guidance on how best to use identity columns based on workload patterns,
see [Working with sequences and identity columns](sequences-identity-columns-working-with.md "sequences-identity-columns-working-with.md").

**`SET STORAGE { PLAIN | EXTERNAL | EXTENDED | MAIN | DEFAULT }`**

This form sets the storage mode for a column. For details on the available storage
modes, see [Storage mode](create-table-syntax-support.md#create-table-storage "create-table-syntax-support.md#create-table-storage") on the [CREATE TABLE](create-table-syntax-support.md "create-table-syntax-support.md") page.

**`ADD `table_constraint_using_index``**

This form adds a new `UNIQUE` constraint to a table based on an existing
unique index. All the columns of the index will be included in the constraint.

The index must be in a `VALID` state; adding a unique constraint using
an index while the index is currently building is not supported.

If a constraint name is provided then the index will be renamed to match the
constraint name. Otherwise the constraint will be named the same as the index.

After this command is executed, the index is "owned" by the constraint, in the same
way as if the index had been built by a regular `CREATE UNIQUE INDEX ASYNC`
command. In particular, dropping the constraint will make the index disappear too.

**`DROP CONSTRAINT [ IF EXISTS ]`**

This form drops the specified constraint on a table, along with any index
underlying the constraint. If `IF EXISTS` is specified and the constraint
does not exist, no error is thrown. In this case a notice is issued instead.

###### Important

Currently, adding a new constraint is supported with the `CREATE TABLE`
expression. `ALTER TABLE ADD CONSTRAINT` (mirroring support for
`DROP CONSTRAINT`) is not yet available. If you have questions about this
upcoming feature, please contact AWS Support or reach out directly via the
[DSQL Public Discord](https://discord.com/invite/nEF6ksFWru "https://discord.com/invite/nEF6ksFWru").

**`OWNER TO`**

This form changes the owner of the table to the specified user.

**`RENAME`**

The `RENAME` forms change the name of a table, the name of an
individual column in a table, or the name of a constraint of the table. When
renaming a constraint that has an underlying index, the index is renamed as well.
There is no effect on the stored data.

**`SET SCHEMA`**

This form moves the table into another schema. Associated indexes, constraints,
and sequences owned by table columns are moved as well.

## Parameters

**`IF EXISTS`**

Do not throw an error if the table does not exist. A notice is issued in
this case.

**`name`**

The name (optionally schema-qualified) of an existing table to alter. If
`ONLY` is specified before the table name, only that table is altered.
If `ONLY` is not specified, the table and all its descendant tables
(if any) are altered. Optionally, `*` can be specified after the table
name to explicitly indicate that descendant tables are included.

**`column_name`**

Name of a new or existing column.

**`new_column_name`**

New name for an existing column.

**`new_name`**

New name for the table.

**`data_type`**

Data type of the new column.

**`constraint_name`**

Name of a new or existing constraint.

**`CASCADE`**

Automatically drop objects that depend on the dropped constraint (for example,
views referencing the column), and in turn all objects that depend on those
objects.

**`RESTRICT`**

Refuse to drop the constraint if there are any dependent objects. This is the
default behavior.

**`new_owner`**

The user name of the new owner of the table.

**`new_schema`**

The name of the schema to which the table will be moved.
