

# How service-managed record distribution works
<a name="service-managed-pk-overview"></a>

When you enable the service-managed record distribution strategy on a stream, Kinesis Data Streams takes over the responsibility of distributing records across shards. The service uses internal algorithms to spread records evenly and avoid hot shards. This eliminates common issues with customer-generated partition keys, such as uneven traffic distribution. It also prevents rotating hot key throttling.

Key characteristics of service-managed record distribution:
+ **Stream-level setting** – The record distribution strategy is configured at the stream level and applies to all records written to that stream.
+ **On-demand streams only** – Service-managed record distribution is available for on-demand streams (On-Demand Standard and On-Demand Advantage). It is not supported on provisioned streams.
+ **No ordering guarantees** – Because the service distributes records across shards using internal algorithms, records with the same business entity do not necessarily arrive at the same shard. Do not use this mode for workloads that depend on ordering.
+ **Partition keys are ignored** – When service-managed mode is enabled, any partition key values provided in [PutRecord](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html) or [PutRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecords.html) API calls are ignored. The service handles distribution internally.
+ **No additional cost** – Service-managed record distribution is available at no additional cost. Standard Kinesis Data Streams pricing applies.