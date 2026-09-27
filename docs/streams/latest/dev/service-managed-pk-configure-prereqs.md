

# Prerequisites
<a name="service-managed-pk-configure-prereqs"></a>

Before you configure service-managed record distribution, ensure the following:
+ Your stream uses **on-demand** capacity mode (On-Demand Standard or On-Demand Advantage). Service-managed record distribution is not supported on provisioned streams.
+ If you use KPL aggregation, ensure the KPL does not aggregate records when writing to a service-managed stream. You can either explicitly disable aggregation, or upgrade to the latest KPL version and grant it the `kinesis:DescribeStreamSummary` permission so that it detects the stream and disables aggregation automatically. Aggregation is not supported on service-managed streams in any KPL version. For more information, see [KPL and KCL with service-managed streams](service-managed-pk-kpl.md).
+ If you want to send records without a partition key (null partition key), upgrade to the latest KPL version. For customers who continue providing partition keys, no KPL or KCL changes are required.