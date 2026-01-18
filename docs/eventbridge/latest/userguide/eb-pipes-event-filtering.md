# Event filtering in Amazon EventBridge Pipes

With EventBridge Pipes, you can filter a given source's events and process only a subset of them.
This filtering works in the same way as filtering on an EventBridge event bus or Lambda event source mapping, by using event patterns.
For more information about event patterns, see [Creating Amazon EventBridge event patterns](eb-event-patterns.md "eb-event-patterns.md").

A filter criteria `FilterCriteria` object is a structure that consists of a list
of filters (`Filters`). Each filter is a structure that defines a filtering
pattern (`Pattern`). A `Pattern` is a string representation of a JSON
filter rule. A `FilterCriteria` object looks like the following example:

```
{
  "Filters": [
    {"Pattern": "{ \"Metadata1\": [ pattern1 ], \"data\": { \"Data1\": [ pattern2 ] }}"
    }
  ]
}
```

For added clarity, here is the value of the filter's `Pattern` expanded in plain JSON:

```
{
  "Metadata1": [ pattern1 ],
  "data": {"Data1": [ pattern2 ]}
}
```

Amazon Kinesis, Amazon MQ, Amazon MSK, and self managed Apache Kafka apply Base64 encoding to the payload, but not the metadata fields. For example, suppose your Kinesis stream contains an event like this:

```
{
  "kinesisSchemaVersion": "1.0",
  "partitionKey": "1",
  "sequenceNumber": "49590338271490256608559692538361571095921575989136588898",
  "data": {"City": "Seattle",
    "State": "WA",
    "Temperature": "46",
    "Month": "December"
  },
  "approximateArrivalTimestamp": 1545084650.987
}
```

When the event flows through your pipe, it'll look like the following with the `data` field base64-encoded:

```
{
  "kinesisSchemaVersion": "1.0",
  "partitionKey": "1",
  "sequenceNumber": "49590338271490256608559692538361571095921575989136588898",
  "data": "SGVsbG8sIHRoaXMgaXMgYSB0ZXN0Lg==",
  "approximateArrivalTimestamp": 1545084650.987,
  "eventSource": "aws:kinesis",
  "eventVersion": "1.0",
  "eventID": "shardId-000000000006:49590338271490256608559692538361571095921575989136588898",
  "eventName": "aws:kinesis:record",
  "invokeIdentityArn": "arn:aws:iam::123456789012:role/lambda-role",
  "awsRegion": "us-east-2",
  "eventSourceARN": "arn:aws:kinesis:us-east-2:123456789012:stream/lambda-stream"
}
```

When you're creating event filters, EventBridge Pipes can access event content. This content is
either JSON-escaped, such as the Amazon SQS `body` field, or base64-encoded, such as the
Kinesis `data` field. If your data is valid JSON, your input templates or JSON paths for
target parameters can reference the content directly, as EventBridge Pipes will automatically decode it. For example, if a Kinesis event source is
valid JSON, you can reference a variable using `<$.data.someKey>`.

Continuing our example, to filter on the non-encoded `partitionKey` metadata outside the `data` object and the base64 encoded `City` property inside the `data` object, you would use the following filter:

```
{
  "partitionKey": [ "1" ],
  "data": {
    "City": [ "Seattle" ]
  }
}
```

When creating event patterns, you can filter based on the fields sent by the source API, and
not on fields added by the polling operation. The following fields can't be used in event
patterns:

- `awsRegion`
- `eventSource`
- `eventSourceARN`
- `eventVersion`
- `eventID`
- `eventName`
- `invokeIdentityArn`
- `eventSourceKey`
  The following sections explain filtering behavior for each supported event source type.

## Filtering Amazon SQS messages

If an Amazon SQS message doesn't satisfy your filter criteria, EventBridge automatically removes the
message from the queue. You don't have to delete these messages manually in Amazon SQS. Connecting multiple pipes to
one SQS queue is unlikely to be a useful setup - the pipes would be competing for messages that'll be dropped if unmatched.

An Amazon SQS message body can contain any string, not just JSON. EventBridge Pipes expects your
`FilterCriteria` format to match the format of the incoming messages, either valid JSON or a plain string.
If there is a mismatch, EventBridge Pipes drops the message. If your `FilterCriteria` don't include
`body`, meaning you filter only by metadata, EventBridge Pipes skips this check. The following table
summarizes the evaluation:

| Filter pattern format        | Incoming format | Result                                             |
| ---------------------------- | --------------- | -------------------------------------------------- |
| Plain string                 | Plain string    | EventBridge filters based on your filter criteria. |
| Plain string                 | Valid JSON      | EventBridge drops the message.                     |
| Valid JSON                   | Plain string    | EventBridge drops the message.                     |
| Valid JSON                   | Valid JSON      | EventBridge filters based on your filter criteria. |
| No filter pattern for `body` | Plain string    | EventBridge filters based on your filter criteria. |
| No filter pattern for `body` | Valid JSON      | EventBridge filters based on your filter criteria. |

## Filtering Kinesis and DynamoDB messages

After your filter criteria processes a Kinesis or DynamoDB record, the streams iterator advances
past this record. If the record doesn't satisfy your filter criteria, you don't have to delete
the record manually from your event source. After the retention period, Kinesis and DynamoDB
automatically delete these old records. If you want records to be deleted sooner, see [Changing the Data Retention
Period](../../../kinesis/latest/dev/kinesis-extended-retention.md "../../../kinesis/latest/dev/kinesis-extended-retention.md").

To properly filter events from stream event sources, both the data field and your filter criteria for the data
field must be in valid JSON format. (For Kinesis, the data field is `data`. For DynamoDB, the data field is
`dynamodb`.) If either field isn't in a valid JSON format, EventBridge drops the message or throws an
exception. The following table summarizes the specific behavior:

| Filter pattern format                                           | Incoming format | Result                                                                                                                |
| --------------------------------------------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------- |
| Valid JSON                                                      | Valid JSON      | EventBridge filters based on your filter criteria.                                                                    |
| Valid JSON                                                      | Non-JSON        | EventBridge drops the message.                                                                                        |
| No filter pattern for `data` (Kinesis) or `dynamodb` (DynamoDB) | Valid JSON      | EventBridge filters based on your filter criteria.                                                                    |
| No filter pattern for `data` (Kinesis) or `dynamodb` (DynamoDB) | Non-JSON        | EventBridge filters based on your filter criteria.                                                                    |
| Non-JSON                                                        | Any             | EventBridge throws an exception at the time of Pipe creation or update. The filter pattern must be valid JSON format. |

## Filtering Amazon Managed Streaming for Apache Kafka, self managed Apache Kafka, and Amazon MQ messages

###### Note

After you attach filter criteria to a pipe with an Apache Kafka or Amazon MQ event source, it can take up to 15 minutes to apply your filtering rules to events.

For [Amazon MQ sources](eb-pipes-mq.md "eb-pipes-mq.md"), the message field is `data`. For Apache Kafka sources ([Amazon MSK](eb-pipes-msk.md "eb-pipes-msk.md") and
[self managed Apache Kafka](eb-pipes-kafka.md "eb-pipes-kafka.md")), there are two message fields: `key` and `value`.

EventBridge drops messages that don't match all fields included in the filter. For Apache Kafka, EventBridge commits offsets for matched and unmatched messages after successfully
invoking the target. For Amazon MQ, EventBridge acknowledges matched messages after successfully invoking the function and acknowledges unmatched messages when filtering them.

Apache Kafka and Amazon MQ messages must be UTF-8 encoded strings, either plain strings or in JSON format. That's because EventBridge decodes Apache Kafka and Amazon MQ byte arrays into UTF-8 before
applying filter criteria. If your messages use another encoding, such as UTF-16 or ASCII, or if the message format doesn't match the `FilterCriteria` format,
EventBridge processes metadata filters only. The following table summarizes the specific behavior:

| Filter pattern format                                                        | Incoming format        | Result                                                                                                                 |
| ---------------------------------------------------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Plain string                                                                 | Plain string           | EventBridge filters based on your filter criteria.                                                                     |
| Plain string                                                                 | Valid JSON             | EventBridge filters on metadata only, ignoring the `data` field (Amazon MQ) or `key` and `value` fields (Apache Kafka) |
| Valid JSON                                                                   | Plain string           | EventBridge filters on metadata only, ignoring the `data` field (Amazon MQ) or `key` and `value` fields (Apache Kafka) |
| Valid JSON                                                                   | Valid JSON             | EventBridge filters based on your filter criteria.                                                                     |
| No filter pattern for `data` (Amazon MQ) or `key` and `value` (Apache Kafka) | Plain string           | EventBridge filters on metadata only, ignoring the `data` field (Amazon MQ) or `key` and `value` fields (Apache Kafka) |
| No filter pattern for `data` (Amazon MQ) or `key` and `value` (Apache Kafka) | Valid JSON             | EventBridge filters on metadata only, ignoring the `data` field (Amazon MQ) or `key` and `value` fields (Apache Kafka) |
| Any                                                                          | Non-UTF encoded string | EventBridge filters on metadata only, ignoring the `data` field (Amazon MQ) or `key` and `value` fields (Apache Kafka) |

## Differences between Lambda ESM and EventBridge Pipes

When filtering events, Lambda ESM and EventBridge Pipes operate generally the same way. The main difference is that
`eventSourceKey` field isn't present in ESM payloads.

## Using comparison operators in pipe filters

Comparison operators enable you to construct event patterns that match against field values in events.

For a complete list of the comparison operators supported for use in pipe filters, see [Comparison operators](eb-create-pattern-operators.md "eb-create-pattern-operators.md").
