

# ADVSUS01-BP01 Run advertising fleets on multiple chipsets, including ARM, to lower energy intensity

 Advertising workloads such as real-time bidding and creative rendering run on large, elastic, interruption-tolerant fleets. With multi-architecture design, your workload absorbs spare capacity that is already provisioned and powered, instead of triggering new dedicated capacity at a peak. It also runs on the most energy-efficient processor it has a validated build for, where AWS reports that Graviton-based instances use up to 60% less energy than comparable EC2 instances for the same performance. 

 **Desired outcome:** 
+  Your advertising workloads run on AMD and Intel x86 instances interchangeably and, where a validated build exists, on ARM-based AWS Graviton instances, so the workload absorbs spare, already-running capacity from whichever pool has it rather than provisioning new dedicated capacity at a peak. 
+  Interruption-tolerant and steady-state ad workloads run on AWS Graviton wherever a multi-architecture build is available, capturing its substantially lower energy per unit of work as the default efficient choice. 
+  Instance selection within an architecture is a configuration choice, so the workload adopts more efficient same-architecture generations without a code change, while adding a new architecture (x86 to ARM) is handled through multi-architecture container images validated in the build pipeline. 
+  Spot capacity diversification across AMD, Intel, and Graviton pools keeps interruption-tolerant ad workloads on shared elastic capacity and reduces reliance on persistent reserved capacity. 

 **Common anti-patterns:** 
+  Pinning bid-processing and ad-serving Auto Scaling groups to a single instance family, so a price spike or capacity shortage in that family forces a fall back to costlier, less efficient on-demand capacity during an auction-traffic peak. 
+  Hard-coding processor-specific instance types in ad-server deployment manifests, so adopting a cheaper equivalent family requires a code change rather than a configuration change. 
+  Assuming an interpreted bidder or creative-rendering service is processor-bound and skipping validation, then discovering a platform-specific dependency breaks only after a campaign launch shifts capacity onto the untested family. 
+  Restricting the eligible fleet to x86 only and never validating a Graviton build, forgoing the single largest energy-per-unit-of-work reduction available for interruption-tolerant ad workloads. 
+  Treating Spot interruptions to real-time bidding fleets as acceptable loss without diversifying pools, so reclaimed capacity drops in-flight auctions and wastes the compute already spent on those bid requests. 

 **Benefits of establishing this best practice:** 
+  Higher utilization of already-provisioned shared capacity, because interruption-tolerant ad workloads can run on spare capacity in either pool instead of triggering new dedicated capacity at a traffic peak. 
+  Lower energy intensity per unit of work as the workload adopts more efficient processor families, and a step-change reduction where it runs on AWS Graviton, which uses up to 60% less energy than comparable EC2 instances for the same performance. 
+  Reduced reliance on persistent reserved capacity for interruption-tolerant ad workloads, which lowers idle, powered capacity. 
+  Higher resilience for latency-sensitive auction traffic, since diversified pools reduce the chance that a single capacity shortage interrupts the fleet and wastes the compute already spent on in-flight bid requests. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Real-time bidding, header-bidding orchestration, and creative rendering run on large fleets where individual node loss is tolerable and capacity scales horizontally. This profile makes shared, elastic capacity such as Spot a good fit, as the workload can run on capacity that already exists and is already powered. When a fleet can only run on one processor family, it can't absorb spare capacity in another family, so a capacity shortage during an auction-traffic peak pushes the workload onto dedicated, persistent capacity instead. Breadth of eligible instance types raises the share of work that runs on already-provisioned capacity and on the more energy-efficient processor generations as AWS introduces them. 

 A chipset-agnostic design treats processor family as a runtime selection driven by configuration. Most ad-platform services are agnostic at the binary level, because interpreted and JIT runtimes such as Java, Python, Node.js, and .NET run across equivalent x86 families without change. Validation effort is the main trade-off. Compiled extensions in bidders or media-processing libraries can carry processor-specific assumptions that appear only under production load, so each family you add widens the test matrix. 

 Adding ARM (AWS Graviton) differs from diversifying between AMD and Intel. AMD and Intel share the x86 instruction set, so a workload validated on one usually runs on the other unmodified. Graviton uses the ARM64 instruction set, so it needs build validation. Interpreted and JIT services (Java, Python, Node.js, and .NET) typically run as-is or with minor dependency updates. Compiled services (C, C\+\+, Go) require recompilation against an ARM64 target and binary validation. Adding Graviton support means multi-architecture container images and a separate validation pass. Graviton uses up to 60% less energy than comparable EC2 instances for the same performance, which makes it the highest-impact efficiency gain in this best practice. For the performance and cost dimensions of the same decision, including advertising-specific benchmarks and a canary migration path, see [ADVPERF02-BP05 Evaluate ARM architecture for performance considerations](advperf02-bp05.md). For a workload that clears that validation, Graviton is the default energy-efficient target. 

 Breadth of eligible instance types improves sustainability because over-provisioning and under-provisioning have unequal costs. Over-provisioning does not always trip al arms, since surplus instances draw power and incur cost but nothing breaks, so the waste often goes unnoticed. Under-provisioning is noisy and, in real-time bidding, expensive, because a bidder that can't answer inside the auction's response window loses the impression outright. That asymmetry biases advertising teams toward carrying excess dedicated capacity, and a fleet eligible for several architectures counters it by meeting a peak from spare capacity that is already running instead of from headroom held in reserve. 

 Decide which workloads justify that validation. The payoff is highest for the largest, most interruption-tolerant fleets, where the gain in eligible capacity and the energy reduction from Graviton are both large. The payoff is lowest for small services where the added diversity doesn't justify the testing. Assign ownership for the instance-architecture configuration so that the eligible list stays current as new efficient generations ship. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Validate x86 agnosticism for your advertising workloads:** Run your test suite on both AMD (m6a, c6a) and Intel (m6i, c6i) instances. For compiled applications (C, C\+\+, Go), compile without chipset-specific flags (-march=native). For interpreted/JIT languages (Java, Python, and Node.js), no changes are typically required. 

1.  **Build for ARM64 alongside x86:** Build a multi-architecture container image (for example with docker buildx targeting linux/amd64,linux/arm64) so the same service can schedule onto x86 or Graviton nodes. Recompile compiled services against an ARM64 target and run the [AWS Porting Advisor for Graviton](https://github.com/aws/porting-advisor-for-graviton) to identify dependencies lacking ARM64 support before functional and load testing. Interpreted and JIT services usually need only ARM64-compatible base images and dependency updates. 

1.  **Externalize instance selection into configuration across architectures:** Replace hardcoded instance-type references in Auto Scaling groups, EKS node groups, and ECS task definitions with lists that include AMD, Intel, and validated Graviton equivalents. For EC2 Spot fleets, list equivalents across architectures (for example, c7g.4xlarge alongside c6i.4xlarge and c6a.4xlarge) so EC2 can draw from whichever pool has available capacity at launch. 

1.  **Configure EC2 Spot Instance diversification across architectures:** Set up the Spot fleet or Auto Scaling group with pools that include Graviton, AMD, and Intel options across multiple sizes, and select the capacity-optimized allocation strategy. This strategy places instances in the pools with the most spare capacity, which raises the share of work running on already-provisioned capacity and reduces interruptions to latency-sensitive auction traffic. Where the Graviton build is validated, weight allocation toward it to capture its lower energy per unit of work. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS01-BP03 Reduce CPU time per bid in agent containers to lower fleet energy intensity](advsus01-bp03.md) 
+  [ADVPERF02-BP05 Evaluate ARM architecture for performance considerations](advperf02-bp05.md) 
+  [ADVSUS04-BP02 Match model capability to task complexity to reduce agent fleet energy use](advsus04-bp02.md) 

 **Related documents:** 
+  [EC2 Fleet and Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Fleets.html) 
+  [AWS Graviton sustainability](https://aws.amazon.com/ec2/graviton/graviton-sustainability/) 
+  [Using Porting Advisor for Graviton](https://github.com/aws/porting-advisor-for-graviton) 

 **Related services:** 
+  [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/) 
+  [Amazon EC2 with AWS Graviton processors](https://aws.amazon.com/ec2/graviton/) 