

# No changes required for existing producers and consumers
<a name="service-managed-pk-kpl-no-changes"></a>

If you continue to provide a partition key in your [PutRecord](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html) and [PutRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecords.html) API calls, and your producer does not use KPL aggregation, no KPL or KCL changes are required. Your existing producer and consumer applications continue to work without modification when service-managed record distribution is enabled on a stream — the service ignores the partition key values you provide and distributes records using internal algorithms.

If your producer uses KPL aggregation (the default in existing KPL versions), you must disable aggregation or upgrade the KPL before writing to a service-managed stream. See [Aggregation is not supported on service-managed streams](service-managed-pk-kpl-aggregation.md).

KCL requires no changes regardless of whether you send null partition keys or not. KCL continues to read records from shards in sequence as it does today.