

# Share groups (queues) on Amazon MSK

Share groups enable point-to-point messaging on your Amazon MSK cluster. Multiple consumers in a share group can process records from the same partition concurrently, without partition-to-consumer assignment. Each record is delivered to one consumer in the group, acquired under a time-limited lock, and individually acknowledged.

Share groups are an alternative to consumer groups for workloads that need work-queue semantics, such as job distribution, task fan-out, and request-response patterns. They decouple consumer parallelism from partition count and remove the need to build custom routing logic for parallel processing. Share groups are available on MSK Provisioned Standard brokers running Apache Kafka 4.2 or later. Follow the best practices in [Best practices for Standard brokers](bestpractices.md).

## When to use share groups
<a name="msk-share-groups-when-to-use"></a>

If your workload is already well served by consumer groups and doesn't need work-queue semantics, or if your workload requires per-partition ordering, continue to use consumer groups.

Use share groups when:
+ You need per-message acknowledgement.
+ You want more consumers than partitions for parallel processing.
+ You need work-queue semantics without deploying a separate messaging system.
+ Your workload doesn't require strict per-partition ordering.

## Limitations of share groups
<a name="msk-share-groups-limitations"></a>
+ Share groups don't preserve per-partition ordering. Records from the same partition might be delivered to different consumers in the group and processed in any order. If your workload needs ordering, use consumer groups.
+ On average, share groups use 1.5 times more broker CPU than consumer groups, and up to 2 times more on `large` through `4xlarge` instance sizes.
+ With default configurations, you might observe consumer lag on instance sizes `4xlarge` and above. To mitigate this, tune the `max.poll.records` and `fetch.max.bytes` client configurations, the `group.share.max.partition.max.record.locks` broker configuration, and the `share.partition.max.record.locks` and `share.renew.acknowledge.enable` group configurations.