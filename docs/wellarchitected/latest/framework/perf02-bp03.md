

# PERF02-BP03 Configure and right-size compute resources

 Right-sizing matches the type and amount of compute to what the workload uses. Provision too much and you pay for idle capacity. Provision too little and performance degrades and users feel it. Because demand and instance options change, revisit right-sizing regularly to improve performance and cost. 

 **Desired outcome:** 
+  Your compute resources are sized from measured workload behavior, avoiding both over-provisioning and under-provisioning. 
+  You match instance family and configuration to each workload's profile rather than standardizing on one size for convenience. 
+  You review right-sizing recommendations on a regular cadence and act on them. 
+  You reassess sizing when new instance types ship or when the workload's demands shift. 

 **Common anti-patterns:** 
+  Teams ignore measured performance needs and provision resources that are too large or too small. 
+  Teams pick the largest or smallest instance available for every workload regardless of fit. 
+  Teams standardize on a single instance family to simplify management, even when other families fit better. 
+  Teams do not review right-sizing recommendations from AWS or third-party tools. 
+  Teams never re-evaluate a running workload against newer instance types. 
+  Teams certify only a handful of instance configurations, forcing every workload into a narrow set. 
+  Teams add instances to absorb high CPU load without profiling for avoidable software overhead. 

 **Benefits of establishing this best practice:** 
+  Performance improves because resources match the workload's real memory, CPU, and network profile. 
+  Cost falls because idle, over-provisioned capacity is removed. 
+  Customer experience improves when under-provisioning and its slowdowns are reduced. 
+  The workload stays efficient over time because sizing is revisited as options and demand change. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Over-provisioning wastes money on capacity that never gets used and can hide inefficiencies in the workload. Under-provisioning produces latency, timeouts, and a poor customer experience that costs more than the capacity would have. Use the instance with a CPU, memory, network, and storage profile that fits how the workload behaves under real load. 

 Workload stability changes how you right-size. A stable, long-running service gives recommendation tools enough consistent history to analyze, so review those recommendations on a cadence. An ephemeral or bursty workload gives them little to work with. Track live utilization metrics over shorter observation windows instead. For serverless functions, you size memory, and CPU scales with the memory you allocate. Choose the memory setting that balances cost against speed for your workload. 

 Recommendation engines analyze historical utilization to suggest a better fit, so their advice reflects only the period they observed. A recommendation drawn from a quiet week under-sizes a workload that spikes monthly. Feed these engines a representative window that includes your peaks, and validate the output before you apply it. 

 Two instances with the same vCPU count can perform differently. The differences come from processor architecture, clock behavior, instruction-set support, and whether the vCPUs map to physical cores or hardware threads. A workload that depends on a specific instruction set, or that scales poorly across hardware threads, needs an instance family chosen for those properties. Certifying only a small set of instance types forces workloads onto configurations that do not fit and blocks adoption of newer, better-value generations. 

 Before you increase instance size in response to high CPU utilization, check whether the load reflects the need or avoidable software overhead. Cryptographic libraries are a common source. A default configuration can perform operations, such as asymmetric signing, that cost more CPU than the encryption itself. Profile CPU-bound hot paths, and if a default looks unnecessary, review it with your security team before you change it. Never weaken a protection to save CPU without that review. 

 On AWS, [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) and [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) analyze historical usage and recommend right-sizing changes. [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) supplies the live utilization data for workloads without enough history for recommendations. For containers, [Karpenter](https://aws.amazon.com/blogs/containers/optimizing-your-kubernetes-compute-costs-with-karpenter-consolidation/) consolidates and right-sizes Kubernetes capacity automatically. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Choose an instance type that fits the workload:** Select the instance family and size whose CPU, memory, and network profile matches your workload rather than defaulting to a familiar type. See [how to choose an EC2 instance type](https://repost.aws/knowledge-center/ec2-instance-choose-type-for-workload), and for fleets use [attribute-based instance type selection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html) so capacity is described by requirements instead of a fixed list. 

1.  **Analyze workload performance characteristics:** Examine how the workload uses memory, network, and CPU, and relate those patterns to candidate instance profiles. Use this analysis to shortlist resources that match the workload's goals. 

1.  **Monitor resource usage:** Track utilization with [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) so sizing decisions rest on observed behavior over a representative period, including peaks. 

1.  **Select the right configuration for the workload type:** For ephemeral workloads, watch live metrics such as CPUUtilization to spot under- or over-utilization. For stable workloads, review [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) and [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) recommendations on a cadence. For functions, use [AWS Lambda Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html) to find the memory setting that balances cost and speed. 

1.  **Test changes in a non-production environment:** Apply the sizing change against representative load in a non-production environment and confirm the result before promoting it to production. 

1.  **Understand CPU architecture differences:** Account for hyper-threading, instruction-set support, and other processor optimizations when comparing instances, so you match architecture to workload rather than comparing vCPU counts alone. 

1.  **Reassess as options change:** Compare running workloads against new instance generations as they ship, and re-size when a newer type offers a better fit. 

1.  **Profile hot paths for avoidable CPU overhead:** Before you enlarge or add instances, profile CPU-bound hot paths for overhead you can remove, such as default cryptographic operations. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF02-BP01 Select the best compute options for your workload](perf02-bp01.md) 
+  [PERF02-BP02 Collect compute-related metrics](perf02-bp02.md) 
+  [PERF02-BP04 Scale your compute resources dynamically](perf02-bp04.md) 
+  [PERF02-BP05 Use optimized hardware-based compute accelerators](perf02-bp05.md) 

 **Related documents:** 
+  [Cloud compute with AWS](https://aws.amazon.com/products/compute/) 
+  [Amazon EC2 instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) 
+  [Amazon ECS container instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-capacity.html) 
+  [Amazon EKS worker nodes](https://docs.aws.amazon.com/eks/latest/userguide/worker.html) 
+  [AWS Lambda function configuration best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html) 
+  [Optimize Kubernetes compute costs with Karpenter consolidation](https://aws.amazon.com/blogs/containers/optimizing-your-kubernetes-compute-costs-with-karpenter-consolidation/) 

 **Related examples:** 
+  [AWS Compute Optimizer demo code](https://github.com/awslabs/ec2-spot-labs/tree/master/aws-compute-optimizer) 
+  [Amazon EKS workshop](https://www.eksworkshop.com/) 