

# MIN function
<a name="MIN"></a>

 The MIN function returns the minimum value in a set of rows. DISTINCT or ALL might be used but do not affect the result.

## Syntax
<a name="MIN-synopsis"></a>

```
MIN ( [ DISTINCT | ALL ] expression )
```

## Arguments
<a name="MIN-arguments"></a>

 *expression *   
The target column or expression that the function operates on. The *expression* is any numerical data type.

DISTINCT \| ALL  
With the argument DISTINCT, the function eliminates all duplicate values from the specified expression before calculating the minimum. With the argument ALL, the function retains all duplicate values from the expression for calculating the minimum. ALL is the default.

## Data types
<a name="Supported_data_types_min"></a>

 Returns the same data type as *expression*. 

## Examples
<a name="MIN-examples"></a>

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