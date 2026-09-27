

# Transition behavior
<a name="service-managed-pk-transition"></a>

You can switch between service-managed and user-managed record distribution at any time. The mode change takes effect immediately without downtime or data loss for records already written. Producer and consumer applications continue to work with the following exceptions:
+ After you switch to user-managed distribution, producers that omit a partition key fail and must be updated to supply one.
+ After you switch to service-managed distribution and producers begin omitting the partition key, consumers that assume a partition key is always present can fail when they read a record that has none. Verify that your consumers handle an absent partition key before you enable `AUTO`. For more information, see the AWS SDK considerations in [Important considerations](service-managed-pk-considerations.md) and [KPL and KCL with service-managed streams](service-managed-pk-kpl.md).

During the transition:
+ Records already in the stream retain their original shard assignments based on the previous strategy.
+ New records arriving after the mode change are distributed according to the new strategy.
+ Consumers continue reading records from shards in sequence regardless of how those records were distributed.

For instructions on enabling or disabling service-managed record distribution, see [Configure service-managed record distribution](service-managed-pk-configure.md).

Switching strategies changes how records are placed on shards going forward, which affects per–partition-key ordering:
+ **User-managed to service-managed (USER\_PARTITION\_KEY → AUTO)** – Records that previously shared a partition key were routed to the same shard and ordered relative to one another. After the switch, new records are distributed evenly across shards regardless of partition key, so records sharing a partition key are no longer guaranteed to land on the same shard or be processed in order.
+ **Service-managed to user-managed (AUTO → USER\_PARTITION\_KEY)** – After the switch, new records are again routed by partition key hash, so records with the same partition key resume landing on the same shard. Producers must supply a partition key after the switch; [PutRecord](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html) and [PutRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecords.html) calls that omit it fail. Records written while the stream was in AUTO mode keep their original shard placement and are not redistributed, so a single partition key's records can be split across the pre-switch (AUTO) and post-switch shards.