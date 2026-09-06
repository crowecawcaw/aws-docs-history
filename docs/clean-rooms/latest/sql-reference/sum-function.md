

# SUM and SUM DISTINCT functions
<a name="sum-function"></a>

The SUM function returns the sum of the input column or expression values. The SUM function works with numeric values and ignores NULL values. 

The SUM DISTINCT function eliminates all duplicate values from the specified expression before calculating the sum.

## Syntax
<a name="sum-function-syntax"></a>

```
SUM (DISTINCT {{column}} )
```

## Arguments
<a name="sum-function-arguments"></a>

{{column}}  
The target column that the function operates on. The column is any numeric data types.

## Examples
<a name="sum-function-examples"></a>

Find the sum of all commissions paid from the SALES table.

```
select sum(commission) from sales
```

Find the sum of all distinct commissions paid from the SALES table.

```
select sum (distinct (commission)) from sales
```