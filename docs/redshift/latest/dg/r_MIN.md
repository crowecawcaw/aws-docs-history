Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# MIN function

The MIN function returns the minimum value in a set of rows. DISTINCT or ALL might be
used but do not affect the result.

## Syntax

```
MIN ( [ DISTINCT | ALL ] *expression* )
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
from the specified expression before calculating the minimum. With the
argument ALL, the function retains all duplicate values from the expression
for calculating the minimum. ALL is the default.

## Data types

Returns the same data type as
_expression_. The Boolean equivalent of the MIN function is
[BOOL\_AND function](r_BOOL_AND.md "r_BOOL_AND.md"), and the Boolean
equivalent of MAX is [BOOL\_OR function](r_BOOL_OR.md "r_BOOL_OR.md").

## Examples

Find the lowest price paid from all sales:

```
select min(pricepaid) from sales;

min
-------
20.00
(1 row)
```

Find the lowest price paid per ticket from all sales:

```
select min(pricepaid/qtysold)as min_ticket_price
from sales;

min_ticket_price
------------------
20.00000000
(1 row)
```
