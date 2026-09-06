

# ACOS function
<a name="ACOS"></a>

ACOS is a trigonometric function that returns the arc cosine of a number. The return value is in radians and is between `0` and `PI`.

## Syntax
<a name="ACOS-synopsis"></a>

```
ACOS(number)
```

## Arguments
<a name="ACOS-arguments"></a>

 *number*   
The input parameter is a `DOUBLE PRECISION` number. 

## Return type
<a name="ACOS-return-type"></a>

`DOUBLE PRECISION`

## Examples
<a name="ACOS-examples"></a>

To return the arc cosine of `-1`, use the following example. 

```
SELECT ACOS(-1);

+-------------------+
|       acos        |
+-------------------+
| 3.141592653589793 |
+-------------------+
```