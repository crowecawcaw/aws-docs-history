Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# IS_VALID_JSON function

###### Note

CAN_JSON_PARSE and its associated functions
parse JSON values as SUPER, which Amazon Redshift parses more efficiently than VARCHAR.

Instead of using IS_VALID_JSON, we recommend that you validate your JSON strings using the
[CAN_JSON_PARSE function](CAN_JSON_PARSE.md "CAN_JSON_PARSE.md").

The IS_VALID_JSON function validates a JSON string. The function returns Boolean
`true` if the string is properly formed JSON or
`false` if the string is malformed. To validate a JSON
array, use [IS_VALID_JSON_ARRAY function](IS_VALID_JSON_ARRAY.md "IS_VALID_JSON_ARRAY.md")

For more information, see [JSON functions](json-functions.md "json-functions.md").

## Syntax

```
IS_VALID_JSON('*json\_string*')
```

## Arguments

_json_string_

A string or expression that evaluates to a JSON string.

## Return type

`BOOLEAN`

## Examples

To create a table and insert JSON strings for testing, use the following example.

```
`CREATE TABLE test_json(id int IDENTITY(0,1), json_strings VARCHAR);

-- Insert valid JSON strings --
INSERT INTO test_json(json_strings) VALUES
('{"a":2}'),
('{"a":{"b":{"c":1}}}'),
('{"a": [1,2,"b"]}');

-- Insert invalid JSON strings --
INSERT INTO test_json(json_strings) VALUES
('{{}}'),
('{1:"a"}'),
('[1,2,3]');`
```

To validate the strings in the preceding example, use the following example.

```
`SELECT id, json_strings, IS_VALID_JSON(json_strings)
FROM test_json
ORDER BY id;`

`+----+---------------------+---------------+
| id | json_strings | is_valid_json |
+----+---------------------+---------------+
| 0 | {"a":2} | true |
| 4 | {"a":{"b":{"c":1}}} | true |
| 8 | {"a": [1,2,"b"]} | true |
| 12 | {{}} | false |
| 16 | {1:"a"} | false |
| 20 | [1,2,3] | false |
+----+---------------------+---------------+`
```
