

# AVG function
<a name="avg-function"></a>

The AVG function returns the average (arithmetic mean) of the input expression values. The AVG function works with numeric values and ignores NULL values.

## Syntax
<a name="avg-function-syntax"></a>

```
AVG ({{column}})
```

## Arguments
<a name="avg-function-arguments"></a>

{{column}}  
The target column that the function operates on. The column is one of the following data types:  
+ SMALLINT
+ INTEGER
+ BIGINT
+ DECIMAL
+ DOUBLE
+ FLOAT

## Data types
<a name="avg-function-data-types"></a>

The argument types supported by the AVG function are SMALLINT, INTEGER, BIGINT, DECIMAL, and DOUBLE.

The return types supported by the AVG function are:
+ BIGINT for any integer type argument
+ DOUBLE for a floating point argument
+ Returns the same data type as expression for any other argument type

The default precision for an AVG function result with a DECIMAL argument is 38. The scale of the result is the same as the scale of the argument. For example, an AVG of a DEC(5,2) column returns a DEC(38,2) data type.

## Example
<a name="avg-function-example"></a>

Find the average quantity sold per transaction from the SALES table.

```
select avg(qtysold) from sales;
```