Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SUM function

The SUM function returns the sum of the input column or expression values. The SUM
function works with numeric values and ignores NULL values.

## Syntax

```
SUM ( [ DISTINCT | ALL ] *expression* )
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
from the specified expression before calculating the sum. With the argument
ALL, the function retains all duplicate values from the expression for
calculating the sum. ALL is the default.

## Data types

The argument types supported by the SUM function are SMALLINT, INTEGER, BIGINT,
NUMERIC, DECIMAL, REAL, DOUBLE PRECISION, and SUPER.

The return types supported by the SUM function are

- BIGINT for BIGINT, SMALLINT, and INTEGER arguments
- NUMERIC for NUMERIC arguments
- DOUBLE PRECISION for floating point arguments
- Returns the same data type as expression for any other argument type.

The default precision for a SUM function result with a NUMERIC or DECIMAL argument is 38. The scale of the result is the same as the scale of the argument. For example, a SUM of a DEC(5,2) column returns a DEC(38,2) data type.

## Examples

Find the sum of all commissions paid from the SALES table:

```
select sum(commission) from sales;

sum
-------------
16614814.65
(1 row)
```

Find the number of seats in all venues in the state of Florida:

```
select sum(venueseats) from venue
where venuestate = 'FL';

sum
--------
250411
(1 row)
```

Find the number of seats sold in May:

```
select sum(qtysold) from sales, date
where sales.dateid = date.dateid and date.month = 'MAY';

sum
-------
32291
(1 row)
```
