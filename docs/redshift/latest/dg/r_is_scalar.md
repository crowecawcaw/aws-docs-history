

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# IS\_SCALAR function
<a name="r_is_scalar"></a>

Checks whether a variable is a scalar. The IS\_SCALAR function returns `true` for any value that is not an array or an object. The function returns `false` for any other values, including null.

The set of IS\_ARRAY, IS\_OBJECT, and IS\_SCALAR cover all values except nulls.

## Syntax
<a name="r_is_scalar-synopsis"></a>

```
IS_SCALAR(super_expression)
```

## Arguments
<a name="r_is_scalar-arguments"></a>

*super\_expression*  
A `SUPER` expression or column.

## Return type
<a name="r_is_scalar-returns"></a>

`BOOLEAN`

## Examples
<a name="r_is_scalar_example"></a>

To check if `{"name": "Joe"}` is a scalar using the IS\_SCALAR function, use the following example.

```
CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (JSON_PARSE('{"name": "Joe"}'));

SELECT s, IS_SCALAR(s.name) FROM t;

+----------------+-----------+
|       s        | is_scalar |
+----------------+-----------+
| {"name":"Joe"} | true      |
+----------------+-----------+
```