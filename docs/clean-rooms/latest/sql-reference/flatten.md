# FLATTEN function

The FLATTEN function is used to "flatten" a nested array structure into a single flat
array.

## Syntax

```
flatten(arrayOfArrays)
```

## Arguments

_arrayOfArrays_

An array of arrays.

## Return type

The FLATTEN function returns an array.

## Example

In this example, the input is a nested array with two inner arrays, and the output is
a single flat array containing all the elements from the inner arrays. The FLATTEN
function takes the nested array `[[1, 2], [3, 4]]` and combines all the
elements into a single array `[1, 2, 3, 4]`.

```
SELECT flatten(array(array(1, 2), array(3, 4)));
 [1,2,3,4]
```
