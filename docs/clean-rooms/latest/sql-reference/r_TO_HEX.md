# TO_HEX function

TO_HEX converts a number or binary value to a hexadecimal representation.

## Syntax

```
TO_HEX(*value*)
```

## Arguments

_value_

Either a number or binary value (`VARBYTE`) to be
converted.

## Return type

`VARCHAR`

## Example

To convert a number to its hexadecimal representation, use the following example.

```
`SELECT TO_HEX(2147676847);`

`+----------+
| to_hex |
+----------+
| 8002f2af |
+----------+`To create a table, insert the `VARBYTE` representation of `'abc'` to a hexadecimal number, and select the column with the value, use the following example.
```
