

# `CREATE TABLE`
<a name="create-table-syntax-support"></a>

`CREATE TABLE` defines a new table.

## Supported syntax
<a name="create-table-supported-syntax"></a>

```
CREATE TABLE [ IF NOT EXISTS ] table_name ( [
  { column_name data_type [ STORAGE { PLAIN | EXTERNAL | EXTENDED | MAIN | DEFAULT } ] [ column_constraint [ ... ] ]
    | table_constraint
    | LIKE source_table [ like_option ... ] }
    [, ... ]
] )

where column_constraint is:

[ CONSTRAINT constraint_name ]
{ NOT NULL |
  NULL |
  CHECK ( expression ) |
  DEFAULT default_expr |
  GENERATED ALWAYS AS ( generation_expr ) STORED |
  GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY ( sequence_options ) |
  UNIQUE [ NULLS [ NOT ] DISTINCT ] index_parameters |
  PRIMARY KEY index_parameters |
  REFERENCES reftable [ ( refcolumn ) ] [ MATCH FULL | MATCH SIMPLE ]
    [ ON DELETE referential_action ] [ ON UPDATE referential_action ] }
[ DEFERRABLE | NOT DEFERRABLE ] [ INITIALLY DEFERRED | INITIALLY IMMEDIATE ]

and table_constraint is:

[ CONSTRAINT constraint_name ]
{ CHECK ( expression ) |
  UNIQUE [ NULLS [ NOT ] DISTINCT ] ( column_name [, ... ] ) index_parameters |
  PRIMARY KEY ( column_name [, ... ] ) index_parameters |
  FOREIGN KEY ( column_name [, ... ] ) REFERENCES reftable [ ( refcolumn [, ... ] ) ]
    [ MATCH FULL | MATCH SIMPLE ]
    [ ON DELETE referential_action ] [ ON UPDATE referential_action ] }
[ DEFERRABLE | NOT DEFERRABLE ] [ INITIALLY DEFERRED | INITIALLY IMMEDIATE ]

and referential_action in a FOREIGN KEY/REFERENCES constraint is:

{ NO ACTION | RESTRICT | CASCADE | SET NULL [ ( column_name [, ... ] ) ] | SET DEFAULT [ ( column_name [, ... ] ) ] }

and like_option is:

{ INCLUDING | EXCLUDING } { COMMENTS | CONSTRAINTS | DEFAULTS | GENERATED | IDENTITY | INDEXES | STATISTICS | ALL }

index_parameters in UNIQUE and PRIMARY KEY constraints are:
[ INCLUDE ( column_name [, ... ] ) ]
```

## Identity columns
<a name="create-table-identity-columns"></a>

**Note**  
When using identity columns, the cache value should be carefully considered. For more information, see the Important callout on the [`CREATE SEQUENCE`](create-sequence-syntax-support.md) page.  
For guidance on how best to use identity columns based on workload patterns, see [Working with sequences and identity columns](sequences-identity-columns-working-with.md).

The `GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY ( {{sequence_options}} )` clause creates the column as an *identity column*. It will have an implicit sequence attached to it and in newly-inserted rows the column will automatically have values from the sequence assigned to it. Such a column is implicitly `NOT NULL`.

The clauses `ALWAYS` and `BY DEFAULT` determine how explicitly user-specified values are handled in `INSERT` and `UPDATE` commands.

In an `INSERT` command, if `ALWAYS` is selected, a user-specified value is only accepted if the `INSERT` statement specifies `OVERRIDING SYSTEM VALUE`. If `BY DEFAULT` is selected, then the user-specified value takes precedence.

In an `UPDATE` command, if `ALWAYS` is selected, any update of the column to any value other than `DEFAULT` will be rejected. If `BY DEFAULT` is selected, the column can be updated normally. (There is no `OVERRIDING` clause for the `UPDATE` command.)

The {{sequence\_options}} clause can be used to override the parameters of the sequence. The available options include those shown for [`CREATE SEQUENCE`](create-sequence-syntax-support.md), plus `SEQUENCE NAME {{name}}`. Without `SEQUENCE NAME`, the system chooses an unused name for the sequence.

## Storage mode
<a name="create-table-storage"></a>

The optional `STORAGE` clause sets the storage mode for the column. Use these options to control the behavior of compression for variable-length data types such as `JSON`, `JSONB`, `TEXT`, `VARCHAR`, and `BPCHAR`.

Amazon Aurora DSQL compresses some data types when they exceed a certain size. To disable this behavior, use the `PLAIN` or `EXTERNAL` options.

**`PLAIN`**  
Aurora DSQL stores data inline without compression. This is the only option for fixed-length data types such as `integer`. Use this option to disable compression on some variable-length types.

**`MAIN` \| `EXTENDED` \| `DEFAULT`**  
`MAIN` and `EXTENDED` allow optional compression of the column if the underlying data type supports compression. `DEFAULT` sets the storage mode to the default mode for the column's data type.

**`EXTERNAL`**  
Aurora DSQL doesn't currently support TOAST tables, however `EXTERNAL` disables compression on data types that support compression.

## Foreign key constraints
<a name="create-table-foreign-keys"></a>

The `REFERENCES` and `FOREIGN KEY` clauses specify a foreign key constraint, which requires that a group of one or more columns of the new table must only contain values that match values in the referenced column(s) of some row of the referenced table. If you omit the {{refcolumn}} list, Aurora DSQL uses the primary key of the {{reftable}}. Otherwise, the {{refcolumn}} list must refer to the columns of a non-deferrable unique or primary key constraint.

Aurora DSQL matches a value inserted into the referencing column(s) against the values of the referenced table and referenced columns using the given match type. There are two supported match types: `MATCH FULL` and `MATCH SIMPLE` (which is the default).

You can define a foreign key as either a column constraint or a table constraint:
+ **Column constraint (REFERENCES)** – Use `REFERENCES` after the column data type for single-column foreign keys.
+ **Table constraint (FOREIGN KEY)** – Use `FOREIGN KEY (...) REFERENCES ...` for single-column or multi-column foreign keys.

### Referential actions
<a name="create-table-fk-actions"></a>

When you change data in the referenced columns, Aurora DSQL performs actions on the data in the referencing table's columns. The `ON DELETE` clause specifies the action to perform when a transaction deletes a referenced row in the referenced table. Likewise, the `ON UPDATE` clause specifies the action to perform when a transaction updates a referenced column to a new value. If a transaction updates the row but doesn't change the referenced column, Aurora DSQL takes no action.

Aurora DSQL supports the following referential actions:

**`NO ACTION` (default)**  
Produces an error if the deletion or update would create a foreign key constraint violation. If the constraint is deferred, Aurora DSQL produces this error at constraint check time if any referencing rows still exist. This is the default action.

**`RESTRICT`**  
Produces an error if a row to be deleted or updated matches a row in the referencing table. This prevents the action even if the state after the action wouldn't violate the foreign key constraint. In particular, it prevents updates of referenced rows to values that are distinct but compare as equal. Unlike `NO ACTION`, the `RESTRICT` check can't be deferred.

**Cascading actions count towards transaction modification limits**  
The `CASCADE`, `SET NULL`, and `SET DEFAULT` actions automatically modify rows in the referencing table when a referenced row is updated or deleted. The Aurora DSQL transaction row limit applies to these actions and can cause unexpected failures if not used carefully. Prefer `NO ACTION` or `RESTRICT` for foreign key relationships where child-row cardinality is unbounded or unpredictable. For more information, see [Database limits in Aurora DSQL](CHAP_quotas.md#SECTION_database-limits).

**`CASCADE`**  
Delete any rows referencing the deleted row, or update the values of the referencing column(s) to the new values of the referenced columns, respectively.

**`SET NULL [ ( column_name [, ... ] ) ]`**  
Set all of the referencing columns, or a specified subset of the referencing columns, to null. A subset of columns can only be specified for `ON DELETE` actions.

**`SET DEFAULT [ ( column_name [, ... ] ) ]`**  
Set all of the referencing columns, or a specified subset of the referencing columns, to their default values. A subset of columns can only be specified for `ON DELETE` actions. (There must be a row in the referenced table matching the default values, if they are not null, or the operation will fail.)

### Match types
<a name="create-table-fk-match-types"></a>

Aurora DSQL supports the following match types:

**`MATCH SIMPLE` (default)**  
Allows any of the foreign key columns to be null. If any of them are null, the row isn't required to have a match in the referenced table.

**`MATCH FULL`**  
Doesn't allow one column of a multi-column foreign key to be null unless all foreign key columns are null. If they are all null, the row isn't required to have a match in the referenced table.

You can apply `NOT NULL` constraints to the referencing columns to prevent these cases from arising.

### Deferrability
<a name="create-table-fk-deferrability"></a>

You can control when a foreign key constraint is checked by specifying its deferrability:

**`NOT DEFERRABLE` (default)**  
Aurora DSQL checks this constraint immediately after each statement. You can't change it to deferred with `SET CONSTRAINTS`.

**`DEFERRABLE`**  
The constraint can be deferred to the end of the transaction using `SET CONSTRAINTS`. Without an `INITIALLY` clause, this defaults to `INITIALLY IMMEDIATE`.

**`DEFERRABLE INITIALLY IMMEDIATE`**  
By default, Aurora DSQL checks this constraint after each statement, but you can defer it within a transaction by using `SET CONSTRAINTS ... DEFERRED`.

**`DEFERRABLE INITIALLY DEFERRED`**  
By default, Aurora DSQL checks this constraint at transaction commit time. You can change it to immediate within a transaction by using `SET CONSTRAINTS ... IMMEDIATE`.

For more information about changing constraint check timing within a transaction, see [`SET CONSTRAINTS`](set-constraints-syntax-support.md).

**Foreign key constraints only**  
In Aurora DSQL, the `DEFERRABLE` option applies to foreign key constraints only.

### Foreign key constraint examples
<a name="create-table-fk-constraint-examples"></a>

Assume you have a table storing products:

```
CREATE TABLE products (
    product_no integer PRIMARY KEY,
    name text,
    price numeric
);
```

Now you want a table storing orders of those products. You want to ensure that the orders table contains references to products that actually exist. Define a foreign key constraint in the orders table that references the products table:

```
CREATE TABLE orders (
    order_id integer PRIMARY KEY,
    product_no integer REFERENCES products (product_no),
    quantity integer
);
```

Now you can't create orders with non-NULL `product_no` entries that don't appear in the products table.

In this situation, the orders table is the *referencing* table and the products table is the *referenced* table. Similarly, there are referencing and referenced columns.

You can shorten the above command to:

```
CREATE TABLE orders (
    order_id integer PRIMARY KEY,
    product_no integer REFERENCES products,
    quantity integer
);
```

If you omit the column list, Aurora DSQL uses the primary key of the referenced table as the referenced column(s).

You can assign your own name for a foreign key constraint in the usual way:

```
CREATE TABLE orders (
    order_id integer PRIMARY KEY,
    product_no integer CONSTRAINT fk_product REFERENCES products,
    quantity integer
);
```

A foreign key can also constrain and reference a group of columns. It then needs to be written in table constraint form:

```
CREATE TABLE inventory (
    warehouse_id integer,
    product_no integer,
    quantity integer,
    PRIMARY KEY (warehouse_id, product_no)
);

CREATE TABLE shipments (
    shipment_id integer PRIMARY KEY,
    warehouse_id integer,
    product_no integer,
    FOREIGN KEY (warehouse_id, product_no) REFERENCES inventory (warehouse_id, product_no)
);
```

The number and types of the constrained columns need to be compatible with the number and types of the referenced columns.

A table can have more than one foreign key constraint. This is used to implement many-to-many relationships between tables:

```
CREATE TABLE order_items (
    product_no integer REFERENCES products,
    order_id integer REFERENCES orders,
    quantity integer,
    PRIMARY KEY (product_no, order_id)
);
```

A foreign key constraint can reference the same table it belongs to. This is called a *self-referential* foreign key. For example, if you want rows of a table to represent nodes of a tree structure, you could write:

```
CREATE TABLE tree (
    node_id integer PRIMARY KEY,
    parent_id integer REFERENCES tree,
    name text
);
```

A top-level node would have NULL `parent_id`, while non-NULL `parent_id` entries are constrained to reference valid rows of the table.

You can specify referential actions to control what happens when a referenced row is deleted or updated. The following example uses `ON DELETE RESTRICT` to prevent deletion of a product that is still referenced by an order:

```
CREATE TABLE orders (
    order_id integer PRIMARY KEY,
    product_no integer REFERENCES products ON DELETE RESTRICT,
    quantity integer
);
```

With `RESTRICT`, attempting to delete a product that has orders referencing it produces an error immediately. With the default `NO ACTION`, the check can be deferred to the end of the transaction if the constraint is declared `DEFERRABLE`.

To create a foreign key that can be deferred to the end of a transaction, use the `DEFERRABLE` option. This is useful when you need to insert rows in both tables within the same transaction regardless of order:

```
CREATE TABLE orders (
    order_id integer PRIMARY KEY,
    product_no integer REFERENCES products DEFERRABLE INITIALLY DEFERRED,
    quantity integer
);
```

With `DEFERRABLE INITIALLY DEFERRED`, the constraint isn't checked until commit time. You can insert the order row before the product row exists, as long as the product row is present when the transaction commits.

To use `MATCH FULL` with a composite foreign key, which requires that all referencing columns are null together or all non-null together:

```
CREATE TABLE shipments (
    shipment_id integer PRIMARY KEY,
    warehouse_id integer,
    product_no integer,
    FOREIGN KEY (warehouse_id, product_no)
        REFERENCES inventory (warehouse_id, product_no) MATCH FULL
);
```