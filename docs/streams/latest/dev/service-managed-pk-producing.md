

# Write records to service-managed streams
<a name="service-managed-pk-producing"></a>

When a stream uses service-managed record distribution, Kinesis Data Streams automatically distributes records across shards. You can write records using the [PutRecord](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html) and [PutRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecords.html) APIs without providing partition keys. Existing producers that already provide partition keys continue to work without modification — the service ignores the provided values and uses its own distribution algorithms.

**Important**  
If your producers use the KPL with aggregation enabled (the default in existing KPL versions), you must disable aggregation before writing to a service-managed stream, or upgrade to the latest KPL version. Aggregation is not supported on service-managed streams, and aggregated records that are written can be silently dropped by KCL consumers during de-aggregation. For details, see [KPL and KCL with service-managed streams](service-managed-pk-kpl.md).