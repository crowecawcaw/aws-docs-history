

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# TRUNC function
<a name="r_TRUNC"></a>

The TRUNC function truncates numbers to the previous integer or decimal. 

The TRUNC function can optionally include a second argument as an `INTEGER` to indicate the number of decimal places for rounding, in either direction. When you don't provide the second argument, the function rounds to the nearest whole number. When the second argument *integer* is specified, the function rounds to the nearest number with *integer* decimal places of precision. 

 This function can also truncate a `TIMESTAMP` and return a `DATE`. For more information, see [TRUNC function](r_TRUNC_date.md).

## Syntax
<a name="r_TRUNC-synopsis"></a>

```
TRUNC(number [ , integer ])
```

## Arguments
<a name="r_TRUNC-arguments"></a>

 *number*   
A number or an expression that evaluates to a number. It can be the `DECIMAL`, `FLOAT8` or `SUPER` type. Amazon Redshift can convert other data types per the implicit conversion rules. 

 *integer*  
(Optional) An `INTEGER` that indicates the number of decimal places of precision, in either direction. If no *integer* is provided, the number is truncated as a whole number; if an *integer* is specified, the number is truncated to the specified decimal place. This isn't supported for the `SUPER` data type.

## Return type
<a name="r_TRUNC-return-type"></a>

TRUNC returns the same data type as the input *number*. 

When the input is of the `SUPER` type, the output retains the same dynamic type as the input while the static type remains the `SUPER` type. When the dynamic type of `SUPER` isn't a number, Amazon Redshift returns `NULL`.

## Examples
<a name="r_TRUNC-examples"></a>

Some of the following examples use the TICKIT sample database. For more information, see [Sample database](c_sampledb.md).

To truncate the commission paid for a given sales transaction, use the following example. 

```
SELECT commission, TRUNC(commission)
FROM sales WHERE salesid=784;

+------------+-------+
| commission | trunc |
+------------+-------+
|     111.15 |   111 |
+------------+-------+
```

To truncate the same commission value to the first decimal place, use the following example. 

```
SELECT commission, TRUNC(commission,1)
FROM sales WHERE salesid=784;

+------------+-------+
| commission | trunc |
+------------+-------+
|     111.15 | 111.1 |
+------------+-------+
```

To truncate the commission with a negative value for the second argument, use the following example. Note that `111.15` is rounded down to `110`. 

```
SELECT commission, TRUNC(commission,-1)
FROM sales WHERE salesid=784;

+------------+-------+
| commission | trunc |
+------------+-------+
|     111.15 |   110 |
+------------+-------+
```