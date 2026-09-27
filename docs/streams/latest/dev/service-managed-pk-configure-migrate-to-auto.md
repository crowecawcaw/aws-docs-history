

# Migrate from user-managed to service-managed (USER\_PARTITION\_KEY → AUTO)
<a name="service-managed-pk-configure-migrate-to-auto"></a>

Follow these steps to safely enable service-managed record distribution on a production stream:

1. **Verify consumer compatibility** — Ensure all consumers can handle `null` partition keys in the `GetRecords` and `SubscribeToShard` responses. Test in a non-production environment first.

1. **Handle KPL aggregation** — If any producers use KPL aggregation, ensure the KPL does not aggregate records when writing to the service-managed stream. Either explicitly disable aggregation, or upgrade to the latest KPL version and grant it the `kinesis:DescribeStreamSummary` permission so that it detects the stream and disables aggregation automatically. Aggregation is not supported on service-managed streams. See [KPL and KCL with service-managed streams](service-managed-pk-kpl.md).

1. **Notify consumer teams** — Coordinate with all teams consuming from the stream. Inform them that partition keys will become `null` (or ignored) and that record ordering across shards is no longer guaranteed.

1. **Switch during low-traffic periods** — While the switch itself causes no data loss, performing it during low traffic reduces the number of in-flight records affected by the behavior change.

1. **Enable service-managed distribution** — Call the `UpdateStreamRecordDistributionStrategy` API to set `RecordDistributionStrategy` to `AUTO`.

1. **Monitor after switching** — Watch Amazon CloudWatch metrics for the stream: `IncomingRecords`, `IncomingBytes` (per shard, to verify even distribution), `WriteProvisionedThroughputExceeded` (should drop to zero), and `GetRecords.IteratorAgeMilliseconds` (to verify consumers are keeping up).