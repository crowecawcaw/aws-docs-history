Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SUBARRAY function

Extracts a portion of an array starting from a specified position. Returns a new array containing the specified number of elements from the input array.

## Syntax

```
SUBARRAY( *super\_expr*, *start\_position*, *length* )
```

## Arguments

_super_expr_

A valid SUPER expression in array form.

_start_position_

An integer that specifies the starting position for extraction. The index is 0-based, where 0 indicates the first element. If start_position is beyond the array length, an empty array is returned.

_length_

An optional integer that specifies the number of elements to extract. If omitted, all elements from the start position to the end of the array are returned.

## Return type

The SUBARRAY function returns a SUPER data value.

## Examples

The following is an example of a SUBARRAY function.

```
 SELECT SUBARRAY(ARRAY('a', 'b', 'c', 'd', 'e', 'f'), 2, 3);
   subarray
---------------
 ["c","d","e"]
(1 row)

```

## See also

- [ARRAY_POSITION function](array_position.md "array_position.md")
- [ARRAY_POSITIONS function](array_positions.md "array_positions.md")
- [ARRAY_FLATTEN function](array_flatten.md "array_flatten.md")
- [ARRAY_CONCAT function](r_array_concat.md "r_array_concat.md")
