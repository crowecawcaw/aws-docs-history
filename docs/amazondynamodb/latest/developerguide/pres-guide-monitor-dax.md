# Monitoring DAX

You can monitor key [metrics](dax-metrics-dimensions-dax.md#dax-metrics-dimensions "dax-metrics-dimensions-dax.md#dax-metrics-dimensions"), for example cache hit ratio, to ensure optimal DAX cluster performance, diagnose issues, and determine when you need to scale the cluster. Regularly checking key metrics helps you maintain performance, stability, and cost-efficiency by scaling the cluster to match your workload requirements. For more information about monitoring DAX, see [Production monitoring](dax-production-monitoring.md "dax-production-monitoring.md").

The following list presents some of the key metrics you should monitor:

- **Cache hit ratio** – Shows how effectively DAX serves cached data, reducing the need to access the underlying DynamoDB tables. Few cache misses for the cluster indicate good caching efficiency. But few cache hits suggest that you might need to revisit the caching TTL setting or the workload isn't a good fit for caching.

Use Amazon CloudWatch to calculate your DAX cluster's cache hit ratio. Compare the `ItemCacheHits`, `ItemCacheMisses`, `QueryCacheHits`, and `QueryCacheMisses` metrics to get this ratio. The following formula shows how the cache hit ratio is calculated. To calculate the ratio using this formula, divide your cache hits by the sum of your cache hits and misses.

```
Cache hit ratio = Cache hits / (Cache hits + Cache misses)
```

The cache hit ratio is a number between 0 and 1, which is represented as a percentage. A higher percentage indicates better overall cache utilization.

- **ErrorRequestCount** – Count of requests that resulted in user errors reported by the node or cluster. `ErrorRequestCount` includes requests that were throttled by the node or cluster. Monitoring user errors can help you identify scaling misconfigurations or hot item/partition patterns in your application.
- **Operation latencies** – Monitoring the latency of read and write operations to and from the DAX cluster can help you in identifying performance bottlenecks. Increasing latencies might indicate issues with your DAX cluster configuration, network, or the need to scale.
- **Network consumption** – Keep an eye on the `NetworkBytesIn` and `NetworkBytesOut` metrics to monitor your DAX cluster's network traffic. An unexpected increase in network throughput could mean more client requests or inefficient query patterns that are causing more data to be transferred.

Monitoring network consumption helps you manage costs for your DAX cluster. It also ensures the network doesn't become a bottleneck for cluster performance.

- **Eviction rate** – Shows how often items are removed from your cache to make room for new items. If the eviction rate increases over time, your cache might be too small or your caching strategy isn't effective.

Monitor the `EvictedSize` metric in CloudWatch to determine if your cache size is adequate for your workload. If the total evicted size keeps growing, you might need to scale up your DAX cluster to accommodate a larger cache.

- **CPU utilization** – Refers to the percentage of CPU utilization of the node or cluster. This is a critical metric to monitor for any database or caching system. High CPU utilization could mean your DAX cluster might be overloaded and needs scaling to handle the increased demand.

Monitor the `CPUUtilization` metric for your DAX cluster. If your CPU utilization consistently approaches or exceeds 70-80%, consider [scaling up your DAX cluster](#dax-cluster-scale-monitoring-data "#dax-cluster-scale-monitoring-data") as described in the following section.

If the number of requests sent to DAX exceeds a node's capacity, DAX limits the rate at which it accepts additional requests. It does this by returning a ThrottlingException. DAX continuously evaluates your cluster's CPU utilization to determine the request volume it can process while maintaining a healthy cluster state.

You can monitor the `ThrottledRequestCount` metric that DAX publishes to CloudWatch. If you see these exceptions regularly, you should consider scaling up your cluster.

## Scaling your DAX cluster using monitoring data

You can determine if you need to scale up or down your DAX cluster by monitoring its performance metrics.

- **Scale up or out** – If your DAX cluster has high CPU utilization, low cache hits (after optimizing the caching strategy), or high operation latencies, you should scale up your cluster. Adding more nodes, also called scaling out, can help distribute the load more evenly. For workloads with increasing writes per second, you might need to choose more powerful nodes (scaling up).
- **Scale down** – If you consistently see low CPU utilization and operation latencies below your thresholds, you might have over-provisioned resources. In such cases, scale down nodes to reduce costs. You can reduce the number of nodes down to 1 during low utilization periods, but you can't shut the cluster down entirely.
