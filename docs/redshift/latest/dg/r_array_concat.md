Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ARRAY\_CONCAT function

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

The ARRAY\_CONCAT function returns a SUPER data value.

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

- [ARRAY\_UNION function](array_union.md "array_union.md")
- [ARRAY\_FLATTEN function](array_flatten.md "array_flatten.md")
- [SPLIT\_TO\_ARRAY function](split_to_array.md "split_to_array.md")
- [ARRAY\_DISTINCT function](array_distinct.md "array_distinct.md")
