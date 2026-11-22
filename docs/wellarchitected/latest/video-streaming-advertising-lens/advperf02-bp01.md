

# ADVPERF02-BP01 Evaluate compute benchmarks and compute options certified by the ISVs if applicable

 Evaluate ISV compatibility on AWS, and choose resources based on published benchmarks. For advertising software such as Aerospike and Databricks, suboptimal instances affect bid latency and analytics freshness. 

 **Desired outcome:** 
+  Your team selects ISV solutions that are proven to run effectively on AWS and chooses the right [Amazon EC2](https://aws.amazon.com/ec2/) instance types based on published performance benchmarks rather than assumptions. 
+  Workload placement decisions for high-volume advertising use cases (Aerospike for user profiles, Databricks for attribution modeling) are grounded in evidence, not vendor defaults. 
+  Benchmark data is refreshed when new AWS instance generations are released to capture potential performance improvements. 

 **Common anti-patterns:** 
+  Deploying ISV software on AWS using the same instance types and configurations carried over from on-premises environments, without validating whether those choices are optimal for the AWS infrastructure the ISV runs on. 
+  Selecting EC2 instance families based on general familiarity rather than ISV-published benchmark results. 

 **Benefits of establishing this best practice:** 
+  Using ISV-validated configurations and AWS benchmark data reduces the risk of performance shortfalls after deployment. 
+  For high-volume advertising workloads where latency and throughput directly affect bid win rates and analytics freshness, selecting the right instance type from the start avoids expensive migration cycles later. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Advertising platforms depend on two categories of ISV software that have particularly strong instance-type sensitivity: high-performance NoSQL databases (Aerospike) for the real-time bid path, and large-scale analytics platforms (Databricks) for audience intelligence and attribution modeling. 

 Ad tech uses Aerospike for user profile lookups, frequency capping, and real-time audience segmentation. Its architecture is optimized for high-throughput, low-latency access to NVMe-backed local storage, which fits EC2 Storage Optimized instances (I series). Aerospike publishes benchmark comparisons across Intel and AWS Graviton instance types on AWS, covering throughput, latency percentiles, and cost-per-operation at petabyte scale. The I-series instances provide locally attached NVMe storage that avoids the network round-trip of EBS-backed storage, reducing p99 read latency for user profile lookups during bid evaluation. 

 Ad tech uses Databricks for advertising analytics (attribution modeling, audience intelligence, and campaign performance analysis), where data volumes are large and requirements change rapidly. Databricks publishes performance comparisons across instance types for typical Spark workload patterns. Graviton-based instances (M7g, C7g, and R7g) show performance improvements for Databricks workloads because of better price-performance on compute-intensive operations. 

 ISV-published benchmarks use representative workload patterns, not your specific data model, access patterns, and concurrency profile. After identifying the top candidate instance types from ISV documentation, run a targeted load test against a representative sample of your actual advertising workload (a bid evaluation run for Aerospike, an attribution modeling job for Databricks) before committing to a production configuration. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Review Aerospike's published AWS benchmark results:** Before deploying Aerospike for user profile storage, frequency capping, or audience segmentation, review Aerospike's benchmark documentation comparing EC2 instance types (including I-series Storage Optimized and Graviton variants). Identify the top two or three candidate instance types for your workload profile (read-heavy, write-heavy, or mixed). 

1.  **Review Databricks' published AWS benchmark results:** For advertising analytics and ML workloads on Databricks, consult Databricks' benchmark data comparing Intel and Graviton instance performance for query and processing patterns similar to your use case (streaming ingestion, batch attribution, audience segmentation). Identify candidate cluster configurations. 

1.  **Run targeted benchmarks with your actual advertising workload:** For the top candidate instance types from step 1 and 2, run performance tests using traffic patterns representative of your actual workload, including peak bid volumes for Aerospike and representative Spark job sizes for Databricks. Measure latency percentiles (p50, p95, and p99), throughput, and cost-per-operation. Select the instance type that delivers the best cost-performance ratio for your specific requirements. 

1.  **Document instance type selection rationale:** Record the benchmark results, the evaluation criteria, and the final selection decision. Include the date of the benchmark so future reviews can identify when a re-evaluation is due. This documentation is particularly valuable when new EC2 instance generations are released and the original decision may no longer be optimal. 

1.  **Schedule a benchmark refresh when new instance generations launch:** When AWS releases a new instance generation (for example, I4i compared to I3en for Storage Optimized, or M8g compared to M7g for Graviton-based), re-run your benchmark against the new generation to determine whether migration is warranted. New generations often provide meaningfully better price-performance that justifies migration for workloads at advertising scale. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF02-BP04 Use a specialized instance family and features](advperf02-bp04.md) 
+  [ADVPERF02-BP05 Evaluate ARM architecture for performance considerations](advperf02-bp05.md) 

 **Related documents:** 
+  [Running Ad Tech Workloads on AWS with Aerospike at Petabyte Scale](https://aws.amazon.com/blogs/industries/running-ad-tech-workloads-on-aws-with-aerospike-at-petabyte-scale/) 
+  [Aerospike database comparisons and performance benchmarks](https://aerospike.com/benchmarks/) 

 **Related services:** 
+  [Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types/) 
+  [Amazon EC2 Storage Optimized instances](https://aws.amazon.com/ec2/instance-types/#Storage_Optimized) 