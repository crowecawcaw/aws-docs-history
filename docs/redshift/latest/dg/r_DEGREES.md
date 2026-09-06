

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# DEGREES function
<a name="r_DEGREES"></a>

Converts an angle in radians to its equivalent in degrees. 

## Syntax
<a name="r_DEGREES-synopsis"></a>

```
DEGREES(number)
```

## Argument
<a name="r_DEGREES-argument"></a>

 *number*   
The input parameter is a `DOUBLE PRECISION` number. 

## Return type
<a name="r_DEGREES-return-type"></a>

`DOUBLE PRECISION`

## Examples
<a name="r_DEGREES-examples"></a>

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