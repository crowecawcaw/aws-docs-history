# COLLECT_LIST function

The COLLECT_LIST function collects and returns a list of non-unique elements.

This type of function is useful when you want to collect multiple values from a set of rows
into a single array or list data structure.

###### Note

The function is non-deterministic because the order of the collected results depends on the
order of the rows, which may be non-deterministic after a shuffle operation is performed.

## Syntax

```
collect_list(expr)
```

## Arguments

_expr_

An expression of any type.

## Returns

Returns an ARRAY of the argument type. The order of elements in the array is
non-deterministic.

NULL values are excluded.

If DISTINCT is specified, the function collects only unique values and is a synonym for
`collect_set` aggregate function.

## Example

The following query collects all the values from the col column into a list. The
`VALUES` clause is used to create an inline table with three rows, where each row
has a single column col with the values 1, 2, and 1 respectively. The `collect_list()` function is then used to aggregate all the values from the col column into a single
array. The output of this SQL statement would be the array `[1,2,1]`, which contains
all the values from the col column in the order they appeared in the input data.

```
SELECT collect_list(col) FROM VALUES (1), (2), (1) AS tab(col);
 [1,2,1]
```
