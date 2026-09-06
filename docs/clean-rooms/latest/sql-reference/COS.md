

# COS function
<a name="COS"></a>

COS is a trigonometric function that returns the cosine of a number. The return value is in radians and is between `-1` and `1`, inclusive. 

## Syntax
<a name="COS-synopsis"></a>

```
COS(double_precision)
```

## Argument
<a name="COS-argument"></a>

 *number*   
The input parameter is a double precision number. 

## Return type
<a name="COS-return-type"></a>

The COS function returns a double precision number. 

## Examples
<a name="COS-examples"></a>

The following example returns cosine of 0: 

```
select cos(0);
cos
-----
1
(1 row)
```

The following example returns the cosine of PI: 

```
select cos(pi());
cos
-----
-1
(1 row)
```