Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ABS function

ABS calculates the absolute value of a number, where that number can be a literal or
an expression that evaluates to a number.

## Syntax

```
ABS(*number*)
```

## Arguments

_number_

Number or expression that evaluates to a number. It can be the
`SMALLINT`, `INTEGER`, `BIGINT`, `DECIMAL`, `FLOAT4`, `FLOAT8`, or `SUPER` type.

## Return type

ABS returns the same data type as its argument.

## Examples

To calculate the absolute value of `-38`, use the following example.

```
`SELECT ABS(-38);`

`+-----+
| abs |
+-----+
| 38 |
+-----+`
```

To calculate the absolute value of `(14-76)`, use the following example.

```
`SELECT ABS(14-76);`

`+-----+
| abs |
+-----+
| 62 |
+-----+`
```
