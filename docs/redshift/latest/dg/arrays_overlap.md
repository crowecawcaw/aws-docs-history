Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ARRAYS\_OVERLAP function

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

The ARRAYS\_OVERLAP function returns a Boolean type.

## Example

The following examples show the ARRAYS\_OVERLAP function.

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

- [ARRAY\_INTERSECTION function](array_intersection.md "array_intersection.md")
- [ARRAY\_CONTAINS function](array_contains.md "array_contains.md")
- [ARRAY\_EXCEPT function](array_except.md "array_except.md")
