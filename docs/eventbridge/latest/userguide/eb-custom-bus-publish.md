

# Publishing events to a Custom Event Bus
<a name="eb-custom-bus-publish"></a>

You publish events to a Custom Event Bus with one of two API operations, `PutEvents` or `PutRawEvents`. The operation that you choose fixes the shape of the delivered event, and that shape determines how you write every filter, transformer, and target parameter for the bus. Choose before you write your first subscriber. For the two shapes, see [Event structure: data, metadata, and system metadata](eb-custom-bus-addressing.md).

The two operations produce one kind of event, and EventBridge treats them identically once the event is on the bus. `PutEvents` is a convenience over `PutRawEvents`: EventBridge takes the entry's `Source`, `DetailType`, `Detail`, and other fields, builds a JSON envelope from them, and stores that envelope as a JSON payload with a content type of `application/eventbridge+json`. From then on, filtering, transformation, ordering, deduplication, retention, and delivery work exactly as they do for a JSON event published with `PutRawEvents`. The only difference a subscriber sees is where your fields sit: at the top of `Data` for `PutRawEvents`, and under `Data.detail` inside the envelope for `PutEvents`. For Avro, Protobuf, and opaque payloads, see [Supported content types: JSON, Avro, Protobuf, and raw bytes](eb-custom-bus-open-formats.md).


|  | `PutEvents` | `PutRawEvents` | 
| --- | --- | --- | 
| Payload field | Detail, a JSON string | Data, bytes in any format | 
| Required in each entry | Source, DetailType | Data, SystemMetadata.ContentType | 
| Content type | Set by EventBridge to application/eventbridge\+json | Set by you: application/json, application/avro, application/protobuf, or application/octet-stream. See [Supported content types: JSON, Avro, Protobuf, and raw bytes](eb-custom-bus-open-formats.md). | 
| Your own metadata | Not available | Metadata, a map of up to 100 keys | 
| Ordering and deduplication inputs | SystemMetadata.EventGroupId, SystemMetadata.DeduplicationId | The same two fields | 
| Use when | Your events are JSON and you want the same envelope that Custom Event Bus - Classic produces | Your payload is binary or non-JSON, you need your own metadata keys, or you want the payload delivered exactly as sent | 

## Publish APIs
<a name="eb-custom-bus-publish-apis"></a>

Both operations take a batch of 1 to 100 entries per request and return one result per entry, in request order. EventBridge accepts or rejects each entry on its own: a rejected entry carries an `ErrorCode` and `ErrorMessage` in place of a `SuccessCode`, and the other entries in the same request are unaffected. Batch entries that belong together, and read every result rather than the HTTP status alone; see [Reading the response](#eb-custom-bus-publish-results). Both calls draw from one publish rate budget for your account, and the bus itself has a per-second ingestion quota that counts every publisher and event source; see [Custom Event Bus quotas](eb-quota.md#eb-custom-bus-quotas).

### Publish a JSON event with PutEvents
<a name="eb-custom-bus-publish-putevents"></a>

```
aws eventsv2 put-events \
    --event-bus-arn arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef \
    --entries '[
        {
            "Source": "com.example.orders",
            "DetailType": "OrderPlaced",
            "Detail": "{\"orderId\":\"1001\",\"total\":42.5}"
        }
    ]'
```

### Publish a raw event with PutRawEvents
<a name="eb-custom-bus-publish-putrawevents"></a>

`Data` is a binary field. In the AWS CLI, supply it as base64 text. The following example publishes the same JSON payload as raw bytes with a content type of `application/json`, and adds a metadata key.

```
aws eventsv2 put-raw-events \
    --event-bus-arn arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef \
    --entries '[
        {
            "Data": "eyJvcmRlcklkIjoiMTAwMSIsInRvdGFsIjo0Mi41fQ==",
            "Metadata": { "tenant": "acme" },
            "SystemMetadata": { "ContentType": "application/json" }
        }
    ]'
```

To publish Avro or Protobuf, name a schema registry in the request with `--schema-registry-configuration`. `RegistryUri` is an AWS Glue Schema Registry ARN or a Confluent Cloud HTTPS URL. A registry is named per request, not on the bus. Events with a content type of `application/octet-stream` need no registry, because EventBridge does not decode them.

## Publishing raw bytes
<a name="eb-custom-bus-publish-raw-bytes"></a>

To publish a payload that EventBridge should neither parse nor inspect, call `PutRawEvents` with the bytes Base64-encoded in `Data` and `SystemMetadata.ContentType` set to `application/octet-stream`. EventBridge stores and delivers the bytes exactly as sent, so a `DATA` filter cannot match them; route them with `METADATA` keys you set on the entry or with `SYSTEM_METADATA`. A subscriber's transformer sees the payload as a Base64 string in `$events.Data`. For the delivery choices and the deserialized alternative for Avro and Protobuf, see [Supported content types: JSON, Avro, Protobuf, and raw bytes](eb-custom-bus-open-formats.md); for how the payload appears to a transformer, see [Transforming events with JSONata](eb-custom-bus-transform.md).

## Reading the response
<a name="eb-custom-bus-publish-results"></a>

Both operations return one result for each entry, in the same order as the request. Each result carries either a `SuccessCode` or an `ErrorCode` and `ErrorMessage`. Check every entry, because a request can succeed while individual entries fail.

`SuccessCode` is `PUBLISHED` or `DEDUPLICATED`. `DEDUPLICATED` means that EventBridge recognized the entry as a duplicate of an event that it already accepted and did not store a second copy. It is a success, not an error. For more information, see [Ordering and deduplicating events on a Custom Event Bus](eb-custom-bus-ordering.md).

A publish response reports that EventBridge accepted the event. It does not report delivery. To confirm that an event arrived, check the target.

This section contains the following topics:
+ [Supported content types: JSON, Avro, Protobuf, and raw bytes](eb-custom-bus-open-formats.md)
+ [Event sources for a Custom Event Bus](eb-custom-bus-event-sources.md)
+ [Event structure: data, metadata, and system metadata](eb-custom-bus-addressing.md)