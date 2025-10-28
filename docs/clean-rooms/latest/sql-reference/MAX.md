# MAX function

The MAX function returns the maximum value in a set of rows. DISTINCT or ALL might be used
but do not affect the result.

## Syntax

```
MAX ( [ DISTINCT | ALL ] *expression* )
```

## Arguments

_expression_

The target column or expression that the function operates on. The
_expression_ is any numerical data type.

DISTINCT | ALL

With the argument DISTINCT, the function eliminates all duplicate values from the
specified expression before calculating the maximum. With the argument ALL, the function
retains all duplicate values from the expression for calculating the maximum. ALL is the
default.

## Data types

Returns the same data type as
_expression_.

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
