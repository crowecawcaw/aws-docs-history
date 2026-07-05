Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# FROM\_HEX function

FROM\_HEX converts a hexadecimal to a binary value.

## Syntax

```
FROM_HEX(*hex\_string*)
```

## Arguments

_hex\_string_

Hexadecimal string of data type `VARCHAR` or `TEXT` to be converted. The format must be a literal value.

## Return type

`VARBYTE`

## Examples

To convert the hexadecimal representation of `'6162'` to a binary value, use the following example.
The result is automatically shown as the hexadecimal representation of the binary value.

```
`SELECT FROM_HEX('6162');`

`+----------+
| from_hex |
+----------+
| 6162 |
+----------+`
```
