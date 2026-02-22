Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ARRAY_SORT function

Creates a sorted version of the input array in either ascending or descending order. You can specify where NULL values should appear in the result.
The function is NULL-safe, meaning it treats NULLs are treated as known objects.

## Syntax

```
ARRAY_SORT( *array* [, *sort\_ascending* [, *nulls\_first*]] )
```

## Arguments

_array_

A SUPER expression that specifies the array to be sorted.

_sort_ascending_

A boolean value that specifies whether to sort the array in ascending or descending order:

- Specify TRUE to sort the elements in ascending order.
- Specify FALSE to sort the elements in descending order.

The default is TRUE.

_nulls_first_

A boolean value that specifies the NULL positioning:

- Specify TRUE to place NULLs at the beginning of the sorted array.
- Specify FALSE to place NULLs at the end of the sorted array.

## Return type

The ARRAY_SORT function returns a SUPER type.

## Note

When sorting arrays containing mixed data types, elements are ordered according to the following type precedence:

- Boolean values
- Numeric values
- String values
- Arrays
- Objects/Dictionaries

Within each type category, elements are sorted according to their natural ordering (e.g., numbers are sorted numerically, strings alphabetically).

## Example

The following examples show the ARRAY_SORT function.

```
-- Ascending order (default)
SELECT ARRAY_SORT(ARRAY('b', 'a', 0, NULL, 1, false));
        array_sort
--------------------------
 [false,0,1,"a","b",null]
(1 row)

-- Descending order
SELECT ARRAY_SORT(ARRAY('b', 'a', 0, NULL, 1, false), False);
        array_sort
--------------------------
 [null,"b","a",1,0,false]
(1 row)

-- Descending order with NULLs at the end of the sorted array
SELECT ARRAY_SORT(ARRAY('b', 'a', 0, NULL, 1, false), False, False);
        array_sort
--------------------------
 ["b","a",1,0,false,null]
(1 row)
```

## See also

- [ARRAY_DISTINCT function](array_distinct.md "array_distinct.md")
- [ARRAY_FLATTEN function](array_flatten.md "array_flatten.md")
- [SUBARRAY function](r_subarray.md "r_subarray.md")
