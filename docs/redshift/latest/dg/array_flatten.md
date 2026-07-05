Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ARRAY\_FLATTEN function

Merges multiple arrays into a single array of SUPER type. Elements from the first inner array appear first, followed by elements from subsequent inner arrays. NULLs are treated as known objects.

## Syntax

```
ARRAY_FLATTEN( *array* )
```

## Arguments

_array_

A SUPER expression of array form.

## Return type

The ARRAY\_FLATTEN function returns a SUPER type.

## Example

The following example shows the ARRAY\_FLATTEN function.

```
SELECT ARRAY_FLATTEN(ARRAY(ARRAY(1,2,3,4),ARRAY(5,6,7,8),ARRAY(9,10)));
     array_flatten
------------------------
 [1,2,3,4,5,6,7,8,9,10]
(1 row)
```

## See also

- [ARRAY\_CONCAT function](r_array_concat.md "r_array_concat.md")
- [SUBARRAY function](r_subarray.md "r_subarray.md")
- [ARRAY\_DISTINCT function](array_distinct.md "array_distinct.md")
