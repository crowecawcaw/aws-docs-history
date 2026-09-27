

# Producer API behavior with service-managed distribution
<a name="service-managed-pk-producing-behavior"></a>

When service-managed record distribution is enabled on a stream, the following behavior applies to the [PutRecord](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html) and [PutRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecords.html) APIs:
+ **PartitionKey** – Optional. If provided, the value is ignored for shard placement. The service distributes the record using internal algorithms.
+ **ExplicitHashKey** – If provided, the value is ignored for shard placement, the same as `PartitionKey`. The service distributes the record using internal algorithms.
+ **SequenceNumberForOrdering** ([PutRecord](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html) only) – Must not be provided. `PutRecord` requests that include this field are rejected with an `InvalidArgumentException`. Ordering is not applicable for service-managed distribution. This field does not exist on `PutRecords`.

**Note**  
Existing producer applications that provide partition keys continue to work without modification when service-managed mode is enabled. The service ignores the partition key values, which means you can enable this feature on production streams without coordinating code deployments across your teams.  
If you use the KPL to send records without a partition key, upgrade to the latest KPL version. If you use the AWS SDK directly, no SDK change is required as long as you continue to supply a partition key; to omit the partition key, you must upgrade to the latest SDK version. For more information, see [Important considerations](service-managed-pk-considerations.md) and [KPL and KCL with service-managed streams](service-managed-pk-kpl.md).