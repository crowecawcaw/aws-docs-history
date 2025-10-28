# MIN function

The MIN function returns the minimum value in a set of rows. DISTINCT or ALL might be used
but do not affect the result.

## Syntax

```
MIN ( [ DISTINCT | ALL ] *expression* )
```

## Arguments

_expression_

The target column or expression that the function operates on. The
_expression_ is any numerical data type.

DISTINCT | ALL

With the argument DISTINCT, the function eliminates all duplicate values from the
specified expression before calculating the minimum. With the argument ALL, the function
retains all duplicate values from the expression for calculating the minimum. ALL is the
default.

## Data types

Returns the same data type as
_expression_.

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
