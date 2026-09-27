

# Service-managed record distribution strategy
<a name="service-managed-record-distribution"></a>

Amazon Kinesis Data Streams offers two record distribution strategies that determine how records are distributed across shards in a stream:
+ **User-managed partition keys** (default) – You provide a partition key with each record, and Kinesis Data Streams uses the partition key hash to determine the shard placement. This is the traditional behavior for workloads that require ordering guarantees for related records.
+ **Service-managed record distribution** – Kinesis Data Streams automatically distributes records evenly across shards using service-managed algorithms. You do not need to provide partition keys. This is designed for stateless workloads where record ordering is not required.