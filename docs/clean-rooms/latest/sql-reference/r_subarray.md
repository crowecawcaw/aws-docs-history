# SUBARRAY function

Manipulates arrays to return a subset of the input arrays.

## Syntax

```
SUBARRAY( *super\_expr*, *start\_position*, *length* )
```

## Arguments

_super_expr_

A valid SUPER expression in array form.

_start_position_

The position within the array to begin the extraction, starting at index
position 0. A negative position counts backward from the end of the
array.

_length_

The number of elements to extract (the length of the substring).

## Return type

The subarray function returns a SUPER data value.

## Example

The following is an example of a subarray function.

```
 SELECT SUBARRAY(ARRAY('a', 'b', 'c', 'd', 'e', 'f'), 2, 3);
   subarray
---------------
 ["c","d","e"]
(1 row)

```
