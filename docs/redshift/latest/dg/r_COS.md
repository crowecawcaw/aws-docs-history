

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# COS function
<a name="r_COS"></a>

COS is a trigonometric function that returns the cosine of a number. The return value is in radians and is between `-1` and `1`, inclusive. 

## Syntax
<a name="r_COS-synopsis"></a>

```
COS(double_precision)
```

## Arguments
<a name="r_COS-argument"></a>

 *number*   
The input parameter is a `DOUBLE PRECISION` number. 

## Return type
<a name="r_COS-return-type"></a>

The COS function returns a `DOUBLE PRECISION` number. 

## Examples
<a name="r_COS-examples"></a>

To return the cosine of `0`, use the following example. 

```
SELECT COS(0);

+-----+
| cos |
+-----+
|   1 |
+-----+
```

To return the cosine of `pi`, use the following example. 

```
SELECT COS(PI());

+-----+
| cos |
+-----+
|  -1 |
+-----+
```