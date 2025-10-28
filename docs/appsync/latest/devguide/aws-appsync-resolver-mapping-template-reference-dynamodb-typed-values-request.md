# Type system (request mapping)

When using the AWS AppSync DynamoDB resolver to call your DynamoDB tables, AWS AppSync needs to know the type of each
value to use in that call. This is because DynamoDB supports more type primitives than GraphQL or JSON (such as
sets and binary data). AWS AppSync needs some hints when translating between GraphQL and DynamoDB, otherwise it
would have to make some assumptions on how data is structured in your table.

For more information about DynamoDB data types, see the DynamoDB [Data type descriptors](../../../amazondynamodb/latest/developerguide/Programming.md#Programming.LowLevelAPI.DataTypeDescriptors "../../../amazondynamodb/latest/developerguide/Programming.md#Programming.LowLevelAPI.DataTypeDescriptors") and [Data types](../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes "../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes") documentation.

A DynamoDB value is represented by a JSON object containing a single key-value pair. The key specifies the
DynamoDB type, and the value specifies the value itself. In the following example, the key `S` denotes
that the value is a string, and the value `identifier` is the string value itself.

```
{ "S" : "identifier" }
```

Note that the JSON object cannot have more than one key-value pair. If more than one key-value pair is
specified, the request mapping document isn’t parsed.

A DynamoDB value is used anywhere in a request mapping document where you need to specify a value. Some places
where you need to do this include: `key` and `attributeValue` sections, and the
`expressionValues` section of expression sections. In the following example, the DynamoDB String
value `identifier` is being assigned to the `id` field in a `key` section
(perhaps in a `GetItem` request mapping document).

```
"key" : {
   "id" : { "S" : "identifier" }
}
```

**Supported Types**

AWS AppSync supports the following DynamoDB scalar, document, and set types:

**String type `S`**

A single string value. A DynamoDB String value is denoted by:

```
{ "S" : "some string" }
```

An example usage is:

```
"key" : {
   "id" : { "S" : "some string" }
}
```

**String set type `SS`**

A set of string values. A DynamoDB String Set value is denoted by:

```
{ "SS" : [ "first value", "second value", ... ] }
```

An example usage is:

```
"attributeValues" : {
   "phoneNumbers" : { "SS" : [ "+1 555 123 4567", "+1 555 234 5678" ] }
}
```

**Number type `N`**

A single numeric value. A DynamoDB Number value is denoted by:

```
{ "N" : 1234 }
```

An example usage is:

```
"expressionValues" : {
   ":expectedVersion" : { "N" : 1 }
}
```

**Number set type `NS`**

A set of number values. A DynamoDB Number Set value is denoted by:

```
{ "NS" : [ 1, 2.3, 4 ... ] }
```

An example usage is:

```
"attributeValues" : {
   "sensorReadings" : { "NS" : [ 67.8, 12.2, 70 ] }
}
```

**Binary type `B`**

A binary value. A DynamoDB Binary value is denoted by:

```
{ "B" : "SGVsbG8sIFdvcmxkIQo=" }
```

Note that the value is actually a string, where the string is the base64-encoded representation of
the binary data. AWS AppSync decodes this string back into its binary value before sending it to DynamoDB.
AWS AppSync uses the base64 decoding scheme as defined by RFC 2045: any character that isn’t in the
base64 alphabet is ignored.

An example usage is:

```
"attributeValues" : {
   "binaryMessage" : { "B" : "SGVsbG8sIFdvcmxkIQo=" }
}
```

**Binary set type `BS`**

A set of binary values. A DynamoDB Binary Set value is denoted by:

```
{ "BS" : [ "SGVsbG8sIFdvcmxkIQo=", "SG93IGFyZSB5b3U/Cg==" ... ] }
```

Note that the value is actually a string, where the string is the base64-encoded representation of
the binary data. AWS AppSync decodes this string back into its binary value before sending it to DynamoDB.
AWS AppSync uses the base64 decoding scheme as defined by RFC 2045: any character that is not in the
base64 alphabet is ignored.

An example usage is:

```
"attributeValues" : {
   "binaryMessages" : { "BS" : [ "SGVsbG8sIFdvcmxkIQo=", "SG93IGFyZSB5b3U/Cg==" ] }
}
```

**Boolean type `BOOL`**

A Boolean value. A DynamoDB Boolean value is denoted by:

```
{ "BOOL" : true }
```

Note that only `true` and `false` are valid values.

An example usage is:

```
"attributeValues" : {
   "orderComplete" : { "BOOL" : false }
}
```

**List type `L`**

A list of any other supported DynamoDB value. A DynamoDB List value is denoted by:

```
{ "L" : [ ... ] }
```

Note that the value is a compound value, where the list can contain zero or more of any supported
DynamoDB value (including other lists). The list can also contain a mix of different types.

An example usage is:

```
{ "L" : [
      { "S"  : "A string value" },
      { "N"  : 1 },
      { "SS" : [ "Another string value", "Even more string values!" ] }
   ]
}
```

**Map type `M`**

Representing an unordered collection of key-value pairs of other supported DynamoDB values. A DynamoDB
Map value is denoted by:

```
{ "M" : { ... } }
```

Note that a map can contain zero or more key-value pairs. The key must be a string, and the value
can be any supported DynamoDB value (including other maps). The map can also contain a mix of different
types.

An example usage is:

```
{ "M" : {
      "someString" : { "S"  : "A string value" },
      "someNumber" : { "N"  : 1 },
      "stringSet"  : { "SS" : [ "Another string value", "Even more string values!" ] }
   }
}
```

**Null type `NULL`**

A null value. A DynamoDB Null value is denoted by:

```
{ "NULL" : null }
```

An example usage is:

```
"attributeValues" : {
   "phoneNumbers" : { "NULL" : null }
}
```

For more information about each type, see the [DynamoDB
documentation](../../../amazondynamodb/latest/developerguide/HowItWorks.md "../../../amazondynamodb/latest/developerguide/HowItWorks.md") .
