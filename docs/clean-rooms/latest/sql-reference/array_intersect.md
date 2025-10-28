# ARRAY_INTERSECT function

The ARRAY_INTERSECT function takes two arrays as arguments and returns a new array that
contains the elements that are present in both input arrays. This function is useful when
you need to find the common elements between two arrays. This can be helpful in scenarios
where you need to perform set-like operations on arrays, such as finding the intersection
between two sets of data.

## Syntax

```
array_intersect(array1, array2)
```

## Arguments

_array1_

An ARRAY of any type with comparable elements.

_array2_

An ARRAY of elements sharing a least common type with the elements of
array1.

## Return type

The ARRAY_INTERSECT function returns an ARRAY of matching type to array1 with no
duplicates and elements contained in both array1 and array2.

## Examples

In this example, the first array `[1, 2, 3]` contains the elements 1, 2,
and 3. The second array `[1, 3, 5]` contains the elements 1, 3, and 5. The
ARRAY_INTERSECT function identifies the common elements between the two arrays, which
are 1 and 3. The resulting output array is `[1, 3]`.

```
SELECT array_intersect(array(1, 2, 3), array(1, 3, 5));
 [1,3]
```
