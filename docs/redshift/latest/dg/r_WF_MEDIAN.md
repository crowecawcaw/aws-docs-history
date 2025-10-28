Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# MEDIAN window function

Calculates the median value for the range of values in a window or partition. NULL
values in the range are ignored.

MEDIAN is an inverse distribution function that assumes a continuous distribution
model.

## Syntax

```
MEDIAN ( *median\_expression* )
OVER ( [ PARTITION BY *partition\_expression* ] )
```

## Arguments

_median_expression_

An expression, such as a column name, that provides the values for which
to determine the median. The expression must have either a numeric or
datetime data type or be implicitly convertible to one.

OVER

A clause that specifies the window partitioning. The OVER clause cannot
contain a window ordering or window frame specification.

PARTITION BY _partition_expression_

Optional. An expression that sets the range of records for each group in
the OVER clause.

## Data types

The return type is determined by the data type of
_median_expression_. The following table shows the return type
for each _median_expression_ data type.

| Input Type                         | Return Type |
| ---------------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| INT2, INT4, INT8, NUMERIC, DECIMAL | DECIMAL     |
| FLOAT, DOUBLE                      | DOUBLE      |
| DATE                               | DATE        | ## Usage notes If the _median_expression_ argument is a DECIMAL data type defined with the maximum precision of 38 digits, it is possible that MEDIAN will return either an inaccurate result or an error. If the return value of the MEDIAN function exceeds 38 digits, the result is truncated to fit, which causes a loss of precision. If, during interpolation, an intermediate result exceeds the maximum precision, a numeric overflow occurs and the function returns an error. To avoid these conditions, we recommend either using a data type with lower precision or casting the _median_expression_ argument to a lower precision. For example, a SUM function with a DECIMAL argument returns a default precision of 38 digits. The scale of the result is the same as the scale of the argument. So, for example, a SUM of a DECIMAL(5,2) column returns a DECIMAL(38,2) data type. The following example uses a SUM function in the _median_expression_ argument of a MEDIAN function. The data type of the PRICEPAID column is DECIMAL (8,2), so the SUM function returns DECIMAL(38,2). `select salesid, sum(pricepaid), median(sum(pricepaid)) over() from sales where salesid < 10 group by salesid;` To avoid a potential loss of precision or an overflow error, cast the result to a DECIMAL data type with lower precision, as the following example shows. `select salesid, sum(pricepaid), median(sum(pricepaid)::decimal(30,2)) over() from sales where salesid < 10 group by salesid;` ## Examples The following example calculates the median sales quantity for each seller: `select sellerid, qty, median(qty) over (partition by sellerid) from winsales order by sellerid; sellerid	qty	median --------------------------- 1		10	10.0 1		10	10.0 1		30	10.0 2		20	20.0 2		20	20.0 3		10	17.5 3		15	17.5 3		20	17.5 3		30	17.5 4		10	25.0 4		40	25.0` For a description of the WINSALES table, see [Sample table for window function examples](c_Window_functions.md#r_Window_function_example "c_Window_functions.md#r_Window_function_example"). |
