Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TO_VARBYTE function

TO_VARBYTE converts a string in a specified format to a binary value.

## Syntax

```
TO_VARBYTE(*string*, *format*)
```

## Arguments

_string_

A `CHAR` or `VARCHAR` string.

_format_

The format of the input string.
Case insensitive valid values are `hex`, `binary`, `utf8` (also `utf-8` and `utf_8`), and `base64`.

## Return type

`VARBYTE`

## Examples

To convert the hex `6162` to a binary value, use the following example.
The result is automatically shown as the hexadecimal representation of the binary value.

```
`SELECT TO_VARBYTE('6162', 'hex');`

`+------------+
| to_varbyte |
+------------+
| 6162 |
+------------+`
```

To return the binary representation of `4d`, use the following example.
The binary representation of '4d' is `01001101`.

```
`SELECT TO_VARBYTE('01001101', 'binary');`

`+------------+
| to_varbyte |
+------------+
| 4d |
+------------+`
```

To convert the string `'a'` in UTF-8 to a binary value, use the following example.
The result is automatically shown as the hexadecimal representation of the binary value.

```
`SELECT TO_VARBYTE('a', 'utf8');`

`+------------+
| to_varbyte |
+------------+
| 61 |
+------------+`
```

To convert the string `'4'` in hexadecimal to a binary value, use the following example.
If the hexadecimal string length is an odd number, then a `0` is prepended to form a valid hexadecimal number.

```
`SELECT TO_VARBYTE('4', 'hex');`

`+------------+
| to_varbyte |
+------------+
| 04 |
+------------+`
```
