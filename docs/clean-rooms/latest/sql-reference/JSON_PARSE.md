# JSON_PARSE function

The JSON_PARSE function parses data in JSON format and converts it into the SUPER
representation.

To ingest into SUPER data type using the INSERT or UPDATE command, use the JSON_PARSE
function. When you use JSON_PARSE() to parse JSON strings into SUPER values, certain
restrictions apply.

## Syntax

```
JSON_PARSE(*json\_string*)
```

## Arguments

_json_string_

An expression that returns serialized JSON as a varbyte or varchar type.

## Return type

SUPER

## Example

The following example is an example of the JSON_PARSE function.

```
SELECT JSON_PARSE('[10001,10002,"abc"]');
     json_parse
--------------------------
 [10001,10002,"abc"]
(1 row)
```

```
SELECT JSON_TYPEOF(JSON_PARSE('[10001,10002,"abc"]'));
 json_typeof
----------------
 array
(1 row)
```
