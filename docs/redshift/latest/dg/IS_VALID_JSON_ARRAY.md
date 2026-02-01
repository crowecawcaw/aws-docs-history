Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# IS_VALID_JSON_ARRAY function

###### Note

JSON_PARSE and its associated functions
parse JSON values as SUPER, which Amazon Redshift parses more efficiently than VARCHAR.

Instead of using IS_VALID_JSON_ARRAY, we recommend that you parse your JSON strings using the
[JSON_PARSE function](JSON_PARSE.md "JSON_PARSE.md") to get a SUPER value. Then,
use the
[IS_ARRAY function](r_is_array.md "r_is_array.md") function to confirm that the array is properly formed.

The IS_VALID_JSON_ARRAY function validates a JSON array. The function returns Boolean
`true` if the array is properly formed JSON or
`false` if the array is malformed. To validate a JSON
string, use [IS_VALID_JSON function](IS_VALID_JSON.md "IS_VALID_JSON.md")

For more information, see [JSON functions](json-functions.md "json-functions.md").

## Syntax

```
IS_VALID_JSON_ARRAY('*json\_array*')
```

## Arguments

_json_array_

A string or expression that evaluates to a JSON array.

## Return type

`BOOLEAN`

## Examples

To create a table and insert JSON strings for testing, use the following example.

```
`CREATE TABLE test_json_arrays(id int IDENTITY(0,1), json_arrays VARCHAR);

-- Insert valid JSON array strings --
INSERT INTO test_json_arrays(json_arrays)
VALUES('[]'),
('["a","b"]'),
('["a",["b",1,["c",2,3,null]]]');

-- Insert invalid JSON array strings --
INSERT INTO test_json_arrays(json_arrays)
VALUES('{"a":1}'),
('a'),
('[1,2,]');`
```

To validate the strings in the preceding example, use the following example.

```
`SELECT json_arrays, IS_VALID_JSON_ARRAY(json_arrays)
FROM test_json_arrays ORDER BY id;`

`+------------------------------+---------------------+
| json_arrays | is_valid_json_array |
+------------------------------+---------------------+
| [] | true |
| ["a","b"] | true |
| ["a",["b",1,["c",2,3,null]]] | true |
| {"a":1} | false |
| a | false |
| [1,2,] | false |
+------------------------------+---------------------+`
```
