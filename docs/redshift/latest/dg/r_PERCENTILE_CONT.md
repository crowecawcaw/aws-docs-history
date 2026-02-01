Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PERCENTILE_CONT function

PERCENTILE_CONT is an inverse distribution function that assumes a continuous
distribution model. It takes a percentile value and a sort specification, and returns an
interpolated value that would fall into the given percentile value with respect to the
sort specification.

PERCENTILE_CONT computes a linear interpolation between values after ordering them.
Using the percentile value `(P)` and the number of not null rows
`(N)` in the aggregation group, the function computes the row number after
ordering the rows according to the sort specification. This row number `(RN)`
is computed according to the formula `RN = (1+ (P*(N-1))`. The final result
of the aggregate function is computed by linear interpolation between the values from
rows at row numbers `CRN = CEILING(RN)` and `FRN = FLOOR(RN)`.

The final result will be as follows.

If `(CRN = FRN = RN)` then the result is `(value of expression from
 row at RN)`

Otherwise the result is as follows:

`(CRN - RN) * (value of expression for row at FRN) + (RN - FRN) * (value of
 expression for row at CRN)`.

## Syntax

```
PERCENTILE_CONT(*percentile*)
WITHIN GROUP(ORDER BY *expr*)
```

## Arguments

_percentile_

Numeric constant between 0 and 1. `NULL` values are ignored in the
calculation.

_expr_

Specifies numeric or date/time values to sort and compute the percentile
over.

## Returns

The return type is determined by the data type of the ORDER BY expression in the
WITHIN GROUP clause. The following table shows the return type for each ORDER BY
expression data type.

| Input type                                   | Return type   |
| -------------------------------------------- | ------------- |
| `INT2`, `INT4`, `INT8`, `NUMERIC`, `DECIMAL` | `DECIMAL`     |
| `FLOAT`, `DOUBLE`                            | `DOUBLE`      |
| `DATE`                                       | `DATE`        |
| `TIMESTAMP`                                  | `TIMESTAMP`   |
| `TIMESTAMPTZ`                                | `TIMESTAMPTZ` |

## Usage notes

If the ORDER BY expression is a DECIMAL data type defined with the maximum
precision of 38 digits, it is possible that PERCENTILE_CONT will return either an
inaccurate result or an error. If the return value of the PERCENTILE_CONT function
exceeds 38 digits, the result is truncated to fit, which causes a loss of precision..
If, during interpolation, an intermediate result exceeds the maximum precision, a
numeric overflow occurs and the function returns an error. To avoid these conditions,
we recommend either using a data type with lower precision or casting the ORDER BY
expression to a lower precision.

If a statement includes multiple calls to sort-based aggregate functions (LISTAGG,
PERCENTILE_CONT, or MEDIAN), they must all use the same ORDER BY values. Note that
MEDIAN applies an implicit order by on the expression value.

For example, the following statement returns an error.

```
`SELECT TOP 10 salesid, SUM(pricepaid),
PERCENTILE_CONT(0.6) WITHIN GROUP(ORDER BY salesid),
MEDIAN(pricepaid)
FROM sales
GROUP BY salesid, pricepaid;`

`An error occurred when executing the SQL command:
SELECT TOP 10 salesid, SUM(pricepaid),
PERCENTILE_CONT(0.6) WITHIN GROUP(ORDER BY salesid),
MEDIAN(pricepaid)
FROM sales
GROUP BY salesid, pricepaid;

ERROR: within group ORDER BY clauses for aggregate functions must be the same`
```

The following statement runs successfully.

```
`SELECT TOP 10 salesid, SUM(pricepaid),
PERCENTILE_CONT(0.6) WITHIN GROUP(ORDER BY salesid),
MEDIAN(salesid)
FROM sales
GROUP BY salesid, pricepaid;`
```

## Examples

The following examples use the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

The following example shows that PERCENTILE_CONT(0.5) produces the same results as MEDIAN.

```
`SELECT TOP 10 DISTINCT sellerid, qtysold,
PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER BY qtysold),
MEDIAN(qtysold)
FROM sales
GROUP BY sellerid, qtysold;`

`+----------+---------+-----------------+--------+
| sellerid | qtysold | percentile_cont | median |
+----------+---------+-----------------+--------+
| 2 | 2 | 2 | 2 |
| 26 | 1 | 1 | 1 |
| 33 | 1 | 1 | 1 |
| 38 | 1 | 1 | 1 |
| 43 | 1 | 1 | 1 |
| 48 | 2 | 2 | 2 |
| 48 | 3 | 3 | 3 |
| 77 | 4 | 4 | 4 |
| 85 | 4 | 4 | 4 |
| 95 | 2 | 2 | 2 |
+----------+---------+-----------------+--------+`
```

The following example finds PERCENTILE_CONT(0.5) and PERCENTILE_CONT(0.75) for the quantity sold for each sellerid in the SALES table.

```
`SELECT sellerid,
PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER BY qtysold) as pct_50,
PERCENTILE_CONT(0.75) WITHIN GROUP(ORDER BY qtysold) as pct_75
FROM sales
GROUP BY sellerid
ORDER BY sellerid
LIMIT 10;`

`+----------+--------+---------+
| sellerid | pct_50 | pct_75 |
+----------+--------+---------+
| 1 | 1.5 | 1.75 |
| 2 | 2 | 2.25 |
| 3 | 2 | 3 |
| 4 | 2 | 2 |
| 5 | 1 | 1.5 |
| 6 | 1 | 1 |
| 7 | 1.5 | 1.75 |
| 8 | 1 | 1 |
| 9 | 4 | 4 |
| 12 | 2 | 3.25 |
+----------+--------+---------+`
```

To verify the results of the previous query for the first sellerid, use the following example.

```
`SELECT qtysold
FROM sales
WHERE sellerid=1;`

`+---------+
| qtysold |
+---------+
| 2 |
| 1 |
+---------+`
```
