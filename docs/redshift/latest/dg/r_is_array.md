Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

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

## Examples

To check if `[1,2]` is an array using the IS_ARRAY function, use the following example.

````
`SELECT IS_ARRAY(JSON_PARSE('[1,2]'));`

`+----------+
| is_array | +----------+
| true | +----------+` ```
````
