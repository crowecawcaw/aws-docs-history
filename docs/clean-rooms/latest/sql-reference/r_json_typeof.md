# JSON_TYPEOF function

The JSON_TYPEOF scalar function returns a `VARCHAR` with values boolean,
number, string, object, array, or null, depending on the dynamic type of the
`SUPER` value.

## Syntax

```
JSON_TYPEOF(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`VARCHAR`

## Example

To check the type of JSON for the array `[1,2]` using the JSON_TYPEOF
function, use the following example.

```
`SELECT JSON_TYPEOF(ARRAY(1,2));`

`+-------------+
| json_typeof |
+-------------+
| array |
+-------------+`
```
