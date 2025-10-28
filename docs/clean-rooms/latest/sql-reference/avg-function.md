# AVG function

The AVG function returns the average (arithmetic mean) of the input
expression values. The AVG function works with numeric values and ignores NULL
values.

## Syntax

```
AVG (`column`)
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
- FLOAT

## Data types

The argument types supported by the AVG function are
SMALLINT, INTEGER, BIGINT, DECIMAL,
and DOUBLE.

The return types supported by the AVG function are:

- BIGINT for any integer type argument
- DOUBLE for a floating point argument
- Returns the same data type as expression for any other argument type

The default precision for an AVG function result with a
DECIMAL argument is 38. The scale of the result is the same as the scale of the
argument. For example, an AVG of a DEC(5,2) column returns a
DEC(38,2) data type.

## Example

Find the average quantity sold per transaction from the SALES table.

```
select avg(qtysold) from sales;
```
