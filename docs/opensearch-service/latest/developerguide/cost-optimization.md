

# Cost optimization techniques for Amazon OpenSearch Service
<a name="cost-optimization"></a>

The following are some of the most commonly used techniques to optimize cost while using Amazon OpenSearch Service — both Managed Clusters and Serverless. Since every workload is unique, evaluate these strategies against your specific usage patterns and validate them in a test environment before applying to production.

**Topics**
+ [Save Big with 1-Year or Multi-Year Commitments](#cost-opt-savings-commitments)
+ [Cost optimization for Amazon OpenSearch Service managed clusters](#cost-optimization-managed)
+ [Cost optimization for Amazon OpenSearch Service Serverless](#cost-optimization-serverless)

## Save Big with 1-Year or Multi-Year Commitments
<a name="cost-opt-savings-commitments"></a>

With Amazon OpenSearch Service, you pay only for what you use with no minimum fee or usage requirement. Amazon OpenSearch Service offers two deployment models:
+ For Managed Clusters, you are charged for instance hours, storage, and data transfer. Pricing depends on the instance type and storage tier you choose. For instances, you can use Reserved Instance pricing, or save with Database Savings Plans over on-demand pricing.
+ For Serverless, you are charged for compute and storage separately. Compute capacity is measured in OpenSearch Compute Units (OCUs), which correspond to the CPU, memory, and I/O resources required to index data or run queries. Serverless is also covered by Database Savings Plans.

Database Savings Plans are a flexible pricing model that reduces your Amazon OpenSearch Service costs when you commit (measured in $/hour) to a consistent amount of usage over a 1-year term. This savings plan automatically applies to eligible serverless and provisioned instance usage regardless of engine version, instance family, size, deployment option, or AWS Region with no upfront payment. For more information, see the [Database Savings Plans pricing page](https://aws.amazon.com/savingsplans/database-pricing/).

Reserved Instances offer a pricing model that reduces your Amazon OpenSearch Service costs when you commit to a specific instance configuration for a 1-year or 3-year term. Reserved Instances provide significant discounts compared to On-Demand pricing when you reserve capacity for a particular instance type, size, and AWS Region. Payment options include All Upfront, Partial Upfront, or No Upfront, with greater discounts available for upfront payments. For more information, see the [Amazon OpenSearch Service Reserved Instances pricing page](https://aws.amazon.com/opensearch-service/pricing/).

## Cost optimization for Amazon OpenSearch Service managed clusters
<a name="cost-optimization-managed"></a>

### Derived Source — Skip storing the \_source field
<a name="cost-opt-derived-source"></a>

Derived Source is a storage optimization feature that eliminates the overhead of storing the `_source` field:
+ OpenSearch stores every ingested document twice: once in the `_source` field (raw document) and once as indexed fields for search.
+ The `_source` field alone can consume significant storage space — often 30–50% of total index storage.
+ With Derived Source, you skip storing `_source` and instead dynamically reconstruct it from indexed fields when needed (during search, get, mget, reindex, or update operations).
+ This is opt-in, enabled at index creation using composite index settings.
+ Available in all regions where OpenSearch 3.1 or later is supported.

Best for: Analytical and log workloads where you don't need to retrieve the original raw document frequently but still need to search and aggregate over fields.

For more information, see the [open source documentation](https://docs.opensearch.org/latest/mappings/metadata-fields/source/) and the [What's New announcement](https://aws.amazon.com/about-aws/whats-new/2025/09/amazon-opensearch-derived-source/).

### OR1 / OR2 / OM2 instances — OpenSearch-optimized instance families
<a name="cost-opt-or-instances"></a>

OR1 and the newer OR2 and OM2 instances use Amazon S3 for replica storage via segment replication:
+ OR2: Up to 26% higher indexing throughput than OR1, 70% more than R7g instances.
+ OM2: Up to 15% higher indexing throughput than OR1, 66% more than M7g instances.
+ Both use the same architecture: local EBS for primary storage and S3 for durability.
+ Eliminates replica storage cost — replicas stored in S3 (11 nines durability) instead of expensive EBS volumes.
+ Up to 30% price-performance improvement over previous-generation instances.
+ Supports shallow snapshot v2 — near-instant snapshots with no I/O overhead.

Best for: Indexing-heavy operational analytics and log analytics workloads.

For more information, see the [OR2 and OM2 What's New announcement](https://aws.amazon.com/about-aws/whats-new/2025/03/aws-or2-om2-instances-opensearch-service/) and the [OpenSearch Optimized Instances for Amazon OpenSearch Service domains](or1.md) developer guide topic.

### Index rollups — Aggregate historical time-series data
<a name="cost-opt-rollups"></a>

Index rollups summarize and compress older time-series data into coarser time intervals, dramatically reducing storage volume:
+ IoT/sensor data: Keep per-second data in hot storage for recent periods; roll up to hourly or daily summaries for older data.
+ System metrics: Retain detailed metrics for the last 30 days; aggregate older data into hourly or daily summaries.
+ Log data: Preserve full detail for the active troubleshooting window (for example, 1 week); maintain summarized error patterns for older periods.
+ Combine with ISM policies to automate rollup and tier migration in a single lifecycle policy.
+ Larger savings when aggregating from seconds to hours versus seconds to minutes.

For more information, see the [Index Rollups blog post](https://aws.amazon.com/blogs/big-data/decrease-your-storage-costs-with-amazon-opensearch-service-index-rollups/).

### Index State Management — Automate full data lifecycle
<a name="cost-opt-ism"></a>

ISM policies automate the movement of indexes through storage tiers and lifecycle actions:
+ Automatically migrate indexes: Hot to UltraWarm to Cold to Delete, based on age, size, or document count.
+ Trigger rollups before tier transitions to reduce data volume.
+ Set rollover policies (for example, when an index reaches 50 GB or is 30 days old) to control index growth.
+ Automate force merge on read-only indexes to reclaim storage from deleted documents.
+ Combine with rollups for maximum savings on large time-series datasets.

### Right-size instance types and count
<a name="cost-opt-right-size"></a>

Key guidance from the Well-Architected OpenSearch Lens and right-sizing best practices:
+ Always use the latest generation of instances (for example, Graviton3 instances deliver up to 25% better performance over Graviton2-based instances).
+ Use gp3 EBS volumes instead of gp2 — better performance at lower cost with no additional charge.
+ Match instance type to workload: memory-optimized for search-heavy, compute-optimized for indexing-heavy.
+ Evaluate dedicated cluster manager nodes: Only needed for 3 or more data nodes; avoid over-provisioning master node size.
+ Monitor CloudWatch metrics to detect over-provisioning: sustained CPU below 40%, JVM below 50%, and storage below 50% are signs of waste.
+ Optimal ranges: CPU 60–80%, JVM 65–85%, Storage 70–85% for sustained workloads.

For more information, see the [Right-Sizing Best Practices blog post](https://aws.amazon.com/blogs/big-data/best-practices-for-right-sizing-amazon-opensearch-service-domains/).

### Shard optimization — Avoid over-sharding
<a name="cost-opt-shards"></a>

Over-sharding is a hidden cost driver — too many small shards waste CPU, memory, and JVM heap:
+ Recommended shard sizes: 10–50 GiB per shard depending on workload.
+ No more than 25 shards per GiB of Java heap, no more than 1,000 shards per data node.
+ Use ISM rollover policies to control index growth and avoid unbounded shard proliferation.
+ Reduce replica count where durability allows (OR1/OR2 instances eliminate the need for replicas entirely).
+ Use force merge on read-only indexes to reduce segment count and reclaim storage.

For more information, see [How Many Shards Do I Need?](https://aws.amazon.com/blogs/big-data/amazon-opensearch-service-101-how-many-shards-do-i-need/)

### Zero-ETL / Direct Query with Amazon S3
<a name="cost-opt-direct-query"></a>

For data that is very rarely queried but must remain accessible, Direct Query (zero-ETL with S3) allows querying S3 data directly from OpenSearch without ingesting it:
+ No ingestion cost — data stays in S3.
+ No hot-tier storage cost for archival data.
+ Pay-per-query compute model.
+ Supports OpenSearch Dashboards for visualization.
+ Latency of seconds or minutes is acceptable — not for real-time use cases.

### Sampling and compression at ingestion
<a name="cost-opt-sampling"></a>

Reduce costs before data even reaches OpenSearch:
+ Sampling: Ingest only a representative subset of high-volume log streams (for example, 10% of debug logs).
+ Index compression: Enable the best-compression codec to reduce storage footprint.
+ Field filtering: Drop high-cardinality, low-value fields before indexing (for example, raw stack traces for old logs).
+ Retention policies: Define maximum retention windows aligned to compliance requirements — never store data indefinitely.

### Avoid extended support costs — Stay current on engine versions
<a name="cost-opt-extended-support"></a>

Amazon OpenSearch Service charges a flat fee per Normalized Instance Hour for engine versions in Extended Support:
+ Staying on older, unsupported versions incurs additional charges on top of instance costs.
+ Upgrade to current supported versions to avoid Extended Support fees.

### Cost allocation tags and CloudWatch monitoring
<a name="cost-opt-tags-monitoring"></a>

Proactive cost governance prevents waste:
+ Apply cost allocation tags to OpenSearch domains for detailed cost tracking per team or workload.
+ Set CloudWatch alarms for storage utilization, JVM pressure, and CPU to catch over-provisioning early.
+ Use AWS Cost Explorer to identify domains with consistently low utilization.
+ Evaluate Auto-Tune — automatically adjusts JVM heap size and other settings to improve performance and reduce resource waste.

## Cost optimization for Amazon OpenSearch Service Serverless
<a name="cost-optimization-serverless"></a>

### Disk-optimized vector search (vector collections)
<a name="cost-opt-disk-vector"></a>

Disk-optimized vector search is one of the most powerful cost-reduction techniques for vector workloads. It runs vector search at a fraction of the cost of in-memory mode by keeping only compressed vectors in RAM and storing full-precision vectors on disk.

How it works:
+ In standard (`in_memory`) mode, the full HNSW graph is loaded into RAM — which becomes prohibitively expensive at scale.
+ In `on_disk` mode, only compressed (quantized) vectors are kept in memory for candidate generation; full-precision vectors are retrieved from disk only for the final rescoring phase (two-phase search).
+ This dramatically reduces RAM requirements while maintaining high search quality.
+ Default `on_disk` mode uses 32x binary quantization — reducing memory requirements by 97% versus in-memory mode.
+ Supports compression levels: 2x (FP16), 4x (byte), 8x, 16x, 32x (binary).
+ P90 latency in the 100–200ms range — suitable for workloads that don't require single-digit millisecond response times.

Cost savings benchmarks:


| Dataset | Recall@100 | P90 Latency | Cost Reduction | 
| --- | --- | --- | --- | 
| Cohere TREC-RAG | 0.94 | 104ms | 83% | 
| Tasb-1M | 0.96 | 7ms | 67% | 
| Marco-1M | 0.99 | 7ms | 67% | 

Best for: RAG pipelines, semantic search, document retrieval, and any vector workload where P90 latency of 100–200ms is acceptable and cost reduction is a priority.

**Note**  
To apply this change to existing indexed data, you need to re-index. You can use an external pipeline tool such as to re-index data into a new index.

For more information, see the [Disk-Optimized Vector Search blog post](https://aws.amazon.com/blogs/big-data/opensearch-vector-engine-is-now-disk-optimized-for-low-cost-accurate-vector-search/), the [Quantization Techniques blog post](https://aws.amazon.com/blogs/big-data/cost-optimized-vector-database-introduction-to-amazon-opensearch-service-quantization-techniques/), and [Working with vector search collections](serverless-vector-search.md).

### Vector Auto-Optimize (vector collections)
<a name="cost-opt-auto-optimize"></a>

Auto-optimize automatically evaluates vector index configurations and recommends the best trade-off between search quality, latency, and memory cost — without requiring vector expertise:
+ Delivers optimization recommendations in under an hour.
+ Integrated with vector ingestion pipelines.
+ Can be combined with GPU-accelerated indexing for billion-scale vector databases.

For more information, see the [Auto-Optimize blog post](https://aws.amazon.com/blogs/big-data/auto-optimize-your-amazon-opensearch-service-vector-database/).

### GPU-accelerated vector indexing (vector collections)
<a name="cost-opt-gpu"></a>

GPU acceleration offloads HNSW vector indexing to serverless GPUs, dramatically reducing the time and OCU cost of building large vector indexes:
+ 6.4x to 13.8x faster index build times compared to CPU-only indexing.
+ Up to 75% lower indexing OCU cost for write-heavy vector workloads.
+ GPUs are attached dynamically — you only pay for OCUs when GPU acceleration is active.
+ Enables billion-scale vector databases to be built in under an hour.
+ Charged separately as Vector Acceleration OCUs.

Best for: Large-scale initial vector ingestion or frequent model retraining scenarios where rebuilding indexes is costly.

For more information, see the [GPU Acceleration blog post](https://aws.amazon.com/blogs/big-data/build-billion-scale-vector-databases-in-under-an-hour-with-gpu-acceleration-on-amazon-opensearch-service/).

### Set maximum OCU limits (all collection types)
<a name="cost-opt-ocu-limits"></a>

Amazon OpenSearch Service Serverless auto-scales OCUs based on demand. Without a cap, costs can spike unexpectedly. Set a maximum OCU limit at the account level or per collection group to prevent runaway scaling. The system scales up to this limit during peak loads but will not exceed it.

Allowed values:
+ Account level – Any value up to 1,700 OCUs (not restricted to multiples of 16).
+ Collection groups (NextGen) – 0, 2, 4, 8, 16, and multiples of 16 up to 1,696 OCUs.
+ Collection groups (Classic) – 1, 2, 4, 8, 16, and multiples of 16 up to 1,696 OCUs.

Monitor CloudWatch metrics (`OCUUtilization`) to right-size your maximum OCU setting over time.

**Note**  
If utilization hits the maximum OCU cap, performance may degrade significantly even though costs are contained. Hitting the cap does not resolve the underlying cause of the OCU spike. For vector collections, the root cause is typically in-memory vectors, which should be addressed directly by optimizing vector indexing, reducing index size, or tuning recall and accuracy trade-offs.

**Tip**  
Start with a conservative max OCU and increase only when CloudWatch shows sustained utilization near the cap. If you consistently hit the cap, investigate the root cause — particularly in-memory vector usage for vector collections — rather than simply raising the limit.

For more information, see [Managing capacity limits for Amazon OpenSearch Serverless](serverless-scaling.md).

### Optimize retention period (time-series collections)
<a name="cost-opt-retention"></a>

Data lifecycle policies automatically delete data from time-series collections after a specified retention period, preventing unbounded storage growth. Only time-series collections support data lifecycle policies — search and vector collections do not.

The OCU count for time-series collections is directly driven by how much recent data must be kept in local storage. Time-series collections keep only the most recent portion of data in local OCU storage; older data is offloaded to S3, and the number of OCUs scales accordingly:

OCUs required = max(minimum OCUs, OCUs needed to hold data within your retention window)

Configuring data lifecycle policies:
+ Set retention periods from 24 hours to 3,650 days per index or index pattern.
+ Amazon OpenSearch Service Serverless deletes data automatically on a best-effort basis (typically within 48 hours or 10% of the retention period).
+ Rules can be applied at the collection level, index pattern level, or individual index level — more specific rules take precedence.

Sizing example:
+ 1 TiB/day ingestion with a 30-day retention = approximately 1 TiB of hot data = 20 OCUs for indexing \+ 20 OCUs for search.
+ Reducing to a 7-day retention = approximately 233 GiB of hot data = approximately 4 OCUs for indexing \+ 4 OCUs for search.

Shorter retention means less hot data in local storage, fewer OCUs needed, and a lower compute bill. Align retention periods to actual business and compliance requirements — don't retain data indefinitely by default.

For more information, see [Using data lifecycle policies with Amazon OpenSearch Serverless](serverless-lifecycle.md).

### Avoid storing unnecessary data (all collection types)
<a name="cost-opt-avoid-unnecessary-data"></a>

Reducing the volume of data ingested directly reduces both compute (OCUs) and storage costs:
+ Filter fields at ingestion: Use pipelines to drop low-value fields before they reach the collection.
+ Avoid ingesting duplicate or redundant data: Deduplicate at the pipeline level.
+ Use appropriate index mappings: Disable indexing on fields that are stored but never searched (`"index": false`).
+ For search collections: Avoid storing large binary blobs or raw text that inflates storage without search value.

### Collection groups for multi-tenant workloads (all collection types)
<a name="cost-opt-collection-groups"></a>

Collection Groups allow multiple collections with different KMS keys to share OCU resources within the same security boundary, dramatically reducing costs for multi-tenant architectures. Applicable for customers using multiple KMS keys per tenant or per collection:
+ Previously, each unique KMS key required dedicated OCUs — making per-tenant isolation prohibitively expensive.
+ With collection groups, tenants with separate encryption keys can share OCU capacity.
+ Cost savings of up to 90% for large numbers of smaller tenant workloads.
+ Supports both minimum OCUs (guaranteed baseline, no cold starts) and maximum OCUs (cost cap).
+ Collections with different network access types (public and VPC) can coexist in the same group.
+ CloudWatch metrics provide per-group visibility into resource consumption and latency.

Best for: SaaS providers, multi-tenant platforms, or any workload with many small collections each requiring their own KMS key.

For more information, see the [Collection Groups blog post](https://aws.amazon.com/blogs/big-data/amazon-opensearch-serverless-introduces-collection-groups-to-optimize-cost-for-multi-tenant-workloads/), the [What's New announcement](https://aws.amazon.com/about-aws/whats-new/2026/02/amazon-opensearch-serverless-supports-collection-groups/), and [Amazon OpenSearch Serverless collection groups](serverless-collection-groups.md).