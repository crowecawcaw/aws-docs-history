

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# IS\_SMALLINT function
<a name="r_is_smallint"></a>

Checks whether a variable is a `SMALLINT`. The IS\_SMALLINT function returns `true` for numbers of scale 0 in the 16-bit range. The function returns `false` for any other values, including null and floating point numbers.

## Syntax
<a name="r_is_smallint-synopsis"></a>

```
IS_SMALLINT(super_expression)
```

## Arguments
<a name="r_is_smallint-arguments"></a>

*super\_expression*  
A `SUPER` expression or column.

## Return
<a name="r_is_smallint-returns"></a>

`BOOLEAN`

## Examples
<a name="r_is_smallint_example"></a>

To check if `5` is a `SMALLINT` using the IS\_SMALLINT function, use the following example.

```
CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (5);

SELECT s, IS_SMALLINT(s) FROM t;

+---+-------------+
| s | is_smallint |
+---+-------------+
| 5 | true        |
+---+-------------+
```