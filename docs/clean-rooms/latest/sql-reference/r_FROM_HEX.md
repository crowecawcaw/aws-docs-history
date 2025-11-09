# FROM_HEX function

FROM_HEX converts a hexadecimal to a binary value.

## Syntax

```
FROM_HEX(*hex\_string*)
```

## Arguments

_hex_string_

Hexadecimal string of data type `VARCHAR` or
`TEXT` to be converted. The format must be a literal
value.

## Return type

`VARBYTE`

## Example

To convert the hexadecimal representation of `'6162'` to a binary
value, use the following example. The result is automatically shown as the
hexadecimal representation of the binary value.

```
`SELECT FROM_HEX('6162');`

`+----------+
| from_hex |
+----------+
| 6162 |
+----------+`
```
