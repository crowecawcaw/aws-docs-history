

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# JSON\_SERIALIZE\_TO\_VARBYTE function
<a name="JSON_SERIALIZE_TO_VARBYTE"></a>

The JSON\_SERIALIZE\_TO\_VARBYTE function converts a `SUPER` value to a JSON string similar to JSON\_SERIALIZE(), but stored in a `VARBYTE` value instead.

## Syntax
<a name="JSON_SERIALIZE_TO_VARBYTE-synopsis"></a>

```
JSON_SERIALIZE_TO_VARBYTE(super_expression)
```

## Arguments
<a name="JSON_SERIALIZE_TO_VARBYTE-arguments"></a>

 *super\_expression*  
A `SUPER` expression or column.

## Return type
<a name="JSON_SERIALIZE_TO_VARBYTE-return"></a>

`VARBYTE`

## Examples
<a name="JSON_SERIALIZE_TO_VARBYTE-examples"></a>

To serialize a `SUPER` value and returns the result in `VARBYTE` format, use the following example.

```
SELECT JSON_SERIALIZE_TO_VARBYTE(JSON_PARSE('[10001,10002,"abc"]'));

+----------------------------------------+
|       json_serialize_to_varbyte        |
+----------------------------------------+
| 5b31303030312c31303030322c22616263225d |
+----------------------------------------+
```

To serialize a `SUPER` value and casts the result to `VARCHAR` format, use the following example. For more information, see [CAST function](r_CAST_function.md).

```
SELECT CAST((JSON_SERIALIZE_TO_VARBYTE(JSON_PARSE('[10001,10002,"abc"]'))) AS VARCHAR);

+---------------------------+
| json_serialize_to_varbyte |
+---------------------------+
| [10001,10002,"abc"]       |
+---------------------------+
```