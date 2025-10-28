Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# JSON_TYPEOF function

The JSON_TYPEOF scalar function returns a `VARCHAR` with values boolean, number,
string, object, array, or null, depending on the dynamic type of the `SUPER` value.

## Syntax

```
JSON_TYPEOF(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` expression or column.

## Return type

`VARCHAR`

## Examples

To check the type of JSON for the array `[1,2]` using the JSON_TYPEOF function, use the following example.

````
`SELECT JSON_TYPEOF(ARRAY(1,2));`

`+-------------+
| json_typeof | +-------------+
| array | +-------------+` ``` To check the type of JSON for the object `{"name":"Joe"}` using the JSON\_TYPEOF function, use the following example. ``` `SELECT JSON_TYPEOF(JSON_PARSE('{"name":"Joe"}'));` `+-------------+
| json_typeof | +-------------+
| object | +-------------+` ```
````
