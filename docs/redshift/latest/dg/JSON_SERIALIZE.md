

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# JSON\_SERIALIZE function
<a name="JSON_SERIALIZE"></a>

The JSON\_SERIALIZE function serializes a `SUPER` expression into textual JSON representation to follow RFC 8259. For more information on that RFC, see [The JavaScript Object Notation (JSON) Data Interchange Format](https://tools.ietf.org/html/rfc8259).

The `SUPER` size limit is approximately the same as the block limit, and the `VARCHAR` limit is smaller than the `SUPER` size limit. Therefore, the JSON\_SERIALIZE function returns an error when the JSON format exceeds the VARCHAR limit of the system. To check the size of a `SUPER` expression, see the [JSON\_SIZE](r_json_size.md) function.

## Syntax
<a name="JSON_SERIALIZE-synopsis"></a>

```
JSON_SERIALIZE(super_expression)
```

## Arguments
<a name="JSON_SERIALIZE-arguments"></a>

 *super\_expression*  
A `SUPER` expression or column.

## Return type
<a name="JSON_SERIALIZE-return"></a>

`VARCHAR`

**Note**  
The returned VARCHAR value is always a non-null JSON string. If *super\_expression* is NULL, JSON\_SERIALIZE returns the JSON string `'null'`.

## Examples
<a name="JSON_SERIALIZE-examples"></a>

To serialize a `SUPER` value to a string, use the following example.

```
SELECT JSON_SERIALIZE(JSON_PARSE('[10001,10002,"abc"]'));
   
+---------------------+
|   json_serialize    |
+---------------------+
| [10001,10002,"abc"] |
+---------------------+
```