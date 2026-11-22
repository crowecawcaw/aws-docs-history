

# COST09-BP01 Develop a workload review process

 Cloud services, pricing models, and architectural patterns change. A workload that was cost-optimized last year might not be optimized today, and a single optimization can't keep pace. A repeatable review process finds savings on a cadence that matches each workload's cost and importance. 

 **Desired outcome:** 
+  You have a documented, repeatable process that defines how and when each workload is evaluated for cost optimization. 
+  You set review frequency and depth in proportion to each workload's cost, business importance, and the effort required to change it. 
+  Your reviews assess total cost of ownership, including operational, maintenance, and licensing costs, not resource costs alone. 
+  Your reviews evaluate new services, features, and pricing models as candidate improvements. 
+  You add identified opportunities to a prioritized backlog that feeds your normal development cycle. 

 **Common anti-patterns:** 
+  Teams review a workload only when costs spike or during annual budget planning. 
+  The same review frequency and depth applies to every workload, regardless of its share of the bill. 
+  Reviews examine resource costs but ignore operational, maintenance, and licensing costs. 
+  Legacy components stay in place because their long-term cost is never assessed. 
+  New service capabilities and pricing models never enter the review, so the workload drifts away from more cost-effective options. 

 **Benefits of establishing this best practice:** 
+  Cost optimization opportunities surface proactively instead of after an overrun. 
+  Review effort concentrates where it produces the most savings, because cadence tracks cost impact. 
+  Spend stays aligned with business value as workloads and priorities change. 
+  Technical debt from aging components is identified before its cost compounds. 
+  The workload keeps pace with new cost-saving services and pricing models. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Reactive reviews, during a bill spike or budget season, arrive after the spend has happened and compete with other year-end work. A scheduled review looks for savings before they become overruns and makes optimization routine. 

 Not every workload deserves the same attention. Review effort is itself a cost. Spending a week on a workload that is two percent of the bill rarely pays back. Size review frequency and depth to each workload's share of spend and business importance. A workload that drives revenue or a large share of the bill needs frequent, deep reviews. A small, stable workload needs only an annual check. Proportional cadence reduces review fatigue. 

 Cadence also depends on the effort to act on findings. When a component has high spend and low change effort, such as compute that responds to pricing changes, frequent review pays off. Each review can produce a quick, inexpensive adjustment. When change effort is high, such as a core database that requires extensive testing, review less often. The chance to act arrives slowly. Set the schedule against both potential savings and the cost of capturing them. 

 Assess total cost of ownership (TCO), including operational effort, maintenance, and software licensing. These often dominate for older components. Legacy components carry a particular risk. Their cost rises over time as they fall behind on new features, skilled staff become scarce, and the surrounding system grows more complex. Modernizing looks expensive in any single review, so the decision is easy to defer. Repeated deferral turns a manageable cost into an unavoidable one. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Decompose the workload and estimate component costs:** Break the workload into distinct components and attribute cost to each. Use [AWS Cost Categories](https://docs.aws.amazon.com/cur/latest/userguide/) and [cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) to group and track spend by component, and analyze the patterns in [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html). This cost breakdown is the input to every cadence decision that follows. 

1.  **Assign a review cadence to each component:** Set review frequency and depth from each component's share of spend, its business importance, and the effort required to change it. Factor in software licensing agreements and the cost of changing them. For example, review compute every six months, databases annually, and storage according to access pattern. Record the cadence and the reasoning so the schedule is repeatable. 

1.  **Define review criteria and depth per component:** Match the depth of each review to the component's potential benefit and complexity. A database review might examine [Amazon RDS](https://aws.amazon.com/rds/) configuration, [Amazon Aurora Serverless](https://aws.amazon.com/rds/aurora/serverless/) options, and query patterns in [Amazon RDS Performance Insights](https://aws.amazon.com/cloudwatch/features/analytics-and-insights/). A compute review might analyze [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics, [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) recommendations, and [Savings Plans](https://aws.amazon.com/savingsplans/) coverage. A storage review might assess lifecycle policies and storage class transitions with [Amazon S3 Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/userguide/analytics-storage-class.html). 

1.  **Document findings with a standard template:** Record each review's findings and recommendations in a standardized template. Capture quantitative measures such as potential savings, implementation effort, and risk, so opportunities can be compared. Prioritize by return on investment and business alignment, then add the selected initiatives to your development backlog. Consolidate and deduplicate recommendations across accounts and Regions with [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) so the highest-value opportunities can be ranked quickly. Use [AWS Systems Manager](https://aws.amazon.com/systems-manager/) to maintain a resource inventory and the [Cloud Intelligence Dashboards](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/getting-started.html) for custom visualizations. 

1.  **Build an optimization feedback loop:** Measure the impact of implemented changes and return the results to the process. Track realized savings over time with [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html), and adjust cadence and criteria based on what the reviews actually produce. Where reviews repeatedly recommend the same change, automate it, for example with [AWS Auto Scaling](https://aws.amazon.com/autoscaling/), scheduled [AWS Lambda](https://aws.amazon.com/lambda/) functions, and governance through [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST09-BP02 Continuously review and optimize the workload](cost09-bp02.md) 
+  [COST05-BP06 Perform continuous cost analysis](cost05-bp06.md) 
+  [COST01-BP04 Keep up-to-date with new service releases](cost01-bp04.md) 

 **Related documents:** 
+  [Tags for cost allocation and financial management](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tags-for-cost-allocation-and-financial-management.html) 
+  [AWS Cloud Financial Management](https://aws.amazon.com/aws-cost-management/) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Building an optimized cloud workload with AWS (SUP201)](https://www.youtube.com/watch?v=1DUIwJfNvKg) 
+  [AWS re:Invent 2023 - Scaling AWS Well-Architected best practices across your organization (ARC216)](https://www.youtube.com/watch?v=UXtZCoE9qfQ) 

 **Related examples:** 
+  [Consolidate optimization recommendations in Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) 

 **Related workshops:** 
+  [CFM Technical Implementation Playbooks (CFM TIPs)](https://catalog.workshops.aws/awscff/) 

 **Related services:** 
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) 
+  [AWS Cost Categories](https://aws.amazon.com/aws-cost-management/aws-cost-categories/) 
+  [AWS Data Exports](https://aws.amazon.com/aws-cost-management/aws-data-exports/) 