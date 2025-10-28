Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# AVG function

The AVG function returns the average (arithmetic mean) of the input expression
values. The AVG function works with numeric values and ignores NULL values.

## Syntax

```
AVG ( [ DISTINCT | ALL ] *expression* )
```

## Arguments

_expression_

The target column or expression that the function operates on. The _expression_ is one of the following data types:

- SMALLINT
- INTEGER
- BIGINT
- NUMERIC
- DECIMAL
- REAL
- DOUBLE PRECISON
- SUPER

DISTINCT | ALL

With the argument DISTINCT, the function eliminates all duplicate values
from the specified expression before calculating the average. With the
argument ALL, the function retains all duplicate values from the expression
for calculating the average. ALL is the default.

## Data types

The argument types supported by the AVG function are SMALLINT, INTEGER, BIGINT,
NUMERIC, DECIMAL, REAL, DOUBLE PRECISION, and SUPER.

The return types supported by the AVG function are:

- BIGINT for any integer type argument
- DOUBLE PRECISION for a floating point argument
- Returns the same data type as expression for any other argument type.

The default precision for an AVG function result with a NUMERIC or DECIMAL argument is 38. The scale of the result is the same as the scale of the argument. For example, an AVG of a DEC(5,2) column returns a DEC(38,2) data type.

## Examples

Find the average quantity sold per transaction from the SALES table:

```
select avg(qtysold)from sales;

avg
-----
2
(1 row)
```

Find the average total price listed for all listings:

```
select avg(numtickets*priceperticket) as avg_total_price from listing;

avg_total_price
-----------------
3034.41
(1 row)
```

Find the average price paid, grouped by month in descending order:

```
select avg(pricepaid) as avg_price, month
from sales, date
where sales.dateid = date.dateid
group by month
order by avg_price desc;

avg_price | month
-----------+-------
659.34 | MAR
655.06 | APR
645.82 | JAN
643.10 | MAY
642.72 | JUN
642.37 | SEP
640.72 | OCT
640.57 | DEC
635.34 | JUL
635.24 | FEB
634.24 | NOV
632.78 | AUG
(12 rows)
```
