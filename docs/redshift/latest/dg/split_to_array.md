Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SPLIT\_TO\_ARRAY function

Uses a delimiter as an optional parameter. If no delimiter is present, then the
default is a comma.

## Syntax

```
SPLIT_TO_ARRAY( *string*, *delimiter* )
```

## Arguments

**string**

The input string to be split.

**delimiter**

An optional value on which the input string will be split. The default is
a comma.

## Return type

The SPLIT\_TO\_ARRAY function returns a SUPER data value.

## Example

The following example show the SPLIT\_TO\_ARRAY function.

```
SELECT SPLIT_TO_ARRAY('12|345|6789', '|');
     split_to_array
-------------------------
 ["12","345","6789"]
(1 row)
```

## See also

- [ARRAY function](r_array.md "r_array.md")
- [ARRAY\_CONCAT function](r_array_concat.md "r_array_concat.md")
- [SUBARRAY function](r_subarray.md "r_subarray.md")
- [ARRAY\_FLATTEN function](array_flatten.md "array_flatten.md")
