

# SIN function
<a name="SIN"></a>

SIN is a trigonometric function that returns the sine of a number. The return value is between `-1` and `1`. 

## Syntax
<a name="SIN-synopsis"></a>

```
SIN(number)
```

## Argument
<a name="SIN-argument"></a>

 *number*   
A `DOUBLE PRECISION` number in radians. 

## Return type
<a name="SIN-return-type"></a>

`DOUBLE PRECISION` 

## Example
<a name="SIN-examples"></a>

To return the sine of `-PI`, use the following example.

```
SELECT SIN(-PI());

+-------------------------+
|           sin           |
+-------------------------+
| -0.00000000000000012246 |
+-------------------------+
```