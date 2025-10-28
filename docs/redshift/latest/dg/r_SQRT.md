Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SQRT function

The SQRT function returns the square root of a `NUMERIC` value. The square root is a
number multiplied by itself to get the given value.

## Syntax

```
SQRT(*expression*)
```

## Argument

_expression_

The expression must have an `INTEGER`, `DECIMAL`, or `FLOAT` data
type, or a data type that implicitly converts to those data types. The _expression_ can include functions.

## Return type

`DOUBLE PRECISION`

## Examples

To return the square root of 16, use the following example.

````
`SELECT SQRT(16);`

`+------+
| sqrt | +------+
| 4 | +------+` ``` To return the square root of the string `16` using an implicit type conversion, use the following example. ``` `SELECT SQRT('16');` `+------+
| sqrt | +------+
| 4 | +------+` ``` To return the square root of 16.4 after using the ROUND function, use the following example. ``` `SELECT SQRT(ROUND(16.4));` `+------+
| sqrt | +------+
| 4 | +------+` ``` To return the length of the radius when given the area of a circle, use the following example. It calculates the radius in inches, for instance, when given the area in square inches. The area in the sample is 20. ``` `SELECT SQRT(20/PI()) AS radius;` `+--------------------+
| radius | +--------------------+
| 2.5231325220201604 | +--------------------+` ``` The following examples use the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md"). To return the square root for COMMISSION values from the SALES table, use the following example. The COMMISSION column is a `DECIMAL` column. This example shows how you can use the function in a query with more complex conditional logic. ``` `SELECT SQRT(commission) FROM sales WHERE salesid < 10 ORDER BY salesid;` `+--------------------+
| sqrt | +--------------------+
| 10.449880382090505 |
| 3.3763886032268267 |
| 7.245688373094719 |
| 5.123475382979799 |
| 4.806245936279167 |
| 7.687652437513028 |
| 10.871982339941507 |
| 5.4359911699707535 |
| 9.41541289588513 | +--------------------+` ``` To return the rounded square root for the same set of COMMISSION values, use the following example. ``` `SELECT ROUND(SQRT(commission)) FROM sales WHERE salesid < 10 ORDER BY salesid;` `+-------+
| round | +-------+
| 10 |
| 3 |
| 7 |
| 5 |
| 5 |
| 8 |
| 11 |
| 5 |
| 9 | +-------+` ```
````
