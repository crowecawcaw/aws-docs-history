

# SELECT list
<a name="sql-function-select-list-spark"></a>

The SELECT list names the columns, functions, and expressions that you want the query to return. The list represents the output of the query.

## Syntax
<a name="sql-function-select-list-syntax-spark"></a>

```
SELECT
[ DISTINCT ] | {{expression}} [ AS column_alias ] [, ...]
```

## Parameters
<a name="sql-function-select-list-parameters-spark"></a>

DISTINCT  
Option that eliminates duplicate rows from the result set, based on matching values in one or more columns.

{{expression}}  
An expression formed from one or more columns that exist in the tables referenced by the query. An expression can contain SQL functions. For example:

```
coalesce(dimension, 'stringifnull') AS {{column_alias}}
```

AS column\_alias

A temporary name for the column that is used in the final result set. The AS keyword is optional. For example:

```
coalesce(dimension, 'stringifnull') AS dimensioncomplete
```

If you don't specify an alias for an expression that isn't a simple column name, the result set applies a default name to that column.

**Note**  
The alias is recognized right after it is defined in the target list. You can't use an alias in other expressions defined after it in the same target list. 