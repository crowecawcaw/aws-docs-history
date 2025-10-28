# SUM and SUM DISTINCT

functions

The SUM function returns the sum of the input column or expression values.
The SUM function works with numeric values and ignores NULL values.

The SUM DISTINCT function eliminates all duplicate values from the specified
expression before calculating the sum.

## Syntax

```
SUM (`column`)
```

```
SUM (DISTINCT `column` )
```

## Arguments

`column`

The target column that the function operates on. The column is one of the following data
types:

- SMALLINT
- INTEGER
- BIGINT
- DECIMAL
- DOUBLE

## Data types

The argument types supported by the SUM function are
SMALLINT, INTEGER, BIGINT, DECIMAL,
and DOUBLE.

The SUM function supports the following return types:

- BIGINT for BIGINT, SMALLINT, and
  INTEGER arguments
- DOUBLE for floating point arguments
- Returns the same data type as expression for any other argument type

The default precision for a SUM function result with a
DECIMAL argument is 38. The scale of the result is the same as the scale of the
argument. For example, a SUM of a DEC(5,2) column returns a
DEC(38,2) data type.

## Examples

Find the sum of all commissions paid from the SALES table.

```
select sum(commission) from sales
```

Find the sum of all distinct commissions paid from the SALES table.

```
select sum (distinct (commission)) from sales
```
