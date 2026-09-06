

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# FLOOR function
<a name="r_FLOOR"></a>

The FLOOR function rounds a number down to the next whole number. 

## Syntax
<a name="r_FLOOR-synopsis"></a>

```
FLOOR(number)
```

## Argument
<a name="r_FLOOR-argument"></a>

 *number*   
The number or expression that evaluates to a number. It can be the `SMALLINT`, `INTEGER`, `BIGINT`, `DECIMAL`, `FLOAT4`, `FLOAT8`, or `SUPER` type. 

## Return type
<a name="r_FLOOR-return-type"></a>

FLOOR returns the same data type as its argument. 

When the input is of the `SUPER` type, the output retains the same dynamic type as the input while the static type remains the `SUPER` type. When the dynamic type of `SUPER` isn't a number, Amazon Redshift returns `NULL`.

## Examples
<a name="r_FLOOR-example"></a>

The following examples use the TICKIT sample database. For more information, see [Sample database](c_sampledb.md).

To show the value of the commission paid for a given sales transaction before and after using the FLOOR function, use the following example. 

```
SELECT commission 
FROM sales 
WHERE salesid=10000;

+------------+
| commission |
+------------+
|      28.05 |
+------------+

SELECT FLOOR(commission) 
FROM sales 
WHERE salesid=10000;

+-------+
| floor |
+-------+
|    28 |
+-------+
```