

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# PI function
<a name="r_PI"></a>

The PI function returns the value of pi to 14 decimal places. 

## Syntax
<a name="r_PI-synopsis"></a>

```
PI()
```

## Return type
<a name="r_PI-return-type"></a>

`DOUBLE PRECISION`

## Examples
<a name="r_PI-examples"></a>

To return the value of pi, use the following example.

```
SELECT PI();

+-------------------+
|        pi         |
+-------------------+
| 3.141592653589793 |
+-------------------+
```