

# RADIANS function
<a name="RADIANS"></a>

The RADIANS function converts an angle in degrees to its equivalent in radians. 

## Syntax
<a name="RADIANS-synopsis"></a>

```
RADIANS(number)
```

## Argument
<a name="RADIANS-argument"></a>

 *number*   
The input parameter is a `DOUBLE PRECISION` number. 

## Return type
<a name="RADIANS-return-type"></a>

`DOUBLE PRECISION`

## Example
<a name="RADIANS-examples"></a>

To return the radian equivalent of 180 degrees, use the following example. 

```
SELECT RADIANS(180);

+-------------------+
|      radians      |
+-------------------+
| 3.141592653589793 |
+-------------------+
```