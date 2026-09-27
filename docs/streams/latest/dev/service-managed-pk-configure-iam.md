

# IAM permissions
<a name="service-managed-pk-configure-iam"></a>

To configure the record distribution strategy, the IAM principal must have the following permissions:
+ `kinesis:CreateStream` – to create a stream with service-managed record distribution
+ `kinesis:UpdateStreamRecordDistributionStrategy` – to change the record distribution strategy on an existing stream
+ `kinesis:DescribeStreamSummary` – to view the current record distribution strategy. This permission is also required by the updated KPL, which calls `DescribeStreamSummary` to detect whether a stream uses service-managed record distribution. Grant it to any KPL producer that writes to a service-managed stream. For more information, see [Grant DescribeStreamSummary permission to the KPL](service-managed-pk-kpl-permissions.md).