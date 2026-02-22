Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ARRAY_UNION function

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

The ARRAY_UNION function returns a SUPER type.

## Example

The following examples show the ARRAY_UNION function.

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

- [ARRAY_CONCAT function](r_array_concat.md "r_array_concat.md")
- [ARRAY_DISTINCT function](array_distinct.md "array_distinct.md")
- [ARRAY_INTERSECTION function](array_intersection.md "array_intersection.md")
- [ARRAY_EXCEPT function](array_except.md "array_except.md")
