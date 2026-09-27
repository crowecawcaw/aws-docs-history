

# KPL and KCL with service-managed streams
<a name="service-managed-pk-kpl"></a>

Customers who want to send records without a partition key (null partition key) to service-managed streams should upgrade to the latest KPL version. Customers who continue to provide a partition key do not need KCL changes, but they must ensure the KPL does not aggregate records when writing to a service-managed stream.

**Important**  
Existing KPL versions aggregate records by default. Aggregation is not supported on service-managed streams, and aggregated records that are written can be silently dropped by KCL consumers during de-aggregation, with no error surfaced by the producer or consumer. If you write to a service-managed stream with the KPL, either upgrade to the latest KPL version and grant it the `kinesis:DescribeStreamSummary` permission (so it detects the stream and stops aggregating), or explicitly disable aggregation. For details, see [Grant DescribeStreamSummary permission to the KPL](service-managed-pk-kpl-permissions.md) and [Aggregation is not supported on service-managed streams](service-managed-pk-kpl-aggregation.md).