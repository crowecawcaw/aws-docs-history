

# Filtering events for a subscriber
<a name="eb-custom-bus-filtering"></a>

A filter selects which events a subscriber receives. Attach a `FilterConfiguration` to the subscriber with one or more filters, each naming a `Scope` and a `Pattern` in EventBridge event pattern syntax. For example, a `DATA` filter with the pattern `{"detail":{"amount":[{"numeric":[">",500]}]}}` delivers only orders over 500 published with `PutEvents`. This page describes the filter model; for the pattern operators, see [Amazon EventBridge event patterns](eb-event-patterns.md). Subscriber filters do not support wildcard matching.

## How filtering works
<a name="eb-custom-bus-filtering-how"></a>

Each filter has two parts: a `Scope`, which is the part of the event the filter examines (`DATA`, `METADATA`, or `SYSTEM_METADATA`; see [Event structure: data, metadata, and system metadata](eb-custom-bus-addressing.md)), and a `Pattern`, an event pattern supplied as a JSON string. EventBridge combines the filters in a configuration with AND: an event must match every filter before the subscriber receives it. A subscriber with no `FilterConfiguration` receives all events.

## The three scopes
<a name="eb-custom-bus-filtering-scopes"></a>

`DATA`  
Examines the event data. For `PutRawEvents`, the data is the payload you sent. For `PutEvents`, the data is the EventBridge envelope, and your `Detail` is nested under the `detail` key. `DATA` filters support every event pattern operator except wildcards. EventBridge deserializes `application/avro` and `application/protobuf` events to JSON, and a `DATA` filter examines that JSON like any JSON event. An `application/octet-stream` event has no data a filter can read, so a subscriber with a `DATA` filter never matches one; `METADATA` and `SYSTEM_METADATA` filters still work on it.

`METADATA`  
Examines the key-value pairs the publisher set in `Metadata` with `PutRawEvents`. `METADATA` filters match exact values only: each value in the pattern must be a JSON array of exact values, and operators such as `prefix`, `numeric`, `exists`, and `$or` are not supported. To use those operators, filter on `DATA` or `SYSTEM_METADATA`. A `PutEvents` event has no publisher metadata, so a `METADATA` filter never matches one.

`SYSTEM_METADATA`  
Examines the fields EventBridge sets on the event, listed in the following table. `SYSTEM_METADATA` filters support every event pattern operator except wildcards. Fields that EventBridge generates carry the `aws:` prefix.


| Field | Description | Present on | 
| --- | --- | --- | 
| ContentType | The content type of the event data | Every event | 
| DeduplicationId | The deduplication identifier | Every event | 
| EventGroupId | The event group | Every event | 
| aws:EventId | The identifier EventBridge assigned | Every event | 
| aws:IngestionTime | When EventBridge received the event | Every event | 
| aws:SequenceNumber | The sequence number EventBridge assigned | Every event | 
| aws:DeliveryType | LIVE or REPLAY | Every delivered event | 
| aws:SchemaId | The schema identifier from the registry: a version UUID for Glue, an integer for Confluent | Avro and Protobuf events | 
| aws:RegistryType | Glue or Confluent | Avro and Protobuf events | 
| aws:Source | The source of the event | PutEvents, AWS service, and SaaS partner events | 
| aws:DetailType | The detail type of the event | PutEvents, AWS service, and SaaS partner events | 

**Note**  
To filter on AWS service events or SaaS partner events, use `aws:Source` and `aws:DetailType`. EventBridge writes these fields and no publish call can set a source that begins with `aws.`, so they identify the verified origin of the event. Do not use the `source` and `detail-type` fields in the event data for this purpose; any publisher can write those. See [Event sources for a Custom Event Bus](eb-custom-bus-event-sources.md).

## Example: filter an event published with PutRawEvents
<a name="eb-custom-bus-filtering-raw-example"></a>

`PutRawEvents` publishes a payload with a content type. A `DATA` filter matches the payload directly, and a `METADATA` filter matches the publisher's metadata map. The following configuration has one filter per scope; the subscriber receives an event only when all three match: the payload's `amount` is over 500, the metadata key `region` is `EU`, and the content type is JSON.

```
{
    "Filters": [
        { "Scope": "DATA", "Pattern": "{\"amount\":[{\"numeric\":[\">\",500]}]}" },
        { "Scope": "METADATA", "Pattern": "{\"region\":[\"EU\"]}" },
        { "Scope": "SYSTEM_METADATA", "Pattern": "{\"ContentType\":[\"application/json\"]}" }
    ]
}
```

## Example: filter an event published with PutEvents
<a name="eb-custom-bus-filtering-putevents-example"></a>

`PutEvents` publishes an event in the EventBridge envelope, built from the entry's `Source`, `DetailType`, `Resources`, `Time`, and `Detail`. A `DATA` filter matches this envelope, with your `Detail` nested under `detail`. The event's `ContentType` is `application/eventbridge+json`, `aws:Source` and `aws:DetailType` come from the entry's `Source` and `DetailType`, and the envelope also exposes `source` and `detail-type` in the `DATA` scope. The following configuration matches when the `amount` in the detail is over 500 and the source is `com.myapp.storage`.

```
{
    "Filters": [
        { "Scope": "DATA", "Pattern": "{\"detail\":{\"amount\":[{\"numeric\":[\">\",500]}]}}" },
        { "Scope": "SYSTEM_METADATA", "Pattern": "{\"aws:Source\":[\"com.myapp.storage\"]}" }
    ]
}
```

## Example: filter events from an event source
<a name="eb-custom-bus-filtering-event-source-example"></a>

Events that an event source ingests arrive in the EventBridge envelope, with the originating service or partner in `aws:Source`. To receive only Amazon S3 object-created events for one bucket, match the service in `SYSTEM_METADATA` and the bucket in `DATA`. For a partner, match the partner event source name, for example with a `prefix` on `aws.partner/example.com`.

```
{
    "Filters": [
        { "Scope": "SYSTEM_METADATA", "Pattern": "{\"aws:Source\":[\"aws.s3\"]}" },
        { "Scope": "DATA", "Pattern": "{\"detail-type\":[\"Object Created\"],\"detail\":{\"bucket\":{\"name\":[\"amzn-s3-demo-bucket\"]}}}" }
    ]
}
```

## Behavior and limits
<a name="eb-custom-bus-filtering-limits"></a>
+ **AND combination**: an event must match every filter in the configuration.
+ **No filter**: a subscriber with no filter configuration receives all events.
+ **One filter per scope**: a configuration holds at most one filter for each scope, so at most three filters. EventBridge rejects a configuration with two filters of the same scope.
+ **Wildcards**: the `wildcard` operator and `anything-but` with a wildcard are rejected, with the message *Filter pattern must not contain wildcard matchers (wildcard, anything-but wildcard)*.
+ **Pattern combinations with `$or`**: EventBridge rejects a filter whose `$or` usage produces more than 1,000 pattern combinations. Multiply the number of arguments in each `$or` array: one array of three gives three combinations, a second array of two gives six.
+ **Size**: all filters in a configuration share one limit of 4,096 bytes across the three scopes.
+ **Pattern shape**: a `DATA` pattern can have an array at its root; `METADATA` and `SYSTEM_METADATA` patterns must be JSON objects. A pattern that is not valid JSON is rejected when you create or update the subscriber.
+ **Changes**: a subscriber's filters can change 24 times in any rolling 24 hours; see [Updating, pausing, and resuming a subscriber](eb-custom-bus-update.md).

A pattern written for the wrong shape does not fail; it matches nothing. Before you rely on a subscriber, publish one event that should match and one that should not, and check both at the target.