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

    ADD [ COLUMN ] [ IF NOT EXISTS ] column_name data_type
    ALTER [ COLUMN ] column_name { SET GENERATED { ALWAYS | BY DEFAULT } | SET sequence_option | RESTART [ [ WITH ] restart ] } [...]
    ALTER [ COLUMN ] column_name DROP IDENTITY [ IF EXISTS ]
    OWNER TO { new_owner | CURRENT_ROLE | CURRENT_USER | SESSION_USER }
```

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
