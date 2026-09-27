

# Best practices
<a name="service-managed-pk-producing-best-practices"></a>
+ **Use PutRecords for batching** – Continue using the [PutRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecords.html) API for batch writes. Batching reduces API call overhead and improves throughput regardless of the record distribution strategy.
+ **Remove SequenceNumberForOrdering** – This `PutRecord` field is rejected by service-managed streams (`PutRecords` has no such field). A supplied `ExplicitHashKey` is ignored rather than rejected, but you should remove it as well because it has no effect. Update your producer code to remove these fields.
+ **Monitor shard utilization** – Use CloudWatch metrics to verify that records are evenly distributed across shards. Monitor `WriteProvisionedThroughputExceeded` to confirm no hot shards are occurring.