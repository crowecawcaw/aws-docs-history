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

The format of the returned character string. Case insensitive valid
values are `hex`, `binary`, `utf-8`,
and `utf8`.

## Return type

`VARCHAR`

## Example

To convert the binary value `'ab'` to hexadecimal, use the following
example.

```
`SELECT FROM_VARBYTE('ab', 'hex');`

`+--------------+
| from_varbyte |
+--------------+
| 6162 |
+--------------+`
```
