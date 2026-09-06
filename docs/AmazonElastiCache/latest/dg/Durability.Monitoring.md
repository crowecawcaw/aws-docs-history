

# Monitoring
<a name="Durability.Monitoring"></a>

ElastiCache publishes the following additional CloudWatch metrics for durable clusters:
+ **DurabilityLag**: The age in milliseconds of the oldest write operation that has been acknowledged to the client but not yet persisted to the Multi-AZ transactional log. When this value approaches 10,000 ms (10 seconds), the primary node will begin rejecting new writes. This metric is always 0 for synchronous writes because writes are persisted before being acknowledged.
+ **DurabilityBufferExceededErrorCount**: The number of write commands rejected by a node because the durability buffer exceeded 10 seconds. When this metric is non-zero, your write requests will be rejected. Ensure your client is configured to retry with exponential backoff. This metric is always 0 for synchronous writes.

In addition to durability-specific metrics, ElastiCache also monitors write throughput. In the event that the incoming write traffic exceeds the available throughput of the Multi-AZ transactional log, incoming write commands will be throttled. In the event that customer traffic is throttled, the `TrafficManagementActive` metric will emit 1.