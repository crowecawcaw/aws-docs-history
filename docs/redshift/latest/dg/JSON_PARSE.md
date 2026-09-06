

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# JSON\_PARSE function
<a name="JSON_PARSE"></a>

The JSON\_PARSE function parses data in JSON format and converts it into the `SUPER` representation. 

To ingest into `SUPER` data type using the INSERT or UPDATE command, use the JSON\_PARSE function. When you use JSON\_PARSE() to parse JSON strings into `SUPER` values, certain restrictions apply. For additional information, see [Parsing options for SUPER](super-configurations.md#parsing-options-super).

## Syntax
<a name="JSON_PARSE-synopsis"></a>

```
JSON_PARSE( {json_string | binary_value} )
```

## Arguments
<a name="JSON_PARSE-arguments"></a>

 *json\_string*  
An expression that returns serialized JSON as a `VARBYTE` or `VARCHAR` type. 

 *binary\_value*  
A VARBYTE type binary value.

## Return type
<a name="JSON_PARSE-return"></a>

`SUPER`

## Examples
<a name="JSON_PARSE-examples"></a>

To convert the JSON array `[10001,10002,"abc"]` into the `SUPER` data type, use the following example.

```
SELECT JSON_PARSE('[10001,10002,"abc"]');

+---------------------+
|     json_parse      |
+---------------------+
| [10001,10002,"abc"] |
+---------------------+
```

To make sure that the function converted the JSON array into the `SUPER` data type, use the following example. For more information, see [JSON\_TYPEOF function](r_json_typeof.md)

```
SELECT JSON_TYPEOF(JSON_PARSE('[10001,10002,"abc"]'));

+-------------+
| json_typeof |
+-------------+
| array       |
+-------------+
```