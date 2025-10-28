# CAN_JSON_PARSE function

The CAN_JSON_PARSE function parses data in JSON format and returns `true` if
the result can be converted to a `SUPER` value using the JSON_PARSE
function.

## Syntax

```
CAN_JSON_PARSE(*json\_string*)
```

## Arguments

_json_string_

An expression that returns serialized JSON in the `VARBYTE` or
`VARCHAR` form.

## Return type

`BOOLEAN`

## Example

To see if the JSON array `[10001,10002,"abc"]` can be converted into the
`SUPER` data type, use the following example.

````
`SELECT CAN_JSON_PARSE('[10001,10002,"abc"]');`

`+----------------+
| can_json_parse | +----------------+
| true | +----------------+` ```
````
