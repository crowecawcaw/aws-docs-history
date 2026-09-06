

# `CREATE INDEX`
<a name="create-index-syntax-support"></a>

`CREATE INDEX` defines a new index. In Aurora DSQL, index creation is always asynchronous, so you must specify the `ASYNC` keyword. For information about how Aurora DSQL runs asynchronous index builds and how to monitor them, see [Asynchronous indexes in Aurora DSQL](working-with-create-index-async.md).

## Supported syntax
<a name="create-index-supported-syntax"></a>

```
CREATE [ UNIQUE ] INDEX ASYNC [ [ IF NOT EXISTS ] name ] ON table_name
    ( { column_name | ( expression ) } [ NULLS { FIRST | LAST } ] [, ...] )
    [ INCLUDE ( column_name [, ...] ) ]
    [ NULLS [ NOT ] DISTINCT ]
```

## Description
<a name="create-index-description"></a>

`CREATE INDEX` constructs an index on the specified columns of the specified table. Indexes are primarily used to enhance database performance, though inappropriate use can result in slower performance.

You specify the key fields for the index as column names, or alternatively as expressions written in parentheses. You can specify multiple fields to create a multicolumn index.

An index field can be an expression computed from the values of one or more columns of the table row. Use this feature to obtain fast access to data based on some transformation of the basic data. For example, an index computed on `upper(col)` allows the clause `WHERE upper(col) = 'JIM'` to use an index.

All functions and operators used in an index definition must be immutable. That is, their results must depend only on their arguments and never on any outside influence, such as the contents of another table or the current time. This restriction ensures that the behavior of the index is well-defined. To use a user-defined function in an index expression, remember to mark the function `IMMUTABLE` when you create it.

## Parameters
<a name="create-index-parameters"></a>

**`UNIQUE`**  
Causes the system to check for duplicate values in the table when it creates the index, if data already exists, and each time you add data. Attempts to insert or update data that would result in duplicate entries generate an error.

**`IF NOT EXISTS`**  
Do not throw an error if a relation with the same name already exists. A notice is issued in this case. Note that there is no guarantee that the existing index resembles the one that would have been created. The index name is required when `IF NOT EXISTS` is specified.

**`INCLUDE`**  
The optional `INCLUDE` clause specifies a list of columns to include in the index as *non-key* columns. You can't use a non-key column in an index scan search qualification, and Aurora DSQL disregards it for purposes of any uniqueness or exclusion constraint that the index enforces. However, an index-only scan can return the contents of non-key columns without having to visit the index's table, because they are available directly from the index entry. Adding non-key columns therefore allows index-only scans for queries that otherwise couldn't use them.  
Expressions aren't supported as included columns, because they can't be used in index-only scans.

**{{name}}**  
The name of the index to create. You can't include a schema name here. Aurora DSQL always creates the index in the same schema as its parent table. The name of the index must be distinct from the name of any other relation, such as a table, sequence, index, or view, in that schema. If you omit the name, Aurora DSQL chooses a suitable name based on the parent table's name and the indexed column names.

**{{table\_name}}**  
The name, optionally schema-qualified, of the table to index.

**{{column\_name}}**  
The name of a column of the table.

**{{expression}}**  
An expression based on one or more columns of the table. You usually must write the expression with surrounding parentheses, as shown in the syntax. However, you can omit the parentheses if the expression has the form of a function call.

**`NULLS FIRST`**  
Specifies that nulls sort before non-nulls.

**`NULLS LAST`**  
Specifies that nulls sort after non-nulls.

**`NULLS DISTINCT``NULLS NOT DISTINCT`**  
Specifies whether null values are considered distinct, that is, not equal, for a unique index. The default is that they are distinct, so that a unique index can contain multiple null values in a column.

## Examples
<a name="create-index-examples"></a>

To create a unique index on the column `title` in the table `films`.

```
CREATE UNIQUE INDEX ASYNC title_idx ON films (title);
```

To create a unique index on the column `title` with included columns `director` and `rating` in the table `films`.

```
CREATE UNIQUE INDEX ASYNC title_idx ON films (title) INCLUDE (director, rating);
```

To create an index on the expression `lower(title)`, which allows efficient case-insensitive searches.

```
CREATE INDEX ASYNC ON films ((lower(title)));
```

This example omits the index name, so Aurora DSQL chooses a name, typically `films_lower_idx`.

To create an index with non-default sort ordering of nulls.

```
CREATE INDEX ASYNC title_idx_nulls_low ON films (title NULLS FIRST);
```