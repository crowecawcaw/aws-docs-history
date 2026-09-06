

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# IS\_BOOLEAN function
<a name="r_is_boolean"></a>

Checks whether a value is a `BOOLEAN`. The IS\_BOOLEAN function returns `true` for constant JSON Booleans. The function returns `false` for any other values, including null.

## Syntax
<a name="r_is_boolean-synopsis"></a>

```
IS_BOOLEAN(super_expression)
```

## Arguments
<a name="r_is_boolean-arguments"></a>

*super\_expression*  
A `SUPER` expression or column.

## Return type
<a name="r_is_boolean-returns"></a>

`BOOLEAN`

## Examples
<a name="r_is_boolean_example"></a>

To check if `TRUE` is a `BOOLEAN` using the IS\_BOOLEAN function, use the following example.

```
CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (TRUE);

SELECT s, IS_BOOLEAN(s) FROM t;

+------+------------+
|  s   | is_boolean |
+------+------------+
| true | true       |
+------+------------+
```