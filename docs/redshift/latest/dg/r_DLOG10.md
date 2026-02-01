Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

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
