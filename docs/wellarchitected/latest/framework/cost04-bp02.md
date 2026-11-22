

# COST04-BP02 Perform data transfer modeling

 Data transfer is a significant part of a workload's cost. What you pay depends on where data moves, how often, and how those patterns change as the workload grows. Model data transfer during design to compare architectural options on cost alongside performance and resilience. 

 **Desired outcome:** 
+  You have documented the business reason for each data transfer flow in your workload. 
+  Your cost model shows how data transfer charges change as the workload scales and as usage patterns shift. 
+  You can compare architectural options using modeled transfer cost, not current spend alone. 

 **Common anti-patterns:** 
+  Teams model data transfer from current usage alone, without accounting for growth or seasonal variation. 
+  Cost estimates omit data transfer entirely and cover only compute and storage. 
+  Flows are modeled without recording the business outcome each one serves, so no flow can be questioned or removed. 
+  Models ignore tiered pricing, so projected cost at scale is inaccurate. 

 **Benefits of establishing this best practice:** 
+  Architectural decisions account for data transfer cost early, when changing the design is inexpensive. 
+  Cost projections stay accurate as the workload scales because the model reflects tiered pricing and growth. 
+  Teams can identify and question expensive flows because each flow is tied to a business outcome. 
+  Balancing cost against performance and resilience becomes a data-driven decision. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Data transfer cost is a function of three things: the volume of data, the path it takes, and the rate that path charges. Three paths dominate most bills. Traffic within a Region that crosses Availability Zones, traffic between Regions, and traffic to the internet each carry their own per-gigabyte rate. Estimate volume on each path separately. A change that looks minor, such as moving a component to another Availability Zone for redundancy, can shift a large volume onto a charged path. 

 Record the business reason for each flow. Data crosses Availability Zones for redundancy, crosses Regions for disaster recovery, and moves between components to decouple them. Each flow is a deliberate trade-off of cost against resilience, performance, or maintainability. Without a recorded business reason, you cannot judge whether a flow's cost is justified or whether a cheaper pattern would meet the same requirement. 

 The characteristics of the data shape both cost and architecture. Volume and frequency drive the charge directly. Sensitivity and residency requirements constrain where data can travel and can force it onto more expensive paths. Record these characteristics for each flow, because a residency rule that keeps data in one Region narrows your options. 

 A model built only on today's traffic misleads you the moment the workload grows. Usage-based charges scale with demand, and some transfer services use tiered pricing where the per-gigabyte rate drops as volume rises. Estimate cost across a range of usage levels. Where the architecture is uncertain, run a proof of concept and simulate traffic to measure real transfer volumes. Tag workload resources so you can attribute measured transfer to specific components and refine the model as data accumulates. 

 To measure current transfer, [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), [AWS Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html), and [VPC Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) show which components communicate and over which paths. To project cost, the [AWS Pricing Calculator](https://calculator.aws/) estimates future charges, and the [AWS Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/cur-data-transfers-charges.html) and AWS Cost Explorer show what existing flows cost today. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Tag resources to attribute transfer cost:** [Tag your workload resources](https://aws-samples.github.io/cloud-operations-best-practices/docs/guides/application-operations/#establishing-the-foundation), including individual components or microservices, so measured data transfer maps to the parts of the workload that generate it. Finer tagging granularity produces a more accurate model. 

1.  **Identify each data transfer flow and its business outcome:** For every flow, record the business reason it exists, such as decoupling components, replicating across Availability Zones, or copying data between Regions for disaster recovery. A flow without a stated outcome is a candidate for removal. 

1.  **Classify the source and destination of each flow:** Determine which of the three charged path types applies: within Region across Availability Zones, between Regions, or out to the internet. The path determines the rate, so this classification drives the estimate. 

1.  **Capture data characteristics and constraints:** For each flow, record the data type, volume, transfer frequency, sensitivity, and any residency restrictions. Note how volume is expected to change or scale over time. 

1.  **Measure current data transfer:** Use [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), [AWS Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html), and [VPC Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) to confirm which flows exist and how much data each one moves. 

1.  **Estimate cost across a range of usage levels:** Use the [AWS Pricing Calculator](https://calculator.aws/) to project future charges and the [AWS Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/cur-data-transfers-charges.html) or [Cloud Intelligence Dashboards](https://cid.workshops.aws.dev/demo?dashboard=cudos) to establish current costs. Account for tiered pricing, and refine the estimate with a proof of concept that simulates traffic at expected scale. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST04-BP01 Define network and data transfer infrastructure costs](cost04-bp01.md) 
+  [COST04-BP03 Optimize services to reduce data transfer costs](cost04-bp03.md) 
+  [COST06-BP01 Perform cost modeling](cost06-bp01.md) 
+  [COST07-BP01 Perform pricing model analysis](cost07-bp01.md) 

 **Related documents:** 
+  [Data transfer costs in the AWS Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/cur-data-transfers-charges.html) 
+  [Logging IP traffic using VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) 
+  [What is AWS Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html) 
+  [What is VPC Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) 

 **Related examples:** 
+  [The authenticated AWS Pricing Calculator is now generally available](https://aws.amazon.com/blogs/aws-cloud-financial-management/the-authenticated-aws-pricing-calculator-is-now-generally-available/) 
+  [Overview of Data Transfer Costs for Common Architectures](https://aws.amazon.com/blogs/architecture/overview-of-data-transfer-costs-for-common-architectures/) 
+  [DataTransfer Cost Analysis Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/datatransfer-dashboard.html) 

 **Related tools:** 
+  [AWS Pricing Calculator](https://calculator.aws/) 