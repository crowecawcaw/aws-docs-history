

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# DECIMAL\_SCALE function
<a name="r_decimal_scale"></a>

Checks the number of decimal digits to be stored to the right of the decimal point. The range of the scale is from 0 to the precision point, with a default of 0.

## Syntax
<a name="r_decimal_scale-synopsis"></a>

```
DECIMAL_SCALE(super_expression)
```

## Arguments
<a name="r_decimal_scale-arguments"></a>

*super\_expression*  
A `SUPER` expression or column.

## Return type
<a name="r_decimal_scale-returns"></a>

`INTEGER`

## Examples
<a name="r_decimal_scale_example"></a>

To apply the DECIMAL\_SCALE function to the table t, use the following example.

```
CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (3.14159);

SELECT DECIMAL_SCALE(s) FROM t;

+---------------+
| decimal_scale |
+---------------+
|             5 |
+---------------+
```