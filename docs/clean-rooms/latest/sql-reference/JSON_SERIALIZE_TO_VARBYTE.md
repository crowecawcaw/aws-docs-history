# JSON_SERIALIZE_TO_VARBYTE function

The JSON_SERIALIZE_TO_VARBYTE function converts a SUPER value to a JSON string similar
to JSON_SERIALIZE(), but stored in a VARBYTE value instead.

## Syntax

```
JSON_SERIALIZE_TO_VARBYTE(*super\_expression*)
```

## Arguments

_super_expression_

A super expression or column.

## Return type

varbyte

## Example

The following example serializes a SUPER value and returns the result in VARBYTE
format.

```
SELECT JSON_SERIALIZE_TO_VARBYTE(JSON_PARSE('[10001,10002,"abc"]'));

```

```
       json_serialize_to_varbyte
----------------------------------------
 5b31303030312c31303030322c22616263225d
```

The following example serializes a SUPER value and casts the result to VARCHAR
format.

```
SELECT JSON_SERIALIZE_TO_VARBYTE(JSON_PARSE('[10001,10002,"abc"]'))::VARCHAR;

```

```
  json_serialize_to_varbyte
---------------------------
 [10001,10002,"abc"]
```
