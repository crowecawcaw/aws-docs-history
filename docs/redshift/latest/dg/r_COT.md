Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

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

````
`SELECT COT(1);`

`+--------------------+
| cot | +--------------------+
| 0.6420926159343306 | +--------------------+` ```
````
