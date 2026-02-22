Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ARRAY_FLATTEN function

Merges multiple arrays into a single array of SUPER type. Elements from the first inner array appear first, followed by elements from subsequent inner arrays. NULLs are treated as known objects.

## Syntax

```
ARRAY_FLATTEN( *array* )
```

## Arguments

_array_

A SUPER expression of array form.

## Return type

The ARRAY_FLATTEN function returns a SUPER type.

## Example

The following example shows the ARRAY_FLATTEN function.

```
SELECT ARRAY_FLATTEN(ARRAY(ARRAY(1,2,3,4),ARRAY(5,6,7,8),ARRAY(9,10)));
     array_flatten
------------------------
 [1,2,3,4,5,6,7,8,9,10]
(1 row)
```

## See also

- [ARRAY_CONCAT function](r_array_concat.md "r_array_concat.md")
- [SUBARRAY function](r_subarray.md "r_subarray.md")
- [ARRAY_DISTINCT function](array_distinct.md "array_distinct.md")
