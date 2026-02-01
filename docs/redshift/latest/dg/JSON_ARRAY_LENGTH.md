Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# JSON_ARRAY_LENGTH function

###### Note

JSON_PARSE and its associated functions
parse JSON values as SUPER, which Amazon Redshift parses more efficiently than VARCHAR.

Instead of using JSON_ARRAY_LENGTH, we recommend that you parse your JSON strings using the
[JSON_PARSE function](JSON_PARSE.md "JSON_PARSE.md") to get a SUPER value. Then,
use the
[get_array_length function](get_array_length.md "get_array_length.md") to
get the length of your array.

The JSON_ARRAY_LENGTH function returns the number of elements in the outer array of a
JSON string. If the _null_if_invalid_ argument is set to
`true` and the JSON string is invalid, the function returns `NULL` instead
of returning an error.

For more information, see [JSON functions](json-functions.md "json-functions.md").

## Syntax

```
JSON_ARRAY_LENGTH('*json\_array*' [, *null\_if\_invalid* ] )
```

## Arguments

_json_array_

A properly formatted JSON array.

_null_if_invalid_

(Optional) A `BOOLEAN` value that specifies whether to return `NULL` if the input JSON
string is invalid instead of returning an error. To return `NULL` if the JSON
is invalid, specify `true` (`t`). To return an error
if the JSON is invalid, specify `false` (`f`). The
default is `false`.

## Return type

`INTEGER`

## Examples

To return the number of elements in the array, use the following example.

```
`SELECT JSON_ARRAY_LENGTH('[11,12,13,{"f1":21,"f2":[25,26]},14]');`

`+-------------------+
| json_array_length |
+-------------------+
| 5 |
+-------------------+`
```

To return an error because the JSON is invalid, use the following example.

```
`SELECT JSON_ARRAY_LENGTH('[11,12,13,{"f1":21,"f2":[25,26]},14');`

`ERROR: invalid json array object [11,12,13,{"f1":21,"f2":[25,26]},14`
```

To set _null_if_invalid_ to
_true_, so the statement the returns `NULL` instead of returning
an error for invalid JSON, use the following example.

```
`SELECT JSON_ARRAY_LENGTH('[11,12,13,{"f1":21,"f2":[25,26]},14',true);`

`+-------------------+
| json_array_length |
+-------------------+
| NULL |
+-------------------+`
```
