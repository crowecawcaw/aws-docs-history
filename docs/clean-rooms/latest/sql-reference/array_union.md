# ARRAY_UNION function

The ARRAY_UNION function takes two arrays as arguments and returns a new array that
contains the unique elements from both input arrays. This function is useful when you need
to combine two arrays and eliminate any duplicate elements. This can be helpful in
scenarios where you need to perform set-like operations on arrays, such as finding the
union between two sets of data.

## Syntax

```
array_union(array1, array2)
```

## Arguments

_array1_

An ARRAY.

_array2_

An ARRAY of the same type as _array1_.

## Return type

The ARRAY_UNION function returns an ARRAY of the same type as array.

## Example

In this example, the first array `[1, 2, 3]` contains the elements 1, 2,
and 3. The second array `[1, 3, 5]` contains the elements 1, 3, and 5. The
ARRAY_UNION function combines the unique elements from both arrays, resulting in the
output array `[1, 2, 3, 5]`. T

```
SELECT array_union(array(1, 2, 3), array(1, 3, 5));
 [1,2,3,5]
```
