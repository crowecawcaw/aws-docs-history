

# Enable service-managed record distribution on an existing stream
<a name="service-managed-pk-configure-update"></a>

To enable service-managed record distribution on an existing on-demand stream, use the `UpdateStreamRecordDistributionStrategy` API. The change takes effect immediately. Before you enable `AUTO`, verify that your consumers can handle an absent (null) partition key, and ensure any KPL producers do not aggregate records. For more information, see [Safe migration patterns](service-managed-pk-configure-safe-migration.md).

**Example Enable service-managed distribution on an existing stream (AWS CLI)**  

```
aws kinesis update-stream-record-distribution-strategy \
    --stream-arn arn:aws:kinesis:us-east-1:123456789012:stream/my-telemetry-stream \
    --record-distribution-strategy AUTO
```

**Example Enable service-managed distribution (AWS SDK for Java)**  

```
UpdateStreamRecordDistributionStrategyRequest request =
    UpdateStreamRecordDistributionStrategyRequest.builder()
        .streamName("my-telemetry-stream")
        .recordDistributionStrategy(RecordDistributionStrategy.AUTO)
        .build();

kinesisClient.updateStreamRecordDistributionStrategy(request);
```

You can also specify the stream by name instead of ARN:

```
aws kinesis update-stream-record-distribution-strategy \
    --stream-name my-telemetry-stream \
    --record-distribution-strategy AUTO
```