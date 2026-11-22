

# ADVPERF02-BP05 Evaluate ARM architecture for performance considerations

 To address the low-latency and high-throughput needs of advertising workloads, evaluate ARM-based processors for improved performance and cost optimization. In programmatic advertising, the price-performance advantage compounds differently than in most industries. Cost scales with bid volume, and latency determines auction win rates. Advertising ISVs have published ad tech-specific benchmarks that validate the gains on advertising workload patterns. 

 **Desired outcome:** 
+  Your advertising workloads run on AWS Graviton-based instances where benchmarks confirm a performance or cost advantage over equivalent x86 instances. 
+  Graviton adoption is deliberate and validated, not wholesale, but targeted at the components where ARM architecture delivers measurable gains in bid response latency, auction throughput, or cost per bid. 
+  The cost-per-bid metric improves measurably after Graviton migration, reflecting the compounding effect of per-instance savings across billions of daily auction requests. 
+  A phased migration approach (canary deployment alongside existing x86 instances) validates Graviton compatibility and performance before full rollout. 

 **Common anti-patterns:** 
+  Defaulting to x86 instances across all advertising workload components without evaluating Graviton as an alternative. 
+  Migrating to Graviton without first validating application compatibility and benchmarking workload-specific performance, which produces regressions that force rollback under production conditions. 
+  Treating chipset compatibility as a binary decision rather than evaluating Graviton component by component based on benchmark results. 

 **Benefits of establishing this best practice:** 
+  In programmatic advertising, compute cost scales directly with bid volume. At 500,000 bid requests per second, even a 20% Graviton price-performance gain compounds into material annual infrastructure savings that would not be achievable at lower request volumes. 
+  CPU cycles recovered by Graviton's instruction throughput directly widen the latency margin available for auction logic within the 100 ms RTB window, translating efficiency gains into higher bid win rates, a revenue outcome unique to advertising's latency-competitive economics. 
+  Key advertising ISVs have published Graviton benchmarks specifically for ad tech workloads: Aerospike demonstrated 6x throughput improvement on Graviton4-based I8g instances for ad tech use cases. This industry-specific validation goes beyond generic Graviton benchmarks. 
+  Graviton's ARM Neon SIMD instructions improve parallel processing throughput for video encoding and transcoding of ad creatives at scale. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Graviton's price-performance advantage matters differently in advertising than in most other industries because of compute cost and latency. Advertising compute cost scales linearly with bid volume. A system processing 500,000 bid requests per second runs that compute 24 hours a day, across every auction. At that scale, a 20–40% Graviton price-performance improvement compounds annually across the entire bid fleet. 

 Every microsecond of CPU time recovered by Graviton's instruction throughput on the bid evaluation path widens the margin available for auction logic (audience lookups, targeting evaluation, bid price calculation) within the 100 ms RTB window. Faster CPU within the same window means more auction logic executes before the deadline, improving bid quality and win rates. 

 Advertising ISVs have validated Graviton specifically for ad tech workloads, which distinguishes this from generic compute benchmarking. Aerospike published benchmark results for Graviton4-based I8g instances showing 6x throughput improvement for ad tech workloads. These measurements cover advertising-specific access patterns (user profile lookups, frequency cap checks, and device identification). 

 Stateless services (bid request handlers, audience enrichment, and creative serving) show the strongest Graviton gains. These workloads spend most CPU time on compute operations such as JSON deserialization, string processing, and network I/O handling. The ARM Neoverse core's instruction throughput advantage is most pronounced for this pattern. Video encoding and transcoding of ad creative assets benefit from Graviton's ARM Neon SIMD instructions for parallel media processing. Data processing pipelines for audience analytics and attribution modeling benefit from Graviton's cache utilization and memory access optimizations on large dataset iterations. 

 Most x86 workloads run without modification on ARM64, so the migration path is lower-risk than most infrastructure changes. Java, Python, Node.js, and .NET Core applications typically run as-is or with minor dependency updates. Compiled languages (C, C\+\+, Go) require recompilation against an ARM64 target. The AWS Porting Advisor for Graviton identifies dependencies that need attention before migration. Graviton migration requires binary validation because it uses a different instruction set. This differs from AMD and Intel chipset agnosticism, which is x86-only and works for any compatible application. Teams that have diversified between AMD and Intel for Spot cost optimization still need a separate validation pass to add Graviton to the fleet. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Validate workload compatibility on Graviton before migrating:** Run your full test suite on a Graviton instance in a non-production environment. Check that all libraries, agents, and third-party tools provide ARM64 builds. Use the AWS Porting Advisor for Graviton to identify dependencies that require updates. For compiled languages, recompile against an ARM64 target and validate binary correctness before performance testing. 

1.  **Benchmark your workload on Graviton instances against advertising-specific metrics:** Run performance benchmarks comparing your target Graviton instance (C9g/C8g for compute-optimized bid evaluation, I8g for NVMe-dependent user profile stores, M8g for general-purpose audience processing) against your current x86 instance using realistic advertising traffic patterns and request volumes. Measure latency percentiles (p50, p95, and p99), throughput (bid requests per second), CPU utilization at equivalent load levels, and (critically) cost per bid request. The cost-per-bid metric captures the compounding effect of per-instance savings at advertising scale in a way that generic cost-per-hour comparisons don't. 

1.  **Deploy Graviton instances alongside existing x86 instances using a canary strategy:** Route a small percentage of traffic (10–20%) to Graviton-based instances while keeping the majority on x86. Monitor for functional regressions, latency differences, and error rates over 24–48 hours. Gradually increase Graviton traffic share as confidence in correctness and performance grows. This approach limits the scope of impact if unexpected issues arise. 

1.  **Validate cost savings using [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/):** After full Graviton migration, compare the cost per bid request (or cost per transaction) between Graviton and x86 instances over a representative time period using Cost Explorer instance type filters. Update your infrastructure cost models and document the realized savings to build the business case for further Graviton adoption across additional workload components. 

1.  **Update infrastructure as code to default to Graviton for compatible services:** For services where Graviton migration has been validated, update EKS node group definitions, ECS task definitions, and EC2 Auto Scaling group configurations to specify Graviton instance types as the default. This means new deployments and scaling events use Graviton instances without requiring manual selection, capturing cost savings automatically for the lifetime of the service. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF02-BP01 Evaluate compute benchmarks and compute options certified by the ISVs if applicable](advperf02-bp01.md) 
+  [ADVPERF06-BP01 Adopt a chipset-agnostic workload design for best availability of cloud resources and cost](advperf06-bp01.md) 

 **Related documents:** 
+  [Considerations when transitioning workloads to AWS Graviton based Amazon EC2 instances](https://aws.amazon.com/ec2/graviton/getting-started/) 
+  [Using Porting Advisor for Graviton](https://github.com/aws/porting-advisor-for-graviton) 
+  [How DeviceAtlas optimized Real-Time Advertising Price/Performance on AWS Graviton3](https://aws.amazon.com/blogs/industries/how-deviceatlas-optimized-real-time-advertising-price-performance-on-aws-graviton3/) 
+  [Boost AdTech Performance with AWS Graviton4: Aerospike I8g benchmark](https://aerospike.com/blog/aws-graviton4-adtech-performance/) 

 **Related services:** 
+  [Amazon EC2 Graviton instances](https://aws.amazon.com/ec2/graviton/) 
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) 