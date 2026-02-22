Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ARRAY_EXCEPT function

Returns the difference between two arrays by keeping elements from the first array that do not exist in the second array. The function is NULL-safe, meaning it treats NULLs are treated as known objects.

## Syntax

```
ARRAY_EXCEPT( *array1*, *array2* [, *distinct*] )
```

## Arguments

_array1_

A SUPER expression that specifies the first array.

_array2_

A SUPER expression that specifies the second array.

_distinct_

A boolean value that specifies whether to return distinct elements only:

- _distinct_ = FALSE: Multi-set semantics apply. Each occurrence of an element in the first array is matched against occurrences in the second array. If the first array has more occurrences of an element than the second array, the extra occurrences are preserved in the result.
- _distinct_ = TRUE: Set semantics apply. Both arrays are treated as sets, ignoring duplicate elements. Elements from the first array are removed if they exist anywhere in the second array, regardless of occurrence count.

The default is FALSE.

## Return type

The ARRAY_EXCEPT function returns a SUPER type.

## Example

The following examples show the ARRAY_EXCEPT function.

```
SELECT ARRAY_EXCEPT(ARRAY('a','b','c'), ARRAY('b','c','d'));
 array_except
--------------
 ["a"]
(1 row)
```

Multi-set semantics:

```
SELECT ARRAY_EXCEPT(ARRAY('b','b','b','b'), ARRAY('b','b'));
 array_except
--------------
 ["b","b"]
(1 row)
```

Set semantics:

```
SELECT ARRAY_EXCEPT(ARRAY('a','b','b'), ARRAY('b'), TRUE);
 array_except
--------------
 ["a"]
(1 row)
```

NULLs are treated as known object.

```
SELECT ARRAY_EXCEPT(ARRAY('a',NULL), ARRAY(NULL));
 array_except
--------------
 ["a"]
(1 row)
```

## See also

- [ARRAY_INTERSECTION function](array_intersection.md "array_intersection.md")
- [ARRAY_UNION function](array_union.md "array_union.md")
- [ARRAY_DISTINCT function](array_distinct.md "array_distinct.md")
- [ARRAYS_OVERLAP function](arrays_overlap.md "arrays_overlap.md")
