# ARRAY_REMOVE function

The ARRAY_REMOVE function takes two arguments: The first argument is the input array
from which the elements will be removed. The second argument is the value that will be
removed from the array. This function is useful when you need to remove specific elements
from an array. This can be helpful in scenarios where you need to perform data cleaning or
preprocessing on an array of values.

## Syntax

```
array_remove(array, element)
```

## Arguments

_array_

An ARRAY.

_element_

An expression of a type sharing a least common type with the elements of
array.

## Return type

The ARRAY_REMOVE function returns the result type matched the type of the array. If
the element to be removed is `NULL`, the result is `NULL`.

## Examples

In this example, the ARRAY_REMOVE function takes the array `[1, 2, 3, null,
 3]` and removes all occurrences of the value 3. The resulting output is the
array `[1, 2, null]`.

```
SELECT array_remove(array(1, 2, 3, null, 3), 3);
 [1,2,null]
```
