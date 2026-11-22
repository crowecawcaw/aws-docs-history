

# SUS01-BP01 Understand your resource usage efficiency

 *Resource usage efficiency* (RUE) provides an essential baseline for understanding your workload's resource intensity (which links to Scope 1, 2, and 3 emissions) by helping you calculate an efficiency metric for your workload. RUE is calculated by dividing the core resource provisioned metric (which could be volume of storage or normalized instance hours) by the amount of work completed (measured by a business metric or customer outcome). Track RUE over time to establish clear baselines, set improvement targets, and validate the effectiveness of your sustainability initiatives and optimization efforts. 

 **Desired outcome:** 
+  You define resource usage efficiency metrics that represent the resources provisioned per unit of business value, so you can track and compare efficiency improvements consistently over time. 
+  You use these metrics to identify optimization opportunities, prioritize sustainability efforts, and demonstrate progress toward your sustainability goals. 
+  You recognize that workload carbon emissions derive from the resources you provision in AWS, so RUE gives you useful context for how those resources deliver value and where to optimize. 

 **Common anti-patterns:** 
+  Focusing solely on cost metrics without considering resource utilization or workload efficiency. 
+  Using inconsistent or changing metrics over time, making comparison difficult. 
+  Overlooking key resource consumption areas such as storage, data transfer, or memory. 
+  Not normalizing metrics based on workload output or business value. 

 **Benefits of establishing this best practice:** 
+  Creates a clear baseline for measuring sustainability improvements. 
+  Enables data-driven decision making for workload optimization. 
+  Provides visibility into the most resource-intensive aspects of your workload. 
+  Facilitates communication of sustainability efforts to stakeholders. 
+  Allows for objective comparison between different implementation approaches. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Start by determining the core usage metrics for your workload. To do this, you need to identify the key resources being consumed. Then, establish meaningful efficiency ratios that show the relationship between core usage metrics and appropriate business metrics. For example, if your workload is processing mortgage applications, your RUE may be: 


|  Numerator  |  Denominator  | 
| --- | --- | 
|  vCPU hours provisioned  |  Mortgage applications processed  | 

 The general formula is: 


|  Metric  |  Formula  | 
| --- | --- | 
|  RUE  |  Core resource provisioned metric / Business metric or workload outcome  | 

 To establish a useful RUE, it is essential to understand the resources behind your workload. The numerator of RUE should reflect the core resource consumption patterns of your workload. This provides a clear connection between outcomes and the resources required, which can influence the workload's environmental impact. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Identify the metrics which reflect the core resource consumption patterns of your workload: 

   1.  Start with [CUR 2.0 via Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) to get a high-level view of your AWS usage. 

   1.  Use services such as [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) to identify hot spots of resource usage. 

   1.  Consider standard resource metrics such as vCPU hours, GB-months of storage, and GB transferred. 

1.  Define relevant business metrics to measure workload output: 

   1.  Select business metrics that reflect the value provided by your workload. For example, number of transactions, active users, or API calls served. 

   1.  Verify that metrics are consistent and allow for valid comparisons over time. 

   1.  Avoid purely financial metrics as they may fluctuate independently of resource usage. 

1.  Calculate and monitor you workload's RUE as resource provisioned per unit of business value or customer outcome: 

   1.  Divide your core resource provisioned metric by your business metrics. For example, vCPU minutes per transaction or GB stored per customer 

   1.  Establish baselines for RUE to compare future improvements. 

   1.  Automate collection and reporting of RUE. 

1.  Review and refine your metrics periodically: 

   1.  Evaluate if your metrics still accurately reflect the resources provisioned for your workload. 

   1.  Update metrics as your workload evolves or as new measurement capabilities become available. 

   1.  Add new metrics as needed to capture different aspects of resource efficiency. 

1.  Track RUE over time: 

   1.  Monitor changes to the consumption of resources over time. 

   1.  Identify where accumulated changes result in inefficient or significant increases in resource consumption. 

   1.  Determine the need for improvements to address the changes in consumption and implement the improvements you prioritize. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SUS01-BP02 Create dashboards to combine resource usage efficiency and environmental impact data](sus01-bp02.md) 
+  [SUS03-BP01 Optimize workloads for high resource usage efficiency](sus03-bp01.md) 
+  [COST03-BP01 Track resources over their lifetime](cost03-bp01.md) 
+  [COST01-BP01 Establish cloud budgets and forecasts](cost01-bp01.md) 
+  [PERF01-BP03 Derive and establish KPIs that validate adherence to your performance requirements](perf01-bp03.md) 
+  [OPS02-BP01 Develop key performance indicators](ops02-bp01.md) 
+  [FND06-BP05 Establish organizational metrics to track optimization efforts](fnd06-bp05.md) 

 **Related examples:** 
+  [Unlocking the Power of Carbon Emissions & CUR](https://catalog.workshops.aws/unlock-carbon-and-cur) 
+  [Announcing the AWS Sustainability console: Programmatic access, configurable CSV reports, and Scope 1–3 reporting in one place](https://aws.amazon.com/blogs/aws/announcing-the-aws-sustainability-console-programmatic-access-configurable-csv-reports-and-scope-1-3-reporting-in-one-place/) 