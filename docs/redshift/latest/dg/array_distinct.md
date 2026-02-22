Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ARRAY_DISTINCT function

Creates a new array containing only unique elements from the input array, removing all duplicates. The order of elements in the output array is not guaranteed to match the input order. NULL values are treated as valid elements; if multiple NULLs exist in the input array, only one NULL appears in the output.

## Syntax

```
ARRAY_DISTINCT( *array* )
```

## Arguments

_array_

A SUPER expression that specifies the array.

## Return type

The ARRAY_DISTINCT function returns a SUPER type.

## Example

The following examples show the ARRAY_DISTINCT function.

```
SELECT ARRAY_DISTINCT(ARRAY(1, 1, 'a', 'a', NULL, NULL));
 array_distinct
----------------
 [1,"a",null]
(1 row)

SELECT ARRAY_DISTINCT(ARRAY_CONCAT(ARRAY(1,2,3,3),ARRAY(2,3,4,4)));
 array_distinct
----------------
 [1,2,3,4]
(1 row)
```

## See also

- [ARRAY_UNION function](array_union.md "array_union.md")
- [ARRAY_SORT function](array_sort.md "array_sort.md")
- [ARRAY_EXCEPT function](array_except.md "array_except.md")
- [ARRAY_INTERSECTION function](array_intersection.md "array_intersection.md")
