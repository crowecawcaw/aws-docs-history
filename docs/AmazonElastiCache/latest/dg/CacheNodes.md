# Supported node types

ElastiCache supports the following node types.
Generally speaking, the current generation types provide more memory and computational power
at lower cost when compared to their equivalent previous generation counterparts.

For more information on performance details for each node type, see [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").

###### Note

Amazon ElastiCache is transitioning T2 instances to previous generation status.
You will no longer be able to create new ElastiCache clusters using T2 instances or purchase new T2 reserved nodes.
There is no impact to existing T2 clusters or reservations. We recommend upgrading to newer instance types such as T3 or T4g instances for better performance and cost efficiency.

###### Note

The following instance types are supported in the AWS Asia Pacific (Thailand) and Mexico (Central) Regions:

- **m7g/r7g:** large, xl, 2xl, 4xl, 8xl, 12xl, and 16xl.
- **t3/t4g:** micro, small, and medium.
  For information on which node size to use, see [Choosing your node size](CacheNodes.md "CacheNodes.md").

###### Topics

- [Current Generation (Memcached)](#CacheNodes.CurrentGen-Memcached "#CacheNodes.CurrentGen-Memcached")
- [Current Generation (Valkey or Redis OSS)](#CacheNodes.CurrentGen "#CacheNodes.CurrentGen")
- [Supported node types by AWS
  Region](#CacheNodes.SupportedTypesByRegion "#CacheNodes.SupportedTypesByRegion")
- [Burstable Performance Instances](#CacheNodes.Burstable "#CacheNodes.Burstable")
- [Related Information](#CacheNodes.RelatedInfo "#CacheNodes.RelatedInfo")

## Current Generation (Memcached)

The following tables show the baseline and burst bandwidth for instance types that
use the network I/O credit mechanism to burst beyond their baseline
bandwidth.

###### Note

Instance types with burstable network performance use a network I/O credit
mechanism to burst beyond their baseline bandwidth on a best-effort
basis.

**General**

| Instance type      | Minimum supported Memcached version | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) |
| ------------------ | ----------------------------------- | ------------------------- | ---------------------- |
| cache.m7g.large    |                                     | 0.937                     | 12.5                   |
| cache.m7g.xlarge   |                                     | 1.876                     | 12.5                   |
| cache.m7g.2xlarge  |                                     | 3.75                      | 15                     |
| cache.m7g.4xlarge  |                                     | 7.5                       | 15                     |
| cache.m7g.8xlarge  |                                     | 15                        | N/A                    |
| cache.m7g.12xlarge |                                     | 22.5                      | N/A                    |
| cache.m7g.16xlarge |                                     | 30                        | N/A                    |
| cache.m6g.large    | 1.5.16                              | 0.75                      | 10.0                   |
| cache.m6g.xlarge   | 1.5.16                              | 1.25                      | 10.0                   |
| cache.m6g.2xlarge  | 1.5.16                              | 2.5                       | 10.0                   |
| cache.m6g.4xlarge  | 1.5.16                              | 5.0                       | 10.0                   |
| cache.m6g.8xlarge  | 1.5.16                              | 12                        | N/A                    |
| cache.m6g.12xlarge | 1.5.16                              | 20                        | N/A                    |
| cache.m6g.16xlarge | 1.5.16                              | 25                        | N/A                    |
| cache.m5.large     | 1.5.16                              | 0.75                      | 10.0                   |
| cache.m5.xlarge    | 1.5.16                              | 1.25                      | 10.0                   |
| cache.m5.2xlarge   | 1.5.16                              | 2.5                       | 10.0                   |
| cache.m5.4xlarge   | 1.5.16                              | 5.0                       | 10.0                   |
| cache.m5.12xlarge  | 1.5.16                              | N/A                       | N/A                    |
| cache.m5.24xlarge  | 1.5.16                              | N/A                       | N/A                    |
| cache.m4.large     | 1.5.16                              | 0.45                      | 1.2                    |
| cache.m4.xlarge    | 1.5.16                              | 0.75                      | 2.8                    |
| cache.m4.2xlarge   | 1.5.16                              | 1.0                       | 10.0                   |
| cache.m4.4xlarge   | 1.5.16                              | 2.0                       | 10.0                   |
| cache.m4.10xlarge  | 1.5.16                              | 5.0                       | 10.0                   |
| cache.t4g.micro    | 1.5.16                              | 0.064                     | 5.0                    |
| cache.t4g.small    | 1.5.16                              | 0.128                     | 5.0                    |
| cache.t4g.medium   | 1.5.16                              | 0.256                     | 5.0                    |
| cache.t3.micro     | 1.5.16                              | 0.064                     | 5.0                    |
| cache.t3.small     | 1.5.16                              | 0.128                     | 5.0                    |
| cache.t3.medium    | 1.5.16                              | 0.256                     | 5.0                    |
| cache.t2.micro     | 1.5.16                              | 0.064                     | 1.024                  |
| cache.t2.small     | 1.5.16                              | 0.128                     | 1.024                  |
| cache.t2.medium    | 1.5.16                              | 0.256                     | 1.024                  |

**Memory optimized for Memcached**

| Instance type      | Minimum supported version | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) |
| ------------------ | ------------------------- | ------------------------- | ---------------------- |
| cache.r7g.large    |                           | 0.937                     | 12.5                   |
| cache.r7g.xlarge   |                           | 1.876                     | 12.5                   |
| cache.r7g.2xlarge  |                           | 3.75                      | 15                     |
| cache.r7g.4xlarge  |                           | 7.5                       | 15                     |
| cache.r7g.8xlarge  |                           | 15                        | N/A                    |
| cache.r7g.12xlarge |                           | 22.5                      | N/A                    |
| cache.r7g.16xlarge |                           | 30                        | N/A                    |
| cache.r6g.large    | 1.5.16                    | 0.75                      | 10.0                   |
| cache.r6g.xlarge   | 1.5.16                    | 1.25                      | 10.0                   |
| cache.r6g.2xlarge  | 1.5.16                    | 2.5                       | 10.0                   |
| cache.r6g.4xlarge  | 1.5.16                    | 5.0                       | 10.0                   |
| cache.r6g.8xlarge  | 1.5.16                    | 12                        | N/A                    |
| cache.r6g.12xlarge | 1.5.16                    | 20                        | N/A                    |
| cache.r6g.16xlarge | 1.5.16                    | 25                        | N/A                    |
| cache.r5.large     | 1.5.16                    | 0.75                      | 10.0                   |
| cache.r5.xlarge    | 1.5.16                    | 1.25                      | 10.0                   |
| cache.r5.2xlarge   | 1.5.16                    | 2.5                       | 10.0                   |
| cache.r5.4xlarge   | 1.5.16                    | 5.0                       | 10.0                   |
| cache.r5.12xlarge  | 1.5.16                    | 20                        | N/A                    |
| cache.r5.24xlarge  | 1.5.16                    | 25                        | N/A                    |
| cache.r4.large     | 1.5.16                    | 0.75                      | 10.0                   |
| cache.r4.xlarge    | 1.5.16                    | 1.25                      | 10.0                   |
| cache.r4.2xlarge   | 1.5.16                    | 2.5                       | 10.0                   |
| cache.r4.4xlarge   | 1.5.16                    | 5.0                       | 10.0                   |
| cache.r4.8xlarge   | 1.5.16                    | 12                        | N/A                    |
| cache.r4.16xlarge  | 1.5.16                    | 25                        | N/A                    |

**Network optimized for Memcached**

| Instance type       | Minimum supported version | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) |
| ------------------- | ------------------------- | ------------------------- | ---------------------- |
| cache.c7gn.large    | 1.6.6                     | 6.25                      | 30                     |
| cache.c7gn.xlarge   | 1.6.6                     | 12.5                      | 40                     |
| cache.c7gn.2xlarge  | 1.6.6                     | 25                        | 50                     |
| cache.c7gn.4xlarge  | 1.6.6                     | 50                        | N/A                    |
| cache.c7gn.8xlarge  | 1.6.6                     | 100                       | N/A                    |
| cache.c7gn.12xlarge | 1.6.6                     | 150                       | N/A                    |
| cache.c7gn.16xlarge | 1.6.6                     | 200                       | N/A                    |

## Current Generation (Valkey or Redis OSS)

For more information on Previous Generation, please refer to [Previous
Generation Nodes](https://aws.amazon.com/elasticache/previous-generation/ "https://aws.amazon.com/elasticache/previous-generation/").

###### Note

Instance types with burstable network performance use a network I/O credit
mechanism to burst beyond their baseline bandwidth on a best-effort
basis.

**General**

| Instance type      | Minimum supported Redis OSS version | Enhanced I/O with Redis OSS 5.0.6+ | TLS Offloading with Redis OSS 6.2.5+ | Enhanced I/O Multiplexing with Redis OSS 7.0.4+ | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) |
| ------------------ | ----------------------------------- | ---------------------------------- | ------------------------------------ | ----------------------------------------------- | ------------------------- | ---------------------- |
| cache.m7g.large    | 6.2                                 | N                                  | N                                    | N                                               | 0.937                     | 12.5                   |
| cache.m7g.xlarge   | 6.2                                 | Y                                  | Y                                    | Y                                               | 1.876                     | 12.5                   |
| cache.m7g.2xlarge  | 6.2                                 | Y                                  | Y                                    | Y                                               | 3.75                      | 15                     |
| cache.m7g.4xlarge  | 6.2                                 | Y                                  | Y                                    | Y                                               | 7.5                       | 15                     |
| cache.m7g.8xlarge  | 6.2                                 | Y                                  | Y                                    | Y                                               | 15                        | N/A                    |
| cache.m7g.12xlarge | 6.2                                 | Y                                  | Y                                    | Y                                               | 22.5                      | N/A                    |
| cache.m7g.16xlarge | 6.2                                 | Y                                  | Y                                    | Y                                               | 30                        | N/A                    |
| cache.m6g.large    | 5.0.6                               | N                                  | N                                    | N                                               | 0.75                      | 10.0                   |
| cache.m6g.xlarge   | 5.0.6                               | Y                                  | Y                                    | Y                                               | 1.25                      | 10.0                   |
| cache.m6g.2xlarge  | 5.0.6                               | Y                                  | Y                                    | Y                                               | 2.5                       | 10.0                   |
| cache.m6g.4xlarge  | 5.0.6                               | Y                                  | Y                                    | Y                                               | 5.0                       | 10.0                   |
| cache.m6g.8xlarge  | 5.0.6                               | Y                                  | Y                                    | Y                                               | 12                        | N/A                    |
| cache.m6g.12xlarge | 5.0.6                               | Y                                  | Y                                    | Y                                               | 20                        | N/A                    |
| cache.m6g.16xlarge | 5.0.6                               | Y                                  | Y                                    | Y                                               | 25                        | N/A                    |
| cache.m5.large     | 3.2.4                               | N                                  | N                                    | N                                               | 0.75                      | 10.0                   |
| cache.m5.xlarge    | 3.2.4                               | Y                                  | N                                    | N                                               | 1.25                      | 10.0                   |
| cache.m5.2xlarge   | 3.2.4                               | Y                                  | Y                                    | Y                                               | 2.5                       | 10.0                   |
| cache.m5.4xlarge   | 3.2.4                               | Y                                  | Y                                    | Y                                               | 5.0                       | 10.0                   |
| cache.m5.12xlarge  | 3.2.4                               | Y                                  | Y                                    | Y                                               | 12                        | N/A                    |
| cache.m5.24xlarge  | 3.2.4                               | Y                                  | Y                                    | Y                                               | 25                        | N/A                    |
| cache.m4.large     | 3.2.4                               | N                                  | N                                    | N                                               | 0.45                      | 1.2                    |
| cache.m4.xlarge    | 3.2.4                               | Y                                  | N                                    | N                                               | 0.75                      | 2.8                    |
| cache.m4.2xlarge   | 3.2.4                               | Y                                  | Y                                    | Y                                               | 1.0                       | 10.0                   |
| cache.m4.4xlarge   | 3.2.4                               | Y                                  | Y                                    | Y                                               | 2.0                       | 10.0                   |
| cache.m4.10xlarge  | 3.2.4                               | Y                                  | Y                                    | Y                                               | 5.0                       | 10.0                   |
| cache.t4g.micro    | 3.2.4                               | N                                  | N                                    | N                                               | 0.064                     | 5.0                    |
| cache.t4g.small    | 5.0.6                               | N                                  | N                                    | N                                               | 0.128                     | 5.0                    |
| cache.t4g.medium   | 5.0.6                               | N                                  | N                                    | N                                               | 0.256                     | 5.0                    |
| cache.t3.micro     | 3.2.4                               | N                                  | N                                    | N                                               | 0.064                     | 5.0                    |
| cache.t3.small     | 3.2.4                               | N                                  | N                                    | N                                               | 0.128                     | 5.0                    |
| cache.t3.medium    | 3.2.4                               | N                                  | N                                    | N                                               | 0.256                     | 5.0                    |
| cache.t2.micro     | 3.2.4                               | N                                  | N                                    | N                                               | 0.064                     | 1.024                  |
| cache.t2.small     | 3.2.4                               | N                                  | N                                    | N                                               | 0.128                     | 1.024                  |
| cache.t2.medium    | 3.2.4                               | N                                  | N                                    | N                                               | 0.256                     | 1.024                  |

**Memory optimized**

| Instance type      | Minimum supported Redis OSS version | Enhanced I/O with Redis OSS 5.0.6+ | TLS Offloading with Redis OSS 6.2.5+ | Enhanced I/O Multiplexing with Redis OSS 7.0.4+ | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) |
| ------------------ | ----------------------------------- | ---------------------------------- | ------------------------------------ | ----------------------------------------------- | ------------------------- | ---------------------- |
| cache.r7g.large    | 6.2                                 | N                                  | N                                    | N                                               | 0.937                     | 12.5                   |
| cache.r7g.xlarge   | 6.2                                 | Y                                  | Y                                    | Y                                               | 1.876                     | 12.5                   |
| cache.r7g.2xlarge  | 6.2                                 | Y                                  | Y                                    | Y                                               | 3.75                      | 15                     |
| cache.r7g.4xlarge  | 6.2                                 | Y                                  | Y                                    | Y                                               | 7.5                       | 15                     |
| cache.r7g.8xlarge  | 6.2                                 | Y                                  | Y                                    | Y                                               | 15                        | N/A                    |
| cache.r7g.12xlarge | 6.2                                 | Y                                  | Y                                    | Y                                               | 22.5                      | N/A                    |
| cache.r7g.16xlarge | 6.2                                 | Y                                  | Y                                    | Y                                               | 30                        | N/A                    |
| cache.r6g.large    | 5.0.6                               | N                                  | N                                    | N                                               | 0.75                      | 10.0                   |
| cache.r6g.xlarge   | 5.0.6                               | Y                                  | Y                                    | Y                                               | 1.25                      | 10.0                   |
| cache.r6g.2xlarge  | 5.0.6                               | Y                                  | Y                                    | Y                                               | 2.5                       | 10.0                   |
| cache.r6g.4xlarge  | 5.0.6                               | Y                                  | Y                                    | Y                                               | 5.0                       | 10.0                   |
| cache.r6g.8xlarge  | 5.0.6                               | Y                                  | Y                                    | Y                                               | 12                        | N/A                    |
| cache.r6g.12xlarge | 5.0.6                               | Y                                  | Y                                    | Y                                               | 20                        | N/A                    |
| cache.r6g.16xlarge | 5.0.6                               | Y                                  | Y                                    | Y                                               | 25                        | N/A                    |
| cache.r5.large     | 3.2.4                               | N                                  | N                                    | N                                               | 0.75                      | 10.0                   |
| cache.r5.xlarge    | 3.2.4                               | Y                                  | N                                    | N                                               | 1.25                      | 10.0                   |
| cache.r5.2xlarge   | 3.2.4                               | Y                                  | Y                                    | Y                                               | 2.5                       | 10.0                   |
| cache.r5.4xlarge   | 3.2.4                               | Y                                  | Y                                    | Y                                               | 5.0                       | 10.0                   |
| cache.r5.12xlarge  | 3.2.4                               | Y                                  | Y                                    | Y                                               | 12                        | N/A                    |
| cache.r5.24xlarge  | 3.2.4                               | Y                                  | Y                                    | Y                                               | 25                        | N/A                    |
| cache.r4.large     | 3.2.4                               | N                                  | N                                    | N                                               | 0.75                      | 10.0                   |
| cache.r4.xlarge    | 3.2.4                               | Y                                  | N                                    | N                                               | 1.25                      | 10.0                   |
| cache.r4.2xlarge   | 3.2.4                               | Y                                  | Y                                    | Y                                               | 2.5                       | 10.0                   |
| cache.r4.4xlarge   | 3.2.4                               | Y                                  | Y                                    | Y                                               | 5.0                       | 10.0                   |
| cache.r4.8xlarge   | 3.2.4                               | Y                                  | Y                                    | Y                                               | 12                        | N/A                    |
| cache.r4.16xlarge  | 3.2.4                               | Y                                  | Y                                    | Y                                               | 25                        | N/A                    |

**Memory optimized with data tiering**

| Instance type       | Minimum supported Redis OSS version | Enhanced I/O with Redis OSS 5.0.6+ | TLS Offloading with Redis OSS 6.2.5+ | Enhanced I/O Multiplexing with Redis OSS 7.0.4+ | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) |
| ------------------- | ----------------------------------- | ---------------------------------- | ------------------------------------ | ----------------------------------------------- | ------------------------- | ---------------------- |
| cache.r6gd.xlarge   | 6.2.0                               | Y                                  | N                                    | N                                               | 1.25                      | 10                     |
| cache.r6gd.2xlarge  | 6.2.0                               | Y                                  | Y                                    | Y                                               | 2.5                       | 10                     |
| cache.r6gd.4xlarge  | 6.2.0                               | Y                                  | Y                                    | Y                                               | 5.0                       | 10                     |
| cache.r6gd.8xlarge  | 6.2.0                               | Y                                  | Y                                    | Y                                               | 12                        | N/A                    |
| cache.r6gd.12xlarge | 6.2.0                               | Y                                  | Y                                    | Y                                               | 20                        | N/A                    |
| cache.r6gd.16xlarge | 6.2.0                               | Y                                  | Y                                    | Y                                               | 25                        | N/A                    |

**Network optimized**

| Instance type       | Minimum supported Redis OSS version | Enhanced I/O with Redis OSS 5.0.6+ | TLS Offloading with Redis OSS 6.2.5+ | Enhanced I/O Multiplexing with Redis OSS 7.0.4+ | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) |
| ------------------- | ----------------------------------- | ---------------------------------- | ------------------------------------ | ----------------------------------------------- | ------------------------- | ---------------------- |
| cache.c7gn.large    | 6.2                                 | N                                  | N                                    | N                                               | 6.25                      | 30                     |
| cache.c7gn.xlarge   | 6.2                                 | Y                                  | Y                                    | Y                                               | 12.5                      | 40                     |
| cache.c7gn.2xlarge  | 6.2                                 | Y                                  | Y                                    | Y                                               | 25                        | 50                     |
| cache.c7gn.4xlarge  | 6.2                                 | Y                                  | Y                                    | Y                                               | 50                        | N/A                    |
| cache.c7gn.8xlarge  | 6.2                                 | Y                                  | Y                                    | Y                                               | 100                       | N/A                    |
| cache.c7gn.12xlarge | 6.2                                 | Y                                  | Y                                    | Y                                               | 150                       | N/A                    |
| cache.c7gn.16xlarge | 6.2                                 | Y                                  | Y                                    | Y                                               | 200                       | N/A                    |

## Supported node types by AWS

Region

Supported node types may vary between AWS Regions. For more details, see [Amazon ElastiCache
pricing](https://aws.amazon.com/elasticache/pricing/ "https://aws.amazon.com/elasticache/pricing/").

## Burstable Performance Instances

You can launch general-purpose burstable T4g, T3-Standard and T2-Standard cache
nodes in Amazon ElastiCache. These nodes provide a baseline level of CPU performance with the
ability to burst CPU usage at any time until the accrued credits are exhausted. A
_CPU credit_ provides the performance of a full
CPU core for one minute.

Amazon ElastiCache's T4g, T3 and T2 nodes are configured as standard and suited for
workloads with an average CPU utilization that is consistently below the baseline
performance of the instance. To burst above the baseline, the node spends credits
that it has accrued in its CPU credit balance. If the node is running low on accrued
credits, performance is gradually lowered to the baseline performance level. This
gradual lowering ensures the node doesn't experience a sharp performance drop-off
when its accrued CPU credit balance is depleted. For more information, see [CPU Credits and Baseline Performance for Burstable Performance
Instances](../../../AWSEC2/latest/UserGuide/burstable-credits-baseline-concepts.md "../../../AWSEC2/latest/UserGuide/burstable-credits-baseline-concepts.md") in the _Amazon EC2 User
Guide_.\*\*

The following table lists the burstable performance node types, the rate at which
CPU credits are earned per hour. It also shows the maximum number of earned CPU
credits that a node can accrue and the number of vCPUs per node. In addition, it
gives the baseline performance level as a percentage of a full core performance
(using a single vCPU).

| Node type  | CPU credits earned per hour | Maximum earned credits that can be<br>accrued\* | vCPUs | Baseline performance per vCPU | Memory (GiB) | Network performance |
| ---------- | --------------------------- | ----------------------------------------------- | ----- | ----------------------------- | ------------ | ------------------- |
| t4g.micro  | `12`                        | 288                                             | 2     | 10%                           | 0.5          | Up to 5 Gigabit     |
| t4g.small  | `24`                        | 576                                             | 2     | 20%                           | 1.37         | Up to 5 Gigabit     |
| t4g.medium | `24`                        | 576                                             | 2     | 20%                           | 3.09         | Up to 5 Gigabit     |
| t3.micro   | `12`                        | 288                                             | 2     | 10%                           | 0.5          | Up to 5 Gigabit     |
| t3.small   | `24`                        | 576                                             | 2     | 20%                           | 1.37         | Up to 5 Gigabit     |
| t3.medium  | `24`                        | 576                                             | 2     | 20%                           | 3.09         | Up to 5 Gigabit     |
| t2.micro   | `6`                         | 144                                             | 1     | 10%                           | 0.5          | Low to moderate     |
| t2.small   | `12`                        | 288                                             | 1     | 20%                           | 1.55         | Low to moderate     |
| t2.medium  | `24`                        | 576                                             | 2     | 20%                           | 3.22         | Low to moderate     |

\* The number of credits that can be accrued is equivalent to the number of credits
that can be earned in a 24-hour period.

\*\* The baseline performance in the table is per vCPU. Some node sizes that have
more than one vCPU. For these, calculate the baseline CPU utilization for the node
by multiplying the vCPU percentage by the number of vCPUs.

The following CPU credit metrics are available for T3 and T4g burstable
performance instances:

###### Note

These metrics are not available for T2 burstable performance instances.

- `CPUCreditUsage`
- `CPUCreditBalance`

For more information on these metrics, see [CPU Credit Metrics](../../../AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.md#cpu-credit-metrics "../../../AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.md#cpu-credit-metrics").

In addition, be aware of these details:

- All current generation node types are created in a virtual private cloud
  (VPC) based on Amazon VPC by default.
- Redis OSS append-only files (AOF) aren't supported for T2 instances.
  Redis OSS configuration variables `appendonly` and
  `appendfsync` aren't supported on Redis OSS version 2.8.22 and
  later.

## Related Information

- [Amazon ElastiCache Product
  Features and Details](https://aws.amazon.com/elasticache/details "https://aws.amazon.com/elasticache/details")
- [Memcached Node-Type Specific Parameters for Memcached](ParameterGroups.md#ParameterGroups.Memcached "ParameterGroups.md#ParameterGroups.Memcached")
- [Valkey and Redis OSS parameters](ParameterGroups.md#ParameterGroups.Redis "ParameterGroups.md#ParameterGroups.Redis")
- [In
  Transit Encryption (TLS)](in-transit-encryption.md "in-transit-encryption.md")
