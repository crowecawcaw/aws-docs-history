

# Supported node types
<a name="CacheNodes.SupportedTypes"></a>

ElastiCache supports the following node types. Generally speaking, the latest generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

For performance details for each node type, see [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/).

For information on which node size to use, see [Choosing your node size](CacheNodes.SelectSize.md). 

**Note**  
We are transitioning T2 instances to previous generation status. You will no longer be able to create new ElastiCache clusters using T2 instances or purchase new T2 reserved nodes. There is no impact to your existing T2 clusters or reservations. We recommend upgrading to T4g instances for better performance and cost efficiency.   
Instance types with burstable network performance use a network I/O credit mechanism to burst beyond their baseline bandwidth on a best-effort basis.

**Topics**
+ [Current Generation (Memcached)](#CacheNodes.CurrentGen-Memcached)
+ [Current Generation (Valkey)](#CacheNodes.CurrentGen-Valkey)
+ [Current Generation (Redis OSS)](#CacheNodes.CurrentGen-Redis)
+ [Burstable Performance Instances](#CacheNodes.Burstable)
+ [Supported node types by AWS Region](#CacheNodes.SupportedTypesByRegion)
+ [Related Information](#CacheNodes.RelatedInfo)

## Current Generation (Memcached)
<a name="CacheNodes.CurrentGen-Memcached"></a>

**General**


| Instance type | Minimum supported Memcached version | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) | Memory (GiB) | 
| --- | --- | --- | --- | --- | 
| cache.m8g.large | 1.6.6 | 0.937 | 12.5 | 6.79 | 
| cache.m8g.xlarge | 1.6.6 | 1.875 | 12.5 | 14.18 | 
| cache.m8g.2xlarge | 1.6.6 | 3.75 | 15 | 29.68 | 
| cache.m8g.4xlarge | 1.6.6 | 7.5 | 15 | 61.33 | 
| cache.m8g.8xlarge | 1.6.6 | 15 | N/A | 124.65 | 
| cache.m8g.12xlarge | 1.6.6 | 22.5 | N/A | 187.96 | 
| cache.m8g.16xlarge | 1.6.6 | 30 | N/A | 251.27 | 
| cache.m7g.large | 1.5.16 | 0.937 | 12.5 | 6.38 | 
| cache.m7g.xlarge | 1.5.16 | 1.876 | 12.5 | 12.93 | 
| cache.m7g.2xlarge | 1.5.16 | 3.75 | 15 | 26.04 | 
| cache.m7g.4xlarge | 1.5.16 | 7.5 | 15 | 52.26 | 
| cache.m7g.8xlarge | 1.5.16 | 15 | N/A | 103.68 | 
| cache.m7g.12xlarge | 1.5.16 | 22.5 | N/A | 157.12 | 
| cache.m7g.16xlarge | 1.5.16 | 30 | N/A | 209.55 | 
| cache.m6g.large | 1.5.16 | 0.75 | 10.0 | 6.38 | 
| cache.m6g.xlarge | 1.5.16 | 1.25 | 10.0 | 12.93 | 
| cache.m6g.2xlarge | 1.5.16 | 2.5 | 10.0 | 26.04 | 
| cache.m6g.4xlarge | 1.5.16 | 5.0 | 10.0 | 52.26 | 
| cache.m6g.8xlarge | 1.5.16 | 12 | N/A | 103.68 | 
| cache.m6g.12xlarge | 1.5.16 | 20 | N/A | 157.12 | 
| cache.m6g.16xlarge | 1.5.16 | 25 | N/A | 209.55 | 
| cache.m5.large | 1.5.16 | 0.75 | 10.0 | 6.38 | 
| cache.m5.xlarge | 1.5.16 | 1.25 | 10.0 | 12.93 | 
| cache.m5.2xlarge | 1.5.16 | 2.5 | 10.0 | 26.04 | 
| cache.m5.4xlarge | 1.5.16 | 5.0 | 10.0 | 52.26 | 
| cache.m5.12xlarge | 1.5.16 | 12 | N/A | 157.12 | 
| cache.m5.24xlarge | 1.5.16 | 25 | N/A | 314.32 | 
| cache.m4.large | 1.5.16 | 0.45 | 1.2 | 6.42 | 
| cache.m4.xlarge | 1.5.16 | 0.75 | 2.8 | 14.28 | 
| cache.m4.2xlarge | 1.5.16 | 1.0 | 10.0 | 29.70 | 
| cache.m4.4xlarge | 1.5.16 | 2.0 | 10.0 | 60.78 | 
| cache.m4.10xlarge | 1.5.16 | 5.0 | 10.0 | 154.64 | 
| cache.t4g.micro | 1.5.16 | 0.064 | 5.0 | 0.50 | 
| cache.t4g.small | 1.5.16 | 0.128 | 5.0 | 1.37 | 
| cache.t4g.medium | 1.5.16 | 0.256 | 5.0 | 3.09 | 
| cache.t3.micro | 1.5.16 | 0.064 | 5.0 | 0.50 | 
| cache.t3.small | 1.5.16 | 0.128 | 5.0 | 1.37 | 
| cache.t3.medium | 1.5.16 | 0.256 | 5.0 | 3.09 | 
| cache.t2.micro | 1.5.16 | 0.064 | 1.024 | 0.555 | 
| cache.t2.small | 1.5.16 | 0.128 | 1.024 | 1.55 | 
| cache.t2.medium | 1.5.16 | 0.256 | 1.024 | 3.22 | 

**Memory optimized**


| Instance type | Minimum supported Memcached version | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) | Memory (GiB) | 
| --- | --- | --- | --- | --- | 
| cache.r8g.large | 1.6.6 | 0.937 | 12.5 | 14.18 | 
| cache.r8g.xlarge | 1.6.6 | 1.875 | 12.5 | 29.68 | 
| cache.r8g.2xlarge | 1.6.6 | 3.75 | 15 | 61.33 | 
| cache.r8g.4xlarge | 1.6.6 | 7.5 | 15 | 124.65 | 
| cache.r8g.8xlarge | 1.6.6 | 15 | N/A | 251.27 | 
| cache.r8g.12xlarge | 1.6.6 | 22.5 | N/A | 377.9 | 
| cache.r8g.16xlarge | 1.6.6 | 30 | N/A | 504.52 | 
| cache.r7g.large | 1.5.16 | 0.937 | 12.5 | 13.07 | 
| cache.r7g.xlarge | 1.5.16 | 1.876 | 12.5 | 26.32 | 
| cache.r7g.2xlarge | 1.5.16 | 3.75 | 15 | 52.82 | 
| cache.r7g.4xlarge | 1.5.16 | 7.5 | 15 | 105.81 | 
| cache.r7g.8xlarge | 1.5.16 | 15 | N/A | 209.55 | 
| cache.r7g.12xlarge | 1.5.16 | 22.5 | N/A | 317.77 | 
| cache.r7g.16xlarge | 1.5.16 | 30 | N/A | 419.09 | 
| cache.r6g.large | 1.5.16 | 0.75 | 10.0 | 13.07 | 
| cache.r6g.xlarge | 1.5.16 | 1.25 | 10.0 | 26.32 | 
| cache.r6g.2xlarge | 1.5.16 | 2.5 | 10.0 | 52.82 | 
| cache.r6g.4xlarge | 1.5.16 | 5.0 | 10.0 | 105.81 | 
| cache.r6g.8xlarge | 1.5.16 | 12 | N/A | 209.55 | 
| cache.r6g.12xlarge | 1.5.16 | 20 | N/A | 317.77 | 
| cache.r6g.16xlarge | 1.5.16 | 25 | N/A | 419.09 | 
| cache.r5.large | 1.5.16 | 0.75 | 10.0 | 13.07 | 
| cache.r5.xlarge | 1.5.16 | 1.25 | 10.0 | 26.32 | 
| cache.r5.2xlarge | 1.5.16 | 2.5 | 10.0 | 52.82 | 
| cache.r5.4xlarge | 1.5.16 | 5.0 | 10.0 | 105.81 | 
| cache.r5.12xlarge | 1.5.16 | 20 | N/A | 317.77 | 
| cache.r5.24xlarge | 1.5.16 | 25 | N/A | 635.61 | 
| cache.r4.large | 1.5.16 | 0.75 | 10.0 | 12.30 | 
| cache.r4.xlarge | 1.5.16 | 1.25 | 10.0 | 25.05 | 
| cache.r4.2xlarge | 1.5.16 | 2.5 | 10.0 | 50.47 | 
| cache.r4.4xlarge | 1.5.16 | 5.0 | 10.0 | 101.38 | 
| cache.r4.8xlarge | 1.5.16 | 12 | N/A | 203.26 | 
| cache.r4.16xlarge | 1.5.16 | 25 | N/A | 407.00 | 

**Network optimized**


| Instance type | Minimum supported Memcached version | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) | Memory (GiB) | 
| --- | --- | --- | --- | --- | 
| cache.c8gn.large | 1.6.6 | 6.25 | 30 | 3.1 | 
| cache.c8gn.xlarge | 1.6.6 | 12.5 | 40 | 6.79 | 
| cache.c8gn.2xlarge | 1.6.6 | 25 | 50 | 14.18 | 
| cache.c8gn.4xlarge | 1.6.6 | 50 | N/A | 29.68 | 
| cache.c8gn.8xlarge | 1.6.6 | 100 | N/A | 61.33 | 
| cache.c8gn.12xlarge | 1.6.6 | 150 | N/A | 92.99 | 
| cache.c8gn.16xlarge | 1.6.6 | 200 | N/A | 124.65 | 
| cache.c7gn.large | 1.6.6 | 6.25 | 30 | 3.09 | 
| cache.c7gn.xlarge | 1.6.6 | 12.5 | 40 | 6.38 | 
| cache.c7gn.2xlarge | 1.6.6 | 25 | 50 | 12.94 | 
| cache.c7gn.4xlarge | 1.6.6 | 50 | N/A | 26.05 | 
| cache.c7gn.8xlarge | 1.6.6 | 100 | N/A | 52.26 | 
| cache.c7gn.12xlarge | 1.6.6 | 150 | N/A | 78.56 | 
| cache.c7gn.16xlarge | 1.6.6 | 200 | N/A | 105.81 | 

## Current Generation (Valkey)
<a name="CacheNodes.CurrentGen-Valkey"></a>

**General**


| Instance type | Minimum supported Valkey version | Enhanced I/O | TLS Offloading | Enhanced I/O Multiplexing | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) | Memory (GiB) | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| cache.m8g.large | 7.2 | Yes | No | Yes | 0.937 | 12.5 | 6.79 | 
| cache.m8g.xlarge | 7.2 | Yes | Yes | Yes | 1.875 | 12.5 | 14.18 | 
| cache.m8g.2xlarge | 7.2 | Yes | Yes | Yes | 3.75 | 15 | 29.68 | 
| cache.m8g.4xlarge | 7.2 | Yes | Yes | Yes | 7.5 | 15 | 61.33 | 
| cache.m8g.8xlarge | 7.2 | Yes | Yes | Yes | 15 | N/A | 124.65 | 
| cache.m8g.12xlarge | 7.2 | Yes | Yes | Yes | 22.5 | N/A | 187.96 | 
| cache.m8g.16xlarge | 7.2 | Yes | Yes | Yes | 30 | N/A | 251.27 | 
| cache.m7g.large | 7.2 | Yes | No | Yes | 0.937 | 12.5 | 6.38 | 
| cache.m7g.xlarge | 7.2 | Yes | Yes | Yes | 1.876 | 12.5 | 12.93 | 
| cache.m7g.2xlarge | 7.2 | Yes | Yes | Yes | 3.75 | 15 | 26.04 | 
| cache.m7g.4xlarge | 7.2 | Yes | Yes | Yes | 7.5 | 15 | 52.26 | 
| cache.m7g.8xlarge | 7.2 | Yes | Yes | Yes | 15 | N/A | 103.68 | 
| cache.m7g.12xlarge | 7.2 | Yes | Yes | Yes | 22.5 | N/A | 157.12 | 
| cache.m7g.16xlarge | 7.2 | Yes | Yes | Yes | 30 | N/A | 209.55 | 
| cache.m6g.large | 7.2 | No | No | No | 0.75 | 10.0 | 6.38 | 
| cache.m6g.xlarge | 7.2 | Yes | Yes | Yes | 1.25 | 10.0 | 12.93 | 
| cache.m6g.2xlarge | 7.2 | Yes | Yes | Yes | 2.5 | 10.0 | 26.04 | 
| cache.m6g.4xlarge | 7.2 | Yes | Yes | Yes | 5.0 | 10.0 | 52.26 | 
| cache.m6g.8xlarge | 7.2 | Yes | Yes | Yes | 12 | N/A | 103.68 | 
| cache.m6g.12xlarge | 7.2 | Yes | Yes | Yes | 20 | N/A | 157.12 | 
| cache.m6g.16xlarge | 7.2 | Yes | Yes | Yes | 25 | N/A | 209.55 | 
| cache.m5.large | 7.2 | No | No | No | 0.75 | 10.0 | 6.38 | 
| cache.m5.xlarge | 7.2 | Yes | No | No | 1.25 | 10.0 | 12.93 | 
| cache.m5.2xlarge | 7.2 | Yes | Yes | Yes | 2.5 | 10.0 | 26.04 | 
| cache.m5.4xlarge | 7.2 | Yes | Yes | Yes | 5.0 | 10.0 | 52.26 | 
| cache.m5.12xlarge | 7.2 | Yes | Yes | Yes | 12 | N/A | 157.12 | 
| cache.m5.24xlarge | 7.2 | Yes | Yes | Yes | 25 | N/A | 314.32 | 
| cache.m4.large | 7.2 | No | No | No | 0.45 | 1.2 | 6.42 | 
| cache.m4.xlarge | 7.2 | Yes | No | No | 0.75 | 2.8 | 14.28 | 
| cache.m4.2xlarge | 7.2 | Yes | Yes | Yes | 1.0 | 10.0 | 29.70 | 
| cache.m4.4xlarge | 7.2 | Yes | Yes | Yes | 2.0 | 10.0 | 60.78 | 
| cache.m4.10xlarge | 7.2 | Yes | Yes | Yes | 5.0 | 10.0 | 154.64 | 
| cache.t4g.micro | 7.2 | No | No | No | 0.064 | 5.0 | 0.50 | 
| cache.t4g.small | 7.2 | No | No | No | 0.128 | 5.0 | 1.37 | 
| cache.t4g.medium | 7.2 | No | No | No | 0.256 | 5.0 | 3.09 | 
| cache.t3.micro | 7.2 | No | No | No | 0.064 | 5.0 | 0.50 | 
| cache.t3.small | 7.2 | No | No | No | 0.128 | 5.0 | 1.37 | 
| cache.t3.medium | 7.2 | No | No | No | 0.256 | 5.0 | 3.09 | 
| cache.t2.micro | 7.2 | No | No | No | 0.064 | 1.024 | 0.555 | 
| cache.t2.small | 7.2 | No | No | No | 0.128 | 1.024 | 1.55 | 
| cache.t2.medium | 7.2 | No | No | No | 0.256 | 1.024 | 3.22 | 

**Memory optimized**


| Instance type | Minimum supported Valkey version | Enhanced I/O | TLS Offloading | Enhanced I/O Multiplexing | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) | Memory (GiB) | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| cache.r8g.large | 7.2 | Yes | No | Yes | 0.937 | 12.5 | 14.18 | 
| cache.r8g.xlarge | 7.2 | Yes | Yes | Yes | 1.875 | 12.5 | 29.68 | 
| cache.r8g.2xlarge | 7.2 | Yes | Yes | Yes | 3.75 | 15 | 61.33 | 
| cache.r8g.4xlarge | 7.2 | Yes | Yes | Yes | 7.5 | 15 | 124.65 | 
| cache.r8g.8xlarge | 7.2 | Yes | Yes | Yes | 15 | N/A | 251.27 | 
| cache.r8g.12xlarge | 7.2 | Yes | Yes | Yes | 22.5 | N/A | 377.9 | 
| cache.r8g.16xlarge | 7.2 | Yes | Yes | Yes | 30 | N/A | 504.52 | 
| cache.r7g.large | 7.2 | Yes | No | Yes | 0.937 | 12.5 | 13.07 | 
| cache.r7g.xlarge | 7.2 | Yes | Yes | Yes | 1.876 | 12.5 | 26.32 | 
| cache.r7g.2xlarge | 7.2 | Yes | Yes | Yes | 3.75 | 15 | 52.82 | 
| cache.r7g.4xlarge | 7.2 | Yes | Yes | Yes | 7.5 | 15 | 105.81 | 
| cache.r7g.8xlarge | 7.2 | Yes | Yes | Yes | 15 | N/A | 209.55 | 
| cache.r7g.12xlarge | 7.2 | Yes | Yes | Yes | 22.5 | N/A | 317.77 | 
| cache.r7g.16xlarge | 7.2 | Yes | Yes | Yes | 30 | N/A | 419.09 | 
| cache.r6g.large | 7.2 | No | No | No | 0.75 | 10.0 | 13.07 | 
| cache.r6g.xlarge | 7.2 | Yes | Yes | Yes | 1.25 | 10.0 | 26.32 | 
| cache.r6g.2xlarge | 7.2 | Yes | Yes | Yes | 2.5 | 10.0 | 52.82 | 
| cache.r6g.4xlarge | 7.2 | Yes | Yes | Yes | 5.0 | 10.0 | 105.81 | 
| cache.r6g.8xlarge | 7.2 | Yes | Yes | Yes | 12 | N/A | 209.55 | 
| cache.r6g.12xlarge | 7.2 | Yes | Yes | Yes | 20 | N/A | 317.77 | 
| cache.r6g.16xlarge | 7.2 | Yes | Yes | Yes | 25 | N/A | 419.09 | 
| cache.r5.large | 7.2 | No | No | No | 0.75 | 10.0 | 13.07 | 
| cache.r5.xlarge | 7.2 | Yes | No | No | 1.25 | 10.0 | 26.32 | 
| cache.r5.2xlarge | 7.2 | Yes | Yes | Yes | 2.5 | 10.0 | 52.82 | 
| cache.r5.4xlarge | 7.2 | Yes | Yes | Yes | 5.0 | 10.0 | 105.81 | 
| cache.r5.12xlarge | 7.2 | Yes | Yes | Yes | 12 | N/A | 317.77 | 
| cache.r5.24xlarge | 7.2 | Yes | Yes | Yes | 25 | N/A | 635.61 | 
| cache.r4.large | 7.2 | No | No | No | 0.75 | 10.0 | 12.30 | 
| cache.r4.xlarge | 7.2 | Yes | No | No | 1.25 | 10.0 | 25.05 | 
| cache.r4.2xlarge | 7.2 | Yes | Yes | Yes | 2.5 | 10.0 | 50.47 | 
| cache.r4.4xlarge | 7.2 | Yes | Yes | Yes | 5.0 | 10.0 | 101.38 | 
| cache.r4.8xlarge | 7.2 | Yes | Yes | Yes | 12 | N/A | 203.26 | 
| cache.r4.16xlarge | 7.2 | Yes | Yes | Yes | 25 | N/A | 407.00 | 

**Memory optimized with data tiering**


| Instance type | Minimum supported Valkey version | Enhanced I/O | TLS Offloading | Enhanced I/O Multiplexing | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) | Memory (GiB) | SSD (GiB) | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| cache.r6gd.xlarge | 7.2 | Yes | No | No | 1.25 | 10 | 26.32 | 99.33 | 
| cache.r6gd.2xlarge | 7.2 | Yes | Yes | Yes | 2.5 | 10 | 52.82 | 199.07 | 
| cache.r6gd.4xlarge | 7.2 | Yes | Yes | Yes | 5.0 | 10 | 105.81 | 398.14 | 
| cache.r6gd.8xlarge | 7.2 | Yes | Yes | Yes | 12 | N/A | 209.55 | 796.28 | 
| cache.r6gd.12xlarge | 7.2 | Yes | Yes | Yes | 20 | N/A | 317.77 | 1194.42 | 
| cache.r6gd.16xlarge | 7.2 | Yes | Yes | Yes | 25 | N/A | 419.09 | 1592.56 | 

**Network optimized**


| Instance type | Minimum supported Valkey version | Enhanced I/O | TLS Offloading | Enhanced I/O Multiplexing | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) | Memory (GiB) | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| cache.c8gn.large | 7.2 | No | No | No | 6.25 | 30 | 3.1 | 
| cache.c8gn.xlarge | 7.2 | Yes | Yes | Yes | 12.5 | 40 | 6.79 | 
| cache.c8gn.2xlarge | 7.2 | Yes | Yes | Yes | 25 | 50 | 14.18 | 
| cache.c8gn.4xlarge | 7.2 | Yes | Yes | Yes | 50 | N/A | 29.68 | 
| cache.c8gn.8xlarge | 7.2 | Yes | Yes | Yes | 100 | N/A | 61.33 | 
| cache.c8gn.12xlarge | 7.2 | Yes | Yes | Yes | 150 | N/A | 92.99 | 
| cache.c8gn.16xlarge | 7.2 | Yes | Yes | Yes | 200 | N/A | 124.65 | 
| cache.c7gn.large | 7.2 | No | No | No | 6.25 | 30 | 3.09 | 
| cache.c7gn.xlarge | 7.2 | Yes | Yes | Yes | 12.5 | 40 | 6.38 | 
| cache.c7gn.2xlarge | 7.2 | Yes | Yes | Yes | 25 | 50 | 12.94 | 
| cache.c7gn.4xlarge | 7.2 | Yes | Yes | Yes | 50 | N/A | 26.05 | 
| cache.c7gn.8xlarge | 7.2 | Yes | Yes | Yes | 100 | N/A | 52.26 | 
| cache.c7gn.12xlarge | 7.2 | Yes | Yes | Yes | 150 | N/A | 78.56 | 
| cache.c7gn.16xlarge | 7.2 | Yes | Yes | Yes | 200 | N/A | 105.81 | 

## Current Generation (Redis OSS)
<a name="CacheNodes.CurrentGen-Redis"></a>

**General**


| Instance type | Minimum supported Redis OSS version | Enhanced I/O with Redis OSS 5.0.6\+ | TLS Offloading with Redis OSS 6.2.5\+ | Enhanced I/O Multiplexing with Redis OSS 7.0.4\+ | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) | Memory (GiB) | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| cache.m7g.large | 6.2 | Yes | No | Yes | 0.937 | 12.5 | 6.38 | 
| cache.m7g.xlarge | 6.2 | Yes | Yes | Yes | 1.876 | 12.5 | 12.93 | 
| cache.m7g.2xlarge | 6.2 | Yes | Yes | Yes | 3.75 | 15 | 26.04 | 
| cache.m7g.4xlarge | 6.2 | Yes | Yes | Yes | 7.5 | 15 | 52.26 | 
| cache.m7g.8xlarge | 6.2 | Yes | Yes | Yes | 15 | N/A | 103.68 | 
| cache.m7g.12xlarge | 6.2 | Yes | Yes | Yes | 22.5 | N/A | 157.12 | 
| cache.m7g.16xlarge | 6.2 | Yes | Yes | Yes | 30 | N/A | 209.55 | 
| cache.m6g.large | 5.0.6 | No | No | No | 0.75 | 10.0 | 6.38 | 
| cache.m6g.xlarge | 5.0.6 | Yes | Yes | Yes | 1.25 | 10.0 | 12.93 | 
| cache.m6g.2xlarge | 5.0.6 | Yes | Yes | Yes | 2.5 | 10.0 | 26.04 | 
| cache.m6g.4xlarge | 5.0.6 | Yes | Yes | Yes | 5.0 | 10.0 | 52.26 | 
| cache.m6g.8xlarge | 5.0.6 | Yes | Yes | Yes | 12 | N/A | 103.68 | 
| cache.m6g.12xlarge | 5.0.6 | Yes | Yes | Yes | 20 | N/A | 157.12 | 
| cache.m6g.16xlarge | 5.0.6 | Yes | Yes | Yes | 25 | N/A | 209.55 | 
| cache.m5.large | 4.0.10 | N | N | N | 0.75 | 10.0 | 6.38 | 
| cache.m5.xlarge | 4.0.10 | Y | N | N | 1.25 | 10.0 | 12.93 | 
| cache.m5.2xlarge | 4.0.10 | Y | Y | Y | 2.5 | 10.0 | 26.04 | 
| cache.m5.4xlarge | 4.0.10 | Y | Y | Y | 5.0 | 10.0 | 52.26 | 
| cache.m5.12xlarge | 4.0.10 | Y | Y | Y | 12 | N/A | 157.12 | 
| cache.m5.24xlarge | 4.0.10 | Y | Y | Y | 25 | N/A | 314.32 | 
| cache.m4.large | 4.0.10 | N | N | N | 0.45 | 1.2 | 6.42 | 
| cache.m4.xlarge | 4.0.10 | Y | N | N | 0.75 | 2.8 | 14.28 | 
| cache.m4.2xlarge | 4.0.10 | Y | Y | Y | 1.0 | 10.0 | 29.70 | 
| cache.m4.4xlarge | 4.0.10 | Y | Y | Y | 2.0 | 10.0 | 60.78 | 
| cache.m4.10xlarge | 4.0.10 | Y | Y | Y | 5.0 | 10.0 | 154.64 | 
| cache.t4g.micro | 4.0.10 | N | N | N | 0.064 | 5.0 | 0.50 | 
| cache.t4g.small | 5.0.6 | No | No | No | 0.128 | 5.0 | 1.37 | 
| cache.t4g.medium | 5.0.6 | No | No | No | 0.256 | 5.0 | 3.09 | 
| cache.t3.micro | 4.0.10 | N | N | N | 0.064 | 5.0 | 0.50 | 
| cache.t3.small | 4.0.10 | N | N | N | 0.128 | 5.0 | 1.37 | 
| cache.t3.medium | 4.0.10 | N | N | N | 0.256 | 5.0 | 3.09 | 
| cache.t2.micro | 4.0.10 | N | N | N | 0.064 | 1.024 | 0.555 | 
| cache.t2.small | 4.0.10 | N | N | N | 0.128 | 1.024 | 1.55 | 
| cache.t2.medium | 4.0.10 | N | N | N | 0.256 | 1.024 | 3.22 | 

**Memory optimized**


| Instance type | Minimum supported Redis OSS version | Enhanced I/O with Redis OSS 5.0.6\+ | TLS Offloading with Redis OSS 6.2.5\+ | Enhanced I/O Multiplexing with Redis OSS 7.0.4\+ | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) | Memory (GiB) | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| cache.r7g.large | 6.2 | Yes | No | Yes | 0.937 | 12.5 | 13.07 | 
| cache.r7g.xlarge | 6.2 | Yes | Yes | Yes | 1.876 | 12.5 | 26.32 | 
| cache.r7g.2xlarge | 6.2 | Yes | Yes | Yes | 3.75 | 15 | 52.82 | 
| cache.r7g.4xlarge | 6.2 | Yes | Yes | Yes | 7.5 | 15 | 105.81 | 
| cache.r7g.8xlarge | 6.2 | Yes | Yes | Yes | 15 | N/A | 209.55 | 
| cache.r7g.12xlarge | 6.2 | Yes | Yes | Yes | 22.5 | N/A | 317.77 | 
| cache.r7g.16xlarge | 6.2 | Yes | Yes | Yes | 30 | N/A | 419.09 | 
| cache.r6g.large | 5.0.6 | No | No | No | 0.75 | 10.0 | 13.07 | 
| cache.r6g.xlarge | 5.0.6 | Yes | Yes | Yes | 1.25 | 10.0 | 26.32 | 
| cache.r6g.2xlarge | 5.0.6 | Yes | Yes | Yes | 2.5 | 10.0 | 52.82 | 
| cache.r6g.4xlarge | 5.0.6 | Yes | Yes | Yes | 5.0 | 10.0 | 105.81 | 
| cache.r6g.8xlarge | 5.0.6 | Yes | Yes | Yes | 12 | N/A | 209.55 | 
| cache.r6g.12xlarge | 5.0.6 | Yes | Yes | Yes | 20 | N/A | 317.77 | 
| cache.r6g.16xlarge | 5.0.6 | Yes | Yes | Yes | 25 | N/A | 419.09 | 
| cache.r5.large | 4.0.10 | N | N | N | 0.75 | 10.0 | 13.07 | 
| cache.r5.xlarge | 4.0.10 | Y | N | N | 1.25 | 10.0 | 26.32 | 
| cache.r5.2xlarge | 4.0.10 | Y | Y | Y | 2.5 | 10.0 | 52.82 | 
| cache.r5.4xlarge | 4.0.10 | Y | Y | Y | 5.0 | 10.0 | 105.81 | 
| cache.r5.12xlarge | 4.0.10 | Y | Y | Y | 12 | N/A | 317.77 | 
| cache.r5.24xlarge | 4.0.10 | Y | Y | Y | 25 | N/A | 635.61 | 
| cache.r4.large | 4.0.10 | N | N | N | 0.75 | 10.0 | 12.30 | 
| cache.r4.xlarge | 4.0.10 | Y | N | N | 1.25 | 10.0 | 25.05 | 
| cache.r4.2xlarge | 4.0.10 | Y | Y | Y | 2.5 | 10.0 | 50.47 | 
| cache.r4.4xlarge | 4.0.10 | Y | Y | Y | 5.0 | 10.0 | 101.38 | 
| cache.r4.8xlarge | 4.0.10 | Y | Y | Y | 12 | N/A | 203.26 | 
| cache.r4.16xlarge | 4.0.10 | Y | Y | Y | 25 | N/A | 407.00 | 

**Memory optimized with data tiering**


| Instance type | Minimum supported Redis OSS version | Enhanced I/O with Redis OSS 5.0.6\+ | TLS Offloading with Redis OSS 6.2.5\+ | Enhanced I/O Multiplexing with Redis OSS 7.0.4\+ | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) | Memory (GiB) | SSD (GiB) | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| cache.r6gd.xlarge | 6.2.0 | Yes | No | No | 1.25 | 10 | 26.32 | 99.33 | 
| cache.r6gd.2xlarge | 6.2.0 | Yes | Yes | Yes | 2.5 | 10 | 52.82 | 199.07 | 
| cache.r6gd.4xlarge | 6.2.0 | Yes | Yes | Yes | 5.0 | 10 | 105.81 | 398.14 | 
| cache.r6gd.8xlarge | 6.2.0 | Yes | Yes | Yes | 12 | N/A | 209.55 | 796.28 | 
| cache.r6gd.12xlarge | 6.2.0 | Yes | Yes | Yes | 20 | N/A | 317.77 | 1194.42 | 
| cache.r6gd.16xlarge | 6.2.0 | Yes | Yes | Yes | 25 | N/A | 419.09 | 1592.56 | 

**Network optimized**


| Instance type | Minimum supported Redis OSS version | Enhanced I/O with Redis OSS 5.0.6\+ | TLS Offloading with Redis OSS 6.2.5\+ | Enhanced I/O Multiplexing with Redis OSS 7.0.4\+ | Baseline bandwidth (Gbps) | Burst bandwidth (Gbps) | Memory (GiB) | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| cache.c7gn.large | 6.2 | No | No | No | 6.25 | 30 | 3.09 | 
| cache.c7gn.xlarge | 6.2 | Yes | Yes | Yes | 12.5 | 40 | 6.38 | 
| cache.c7gn.2xlarge | 6.2 | Yes | Yes | Yes | 25 | 50 | 12.94 | 
| cache.c7gn.4xlarge | 6.2 | Yes | Yes | Yes | 50 | N/A | 26.05 | 
| cache.c7gn.8xlarge | 6.2 | Yes | Yes | Yes | 100 | N/A | 52.26 | 
| cache.c7gn.12xlarge | 6.2 | Yes | Yes | Yes | 150 | N/A | 78.56 | 
| cache.c7gn.16xlarge | 6.2 | Yes | Yes | Yes | 200 | N/A | 105.81 | 

## Burstable Performance Instances
<a name="CacheNodes.Burstable"></a>

You can launch general-purpose burstable T4g, T3-Standard and T2-Standard cache nodes in Amazon ElastiCache. These nodes provide a baseline level of CPU performance with the ability to burst CPU usage at any time until the accrued credits are exhausted. A *CPU credit* provides the performance of a full CPU core for one minute.

Amazon ElastiCache's T4g, T3 and T2 nodes are configured as standard and suited for workloads with an average CPU utilization that is consistently below the baseline performance of the instance. To burst above the baseline, the node spends credits that it has accrued in its CPU credit balance. If the node is running low on accrued credits, performance is gradually lowered to the baseline performance level. This gradual lowering ensures the node doesn't experience a sharp performance drop-off when its accrued CPU credit balance is depleted. For more information, see [CPU Credits and Baseline Performance for Burstable Performance Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-credits-baseline-concepts.html) in the *Amazon EC2 User Guide*.**

The following table lists the burstable performance node types, the rate at which CPU credits are earned per hour. It also shows the maximum number of earned CPU credits that a node can accrue and the number of vCPUs per node. In addition, it gives the baseline performance level as a percentage of a full core performance (using a single vCPU).


| Node type | CPU credits earned per hour |  Maximum earned credits that can be accrued\* |  vCPUs  |  Baseline performance per vCPU  |  Network performance  | Memory (GiB) | 
| --- | --- | --- | --- | --- | --- | --- | 
| t4g.micro | 12 | 288 | 2 | 10% | Up to 5 Gigabit | 0.5 | 
| t4g.small | 24 | 576 | 2 | 20% | Up to 5 Gigabit | 1.37 | 
| t4g.medium | 24 | 576 | 2 | 20% | Up to 5 Gigabit | 3.09 | 
| t3.micro | 12 | 288 | 2 | 10% | Up to 5 Gigabit | 0.5 | 
| t3.small | 24 | 576 | 2 | 20% | Up to 5 Gigabit | 1.37 | 
| t3.medium | 24 | 576 | 2 | 20% | Up to 5 Gigabit | 3.09 | 
| t2.micro | 6 | 144 | 1 | 10% | Low to moderate | 0.5 | 
| t2.small | 12 | 288 | 1 | 20% | Low to moderate | 1.55 | 
| t2.medium | 24 | 576 | 2 | 20% | Low to moderate | 3.22 | 

\* The number of credits that can be accrued is equivalent to the number of credits that can be earned in a 24-hour period.

\*\* The baseline performance in the table is per vCPU. Some node sizes that have more than one vCPU. For these, calculate the baseline CPU utilization for the node by multiplying the vCPU percentage by the number of vCPUs.

The following CPU credit metrics are available for T3 and T4g burstable performance instances:

**Note**  
These metrics are not available for T2 burstable performance instances.
+ `CPUCreditUsage`
+ `CPUCreditBalance`

For more information on these metrics, see [CPU Credit Metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html#cpu-credit-metrics).

In addition, be aware of these details:
+ All current generation node types are created in a virtual private cloud (VPC) based on Amazon VPC by default.
+ Redis OSS append-only files (AOF) aren't supported for T2 instances. Redis OSS configuration variables `appendonly` and `appendfsync` aren't supported.

## Supported node types by AWS Region
<a name="CacheNodes.SupportedTypesByRegion"></a>

Supported node types may vary between AWS Regions. For more details, see [Amazon ElastiCache pricing](https://aws.amazon.com/elasticache/pricing/).

## Related Information
<a name="CacheNodes.RelatedInfo"></a>
+ [Amazon ElastiCache Product Features and Details](https://aws.amazon.com/elasticache/details)
+ [Memcached Node-Type Specific Parameters for Memcached](ParameterGroups.Engine.md#ParameterGroups.Memcached) 
+ [Valkey and Redis OSS parameters](ParameterGroups.Engine.md#ParameterGroups.Redis)
+ [In Transit Encryption (TLS)](in-transit-encryption.md)