

# Switch back to user-managed partition keys
<a name="service-managed-pk-configure-disable"></a>

To switch a stream back to user-managed partition keys, call the `UpdateStreamRecordDistributionStrategy` API with `RecordDistributionStrategy` set to `USER_PARTITION_KEY`.

```
aws kinesis update-stream-record-distribution-strategy \
    --stream-arn arn:aws:kinesis:us-east-1:123456789012:stream/my-telemetry-stream \
    --record-distribution-strategy USER_PARTITION_KEY
```

The change takes effect immediately. All subsequent [PutRecord](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html) and [PutRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecords.html) API calls require a partition key, and the service uses the provided partition key to determine shard placement.

**Important**  
Switching to user-managed partition keys restores per-partition-key ordering — records with the same partition key resume landing on the same shard. Before switching, ensure that your producers are providing meaningful partition keys. If producers are still sending records without partition keys after you switch to user-managed mode, the API calls fail.