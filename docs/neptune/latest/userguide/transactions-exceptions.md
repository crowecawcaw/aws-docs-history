

# Exception Handling and Retries
<a name="transactions-exceptions"></a>

Building robust applications on Neptune often means preparing for the unexpected, especially when it comes to handling errors returned by the database. One of the most common responses to server-side exceptions is to retry the failed operation. While retry logic is essential for resilient systems, you need to recognize that not all errors should be treated the same way. Rather than relying on generic retry behaviors, a thoughtful approach can help you build more reliable and efficient applications.

## Why retry logic matters
<a name="why-retry-logic-matters"></a>

Retry logic is a critical component of any distributed application. Transient issues such as network instability, temporary resource constraints, or concurrent modification conflicts can cause operations to fail. In many cases, these failures don't indicate a permanent problem and can be resolved by waiting and trying again. Implementing a solid retry strategy acknowledges the reality of imperfect environments in distributed systems, ensuring stronger reliability and continuity with less need for manual intervention.

## The risks of indiscriminate retries
<a name="risks-of-indiscriminate-retries"></a>

Retrying every error by default can lead to several unintended consequences:
+ **Increased contention** – When operations that fail due to high concurrency are retried repeatedly, the overall contention can get worse. This might result in a cycle of failed transactions and degraded performance.
+ **Resource exhaustion** – Indiscriminate retries can consume additional system resources, both on the client and server side. This can potentially lead to throttling or even service degradation.
+ **Increased latency for clients** – Excessive retries can cause significant delays for client applications, especially if each retry involves waiting periods. This can negatively impact user experience and downstream processes.

## Developing a practical retry strategy
<a name="developing-practical-retry-strategy"></a>

To build a resilient and efficient application, develop a retry strategy that's tailored to the specific error conditions your application might encounter. Here are some considerations to guide your approach:
+ **Identify retryable errors** – Not all exceptions should be retried. For example, syntax errors, authentication failures, or invalid queries should not trigger a retry. Neptune provides [error codes](https://docs.aws.amazon.com/neptune/latest/userguide/errors-engine-codes.html) and general recommendations for which errors are safe to retry, but you need to implement the logic that fits your use case.
+ **Implement exponential backoff** – For transient errors, use an exponential backoff strategy to progressively increase the wait time between retries. This helps alleviate contention and reduces the risk of cascading failures.
+ **Consider initial pause length** – Performing the first retry too quickly might just end with the same error if the server hasn't been given enough time to release resources that the query needs to succeed. A longer pause in the right situations could reduce wasted requests and server pressure.
+ **Add jitter to backoff** – While exponential backoff is effective, it can still lead to synchronized retry storms if many clients fail at the same time and then retry together. Adding jitter, a small random variation to the backoff delay, helps spread out retry attempts thereby reducing the chance of all clients retrying simultaneously and causing another spike in load.
+ **Limit retry attempts** – Set a reasonable maximum number of retries to prevent infinite loops and resource exhaustion.
+ **Monitor and adjust** – Continuously monitor your application's error rate and adjust your retry strategy as needed. If you notice a high number of retries for a particular operation, consider whether the operation can be optimized or serialized.

For a deeper discussion of exponential backoff and jitter as a general cloud design pattern, see [Retry with backoff](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html) in AWS Prescriptive Guidance.

## Example scenarios
<a name="example-scenarios"></a>

The right retry strategy depends on the nature of the failure, the workload, and the error patterns you observe. The following table summarizes some common failure scenarios and how the retry strategy considerations apply to each. Explanatory paragraphs follow for additional context.


|  Scenario  |  Retryable?  |  Backoff & Jitter  |  Initial Pause  |  Retry Limit  |  Monitor & Adjust  | 
| --- | --- | --- | --- | --- | --- | 
| Occasional CME on Short Queries | Yes | Short backoff, add jitter | Short (for example, 100ms) | High | Watch for rising CME Rates | 
| Frequent CME on Longer-Running Queries | Yes | Longer backoff, add jitter | Longer (for example, 2s) | Moderate | Investigate and reduce contention | 
| Memory Limits on Expensive Queries | Yes | Long backoff | Long (for example, 5-10s) | Low | Optimize query, alert if persistent | 
| Timeout on Moderate Queries | Maybe | Moderate backoff, add jitter | Moderate (for example, 1s) | Low to Moderate | Assess server load and query design | 

### Scenario 1: Occasional CME on short queries
<a name="scenario-1-occasional-cme"></a>

For a workload where `ConcurrentModificationException` appears infrequently during short, simple updates, these errors are typically transient and safe to retry. Use a short initial pause (for example, 100 milliseconds) before the first retry. This time allows any brief lock to clear. Combine this with a short exponential backoff and jitter to avoid synchronized retries. Since the cost of retrying is low, a higher retry limit is reasonable. Still, monitor the CME rate to catch any trend toward increased contention in your data.

### Scenario 2: Frequent CME on long-running queries
<a name="scenario-2-frequent-cme"></a>

If your application sees frequent CMEs on long-running queries, this suggests more severe contention. In this case, start with a longer initial pause (for example, 2 seconds), to give the current query holding the lock enough time to complete. Use a longer exponential backoff and add jitter. Limit the number of retries to avoid excessive delays and resource usage. If contention persists, review your workload for patterns and consider serializing updates or reducing concurrency to address the root cause.

### Scenario 3: Memory limits on expensive queries
<a name="scenario-3-memory-limits"></a>

When memory-based errors occur during a known resource-intensive query, retries can make sense, but only after a long initial pause (for example, 5 to 10 seconds or more) to allow the server to release resources. Use a long backoff strategy and set a low retry limit, since repeated failures are unlikely to resolve without changes to the query or workload. Persistent errors should trigger alerts and prompt a review of query complexity and resource usage.

### Scenario 4: Timeout on moderate queries
<a name="scenario-4-timeout-moderate"></a>

A timeout on a moderately expensive query is a more ambiguous case. Sometimes, a retry might succeed if the timeout was due to a temporary spike in server load or network conditions. Start with a moderate initial pause (for example, 1 second) to give the system a chance to recover. Apply a moderate backoff and add jitter to avoid synchronized retries. Keep the retry limit low to moderate, since repeated timeouts might indicate a deeper issue with the query or the server's capacity. Monitor for patterns: if timeouts become frequent, assess whether the query needs optimization or if the Neptune cluster is under-provisioned.

## Monitoring and observability
<a name="monitoring-and-observability"></a>

Monitoring is a critical part of any retry strategy. Effective observability helps you understand how well your retry logic is working and provides early signals when something in your workload or cluster configuration needs attention.

### MainRequestQueuePendingRequests
<a name="main-request-queue"></a>

This CloudWatch metric tracks the number of requests waiting in Neptune's input queue. A rising value indicates that queries are backing up, which can be a sign of excessive contention, under-provisioned resources, or retry storms. Monitoring this metric helps you spot when your retry strategy is causing or compounding queuing issues, and can prompt you to adjust your approach before failures escalate.

### Other CloudWatch metrics
<a name="other-cloudwatch-metrics"></a>

Other [Neptune metrics](https://docs.aws.amazon.com/neptune/latest/userguide/cw-metrics.html) like `CPUUtilization`, `TotalRequestsPerSecond`, and query latency provide additional context. For example, high CPU and I/O combined with growing queue lengths might indicate that your cluster is overloaded or that queries are too large or too frequent. [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) can be set on these metrics to alert you to abnormal behavior and help you correlate spikes in errors or retries with underlying resource constraints.

### Neptune Status and Query APIs
<a name="neptune-status-query-apis"></a>

The Neptune [Status API for Gremlin](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-api-status.html) and its analogous APIs for [OpenCypher](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-status.html) and [SPARQL](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-api-status.html) give a real-time view of the queries accepted and running on the cluster which is useful for diagnosing bottlenecks or understanding the impact of retry logic in real time.

By combining these monitoring tools, you can:
+ Detect when retries are contributing to queuing and performance degradation.
+ Identify when to scale your Neptune cluster or optimize queries.
+ Validate that your retry strategy is resolving transient failures without masking deeper issues.
+ Receive early warnings about emerging contention or resource exhaustion.

Proactive monitoring and alerting are essential for maintaining a healthy Neptune deployment, especially as your application's concurrency and complexity grow.