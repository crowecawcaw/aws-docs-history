

# Upgrade KPL to send null partition keys
<a name="service-managed-pk-kpl-upgrade-for-null"></a>

To send records without providing a partition key to a service-managed stream, you must upgrade to the latest KPL version. The updated KPL can detect whether a stream uses service-managed record distribution (AUTO) and handle null partition keys accordingly.

Customers using Kinesis Producer Library can simply upgrade to the latest version at the [Amazon Kinesis Producer Library GitHub repository](https://github.com/awslabs/amazon-kinesis-producer) to benefit from this capability.

The updated KPL detects the stream's record distribution strategy by calling the `DescribeStreamSummary` API. Grant the `kinesis:DescribeStreamSummary` permission to the identity the KPL uses. Without it, the KPL cannot detect a service-managed stream and falls back to aggregating records. For details, see [Grant DescribeStreamSummary permission to the KPL](service-managed-pk-kpl-permissions.md).