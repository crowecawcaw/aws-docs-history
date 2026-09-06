

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# CBRT function
<a name="r_CBRT"></a>

 The CBRT function is a mathematical function that calculates the cube root of a given number. 

## Syntax
<a name="r_CBRT-synopsis"></a>

```
CBRT(number)
```

## Arguments
<a name="r_CBRT-argument"></a>

CBRT takes a `DOUBLE PRECISION` number as an argument. 

## Return type
<a name="r_CBRT-return-type"></a>

`DOUBLE PRECISION` 

## Examples
<a name="r_CBRT-examples"></a>

The following example uses the TICKIT sample database. For more information, see [Sample database](c_sampledb.md).

To calculate the cube root of the commission paid for a given transaction, use the following example. 

```
SELECT CBRT(commission) FROM sales WHERE salesid=10000;

+--------------------+
|        cbrt        |
+--------------------+
| 3.0383953904884344 |
+--------------------+
```