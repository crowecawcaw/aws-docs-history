Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ARRAYS_OVERLAP function

Checks whether two arrays have any common elements. Returns TRUE if the arrays share at least one element, or FALSE if no common elements exist. The function is NULL-safe, meaning it treats NULLs are treated as known objects.

## Syntax

```
ARRAYS_OVERLAP( *array1*, *array2* )
```

## Arguments

_array1_

A SUPER expression that specifies an array.

_array2_

A SUPER expression that specifies an array.

## Return type

The ARRAYS_OVERLAP function returns a Boolean type.

## Example

The following examples show the ARRAYS_OVERLAP function.

```
SELECT ARRAYS_OVERLAP(ARRAY('blue', 'green'), ARRAY('red', 'green'));
 arrays_overlap
----------------
 t
(1 row)
```

The following examples show that NULLs are treated as valid elements.

```
SELECT ARRAYS_OVERLAP(ARRAY('red', NULL, 'blue'), ARRAY('green', NULL));
 arrays_overlap
----------------
 t
(1 row)

SELECT ARRAYS_OVERLAP(ARRAY('red', NULL, 'blue'), ARRAY('green'));
 arrays_overlap
----------------
 f
(1 row)

SELECT ARRAYS_OVERLAP(JSON_PARSE('[null]'), ARRAY(NULL));
 arrays_overlap
----------------
 t
(1 row)
```

## See also

- [ARRAY_INTERSECTION function](array_intersection.md "array_intersection.md")
- [ARRAY_CONTAINS function](array_contains.md "array_contains.md")
- [ARRAY_EXCEPT function](array_except.md "array_except.md")
