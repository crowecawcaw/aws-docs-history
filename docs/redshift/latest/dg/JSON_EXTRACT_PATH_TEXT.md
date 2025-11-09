Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# JSON_EXTRACT_PATH_TEXT function

###### Note

JSON_PARSE and its associated functions
parse JSON values as SUPER, which Amazon Redshift parses more efficiently than VARCHAR.

Instead of using JSON_EXTRACT_PATH_TEXT, we recommend that you parse your
JSON strings using the [JSON_PARSE function](JSON_PARSE.md "JSON_PARSE.md") to get a SUPER value.
Then, query the element you want using the `value.attribute` syntax.
For more information on querying array elements
in SUPER values, go to [Querying semi-structured data](query-super.md "query-super.md").

The JSON_EXTRACT_PATH_TEXT function returns the value for the
key-value pair referenced by a series of path elements in a JSON
string. The JSON path can be nested up to five levels deep. Path elements are
case-sensitive. If a path element does not exist in the JSON string,
JSON_EXTRACT_PATH_TEXT returns `NULL`.

If the _null_if_invalid_
argument is set to `TRUE` and the JSON string is invalid, the function
returns `NULL` instead of returning an error.

JSON_EXTRACT_PATH_TEXT has a 64KB data-size maximum.
Thus, if any JSON record is larger than 64KB, processing it with JSON_EXTRACT_PATH_TEXT results in an error.

For information about additional JSON functions, see [JSON functions](json-functions.md "json-functions.md"). For more information about working with JSON, see [COPY from JSON format](copy-usage_notes-copy-from-json.md "copy-usage_notes-copy-from-json.md").

## Syntax

```
JSON_EXTRACT_PATH_TEXT('*json\_string*', '*path\_elem*' [,'*path\_elem*'[, …] ] [, *null\_if\_invalid* ] )
```

## Arguments

_json_string_

A properly formatted JSON string.

_path_elem_

A path element in a JSON string. One path element is required. Additional
path elements can be specified, up to five levels deep.

_null_if_invalid_

(Optional) A `BOOLEAN` value that specifies whether to return `NULL` if the input JSON
string is invalid instead of returning an error. To return `NULL` if the JSON
is invalid, specify `TRUE` (`t`). To return an error
if the JSON is invalid, specify `FALSE` (`f`). The
default is `FALSE`.

In a JSON string, Amazon Redshift recognizes `\n` as a newline character and
`\t` as a tab character. To load a backslash, escape it with a
backslash (`\\`). For more information, see [Escape characters in JSON](copy-usage_notes-copy-from-json.md#copy-usage-json-escape-characters "copy-usage_notes-copy-from-json.md#copy-usage-json-escape-characters").

## Return type

`VARCHAR`

A `VARCHAR` string representing the JSON value referenced by the path elements.

## Examples

To return the value for the path `'f4', 'f6'`, use the following example.

```
`SELECT JSON_EXTRACT_PATH_TEXT('{"f2":{"f3":1},"f4":{"f5":99,"f6":"star"}}','f4', 'f6');`

`+------------------------+
| json_extract_path_text |
+------------------------+
| star |
+------------------------+`
```

To return an error because the JSON is invalid, use the following example.

```
`SELECT JSON_EXTRACT_PATH_TEXT('{"f2":{"f3":1},"f4":{"f5":99,"f6":"star"}','f4', 'f6');`

`ERROR: invalid json object {"f2":{"f3":1},"f4":{"f5":99,"f6":"star"}`
```

To set _null_if_invalid_ to
_TRUE_, so the statement returns `NULL` for invalid JSON instead of
returning an error, use the following example.

```
`SELECT JSON_EXTRACT_PATH_TEXT('{"f2":{"f3":1},"f4":{"f5":99,"f6":"star"}','f4', 'f6',true);`

`+------------------------+
| json_extract_path_text |
+------------------------+
| NULL |
+------------------------+`
```

Consider the following example, which selects the value for the path `'farm', 'barn', 'color'`, where the
value retrieved is at the third level, use the following example. This sample is formatted with a JSON lint tool, to make it easier to read.

```
`SELECT JSON_EXTRACT_PATH_TEXT('{
 "farm": {
 "barn": {
 "color": "red",
 "feed stocked": true
 }
 }
}', 'farm', 'barn', 'color');`
`+------------------------+
| json_extract_path_text |
+------------------------+
| red |
+------------------------+`
```

To return `NULL` because the `'color'` element is missing, use the following example. This sample is
formatted with a JSON lint tool.

```
`SELECT JSON_EXTRACT_PATH_TEXT('{
 "farm": {
 "barn": {}
 }
}', 'farm', 'barn', 'color');`

`+------------------------+
| json_extract_path_text |
+------------------------+
| NULL |
+------------------------+`
```

If the JSON is valid, trying to extract an element that's missing returns `NULL`.

To return the value for the path `'house', 'appliances', 'washing machine', 'brand'`, use the following example.

```
`SELECT JSON_EXTRACT_PATH_TEXT('{
 "house": {
 "address": {
 "street": "123 Any St.",
 "city": "Any Town",
 "state": "FL",
 "zip": "32830"
 },
 "bathroom": {
 "color": "green",
 "shower": true
 },
 "appliances": {
 "washing machine": {
 "brand": "Any Brand",
 "color": "beige"
 },
 "dryer": {
 "brand": "Any Brand",
 "color": "white"
 }
 }
 }
}', 'house', 'appliances', 'washing machine', 'brand');`

`+------------------------+
| json_extract_path_text |
+------------------------+
| Any Brand |
+------------------------+`
```

The following example creates a sample table and populates it
with SUPER values, then returns the value for the path
`'f2'` for both rows.

```
CREATE TABLE json_example(id INT, json_text SUPER);

INSERT INTO json_example VALUES
(1, JSON_PARSE('{"f2":{"f3":1},"f4":{"f5":99,"f6":"star"}}')),
(2, JSON_PARSE('{
    "farm": {
        "barn": {
            "color": "red",
            "feed stocked": true
        }
    }
}'));

SELECT * FROM json_example;
`id | json_text
------------+--------------------------------------------
1 | {"f2":{"f3":1},"f4":{"f5":99,"f6":"star"}}
2 | {"farm":{"barn":{"color":"red","feed stocked":true}}}`

SELECT id, JSON_EXTRACT_PATH_TEXT(JSON_SERIALIZE(json_text), 'f2') FROM json_example;

`id | json_text
------------+--------------------------------------------
1 | {"f3":1}
2 |`
```

Consider the following example statements. The provided _path_elem_ is NULL, so
JSON_EXTRACT_PATH_TEXT returns NULL regardless of the value of any other parameters.

```
--Statement where path_elem is NULL and json_string is valid JSON.
SELECT JSON_EXTRACT_PATH_TEXT('{"f2":{"f3":1},"f4":{"f5":99,"f6":"star"}}',NULL);
`json_extract_path_text
------------------------
 NULL`

--Statement where only one path_elem is NULL.
SELECT JSON_EXTRACT_PATH_TEXT('{"f2":{"f3":1},"f4":{"f5":99,"f6":"star"}}','f4',NULL);
`json_extract_path_text
------------------------
 NULL`

--Statement where path_elem is NULL and json_string is invalid JSON.
SELECT json_extract_path_text('invalid_json', NULL);

 `json_extract_path_text
------------------------
 NULL`

--Statement where path_elem is NULL and null_if_invalid is FALSE.
SELECT json_extract_path_text(NULL, 0, FALSE);

 `json_extract_path_text
------------------------
 NULL`
```

Consider the following example statements. When _null_if_invalid_ is TRUE,
JSON_EXTRACT_PATH_TEXT returns NULL when _json_string_ is invalid JSON.
If _null_if_invalid_ is FALSE or isn’t set, the function returns an
error when _json_string_ is invalid.

```
--Statement with invalid JSON where null_if_invalid is TRUE.
SELECT json_extract_path_text('invalid_json', 0, TRUE);

 `json_extract_path_text
------------------------
 NULL`

--Statement with invalid JSON where null_if_invalid is FALSE.
SELECT json_extract_path_text('invalid_json', 0, FALSE);

`ERROR: JSON parsing error`

```

Consider the following examples, where _json_string_ is valid JSON,
and _path_elem_ refers to a JSON `null` value. In this case,
JSON_EXTRACT_PATH_TEXT returns NULL. Similarly, when _path_elem_ refers to a
non-existing value, JSON_EXTRACT_PATH_TEXT returns NULL, regardless of
the value of _null_if_invalid_.

```
--Statement selecting a null value.
SELECT json_extract_path_text('[null]', 0);

  json_extract_path_text
-------------------------
                    NULL

--Statement selecting a non-existing value.
SELECT json_extract_path_text('{}', 'a');

  json_extract_path_text
-------------------------
                    NULL
```
