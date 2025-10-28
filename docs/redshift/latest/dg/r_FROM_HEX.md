Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# FROM_HEX function

FROM_HEX converts a hexadecimal to a binary value.

## Syntax

```
FROM_HEX(*hex\_string*)
```

## Arguments

_hex_string_

Hexadecimal string of data type `VARCHAR` or `TEXT` to be converted. The format must be a literal value.

## Return type

`VARBYTE`

## Examples

To convert the hexadecimal representation of `'6162'` to a binary value, use the following example.
The result is automatically shown as the hexadecimal representation of the binary value.

````
`SELECT FROM_HEX('6162');`

`+----------+
| from_hex | +----------+
| 6162 | +----------+` ```
````
