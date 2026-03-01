# Troubleshooting latency issues in Amazon DynamoDB

If your workload appears to experience high latency, you can analyze the CloudWatch
`SuccessfulRequestLatency` metric, and check the average latency and median
latency through percentile metrics (p50) to see if it’s related to DynamoDB. Some variability
in the reported `SuccessfulRequestLatency` is normal, and occasional spikes
(particularly in the `Maximum` statistic and high percentiles) should not be
cause for concern. However, if the `Average` statistic or p50 (median) shows a
sharp increase and persists, you should check the AWS Service Health Dashboard and your
Personal Health Dashboard for more information. Some possible causes include the size of the
item in your table (a 1 KB item and a 400 KB item will vary in latency) or the size of the
query (10 items versus 100 items).

The percentile metrics (p99, p90, etc.) can help you better understand your latency
distribution. For example:

- p50 (median) shows the typical latency for your workload.
- p90 shows that 90 percent of requests are faster than this value.
- p99 helps identify the worst-case latency affecting 1 percent of requests.
  High p99 values with normal p50 values might indicate sporadic issues affecting a small
  portion of requests, while consistently elevated p50 values might suggest some performance
  degradation.

###### Note

To analyze custom percentile values (such as p99.9), you can manually enter the
desired percentile (e.g., p99.9) in the CloudWatch metric statistic field. This allows you to
evaluate latency distributions beyond the default percentiles listed in the
dropdown.

Some variation in latency metrics, particularly in higher percentiles, is expected and can
be seen as a result of DynamoDB-driven background operations that help maintain high
availability and durability for your data stored in DynamoDB tables or transient infrastructure
issues.

If necessary, consider opening a support case with AWS Support, and continue to
assess any available fall-back options for your application (such as evacuation of a Region
if you have a multi-Region architecture) according to your runbooks. You should log request
IDs for slow requests for providing these IDs to AWS Support when you open a
support case.

The `SuccessfulRequestLatency` metric only measures latency which is internal
to the DynamoDB service — client side activity and network trip times are not included.
To learn more about overall latency for calls from your client to the DynamoDB service, you can
enable latency metric logging in your AWS SDK.

###### Note

For most singleton operations (operations which apply to a single item by fully
specifying the primary key's value), DynamoDB delivers single-digit millisecond
`Average SuccessfulRequestLatency`. This value does not include the
transport overhead for the caller code accessing the DynamoDB endpoint. For multi-item data
operations, the latency will vary based on factors such as size of the result set, the
complexity of the data structures returned, and any condition expressions and filter
expressions applied. For repeated multi-item operations to the same data set with the
same parameters, DynamoDB will provide highly consistent `Average
 SuccessfulRequestLatency`.

Consider one or more of the following strategies to reduce latency:

- **Reuse connections:** DynamoDB requests are made via an
  authenticated session over HTTPS by default. Initiating the connection requires
  multiple round-trips and takes time so the latency of the first request is higher
  than following requests that reuse the connection. Requests over an already
  initialized connection deliver DynamoDB's consistent low latency. To avoid the latency
  overhead of establishing new connections, you may want to implement a "keep-alive"
  mechanism by sending a `GetItem` request every 30 seconds if no other
  requests are made.
- **Use eventually consistent reads:** If your
  application doesn't require strongly consistent reads, consider using the default
  eventually consistent reads. Eventually consistent reads have lower cost and can
  come from multiple availability zones, allowing selection of an availability zone
  co-located to the requester which decreases latency. For more information, see [DynamoDB read consistency](HowItWorks.md "HowItWorks.md").
- **Implement request hedging:** For very low p99
  latency requirements, consider implementing request hedging. With request hedging,
  if the initial request doesn't receive a response quickly enough, send a second
  equivalent request and let them race, first response wins. This improves tail
  latency at the cost of some extra requests. You can decide how long to wait before
  sending the second request. Hedging is easier for reads. For writes, use
  timestamp-based ordering to ensure hedged requests are treated as occurring at the
  time of the first attempt, preventing out-of-order updates. This approach has been
  discussed in [Timestamp
  writes for write hedging in Amazon DynamoDB](https://aws.amazon.com/blogs/database/timestamp-writes-for-write-hedging-in-amazon-dynamodb "https://aws.amazon.com/blogs/database/timestamp-writes-for-write-hedging-in-amazon-dynamodb").
- **Adjust request timeout and retry behavior:** The
  path from your client to DynamoDB traverses many components, each designed with
  redundancy in mind. Consider the following aspects:

      + Network resiliency
      + TCP packet timeouts
      + DynamoDB's distributed architecture

  Default SDK behaviors are optimized for most applications. However, you can
  implement a fail-fast strategy and adjust timeout settings. Requests taking
  significantly longer than normal are less likely to ultimately succeed. By failing
  fast and retrying, you may quickly succeed through a different path. This is similar
  to request hedging but ends the first request instead of allowing it to
  proceed.

Avoid setting timeout values too low. Overly low timeouts can lead to
client-induced availability issues. For example, a 50-millisecond socket timeout
could cause connection errors during network latency spikes, such as when
approaching Amazon EC2 instance bandwidth limits for single-flow traffic. Carefully weigh
the benefits of lower timeouts against potential risks to application availability,
and prefer hedging to short timeouts.

For a helpful discussion on this topic, see [Tuning AWS Java SDK HTTP request settings for latency-aware Amazon DynamoDB
applications](https://aws.amazon.com/blogs/database/tuning-aws-java-sdk-http-request-settings-for-latency-aware-amazon-dynamodb-applications/ "https://aws.amazon.com/blogs/database/tuning-aws-java-sdk-http-request-settings-for-latency-aware-amazon-dynamodb-applications/").

- **Reduce the distance between the client and DynamoDB
  endpoint:** If you have globally dispersed users, consider using [Global tables - multi-active, multi-Region replication](GlobalTables.md "GlobalTables.md"). With global tables, you
  can replicate your table to specified AWS Regions where you want the table to be
  available. You can place a copy of the data closer to the end user to reduce network
  latency during read and write operations. For more information about using DynamoDB
  global tables effectively, see [Using Amazon DynamoDB global tables](../../../prescriptive-guidance/latest/dynamodb-global-tables/introduction.md "../../../prescriptive-guidance/latest/dynamodb-global-tables/introduction.md") in AWS Prescriptive Guidance.
- **Use caching:** If your traffic is read heavy,
  consider using one of these caching services:
  - DynamoDB Accelerator (DAX): A fully managed, highly available, in-memory cache for
    DynamoDB that delivers up to a 10x performance improvement, from milliseconds
    to microseconds, even at millions of requests per second. For more
    information about DAX, see [In-memory acceleration with DynamoDB Accelerator (DAX)](DAX.md "DAX.md"):
  - Amazon ElastiCache: A fully managed, in-memory caching service that can be
    integrated with DynamoDB to improve read performance using the cache-aside
    pattern. For more information, see [Integrating Amazon DynamoDB and Amazon ElastiCache by using read-through
    caching](../../../prescriptive-guidance/latest/dynamodb-elasticache-integration/introduction.md "../../../prescriptive-guidance/latest/dynamodb-elasticache-integration/introduction.md") in AWS Prescriptive Guidance.
