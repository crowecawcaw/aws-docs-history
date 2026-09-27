

# Migrate existing producers
<a name="service-managed-pk-producing-migration"></a>

You do not need to modify existing producers when enabling service-managed record distribution on a stream. Existing producers that provide partition keys continue to function — the service ignores the partition key values and distributes records using internal algorithms.

To migrate producers over time:

1. Enable service-managed record distribution on your stream (see [Configure service-managed record distribution](service-managed-pk-configure.md)).

1. Verify that your stream is receiving records and distributing them evenly by monitoring CloudWatch metrics (see `IncomingRecords` and `IncomingBytes` per shard).

1. (Optional) Update your producer code to remove partition key logic over time. This is not required for the feature to work but simplifies your codebase.

**Important**  
If your producers use KPL aggregation, note that aggregation is not supported on service-managed streams in any KPL version. You must disable aggregation before enabling service-managed record distribution. Aggregated records that are written to a service-managed stream can be silently dropped by KCL consumers during de-aggregation, with no error surfaced by the producer or consumer. For details, see [KPL and KCL with service-managed streams](service-managed-pk-kpl.md).