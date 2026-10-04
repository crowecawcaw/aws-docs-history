

# Choosing the right DB instance class
<a name="aurora-analytics-instance-class"></a>

The right instance class depends on how your foreign table queries use memory, storage, and CPU. For details about each of these resources, see [Resource management](aurora-analytics-resource-management.md).
+ **Memory**: A foreign table query holds its working data (sorts, aggregations, and hash tables for joins) in memory, bounded by the `aurora_analytics.query_mem` setting (`query_mem` for short). The default value of `query_mem` scales with instance size, so a larger instance gives each query more memory automatically. When a query exceeds `query_mem`, it spills to local storage, which is slower. For more information, see [Tuning query\_mem for your workload](aurora-analytics-tuning-query-mem.md).
+ **Concurrency**: Each concurrent foreign table query allocates memory up to `query_mem`, but actual usage depends on the query, and simple queries might use far less. When you size for concurrency, budget for peak memory rather than assuming every query uses the full `query_mem`. For more information, see [Concurrency sizing](aurora-analytics-concurrency-sizing.md).
+ **Caching and spilling**: The on-disk cache for Amazon S3 data and the temporary files that queries spill both use the instance's local storage. Local NVMe (available on d-type instances such as `db.r8gd`) is faster than Amazon EBS for both, so choose a class with local NVMe storage for production workloads that query foreign tables.
+ **Workload isolation**: Foreign table queries compete with the rest of the instance's traffic for CPU and memory. For workloads that query foreign tables heavily, run them on a dedicated reader instead. For more information, see [Using a dedicated reader instance for analytics](aurora-analytics-dedicated-reader.md).

Start with a class that fits your workload and adjust from there, using these signals.
+ Rising `AuroraAnalyticsMemoryUsage` means overall memory pressure is growing. Scale up to a larger instance class, or lower `query_mem` to leave room for concurrency.
+ Rising `AuroraAnalyticsDiskSpillSize` means individual queries are exceeding `query_mem` and spilling to local storage. Scale up, or raise `query_mem` to give each query more room.
+ A falling `AuroraAnalyticsCacheHitRatio` means more of your working data is being re-read from Amazon S3. A larger instance class caches more of it locally.
+ High CPU while querying foreign tables means queries need more vCPUs.

To handle more concurrent queries, scale up for more memory headroom, or add a reader to spread the load.

For these metrics and how to monitor them, see [Monitoring and troubleshooting](aurora-analytics-monitoring-troubleshooting.md).

## When to use EBS-only instances
<a name="aurora-analytics-ebs-only"></a>

Instances without local NVMe storage (such as `db.r8g` and `db.r8i`) use Amazon EBS for caching. Use them for the following.
+ Workloads that are more cost-sensitive than performance-sensitive.
+ Light or ad hoc foreign table queries.
+ Development and testing environments.