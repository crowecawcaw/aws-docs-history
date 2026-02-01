Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# RATIO_TO_REPORT window function

Calculates the ratio of a value to the sum of the values in a window or partition.
The ratio to report value is determined using the formula:

`value of` _ratio_expression_
`argument for the current row / sum of`
_ratio_expression_
`argument for the window or partition`

The following dataset illustrates use of this formula:

```
Row#	Value	Calculation	RATIO_TO_REPORT
1	2500	(2500)/(13900)	0.1798
2	2600	(2600)/(13900)	0.1870
3	2800	(2800)/(13900)	0.2014
4	2900	(2900)/(13900)	0.2086
5	3100	(3100)/(13900)	0.2230
```

The return value range is 0 to 1, inclusive. If _ratio_expression_
is NULL, then the return value is `NULL`. If a value in _partition_expression_ is unique, then function will return `1` for that value.

## Syntax

```
RATIO_TO_REPORT ( *ratio\_expression* )
OVER ( [ PARTITION BY *partition\_expression* ] )
```

## Arguments

_ratio_expression_

An expression, such as a column name, that provides the value for which
to determine the ratio. The expression must have either a numeric data type
or be implicitly convertible to one.

You cannot use any other analytic function in
_ratio_expression_.

OVER

A clause that specifies the window partitioning. The OVER clause cannot
contain a window ordering or window frame specification.

PARTITION BY _partition_expression_

Optional. An expression that sets the range of records for each group in
the OVER clause.

## Return type

FLOAT8

## Examples

The following examples use the WINSALES table. For a information about how to create the WINSALES table, see [Sample table for window function examples](c_Window_functions.md#r_Window_function_example "c_Window_functions.md#r_Window_function_example").

The following example calculates the ratio-to-report value of each row of a seller's quantity to the total of all seller's quantities.

```
`select sellerid, qty, ratio_to_report(qty)
over()
from winsales
order by sellerid;`
`sellerid qty ratio_to_report
--------------------------------------
1 30 0.13953488372093023
1 10 0.046511627906976744
1 10 0.046511627906976744
2 20 0.09302325581395349
2 20 0.09302325581395349
3 30 0.13953488372093023
3 20 0.09302325581395349
3 15 0.06976744186046512
3 10 0.046511627906976744
4 10 0.046511627906976744
4 40 0.18604651162790697`
```

The following example calculates the ratios of the sales quantities for each seller by partition.

```
`select sellerid, qty, ratio_to_report(qty)
over(partition by sellerid)
from winsales;`
`sellerid qty ratio_to_report
-------------------------------------------
2 20 0.5
2 20 0.5
4 40 0.8
4 10 0.2
1 10 0.2
1 30 0.6
1 10 0.2
3 10 0.13333333333333333
3 15 0.2
3 20 0.26666666666666666
3 30 0.4`
```
