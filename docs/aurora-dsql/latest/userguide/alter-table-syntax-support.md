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
ALTER TABLE ASYNC [ IF EXISTS ] [ ONLY ] name [ * ]
    VALIDATE CONSTRAINT constraint_name

where action is one of:

    ADD [ COLUMN ] [ IF NOT EXISTS ] column_name data_type [ STORAGE { PLAIN | EXTERNAL | EXTENDED | MAIN | DEFAULT } ]
    DROP [ COLUMN ] [ IF EXISTS ] column_name [ RESTRICT | CASCADE ]
    ALTER [ COLUMN ] column_name SET DEFAULT expression
    ALTER [ COLUMN ] column_name DROP DEFAULT
    ALTER [ COLUMN ] column_name DROP NOT NULL
    ALTER [ COLUMN ] column_name DROP EXPRESSION [ IF EXISTS ]
    ALTER [ COLUMN ] column_name ADD GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY [ ( sequence_options ) ]
    ALTER [ COLUMN ] column_name { SET GENERATED { ALWAYS | BY DEFAULT } | SET sequence_option | RESTART [ [ WITH ] restart ] } [...]
    ALTER [ COLUMN ] column_name DROP IDENTITY [ IF EXISTS ]
    ALTER [ COLUMN ] column_name SET STORAGE { PLAIN | EXTERNAL | EXTENDED | MAIN | DEFAULT }
    ALTER CONSTRAINT constraint_name [ DEFERRABLE | NOT DEFERRABLE ] [ INITIALLY DEFERRED | INITIALLY IMMEDIATE ]
    ADD table_constraint NOT VALID
    ADD table_constraint_using_index
    DROP CONSTRAINT [ IF EXISTS ] constraint_name [ RESTRICT | CASCADE ]
    OWNER TO { new_owner | CURRENT_ROLE | CURRENT_USER | SESSION_USER }

and table_constraint is:

    [ CONSTRAINT constraint_name ]
    { CHECK ( expression ) |
      FOREIGN KEY ( column_name [, ... ] ) REFERENCES reftable [ ( refcolumn [, ... ] ) ]
        [ MATCH FULL | MATCH SIMPLE ]
        [ ON DELETE referential_action ] [ ON UPDATE referential_action ] }
    [ DEFERRABLE | NOT DEFERRABLE ] [ INITIALLY DEFERRED | INITIALLY IMMEDIATE ]

and table_constraint_using_index is:

    [ CONSTRAINT constraint_name ]
    UNIQUE USING INDEX index_name

and referential_action in a FOREIGN KEY/REFERENCES constraint is:

    { NO ACTION | RESTRICT | CASCADE | SET NULL [ ( column_name [, ... ] ) ] | SET DEFAULT [ ( column_name [, ... ] ) ] }
```

## Description

**`ADD [ COLUMN ] [ IF NOT EXISTS ]`**

This form adds a new column to the table, using the same syntax as
[CREATE TABLE](create-table-syntax-support.md "create-table-syntax-support.md"). If `IF NOT EXISTS` is
specified and a column already exists with this name, no error is thrown.

**`DROP [ COLUMN ] [ IF EXISTS ]`**

This form drops a column from a table. Indexes and table constraints involving the
column will be automatically dropped except for primary key constraints. Dropping of
primary key columns is not supported. Multivariate statistics referencing the dropped
column will also be removed if the removal of the column would cause the statistics to
contain data for only a single column. You will need to say `CASCADE` if
anything outside the table depends on the column, for example, foreign key references or
views. If `IF EXISTS` is specified and the column does not exist, no error is
thrown. In this case a notice is issued instead.

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

**`ALTER CONSTRAINT`**

This form alters the attributes of an existing foreign key constraint. You
can change a foreign key constraint between `DEFERRABLE` and `NOT
 DEFERRABLE`, and set whether it defaults to `INITIALLY DEFERRED`
or `INITIALLY IMMEDIATE`. For a description of these options, see
[Deferrability](create-table-syntax-support.md#create-table-fk-deferrability "create-table-syntax-support.md#create-table-fk-deferrability") on the
[CREATE TABLE](create-table-syntax-support.md "create-table-syntax-support.md") page.

**`ADD `table_constraint` NOT VALID`**

This form adds a new `CHECK` or `FOREIGN KEY` constraint to a
table. In Aurora DSQL, `CHECK` and `FOREIGN KEY` constraints added via
`ALTER TABLE ADD CONSTRAINT` must use the `NOT VALID` option.
Aurora DSQL creates the
constraint but doesn't immediately validate it against existing data. This allows the
constraint to be added without scanning the entire table. The constraint applies
immediately to all new rows and updates.

After adding a constraint with `NOT VALID`, use `ALTER TABLE ASYNC ...
 VALIDATE CONSTRAINT` to validate that existing data also satisfies the constraint.
The validation runs as an asynchronous DDL job. You can monitor its progress using `sys.jobs`.

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

**`VALIDATE CONSTRAINT`**

This form validates a constraint that was previously created with the `NOT
 VALID` option. This command is an asynchronous DDL operation that doesn't block
other transactions. When you run `ALTER TABLE ASYNC ... VALIDATE CONSTRAINT`,
Aurora DSQL immediately returns a `job_id`.

You can monitor the status of this asynchronous job using the `sys.jobs`
system view. You can also use `sys.wait_for_job(`'job_id'`)`
to block the current session until the validation completes or fails.

The validation job scans the entire table to verify that all existing rows satisfy
the constraint. Once validation completes successfully, Aurora DSQL marks the constraint as valid
and the query planner enforces it for all queries. If validation fails because
existing rows violate the constraint, the job fails and the constraint remains in the
`NOT VALID` state.

This command validates only constraints that you created with the `NOT
 VALID` option. Attempting to validate an already-valid constraint results in an
error.

**`DROP CONSTRAINT [ IF EXISTS ]`**

This form drops the specified constraint on a table, along with any index
underlying the constraint. If `IF EXISTS` is specified and the constraint
does not exist, no error is thrown. In this case a notice is issued instead.

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

**`table_constraint`**

A `CHECK` or `FOREIGN KEY` constraint definition. In Aurora DSQL, these
constraints must be added with the `NOT VALID` option using `ALTER TABLE
 ADD CONSTRAINT`. See [CREATE TABLE](create-table-syntax-support.md "create-table-syntax-support.md") for the full constraint syntax.

**`constraint_name`**

Name of a new or existing constraint.

**`CASCADE`**

Automatically drop objects that depend on the dropped column or constraint (for
example, views referencing the column), and in turn all objects that depend on those
objects.

**`RESTRICT`**

Refuse to drop the column or constraint if there are any dependent objects. This is
the default behavior.

**`new_owner`**

The user name of the new owner of the table.

**`new_schema`**

The name of the schema to which the table will be moved.

## Notes

The `DROP COLUMN` form does not physically remove the column, but simply makes
it invisible to SQL operations. Subsequent insert and update operations in the table will store
a null value for the column. Thus, dropping a column is quick but it will not immediately
reduce the on-disk size of your table, as the space occupied by the dropped column is not
reclaimed. The space will be reclaimed over time as existing rows are updated.

If a dropped column is referenced as an `INCLUDE` column in the primary key, the
primary key definition will be updated to remove the dropped column.

A table in Aurora DSQL can have at most 255 active columns at one time and a maximum of 1600
columns over the lifetime of the table. Dropping a column does not reclaim its attribute
number. It removes it from the set of active columns but the dropped column continues to count
against the lifetime limit of 1600 columns. For more information, see [Database limits in Aurora DSQL](CHAP_quotas.md#SECTION_database-limits "CHAP_quotas.md#SECTION_database-limits").
