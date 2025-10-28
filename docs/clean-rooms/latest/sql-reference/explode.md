# EXPLODE function

The EXPLODE function is used to transform a single row with an array or map column into
multiple rows, where each row corresponds to a single element from the array or map.

## Syntax

```
explode(expr)
```

## Arguments

_expr_

An array expression or a map expression.

## Return type

The EXPLODE function returns a set of rows, where each row represents a single
element from the input array or map.

The data type of the output rows depends on the data type of the elements in the
input array or map.

## Examples

The following example takes the single-row array [10, 20] and transforms it into two
separate rows, each containing one of the array elements (10 and 20).

```
SELECT explode(array(10, 20));

```

In the first example, the input array was directly passed as an argument to
`explode()`. In this example, the input array is specified using the
`=>` syntax, where the column name (`collection`) is explicitly
provided.

```
SELECT explode(array(10, 20));

```

Both approaches are valid and achieve the same result, but the second syntax can be
more useful when you need to explode a column from a larger dataset, rather than just a
simple array literal.
