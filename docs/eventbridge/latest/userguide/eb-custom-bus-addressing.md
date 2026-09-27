

# Event structure: data, metadata, and system metadata
<a name="eb-custom-bus-addressing"></a>

Filters, transformers, and target parameters share one addressing model. EventBridge delivers every event under three top-level names: `Data` holds the payload, `Metadata` holds the keys that you supplied with `PutRawEvents`, and `SystemMetadata` holds the fields that EventBridge assigns. Where your own fields sit inside `Data` depends on the publish API. Both APIs produce the same kind of event, and EventBridge filters and transforms both the same way. The difference is only what sits inside `Data`.


| Part | Published with `PutRawEvents` | Published with `PutEvents` | 
| --- | --- | --- | 
| Data | Your payload, exactly as sent | An envelope with source, detail-type, time, and other fields. Your payload is the value of detail. | 
| Metadata | Your metadata keys | Not present | 
| SystemMetadata | Fields assigned by EventBridge | Fields assigned by EventBridge | 

A JSONata expression sees the event as `$events`. The same order identifier is at a different path for each API.

Published with `PutRawEvents`:

```
$events.Data.orderId
```

Published with `PutEvents`:

```
$events.Data.detail.orderId
```

The same difference applies to a filter with a scope of `DATA`. The pattern is written against the contents of `Data`.

Published with `PutRawEvents`:

```
{ "total": [ { "numeric": [ ">", 500 ] } ] }
```

Published with `PutEvents`:

```
{ "detail": { "total": [ { "numeric": [ ">", 500 ] } ] } }
```

**Important**  
An expression or pattern written for the wrong shape does not fail. It resolves to nothing, the filter matches no events, and the transformer produces no output. A subscriber whose filter matches nothing looks identical to a subscriber that is not working. Before you rely on a subscriber, publish one event that should match and one that should not, and confirm both outcomes at the target. If producers publish with both APIs to the same bus, give each kind of traffic its own subscribers.

## SystemMetadata fields
<a name="eb-custom-bus-addressing-system"></a>

`SystemMetadata` is the same for both APIs and is the only part of the event that EventBridge itself writes. A filter with a scope of `SYSTEM_METADATA` matches against it, and a JSONata expression reads it as `$events.SystemMetadata`. Every value is a string. EventBridge omits a field that has no value, so a JSONata reference to it evaluates as `undefined`; only `aws:DeliveryType` is always present. The following table lists the fields.


| Field | Value | 
| --- | --- | 
| aws:EventId | The identifier EventBridge assigned, returned to the publisher as EventId | 
| aws:Source, aws:DetailType | The entry's Source and DetailType for PutEvents; the originating service or partner and its event type for an event source. No publish call can set a source that begins with aws., so {"aws:Source":["aws.s3"]} proves that Amazon S3 produced the event | 
| aws:DeliveryType | LIVE for an event delivered as it arrived, REPLAY for one read from retained history. See [Replaying retained events to a subscriber](eb-custom-bus-replay.md) | 
| EventGroupId, DeduplicationId | As supplied at publish time. See [Ordering and deduplicating events on a Custom Event Bus](eb-custom-bus-ordering.md) | 
| ContentType | The content type as published: application/eventbridge\+json for PutEvents; for PutRawEvents, the entry's value, so Avro and Protobuf data that EventBridge decoded to JSON still shows application/avro or application/protobuf | 
| aws:IngestionTime | When the bus accepted the event | 
| aws:SequenceNumber | The event's position on the bus; increases with ingestion order | 
| aws:SchemaId, aws:RegistryType | The schema and registry used to deserialize an Avro or Protobuf payload; absent otherwise | 

`Metadata` is present only on events published with `PutRawEvents` that set it; for every other event it is empty. For `application/octet-stream`, `Data` is a Base64 string. In a `Transformer` expression `$events` is one event; only in a universal target's `Input` is it an array. See [Transforming events with JSONata](eb-custom-bus-transform.md).