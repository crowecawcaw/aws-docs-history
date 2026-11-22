

# Type system (response mapping)

When receiving a response from DynamoDB, AWS AppSync automatically converts it into GraphQL and JSON primitive types. Each attribute in DynamoDB is decoded and returned in the response mapping context.

For example, if DynamoDB returns the following:

```TypeScript
{
    "id" : { "S" : "1234" },
    "name" : { "S" : "Nadia" },
    "age" : { "N" : 25 }
}
```

Then the AWS AppSync DynamoDB resolver converts it into GraphQL and JSON types as:

```TypeScript
{
    "id" : "1234",
    "name" : "Nadia",
    "age" : 25
}
```

This section explains how AWS AppSync converts the following DynamoDB scalar, document, and set types:

**String type `S` **  
A single string value. A DynamoDB String value is returned as a string.  
For example, if DynamoDB returned the following DynamoDB String value:  

```TypeScript
{ "S" : "some string" }
```
AWS AppSync converts it to a string:  

```TypeScript
"some string"
```

**String set type `SS` **  
A set of string values. A DynamoDB String Set value is returned as a list of strings.  
For example, if DynamoDB returned the following DynamoDB String Set value:  

```TypeScript
{ "SS" : [ "first value", "second value", ... ] }
```
AWS AppSync converts it to a list of strings:  

```TypeScript
[ "+1 555 123 4567", "+1 555 234 5678" ]
```

**Number type `N` **  
A single numeric value. A DynamoDB Number value is returned as a number.  
For example, if DynamoDB returned the following DynamoDB Number value:  

```TypeScript
{ "N" : 1234 }
```
AWS AppSync converts it to a number:  

```TypeScript
1234
```

**Number set type `NS` **  
A set of number values. A DynamoDB Number Set value is returned as a list of numbers.  
For example, if DynamoDB returned the following DynamoDB Number Set value:  

```TypeScript
{ "NS" : [ 67.8, 12.2, 70 ] }
```
AWS AppSync converts it to a list of numbers:  

```TypeScript
[ 67.8, 12.2, 70 ]
```

**Binary type `B` **  
A binary value. A DynamoDB Binary value is returned as a string containing the base64 representation of that value.  
For example, if DynamoDB returned the following DynamoDB Binary value:  

```TypeScript
{ "B" : "SGVsbG8sIFdvcmxkIQo=" }
```
AWS AppSync converts it to a string containing the base64 representation of the value:  

```TypeScript
"SGVsbG8sIFdvcmxkIQo="
```
Note that the binary data is encoded in the base64 encoding scheme as specified in [RFC 4648](https://tools.ietf.org/html/rfc4648) and [RFC 2045](https://tools.ietf.org/html/rfc2045).

**Binary set type `BS` **  
A set of binary values. A DynamoDB Binary Set value is returned as a list of strings containing the base64 representation of the values.  
For example, if DynamoDB returned the following DynamoDB Binary Set value:  

```TypeScript
{ "BS" : [ "SGVsbG8sIFdvcmxkIQo=", "SG93IGFyZSB5b3U/Cg==" ... ] }
```
AWS AppSync converts it to a list of strings containing the base64 representation of the values:  

```TypeScript
[ "SGVsbG8sIFdvcmxkIQo=", "SG93IGFyZSB5b3U/Cg==" ... ]
```
Note that the binary data is encoded in the base64 encoding scheme as specified in [RFC 4648](https://tools.ietf.org/html/rfc4648) and [RFC 2045](https://tools.ietf.org/html/rfc2045).

**Boolean type `BOOL` **  
A Boolean value. A DynamoDB Boolean value is returned as a Boolean.  
For example, if DynamoDB returned the following DynamoDB Boolean value:  

```TypeScript
{ "BOOL" : true }
```
AWS AppSync converts it to a Boolean:  

```TypeScript
true
```

**List type `L` **  
A list of any other supported DynamoDB value. A DynamoDB List value is returned as a list of values, where each inner value is also converted.  
For example, if DynamoDB returned the following DynamoDB List value:  

```TypeScript
{ "L" : [
      { "S"  : "A string value" },
      { "N"  : 1 },
      { "SS" : [ "Another string value", "Even more string values!" ] }
   ]
}
```
AWS AppSync converts it to a list of converted values:  

```TypeScript
[ "A string value", 1, [ "Another string value", "Even more string values!" ] ]
```

**Map type `M` **  
A key/value collection of any other supported DynamoDB value. A DynamoDB Map value is returned as a JSON object, where each key/value is also converted.  
For example, if DynamoDB returned the following DynamoDB Map value:  

```TypeScript
{ "M" : {
      "someString" : { "S"  : "A string value" },
      "someNumber" : { "N"  : 1 },
      "stringSet"  : { "SS" : [ "Another string value", "Even more string values!" ] }
   }
}
```
AWS AppSync converts it to a JSON object:  

```TypeScript
{
   "someString" : "A string value",
   "someNumber" : 1,
   "stringSet"  : [ "Another string value", "Even more string values!" ]
}
```

**Null type `NULL` **  
A null value.  
For example, if DynamoDB returned the following DynamoDB Null value:  

```TypeScript
{ "NULL" : null }
```
AWS AppSync converts it to a null:  

```TypeScript
null
```