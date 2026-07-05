Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# IS\_ARRAY function

Checks whether a variable is an array. The function returns `true` if the
variable is an array. The function also includes empty arrays. Otherwise, the function
returns `false` for all other values, including null.

## Syntax

```
IS_ARRAY(*super\_expression*)

```

## Arguments

_super\_expression_

A `SUPER` expression or column.

## Return type

`BOOLEAN`

## Examples

To check if `[1,2]` is an array using the IS\_ARRAY function, use the following example.

```
`SELECT IS_ARRAY(JSON_PARSE('[1,2]'));`

`+----------+
| is_array |
+----------+
| true |
+----------+`
```
