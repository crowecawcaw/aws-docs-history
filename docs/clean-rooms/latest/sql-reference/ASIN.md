

# ASIN function
<a name="ASIN"></a>

ASIN is a trigonometric function that returns the arc sine of a number. The return value is in radians and is between `PI/2` and `-PI/2`. 

## Syntax
<a name="ASIN-synopsis"></a>

```
ASIN(number)
```

## Arguments
<a name="ASIN-argument"></a>

 *number*   
The input parameter is a `DOUBLE PRECISION` number. 

## Return type
<a name="ASIN-return-type"></a>

`DOUBLE PRECISION`

## Examples
<a name="ASIN-examples"></a>

To return the arc sine of `1`, use the following example. 

```
SELECT ASIN(1) AS halfpi;

+--------------------+
|       halfpi       |
+--------------------+
| 1.5707963267948966 |
+--------------------+
```