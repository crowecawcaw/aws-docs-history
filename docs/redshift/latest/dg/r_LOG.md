

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# LOG function
<a name="r_LOG"></a>

Returns logarithm of a number.

If you're using this function to calculate the base 10 logarithm, you can also use [DLOG10 function](r_DLOG10.md). 

## Syntax
<a name="r_LOG-synopsis"></a>

```
LOG([base, ]argument)
```

## Parameters
<a name="r_LOG-argument"></a>

 *base*   
(Optional) The base of the logarithm function. This number must be positive and can't equal `1`. If this parameter is omitted, Amazon Redshift computes the base 10 logarithm of the *argument*.

 *argument*   
The argument of the logarithm function. This number must be positive. If the *argument* value is `1`, the function returns `0`.

## Return type
<a name="r_LOG-return-type"></a>

The LOG function returns a `DOUBLE PRECISION` number. 

## Examples
<a name="r_LOG-example"></a>

To find the base 2 logarithm of 100, use the following example. 

```
SELECT LOG(2, 100);
+-------------------+
|        log        |
+-------------------+
| 6.643856189774725 |
+-------------------+
```

To find the base 10 logarithm of 100, use the following example. Note that if you omit the base parameter, Amazon Redshift assumes a base of 10.

```
SELECT LOG(100);
            
+-----+
| log |
+-----+
|   2 |
+-----+
```