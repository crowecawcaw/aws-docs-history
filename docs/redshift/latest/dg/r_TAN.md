

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# TAN function
<a name="r_TAN"></a>

TAN is a trigonometric function that returns the tangent of a number. The input argument is a number (in radians). 

## Syntax
<a name="r_TAN-synopsis"></a>

```
TAN(number)
```

## Argument
<a name="r_TAN-argument"></a>

 *number*   
A `DOUBLE PRECISION` number. 

## Return type
<a name="r_TAN-return-type"></a>

`DOUBLE PRECISION`

## Examples
<a name="r_TAN-examples"></a>

To return the tangent of zero, use the following example. 

```
SELECT TAN(0);

+-----+
| tan |
+-----+
|   0 |
+-----+
```