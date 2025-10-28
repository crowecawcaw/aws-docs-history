# AOSPERF02-BP02 Implement Java memory utilization

monitoring

Keep `JVMMemoryPressure` below 85% to maintain efficient memory
utilization and prevent potential performance issues.

**Level of risk exposed if this best practice
is not established:** High

**Desired outcome:** The
JVMMemoryPressure metric remains below 85% for efficient memory
utilization and minimizing potential performance issues or domain
blocks.

**Benefits of establishing this best
practice:** Closely monitoring `JVMMemoryPressure` helps
you identify and address any potential issues related to high memory
pressure, such as excessive garbage collection or memory leaks,
before they impact your domain's performance, availability and
scalability.

## Implementation guidance

To maintain optimal performance and memory utilization for your
OpenSearch Service domains, closely monitor the `JVMMemoryPressure` metric. Specifically, track this metric to verify that it
remains below the recommended threshold of 85 percent. This helps
you identify and address any potential issues related to high
memory pressure, such as excessive garbage collection or out of
memory problems, before they impact your domain's performance or
scalability.

### Implementation steps

- Log in to the AWS Management Console.
- Navigate to the Amazon OpenSearch Service console.
- Select your OpenSearch Service domain name.
- Choose the **Cluster health tab**.
- Navigate to the Data nodes box.
- Choose the `JVMMemoryPressure` graph.
- Adjust time range to `2w` and Statistic to `Maximum`.

If you notice that your `JVMMemoryPressure` exceeds 85% over a 14-day
period, investigate further by reviewing the best practices
outlined in [AOSPERF01](architecture-selection.md "architecture-selection.md") as well as reviewing some of the common
issues outlined in
[How
do I troubleshoot high JVM memory pressure on my OpenSearch Service cluster](https://repost.aws/knowledge-center/opensearch-high-jvm-memory-pressure "https://repost.aws/knowledge-center/opensearch-high-jvm-memory-pressure").

## Resources

- [How
  do I troubleshoot high JVM memory pressure on my OpenSearch Service cluster](https://repost.aws/knowledge-center/opensearch-high-jvm-memory-pressure "https://repost.aws/knowledge-center/opensearch-high-jvm-memory-pressure")
- [Troubleshooting
  Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/handling-errors.md#troubleshooting-cluster-block "../../../opensearch-service/latest/developerguide/handling-errors.md#troubleshooting-cluster-block")
- [Choosing
  the number of shards](../../../opensearch-service/latest/developerguide/bp-sharding.md "../../../opensearch-service/latest/developerguide/bp-sharding.md")
- [Sizing
  OpenSearch Service domains](../../../opensearch-service/latest/developerguide/sizing-domains.md "../../../opensearch-service/latest/developerguide/sizing-domains.md")
