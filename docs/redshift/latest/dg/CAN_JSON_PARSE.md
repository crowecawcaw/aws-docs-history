Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CAN_JSON_PARSE function

The CAN_JSON_PARSE function parses data in JSON format and returns `true` if the result can be converted to a `SUPER` value using the JSON_PARSE function.

## Syntax

```
CAN_JSON_PARSE( {*json\_string* | *binary\_value*} )
```

## Arguments

_json_string_

An expression that returns serialized JSON in `VARCHAR`
form.

_binary_value_

A VARBYTE type binary value.

## Return type

`BOOLEAN`

## Usage notes

- CAN_JSON_PARSE returns false for empty strings. It returns NULL when the input argument is null.

## Examples

The following example shows CAN_JSON_PARSE running on a properly formed JSON array
using a CASE condition.
It returns true, so Amazon Redshift runs the JSON_PARSE function on the example value.

```
`SELECT CASE
 WHEN CAN_JSON_PARSE('[10001,10002,"abc"]')
 THEN JSON_PARSE('[10001,10002,"abc"]')
 END;`

 `case
---------------------
'[10001,10002,"abc"]'`
```

The following example shows CAN_JSON_PARSE running on a value that isn’t JSON format
using a CASE condition.
It returns false, so Amazon Redshift returns the segment in the ELSE clause of the CASE condition instead.

```
`SELECT CASE
 WHEN CAN_JSON_PARSE('This is a string.')
 THEN JSON_PARSE('This is a string.')
 ELSE 'This is not JSON.'
 END;`

 `case
---------------------
"This is not JSON."`
```
