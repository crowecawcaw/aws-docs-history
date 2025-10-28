# Amazon EventBridge Pipes input transformation

Amazon EventBridge Pipes support optional input transformers when passing data to the enrichment and
the target. You can use Input transformers to reshape the JSON event input payload to serve the
needs of the enrichment or target service. For Amazon API Gateway and API destinations, this is how you
shape the input event to the RESTful model of your API. Input transformers are modeled as an
`InputTemplate` parameter. They can be free text, a JSON path to the event payload,
or a JSON object that includes inline JSON paths to the event payload. For enrichment, the event
payload is coming from the source. For targets, the event payload is what is returned from the
enrichment, if one is configured on the pipe. In addition to the service-specific data in the
event payload, you can use [reserved variables](#input-transform-reserved "#input-transform-reserved") in
your `InputTemplate` to reference data for your pipe.

To access items in an array, use square bracket notation.

###### Note

EventBridge does not support all JSON Path syntax and evaluate it at runtime.
Supported syntax includes:

- dot notation (for example,`$.detail`)
- dashes
- underscores
- alphanumeric characters
- array indices
- wildcards (\*)
  The following are sample `InputTemplate` parameters referencing an Amazon SQS event payload:

**Static string**

```
InputTemplate: "Hello, sender"
```

**JSON Path**

```
InputTemplate: <$.attributes.SenderId>
```

**Dynamic string**

```
InputTemplate: "Hello, <$.attributes.SenderId>"
```

**Static JSON**

```
InputTemplate: >
{
  "key1": "value1",
  "key2": "value2",
  "key3": "value3",
}
```

**Dynamic JSON**

```
InputTemplate: >
{
  "key1": "value1"
  "key2": <$.body.key>,
  "d": <aws.pipes.event.ingestion-time>
}
```

Using square bracket notation to access an item in an array:

```
InputTemplate: >
{
  "key1": "value1"
  "key2": <$.body.Records[3]>,
  "d": <aws.pipes.event.ingestion-time>
}
```

###### Note

EventBridge replaces input transformers at runtime to ensure a valid JSON output.
Because of this, put quotes around variables that refer to JSON path parameters, but do not
put quotes around variables that refer to JSON objects or arrays.

## Reserved variables

Input templates can use the following reserved variables:

- `<aws.pipes.pipe-arn>` – The Amazon Resource Name (ARN) of the
  pipe.
- `<aws.pipes.pipe-name>` – The name of the pipe.
- `<aws.pipes.source-arn>` – The ARN of the event source of the pipe.
- `<aws.pipes.enrichment-arn>` – The ARN of the enrichment of the pipe.
- `<aws.pipes.target-arn>` – The ARN of the target of the pipe.
- `<aws.pipes.event.ingestion-time>` – The time at which the event was
  received by the input transformer. This is an ISO 8601 timestamp. This time is different
  for the enrichment input transformer and the target input transformer, depending on when
  the enrichment completed processing the event.
- `<aws.pipes.event>` – The event as received by the input transformer.

For an enrichment input transformer, this is the event from the source. This contains the original payload from the source,
plus additional service-specific metadata. See the topics in [Amazon EventBridge Pipes sources](eb-pipes-event-source.md "eb-pipes-event-source.md") for service-specific examples.

For a target input transformer, this is the event returned by the enrichment, if one
is configured, with no additional metadata. As such, an enrichment-returned payload may be
non-JSON. If no enrichment is configured on the pipe, this is the event from the source
with metadata.

- `<aws.pipes.event.json>` – The same as `aws.pipes.event`,
  but the variable only has a value if the original payload, either from the source or returned by the enrichment, is JSON.
  If the pipe has an encoded field, such as the Amazon SQS `body` field or the Kinesis `data`, those fields are decoded and turned into valid JSON.
  Because it isn't escaped, the variable can only be used as a value for a JSON field. For more information, see [Implicit body data parsing](#input-transform-implicit "#input-transform-implicit").

## Input transform example

The following is an example Amazon EC2 event that we can use as our _sample event_.

```

{
  "version": "0",
  "id": "7bf73129-1428-4cd3-a780-95db273d1602",
  "detail-type": "EC2 Instance State-change Notification",
  "source": "aws.ec2",
  "account": "123456789012",
  "time": "2015-11-11T21:29:54Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:ec2:us-east-1:123456789012:instance/i-abcd1111"
  ],
  "detail": {
    "instance-id": "i-0123456789",
    "state": "RUNNING"
  }
}

```

Let's use the following JSON as our _Transformer_.

```
{
  "instance" : <$.detail.instance-id>,
  "state": <$.detail.state>,
  "pipeArn" : <aws.pipes.pipe-arn>,
  "pipeName" : <aws.pipes.pipe-name>,
  "originalEvent" : <aws.pipes.event.json>
}
```

The following will be the resulting _Output_:

```
{
  "instance" : "i-0123456789",
  "state": "RUNNING",
  "pipeArn" : "arn:aws:pipe:us-east-1:123456789012:pipe/example",
  "pipeName" : "example",
  "originalEvent" : {
    ... // commented for brevity
  }
}
```

## Implicit body data parsing

The following fields in the incoming payload may be JSON-escaped, such
as the Amazon SQS `body` object, or base64-encoded, such as the Kinesis `data`
object. For both [filtering](eb-pipes-event-filtering.md "eb-pipes-event-filtering.md") and input transformation, EventBridge transforms these fields into valid JSON so sub-values can be referenced directly.
For example, `<$.data.someKey>` for Kinesis.

To have the target receive the original payload without any additional metadata, use an
input transformer with this body data, specific to the source. For example,
`<$.body>` for Amazon SQS, or `<$.data>` for Kinesis. If the
original payload is a valid JSON string (for example `{"key": "value"}`), then use
of the input transformer with source specific body data will result in the quotes within the
original source payload being removed. For example, `{"key": "value"}` will become
`"{key: value}"` when delivered to the target. If your target requires valid JSON
payloads (for example, EventBridge Lambda or Step Functions), this will cause delivery failure. To have the
target receive the original source data without generating invalid JSON, wrap the source body
data input transformer in JSON. For example, `{"data": <$.data>}`.

Implicit body parsing can also be used to dynamically populate values for most pipe target or enrichment parameters.
For more information, see [Dynamic path parameters](eb-pipes-event-target.md#pipes-targets-dynamic-parms "eb-pipes-event-target.md#pipes-targets-dynamic-parms")

###### Note

If the original payload is valid JSON, this field will contain the unescaped,
non-base64-encoded JSON. However, if the payload is not valid JSON, EventBridge base64-encodes for
the fields listed below, with the exception of Amazon SQS.

- Active MQ – `data`
- Kinesis – `data`
- Amazon MSK – `key` and `value`
- Rabbit MQ – `data`
- Self managed Apache Kafka; – `key` and `value`
- Amazon SQS – `body`

## Common issues with transforming

input

These are some common issues when transforming input in EventBridge pipes:

- For Strings, quotes are required.
- There is no validation when creating JSON path for your template.
- If you specify a variable to match a JSON path that doesn't exist in the event, that
  variable isn't created and won't appear in the output.
- JSON properties like `aws.pipes.event.json` can only be used as the value of a JSON field, not inline in other strings.
- EventBridge doesn't escape values extracted by _Input Path_,
  when populating the _Input Template_ for a target.
- If a JSON path references a JSON object or array, but the variable is referenced in a string, EventBridge removes any internal quotes to ensure a valid string.
  For example, "Body is <$.body>" would result in EventBridge removing quotes from the object.

Therefore, if you want to output a JSON object based on a single JSON path variable, you must place it as a key. In this example, `{"body": <$.body>}`.

- Quotes are not required for variables that represent strings. They are permitted, but EventBridge Pipes automatically adds quotes to string variable values during transformation,
  to ensure the transformation output is valid JSON. EventBridge Pipes does not add quotes to variables that represent JSON objects or arrays. Do not add quotes for variables that
  represent JSON objects or arrays.

For example, the following input template includes variables that represent both strings and JSON objects:

```
{
  "pipeArn" : <aws.pipes.pipe-arn>,
  "pipeName" : <aws.pipes.pipe-name>,
  "originalEvent" : <aws.pipes.event.json>
}
```

Resulting in valid JSON with proper quotation:

```
{
  "pipeArn" : "arn:aws:events:us-east-2:123456789012:pipe/example",
  "pipeName" : "example",
  "originalEvent" : {
    ... // commented for brevity
  }
}
```

- For Lambda or Step Functions enrichments or targets, batches are delivered to the target as JSON arrays, even if the batch size is 1.
  However, input transformers will still be applied to individual records in the JSON Array, not the array as a whole.
  For more information, see [Amazon EventBridge Pipes batching and concurrency](eb-pipes-batching-concurrency.md "eb-pipes-batching-concurrency.md").
