# ARRAY_EXCEPT function

The ARRAY_EXCEPT function takes two arrays as arguments and returns a new array that
contains only the elements that are present in the first array but not the second
array.

The ARRAY_EXCEPT is useful when you need to find the elements that are unique to one
array compared to another. This can be helpful in scenarios where you need to perform
set-like operations on arrays, such as finding the difference between two sets of
data.

## Syntax

```
array_except(array1, array2)
```

## Arguments

_array1_

An ARRAY of any type with comparable elements.

_array2_

An ARRAY of elements sharing a least common type with the elements of
_array1_.

## Return type

The ARRAY_EXCEPT function returns an ARRAY of matching type to _array1_ with no duplicates.

## Examples

In this example, the first array `[1, 2, 3]` contains the elements 1, 2,
and 3. The second array `[2, 3, 4]` contains the elements 2, 3, and 4. The
`array_except` function removes the elements 2 and 3 from the first array,
since they're also present in the second array. The resulting output is the array
`[1]`.

```
SELECT array_except(array(1, 2, 3), array(2, 3, 4))
  [1]
```

In this example, the first array `[1, 2, 3]` contains the elements 1, 2,
and 3. The second array `[1, 3, 5]` contains the elements 1, 3, and 5. The
`array_except` function removes the elements 1 and 3 from the first array,
since they're also present in the second array. The resulting output is the array
`[2]`.

```
SELECT array_except(array(1, 2, 3), array(1, 3, 5));
 [2]

```
