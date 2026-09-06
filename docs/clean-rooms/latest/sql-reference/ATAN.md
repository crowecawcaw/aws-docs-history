

# ATAN function
<a name="ATAN"></a>

ATAN is a trigonometric function that returns the arc tangent of a number. The return value is in radians and is between `-PI` and `PI`.

## Syntax
<a name="ATAN-synopsis"></a>

```
ATAN(number)
```

## Arguments
<a name="ATAN-argument"></a>

 *number*   
The input parameter is a `DOUBLE PRECISION` number. 

## Return type
<a name="ATAN-return-type"></a>

`DOUBLE PRECISION`

## Examples
<a name="ATAN-examples"></a>

To return the arc tangent of `1` and multiply it by 4, use the following example.

```
SELECT ATAN(1) * 4 AS pi;
            
+-------------------+
|        pi         |
+-------------------+
| 3.141592653589793 |
+-------------------+
```