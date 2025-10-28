Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# FROM_VARBYTE function

FROM_VARBYTE converts a binary value to a character string in the specified format.

## Syntax

```
FROM_VARBYTE(*binary\_value*, *format*)
```

## Arguments

_binary_value_

A binary value of data type `VARBYTE`.

_format_

The format of the returned character string.
Case insensitive valid values are `hex`, `binary`, `utf8` (also `utf-8` and `utf_8`), and `base64`.

## Return type

`VARCHAR`

## Examples

To convert the binary value `'ab'` to hexadecimal, use the following example.

````
`SELECT FROM_VARBYTE('ab', 'hex');`

`+--------------+
| from_varbyte | +--------------+
| 6162 | +--------------+` ``` To return the binary representation of `'4d'`, use the following example. The binary representation of `'4d'` is the character string `01001101`. ``` `SELECT FROM_VARBYTE(FROM_HEX('4d'), 'binary');` `+--------------+
| from_varbyte | +--------------+
| 01001101 | +--------------+` ```
````
