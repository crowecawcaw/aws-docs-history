

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# IS\_OBJECT function
<a name="r_is_object"></a>

Checks whether a variable is an object. The IS\_OBJECT function returns `true` for objects, including empty objects. The function returns `false` for any other values, including null.

## Syntax
<a name="r_is_object-synopsis"></a>

```
IS_OBJECT(super_expression)
```

## Arguments
<a name="r_is_object-arguments"></a>

*super\_expression*  
A `SUPER` expression or column.

## Return type
<a name="r_is_object-returns"></a>

`BOOLEAN`

## Examples
<a name="r_is_object_example"></a>

To check if `{"name": "Joe"}` is an object using the IS\_OBJECT function, use the following example.

```
CREATE TABLE t(s super);

INSERT INTO t VALUES (JSON_PARSE('{"name": "Joe"}'));

SELECT s, IS_OBJECT(s) FROM t;

+----------------+-----------+
|       s        | is_object |
+----------------+-----------+
| {"name":"Joe"} | true      |
+----------------+-----------+
```