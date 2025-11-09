Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PERCENTILE_DISC window function

PERCENTILE_DISC is an inverse distribution function that assumes a discrete
distribution model. It takes a percentile value and a sort specification and returns an
element from the given set.

For a given percentile value P, PERCENTILE_DISC sorts the values of the expression in
the ORDER BY clause and returns the value with the smallest cumulative distribution
value (with respect to the same sort specification) that is greater than or equal to P.

You can specify only the PARTITION clause in the OVER clause.

## Syntax

```
PERCENTILE_DISC ( *percentile* )
WITHIN GROUP (ORDER BY *expr*)
OVER (  [ PARTITION BY *expr\_list* ]  )

```

## Arguments

_percentile_

Numeric constant between 0 and 1. Nulls are ignored in the
calculation.

WITHIN GROUP ( ORDER BY _expr_)

Specifies numeric or date/time values to sort and compute the percentile
over.

OVER

Specifies the window partitioning. The OVER clause cannot contain a
window ordering or window frame specification.

PARTITION BY _expr_

Optional argument that sets the range of records for each group in the
OVER clause.

## Returns

The same data type as the ORDER BY expression in the WITHIN GROUP clause.

## Examples

The following examples use the WINSALES table. For a description of the WINSALES
table, see [Sample table for window function examples](c_Window_functions.md#r_Window_function_example "c_Window_functions.md#r_Window_function_example").

```
`SELECT sellerid, qty, PERCENTILE_DISC(0.5)
WITHIN GROUP (ORDER BY qty)
OVER() AS MEDIAN FROM winsales;`

`+----------+-----+--------+
| sellerid | qty | median |
+----------+-----+--------+
| 3 | 10 | 20 |
| 1 | 10 | 20 |
| 1 | 10 | 20 |
| 4 | 10 | 20 |
| 3 | 15 | 20 |
| 2 | 20 | 20 |
| 2 | 20 | 20 |
| 3 | 20 | 20 |
| 1 | 30 | 20 |
| 3 | 30 | 20 |
| 4 | 40 | 20 |
+----------+-----+--------+`

`SELECT sellerid, qty, PERCENTILE_DISC(0.5)
WITHIN GROUP (ORDER BY qty)
OVER(PARTITION BY sellerid) AS MEDIAN FROM winsales;`

`+----------+-----+--------+
| sellerid | qty | median |
+----------+-----+--------+
| 4 | 10 | 10 |
| 4 | 40 | 10 |
| 3 | 10 | 15 |
| 3 | 15 | 15 |
| 3 | 20 | 15 |
| 3 | 30 | 15 |
| 2 | 20 | 20 |
| 2 | 20 | 20 |
| 1 | 10 | 10 |
| 1 | 10 | 10 |
| 1 | 30 | 10 |
+----------+-----+--------+`
```

To find PERCENTILE_DISC(0.25) and PERCENTILE_DISC(0.75) for the quantity when partitioned by the seller ID, use the following examples.

```
`SELECT sellerid, qty, PERCENTILE_DISC(0.25)
WITHIN GROUP (ORDER BY qty)
OVER(PARTITION BY sellerid) AS quartile1 FROM winsales;`

`+----------+-----+-----------+
| sellerid | qty | quartile1 |
+----------+-----+-----------+
| 4 | 10 | 10 |
| 4 | 40 | 10 |
| 2 | 20 | 20 |
| 2 | 20 | 20 |
| 3 | 10 | 10 |
| 3 | 15 | 10 |
| 3 | 20 | 10 |
| 3 | 30 | 10 |
| 1 | 10 | 10 |
| 1 | 10 | 10 |
| 1 | 30 | 10 |
+----------+-----+-----------+`

`SELECT sellerid, qty, PERCENTILE_DISC(0.75)
WITHIN GROUP (ORDER BY qty)
OVER(PARTITION BY sellerid) AS quartile3 FROM winsales;`

`+----------+-----+-----------+
| sellerid | qty | quartile3 |
+----------+-----+-----------+
| 3 | 10 | 20 |
| 3 | 15 | 20 |
| 3 | 20 | 20 |
| 3 | 30 | 20 |
| 4 | 10 | 40 |
| 4 | 40 | 40 |
| 2 | 20 | 20 |
| 2 | 20 | 20 |
| 1 | 10 | 30 |
| 1 | 10 | 30 |
| 1 | 30 | 30 |
+----------+-----+-----------+`
```
