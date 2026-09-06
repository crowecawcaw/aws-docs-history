

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# IS\_BIGINT function
<a name="r_is_bigint"></a>

Checks whether a value is a `BIGINT`. The IS\_BIGINT function returns `true` for numbers of scale 0 in the 64-bit range. Otherwise, the function returns `false` for all other values, including null and floating point numbers.

The IS\_BIGINT function is a superset of IS\_INTEGER.

## Syntax
<a name="r_is_bigint-synopsis"></a>

```
IS_BIGINT(super_expression)
```

## Arguments
<a name="r_is_bigint-arguments"></a>

*super\_expression*  
A `SUPER` expression or column.

## Return type
<a name="r_is_bigint-returns"></a>

`BOOLEAN`

## Examples
<a name="r_is_bigint_example"></a>

To check if `5` is a `BIGINT` using the IS\_BIGINT function, use the following example.

```
CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (5);

SELECT s, IS_BIGINT(s) FROM t;

+---+-----------+
| s | is_bigint |
+---+-----------+
| 5 | true      |
+---+-----------+
```