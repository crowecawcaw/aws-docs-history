# Amazon ElastiCache Well-Architected Lens Reliability Pillar

The reliability pillar focuses on workloads performing their intended functions and how to recover quickly from failure to meet demands. Key topics include distributed system design, recovery planning, and adapting to changing requirements.

###### Topics

- [REL 1: How are you supporting high availability (HA) architecture deployments?](#ReliabilityPillarREL1 "#ReliabilityPillarREL1")
- [REL 2: How are you meeting your Recovery Point Objectives (RPOs) with ElastiCache?](#ReliabilityPillarREL2 "#ReliabilityPillarREL2")
- [REL 3: How do you support disaster recovery (DR) requirements?](#ReliabilityPillarREL3 "#ReliabilityPillarREL3")
- [REL 4: How do you effectively plan for failovers?](#ReliabilityPillarREL4 "#ReliabilityPillarREL4")
- [REL 5: Are your ElastiCache components designed to scale?](#ReliabilityPillarREL5 "#ReliabilityPillarREL5")

## REL 1: How are you supporting high availability (HA) architecture deployments?

**Question-level introduction:** Understanding the
high availability architecture of Amazon ElastiCache will enable you to operate in a
resilient state during availability events.

**Question-level benefit:** Architecting your
ElastiCache clusters to be resilient to failures ensures higher availability for
your ElastiCache deployments.

- **[Required]** Determine the level of
  reliability you require for your ElastiCache cluster. Different workloads
  have different resiliency standards, from entirely ephemeral to mission
  critical workloads. Define needs for each type of environment you operate
  such as dev, test, and production.

Caching engine: ElastiCache for Memcached vs ElastiCache for Valkey and Redis OSS

    1. ElastiCache for Memcached does not provide any replication mechanism and is used
     primarily for ephemeral workloads.
    2. ElastiCache for Valkey and Redis OSS offers HA features discussed below

- **[Best]** For workloads that require HA, use
  ElastiCache in cluster mode with a minimum of two replicas per
  shard, even for small throughput requirement workloads that require only one
  shard.

      1. For cluster mode enabled, multi-AZ is enabled
       automatically.


      Multi-AZ minimizes downtime by performing automatic failovers from
       primary node to replicas, in case of any planned or unplanned
       maintenance as well as mitigating AZ failure.
      2. For sharded workloads, a minimum of three shards provides faster
       recovery during failover events as the Valkey or Redis OSS Cluster Protocol
       requires a majority of primary nodes be available to achieve
       quorum.
      3. Set up two or more replicas across Availability.


      Having two replicas provides improved read scalability and also
       read availability in scenarios where one replica is undergoing
       maintenance.
      4. Use Graviton2-based node types (default nodes in most
       regions).


      ElastiCache has added optimized performance on these
       nodes. As a result, you get better replication and synchronization
       performance, resulting in overall improved availability.
      5. Monitor and right-size to deal with anticipated traffic peaks:
       under heavy load, the engine may become
       unresponsive, which affects availability.
       `BytesUsedForCache` and
       `DatabaseMemoryUsagePercentage` are good indicators
       of your memory usage, whereas `ReplicationLag` is an
       indicator of your replication health based on your write rate. You
       can use these metrics to trigger cluster scaling.
      6. Ensure client-side resiliency by testing with the [Failover API prior to a production failover
       event](https://docs.amazonaws.cn/en_us/AmazonElastiCache/latest/APIReference/API_TestFailover.html "https://docs.amazonaws.cn/en_us/AmazonElastiCache/latest/APIReference/API_TestFailover.html").

  **[Resources]:**

      + [Configure ElastiCache for Redis OSS for higher
       availability](https://aws.amazon.com/blogs/database/configuring-amazon-elasticache-for-redis-for-higher-availability/ "https://aws.amazon.com/blogs/database/configuring-amazon-elasticache-for-redis-for-higher-availability/")
      + [High
       availability using replication groups](Replication.md "Replication.md")

## REL 2: How are you meeting your Recovery Point Objectives (RPOs) with ElastiCache?

**Question-level introduction:** Understand workload
RPO to inform decisions on ElastiCache backup and recovery strategies.

**Question-level benefit:** Having an in-place RPO
strategy can improve business continuity in the event of a disaster recovery
scenarios. Designing your backup and restore policies can help you meet your
Recovery Point Objectives (RPO) for your ElastiCache data. ElastiCache
offers snapshot capabilities which are stored in Amazon S3, along with a
configurable retention policy. These snapshots are taken during a defined backup
window, and handled by the service automatically. If your workload requires
additional backup granularity, you have the option to create up to 20 manual backups
per day. Manually created backups do not have a service retention policy and can be
kept indefinitely.

- **[Required]** Understand and document the
  RPO of your ElastiCache deployments.
  - Be aware that Memcached does not offer any backup
    processes.
  - Review the capabilities of ElastiCache Backup and Restore
    features.

- **[Best]** Have a well-communicated process
  in place for backing up your cluster.
  - Initiate manual backups on an as-needed basis.
  - Review retention policies for automatic backups.
  - Note that manual backups will be retained indefinitely.
  - Schedule your automatic backups during periods of low
    usage.
  - Perform backup operations against read-replicas to ensure you
    minimize the impact on cluster performance.

- **[Good]** Leverage the scheduled backup
  feature of ElastiCache to regularly back up your data during a defined
  window.
  - Periodically test restores from your backups.

- **[Resources]:**
  - [Redis OSS](https://aws.amazon.com/elasticache/faqs/#Redis "https://aws.amazon.com/elasticache/faqs/#Redis")
  - [Backup and
    restore for ElastiCache](backups.md "backups.md")
  - [Making
    manual backups](backups-manual.md "backups-manual.md")
  - [Scheduling automatic backups](backups-automatic.md "backups-automatic.md")
  - [Backup and Restore ElastiCache Clusters](https://aws.amazon.com/blogs/aws/backup-and-restore-elasticache-redis-nodes/ "https://aws.amazon.com/blogs/aws/backup-and-restore-elasticache-redis-nodes/")

## REL 3: How do you support disaster recovery (DR) requirements?

**Question-level introduction:** Disaster recovery is
an important aspect of any workload planning. ElastiCache offers several
options to implement disaster recovery based on workload resilience requirements.
With Amazon ElastiCache Global Datastore, you can write to your cluster in one Region and have the data available to be read from two other
cross-Region replica clusters, thereby enabling low-latency reads and disaster
recovery across regions.

**Question-level benefit:** Understanding and
planning for a variety of disaster scenarios can ensure business continuity. DR
strategies must be balanced against cost, performance impact, and data loss
potential.

- **[Required]** Develop and document DR
  strategies for all your ElastiCache components based upon workload
  requirements. ElastiCache is unique in that some use cases are entirely
  ephemeral and don’t require any DR strategy, whereas others are on the
  opposite end of the spectrum and require an extremely robust DR strategy.
  All options must be weighed against Cost Optimization – greater resiliency
  requires larger amounts of instrastructure.

Understand the DR options available on a regional and multi-region
level.

    + Multi-AZ Deployments are recommended to guard against AZ failure.
     Be sure to deploy with Cluster-Mode enabled in Multi-AZ
     architectures, with a minimum of 3 AZs available.
    + Global Datastore is recommended to guard against regional
     failures.

- **[Best]** Enable Global Datastore for
  workloads that require region level resiliency.
  - Have a plan to failover to secondary region in case of primary
    degradation.
  - Test multi-region failover process prior to a failover over in
    production.
  - Monitor `ReplicationLag` metric to understand potential
    impact of data loss during failover events.

- **[Resources]:**
  - [Mitigating Failures](disaster-recovery-resiliency.md#FaultTolerance "disaster-recovery-resiliency.md#FaultTolerance")
  - [Replication across AWS Regions using global
    datastores](Redis-Global-Datastore.md "Redis-Global-Datastore.md")
  - [Restoring from a backup with optional cluster
    resizing](backups-restoring.md "backups-restoring.md")
  - [Minimizing downtime in ElastiCache for Valkey and Redis OSS with
    Multi-AZ](AutoFailover.md "AutoFailover.md")

## REL 4: How do you effectively plan for failovers?

**Question-level introduction:** Enabling multi-AZ
with automatic failovers is an ElastiCache best practice. In certain cases,
ElastiCache for Valkey and Redis OSS replaces primary nodes as part of service operations. Examples
include planned maintenance events and the unlikely case of a node failure or
availability zone issue. Successful failovers rely on both ElastiCache and your
client library configuration.

**Question-level benefit:** Following best practices
for ElastiCache failovers in conjunction with your specific ElastiCache
client library helps you minimize potential downtime during failover events.

- **[Required]** For cluster mode disabled, use
  timeouts so your clients detect if it needs to disconnect from the old
  primary node and reconnect to the new primary node, using the updated
  primary endpoint IP address. For cluster mode enabled, the client library is
  responsible with detecting changes in the underlying cluster topology. This
  is accomplished most often by configuration settings in the ElastiCache client library, which also allow you to configure the frequency and
  the method of refresh. Each client library offers its own settings and more
  details are available in their corresponding documentation.

**[Resources]:**

    + [Minimizing downtime in ElastiCache for Valkey and Redis OSS with
     Multi-AZ](AutoFailover.md "AutoFailover.md")
    + Review the best practices of your ElastiCache client
     library.

- **[Required]** Successful failovers depend on
  a healthy replication environment between the primary and the replica nodes.
  Review and understand the asynchronous nature of Valkey and Redis OSS replication, as well
  as the available CloudWatch metrics to report on the replication lag between
  primary and replica nodes. For use cases that require greater data safety,
  leverage the WAIT command to force replicas to acknowledge writes
  before responding to connected clients.

**[Resources]:**

    + [Metrics for Valkey or Redis OSS](CacheMetrics.md "CacheMetrics.md")
    + [Monitoring best practices with ElastiCache using Amazon CloudWatch](https://aws.amazon.com/blogs/database/monitoring-best-practices-with-amazon-elasticache-for-redis-using-amazon-cloudwatch/ "https://aws.amazon.com/blogs/database/monitoring-best-practices-with-amazon-elasticache-for-redis-using-amazon-cloudwatch/")

- **[Best]** Regularly validate the
  responsiveness of your application during failover using the ElastiCache
  Test Failover API.

**[Resources]:**

    + [Testing Automatic Failover to a Read Replica on ElastiCache](https://aws.amazon.com/blogs/database/testing-automatic-failover-to-a-read-replica-on-amazon-elasticache-for-redis/ "https://aws.amazon.com/blogs/database/testing-automatic-failover-to-a-read-replica-on-amazon-elasticache-for-redis/")
    + [Testing automatic failover](AutoFailover.md#auto-failover-test "AutoFailover.md#auto-failover-test")

## REL 5: Are your ElastiCache components designed to scale?

**Question-level introduction:** By understanding the
scaling capabilities and available deployment topologies, your ElastiCache
components can adjust over time to meet changing workload requirements. ElastiCache
offers 4-way scaling: in/out (horizontal) as well as up/down (vertical).

**Question-level benefit:** Following best practices
for ElastiCache deployments provides the greatest amount of scaling flexibility, as
well as meeting the Well Architected principle of scaling horizontally to minimize
the impact of failures.

- **[Required]** Understand the difference
  between Cluster-mode Enabled and Cluster-mode Disabled topologies. In almost
  all cases it is recommended to deploy with Cluster-mode enabled as it allow
  for greater scalability over time. Cluster-mode disabled components are
  limited in their ability to horizontally scale by adding read
  replicas.
- **[Required]** Understand when and how to
  scale.
  - For more READIOPS: add replicas
  - For more WRITEOPS: add shards (scale out)
  - For more network IO – use network optimized instances, scale
    up

- **[Best]** Deploy your ElastiCache components
  with Cluster-mode enabled, with a bias toward more, smaller nodes rather
  than fewer, larger nodes. This effectively limits the blast radius of a node
  failure.
- **[Best]** Include replicas in your clusters
  for enhanced responsiveness during scaling events
- **[Good]** For cluster-mode disabled,
  leverage read replicas to increase overall read capacity. ElastiCache has
  support for up to 5 read replicas in cluster-mode disabled, as well as
  vertical scaling.
- **[Resources]:**
  - [Scaling
    ElastiCache clusters](Scaling.md "Scaling.md")
  - [Online scaling up](redis-cluster-vertical-scaling.md#redis-cluster-vertical-scaling-scaling-up "redis-cluster-vertical-scaling.md#redis-cluster-vertical-scaling-scaling-up")
