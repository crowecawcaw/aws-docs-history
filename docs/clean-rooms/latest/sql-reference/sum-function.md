# SUM and SUM DISTINCT

functions

The SUM function returns the sum of the input column or expression values.
The SUM function works with numeric values and ignores NULL values.

The SUM DISTINCT function eliminates all duplicate values from the specified
expression before calculating the sum.

## Syntax

```
SUM (DISTINCT `column` )
```

## Arguments

`column`

The target column that the function operates on. The column is any numeric data
types.

## Examples

Find the sum of all commissions paid from the SALES table.

```
select sum(commission) from sales
```

Find the sum of all distinct commissions paid from the SALES table.

```
select sum (distinct (commission)) from sales
```
