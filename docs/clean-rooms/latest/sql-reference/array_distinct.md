# ARRAY_DISTINCT function

The ARRAY_DISTINCT function can be used to remove duplicate values from an array. The
ARRAY_DISTINCT function is useful when you need to remove duplicates from an array and work
with only the unique elements. This can be helpful in scenarios where you want to perform
operations or analyses on a dataset without the interference of repeated values.

## Syntax

```
array_distinct(array)
```

## Arguments

_array_

An ARRAY expression.

## Return type

The ARRAY_DISTINCT function returns an ARRAY that contains only the unique elements
from the input array.

## Examples

In this example, the input array `[1, 2, 3, null, 3]` contains a duplicate
value of `3`. The `array_distinct` function removes this duplicate
value `3` and returns a new array with the unique elements: `[1, 2, 3,
 null]`.

```
SELECT array_distinct(array(1, 2, 3, null, 3));
 [1,2,3,null]
```

In this example, the input array `[1, 2, 2, 3, 3, 3]` contains duplicate
values of `2` and `3`. The `array_distinct` function
removes these duplicates and returns a new array with the unique elements: `[1, 2,
 3]`.

```
SELECT array_distinct(array(1, 2, 2, 3, 3, 3))
  [1,2,3]
```
