Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ARRAY_INTERSECTION function

Returns a new array containing only the elements that exist in both input arrays. The function is NULL-safe, meaning it treats NULLs are treated as known objects. The order of elements in the result is not guaranteed.

## Syntax

```
ARRAY_INTERSECTION( *array1*, *array2* [, *distinct*] )
```

## Arguments

_array1_

A SUPER expression that specifies an array.

_array2_

A SUPER expression that specifies an array.

_distinct_

A boolean value that specifies whether to return distinct elements only:

- _distinct_ = FALSE: Multi-set semantics apply. Duplicate elements are preserved, and the frequency of each element in the result equals the minimum of its frequencies in the two input arrays.
- _distinct_ = TRUE: Set semantics apply. Only unique elements common to both arrays are returned, with no duplicates.

The default is FALSE.

## Return type

The ARRAY_INTERSECTION function returns a SUPER type.

## Example

The following examples show the ARRAY_INTERSECTION function.

```
SELECT ARRAY_INTERSECTION(ARRAY('a','b','c'), ARRAY('b','c','d'));
 array_intersection
--------------------
 ["b","c"]
(1 row)
```

Multi-set semantics:

```
SELECT ARRAY_INTERSECTION(ARRAY('a','b','b'), ARRAY('b','b','b'));
 array_intersection
--------------------
 ["b","b"]
(1 row)
```

Set semantics:

```
SELECT ARRAY_INTERSECTION(ARRAY('a','b','b'), ARRAY('b','b','b'), TRUE);
 array_intersection
--------------------
 ["b"]
(1 row)
```

NULLs are treated as known object.

```
SELECT ARRAY_INTERSECTION(ARRAY('a',NULL), ARRAY('b',NULL));
 array_intersection
--------------------
 [null]
(1 row)
```

## See also

- [ARRAY_EXCEPT function](array_except.md "array_except.md")
- [ARRAYS_OVERLAP function](arrays_overlap.md "arrays_overlap.md")
- [ARRAY_UNION function](array_union.md "array_union.md")
- [ARRAY_DISTINCT function](array_distinct.md "array_distinct.md")
