Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# LOG function

Returns logarithm of a number.

If you're using this function to calculate
the base 10 logarithm, you can also use [DLOG10 function](r_DLOG10.md "r_DLOG10.md").

## Syntax

```
LOG([*base*, ]*argument*)
```

## Parameters

_base_

(Optional) The base of the logarithm function. This number must be positive and can't equal `1`. If this parameter is omitted, Amazon Redshift computes the base 10 logarithm of the _argument_.

_argument_

The argument of the logarithm function. This number must be positive. If the _argument_ value is `1`, the function returns `0`.

## Return type

The LOG function returns a `DOUBLE PRECISION` number.

## Examples

To find the base 2 logarithm of 100, use the following example.

```
`SELECT LOG(2, 100);`
`+-------------------+
| log |
+-------------------+
| 6.643856189774725 |
+-------------------+`
```

To find the base 10 logarithm of 100, use the following example. Note that if you omit the base parameter, Amazon Redshift assumes a base of 10.

```
`SELECT LOG(100);`

`+-----+
| log |
+-----+
| 2 |
+-----+`
```
