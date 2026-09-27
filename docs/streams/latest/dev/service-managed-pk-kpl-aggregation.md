

# Aggregation is not supported on service-managed streams
<a name="service-managed-pk-kpl-aggregation"></a>

KPL aggregation is not supported on streams configured with service-managed record distribution, in any KPL version. Aggregated records are not rejected at write time. The failure surfaces in one of two ways, depending on whether the KPL treats the write as successful:
+ **Silent drop at the consumer** – KPL aggregation groups multiple user records into a single Kinesis Data Streams record based on the partition key hash, and expects those records to land on the shard the KPL predicts. On a service-managed stream, the service places records using its own algorithm rather than the partition key, which breaks the KPL and KCL aggregation contract. Aggregated records that are written are silently dropped by KCL consumers during de-aggregation, with no error surfaced by the producer or consumer.
+ **Reported write failure at the producer** – When the aggregated records the KPL sends are not committed to the shard the KPL predicts, the KPL retries them for approximately 30 seconds and then reports a write failure to your application through its callbacks.

To avoid both conditions, disable aggregation, or upgrade to the latest KPL version and grant it the `kinesis:DescribeStreamSummary` permission so that it detects service-managed streams and disables aggregation automatically. You can also set `setRecordDistributionStrategyDefault` to `AUTO` so the KPL does not aggregate before it discovers the stream's strategy.

**Note**  
For on-demand streams, KPL aggregation provides no cost benefit because pricing is based on throughput rather than the number of PUT requests. Consider disabling aggregation if you want to use service-managed record distribution.