

# DEGREES function
<a name="DEGREES"></a>

Converts an angle in radians to its equivalent in degrees. 

## Syntax
<a name="DEGREES-synopsis"></a>

```
DEGREES(number)
```

## Argument
<a name="DEGREES-argument"></a>

 *number*   
The input parameter is a `DOUBLE PRECISION` number. 

## Return type
<a name="DEGREES-return-type"></a>

`DOUBLE PRECISION`

## Example
<a name="DEGREES-examples"></a>

To return the degree equivalent of .5 radians, use the following example. 

```
SELECT DEGREES(.5);

+-------------------+
|      degrees      |
+-------------------+
| 28.64788975654116 |
+-------------------+
```

To convert PI radians to degrees, use the following example. 

```
SELECT DEGREES(pi());

+---------+
| degrees |
+---------+
|     180 |
+---------+
```