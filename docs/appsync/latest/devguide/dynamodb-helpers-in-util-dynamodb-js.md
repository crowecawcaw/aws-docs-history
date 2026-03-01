# DynamoDB helpers in util.dynamodb

`util.dynamodb` contains helper methods that make it easier to write and read
data to Amazon DynamoDB, such as automatic type mapping and formatting.

## toDynamoDB

**`util.dynamodb.toDynamoDB(Object)`**

General object conversion tool for DynamoDB that converts input objects
to the appropriate DynamoDB representation. It's opinionated about how it
represents some types: e.g., it will use lists ("L") rather than sets
("SS", "NS", "BS"). This returns an object that describes the DynamoDB
attribute value.

**String example**

```
Input:      util.dynamodb.toDynamoDB("foo")
Output:     { "S" : "foo" }
```

**Number example**

```
Input:      util.dynamodb.toDynamoDB(12345)
Output:     { "N" : 12345 }
```

**Boolean example**

```
Input:      util.dynamodb.toDynamoDB(true)
Output:     { "BOOL" : true }
```

**List example**

```
Input:      util.dynamodb.toDynamoDB([ "foo", 123, { "bar" : "baz" } ])
Output:     {
               "L" : [
                   { "S" : "foo" },
                   { "N" : 123 },
                   {
                       "M" : {
                           "bar" : { "S" : "baz" }
                       }
                   }
               ]
           }
```

**Map example**

```
Input:      util.dynamodb.toDynamoDB({ "foo": "bar", "baz" : 1234, "beep": [ "boop"] })
Output:     {
               "M" : {
                   "foo"  : { "S" : "bar" },
                   "baz"  : { "N" : 1234 },
                   "beep" : {
                       "L" : [
                           { "S" : "boop" }
                       ]
                   }
               }
           }
```

## toString utils

**`util.dynamodb.toString(String)`**

Converts an input string to the DynamoDB string format. This returns an
object that describes the DynamoDB attribute value.

```
Input:      util.dynamodb.toString("foo")
Output:     { "S" : "foo" }
```

**`util.dynamodb.toStringSet(List<String>)`**

Converts a list with Strings to the DynamoDB string set format. This
returns an object that describes the DynamoDB attribute value.

```
Input:      util.dynamodb.toStringSet([ "foo", "bar", "baz" ])
Output:     { "SS" : [ "foo", "bar", "baz" ] }
```

## toNumber utils

**`util.dynamodb.toNumber(Number)`**

Converts a number to the DynamoDB number format. This returns an object
that describes the DynamoDB attribute value.

```
Input:      util.dynamodb.toNumber(12345)
Output:     { "N" : 12345 }
```

**`util.dynamodb.toNumberSet(List<Number>)`**

Converts a list of numbers to the DynamoDB number set format. This
returns an object that describes the DynamoDB attribute value.

```
Input:      util.dynamodb.toNumberSet([ 1, 23, 4.56 ])
Output:     { "NS" : [ 1, 23, 4.56 ] }
```

## toBinary utils

**`util.dynamodb.toBinary(String)`**

Converts binary data encoded as a base64 string to DynamoDB binary
format. This returns an object that describes the DynamoDB attribute
value.

```
Input:      util.dynamodb.toBinary("foo")
Output:     { "B" : "foo" }
```

**`util.dynamodb.toBinarySet(List<String>)`**

Converts a list of binary data encoded as base64 strings to DynamoDB
binary set format. This returns an object that describes the DynamoDB
attribute value.

```
Input:      util.dynamodb.toBinarySet([ "foo", "bar", "baz" ])
Output:     { "BS" : [ "foo", "bar", "baz" ] }
```

## toBoolean utils

**`util.dynamodb.toBoolean(Boolean)`**

Converts a Boolean to the appropriate DynamoDB Boolean format. This
returns an object that describes the DynamoDB attribute value.

```
Input:      util.dynamodb.toBoolean(true)
Output:     { "BOOL" : true }
```

## toNull utils

**`util.dynamodb.toNull()`**

Returns a null in DynamoDB null format. This returns an object that
describes the DynamoDB attribute value.

```
Input:      util.dynamodb.toNull()
Output:     { "NULL" : null }
```

## toList utils

**`util.dynamodb.toList(List)`**

Converts a list of objects to the DynamoDB list format. Each item in the
list is also converted to its appropriate DynamoDB format. It's opinionated
about how it represents some of the nested objects: e.g., it will use
lists ("L") rather than sets ("SS", "NS", "BS"). This returns an object
that describes the DynamoDB attribute value.

```
Input:      util.dynamodb.toList([ "foo", 123, { "bar" : "baz" } ])
Output:     {
               "L" : [
                   { "S" : "foo" },
                   { "N" : 123 },
                   {
                       "M" : {
                           "bar" : { "S" : "baz" }
                       }
                   }
               ]
           }
```

## toMap utils

**`util.dynamodb.toMap(Map)`**

Converts a map to the DynamoDB map format. Each value in the map is also
converted to its appropriate DynamoDB format. It's opinionated about how it
represents some of the nested objects: e.g., it will use lists ("L")
rather than sets ("SS", "NS", "BS"). This returns an object that
describes the DynamoDB attribute value.

```
Input:      util.dynamodb.toMap({ "foo": "bar", "baz" : 1234, "beep": [ "boop"] })
Output:     {
               "M" : {
                   "foo"  : { "S" : "bar" },
                   "baz"  : { "N" : 1234 },
                   "beep" : {
                       "L" : [
                           { "S" : "boop" }
                       ]
                   }
               }
           }
```

**`util.dynamodb.toMapValues(Map)`**

Creates a copy of the map where each value has been converted to its
appropriate DynamoDB format. It's opinionated about how it represents some
of the nested objects: e.g., it will use lists ("L") rather than sets
("SS", "NS", "BS").

```
Input:      util.dynamodb.toMapValues({ "foo": "bar", "baz" : 1234, "beep": [ "boop"] })
Output:     {
               "foo"  : { "S" : "bar" },
               "baz"  : { "N" : 1234 },
               "beep" : {
                   "L" : [
                       { "S" : "boop" }
                   ]
               }
           }
```

###### Note

This is slightly different to `util.dynamodb.toMap(Map)`
as it returns only the contents of the DynamoDB attribute value, but not
the whole attribute value itself. For example, the following
statements are exactly the same:

```
util.dynamodb.toMapValues(<map>)
util.dynamodb.toMap(<map>)("M")
```

## S3Object utils

**`util.dynamodb.toS3Object(String key, String
 bucket, String region)`**

Converts the key, bucket and region into the DynamoDB S3 Object
representation. This returns an object that describes the DynamoDB attribute
value.

```
Input:      util.dynamodb.toS3Object("foo", "bar", region = "baz")
Output:     { "S" : "{ \"s3\" : { \"key\" : \"foo", \"bucket\" : \"bar", \"region\" : \"baz" } }" }
```

**`util.dynamodb.toS3Object(String key, String
 bucket, String region, String version)`**

Converts the key, bucket, region and optional version into the DynamoDB
S3 Object representation. This returns an object that describes the DynamoDB
attribute value.

```
Input:      util.dynamodb.toS3Object("foo", "bar", "baz", "beep")
Output:     { "S" : "{ \"s3\" : { \"key\" : \"foo\", \"bucket\" : \"bar\", \"region\" : \"baz\", \"version\" = \"beep\" } }" }
```

**`util.dynamodb.fromS3ObjectJson(String)`**

Accepts the string value of a DynamoDB S3 Object and returns a map that
contains the key, bucket, region and optional version.

```
Input:      util.dynamodb.fromS3ObjectJson({ "S" : "{ \"s3\" : { \"key\" : \"foo\", \"bucket\" : \"bar\", \"region\" : \"baz\", \"version\" = \"beep\" } }" })
Output:     { "key" : "foo", "bucket" : "bar", "region" : "baz", "version" : "beep" }
```
