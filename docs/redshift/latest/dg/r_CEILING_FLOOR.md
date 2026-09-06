

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# CEILING (or CEIL) function
<a name="r_CEILING_FLOOR"></a>

The CEILING or CEIL function is used to round a number up to the next whole number. (The [FLOOR function](r_FLOOR.md) rounds a number down to the next whole number.) 

## Syntax
<a name="r_CEILING_FLOOR-synopsis"></a>

```
{CEIL | CEILING}(number)
```

## Arguments
<a name="r_CEILING_FLOOR-arguments"></a>

 *number*   
The number or expression that evaluates to a number. It can be the `SMALLINT`, `INTEGER`, `BIGINT`, `DECIMAL`, `FLOAT4`, `FLOAT8`, or `SUPER` type.

## Return type
<a name="r_CEILING_FLOOR-return-type"></a>

CEILING and CEIL return the same data type as its argument. 

When the input is of the `SUPER` type, the output retains the same dynamic type as the input while the static type remains the SUPER type. When the dynamic type of `SUPER` isn't a number, Amazon Redshift returns a null.

## Examples
<a name="r_CEILING_FLOOR-example"></a>

The following example uses the TICKIT sample database. For more information, see [Sample database](c_sampledb.md).

To calculate the ceiling of the commission paid for a given sales transaction, use the following example. 

```
SELECT CEILING(commission) FROM sales
WHERE salesid=10000;

+---------+
| ceiling |
+---------+
|      29 |
+---------+
```