

# Migrate from service-managed to user-managed (AUTO → USER\_PARTITION\_KEY)
<a name="service-managed-pk-configure-migrate-to-user"></a>

Follow these steps to safely switch a production stream back to user-managed partition keys:

1. **Verify all producers provide partition keys** — After switching, [PutRecord](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html) and [PutRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecords.html) calls that omit the `PartitionKey` field will fail with a validation error. Confirm that all producers are sending meaningful partition keys before switching.

1. **Verify consumer logic handles partition key changes** — Consumers that were processing `null` partition keys will now receive actual values. If your consumer logic uses partition keys for routing or grouping, verify it handles the transition correctly.

1. **Notify all consuming teams** — Inform teams that records will resume being distributed by partition key hash. Related records with the same partition key will again be sent to the same shard.

1. **Switch during low-traffic periods** — Minimize the number of in-flight records affected by the behavior change.

1. **Switch to user-managed** — Call the `UpdateStreamRecordDistributionStrategy` API to set `RecordDistributionStrategy` to `USER_PARTITION_KEY`.

1. **Monitor after switching** — Watch for `WriteProvisionedThroughputExceeded` (hot shards may return if partition key distribution is uneven) and consumer lag metrics.