# Amazon Keyspaces multi-Region replication usage notes

Consider the following when you're using multi-Region replication with Amazon Keyspaces.

- You can select any of the [available
  public](programmatic.md#global_endpoints "programmatic.md#global_endpoints") AWS Regions. For more information about AWS Regions [that are disabled by
  default](../../../general/latest/gr/rande-manage.md#rande-manage-enable "../../../general/latest/gr/rande-manage.md#rande-manage-enable"), see [Multi-Region replication in AWS Regions disabled by default](multiRegion-replication_how-it-works.md#howitworks_mrr_opt_in "multiRegion-replication_how-it-works.md#howitworks_mrr_opt_in").
- AWS GovCloud (US) Regions and China Regions are not supported.
- Consider the following workarounds until the features become available:

Configure Time to Live (TTL) when creating the multi-Region table. You
won't be able to enable and disable TTL, or adjust the TTL value later. For
more information, see [Expire data with Time to Live (TTL) for Amazon Keyspaces (for Apache Cassandra)](TTL.md "TTL.md").

    + For encryption at rest, use an AWS owned key. Customer managed keys are currently
     not supported for multi-Region tables. For more information, see


    [Encryption at rest: How it works in Amazon Keyspaces](encryption.md "encryption.md").

- You can use `ALTER KEYSPACE` to add a Region to a single-Region or a multi-Region keyspace. For more
  information, see [Add an AWS Region to a keyspace in Amazon Keyspaces](keyspaces-multi-region-add-replica.md "keyspaces-multi-region-add-replica.md").
  - Before adding a Region to a single-Region keyspace, ensure that no tables under the keyspace are configured with
    customer managed keys.
  - Any existing tags configured for keyspaces or tables are not replicated to the new
    Region.

- When you're using provisioned capacity management with Amazon Keyspaces auto scaling, make
  sure to use the Amazon Keyspaces API operations to create and configure your multi-Region
  tables. The underlying Application Auto Scaling API operations that Amazon Keyspaces calls on
  your behalf don't have multi-Region capabilities.

For more information, see [Update the provisioned capacity and auto scaling settings for a multi-Region table in Amazon Keyspaces](tables-mrr-autoscaling.md "tables-mrr-autoscaling.md"). For
more information on how to estimate the write capacity throughput of provisioned
multi-Region tables, see [Estimate and provision capacity for a multi-Region table in Amazon Keyspaces](tables-multi-region-capacity.md "tables-multi-region-capacity.md").

- Although data is automatically replicated across the selected Regions of a multi-Region
  table, when a client connects to an endpoint in one Region and queries the
  `system.peers` table, the query returns only local information. The query
  result appears like a single data center cluster to the client.
- Amazon Keyspaces multi-Region replication is asynchronous, and it supports `LOCAL_QUORUM` consistency
  for writes. `LOCAL_QUORUM` consistency requires that an update to a row
  is durably persisted on two replicas in the local Region before returning success to
  the client. The propagation of writes to the replicated Region (or Regions) is then
  performed asynchronously.

Amazon Keyspaces multi-Region replication doesn't support synchronous replication or `QUORUM`
consistency.

- When you create a multi-Region keyspace or table, any tags that you define during the creation
  process are automatically applied to all keyspaces and tables in all Regions. When
  you change the existing tags using `ALTER KEYSPACE` or `ALTER
TABLE`, the update is only applied to the keyspace or table in the Region
  where you're making the change.
- Amazon CloudWatch provides a `ReplicationLatency` metric for each replicated
  Region. It calculates this metric by tracking arriving rows, comparing their arrival
  time with their initial write time, and computing an average. Timings are stored
  within CloudWatch in the source Region. For more information, see [Monitoring Amazon Keyspaces with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

It can be useful to view the average and maximum timings to determine the average
and worst-case replication lag. There is no SLA on this latency.

- When using a multi-Region table in on-demand mode, you may observe an increase in latency for
  asynchronous replication of writes if a table replica experiences a new
  traffic peak. Similar to how Amazon Keyspaces automatically adapts the capacity of a single-Region on-demand table to the
  application traffic it receives, Amazon Keyspaces automatically adapts the capacity of a multi-Region on-demand table
  replica to the traffic that it receives. The increase in replication latency is transient because Amazon Keyspaces automatically
  allocates more capacity as your traffic volume increases. Once all replicas have adapted to your traffic volume,
  replication latency should return back to normal. For more information, see [Peak traffic and scaling
  properties](ReadWriteCapacityMode.md#ReadWriteCapacityMode.PeakTraffic "ReadWriteCapacityMode.md#ReadWriteCapacityMode.PeakTraffic").
- When using a multi-Region table in provisioned mode, if your application exceeds your
  provisioned throughput capacity, you may observe insufficient capacity errors and an
  increase in replication latency. To ensure that there's always enough read and write
  capacity for all table replicas in all AWS Regions of a multi-Region table, we
  recommend that you configure Amazon Keyspaces auto scaling. Amazon Keyspaces
  auto scaling helps you provision throughput capacity efficiently for variable
  workloads by adjusting throughput capacity automatically in response to actual
  application traffic. For more information, see [How auto scaling works for multi-Region
  tables](autoscaling.md#autoscaling.multi-region "autoscaling.md#autoscaling.multi-region").
