# AOSPERF03-BP01 Establish storage utilization thresholds

Maintain efficient resource utilization by keeping domain storage
usage under 75% to prevent potential performance issues or cluster
write blocks.

**Level of risk exposed if this best practice
is not established:** High

**Desired outcome**: Domain storage
usage remains below 75%, which improves resource utilization and
minimizes potential performance issues due to storage constraints.

**Benefits of establishing this best
practice:** You can prevent write operations such as adding
documents or creating indices to fail.

## Implementation guidance

If one or more data nodes in your cluster have storage space less
than the minimum value of either 20% of available storage space or
20 GB, basic write operations such as adding documents and
creating indexes may fail.

- The Amazon CloudWatch `FreeStorageSpace` metric is used to
  monitor available storage in the data nodes.
- Adjusting your indexing rate or deleting unnecessary data can
  help keep your storage usage below the set threshold.
- If you are using UltraWarm nodes, consider migrating logs and
  time-series indices from the hot storage to the UltraWarm
  nodes.

### Implementation steps

- Log in to the AWS Management Console.
- Navigate to the Amazon OpenSearch Service console.
- Select your OpenSearch Service domain name.
- Choose the **Cluster health** tab.
- Navigate to the Data nodes box.
- Choose the `FreeStorageSpace` graph.
- Adjust time range to `2w` and Statistic to `Maximum`.
- Remove unnecessary or redundant data from your domain. Use
  the `GET _cat/indices` API to list and investigate your
  indices and the `DELETE /<index_name>` API to remove
  unnecessary or redundant data.
- Consider adding more storage to your domain by increasing
  EBS storage size or add more data nodes to your domain. Keep
  this step consistent with shard-to-CPU ratio,
  shard-to-java-heap ratio, and shards distribution across
  your domain. For more information, see [AOSPERF01-BP01](aosperf01-bp01.md "aosperf01-bp01.md"),
  [AOSPERF01-BP02](aosperf01-bp02.md "aosperf01-bp02.md"), and [AOSPERF03-BP02](aosperf03-bp02.md "aosperf03-bp02.md").
- For more detail, see
  [Lack
  of available storage space](../../../opensearch-service/latest/developerguide/handling-errors.md#troubleshooting-cluster-block "../../../opensearch-service/latest/developerguide/handling-errors.md#troubleshooting-cluster-block").

## Resources

- [Monitoring
  OpenSearch cluster metrics with Amazon CloudWatch](../../../opensearch-service/latest/developerguide/managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-box-charts "../../../opensearch-service/latest/developerguide/managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-box-charts")
- [Choosing
  the number of shards](../../../opensearch-service/latest/developerguide/bp-sharding.md "../../../opensearch-service/latest/developerguide/bp-sharding.md")
- [Sizing
  OpenSearch Service domains](../../../opensearch-service/latest/developerguide/sizing-domains.md "../../../opensearch-service/latest/developerguide/sizing-domains.md")
- [Lack
  of available storage](../../../opensearch-service/latest/developerguide/handling-errors.md#troubleshooting-cluster-block "../../../opensearch-service/latest/developerguide/handling-errors.md#troubleshooting-cluster-block")
