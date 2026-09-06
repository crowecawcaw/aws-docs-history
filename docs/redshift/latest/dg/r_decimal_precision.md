

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# DECIMAL\_PRECISION function
<a name="r_decimal_precision"></a>

Checks the precision of the maximum total number of decimal digits to be stored. This number includes both the left and right digits of the decimal point. The range of the precision is from 1 to 38, with a default of 38.

## Syntax
<a name="r_decimal_precision-synopsis"></a>

```
DECIMAL_PRECISION(super_expression)
```

## Arguments
<a name="r_decimal_precision-arguments"></a>

*super\_expression*  
A `SUPER` expression or column.

## Return type
<a name="r_decimal_precision-returns"></a>

`INTEGER`

## Examples
<a name="r_decimal_precision_example"></a>

To apply the DECIMAL\_PRECISION function to the table t, use the following example.

```
CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (3.14159);

SELECT DECIMAL_PRECISION(s) FROM t;

+-------------------+
| decimal_precision |
+-------------------+
|                 6 |
+-------------------+
```