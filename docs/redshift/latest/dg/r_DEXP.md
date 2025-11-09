Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DEXP function

The DEXP function returns the exponential value in scientific notation for a double
precision number. The only difference between the DEXP and EXP functions is that the
parameter for DEXP must be a `DOUBLE PRECISION`.

## Syntax

```
DEXP(*number*)
```

## Argument

_number_

The input parameter is a `DOUBLE PRECISION` number.

## Return type

`DOUBLE PRECISION`

## Example

The following example uses the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

Use the DEXP function to forecast ticket sales based on a continuous growth
pattern. In this example, the subquery returns the number of tickets sold in 2008.
That result is multiplied by the result of the DEXP function, which specifies a
continuous growth rate of 7% over 10 years.

```
`SELECT (SELECT SUM(qtysold)
FROM sales, date
WHERE sales.dateid=date.dateid
AND year=2008) * DEXP((7::FLOAT/100)*10) qty2010;`

`+-------------------+
| qty2010 |
+-------------------+
| 695447.4837722216 |
+-------------------+`
```
