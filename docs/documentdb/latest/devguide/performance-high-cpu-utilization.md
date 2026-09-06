

# High CPU Utilization
<a name="performance-high-cpu-utilization"></a>

High CPU utilization is one of the issues you might encounter at some point while working with Amazon DocumentDB. This section provides insights to resolve the issue.

## Identification - Spot the problem
<a name="high-cpu-identification"></a>

High CPU utilization on Amazon DocumentDB instances causes application slowness by increasing latencies across all database operations. When Amazon DocumentDB CPU usage rises above optimal levels, query execution times increase, connection establishment takes longer, and application responsiveness decreases. CPU peaks on the primary instance slow write operations, while peaks on replicas result in higher latency for read operations.

Some of the Common Causes of High CPU Utilization in Amazon DocumentDB could be:
+ **Collection Scans**: Queries without proper indexes force full collection scans, consuming excessive CPU to examine every document.
+ **Connection Spikes**: Sudden surges in application connections overwhelm CPU resources needed for authentication and session management.
+ **Complex Aggregations**: Multi-stage operations (sorting, grouping, joining) consume significant CPU, especially on large datasets without optimized indexes.
+ **Inefficient Queries**: High CPU usage results from scanning large result sets and regex operations.
+ **Write-Heavy Workloads**: Frequent updates and bulk inserts strain CPU with document processing, index updates, and transaction logging.

## Investigate - Gather metrics
<a name="high-cpu-investigate"></a>

Amazon DocumentDB provides monitoring through Amazon CloudWatch. Amazon DocumentDB metrics can be broadly categorized into cluster level and instance level metrics. For resources related to CPU, memory, and connections, Look at the instance level metrics as the resource consumption is specific to the instance. Identify the instances (primary or replica) that are showing the CPU spikes and note the times of spike.

The CloudWatch metric for the CPU utilization for `CPUUtilization`.

## Diagnose - Find root cause
<a name="high-cpu-diagnose"></a>

After identifying the instance and timeline of the CPU spike, next is to diagnose for the cause that is impacting CPU usage by large. As there are multiple reasons that can cause CPU spike, lets identify what is contributing to it starting with:

**Connections**: Check CloudWatch metrics including, `DatabaseConnections` and `DatabaseConnectionsMax`, if there are spikes in connections and it coincides with the CPU spike time, the surge in connections over a short time is likely the cause of the CPU spike.

**Queries**: If it is not the connection, then a query might be the cause. If you have enabled performance insights, then go to the Performance insights console for the instance and see the queries on the instance. The other thing to look at queries is from profiler.

## Resolve - Fix the issue
<a name="high-cpu-resolve"></a>

**Connection bursts**: If connection bursts are the cause of CPU spikes, consider reusing connections in your application or implementing connection pooling. For more information on optimizing high connections, see [Connection issues with Amazon DocumentDB](performance-connection-issues.md).

**Query Distribution**: If the CPU spikes are caused by read queries on the primary instance, consider redirecting read operations to replica instances if your query results can be eventually consistent.

**Query optimizations**: If a query or set of queries are causing the CPU to spike, consider optimizing the query such as adding an index if the query is not using one. For more information on optimizing a query, see [Query running slow](performance-slow-queries.md).

**Instance Scaling**: If CPU utilization remains consistently high after optimization efforts, upgrade to a larger instance class with more CPU capacity to handle your workload requirements effectively.

**Serverless**: For unpredictable workloads causing short-duration CPU spikes, consider using [Using Amazon DocumentDB serverless](docdb-serverless.md). Serverless instances automatically scale resources based on demand, eliminating the need to provision fixed instance sizes for such workloads.