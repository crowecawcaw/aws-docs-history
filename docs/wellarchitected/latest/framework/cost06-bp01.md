

# COST06-BP01 Perform cost modeling

 Cost modeling estimates the cost of a workload and each of its components under expected load before you commit to a configuration. Model the components that carry the most cost or risk first, so the effort matches the potential return. 

 **Desired outcome:** 
+  You have a cost model for the workload that breaks cost down by component, so you can see which parts drive spend. 
+  Your models include total cost of ownership, covering licensing, operations, and maintenance alongside infrastructure charges. 
+  You benchmark components under several predicted load levels and compare cost against performance at each level. 
+  Your models are reviewed on a regular cadence and adjusted as business conditions and pricing change. 

 **Common anti-patterns:** 
+  Deploying a workload with no analysis of whether its benefit outweighs its cost. 
+  Sizing resources without benchmarking against predicted load. 
+  Counting infrastructure charges alone and ignoring licensing, operations, and maintenance. 
+  Building a cost model once and never revisiting it as demand or pricing shifts. 
+  Optimizing for short-term cost rather than total cost of ownership. 

 **Benefits of establishing this best practice:** 
+  Investment decisions are grounded in the balance between a workload's cost and the value it delivers. 
+  High-cost components receive analytical attention proportional to their spend. 
+  Technical and business stakeholders share a common view of cost, so decisions are made with the same data. 
+  Configuration choices are validated against real load before they reach production. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A cost model expresses the workload and each component as a cost at a given performance level. Use the model to weigh cost against expected value and to compare configurations. 

 Total cost of ownership includes software licensing, the engineering effort to deploy and operate the workload, and ongoing maintenance. A configuration that looks cheaper on compute can cost more once you include this operational burden. For changes to an existing workload, [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-optimization-strategies.html) grades each recommended action by implementation effort. It also states whether the action needs a restart and whether it can be rolled back. Weigh that operational burden against the saving. 

 Direct the deepest modeling effort toward the highest-cost components. Accept coarser estimates for components that represent a small fraction of spend. 

 Benchmark the workload at several predicted load levels to show how cost scales with demand and where performance degrades. A measurement window that is too short hides cyclical demand and a two-week benchmark can miss a monthly peak and lead to under-provisioning. Choose metrics that reflect user experience, such as the 99th percentile, because averages hide the spikes that drive cost and performance risk. 

 Workloads, business conditions, and cloud pricing all change, so review the cost model on a regular cadence. Share the model with both technical and business stakeholders so decisions draw on the same data. For a review cadence to adopt, see the [review guidance in the Performance Efficiency Pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/performance-efficiency.html). 

 [AWS Pricing Calculator](https://docs.aws.amazon.com/cost-management/latest/userguide/pricing-calculator.html) in the AWS Billing and Cost Management and Cost Management console estimates cost for planned configurations before deployment. It can import your existing usage as a baseline and price it at your own discount and commitment rates. Use the [public calculator](https://calculator.aws/#/) if you do not have an AWS account. [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) models cost for running workloads and produces right-sizing recommendations for compute, storage, and functions from historical usage. [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) supplies the utilization metrics that feed accurate models. Install the CloudWatch agent to add memory metrics that instances do not report by default. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Gather requirements and set modeling depth:** Collect the business needs, existing commitments, and performance targets that constrain the workload. Rank components by expected cost or risk, and decide how much modeling effort each one receives so that high-value components get the deepest analysis. 

1.  **Estimate planned configurations:** Use [AWS Pricing Calculator](https://docs.aws.amazon.com/cost-management/latest/userguide/pricing-calculator.html) to estimate the cost of candidate resource types and sizes before deployment. Import existing usage as a baseline and select the rate configuration that includes your discounts and purchase commitments, so the estimate reflects what you will pay rather than public On-Demand rates. Include software licensing and estimated operations and maintenance effort so the estimate reflects total cost of ownership, not infrastructure alone. 

1.  **Benchmark under predicted loads:** Deploy the workload or a proof of concept into a separate account with the resource types and sizes you want to test. Run representative test data at several predicted load levels, and record output results alongside cost data for each run. Redeploy with alternative types and sizes and repeat, so you can compare cost against performance across configurations. 

1.  **Choose the measurement window and metrics:** Set an analysis window long enough to cover the workload's demand cycles, so a monthly peak is not lost in a two-week sample. Select metrics that reflect the user experience, such as the maximum or 99th percentile rather than the average. 

1.  **Model cost over time:** Evaluate the workload across time horizons, such as hourly, monthly, and multi-year. This exposes the effect of auto scaling, scheduled start and stop, and commitment-based discounts that a single snapshot hides. 

1.  **Review and refine on a cadence:** Set a recurring review, such as monthly, to compare modeled cost against actuals and adjust for changes in demand, business direction, and pricing. Share the updated model with technical and business stakeholders so decisions draw on current data. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST05-BP01 Identify workload requirements for cost](cost05-bp01.md) 
+  [COST06-BP02 Select resource type, size, and number based on data](cost06-bp02.md) 
+  [COST06-BP03 Select resource type, size, and number automatically based on metrics](cost06-bp03.md) 

 **Related documents:** 
+  [AWS Pricing Calculator](https://aws.amazon.com/aws-cost-management/aws-pricing-calculator/) 
+  [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) 
+  [Identifying opportunities to right size](https://docs.aws.amazon.com/compute-optimizer/latest/ug/ec2-metrics-analyzed.html) 
+  [Optimizing your cost with rightsizing recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html) 
+  [How do I estimate the cost of my planned AWS resource configurations?](https://repost.aws/knowledge-center/estimating-aws-resource-costs) 

 **Related services:** 
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Pricing Calculator](https://calculator.aws/#/) 