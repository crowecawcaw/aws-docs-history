Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# DLOG10 function

The DLOG10 returns the base 10 logarithm of the input parameter.

Synonym of [LOG function](r_LOG.md "r_LOG.md").

## Syntax

```
DLOG10(*number*)
```

## Argument

_number_

The input parameter is a `DOUBLE PRECISION` number.

## Return type

`DOUBLE PRECISION`

## Example

To return the base 10 logarithm of the number 100, use the following example.

```
`SELECT DLOG10(100);`

`+--------+
| dlog10 |
+--------+
| 2 |
+--------+`
```
