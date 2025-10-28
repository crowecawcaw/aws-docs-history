# Add annotations and metadata to segments with the X-Ray SDK for Node.js

###### Note

End-of-support notice – On February 25th, 2027, AWS X-Ray will discontinue support for AWS X-Ray SDKs and daemon. After February 25th, 2027, you will no longer receive updates or releases. For more information on the support timeline, see
[X-Ray SDK and daemon end of support timeline](xray-daemon-eos.md "xray-daemon-eos.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

You can record additional information about requests, the
environment, or your application with annotations and metadata. You can add annotations and
metadata to the segments that the X-Ray SDK creates, or to custom subsegments that you create.

**Annotations** are
key-value pairs with string, number, or Boolean values. Annotations are indexed for use with
[filter expressions](xray-console-filters.md "xray-console-filters.md"). Use annotations to record data
that you want to use to group traces in the console, or when calling the [`GetTraceSummaries`](../api/API_GetTraceSummaries.md "../api/API_GetTraceSummaries.md")
API.

**Metadata** are key-value
pairs that can have values of any type, including objects and lists, but are not indexed for use
with filter expressions. Use metadata to record additional data that you want stored in the trace
but don't need to use with search.

In addition to annotations and metadata, you can also [record user ID strings](#xray-sdk-nodejs-segment-userid "#xray-sdk-nodejs-segment-userid") on segments. User IDs are recorded in a
separate field on segments and are indexed for use with search.

###### Sections

- [Recording annotations with the X-Ray SDK for Node.js](#xray-sdk-nodejs-segment-annotations "#xray-sdk-nodejs-segment-annotations")
- [Recording metadata with the X-Ray SDK for Node.js](#xray-sdk-nodejs-segment-metadata "#xray-sdk-nodejs-segment-metadata")
- [Recording user IDs with the X-Ray SDK for Node.js](#xray-sdk-nodejs-segment-userid "#xray-sdk-nodejs-segment-userid")

## Recording annotations with the X-Ray SDK for Node.js

Use annotations to record information on segments or subsegments that you want indexed for search.

###### Annotation Requirements

- **Keys** – The key for an X-Ray annotation can have
  up to 500 alphanumeric characters. You cannot use spaces or symbols other
  than a dot or period ( . )
- **Values** – The value for an X-Ray annotation can have up to 1,000 Unicode
  characters.
- The number of **Annotations** – You can use up to 50 annotations per
  trace.

###### To record annotations

1. Get a reference to the current segment or subsegment.

```
var AWSXRay = require('aws-xray-sdk');
...
var document = AWSXRay.getSegment();
```

2. Call `addAnnotation` with a String key, and a Boolean, Number, or String value.

```
document.addAnnotation("mykey", "my value");
```

The following example shows how to call `putAnnotation` with a String key
that includes a dot, and a Boolean, Number, or String value.

```
document.putAnnotation("testkey.test", "my value");
```

The SDK records annotations as key-value pairs in an `annotations` object in the segment document.
Calling `addAnnotation` twice with the same key overwrites previously recorded values on the same
segment or subsegment.

To find traces that have annotations with specific values, use the
`annotation[`key`]` keyword in a [filter expression](xray-console-filters.md "xray-console-filters.md").

###### Example app.js - annotations

```
var AWS = require('aws-sdk');
var AWSXRay = require('aws-xray-sdk');
var ddb = AWSXRay.captureAWSClient(new AWS.DynamoDB());
...
app.post('/signup', function(req, res) {
    var item = {
        'email': {'S': req.body.email},
        'name': {'S': req.body.name},
        'preview': {'S': req.body.previewAccess},
        'theme': {'S': req.body.theme}
    };

    var seg = AWSXRay.getSegment();
    `seg.addAnnotation('theme', req.body.theme);`

    ddb.putItem({
      'TableName': ddbTable,
      'Item': item,
      'Expected': { email: { Exists: false } }
  }, function(err, data) {
...
```

## Recording metadata with the X-Ray SDK for Node.js

Use metadata to record information on segments or subsegments that you don't need indexed for search. Metadata
values can be strings, numbers, Booleans, or any other object that can be serialized into a JSON object or
array.

###### To record metadata

1. Get a reference to the current segment or subsegment.

```
var AWSXRay = require('aws-xray-sdk');
...
var document = AWSXRay.getSegment();
```

2. Call `addMetadata` with a string key, a Boolean, number, string, or object value, and a string
   namespace.

```
document.addMetadata("`my key`", "`my value`", "`my namespace`");
```

or

Call `addMetadata` with just a key and value.

```
document.addMetadata("`my key`", "`my value`");
```

If you don't specify a namespace, the SDK uses `default`. Calling `addMetadata` twice
with the same key overwrites previously recorded values on the same segment or subsegment.

## Recording user IDs with the X-Ray SDK for Node.js

Record user IDs on request segments to identify the user who sent the request. This operation isn’t compatible
with AWS Lambda functions because segments in Lambda environments are immutable. The `setUser` call
can be applied only to segments, not subsegments.

###### To record user IDs

1. Get a reference to the current segment or subsegment.

```
var AWSXRay = require('aws-xray-sdk');
...
var document = AWSXRay.getSegment();
```

2. Call `setUser()` with a string ID of the user who sent the request.

```
var user = 'john123';

AWSXRay.getSegment().setUser(user);
```

You can call `setUser` to record the user ID as soon as your express application starts processing
a request. If you will use the segment only to set the user ID, you can chain the calls in a single line.

###### Example app.js - user ID

```
var AWS = require('aws-sdk');
var AWSXRay = require('aws-xray-sdk');
var uuidv4 = require('uuid/v4');
var ddb = AWSXRay.captureAWSClient(new AWS.DynamoDB());
...
    `app.post('/signup', function(req, res) {
 var userId = uuidv4();
 var item = {
 'userId': {'S': userId},
 'email': {'S': req.body.email},
 'name': {'S': req.body.name}
 };

 var seg = AWSXRay.getSegment().setUser(userId);`

    ddb.putItem({
      'TableName': ddbTable,
      'Item': item,
      'Expected': { email: { Exists: false } }
  }, function(err, data) {
...
```

To find traces for a user ID, use the `user` keyword in a [filter
expression](xray-console-filters.md "xray-console-filters.md").
