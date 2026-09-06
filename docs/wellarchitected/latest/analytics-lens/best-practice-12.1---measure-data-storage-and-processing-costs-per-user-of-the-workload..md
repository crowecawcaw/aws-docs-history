

# Best practice 12.1 – Measure data storage and processing costs per user of the workload
<a name="best-practice-12.1---measure-data-storage-and-processing-costs-per-user-of-the-workload."></a>

 Data analytics workloads have recurring stable costs and per-use costs, for example, a weekly reporting job with relatively static data storage fees or periodic unpredictable processing runtime fees. Your organization should establish a financial attribution mechanism that captures data storage and workload usage when analytics systems are run. Using this approach, your end users (business unit, team, or individual) can be notified of their consumption at regular intervals. 

## Suggestion 12.1.1 – Use tagging or other attribution methods to identify workload and data storage ownership
<a name="suggestion-12.1.1---use-tagging-or-other-attribution-methods-to-identify-workload-and-data-storage-ownership."></a>

 Collaboration between business, IT, and finance team to agree on cost allocation, cost ownership, cost charging, and budget management. Create budget tracking policy for storage and workload using tagging. Agree on the governance approach to implement policy (that is, central and decentralize), billing allocation, charge back, and budget reporting. 

 For more details, refer to the following information: 
+  AWS Cloud Financial Management Blog: Cost [Tagging and Reporting with AWS Organizations](https://aws.amazon.com/blogs/aws-cloud-financial-management/cost-tagging-and-reporting-with-aws-organizations/) 
+  AWS Billing and Cost Management and Cost Management User Guide: [Reporting your budget metrics with budget reports](https://docs.aws.amazon.com/cost-management/latest/userguide/reporting-cost-budget.html), [Configuring AWS Budgets actions](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html) and [Creating an Amazon SNS topic for budget notifications](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-sns-policy.html) 

 

## Suggestion 12.1.2 – Implement cost-visibility and internal bill-back method to aggregate your teams' use of analytics resources
<a name="suggestion-12.1.2"></a>

 Notify teams of their analytics usage costs periodically. Build dashboards that provide teams visibility into how their work impacts costs to the business using a self-service approach. 

 You can view and optimize your costs through the AWS Cost and Usage Report and the Cost and Usage Dashboards Operations Solution (CUDOS) reports. 