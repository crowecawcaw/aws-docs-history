# Evaluating the suitability of DAX for your use cases

This section explains when and why to use DAX. Using this guidance helps you to determine if integrating DAX with DynamoDB is advantageous for your application's workload patterns, performance requirements, and data consistency needs. It also covers scenarios where DAX might not be suitable, for example, write-heavy workloads and infrequently accessed data.

###### In this section

- [When and why to choose DAX](#choose-dax "#choose-dax")
- [When not to use DAX](#dax-unsuitable-scenarios "#dax-unsuitable-scenarios")

## When and why to choose DAX

You can consider adding DAX to your application stack in several scenarios. For example, use DAX to reduce the overall latency of read requests against DynamoDB or to minimize repeated reads of the same data from a table. The following list presents examples of scenarios in which you can take advantage of integrating DAX with DynamoDB:

- **High-performance requirement**
  - **Low latency reads** – You should consider using DAX if your application requires response times in microseconds for eventually-consistent reads. DAX can also drastically reduce the response time for accessing frequently read data.

- **Read-intensive workloads**
  - **Read-heavy applications** – For applications with a high read-to-write ratio, for example, 10:1 or more, DAX results in more cache hits and less stale data. This reduces reads against a table. To avoid reading stale data from the cache if your application is write-heavy, make sure to set a lower [Using time to live (TTL) in DynamoDB](TTL.md "TTL.md") for the cache.
  - **Caching common queries** – If your application frequently reads the same data, for example, popular products on an e-commerce platform, DAX can serve these requests directly from its cache.

- **Bursty traffic patterns**
  - **Smoother table scaling** – DAX helps smooth out impacts of sudden traffic spikes. DAX provides a buffer to scale up DynamoDB table capacity gracefully, which reduces the risk of read throttling.
  - **Higher read throughput for each item** – DynamoDB allocates individual partitions for each item. However, a partition starts throttling reads of an item when it reaches 3,000 [read capacity units](provisioned-capacity-mode.md#read-write-capacity-units "provisioned-capacity-mode.md#read-write-capacity-units") (RCU). DAX lets you scale reads of a single item beyond 3,000 RCU.

- **Cost optimization**
  - **Reducing DynamoDB costs** – Reading from DAX can reduce reads sent to a DynamoDB table, which can then directly impact cost. With a high cache hit rate, the reduced table read cost can exceed a DAX cluster cost, which results in a net cost reduction.

- **Data consistency requirements**
  - **Eventual consistency** – DAX supports eventually consistent reads. This makes DAX suitable for use cases where immediate consistency isn't critical.
  - **Write-through caching** – Writes that you make against DAX are [write-through](DAX.md "DAX.md"). Once DAX confirms that it's written an item to DynamoDB, it persists that item version in the item cache. This write-through mechanism helps maintain tighter data consistency between cache and database, but uses additional DAX cluster resources.

## When not to use DAX

While DAX is powerful, it's not suitable for all scenarios. The following list presents examples of scenarios in which integrating DAX with DynamoDB is unsuitable:

- **Write-heavy workloads** – The primary advantage of DAX is speeding up reads, but writes use more DAX resources than reads. If your application is predominantly write-heavy, DAX benefits might be limited.
- **Infrequently read data** – If your application accesses data infrequently or a wide range of rarely reused data (cold data), you'll likely experience a low [cache hit ratio](pres-guide-monitor-dax.md#cachehitratio "pres-guide-monitor-dax.md#cachehitratio"). In this case, the overhead of maintaining the cache might not justify the performance gains.
- **Bulk reads or writes** – If your application performs more bulk writes than individual writes, you should write around DAX. In addition, for bulk reads, you should run full table scans directly against a DynamoDB table.
- **Strong consistency or transaction requirements** – DAX passes strongly consistent reads and [TransactGetItems](../APIReference/API_TransactGetItems.md "../APIReference/API_TransactGetItems.md") calls to a DynamoDB table. You should make these reads around the DAX cluster to avoid using cluster resources. Items read this way won't be cached; therefore, routing such items through DAX serves no purpose.
- **Simple applications with modest performance requirements** – For applications with modest performance requirements and tolerance for direct DynamoDB latency, the complexity and cost of adding DAX might not be necessary. On its own, DynamoDB handles high throughput and provides single-digit millisecond performance.
- **Complex querying needs beyond key-value access** – DAX is optimized for key-value access patterns. If your application requires complex querying capabilities with complex filtering, such as [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") and [Scan](../APIReference/API_Scan.md "../APIReference/API_Scan.md") operations, DAX caching benefits might be limited.

In these situations, use [Amazon ElastiCache (Redis OSS)](../../../AmazonElastiCache/latest/red-ug/WhatIs.md "../../../AmazonElastiCache/latest/red-ug/WhatIs.md") as an alternative. ElastiCache (Redis OSS) supports advanced data structures, such as, lists, sets, and hashes. It also offers features, such as pub/sub, geospatial indexes, and scripting.

- **Compliance requirements** – DAX doesn't currently offer the same compliance accreditations as as DynamoDB. For example, DAX hasn't obtained the SOC accreditation yet.
