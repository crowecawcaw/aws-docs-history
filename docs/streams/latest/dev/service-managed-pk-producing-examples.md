

# Examples
<a name="service-managed-pk-producing-examples"></a>

**Example Write a single record without a partition key (AWS CLI)**  

```
aws kinesis put-record \
    --stream-name my-telemetry-stream \
    --data "eyJtZXRyaWMiOiAiY3B1X3V0aWxpemF0aW9uIiwgInZhbHVlIjogNzIuNX0="
```

**Example Write a single record without a partition key (AWS SDK for Java)**  

```
PutRecordRequest request = PutRecordRequest.builder()
    .streamName("my-telemetry-stream")
    .data(SdkBytes.fromUtf8String("{\"metric\": \"cpu_utilization\", \"value\": 72.5}"))
    .build();

PutRecordResponse response = kinesisClient.putRecord(request);
```

**Example Write a batch of records without partition keys (AWS SDK for Java)**  

```
List<PutRecordsRequestEntry> entries = new ArrayList<>();
entries.add(PutRecordsRequestEntry.builder()
    .data(SdkBytes.fromUtf8String("{\"event\": \"page_view\", \"page\": \"/home\"}"))
    .build());
entries.add(PutRecordsRequestEntry.builder()
    .data(SdkBytes.fromUtf8String("{\"event\": \"page_view\", \"page\": \"/products\"}"))
    .build());

PutRecordsRequest request = PutRecordsRequest.builder()
    .streamName("my-telemetry-stream")
    .records(entries)
    .build();

PutRecordsResponse response = kinesisClient.putRecords(request);
```

**Example Existing producer with partition key (continues to work)**  

```
// This producer code continues to work without modification.
// The partition key is ignored by the service when service-managed
// record distribution is enabled.
PutRecordRequest request = PutRecordRequest.builder()
    .streamName("my-telemetry-stream")
    .partitionKey("device-12345")
    .data(SdkBytes.fromUtf8String("{\"temp\": 22.1}"))
    .build();

PutRecordResponse response = kinesisClient.putRecord(request);
```