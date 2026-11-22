

# ADVPERF06-BP01 Adopt a chipset-agnostic workload design for best availability of cloud resources and cost

 Implement an x86 chipset-agnostic design for advertising workloads to optimize Spot Instance compute costs. Spot Instance pricing for AMD and Intel x86 instances fluctuates independently based on capacity supply and demand. Workloads that can run on either chipset consistently select the lower-cost option, which maximizes Spot savings without sacrificing instance availability. 

 **Desired outcome:** 
+  Your advertising workloads run on either AMD or Intel x86 EC2 instances interchangeably, with instance family selection driven by configuration rather than hardcoded dependencies. 
+  With this flexibility, you can consistently choose the lowest-cost Spot Instance option available at any given time, regardless of which chipset has the pricing advantage. 

 **Common anti-patterns:** 
+  Hard-coding a specific x86 chipset (AMD or Intel) into your instance selection configuration, locking your workload into a single option and missing cost savings when pricing shifts. 
+  Treating chipset compatibility as a fixed architectural constraint rather than a configuration choice, which then requires engineering effort to switch chipsets when pricing changes. 

 **Benefits of establishing this best practice:** 
+  Spot Instance pricing for AMD and Intel x86 instances fluctuates independently based on capacity supply and demand in each Availability Zone. Workloads that can run on either chipset can consistently select the lower-cost option, which maximizes Spot savings over time. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Most x86 workloads are chipset-agnostic at the binary level: Java, Python, Node.js, and .NET Core applications run identically on AMD (for example, m6a and c6a) and Intel (for example, m6i and c6i) instances. The source of chipset lock-in is usually configuration, such as launch templates, EKS node group definitions, or ECS task definitions that specify a single instance type rather than a list of equivalent options. 

 Instead of specifying a single instance type (for example, c6i.4xlarge), specify both AMD and Intel equivalents at the same size (for example, c6i.4xlarge and c6a.4xlarge). When requesting Spot capacity, EC2 selects from the list based on current availability and pricing, favoring whichever chipset has lower cost. 

 Graviton (ARM) is a separate migration that requires binary validation because ARM uses a different instruction set from x86. Chipset-agnostic design for AMD or Intel does not require any binary validation beyond confirming that your application runs correctly on x86 (which it already does if it was previously running). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Validate x86 chipset agnosticism for your workload:** Run your test suite on both an AMD (m6a or c6a) and Intel (m6i or c6i) instance of the same size to confirm functional equivalence. For compiled applications (C, C\+\+, Go), recompile without chipset-specific optimization flags (-march=native) to produce portable x86-64 binaries. For interpreted or JIT languages (Java, Python, and Node.js), no changes are required. These run identically on AMD and Intel x86. 

1.  **Externalize instance type selection into configuration:** Replace any hardcoded AMD or Intel instance type references in your launch templates, Auto Scaling group configurations, or EKS node group definitions with configuration-driven instance type lists. For EC2 Spot fleets and Auto Scaling groups, specify multiple instance types (for example, c6i.4xlarge paired with c6a.4xlarge) at equivalent sizes so that EC2 can select the lowest-cost available option at launch time. 

1.  **Use EC2 Spot Instance diversification across both chipsets:** Configure your Spot fleet or Auto Scaling group with a diversified instance type pool that includes equivalent AMD and Intel options across multiple sizes (for example, c6i.2xlarge, c6a.2xlarge, c6i.4xlarge, c6a.4xlarge). Larger pools provide more Spot capacity options and reduce interruption risk. EC2's Spot pricing algorithm allocates from the pool based on current capacity pricing. 

1.  **Monitor Spot savings and chipset distribution:** Use [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) with instance type and purchase option filters to track the cost savings from Spot compared to On-Demand pricing. Monitor the distribution of AMD compared to Intel launches over time to confirm that the diversification pool is being utilized. If one chipset is consistently selected, verify that the equivalent instances from the other chipset are correctly included in the launch template. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF02-BP05 Evaluate ARM architecture for performance considerations](advperf02-bp05.md) 

 **Related documents:** 
+  [EC2 Fleet and Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet.html) 

 **Related services:** 
+  [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/) 