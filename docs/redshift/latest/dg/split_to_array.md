Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# split_to_array function

Uses a delimiter as an optional parameter. If no delimiter is present, then the
default is a comma.

## Syntax

```
split_to_array( *string*,*delimiter* )
```

## Arguments

**string**

The input string to be split.

**delimiter**

An optional value on which the input string will be split. The default is
a comma.

## Return type

The split_to_array function returns a SUPER data value.

## Example

The following example show a split_to_array function.

```
SELECT SPLIT_TO_ARRAY('12|345|6789', '|');
     split_to_array
-------------------------
 ["12","345","6789"]
(1 row)
```
