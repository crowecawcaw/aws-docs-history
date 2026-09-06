

# POWER function
<a name="POWER"></a>

 The POWER function is an exponential function that raises a numeric expression to the power of a second numeric expression. For example, 2 to the third power is calculated as `POWER(2,3)`, with a result of `8`. 

## Syntax
<a name="POWER-synopsis"></a>

```
{POWER(expression1, expression2)
```

## Arguments
<a name="POWER-arguments"></a>

 *expression1*   
Numeric expression to be raised. Must be an `INTEGER`, `DECIMAL`, or `FLOAT` data type. 

 *expression2*   
Power to raise *expression1*. Must be an `INTEGER`, `DECIMAL`, or `FLOAT` data type. 

## Return type
<a name="POWER-return-type"></a>

`DOUBLE PRECISION`

## Example
<a name="POWER-examples"></a>

```
SELECT (SELECT SUM(qtysold) FROM sales, date
WHERE sales.dateid=date.dateid
AND year=2008) * POW((1+7::FLOAT/100),10) qty2010;

+-------------------+
|      qty2010      |
+-------------------+
| 679353.7540885945 |
+-------------------+
```