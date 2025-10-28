Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CBRT function

The CBRT function is a mathematical function that calculates the cube root of a
given number.

## Syntax

```
CBRT(*number*)
```

## Arguments

CBRT takes a `DOUBLE PRECISION` number as an argument.

## Return type

`DOUBLE PRECISION`

## Examples

The following example uses the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To calculate the cube root of the commission paid for a given transaction, use the following example.

````
`SELECT CBRT(commission) FROM sales WHERE salesid=10000;`

`+--------------------+
| cbrt | +--------------------+
| 3.0383953904884344 | +--------------------+` ```
````
