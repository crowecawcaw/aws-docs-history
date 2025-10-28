Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# FLOOR function

The FLOOR function rounds a number down to the next whole number.

## Syntax

```
FLOOR(*number*)
```

## Argument

_number_

The number or expression that evaluates to a number. It can be the
`SMALLINT`, `INTEGER`, `BIGINT`, `DECIMAL`, `FLOAT4`, `FLOAT8`, or `SUPER` type.

## Return type

FLOOR returns the same data type as its argument.

When the input is of the `SUPER` type, the output retains the same dynamic type as the input while the static type remains the `SUPER` type. When the dynamic type of `SUPER` isn't a number, Amazon Redshift returns `NULL`.

## Examples

The following examples use the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To show the value of the commission paid for a given sales transaction before and after using the FLOOR function, use the following example.

````
`SELECT commission
FROM sales
WHERE salesid=10000;`

`+------------+
| commission | +------------+
| 28.05 | +------------+` `SELECT FLOOR(commission) FROM sales WHERE salesid=10000;` `+-------+
| floor | +-------+
| 28 | +-------+` ```
````
