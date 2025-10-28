Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SIGN function

The SIGN function returns the sign (positive or negative) of a number. The
result of the SIGN function is `1` if the argument is positive, `-1` if the argument is negative, or `0`
if the argument is `0`.

## Syntax

```
SIGN(*number*)
```

## Argument

_number_

Number or expression that evaluates to a number. It can be a `DECIMAL`, `FLOAT8`, or `SUPER` type. Amazon Redshift can convert other data types per the implicit conversion rules.

## Return type

SIGN returns the same numeric data type as the input argument. If the input is `DECIMAL`, the output is `DECIMAL(1,0)`.

When the input is of the `SUPER` type, the output retains the same dynamic type as the input while the static type remains the `SUPER` type. When the dynamic type of `SUPER` isn't a number, Amazon Redshift returns a `NULL`.

## Examples

The following example shows that column `d` in table t2 has `DOUBLE PRECISION` as its type since
the input is `DOUBLE PRECISION` and that column `n` in table t2 has `NUMERIC(1,0)` as the
output since the input is `NUMERIC`.

````
`CREATE TABLE t1(d DOUBLE PRECISION, n NUMERIC(12, 2));
INSERT INTO t1 VALUES (4.25, 4.25), (-4.25, -4.25);
CREATE TABLE t2 AS SELECT SIGN(d) AS d, SIGN(n) AS n FROM t1;
SELECT table_name, column_name, data_type FROM SVV_REDSHIFT_COLUMNS WHERE table_name='t1' OR table_name='t2';`

`+------------+-------------+-----------------------+
| table_name | column_name | data_type | +------------+-------------+-----------------------+
| t1 | d | double precision |
| t1 | n | numeric(12,2) |
| t2 | d | double precision |
| t2 | n | numeric(1,0) |
| t1 | col1 | character varying(20) | +------------+-------------+-----------------------+` ``` The following example uses the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md"). To determine the sign of the commission paid for a given transaction from the SALES table, use the following example. ``` `SELECT commission, SIGN(commission) FROM sales WHERE salesid=10000;` `+------------+------+
| commission | sign | +------------+------+ | 28.05 | 1 | +------------+------+` ```
````
