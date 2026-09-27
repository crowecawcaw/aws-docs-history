

# SubscribeToShard API behavior
<a name="service-managed-pk-consuming-subscribe"></a>

When using enhanced fan-out with the `SubscribeToShard` API, the behavior is the same as [GetRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetRecords.html). The `PartitionKey` field in each record in the `SubscribeToShardEvent` follows the same rules:
+ Returns `null` if the producer did not provide a partition key.
+ Returns the original value if the producer provided one (even though it was ignored for shard placement).