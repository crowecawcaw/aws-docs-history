Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# array_concat function

The array_concat function concatenates two arrays to create an array that contains
all the elements in the first array followed by all the elements in the second array.
The two arguments must be valid arrays.

## Syntax

```
array_concat( *super\_expr1*,  *super\_expr2* )
```

## Arguments

_super_expr1_

The value that specifies the first of the two arrays to concatenate.

_super_expr2_

The value that specifies the second of the two arrays to concatenate.

## Return type

The array_concat function returns a SUPER data value.

## Example

The following examples shows concatenation of two arrays of the same type and concatenation of two arrays of different types.

```
-- concatenating two arrays
SELECT ARRAY_CONCAT(ARRAY(10001,10002),ARRAY(10003,10004));
              array_concat
------------------------------------
 [10001,10002,10003,10004]
(1 row)

-- concatenating two arrays of different types
SELECT ARRAY_CONCAT(ARRAY(10001,10002),ARRAY('ab','cd'));
          array_concat
------------------------------
 [10001,10002,"ab","cd"]
(1 row)
```
