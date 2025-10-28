# ARRAY_CONTAINS function

The ARRAY_CONTAINS function can be used to perform basic membership checks on array data
structures. The ARRAY_CONTAINS function is useful when you need to check if a specific
value is present within an array.

## Syntax

```
array_contains(array, value)
```

## Arguments

_array_

An ARRAY to be searched.

_value_

An expression with a type sharing a least common type with the array
elements.

## Return type

The ARRAY_CONTAINS function returns a BOOLEAN.

If value is NULL, the result is NULL.

If any element in array is NULL, the result is NULL if value is not matched to any
other element.

## Examples

The following example checks if the array `[1, 2, 3]` contains the value
`4`. Since the array `[1, 2, 3`] doesn't contain the value
`4`, the array_contains function returns `false`.

```
SELECT array_contains(array(1, 2, 3), 4)
false
```

The following example checks if the array `[1, 2, 3]` contains the value
`2`. Since the array `[1, 2, 3]` does contain the value
`2`, the array_contains function returns `true`.

```
SELECT array_contains(array(1, 2, 3), 2);
 true
```
