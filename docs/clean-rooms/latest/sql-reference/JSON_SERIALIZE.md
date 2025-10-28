# JSON_SERIALIZE function

The JSON_SERIALIZE function serializes a SUPER expression into textual JSON
representation to follow RFC 8259. For more information on that RFC, see [The JavaScript Object Notation (JSON) Data
Interchange Format](https://tools.ietf.org/html/rfc8259 "https://tools.ietf.org/html/rfc8259").

The SUPER size limit is approximately the same as the block limit, and the varchar limit
is smaller than the SUPER size limit. Therefore, the JSON_SERIALIZE function returns an
error when the JSON format exceeds the varchar limit of the system.

## Syntax

```
JSON_SERIALIZE(*super\_expression*)
```

## Arguments

_super_expression_

A super expression or column.

## Return type

varchar

## Example

The following example serializes a SUPER value to a string.

```
 SELECT JSON_SERIALIZE(JSON_PARSE('[10001,10002,"abc"]'));
   json_serialize
---------------------
 [10001,10002,"abc"]
(1 row)
```
