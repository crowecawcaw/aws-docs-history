# AOSOPS03-BP03 Enable search and indexing slow log

functionality

Turn on slow log functionality to gain insights into query latency
and optimize search and indexing operations.

**Level of risk exposed if this best practice
is not established:** Medium

**Desired outcome**: You use slow
logs for search and indexing operations, providing a detailed view
of query latency and enabling optimization efforts.

**Benefits of establishing this best
practice:**

- **Optimize queries:** Slow logs
  provide detailed information about slow or long-running queries,
  which helps you identify areas for optimization and make changes
  to improve performance.
- **Troubleshoot issues:** By
  capturing logs of slow searches, indexing operations, and other
  queries, slow logs help you troubleshoot issues more
  effectively, reducing downtime and improving overall efficiency
  in your OpenSearch Service domains.

## Implementation guidance

Search slow logs, indexing slow logs, and error logs are valuable
for diagnosing performance and stability issues. Audit logs record
user activity for compliance purposes.

For a detailed guide on enabling logging slow index and search
operations, see [AOSPERF04-BP01](aosperf04-bp01.md "aosperf04-bp01.md").

## Resources

- [Monitoring
  OpenSearch logs with Amazon CloudWatch Logs](../../../opensearch-service/latest/developerguide/createdomain-configure-slow-logs.md "../../../opensearch-service/latest/developerguide/createdomain-configure-slow-logs.md")
