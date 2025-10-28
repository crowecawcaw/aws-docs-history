# ARRAY_FLATTEN function

The ARRAY_FLATTEN function merges multiple arrays into a single array of SUPER type.

## Syntax

```
array_flatten( super_expr1,super_expr2,.. )
```

## Arguments

_super_expr1, super_expr2_

A valid SUPER expression of array form.

## Return type

The ARRAY_FLATTEN function returns a SUPER data value.

## Example

The following example shows an ARRAY_FLATTEN function.

```
SELECT ARRAY_FLATTEN(ARRAY(ARRAY(1,2,3,4),ARRAY(5,6,7,8),ARRAY(9,10)));
     array_flatten
------------------------
 [1,2,3,4,5,6,7,8,9,10]
(1 row)
```
