

# ADVPERF01-BP05 Benchmark managed and self-hosted services for latency-sensitive bid paths

 Before committing to a managed service or self-managed open-source deployment for any component on the advertising bid path, run performance benchmarks under realistic advertising traffic conditions. After the bidding infrastructure is built around a service that fails to meet latency or throughput requirements in production, migrating away is expensive and disruptive. 

 **Desired outcome:** 
+  Every component on the bid evaluation critical path is validated against your latency and throughput requirements under realistic advertising traffic before production commitment. 
+  Managed service throughput limits, connection pool constraints, and configuration restrictions are discovered during benchmarking rather than under production load. 
+  Self-managed deployments are tested under burst traffic conditions representative of live advertising events (not just steady-state load) before replacing a managed service alternative. 
+  ISV-published benchmark data for advertising-specific workloads (Aerospike, Databricks) is consulted alongside your own measurements when selecting instance types and configurations. 

 **Common anti-patterns:** 
+  Relying solely on vendor-published benchmark specifications or managed service documentation to validate that a service meets your latency requirements, without running benchmarks against your actual advertising traffic patterns. 
+  Benchmarking only at steady-state QPS rather than at the burst traffic volumes that occur during live advertising events. 
+  Treating managed service throughput limits and configuration constraints as acceptable after deployment rather than as disqualifying criteria to evaluate before commitment. 
+  Selecting EC2 instance types for self-managed deployments without consulting ISV-published benchmark data for advertising-specific workload patterns. 

 **Benefits of establishing this best practice:** 
+  Discovering that a managed service throttles under advertising-scale burst traffic during a benchmark run costs hours. Discovering the same issue after building a bidding platform around that service costs weeks of rearchitecting under production pressure. 
+  ISV-published benchmark data for ad tech workloads (Aerospike on I-series Storage Optimized instances, Databricks on Graviton) reflects advertising-specific access patterns (frequency cap lookups, user profile reads, audience segment joins) that general-purpose cloud benchmarks don't capture. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A managed service that meets your latency requirements at launch may throttle as bid volume grows. Many managed services scale by adding capacity like self-managed deployments, sometimes faster. Each managed service still has hard per-tier or per-quota ceilings that your benchmark must test against. A self-managed deployment that performs correctly under synthetic load may degrade under the bursty, correlated traffic patterns of live advertising events. A major sporting event can drive 10x normal QPS across all connected publishers simultaneously. 

 Advertising workloads expose managed service limitations that general workloads don't. Connection pool exhaustion is the most common: bid evaluation services opening thousands of concurrent database connections during traffic bursts can exceed managed service connection limits that never bind under normal enterprise workloads. Throughput throttling at high QPS is the second, and both DynamoDB capacity modes have a window where a live event can outrun them. On-demand instantly accommodates up to double a table's previous peak, so a spike beyond that within 30 minutes can throttle, and a new table starts at 4,000 writes and 12,000 reads per second. Provisioned tables with auto scaling take minutes to react. DynamoDB retains only five minutes of unused capacity as best-effort burst. Per-partition ceilings of 3,000 reads and 1,000 writes per second apply in both modes, as do the 40,000 table-level read and write quotas. For a known event, pre-warm the table with warm throughput. Reproduce these failure modes in benchmarks before production commitment. 

 For self-managed deployments, the software itself can handle the load, because Kafka, Aerospike, and Cassandra are proven at advertising scale. Validate that your specific configuration, on your selected instance types and with your data model and access patterns, meets your latency SLOs. This requires benchmarking with advertising-specific data: user profile records at production scale (hundreds of millions of records), frequency cap check patterns (high read volume, moderate write volume, uniform distribution by user ID hash), and burst traffic profiles derived from historical advertising event data instead of synthetic load generators. 

 Measure latency percentiles (p50, p95, and p99) at peak advertising QPS. The bid path's latency SLO is a p99 requirement. A service that delivers 2ms p50 but 50ms p99 under burst traffic fails the auction deadline even though average performance looks acceptable. Measure under burst conditions (simulate a live event traffic spike) in addition to steady-state load. Record the specific instance types, configuration parameters, and data scale used in each benchmark so future re-evaluations can compare against the same baseline. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define latency and throughput acceptance criteria before benchmarking:** For each bid path component under evaluation, document the p99 latency threshold and peak QPS requirement that the chosen service must meet. These become the pass/fail criteria for the benchmark. For user profile databases, a p99 read latency of 5ms or less at peak bid QPS is a common starting point. For streaming services on the bid log ingest path, sustained throughput at 2–3x average bid volume covers live event bursts. 

1.  **Run benchmarks under advertising-specific burst traffic conditions:** Design benchmark scenarios that reproduce the traffic patterns specific to advertising: gradual ramp to steady-state QPS, followed by a sudden 5–10x spike (simulating a live event), sustained for 60–120 seconds, then ramp-down. Measure p99 latency and error rate throughout the spike, not just at steady state. Reproduce the access pattern of the bid path (key-value lookups by user ID, not sequential scans) using data at production scale. 

1.  **Evaluate Aerospike for high-volume, low-latency data workloads:** Aerospike is widely deployed in ad tech for user profile lookups, frequency capping, and real-time audience segmentation. Review Aerospike's published AWS benchmark results to identify the EC2 instance types (including both Intel and AWS Graviton options) that deliver the best performance-to-cost ratio for your specific workload characteristics before committing to a deployment configuration. Aerospike's I8g (Graviton4) benchmark for ad tech workloads covers user profile lookups and campaign-data access. It doesn't model frequency capping, so validate that pattern separately. 

1.  **Evaluate Databricks for large-scale advertising analytics and ML workloads:** Databricks is broadly adopted for advertising analytics, attribution modeling, audience intelligence, and campaign performance analysis where data volumes are large. Consult Databricks' published AWS benchmark results to compare Intel and Graviton instance performance for your query and processing patterns before finalizing your cluster configuration. For advertising ML workloads, measure training job completion time and inference latency on candidate instance types rather than relying on general-purpose compute benchmarks. 

1.  **Document benchmark results as the binding record for service selection:** Record the instance types, service configuration, data scale, traffic pattern, and measured latency percentiles for each benchmark run. Link the benchmark record to the architecture decision. When a service is re-evaluated (because bid volume has grown, because a new AWS service generation has launched, or because a managed service has released new throughput tiers), compare new benchmark results against the documented baseline to determine whether migration is warranted. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF02-BP01 Evaluate compute benchmarks and compute options certified by the ISVs if applicable](advperf02-bp01.md) 

 **Related documents:** 
+  [Running Ad Tech Workloads on AWS with Aerospike at Petabyte Scale](https://aws.amazon.com/blogs/industries/running-ad-tech-workloads-on-aws-with-aerospike-at-petabyte-scale/) 
+  [Boost AdTech Performance with AWS Graviton4: Aerospike I8g benchmark](https://aerospike.com/blog/aws-graviton4-adtech-performance/) 
+  [How to choose the right Amazon MSK cluster type for you](https://aws.amazon.com/blogs/big-data/how-to-choose-the-right-amazon-msk-cluster-type-for-you/) 

 **Related services:** 
+  [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) 
+  [Amazon Managed Streaming for Apache Kafka (MSK)](https://aws.amazon.com/msk/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 