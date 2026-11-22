

# ADVCOST02-BP01 Use ARM processors for faster and more cost-effective bidder nodes

 For RTB bidder nodes, ARM-based instances cost less than comparable x86 instances and deliver up to 40% better price-performance for supported workloads. 

 **Desired outcome:** 
+  You have assessed your RTB workloads for Graviton compatibility and migrated eligible workloads to ARM-based instances, with measurable cost savings and performance improvements. 
+  Graviton instances are the default for compatible services in your infrastructure as code templates. 

 **Common anti-patterns:** 
+  Defaulting to x86 instance types out of habit without evaluating ARM-based alternatives. 
+  Assuming application code or dependencies are incompatible with ARM without performing actual compatibility testing. 
+  Migrating all workloads to Graviton at once instead of using a phased approach, which increases the risk of unforeseen issues. 

 **Benefits of establishing this best practice:** 
+  AWS Graviton instances deliver up to 40% better price-performance over comparable x86 instances for supported workloads. 
+  Reduced cost per bid processed directly improves campaign profitability. 
+  Graviton instances are available across multiple instance families (C, M, R, and T), providing flexibility for diverse RTB workload profiles. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 AWS Graviton processors use an ARM64 instruction set, which differs from the x86-64 architecture most bidding stacks default to. Compiled binaries, environment-specific libraries, and architecture-specific agents all need ARM64-compatible builds. Interpreted languages such as Python and Node.js and JVM-based applications typically run without modification on Graviton, but C/C\+\+ extensions, environment-specific SDKs for ad fraud detection or identity resolution, and observability agents each need explicit verification. Incompatibilities are rare, but an undetected one in production can cause data corruption in bid logic or hard crashes under load. 

 Price-performance gains from Graviton vary by workload profile. CPU-bound bid evaluation logic and in-memory auction calculations gain the most because Graviton's single-threaded performance and cache hierarchy favor tight computational loops. I/O-bound workloads that spend most cycles waiting on network or database responses see smaller gains because the processor is not the bottleneck. Benchmark your specific workload before migrating to confirm the gains apply. 

 Migrate in phases to limit risk. Run Graviton instances alongside existing x86 instances in the same Auto Scaling group or ECS cluster, then compare cost per bid and latency distributions between them using real production traffic. [Mixed instance policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/mixed-instances-groups.html) in Auto Scaling groups support this pattern. Without this validation step, a subtle performance regression can stay invisible under synthetic load and occur only at peak QPS. 

 Coordinate the Graviton migration with your purchasing strategy. Savings Plans and Reserved Instances are instance-family specific, so moving from c6i to c7g means existing x86 commitments no longer apply. Do not purchase new Graviton commitments until the migration is validated and stable. Otherwise, you either lose coverage during the transition or lock into commitments on an unvalidated architecture. 

 Configure your build pipelines for multi-architecture support, producing ARM64 and x86-64 artifacts in parallel, so rollback stays possible without a rebuild cycle. [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) identifies instances where Graviton provides better price-performance, but its recommendations are based on utilization patterns, not application correctness. Treat its output as a list of candidates to validate before migration. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Inventory current instance types and identify Graviton migration candidates:** Prioritize containerized services, JVM, Python, or Node.js applications, and stateless bid evaluation components. Use AWS Compute Optimizer to identify workloads where Graviton provides better price-performance. 

1.  **Validate compatibility and build on Graviton:** Check that all libraries, agents, and third-party tools (ad fraud detection SDKs and identity resolution libraries) provide ARM64 builds. Build and test on Graviton in a non-production environment. Run performance benchmarks comparing throughput, p99 bid response latency, and cost against your current x86 baseline. 

1.  **Deploy Graviton alongside existing x86 using canary or blue/green:** Route a small percentage of bid traffic (5–10%) to Graviton-based instances and monitor for correctness and performance parity over 24–48 hours. Compare cost per bid processed between Graviton and x86 using AWS Cost Explorer with instance type filters. 

1.  **Update infrastructure as code to default to Graviton for compatible services:** Once validated, update ECS task definitions, EKS node group configurations, and Auto Scaling launch templates to use Graviton instance types as the default. This captures savings automatically for all future scaling events. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Use Graviton instances and containers](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-graviton.html) 
+  [How DeviceAtlas optimized Real-Time Advertising Price/Performance on AWS Graviton3](https://aws.amazon.com/blogs/industries/how-deviceatlas-optimized-real-time-advertising-price-performance-on-aws-graviton3/) 
+  [Using Porting Advisor for Graviton](https://github.com/aws/porting-advisor-for-graviton) 
+  [AWS Unveils Next Generation AWS-Designed Chips](https://press.aboutamazon.com/2023/11/aws-unveils-next-generation-aws-designed-chips) 

 **Related services:** 
+  [Amazon EC2 Graviton instances](https://aws.amazon.com/ec2/graviton/) 
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) 