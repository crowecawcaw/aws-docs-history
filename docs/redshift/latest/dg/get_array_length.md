Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# get_array_length function

Returns the length of the specified array. The GET_ARRAY_LENGTH function returns the
length of a SUPER array given an object or array path.

## Syntax

```
get_array_length( *super\_expr* )
```

## Arguments

_super_expr_

A valid SUPER expression of array form.

## Return type

The get_array_length function returns an INT.

## Example

The following example shows a get_array_length function.

```
SELECT GET_ARRAY_LENGTH(ARRAY(1,2,3,4,5,6,7,8,9,10));
 get_array_length
----------------------
            10
(1 row)
```
