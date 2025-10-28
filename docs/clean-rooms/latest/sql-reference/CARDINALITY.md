# CARDINALITY function

The CARDINALITY function returns the size of an ARRAY or MAP expression (_expr_).

This function is useful to find the size or length of an array.

## Syntax

```
cardinality(expr)
```

## Arguments

_expr_

An ARRAY or MAP expression.

## Returns

Returns the size of an array or a map (INTEGER).

The function returns `NULL` for null input if `sizeOfNull` is set to
`false` or `enabled` is set to `true`.

Otherwise, the function returns `-1` for null input. With the default settings,
the function returns `-1` for null input.

## Example

The following query calculates the cardinality, or the number of elements, in the given
array. The array (`'b', 'd', 'c', 'a'`) has 4 elements, so the output of this query
would be `4`.

```
SELECT cardinality(array('b', 'd', 'c', 'a'));
 4
```
