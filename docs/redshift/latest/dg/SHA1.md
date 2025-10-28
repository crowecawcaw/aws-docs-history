Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHA1 function

The SHA1 function uses the SHA1 cryptographic hash function to convert a
variable-length string into a 40-character string that is a text representation of the
hexadecimal value of a 160-bit checksum.

## Syntax

SHA1 is a synonym of [SHA function](SHA.md "SHA.md") and [FUNC_SHA1 function](FUNC_SHA1.md "FUNC_SHA1.md").

```
SHA1(*string*)
```

## Arguments

_string_

A variable-length string.

## Return type

The SHA1 function returns a 40-character string that is a text representation
of the hexadecimal value of a 160-bit checksum.

## Example

The following example returns the 160-bit value for the word 'Amazon Redshift':

```
select sha1('Amazon Redshift');

```
