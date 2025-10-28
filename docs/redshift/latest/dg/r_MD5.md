Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# MD5 function

Uses the MD5 cryptographic hash function to convert a variable-length string into a
32-character string that is a text representation of the hexadecimal value of a 128-bit
checksum.

## Syntax

```
MD5(*string*)
```

## Arguments

_string_

A variable-length string.

## Return type

The MD5 function returns a 32-character string that is a text representation of
the hexadecimal value of a 128-bit checksum.

## Examples

The following example shows the 128-bit value for the string 'Amazon Redshift':

```
select md5('Amazon Redshift');
md5
----------------------------------
f7415e33f972c03abd4f3fed36748f7a
(1 row)

```
