# GET_ARRAY_LENGTH function

Returns the length of the specified array. The GET_ARRAY_LENGTH function returns the
length of a SUPER array given an object or array path.

## Syntax

```
get_array_length( *super\_expr* )
```

## Arguments

_super_expr_

A valid SUPER expression of array form.

## Return type

The get_array_length function returns a BIGINT.

## Example

The following example shows a get_array_length function.

```
SELECT GET_ARRAY_LENGTH(ARRAY(1,2,3,4,5,6,7,8,9,10));
 get_array_length
----------------------
            10
(1 row)
```
