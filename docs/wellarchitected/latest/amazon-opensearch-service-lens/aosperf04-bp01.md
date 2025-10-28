# AOSPERF04-BP01 Enable slow log functionality for search and

indexing

Gain visibility into query latency by enabling slow logs for search
and indexing. This visibility helps you optimize queries and
troubleshoot issues.

**Level of risk exposed if this best practice
is not established:** Medium

**Desired outcome**: You have enabled
slow logs for search and indexing operations, which provides you a
detailed view of query latency and enabling optimization efforts.

**Benefits of establishing this best
practice:**

- **Optimize queries:** Slow logs
  provide detailed information about slow or long-running queries,
  which you can use to identify areas for optimization and make
  changes to improve performance.
- **Troubleshoot issues:** By
  capturing logs of slow searches, indexing operations, and other
  queries, slow logs help you troubleshoot issues more
  effectively. This process reduces downtime and improves overall
  efficiency in your OpenSearch Service domains.

## Implementation guidance

To optimize the logging and troubleshooting process for your
OpenSearch Service domains, enable slow log functionality
for both search and indexing operations. Capture detailed logs of
slow or long-running queries and indexing operations, which
provide insights into performance bottlenecks and optimization
areas. By enabling slow log functionality, you can better
understand how your OpenSearch Service domains are performing under
various loads and conditions and make data-driven decisions to
improve overall efficiency and scalability.

Understand the benefits of slow logs. Slow logs help you identify
performance bottlenecks in your OpenSearch instance by capturing
detailed information about slow searches, indexing operations, and
other queries. This information can be used to optimize your
queries, improve performance, and troubleshoot issues.

### Implementation steps

- Enable log publishing to CloudWatch (as described in
  [Monitoring
  OpenSearch logs with Amazon CloudWatch Logs](../../../opensearch-service/latest/developerguide/createdomain-configure-slow-logs.md#createdomain-configure-slow-logs-console "../../../opensearch-service/latest/developerguide/createdomain-configure-slow-logs.md#createdomain-configure-slow-logs-console")).
- Set up the search and index (shard) slow log thresholds.
  Search slow logs are configured with cluster settings, while
  shard slow logs are configured at index level.
- Search slow log:

```
PUT domain-endpoint/_cluster/settings
          {
          "transient": {
          "cluster.search.request.slowlog.threshold.warn":
          "5s",
          "cluster.search.request.slowlog.threshold.info":
          "2s"
          }
          }
```

- Shard level slow logs:

```
PUT domain-endpoint/index/_settings
          {
          "index.search.slowlog.threshold.query.warn":
          "5s",
          "index.search.slowlog.threshold.query.info":
          "2s"
          }
```

## Resources

- [Monitoring
  OpenSearch logs with Amazon CloudWatch Logs](../../../opensearch-service/latest/developerguide/createdomain-configure-slow-logs.md "../../../opensearch-service/latest/developerguide/createdomain-configure-slow-logs.md")
- [Shards
  slow logs](https://opensearch.org/docs/latest/install-and-configure/configuring-opensearch/logs/#shard-slow-logs "https://opensearch.org/docs/latest/install-and-configure/configuring-opensearch/logs/#shard-slow-logs")
