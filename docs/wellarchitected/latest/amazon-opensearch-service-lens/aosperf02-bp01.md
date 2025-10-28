# AOSPERF02-BP01 Implement processor utilization

monitoring

Keep CPU usage under 75% to maintain efficient resource utilization
and prevent potential performance issues.

**Level of risk exposed if this best practice
is not established**: High

**Desired outcome**: CPU utilization
is below 75% for efficient resource utilization and minimizing
potential performance issues.

**Benefits of establishing this best practice:**

- **Prevent performance issues:**
  Keeping CPU utilization below 75% helps identify and address
  potential issues related to high CPU usage, minimizing the risk
  of indexing or query processing bottlenecks.
- **Maintain scalability:** By
  keeping CPU utilization within a safe threshold, you can prevent
  scalability issues and ensure that your OpenSearch Service domains can handle increased traffic or workloads
  without degradation.

## Implementation guidance

The performance and efficiency in your OpenSearch Service domain can be maintained by closely monitoring CPU utilization.
This involves tracking CPU usage over the past 14 days and
verifying that the average rate remains below 75 percent. By doing
so, you can proactively identify and address potential issues
related to high CPU utilization, such as indexing or query
processing bottlenecks, before they affect your domain's
performance or scalability.

### Implementation steps

- Log in to the AWS Management Console.
- Navigate to the Amazon OpenSearch Service console.
- Select your OpenSearch Service domain name.
- Choose the **Cluster health** tab.
- Navigate to the Data nodes box.
- Choose the **CPU utilization** graph.
- Adjust time range to `2w` and Statistic to `Average`.

If you notice that your average CPU utilization exceeds 75% over
a 14-day period, it's recommended to investigate further by
checking for dedicated leader nodes and reviewing the best
practices outlined in [AOSPERF01](architecture-selection.md "architecture-selection.md").

## Resources

- [Monitoring
  OpenSearch cluster metrics with Amazon CloudWatch](../../../opensearch-service/latest/developerguide/managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-cluster-metrics "../../../opensearch-service/latest/developerguide/managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-cluster-metrics")
- [Choosing
  the number of shards](../../../opensearch-service/latest/developerguide/bp-sharding.md "../../../opensearch-service/latest/developerguide/bp-sharding.md")
- [Sizing
  OpenSearch Service domains](../../../opensearch-service/latest/developerguide/sizing-domains.md "../../../opensearch-service/latest/developerguide/sizing-domains.md")
