

# Transforming events with JSONata
<a name="eb-custom-bus-transform"></a>

To change what a target receives, set `Transformer` on `CreateSubscriber` or `UpdateSubscriber`. `Transformer.Type` `RAW`, the default, delivers the published data alone; `WITH_METADATA` delivers the data with its metadata; and `JSONATA` delivers the result of an expression, for example `{% { "orderId": $events.Data.orderId, "priority": $events.Data.priority } %}`. A subscriber whose target is a Custom Event Bus - Classic supports only `RAW`. A universal target does not use `Transformer`; it shapes its request in `UniversalTargetParameters.Input`, which takes the same expressions.


| Transformer type | Use when | Target payload | 
| --- | --- | --- | 
| RAW | The target needs the published event data | The published data, unchanged. The default. | 
| WITH\_METADATA | The target needs the data and its metadata | A JSON envelope with Data, Metadata, and SystemMetadata | 
| JSONATA | The target needs selected values or a new shape | The result of one JSONata expression per event | 

## What `$events` holds
<a name="eb-custom-bus-transform-shape"></a>

`WITH_METADATA`, `JSONATA`, and every target parameter expression read the same input object, which a JSONata expression sees as `$events`. It has three parts.

```
{
    "Data": { "orderId": "12345", "priority": "high" },
    "Metadata": { "tenant": "acme" },
    "SystemMetadata": {
        "ContentType": "application/json",
        "aws:EventId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "aws:IngestionTime": "2026-09-23T18:00:00Z",
        "aws:DeliveryType": "LIVE"
    }
}
```
+ `Data` is the published data and keeps its JSON type: an object, array, string, number, Boolean, or null. For `PutRawEvents` it is the entry's `Data` value, so an order identifier is at `$events.Data.orderId`. For `PutEvents` it is the whole EventBridge envelope, with `version`, `id`, `detail-type`, `source`, `account`, `time`, `region`, `resources`, and `detail`, so the same identifier is at `$events.Data.detail.orderId`. For `application/octet-stream` it is a Base64 string; see [Transforming binary data](#eb-custom-bus-transform-binary).
+ `Metadata` is the string-to-string map the producer set with `PutRawEvents`. `PutEvents` takes no metadata, so for its events the map is empty.
+ `SystemMetadata` holds the fields EventBridge assigns. Every value is a string. EventBridge omits an optional field that has no value, and an omitted field evaluates as `undefined` in JSONata; only `aws:DeliveryType` is always present. `ContentType` keeps the published value, so Avro and Protobuf data that EventBridge decoded to JSON still shows `application/avro` or `application/protobuf` here, and a `PutEvents` event shows `application/eventbridge+json`. For every field, see [SystemMetadata fields](eb-custom-bus-addressing.md#eb-custom-bus-addressing-system).

Quote a field name that contains a colon, as in `$events.SystemMetadata."aws:EventId"`.

## Building a target payload with JSONata
<a name="eb-custom-bus-transform-jsonata"></a>

Set `Transformer.Type` to `JSONATA` and put one complete expression, enclosed in `{%` and `%}`, in `JsonataConfiguration.Expression`. For a `PutRawEvents` entry whose data is `{"orderId": "12345", "priority": "high", "items": [...]}`, the following transformer delivers only the two named fields.

```
{
    "Transformer": {
        "Type": "JSONATA",
        "JsonataConfiguration": {
            "Expression": "{% {\"orderId\": $events.Data.orderId, \"priority\": $events.Data.priority} %}"
        }
    }
}
```

The target receives `{"orderId": "12345", "priority": "high"}`. EventBridge evaluates the expression once for each event, before batching. The result's type decides what the target receives.


| Expression result | Target payload | 
| --- | --- | 
| String | The string, without JSON quotation marks | 
| Object or array | The serialized JSON object or array. A null nested inside it stays JSON null. | 
| Number or Boolean | The serialized JSON value | 
| null or undefined | A transformation failure; see [Limits and failures](#eb-custom-bus-transform-limits) | 

## Transforming binary data
<a name="eb-custom-bus-transform-binary"></a>

When `SystemMetadata.ContentType` is `application/octet-stream`, EventBridge stores the published bytes without parsing them and exposes them to an expression as a Base64 string in `$events.Data`. The bytes of `hello` arrive as `$events.Data = "aGVsbG8="`. EventBridge does not parse that string as JSON even when the decoded bytes are JSON text, so check `ContentType` before you interpret `Data`, and use `$base64decode($events.Data)` only when the original bytes are text.

```
{% {
    "contentType": $events.SystemMetadata.ContentType,
    "base64Data": $events.Data
} %}
```

The transformer type decides how the bytes reach the target. Only `RAW` can forward the original byte array.


| Transformer type | What the target receives | 
| --- | --- | 
| RAW | The original bytes, for Kinesis, Firehose, API Gateway, and Custom Event Bus targets. Base64 text, for Amazon SQS and Amazon SNS targets. A JSON string containing the Base64 text, for Lambda, Step Functions, Custom Event Bus - Classic, and API destination targets; a batched Lambda or Step Functions invocation receives an array of those strings. | 
| WITH\_METADATA | The envelope as UTF-8 JSON, with Data holding the Base64 text | 
| JSONATA | The expression result as UTF-8 text or JSON; the expression reads the Base64 text | 

A transformer cannot set `ContentType`. When the target is another Custom Event Bus, EventBridge copies the published value, except that Avro and Protobuf data is delivered as JSON and so arrives as `application/json`.

## Using JSONata in target parameters
<a name="eb-custom-bus-transform-parameters"></a>

A target parameter in `InvokeConfiguration`, such as `SqsParameters.MessageGroupId`, holds either a literal value or one complete JSONata expression enclosed in `{%` and `%}`. EventBridge does not evaluate an expression embedded inside a longer string. Target parameter expressions read the original input object, not the payload that `Transformer` produced. The following Amazon SQS parameters take the FIFO values from each event.

```
{
    "InvokeConfiguration": {
        "TargetArn": "arn:aws:sqs:us-east-1:111122223333:orders.fifo",
        "RoleArn": "arn:aws:iam::111122223333:role/SubscriberTargetRole",
        "SqsParameters": {
            "MessageGroupId": "{% $events.Data.customerId %}",
            "MessageDeduplicationId": "{% $events.SystemMetadata.\"aws:EventId\" %}"
        }
    }
}
```

What `$events` holds depends on the parameter. Parameters that EventBridge resolves per event see one input object. Parameters that it resolves once per target invocation see an array of input objects, one per event in the batch, so the first event is `$events[0].Data`.


| Parameters | `$events` holds | 
| --- | --- | 
| SqsParameters, SnsParameters, KinesisParameters, HttpParameters, and EventBusV2Parameters.Metadata | One input object, per event | 
| LambdaParameters, StepFunctionsParameters, and EventBusV2Parameters.DeduplicationConfiguration | An array of input objects, per invocation | 
| UniversalTargetParameters.Input | An array of input objects, per invocation | 

A target parameter expression must return a string, unless the field defines another type; `UniversalTargetParameters.Input` can return any JSON value that forms the API request. In a map-valued parameter, both the keys and the string values can be expressions: `SqsParameters.MessageAttributes.{{name}}.StringValue`, `SqsParameters.MessageSystemAttributes.{{name}}.StringValue`, `SnsParameters.MessageAttributes.{{name}}.StringValue`, `HttpParameters.QueryStringParameters.{{key}}`, and `EventBusV2Parameters.Metadata.{{key}}`. The `BinaryValue` of an Amazon SQS or Amazon SNS message attribute is a literal Base64 value that EventBridge never evaluates, so `"BinaryValue": "AQID"` reaches the target as the bytes `0x01 0x02 0x03`; use `StringValue` for an expression.

For an API Gateway target, each `HttpParameters.HeaderParameters` key must be a literal; an API destination target also permits expressions in header keys. EventBridge rejects a header that would override request signing: `Authorization`, `Host`, and any header that begins with `X-Amz`. Every `$now()` and `$millis()` call within one resolution of a subscriber's parameters returns the same timestamp.

## Functions beyond standard JSONata
<a name="eb-custom-bus-transform-functions"></a>

In addition to the standard JSONata library, six functions are available.


| Function | Result | 
| --- | --- | 
| $hash(input, algorithm) | Lowercase hex digest. algorithm is case-sensitive: MD5, SHA-1, SHA-256, SHA-384, or SHA-512 | 
| $uuid() | A version 4 UUID | 
| $parse(jsonString) | The parsed JSON; an error if the string is not valid JSON | 
| $partition(array, chunkSize) | The array split into chunks | 
| $range(start, end, delta) | A numeric range; all three arguments are required, and the result is capped at 10,000,000 elements | 
| $random(seed) | A number in [0, 1); the same seed gives the same number | 

The `$eval` function is not available.

## Limits and failures
<a name="eb-custom-bus-transform-limits"></a>

A `Transformer` expression and each target parameter expression can be up to 8,192 characters; a universal target's `Input` expression up to 262,144. EventBridge checks the syntax when you create or update the subscriber and rejects an invalid expression with `InvalidInputException`. At delivery, an expression can run for one second, use a stack depth of 100, and allocate 10 MiB.

An expression that throws, exceeds those limits, or produces `null` or `undefined` fails the delivery of that event. EventBridge retries under the subscriber's `RetryPolicy`, then sends the event to the on-failure destination if one is configured. The `EventTransformationFailures` metric counts each failure, an `EVENT_TRANSFORMATION_FAILURE` log record carries the error, and the dead-letter record's `errorCode` is `INPUT_TRANSFORMATION_FAILURE`. See [Observability for the Custom Event Bus: metrics, logs, and CloudTrail](eb-custom-bus-observability.md) and [Retry policies and dead-letter queues](eb-custom-bus-retry.md).