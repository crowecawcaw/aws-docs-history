Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# MAX function

The MAX function returns the maximum value in a set of rows. DISTINCT or ALL might be
used but do not affect the result.

## Syntax

```
MAX ( [ DISTINCT | ALL ] *expression* )
```

## Arguments

_expression_

The target column or expression that the function operates on. The _expression_ is one of the following data types:

- SMALLINT
- INTEGER
- BIGINT
- DECIMAL
- REAL
- DOUBLE PRECISON
- CHAR
- VARCHAR
- DATE
- TIMESTAMP
- TIMESTAMPTZ
- TIME
- TIMETZ
- VARBYTE
- SUPER

DISTINCT | ALL

With the argument DISTINCT, the function eliminates all duplicate values
from the specified expression before calculating the maximum. With the
argument ALL, the function retains all duplicate values from the expression
for calculating the maximum. ALL is the default.

## Data types

Returns the same data type as
_expression_. The Boolean equivalent of the MIN function is the
[BOOL\_AND function](r_BOOL_AND.md "r_BOOL_AND.md"), and the Boolean
equivalent of MAX is the [BOOL\_OR function](r_BOOL_OR.md "r_BOOL_OR.md").

## Examples

Find the highest price paid from all sales:

```
select max(pricepaid) from sales;

max
----------
12624.00
(1 row)
```

Find the highest price paid per ticket from all sales:

```
select max(pricepaid/qtysold) as max_ticket_price
from sales;

max_ticket_price
-----------------
2500.00000000
(1 row)
```
