Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ARRAY\_DISTINCT function

Creates a new array containing only unique elements from the input array, removing all duplicates. The order of elements in the output array is not guaranteed to match the input order. NULL values are treated as valid elements; if multiple NULLs exist in the input array, only one NULL appears in the output.

## Syntax

```
ARRAY_DISTINCT( *array* )
```

## Arguments

_array_

A SUPER expression that specifies the array.

## Return type

The ARRAY\_DISTINCT function returns a SUPER type.

## Example

The following examples show the ARRAY\_DISTINCT function.

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

- [ARRAY\_UNION function](array_union.md "array_union.md")
- [ARRAY\_SORT function](array_sort.md "array_sort.md")
- [ARRAY\_EXCEPT function](array_except.md "array_except.md")
- [ARRAY\_INTERSECTION function](array_intersection.md "array_intersection.md")
