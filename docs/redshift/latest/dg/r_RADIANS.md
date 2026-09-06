

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# RADIANS function
<a name="r_RADIANS"></a>

The RADIANS function converts an angle in degrees to its equivalent in radians. 

## Syntax
<a name="r_RADIANS-synopsis"></a>

```
RADIANS(number)
```

## Argument
<a name="r_RADIANS-argument"></a>

 *number*   
The input parameter is a `DOUBLE PRECISION` number. 

## Return type
<a name="r_RADIANS-return-type"></a>

`DOUBLE PRECISION`

## Examples
<a name="r_RADIANS-examples"></a>

To return the radian equivalent of 180 degrees, use the following example. 

```
SELECT RADIANS(180);

+-------------------+
|      radians      |
+-------------------+
| 3.141592653589793 |
+-------------------+
```