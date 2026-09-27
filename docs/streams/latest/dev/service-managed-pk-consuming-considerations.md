

# Consumer considerations
<a name="service-managed-pk-consuming-considerations"></a>

When consuming from service-managed streams, keep the following in mind:
+ **Handle null partition keys** – Your consumer application should handle `null` partition key values gracefully. Do not use partition keys from service-managed streams for any business logic.
+ **Shard iteration is unchanged** – You continue to use shard iterators to read records. The mechanism for traversing shards, handling resharding, and managing checkpoints remains the same.
+ **No ordering assumptions** – Do not assume any ordering relationship between records in a service-managed stream. Records from the same producer or business entity may appear on different shards.
+ **Downstream services work as-is** – AWS Lambda, Amazon Data Firehose, Amazon Managed Service for Apache Flink, and other AWS services that consume from Kinesis Data Streams continue to work without modification. However, if your downstream processing logic relies on partition keys for routing or grouping, you should review that logic.