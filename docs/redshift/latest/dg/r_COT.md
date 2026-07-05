Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# COT function

COT is a trigonometric function that returns the cotangent of a number. The input
parameter must be nonzero.

## Syntax

```
COT(*number*)
```

## Argument

_number_

The input parameter is a `DOUBLE PRECISION` number.

## Return type

`DOUBLE PRECISION`

## Examples

To return the cotangent of 1, use the following example.

```
`SELECT COT(1);`

`+--------------------+
| cot |
+--------------------+
| 0.6420926159343306 |
+--------------------+`
```
