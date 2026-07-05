Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ARRAY\_UNION function

Combines two arrays and returns a single array containing all unique values, removing any duplicates. The function is NULL-safe, meaning it treats NULLs are treated as known objects. The order of elements in the result is not guaranteed.

## Syntax

```
ARRAY_UNION( *array1*, *array2* )
```

## Arguments

_array1_

A SUPER expression that specifies the first array.

_array2_

A SUPER expression that specifies the second array.

## Return type

The ARRAY\_UNION function returns a SUPER type.

## Example

The following examples show the ARRAY\_UNION function.

```
SELECT ARRAY_UNION(ARRAY('a','b','b'), ARRAY('b','c','c'));
  array_union
---------------
 ["a","b","c"]
(1 row)
```

The order of elements is not guaranteed:

```
SELECT ARRAY_UNION(ARRAY('b','a','b'), ARRAY(NULL,'b',NULL));
  array_union
----------------
 ["b","a",null]
(1 row)
```

## See also

- [ARRAY\_CONCAT function](r_array_concat.md "r_array_concat.md")
- [ARRAY\_DISTINCT function](array_distinct.md "array_distinct.md")
- [ARRAY\_INTERSECTION function](array_intersection.md "array_intersection.md")
- [ARRAY\_EXCEPT function](array_except.md "array_except.md")
