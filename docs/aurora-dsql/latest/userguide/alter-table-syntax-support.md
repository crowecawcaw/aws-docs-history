# `ALTER TABLE`

`ALTER TABLE` changes the definition of a table.

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
    ADD table_constraint_using_index
    ALTER [ COLUMN ] column_name SET STORAGE { PLAIN | EXTERNAL | EXTENDED | MAIN | DEFAULT }
    ALTER [ COLUMN ] column_name { SET GENERATED { ALWAYS | BY DEFAULT } | SET sequence_option | RESTART [ [ WITH ] restart ] } [...]
    ALTER [ COLUMN ] column_name DROP IDENTITY [ IF EXISTS ]
    OWNER TO { new_owner | CURRENT_ROLE | CURRENT_USER | SESSION_USER }

and table_constraint_using_index is:

    [ CONSTRAINT constraint_name ]
    UNIQUE USING INDEX index_name
```

## Storage mode

**`SET STORAGE`**

This form sets the storage mode for a column. For details on the available storage
modes, see [Storage mode](create-table-syntax-support.md#create-table-storage "create-table-syntax-support.md#create-table-storage") on the [CREATE TABLE](create-table-syntax-support.md "create-table-syntax-support.md") page.

## Identity column actions

**`SET GENERATED { ALWAYS | BY DEFAULT }` / `SET `sequence_option``/`RESTART`**

These forms change whether a column is an identity column or change the generation
attribute of an existing identity column. See
[CREATE TABLE](create-table-syntax-support.md "create-table-syntax-support.md") for details. Like `SET
 DEFAULT`, these forms only affect the behavior of subsequent `INSERT`
and `UPDATE` commands; they do not cause rows already in the table to
change.

The `sequence_option` is an option supported by
[ALTER SEQUENCE](alter-sequence-syntax-support.md "alter-sequence-syntax-support.md") such as `INCREMENT BY`.
These forms alter the sequence that underlies an existing identity column.

**`DROP IDENTITY [ IF EXISTS ]`**

This form removes the identity property from a column. If `DROP IDENTITY IF
 EXISTS` is specified and the column is not an identity column, no error is thrown.
In this case a notice is issued instead.

## Add constraint actions

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
