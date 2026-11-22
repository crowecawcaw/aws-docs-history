

# Verify the current record distribution strategy

To check which record distribution strategy a stream is currently using, call the `DescribeStreamSummary` API. The response includes the `RecordDistributionStrategy` field.

**Example Check record distribution strategy (AWS CLI)**  

```bash
aws kinesis describe-stream-summary \
    --stream-arn arn:aws:kinesis:us-east-1:111122223333:stream/my-telemetry-stream
```

The response includes:

```json
{
    "StreamDescriptionSummary": {
        "StreamName": "my-telemetry-stream",
        "StreamARN": "arn:aws:kinesis:us-east-1:111122223333:stream/my-telemetry-stream",
        "StreamStatus": "ACTIVE",
        "StreamModeDetails": {
            "StreamMode": "ON_DEMAND"
        },
        "RecordDistributionStrategy": "AUTO",
        ...
    }
}
```