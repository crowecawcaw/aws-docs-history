

# COST05-BP02 Analyze all components of the workload

 A workload has many components, and small ones add up as usage grows. Review every component, and scale review depth to potential savings. 

 **Desired outcome:** 
+  Every workload component is inventoried with its cost, usage pattern, and business context. 
+  You keep analysis effort proportional to the savings each component can yield. 
+  You understand and record the cost-to-value relationship of each component. 
+  You surface optimization opportunities consistently rather than by chance. 

 **Common anti-patterns:** 
+  Teams analyze only high-cost components and ignore the long tail of smaller ones. 
+  Component analysis ignores projected growth, so a low-cost component today becomes a cost driver later. 
+  Analysis decisions and their rationale go undocumented. 
+  Component costs are assessed without reference to the business value they support. 

 **Benefits of establishing this best practice:** 
+  Cost efficiency improves across the whole workload, not just its largest parts. 
+  Resource allocation tracks business value because every component is measured against it. 
+  Decisions to keep, replace, or change a component rely on data. 
+  Future costs become more predictable because growth is factored into the analysis. 
+  The risk of unexpected cost escalation drops. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 If you focus on only the three biggest line items, you miss savings and leave small components unwatched. Analysis costs time. A component that costs $10 a month might not justify a day of engineering to halve it. Scale each review to potential savings, and use fast, data-driven estimates for low-stakes components. 

 Include projected growth in the analysis. A service that suits an early, low-volume stage can cost more than an alternative at scale. Switching later carries migration effort you avoid by choosing for expected volume. 

 Each service prices on different dimensions such as requests, storage, throughput, or run time. Two components with similar monthly totals can respond differently to a change in load. Baseline each component's cost, usage, and pricing model as the reference point for every review. 

 Consumption-priced and serverless components need particular care because their cost scales with usage. Services such as AWS Lambda, AWS Fargate, Amazon DynamoDB on-demand, and Amazon Aurora Serverless bill per request, per unit of duration, or per unit of throughput. A component that is inexpensive at low volume can dominate the bill at scale. The same holds for consumption-priced AI services, where inference and token-based pricing make model choice and call frequency cost decisions. Treat these components like any other and baseline how their cost moves with load. The AI-focused Well-Architected lenses cover deeper analysis (for example, [Agentic AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentic-ai-lens.html)). 

 A repeatable review workflow keeps analysis consistent across teams. Make it simple enough to follow, and complete enough to cover each component's pricing model. Different teams can adapt the same workflow to their own workloads. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Build a component inventory and baseline:** Inventory every workload component, regardless of size or cost, and record its usage pattern, cost, and business impact. Apply tagging and resource naming conventions that support your analysis tooling. Capture the [pricing dimensions](https://aws.amazon.com/pricing/) of each service so the baseline reflects how each component responds to load, not just its current total. 

1.  **Define an analysis framework:** Set clear criteria for evaluating each component, such as current cost, projected growth, business criticality, and optimization potential. Use the framework to prioritize where teams spend analysis effort while keeping the approach consistent across all components. 

1.  **Set up monitoring and analysis tooling:** Configure tools that give visibility into both component cost and performance, and correlate resource usage with business outcomes. Use [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html), [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html), [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html), [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), and [Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html) for measurement. Add [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) and [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html) to alert on unexpected cost and trends. 

1.  **Run reviews on a cadence:** Align component reviews with your development and business cycles. Examine both individual component efficiency and the cost of the workload as a whole, so cross-component effects do not go unnoticed. 

1.  **Document findings and act on them:** Record each finding with a clear owner, a measurable target, and a timeline. Prioritize opportunities by potential impact against implementation effort, and track the impact of each change so you can confirm the analysis paid off. Estimate future-state costs with the [AWS Pricing Calculator](https://calculator.aws/#/) before committing to a change. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST05-BP03 Analyze the total cost of ownership of each component](cost05-bp03.md) 
+  [COST05-BP06 Perform continuous cost analysis](cost05-bp06.md) 

 **Related documents:** 
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) 
+  [AWS Pricing Calculator](https://calculator.aws/#/) 
+  [AWS Cost Optimization Hub](https://aws.amazon.com/aws-cost-management/cost-optimization-hub/) 
+  [Werner Vogels - The Frugal Architect](https://www.thefrugalarchitect.com/) 
+  [Generative AI Lens - Cost Optimization](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/) 
+  [Machine Learning Lens - Cost Optimization](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/cost-optimization.html) 
+  [Agentic AI Lens - Cost Optimization](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/cost-optimization.html) 