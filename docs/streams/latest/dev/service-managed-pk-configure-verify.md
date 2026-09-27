

# Verify the current record distribution strategy
<a name="service-managed-pk-configure-verify"></a>

To check which record distribution strategy a stream is currently using, call the `DescribeStreamSummary` API. The response includes the `RecordDistributionStrategy` field.

**Example Check record distribution strategy (AWS CLI)**  

```
aws kinesis describe-stream-summary \
    --stream-arn arn:aws:kinesis:us-east-1:123456789012:stream/my-telemetry-stream
```

The response includes:

```
{
    "StreamDescriptionSummary": {
        "StreamName": "my-telemetry-stream",
        "StreamARN": "arn:aws:kinesis:us-east-1:123456789012:stream/my-telemetry-stream",
        "StreamStatus": "ACTIVE",
        "StreamModeDetails": {
            "StreamMode": "ON_DEMAND"
        },
        "RecordDistributionStrategy": "AUTO",
        ...
    }
}
```