# Amazon ElastiCache Well-Architected Lens

Performance Efficiency Pillar

The performance efficiency pillar focuses on using IT and computing resources
efficiently. Key topics include selecting the right resource types and sizes based on
workload requirements, monitoring performance, and making informed decisions to maintain
efficiency as business needs evolve.

###### Topics

- [PE 1: How do you monitor the performance of your Amazon ElastiCache cluster?](#PerformanceEfficiencyPillarPE1 "#PerformanceEfficiencyPillarPE1")
- [PE 2: How are you distributing work across your ElastiCache Cluster
  nodes?](#PerformanceEfficiencyPillarPE2 "#PerformanceEfficiencyPillarPE2")
- [PE 3: For caching workloads, how do you track and report the effectiveness
  and performance of your cache?](#PerformanceEfficiencyPillarPE3 "#PerformanceEfficiencyPillarPE3")
- [PE 4: How does your workload optimize the use of networking resources and
  connections?](#PerformanceEfficiencyPillarPE4 "#PerformanceEfficiencyPillarPE4")
- [PE 5: How do you manage key deletion and/or eviction?](#PerformanceEfficiencyPillarPE5 "#PerformanceEfficiencyPillarPE5")
- [PE 6: How do you model and interact with data in ElastiCache?](#PerformanceEfficiencyPillarPE6 "#PerformanceEfficiencyPillarPE6")
- [PE 7: How do you log slow running commands in your Amazon ElastiCache cluster?](#PerformanceEfficiencyPillarPE7 "#PerformanceEfficiencyPillarPE7")
- [PE8: How does Auto Scaling help in increasing the performance of the
  ElastiCache cluster?](#PerformanceEfficiencyPillarPE8 "#PerformanceEfficiencyPillarPE8")

## PE 1: How do you monitor the performance of your Amazon ElastiCache cluster?

**Question-level introduction:** By understanding the
existing monitoring metrics, you can identify current utilization. Proper monitoring
can help identify potential bottlenecks impacting the performance of your cluster.

**Question-level benefit:** Understanding the metrics
associated with your cluster can help guide optimization techniques that can lead to
reduced latency and increased throughput.

- **[Required]** Baseline performance testing
  using a subset of your workload.
  - You should monitor performance of the actual workload using
    mechanisms such as load testing.
  - Monitor the CloudWatch metrics while running these tests to gain
    an understanding of metrics available, and to establish a
    performance baseline.

- **[Best]** For ElastiCache for Valkey and Redis OSS
  workloads, rename computationally expensive commands, such as
  `KEYS`, to limit the ability of users to run blocking
  commands on production clusters.
  - ElastiCache workloads running engine 6.x for Redis OSS can leverage
    role-based access control to restrict certain commands. Access to
    the commands can be controlled by creating Users and User Groups
    with the AWS Console or CLI, and associating the User Groups to a
    cluster. In Redis OSS 6, when RBAC is enabled, we
    can use "-@dangerous" and it will disallow expensive commands like
    KEYS, MONITOR, SORT, etc. for that user.
  - For engine version 5.x, rename commands using the
    `rename-commands` parameter on the cluster parameter group.

- **[Better]** Analyze slow queries and look
  for optimization techniques.
  - For ElastiCache for Valkey and Redis OSS workloads, learn more about your queries
    by analyzing the Slow Log. For example, you can use the following
    command, `valkey-cli slowlog get 10` to show last 10
    commands which exceeded latency thresholds (10 milliseconds by
    default).
  - Certain queries can be performed more efficiently using complex
    ElastiCache for Valkey and Redis OSS data structures. As an example, for numerical
    style range lookups, an application can implement simple numerical
    indexes with Sorted Sets. Managing these indexes can reduce scans
    performed on the data set, and return data with greater performance
    efficiency.
  - For ElastiCache for Valkey and Redis OSS workloads, `redis-benchmark`
    provides a simple interface for testing the performance of different
    commands using user defined inputs like number of clients, and size
    of data.
  - Since Memcached only supports simple key level commands, consider
    building additional keys as indexes to avoid iterating through the
    key space to serve client queries.

- **[Resources]:**
  - [Monitoring use with CloudWatch Metrics](CacheMetrics.md "CacheMetrics.md")
  - [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
  - [Valkey and Redis OSS specific parameters](ParameterGroups.md#ParameterGroups.Redis "ParameterGroups.md#ParameterGroups.Redis")
  - [SLOWLOG](https://valkey.io/commands/slowlog/ "https://valkey.io/commands/slowlog/")
  - [benchmark](https://valkey.io/topics/benchmark/ "https://valkey.io/topics/benchmark/")

## PE 2: How are you distributing work across your ElastiCache Cluster

nodes?

**Question-level introduction:** The way your
application connects to Amazon ElastiCache nodes can impact the performance and scalability
of the cluster.

**Question-level benefit:** Making proper use of the
available nodes in the cluster will ensure that work is distributed across the
available resources. The following techniques help avoid idle resources as
well.

- **[Required]** Have clients connect to the
  proper ElastiCache endpoint.
  - ElastiCache for Valkey and Redis OSS implements different endpoints based on the
    cluster mode in use. For cluster mode enabled, ElastiCache will
    provide a configuration endpoint. For cluster mode disabled,
    ElastiCache provides a primary endpoint, typically used for writes,
    and a reader endpoint for balancing reads across replicas.
    Implementing these endpoints correctly will results in better
    performance, and easier scaling operations. Avoid connecting to
    individual node endpoints unless there is a specific requirement to
    do so.
  - For multi-node Memcached clusters, ElastiCache provides a
    configuration endpoint which enables Auto Discovery. It is
    recommended to use a hashing algorithm to distribute work evenly
    across the cache nodes. Many Memcached client libraries implement
    consistent hashing. Check the documentation for the library you are
    using to see if it supports consistent hashing and how to implement
    it. You can find more information on implementing these features
    [here](BestPractices.md "BestPractices.md").

- **[Better]** Take advantage of ElastiCache for Valkey and Redis OSS cluster mode enabled clusters to improve scalability.
  - ElastiCache for Valkey and Redis OSS (cluster mode enabled) clusters support
    [online scaling operations](scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online "scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online") (out/in and up/down) to help
    distribute data dynamically across shards. Using the Configuration
    Endpoint will ensure your cluster aware clients can adjust to
    changes in the cluster topology.
  - You may also rebalance the cluster by moving hashslots between
    available shards in your ElastiCache for Valkey and Redis OSS (cluster mode
    enabled) cluster. This helps distribute work more efficiently across
    available shards.

- **[Better]** Implement a strategy for
  identifying and remediating hot keys in your workload.
  - Consider the impact of multi-dimensional Valkey or Redis OSS data structures
    such a lists, streams, sets, etc. These data structures are stored
    in single Keys, which reside on a single node. A very large
    multi-dimensional key has the potential to utilize more network
    capacity and memory than other data types and can cause a
    disproportionate use of that node. If possible, design your workload
    to spread out data access across many discrete Keys.
  - Hot keys in the workload can impact performance of the node in
    use. For ElastiCache for Valkey and Redis OSS workloads, you can detect hot keys
    using `valkey-cli --hotkeys` if an LFU max-memory policy
    is in place.
  - Consider replicating hot keys across multiple nodes to distribute
    access to them more evenly. This approach requires the client to
    write to multiple primary nodes (the Valkey or Redis OSS node itself will not
    provide this functionality) and to maintain a list of key names to
    read from, in addition to the original key name.
  - ElastiCache engine 7.2 for Valkey and above, and ElastiCache version 6 for Redis OSS and above, all support server-assisted [client-side caching](https://valkey.io/topics/client-side-caching/ "https://valkey.io/topics/client-side-caching/"). This enables applications to wait
    for changes to a key before making network calls back to
    ElastiCache.

- **[Resources]:**
  - [Configure ElastiCache for Valkey and Redis OSS for higher availability](https://aws.amazon.com/blogs/database/configuring-amazon-elasticache-for-redis-for-higher-availability/ "https://aws.amazon.com/blogs/database/configuring-amazon-elasticache-for-redis-for-higher-availability/")
  - [Finding connection endpoints in ElastiCache](Endpoints.md "Endpoints.md")
  - [Load balancing best practices](BestPractices.md "BestPractices.md")
  - [Online resharding for Valkey or Redis OSS (cluster mode enabled)](scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online "scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online")
  - [Client-side caching in Valkey and Redis OSS](https://valkey.io/topics/client-side-caching/ "https://valkey.io/topics/client-side-caching/")

## PE 3: For caching workloads, how do you track and report the effectiveness

and performance of your cache?

**Question-level introduction:** Caching is a
commonly encountered workload on ElastiCache and it is important that you understand
how to manage the effectiveness and performance of your cache.

**Question-level benefit:** Your application may show
signs of sluggish performance. Your ability to use cache specific metrics to inform
your decision on how to increase app performance is critical for your cache
workload.

- **[Required]** Measure and track over time
  the cache-hits ratio. The efficiency of your cache is determined by its
  ‘cache hits ratio’. The cache hits ratio is defined by the total of key hits
  divided by the total hits and misses. The closer to 1 the ratio is, the more
  effective your cache is. A low cache hits ratio is caused by the volume of
  cache misses. Cache misses occur when the requested key is not found in the
  cache. A key is not in the cache because it either has been evicted or
  deleted, has expired, or has never existed. Understand why keys are not in
  cache and develop appropriate strategies to have them in cache.

**[Resources]:**

    + [Metrics for Valkey and Redis OSS](CacheMetrics.md "CacheMetrics.md")

- **[Required]** Measure and collect your
  application cache performance in conjunction with latency and CPU
  utilization values to understand whether you need to make adjustments to
  your time-to-live or other application components. ElastiCache provides a
  set of CloudWatch metrics for aggregated latencies for each data structure.
  These latency metrics are calculated using the commandstats statistic from
  the INFO command and do not include the network and
  I/O time. This is only the time consumed by ElastiCache to process
  the operations.

**[Resources]:**

    + [Metrics for Valkey and Redis OSS](CacheMetrics.md "CacheMetrics.md")
    + [Monitoring best practices with ElastiCache using Amazon
     CloudWatch](https://aws.amazon.com/blogs/database/monitoring-best-practices-with-amazon-elasticache-for-redis-using-amazon-cloudwatch/ "https://aws.amazon.com/blogs/database/monitoring-best-practices-with-amazon-elasticache-for-redis-using-amazon-cloudwatch/")

- **[Best]** Choose the right caching strategy
  for your needs. A low cache hits ratio is caused by the volume of cache
  misses. If your workload is designed to have low volume of cache misses
  (such as real time communication), it is best to conduct reviews of your
  caching strategies and apply the most appropriate resolutions for your
  workload, such as query instrumentation to measure memory and performance.
  The actual strategies you use to implement for populating and maintaining
  your cache depend on what data your clients need to cache and the access
  patterns to that data. For example, it is unlikely that you will use the
  same strategy for both personalized recommendations on a streaming
  application, and for trending news stories.

**[Resources]:**

    + [Caching strategies for Memcached](Strategies.md "Strategies.md")
    + [Caching Best Practices](https://aws.amazon.com/caching/best-practices/ "https://aws.amazon.com/caching/best-practices/")
    + [Performance at Scale with Amazon ElastiCache Whitepaper](https://d0.awsstatic.com/whitepapers/performance-at-scale-with-amazon-elasticache.pdf "https://d0.awsstatic.com/whitepapers/performance-at-scale-with-amazon-elasticache.pdf")

## PE 4: How does your workload optimize the use of networking resources and

connections?

**Question-level introduction:** ElastiCache for Valkey, Memcached, and Redis OSS are supported by many application clients, and implementations
may vary. You need to understand the networking and connection management in place
to analyze potential performance impact.

**Question-level benefit:** Efficient use of
networking resources can improve the performance efficiency of your cluster. The
following recommendations can reduce networking demands, and improve cluster latency
and throughput.

- **[Required]** Proactively manage connections
  to your ElastiCache cluster.
  - Connection pooling in the application reduces the amount of
    overhead on the cluster created by opening and closing connections.
    Monitor connection behavior in Amazon CloudWatch using
    `CurrConnections` and
    `NewConnections`.
  - Avoid connection leaking by properly closing client connections
    where appropriate. Connection management strategies include properly
    closing connections that are not in use, and setting connection
    time-outs.
  - For Memcached workloads, there is a configurable amount of memory
    reserved for handling connections called,
    `memcached_connections_overhead`.

- **[Better]** Compress large objects to reduce
  memory, and improve network throughput.
  - Data compression can reduce the amount of network throughput
    required (Gbps), but increases the amount of work on the application
    to compress and decompress data.
  - Compression also reduces the amount of memory consumed by
    keys
  - Based on your application needs, consider the trade-offs between
    compression ratio and compression speed.

- **[Resources]:**
  - [ElastiCache - Global Datastore](https://aws.amazon.com/elasticache/redis/global-datastore/ "https://aws.amazon.com/elasticache/redis/global-datastore/")
  - [Memcached specific parameters](ParameterGroups.md#ParameterGroups.Memcached "ParameterGroups.md#ParameterGroups.Memcached")
  - [ElastiCache version 5.0.3 for Redis OSS enhances I/O handling to boost
    performance](https://aws.amazon.com/about-aws/whats-new/2019/03/amazon-elasticache-for-redis-503-enhances-io-handling-to-boost-performance/ "https://aws.amazon.com/about-aws/whats-new/2019/03/amazon-elasticache-for-redis-503-enhances-io-handling-to-boost-performance/")
  - [Metrics for Valkey and Redis OSS](CacheMetrics.md "CacheMetrics.md")
  - [Configure ElastiCache for higher
    availability](https://aws.amazon.com/blogs/database/configuring-amazon-elasticache-for-redis-for-higher-availability/ "https://aws.amazon.com/blogs/database/configuring-amazon-elasticache-for-redis-for-higher-availability/")

## PE 5: How do you manage key deletion and/or eviction?

**Question-level introduction:** Workloads have
different requirements, and expected behavior when a cluster node is approaching
memory consumption limits. ElastiCache has different policies for handling
these situations.

**Question-level benefit:** Proper management of
available memory, and understanding of eviction policies will help ensure awareness
of cluster behavior when instance memory limits are exceeded.

- **[Required]** Instrument the data access to
  evaluate which policy to apply. Identify an appropriate max-memory policy to
  control if and how evictions are performed on the cluster.
  - Eviction occurs when the max-memory on the cluster is consumed and
    a policy is in place to allow eviction. The behavior of the cluster
    in this situation depends on the eviction policy specified. This
    policy can be managed using the `maxmemory-policy` on the
    cluster parameter group.
  - The default policy `volatile-lru` frees up memory by
    evicting keys with a set expiration time (TTL value). Least
    frequently used (LFU) and least recently used (LRU) policies remove
    keys based on usage.
  - For Memcached workloads, there is a default LRU policy in place
    controlling evictions on each node. The number of evictions on your
    Amazon ElastiCache cluster can be monitored using the Evictions metric on
    Amazon CloudWatch.

- **[Better]** Standardize delete behavior to
  control performance impact on your cluster to avoid unexpected performance
  bottlenecks.
  - For ElastiCache for Valkey and Redis OSS workloads, when explicitly removing keys
    from the cluster, `UNLINK` is like `DEL`: it
    removes the specified keys. However, the command performs the actual
    memory reclaiming in a different thread, so it is not blocking,
    while `DEL` is. The actual removal will happen later
    asynchronously.
  - For ElastiCache version 6.x for Redis OSS workloads, the behavior of the
    `DEL` command can be modified in the parameter group
    using `lazyfree-lazy-user-del` parameter.

- **[Resources]:**
  - [Configuring engine parameters using ElastiCache parameter
    groups](ParameterGroups.md "ParameterGroups.md")
  - [UNLINK](https://valkey.io/commands/unlink/ "https://valkey.io/commands/unlink/")
  - [Cloud Financial Management with AWS](https://aws.amazon.com/aws-cost-management/ "https://aws.amazon.com/aws-cost-management/")

## PE 6: How do you model and interact with data in ElastiCache?

**Question-level introduction:** ElastiCache is
heavily application dependent on the data structures and the data model used, but it
also needs to consider the underlying data store (if present). Understand the
data structures available and ensure you are using the most
appropriate data structures for your needs.

**Question-level benefit:** Data modeling in
ElastiCache has several layers, including application use case, data types, and
relationships between data elements. Additionally, each data
type and command have their own well documented performance signatures.

- **[Best]** A best practice is to reduce
  unintentional overwriting of data. Use a naming convention that minimizes
  overlapping key names. Conventional naming of your data structures uses a
  hierarchical method such as: `APPNAME:CONTEXT:ID`, such as
  `ORDER-APP:CUSTOMER:123`.

**[Resources]:**

    + [Key naming](https://docs.gitlab.com/ee/development/redis.html#key-naming "https://docs.gitlab.com/ee/development/redis.html#key-naming")

- **[Best]** ElastiCache for Valkey and Redis OSS commands
  have a time complexity defined by the Big O notation. This time complexity
  of a command is a algorithmic/mathematical representation of its impact.
  When introducing a new data type in your application you need to carefully
  review the time complexity of the related commands. Commands with a time
  complexity of O(1) are constant in time and do not depend on the size of the
  input however commands with a time complexity of O(N) are linear in time and
  are subject to the size of the input. Due to the single threaded design of
  ElastiCache for Valkey and Redis OSS, large volume of high time complexity operations will
  result in lower performance and potential operation timeouts.

**[Resources]:**

    + [Commands](https://valkey.io/commands/ "https://valkey.io/commands/")

- **[Best]** Use APIs to gain GUI visibility
  into the data model in your cluster.

**[Resources]:**

    + [Redis OSS Commander](https://www.npmjs.com/package/ElastiCache for Redis-commander "https://www.npmjs.com/package/ElastiCache for Redis-commander")
    + [Redis OSS Browser](https://github.com/humante/redis-browser "https://github.com/humante/redis-browser")
    + [Redsmin](https://www.redsmin.com/ "https://www.redsmin.com/")

## PE 7: How do you log slow running commands in your Amazon ElastiCache cluster?

**Question-level introduction:** Performance tuning
benefits through the capture, aggregation, and notification of long-running
commands. By understanding how long it takes for commands to execute, you can
determine which commands result in poor performance as well as commands that block
the engine from performing optimally. ElastiCache also has the capability to
forward this information to Amazon CloudWatch or Amazon Kinesis Data
Firehose.

**Question-level benefit:** Logging to a dedicated
permanent location and providing notification events for slow commands can help with
detailed performance analysis and can be used to trigger automated events.

- **[Required]** ElastiCache running a Valkey engine 7.2 or newer, or running a
  Redis OSS engine version 6.0 or newer, properly configured parameter group and SLOWLOG
  logging enabled on the cluster.
  - The required parameters are only available when engine version
    compatibility is set to Valkey 7.2 and higher, or Redis OSS version 6.0 or higher.
  - SLOWLOG logging occurs when the server execution time of a command
    takes longer than a specified value. The behavior of the cluster
    depends on the associated Parameter Group parameters which are
    `slowlog-log-slower-than` and
    `slowlog-max-len`.
  - Changes take effect immediately.

- **[Best]** Take advantage of CloudWatch or
  Kinesis Data Firehose capabilities.
  - Use the filtering and alarm capabilities of CloudWatch, CloudWatch
    Logs Insights and Amazon Simple Notification Services to achieve
    performance monitoring and event notification.
  - Use the streaming capabilities of Kinesis Data Firehose to archive
    SLOWLOG logs to permanent storage or to trigger automated cluster
    parameter tuning.
  - Determine if JSON or plain TEXT format suits your needs
    best.
  - Provide IAM permissions to publish to CloudWatch or Kinesis Data
    Firehose.

- **[Better]** Configure
  `slowlog-log-slower-than` to a value other than the
  default.
  - This parameter determines how long a command may execute for
    within the Valkey or Redis OSS engine before it is logged as a slow running
    command. The default value is 10,000 microseconds (10 milliseconds).
    The default value may be too high for some workloads.
  - Determine a value that is more appropriate for your workload based
    on application needs and testing results; however, a value that is
    too low may generate excessive data.

- **[Better]** Leave
  `slowlog-max-len` at the default value.
  - This parameter determines the upper limit for how many
    slow-running commands are captured in Valkey or Redis OSS memory at any given
    time. A value of 0 effectively disables the capture. The higher the
    value, the more entries will be stored in memory, reducing the
    chance of important information being evicted before it can be
    reviewed. The default value is 128.
  - The default value is appropriate for most workloads. If there is a
    need to analyze data in an expanded time window from the valkey-cli
    via the SLOWLOG command, consider increasing this value. This allows
    more commands to remain in Valkey or Redis OSS memory.

  If you are emitting the SLOWLOG data to either CloudWatch Logs or
  Kinesis Data Firehose, the data will be persisted and can be
  analyzed outside of the ElastiCache system, reducing the need to
  store large numbers of slow running commands in Valkey or Redis OSS memory.

- **[Resources]:**
  - [How do I turn on Slow log in a cluster?](https://repost.aws/knowledge-center/elasticache-turn-on-slow-log "https://repost.aws/knowledge-center/elasticache-turn-on-slow-log")
  - [Log
    delivery](Log_Delivery.md "Log_Delivery.md")
  - [Redis OSS-specific parameters](ParameterGroups.md#ParameterGroups.Redis "ParameterGroups.md#ParameterGroups.Redis")
  - [https://aws.amazon.com/cloudwatch/](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")Amazon CloudWatch
  - [Amazon
    Kinesis Data Firehose](https://aws.amazon.com/kinesis/data-firehose/ "https://aws.amazon.com/kinesis/data-firehose/")

## PE8: How does Auto Scaling help in increasing the performance of the

ElastiCache cluster?

**Question-level introduction:** By implementing the
feature of Valkey or Redis OSS auto scaling, your ElastiCache components can adjust over time to
increase or decrease the desired shards or replicas automatically. This can be done
by implementing either the target tracking or scheduled scaling policy.

**Question-level benefit:** Understanding and
planning for the spikes in the workload can ensure enhanced caching performance and
business continuity. ElastiCache Auto Scaling continually monitors your
CPU/Memory utilization to make sure your cluster is operating at your desired
performance levels.

- **[Required]** When launching a cluster for
  ElastiCache for Valkey or Redis OSS:

      1. Ensure that the Cluster mode is enabled
      2. Make sure the instance belongs to a family of certain type and
       size that support auto scaling
      3. Ensure the cluster is not running in Global datastores, Outposts
       or Local Zones

  **[Resources]:**

      + [Scaling clusters in Valkey and Redis OSS (Cluster Mode Enabled)](scaling-redis-cluster-mode-enabled.md "scaling-redis-cluster-mode-enabled.md")
      + [Using Auto Scaling with shards](AutoScaling-Using-Shards.md "AutoScaling-Using-Shards.md")
      + [Using Auto Scaling with replicas](AutoScaling-Using-Replicas.md "AutoScaling-Using-Replicas.md")

- **[Best]** Identify if your workload is
  read-heavy or write-heavy to define scaling policy. For best performance,
  use just one tracking metric. It is recommended to avoid multiple policies
  for each dimension, as auto scaling policies scale out when the target is
  hit, but scale in only when all target tracking policies are ready to scale
  in.

**[Resources]:**

    + [Auto Scaling policies](AutoScaling-Policies.md "AutoScaling-Policies.md")
    + [Defining a scaling policy](AutoScaling-Scaling-Defining-Policy-API.md "AutoScaling-Scaling-Defining-Policy-API.md")

- **[Best]** Monitoring performance over time
  can help you detect workload changes that would remain unnoticed if
  monitored at a particular point in time. You can analyze corresponding
  CloudWatch metrics for cluster utilization over a four-week period to
  determine the target value threshold. If you are still not sure of what
  value to choose, we recommend starting with a minimum supported predefined
  metric value.

**[Resources]:**

    + [Monitoring use with CloudWatch Metrics](CacheMetrics.md "CacheMetrics.md")

- **[Better]** We advise testing your
  application with expected minimum and maximum workloads, to identify the
  exact number of shards/replicas required for the cluster to develop scaling
  policies and mitigate availability issues.

**[Resources]:**

    + [Registering a Scalable Target](AutoScaling-Register-Policy.md "AutoScaling-Register-Policy.md")
    + [Registering a Scalable Target using the AWS CLI](AutoScaling-Scaling-Registering-Policy-CLI.md "AutoScaling-Scaling-Registering-Policy-CLI.md")
