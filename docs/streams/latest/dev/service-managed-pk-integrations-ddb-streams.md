

# Amazon DynamoDB with Kinesis data streams
<a name="service-managed-pk-integrations-ddb-streams"></a>

You can stream Amazon DynamoDB change data capture (CDC) records to a Kinesis Data Streams stream that you own. DynamoDB always sets a non-null partition key (a hash of the item's key) and never reads records back from the stream. On a service-managed stream, DynamoDB continues to work without changes.

Be aware of one behavior change: on a user-managed stream, all change records for a single item map to the same shard because they share a partition key. On a service-managed stream, the partition key is ignored for routing, so change records for a single item are distributed across shards. DynamoDB makes no ordering guarantee based on shard placement. Consumers order records by using the `ApproximateCreationDateTime` field, so this behavior does not affect correctness for consumers that order records by timestamp.