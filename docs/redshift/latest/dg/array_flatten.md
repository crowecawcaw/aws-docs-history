Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# array_flatten function

Merges multiple arrays into a single array of SUPER type.

## Syntax

```
array_flatten( *super\_expr1*,*super\_expr2*,.. )
```

## Arguments

_super_expr1_,_super_expr2_

A valid SUPER expression of array form.

## Return type

The array_flatten function returns a SUPER data value.

## Example

The following example shows an array_flatten function.

```
SELECT ARRAY_FLATTEN(ARRAY(ARRAY(1,2,3,4),ARRAY(5,6,7,8),ARRAY(9,10)));
     array_flatten
------------------------
 [1,2,3,4,5,6,7,8,9,10]
(1 row)
```
