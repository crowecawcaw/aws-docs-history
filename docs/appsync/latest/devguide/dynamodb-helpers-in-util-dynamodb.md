# DynamoDB helpers in

$util.dynamodb

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please
consider using the APPSYNC_JS runtime and its guides [here](resolver-reference-js-version.md "resolver-reference-js-version.md").

`$util.dynamodb` contains helper methods that make it easier to write and
read data to Amazon DynamoDB, such as automatic type mapping and formatting. These methods are
designed to make mapping primitive types and Lists to the proper DynamoDB input format
automatically, which is a `Map` of the format `{ "TYPE" : VALUE
 }`.

For example, previously, a request mapping template to create a new item in DynamoDB might
have looked like this:

```
{
    "version" : "2017-02-28",
    "operation" : "PutItem",
    "key": {
        "id" : { "S" : "$util.autoId()" }
    },
    "attributeValues" : {
         "title" : { "S" : $util.toJson($ctx.args.title) },
         "author" : { "S" : $util.toJson($ctx.args.author) },
         "version" : { "N", $util.toJson($ctx.args.version) }
    }
}
```

If we wanted to add fields to the object we would have to update the GraphQL query in
the schema, as well as the request mapping template. However, we can now restructure our
request mapping template so it automatically picks up new fields added in our schema and
adds them to DynamoDB with the correct types:

```
{
    "version" : "2017-02-28",
    "operation" : "PutItem",
    "key": {
        "id" : $util.dynamodb.toDynamoDBJson($util.autoId())
    },
    "attributeValues" : $util.dynamodb.toMapValuesJson($ctx.args)
}
```

In the previous example, we are using the
`$util.dynamodb.toDynamoDBJson(...)` helper to automatically take the
generated id and convert it to the DynamoDB representation of a string attribute. We then take
all the arguments and convert them to their DynamoDB representations and output them to the
`attributeValues` field in the template.

Each helper has two versions: a version that returns an object (for example,
`$util.dynamodb.toString(...)`), and a version that returns the object as a
JSON string (for example, `$util.dynamodb.toStringJson(...)`). In the previous
example, we used the version that returns the data as a JSON string. If you want to
manipulate the object before it's used in the template, you can choose to return an object
instead, as shown following:

```
{
    "version" : "2017-02-28",
    "operation" : "PutItem",
    "key": {
        "id" : $util.dynamodb.toDynamoDBJson($util.autoId())
    },

    #set( $myFoo = $util.dynamodb.toMapValues($ctx.args) )
    #set( $myFoo.version = $util.dynamodb.toNumber(1) )
    #set( $myFoo.timestamp = $util.dynamodb.toString($util.time.nowISO8601()))

    "attributeValues" : $util.toJson($myFoo)
}
```

In the previous example, we are returning the converted arguments as a map instead of a
JSON string, and are then adding the `version` and `timestamp` fields
before finally outputting them to the `attributeValues` field in the template
using `$util.toJson(...)`.

The JSON version of each of the helpers is equivalent to wrapping the non-JSON version
in `$util.toJson(...)`. For example, the following statements are exactly the
same:

```
$util.toStringJson("Hello, World!")
$util.toJson($util.toString("Hello, World!"))
```

## toDynamoDB

**`$util.dynamodb.toDynamoDB(Object) : Map`**

General object conversion tool for DynamoDB that converts input objects
to the appropriate DynamoDB representation. It's opinionated about how it
represents some types: e.g., it will use lists ("L") rather than sets
("SS", "NS", "BS"). This returns an object that describes the DynamoDB
attribute value.

**String example**

```
Input:      $util.dynamodb.toDynamoDB("foo")
Output:     { "S" : "foo" }
```

**Number example**

```
Input:      $util.dynamodb.toDynamoDB(12345)
Output:     { "N" : 12345 }
```

**Boolean example**

```
Input:      $util.dynamodb.toDynamoDB(true)
Output:     { "BOOL" : true }
```

**List example**

```
Input:      $util.dynamodb.toDynamoDB([ "foo", 123, { "bar" : "baz" } ])
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
Input:      $util.dynamodb.toDynamoDB({ "foo": "bar", "baz" : 1234, "beep": [ "boop"] })
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

\***\*`$util.dynamodb.toDynamoDBJson(Object) :
 String`\*\***

The same as `$util.dynamodb.toDynamoDB(Object) : Map`, but
returns the DynamoDB attribute value as a JSON encoded string.

## toString utils

\***\*`$util.dynamodb.toString(String) :
 String`\*\***

Converts an input string to the DynamoDB string format. This returns an
object that describes the DynamoDB attribute value.

```
Input:      $util.dynamodb.toString("foo")
Output:     { "S" : "foo" }
```

**`$util.dynamodb.toStringJson(String) : Map`**

The same as `$util.dynamodb.toString(String) : String`, but
returns the DynamoDB attribute value as a JSON encoded string.

**`$util.dynamodb.toStringSet(List<String>) : Map`**

Converts a list with Strings to the DynamoDB string set format. This
returns an object that describes the DynamoDB attribute value.

```
Input:      $util.dynamodb.toStringSet([ "foo", "bar", "baz" ])
Output:     { "SS" : [ "foo", "bar", "baz" ] }
```

**`$util.dynamodb.toStringSetJson(List<String>) : String`**

The same as `$util.dynamodb.toStringSet(List<String>) :
 Map`, but returns the DynamoDB attribute value as a JSON encoded
string.

## toNumber utils

**`$util.dynamodb.toNumber(Number) : Map`**

Converts a number to the DynamoDB number format. This returns an object
that describes the DynamoDB attribute value.

```
Input:      $util.dynamodb.toNumber(12345)
Output:     { "N" : 12345 }
```

**`$util.dynamodb.toNumberJson(Number) : String`**

The same as `$util.dynamodb.toNumber(Number) : Map`, but
returns the DynamoDB attribute value as a JSON encoded string.

**`$util.dynamodb.toNumberSet(List<Number>) : Map`**

Converts a list of numbers to the DynamoDB number set format. This
returns an object that describes the DynamoDB attribute value.

```
Input:      $util.dynamodb.toNumberSet([ 1, 23, 4.56 ])
Output:     { "NS" : [ 1, 23, 4.56 ] }
```

**`$util.dynamodb.toNumberSetJson(List<Number>) : String`**

The same as `$util.dynamodb.toNumberSet(List<Number>) :
 Map`, but returns the DynamoDB attribute value as a JSON encoded
string.

## toBinary utils

**`$util.dynamodb.toBinary(String) : Map`**

Converts binary data encoded as a base64 string to DynamoDB binary
format. This returns an object that describes the DynamoDB attribute
value.

```
Input:      $util.dynamodb.toBinary("foo")
Output:     { "B" : "foo" }
```

**`$util.dynamodb.toBinaryJson(String) : String`**

The same as `$util.dynamodb.toBinary(String) : Map`, but
returns the DynamoDB attribute value as a JSON encoded string.

**`$util.dynamodb.toBinarySet(List<String>) : Map`**

Converts a list of binary data encoded as base64 strings to DynamoDB
binary set format. This returns an object that describes the DynamoDB
attribute value.

```
Input:      $util.dynamodb.toBinarySet([ "foo", "bar", "baz" ])
Output:     { "BS" : [ "foo", "bar", "baz" ] }
```

**`$util.dynamodb.toBinarySetJson(List<String>) : String`**

The same as `$util.dynamodb.toBinarySet(List<String>) :
 Map`, but returns the DynamoDB attribute value as a JSON encoded
string.

## toBoolean utils

**`$util.dynamodb.toBoolean(Boolean) : Map`**

Converts a Boolean to the appropriate DynamoDB Boolean format. This
returns an object that describes the DynamoDB attribute value.

```
Input:      $util.dynamodb.toBoolean(true)
Output:     { "BOOL" : true }
```

**`$util.dynamodb.toBooleanJson(Boolean) : String`**

The same as `$util.dynamodb.toBoolean(Boolean) : Map`, but
returns the DynamoDB attribute value as a JSON encoded string.

## toNull utils

**`$util.dynamodb.toNull() : Map`**

Returns a null in DynamoDB null format. This returns an object that
describes the DynamoDB attribute value.

```
Input:      $util.dynamodb.toNull()
Output:     { "NULL" : null }
```

**`$util.dynamodb.toNullJson() : String`**

The same as `$util.dynamodb.toNull() : Map`, but returns
the DynamoDB attribute value as a JSON encoded string.

## toList utils

\***\*`$util.dynamodb.toList(List) :
 Map`\*\***

Converts a list of objects to the DynamoDB list format. Each item in the
list is also converted to its appropriate DynamoDB format. It's opinionated
about how it represents some of the nested objects: e.g., it will use
lists ("L") rather than sets ("SS", "NS", "BS"). This returns an object
that describes the DynamoDB attribute value.

```
Input:      $util.dynamodb.toList([ "foo", 123, { "bar" : "baz" } ])
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

**`$util.dynamodb.toListJson(List) : String`**

The same as `$util.dynamodb.toList(List) : Map`, but
returns the DynamoDB attribute value as a JSON encoded string.

## toMap utils

**`$util.dynamodb.toMap(Map) : Map`**

Converts a map to the DynamoDB map format. Each value in the map is also
converted to its appropriate DynamoDB format. It's opinionated about how it
represents some of the nested objects: e.g., it will use lists ("L")
rather than sets ("SS", "NS", "BS"). This returns an object that
describes the DynamoDB attribute value.

```
Input:      $util.dynamodb.toMap({ "foo": "bar", "baz" : 1234, "beep": [ "boop"] })
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

**`$util.dynamodb.toMapJson(Map) : String`**

The same as `$util.dynamodb.toMap(Map) : Map`, but returns
the DynamoDB attribute value as a JSON encoded string.

**`$util.dynamodb.toMapValues(Map) : Map`**

Creates a copy of the map where each value has been converted to its
appropriate DynamoDB format. It's opinionated about how it represents some
of the nested objects: e.g., it will use lists ("L") rather than sets
("SS", "NS", "BS").

```
Input:      $util.dynamodb.toMapValues({ "foo": "bar", "baz" : 1234, "beep": [ "boop"] })
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

This is slightly different to `$util.dynamodb.toMap(Map) :
 Map` as it returns only the contents of the DynamoDB attribute
value, but not the whole attribute value itself. For example, the
following statements are exactly the same:

```
$util.dynamodb.toMapValues($map)
$util.dynamodb.toMap($map).get("M")
```

**`$util.dynamodb.toMapValuesJson(Map) : String`**

The same as `$util.dynamodb.toMapValues(Map) : Map`, but
returns the DynamoDB attribute value as a JSON encoded string.

## S3Object utils

**`$util.dynamodb.toS3Object(String key, String bucket, String region) :
 Map`**

Converts the key, bucket and region into the DynamoDB S3 Object
representation. This returns an object that describes the DynamoDB attribute
value.

```
Input:      $util.dynamodb.toS3Object("foo", "bar", region = "baz")
Output:     { "S" : "{ \"s3\" : { \"key\" : \"foo", \"bucket\" : \"bar", \"region\" : \"baz" } }" }
```

**`$util.dynamodb.toS3ObjectJson(String key, String bucket, String
 region) : String`**

The same as `$util.dynamodb.toS3Object(String key, String bucket,
 String region) : Map`, but returns the DynamoDB attribute value as
a JSON encoded string.

**`$util.dynamodb.toS3Object(String key, String bucket, String region,
 String version) : Map`**

Converts the key, bucket, region and optional version into the DynamoDB
S3 Object representation. This returns an object that describes the DynamoDB
attribute value.

```
Input:      $util.dynamodb.toS3Object("foo", "bar", "baz", "beep")
Output:     { "S" : "{ \"s3\" : { \"key\" : \"foo\", \"bucket\" : \"bar\", \"region\" : \"baz\", \"version\" = \"beep\" } }" }
```

**`$util.dynamodb.toS3ObjectJson(String key, String bucket, String
 region, String version) : String`**

The same as `$util.dynamodb.toS3Object(String key, String bucket,
 String region, String version) : Map`, but returns the DynamoDB
attribute value as a JSON encoded string.

**`$util.dynamodb.fromS3ObjectJson(String) : Map`**

Accepts the string value of a DynamoDB S3 Object and returns a map that
contains the key, bucket, region and optional version.

```
Input:      $util.dynamodb.fromS3ObjectJson({ "S" : "{ \"s3\" : { \"key\" : \"foo\", \"bucket\" : \"bar\", \"region\" : \"baz\", \"version\" = \"beep\" } }" })
Output:     { "key" : "foo", "bucket" : "bar", "region" : "baz", "version" : "beep" }
```
