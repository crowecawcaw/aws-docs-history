Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# COS function

COS is a trigonometric function that returns the cosine of a number.

The return value is in radians and is between `-1` and `1`, inclusive.

## Syntax

```
COS(*double\_precision*)
```

## Arguments

_number_

The input parameter is a `DOUBLE PRECISION` number.

## Return type

The COS function returns a `DOUBLE PRECISION` number.

## Examples

To return the cosine of `0`, use the following example.

````
`SELECT COS(0);`

`+-----+
| cos | +-----+
| 1 | +-----+` ``` To return the cosine of `pi`, use the following example. ``` `SELECT COS(PI());` `+-----+
| cos | +-----+
| -1 | +-----+` ```
````
