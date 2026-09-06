

# MAX function
<a name="MAX"></a>

 The MAX function returns the maximum value in a set of rows. DISTINCT or ALL might be used but do not affect the result. 

## Syntax
<a name="MAX-synopsis"></a>

```
MAX ( [ DISTINCT | ALL ] expression )
```

## Arguments
<a name="MAX-arguments"></a>

 *expression *   
The target column or expression that the function operates on. The *expression* is any numerical data type.

DISTINCT \| ALL   
With the argument DISTINCT, the function eliminates all duplicate values from the specified expression before calculating the maximum. With the argument ALL, the function retains all duplicate values from the expression for calculating the maximum. ALL is the default. 

## Data types
<a name="Supported_data_types_max"></a>

Returns the same data type as *expression*. 

## Examples
<a name="MAX-examples"></a>

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