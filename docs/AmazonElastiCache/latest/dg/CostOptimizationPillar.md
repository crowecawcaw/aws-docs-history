# Amazon ElastiCache Well-Architected Lens Cost Optimization Pillar

The cost optimization pillar focuses on avoiding unnecessary costs. Key topics include
understanding and controlling where money is being spent, selecting the most appropriate
node type (use instances that support data tiering based on workload needs), the right
number of resource types (how many read replicas) , analyzing spend over time, and
scaling to meet business needs without overspending.

###### Topics

- [COST 1: How do you identify and track costs associated with your ElastiCache resources? How do you develop mechanisms to enable users to create, manage, and dispose of created resources?](#CostOptimizationPillarCOST1 "#CostOptimizationPillarCOST1")
- [COST 2: How do you use continuous monitoring tools to help you optimize the costs associated with your ElastiCache resources?](#CostOptimizationPillarCOST2 "#CostOptimizationPillarCOST2")
- [COST 3: Should you use an instance type that support data tiering? What are the advantages of a data tiering? When not to use data tiering instances?](#CostOptimizationPillarCOST3 "#CostOptimizationPillarCOST3")

## COST 1: How do you identify and track costs associated with your ElastiCache resources? How do you develop mechanisms to enable users to create, manage, and dispose of created resources?

**Question-level introduction:** Understanding cost
metrics requires the participation of and collaboration across multiple teams:
software engineering, data management, product owners, finance, and leadership.
Identifying key cost drivers requires all involved parties understand service usage
control levers and cost management trade-offs and it is frequently the key
difference between successful and less successful cost optimization efforts.
Ensuring you have processes and tools in place to track resources created from
development to production and retirement helps you manage the costs associated with
ElastiCache.

**Question-level benefit:** Continuous tracking of
all costs associated with your workload requires a deep understanding of the
architecture that includes ElastiCache as one of its components. Additionally, you
should have a cost management plan in place to collect and compare usage against
your budget.

- **[Required]** Institute a Cloud Center of
  Excellence (CCoE) with one of its founding charters to own defining,
  tracking, and taking action on metrics around your organizations’
  ElastiCache usage. If a CCoE exists and functions, ensure that it knows how
  to read and track costs associated with ElastiCache. When resources are
  created, use IAM roles and policies to validate that only specific teams and
  groups can instantiate resources. This ensures that costs are associated
  with business outcomes and a clear line of accountability is established,
  from a cost perspective.

      1. CCoE should identify, define, and publish cost metrics that are
       updated on a regular -monthly- basis around key ElastiCache usage
       across categorical data such as:




      	1. Types of nodes used and their attributes: standard vs.
      	 memory optimized, on-demand vs. reserved instances, regions
      	 and availability zones
      	2. Types of environments: free, dev, testing, and
      	 production
      	3. Backup storage and retention strategies
      	4. Data transfer within and across regions
      	5. Instances running on Amazon Outposts
      2. CCoE consists of a cross-functional team with non-exclusive
       representation from software engineering, data management, product
       team, finance, and leadership teams in your organization.

  **[Resources]:**

      + [Create a Cloud Center of Excellence](../../../whitepapers/latest/cost-optimization-laying-the-foundation/cloud-center-of-excellence.md "../../../whitepapers/latest/cost-optimization-laying-the-foundation/cloud-center-of-excellence.md")
      + [Amazon ElastiCache
       pricing](https://aws.amazon.com/elasticache/pricing/ "https://aws.amazon.com/elasticache/pricing/")

- **[Required]** Use cost allocation tags to
  track costs at a low level of granularity. Use AWS Cost Management to
  visualize, understand, and manage your AWS costs and usage over time.

      1. Use tags to organize your resources, and cost allocation tags to
       track your AWS costs on a detailed level. After you activate cost
       allocation tags, AWS uses the cost allocation tags to organize
       your resource costs on your cost allocation report, to make it
       easier for you to categorize and track your AWS costs. AWS
       provides two types of cost allocation tags, an AWS generated tags
       and user-defined tags. AWS defines, creates, and applies the AWS
       generated tags for you, and you define, create, and apply
       user-defined tags. You must activate both types of tags separately
       before they can appear in Cost Management or on a cost allocation
       report.
      2. Use cost allocation tags to organize your AWS bill to reflect
       your own cost structure. When you add cost allocation tags to your
       resources in Amazon ElastiCache, you will be able to track costs by grouping
       expenses on your invoices by resource tag values. You should
       consider combining tags to track costs at a greater level of
       detail.

  **[Resources]:**

      + [Using AWS cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md")
      + [Monitoring
       costs with cost allocation tags](Tagging.md "Tagging.md")
      + [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/ "https://aws.amazon.com/aws-cost-management/aws-cost-explorer/")

- **[Best]** Connect ElastiCache cost to metrics that
  reach across the organization.

      1. Consider business metrics as well as operational metrics like
       latency - what concepts in your business model are understandable
       across roles? The metrics need to be understandable by as many roles
       as possible in the organization.
      2. Examples - simultaneous served users, max and average latency per
       operation and user, user engagement scores, user return rates/week,
       session length/user, abandonment rate, cache hit rate, and keys
       tracked

  **[Resources]:**

      + [Monitoring use with CloudWatch Metrics](CacheMetrics.md "CacheMetrics.md")

- **[Good]** Maintain up-to-date architectural
  and operational visibility on metrics and costs across the entire workload
  that uses ElastiCache.
  1.  Understand your entire solution ecosystem, ElastiCache tends to be part
      of a full ecosystem of AWS services in their technology set, from
      clients to API Gateway, Redshift, and QuickSight for reporting tools
      (for example).
  2.  Map components of your solution from clients, connections,
      security, in-memory operations, storage, resource automation, data
      access and management, on your architecture diagram. Each layer
      connects to the entire solution and has its own needs and
      capabilities that add to and/or help you manage the overall
      cost.
  3.  Your diagram should include the use of compute, networking,
      storage, lifecycle policies, metrics gathering as well as the
      operational and functional ElastiCache elements of your application
  4.  The requirements of your workload are likely to evolve over time
      and it is essential that you continue to maintain and document your
      understanding of the underlying components as well as your primary
      functional objectives in order to remain proactive in your workload
      cost management.
  5.  Executive support for visibility, accountability, prioritization,
      and resources is crucial to you having an effective cost management
      strategy for your ElastiCache.

## COST 2: How do you use continuous monitoring tools to help you optimize the costs associated with your ElastiCache resources?

**Question-level introduction:** You need to aim for
a proper balance between your ElastiCache cost and application performance metrics. Amazon
CloudWatch provides visibility into key operational metrics that can help you assess
whether your ElastiCache resources are over or under utilized, relative to your needs.
From a cost optimization perspective, you need to understand when you are
overprovisioned and be able to develop appropriate mechanisms to resize your ElastiCache
resources while maintaining your operational, availability, resilience, and
performance needs.

**Question-level benefit:** In an ideal state, you
will have provisioned sufficient resources to meet your workload operational needs
and not have under-utilized resources that can lead to a sub-optimal cost state. You
need to be able to both identify and avoid operating oversized ElastiCache resources for
long periods of time.

- **[Required]** Use CloudWatch to monitor your
  ElastiCache clusters and analyze how these metrics relate to your AWS Cost
  Explorer dashboards.

      1. ElastiCache provides both host-level metrics (for example, CPU usage)
       and metrics that are specific to the cache engine software (for
       example, cache gets and cache misses). These metrics are measured
       and published for each cache node in 60-second intervals.
      2. ElastiCache performance metrics (CPUUtilization, EngineUtilization,
       SwapUsage, CurrConnections, and Evictions) may indicate that you
       need to scale up/down (use larger/smaller cache node types) or
       in/out (add more/less shards). Understand the cost implications of
       scaling decisions by creating a playbook matrix that estimates the
       additional cost and the min and max lengths of time required to meet
       your application performance thresholds.

  **[Resources]:**

      + [Monitoring use with CloudWatch Metrics](CacheMetrics.md "CacheMetrics.md")
      + [Which Metrics Should I Monitor?](CacheMetrics.md "CacheMetrics.md")
      + [Amazon ElastiCache
       pricing](https://aws.amazon.com/elasticache/pricing/ "https://aws.amazon.com/elasticache/pricing/")

- **[Required]** Understand and document your
  backup strategy and cost implications.

      1. With ElastiCache, the backups are stored in Amazon S3, which provides
       durable storage. You need to understand the cost implications in
       relation to your ability to recover from failures.
      2. Enable automatic backups that will delete backup files that are
       past the retention limit.

  **[Resources]:**

      + [Scheduling automatic backups](backups-automatic.md "backups-automatic.md")
      + [Amazon Simple Storage Service
       pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/")

- **[Best]** Use Reserved Nodes for your
  instances as a deliberate strategy to manage costs for workloads that are
  well understood and documented. Reserved nodes are charged an up front fee
  that depends upon the node type and the length of reservation—one or three
  years. This charge is much less than the hourly usage charge that you incur
  with On-Demand nodes.
  1.  You may need to operate your ElastiCache clusters using on-demand nodes
      until you have gathered sufficient data to estimate the reserved
      instance requirements. Plan and document the resources needed to
      meet your needs and compare expected costs across instance types
      (on-demand vs. reserved)
  2.  Regularly evaluate new cache node types available and assess
      whether it makes sense, from a cost and operational metrics
      perspective, to migrate your instance fleet to new cache node
      types

## COST 3: Should you use an instance type that support data tiering? What are the advantages of a data tiering? When not to use data tiering instances?

**Question-level introduction:** Selecting the
appropriate instance type can not only have performance and service level impact but
also financial impact. Instance types have different cost associated with them.
Selecting one or a few large instance types that can accommodate all storage needs
in memory might be a natural decision. However, this could have significant cost
impact as the project matures. Ensuring that the correct instance type is selected
requires periodic examination of ElastiCache object idle time.

**Question-level benefit:** You should have a clear
understanding of how various instance types impact your cost at the present and in
the future. Marginal or periodic workload changes should not cause disproportionate
costs changes. If the workload permits it, instance types that support data tiering
offer a better price per storage available storage. Because of the per instance
available SSD storage data tiering instances support a much higher total data per
instance capability.

- **[Required]** Understand limitations of data
  tiering instances

      1. Only available for ElastiCache for Valkey or Redis OSS clusters.
      2. Only limited instance types support data tiering.
      3. Only ElastiCache version 6.2 for Redis OSS and above is supported
      4. Large items are not swapped out to SSD. Objects over 128 MiB are
       kept in memory.

  **[Resources]:**

      + [Data
       tiering](data-tiering.md "data-tiering.md")
      + [Amazon ElastiCache
       pricing](https://aws.amazon.com/elasticache/pricing/ "https://aws.amazon.com/elasticache/pricing/")

- **[Required]** Understand what percentage of
  your database is regularly accessed by your workload.
  1.  Data tiering instances are ideal for workloads that often access a
      small portion of your overall dataset but still requires fast access
      to the remaining data. In other words, the ratio of hot to warm
      data is about 20:80.
  2.  Develop cluster level tacking of object idle time.
  3.  Large implementations of over 500 Gb of data are good
      candidates

- **[Required]** Understand that data tiering
  instances are not optional for certain workloads.

      1. There is a small performance cost for accessing less frequently
       used objects as those are swapped out to local SSD. If your
       application is response time sensitive test the impact on your
       workload.
      2. Not suitable for caches that store mostly large objects over 128
       MiB in size.

  **[Resources]:**

      + [Limitations](data-tiering.md#data-tiering-prerequisites "data-tiering.md#data-tiering-prerequisites")

- **[Best]** Reserved instance types support
  data tiering. This assures the lowest cost in terms of amount of data
  storage per instance.

      1. You may need to operate your ElastiCache clusters using non-data tiering
       instances until you have a better understanding of your
       requirements.
      2. Analyze your ElastiCache clusters data usage pattern.
      3. Create an automated job that periodically collects object idle
       time.
      4. If you notice that a large percentage (about 80%) of objects are
       idle for a period of time deemed appropriate for your workload
       document the findings and suggest migrating the cluster to instances
       that support data tiering.
      5. Regularly evaluate new cache node types available and assess
       whether it makes sense, from a cost and operational metrics
       perspective, to migrate your instance fleet to new cache node
       types.

  **[Resources]:**

      + [OBJECT
       IDLETIME](https://valkey.io/commands/object-idletime/ "https://valkey.io/commands/object-idletime/")
      + [Amazon ElastiCache
       pricing](https://aws.amazon.com/elasticache/pricing/ "https://aws.amazon.com/elasticache/pricing/")
