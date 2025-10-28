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

The format of the input string. Case insensitive valid values are
`hex`, `binary`, `utf-8`, and
`utf8`.

## Return type

`VARBYTE`

## Example

To convert the hex `6162` to a binary value, use the following example.
The result is automatically shown as the hexadecimal representation of the binary
value.

````
`SELECT TO_VARBYTE('6162', 'hex');`

`+------------+
| to_varbyte | +------------+
| 6162 | +------------+` ```
````
