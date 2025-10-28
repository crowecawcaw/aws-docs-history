Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# POWER function

The POWER function is an exponential function that raises a numeric expression to
the power of a second numeric expression. For example, 2 to the third power is
calculated as `POWER(2,3)`, with a result of `8`.

## Syntax

```
{POW | POWER}(*expression1*, *expression2*)
```

## Arguments

_expression1_

Numeric expression to be raised. Must be an `INTEGER`, `DECIMAL`, or
`FLOAT` data type.

_expression2_

Power to raise _expression1_. Must be an `INTEGER`, `DECIMAL`, or
`FLOAT` data type.

## Return type

`DOUBLE PRECISION`

## Examples

The following examples use the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

In the following example, the POWER function is used to forecast what ticket sales
will look like in the next 10 years, based on the number of tickets sold in 2008 (the
result of the subquery). The growth rate is set at 7% per year in this example.

````
`SELECT (SELECT SUM(qtysold) FROM sales, date
WHERE sales.dateid=date.dateid
AND year=2008) * POW((1+7::FLOAT/100),10) qty2010;`

`+-------------------+
| qty2010 | +-------------------+
| 679353.7540885945 | +-------------------+` ``` The following example is a variation on the previous example, with the growth rate at 7% per year but the interval is set to months (120 months over 10 years). ``` `SELECT (SELECT SUM(qtysold) FROM sales, date WHERE sales.dateid=date.dateid AND year=2008) * POW((1+7::FLOAT/100/12),120) qty2010;` `+-----------------+
| qty2010 | +-----------------+
| 694034.54678046 | +-----------------+` ```
````
