# IS_ARRAY function

Checks whether a variable is an array. The function returns `true` if the
variable is an array. The function also includes empty arrays. Otherwise, the function
returns `false` for all other values, including null.

## Syntax

```
IS_ARRAY(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Example

To check if `[1,2]` is an array using the IS_ARRAY function, use the
following example.

````
`SELECT IS_ARRAY(JSON_PARSE('[1,2]'));`

`+----------+
| is_array | +----------+
| true | +----------+` ```
````
