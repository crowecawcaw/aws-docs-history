

# Choosing between deployment options
<a name="WhatIs.deployment"></a>

Amazon ElastiCache has two deployment options:
+ Serverless caching
+ Node-based clusters

For a list of supported commands for both, see [Supported and restricted Valkey, Memcached, and Redis OSS commands](SupportedCommands.md).

**Serverless caching**

Amazon ElastiCache Serverless simplifies cache creation and instantly scales to support customers' most demanding applications. With ElastiCache Serverless, you can create a highly-available and scalable cache in less than a minute, eliminating the need to provision, plan for, and manage cluster capacity. ElastiCache Serverless automatically stores data redundantly across three Availability Zones and provides a 99.99% availability Service Level Agreement (SLA). Backups from Valkey or Redis OSS node-based clusters can be restored into a serverless configuration.

**Node-based clusters**

If you need fine-grained control over your Valkey, Memcached, or Redis OSS cluster, you can create a node-based cluster with ElastiCache. You choose the node-type, number of nodes, and node placement across AWS Availability Zones for your cluster. Since ElastiCache is a fully-managed service, it helps manage hardware provisioning, monitoring, node replacements, and software patching for your cluster. Node-based clusters can be designed to provide an up to 99.99% availability SLA. Backups from serverless Valkey or Redis OSS caches can be restored into a node-based cluster.

**Choosing between deployment options**

Choose serverless caching if:
+ You are creating a cache for workloads that are either new or difficult to predict.
+ You have unpredictable application traffic.
+ You want the easiest way to get started with a cache.

Create your own node-based cluster if:
+ You are already running ElastiCache Serverless and want finer grained control over the type of node running Valkey, Memcached, or Redis OSS, the number of nodes, and the placement of those nodes. 
+ You expect your application traffic to be relatively predictable, and you want fine-grained control over performance, availability, and cost. 
+ You can forecast your capacity requirements to control costs.
+ You need durability for your data. When creating a node-based Valkey 9.0\+ cluster, you can choose to enable durability through a Multi-AZ transactional log, enabling your cache to serve as a durable data store with zero data loss during failures.

## Comparing serverless caching and node-based clusters
<a name="WhatIs.deployment.comparing"></a>


| Feature | Serverless caching | Node-based clusters | 
| --- | --- | --- | 
| Cache setup | Create a cache with just a name in under a minute | Provides fine-grained control over cluster design. User can choose node-type, number of nodes, and placement across AWS availability zones | 
| Supported ElastiCache version | Valkey 7.2 and higher, Redis OSS version 7.1, Memcached 1.6.22 and higher | Valkey 7.2 and higher, Redis OSS version 4.0 to 7.1, Memcached 1.4 and higher | 
| Cluster Mode (Valkey and Redis OSS) | Operates engines in `cluster mode enabled` only. Clients must support `cluster mode enabled` to connect to ElastiCache Serverless. | Can be configured to operate in cluster mode enabled or cluster mode disabled. | 
| Scaling | Automatically scales engines both vertically and horizontally without any capacity management. | Provides control over scaling, while also requiring monitoring to make sure current capacity is adequately meeting demand.<br />For Valkey and Redis OSS, you can choose to scale vertically by increasing or decreasing the cache node size when needed. You can also scale horizontally, by adding new shards or adding more replicas to your shards. This capability is not available for Memcached.<br />With the Auto-Scaling feature you can also configure scaling based on a schedule, or scale based on metrics like CPU and Memory usage on the cache. | 
| Client connection | Clients connect to a single endpoint. This enables the underlying cache node topology (scaling, replacements, and upgrades) to change without disconnecting the client. | Clients connect to each individual cache node. If a node is replaced, the client rediscovers cluster topology and re-establishes connections. | 
| Configurability | No fine-grained configuration available. Customers can configure basic settings including subnets which can access the cache, whether automatic backups are turned on or off, and maximum cache usage limits.  | Node-based clusters provide fine-grained configuration options. Customers can use parameter groups for fine-grained control. For a table of these parameter values by node type, see [Engine specific parameters](ParameterGroups.Engine.md). | 
| Multi-AZ | Data is replicated asynchronously across multiple Availability Zones for higher availability and improved read latency. | Provides an option to create the cluster in a single Availability Zone or across multiple Availability Zones (AZs). When using Valkey or Redis OSS, provides Multi-AZ clusters with data replicated asynchronously across multiple Availability Zones for higher availability and improved read latency. | 
| Encryption at rest | Always enabled. Customers can use an AWS managed key or a customer managed key in AWS KMS. | Option to enable or disable encryption at rest. When enabled, customers can use an AWS managed key or a customer managed key in AWS KMS.  | 
| Encryption in transit (TLS) | Always enabled. Clients must support TLS connectivity.  | Option to enable or disable. | 
| Backups | Supports automatic and manual backups of caches with no performance impact.<br />Valkey and Redis OSS backups are cross-compatible, and can be restored into an ElastiCache Serverless cache or a node-based cluster. | Supports automatic and manual backups for Valkey and Redis OSS. Clusters may see some performance impact depending on the available reserved memory. For more information, see [Managing reserved memory for Valkey and Redis OSS](redis-memory-management.md).<br />Valkey and Redis OSS backups are cross-compatible, and can be restored into an ElastiCache Serverless cache or a node-based cluster. | 
| Monitoring | Support cache level metrics including cache hit rate, cache miss rate, data size, and ECPUs consumed.<br />ElastiCache Serverless sends events using EventBridge when significant events happen on your cache. You can choose to monitor, ingest, transform, and act on ElastiCache events using Amazon EventBridge. For more information, see [Serverless cache events](serverless-metrics-events-redis.md#serverless-events). | Node-based ElastiCache clusters emit metrics at each node level, including both host-level metrics and cache metrics.<br />Node-based clusters emit SNS notifications for significant events. See [Metrics for Memcached](CacheMetrics.Memcached.md) and [Metrics for Valkey and Redis OSS](CacheMetrics.Redis.md). | 
| Availability | 99.99% availability [Service Level Agreement (SLA)](https://aws.amazon.com/elasticache/sla/) | Node-based clusters can be designed to achieve up to 99.99% availability [Service Level Agreement (SLA)](https://aws.amazon.com/elasticache/sla/), depending on the configuration. | 
| Software upgrades and patching | Automatically upgrades cache software to the latest minor and patch version, without application impact. Customers receive a notification for major version upgrades, and customers can upgrade to the latest major version when they want. | Node-based clusters offer customer-enabled self-service for minor and patching version upgrades, as well as major version upgrades. Managed updates are automatically applied during customer defined maintenance windows. Customers can also choose to apply a minor or patch version upgrade on-demand.  | 
| Global Data Store  | Not supported  | Supports Global Data Store, which enables cross region replication with single region writes and multi-region reads | 
| Data Tiering | Not supported | Clusters that are created using nodes from the r6gd family have their data tiered between memory and local SSD (solid state drives) storage. Data tiering provides a price-performance option for Valkey and Redis OSS workloads by utilizing lower-cost solid state drives (SSDs) in each cluster node, in addition to storing data in memory. | 
| Durability | Not supported | Supported for Valkey 9.0 and higher. Provides synchronous or asynchronous writes through a Multi-AZ transactional log. | 
| Pricing model | Pay-per-use, based on data stored in GB-hours and requests in ElastiCache Processing Units (ECPU). See pricing details [here](https://aws.amazon.com/elasticache/pricing/). | Pay-per-hour, based on cache node usage. See pricing details [here](https://aws.amazon.com/elasticache/pricing/). | 

Related topics:
+ [Creating and managing a node-based ElastiCache cluster](designing-elasticache-cluster.md)