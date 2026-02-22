Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ARRAY_CONCAT function

Concatenates two arrays to create an array that contains
all the elements in the first array followed by all the elements in the second array.
The two arguments must be valid SUPER arrays.

## Syntax

```
ARRAY_CONCAT( *array1*, *array2* )
```

## Arguments

_array1_

The value that specifies the first of the two arrays to concatenate.

_array2_

The value that specifies the second of the two arrays to concatenate.

## Return type

The ARRAY_CONCAT function returns a SUPER data value.

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

## See also

- [ARRAY_UNION function](array_union.md "array_union.md")
- [ARRAY_FLATTEN function](array_flatten.md "array_flatten.md")
- [SPLIT_TO_ARRAY function](split_to_array.md "split_to_array.md")
- [ARRAY_DISTINCT function](array_distinct.md "array_distinct.md")
