# COLLECT_SET function

The COLLECT_SET function collects and returns a set of unique elements.

This function is useful when you want to collect all the distinct values from a set of rows
into a single data structure, without including any duplicates.

###### Note

The function is non-deterministic because the order of the collected results depends on the
order of the rows, which may be non-deterministic after a shuffle operation is performed.

## Syntax

```
collect_set(expr)
```

## Arguments

_expr_

An expression of any type except MAP.

## Returns

Returns an ARRAY of the argument type. The order of elements in the array is
non-deterministic.

NULL values are excluded.

## Example

The following query collects all the unique values from the col column into a set. The
`VALUES` clause is used to create an inline table with three rows, where each row
has a single column col with the values 1, 2, and 1 respectively. The `collect_set()`
function is then used to aggregate all the unique values from the col column into a single set.
The output of this SQL statement would be the set `[1,2]`, which contains the unique
values from the col column. The duplicate value of 1 is only included once in the result.

```
SELECT collect_set(col) FROM VALUES (1), (2), (1) AS tab(col);
 [1,2]
```
