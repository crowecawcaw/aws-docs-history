

# COST01-BP02 Implement goals and targets

 Set goals that state the outcome your organization expects, and set targets that make each goal specific, measurable, and time-bound. Teams can then track progress and hold themselves accountable. 

 **Desired outcome:** 
+  You have cost and usage goals that state the direction your organization expects, expressed in terms the business understands. 
+  Each of your goals has at least one target that is specific, measurable, assignable, realistic, and time-bound. 
+  Your targets track efficiency, such as cost per unit of business outcome, rather than absolute spend alone. 
+  Your cost and usage key performance indicators are visible to the finance, engineering, and business stakeholders who share accountability for them. 
+  You review progress against targets on a regular cadence and adjust goals as business conditions change. 

 **Common anti-patterns:** 
+  Setting goals that cannot be measured, so no one can tell whether the organization is making progress. 
+  Defining a goal without an accompanying target, which leaves the expected magnitude and deadline undefined. 
+  Tracking absolute spend as the only metric, which penalizes growth even when efficiency improves. 
+  Measuring infrastructure metrics that do not connect to any business outcome. 
+  Setting goals inside one team, without input from finance, engineering, or the business. 

 **Benefits of establishing this best practice:** 
+  Teams know which cost outcomes matter and can prioritize the work that moves a target. 
+  Efficiency becomes visible over time, because targets measure cost against business output instead of raw spend. 
+  Shared, measurable targets align technical decisions with business objectives. 
+  Progress reviews catch drift early, before a missed goal becomes a budget problem. 
+  Cost-conscious decisions become part of engineering culture rather than a periodic finance exercise. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A goal names the direction: workload usage grows while cost grows more slowly. A target names how far and by when: usage rises 20% while cost rises less than 5% over the next two quarters. Organizations stall when they set one without the other. Goals give teams a shared sense of what good looks like, and targets make that direction tangible enough to measure. 

 Well-formed targets follow the [SMART criteria](https://en.wikipedia.org/wiki/SMART_criteria): specific, measurable, assignable, realistic, and time-bound. "Reduce waste" is a vague optimization goal. "Keep first-tier production compute over-provisioning below 10% of tier cost by the end of Q2, owned by the infrastructure team" is a target. 

 Absolute spend should not be tracked as a measure of success. Your costs may rise when the business grows. A falling bill can then reflect shrinking demand while efficiency is unchanged. A better measure is cost per unit of business outcome, such as cost per order, per active user, or per gigabyte processed. A unit metric separates growth from efficiency. A workload can serve twice the demand at a lower cost per unit even as its total bill increases. 

 Every metric that you're measuring should correlate with the business outcome. Infrastructure metrics such as instance utilization or response time show system performance. Efficiency metrics such as Spot adoption or AWS Graviton coverage show how cost-effectively you consume services. Business metrics tie spend to outcomes the organization cares about. Choose a small set that spans these types, but avoid setting targets for every metric you collect. Too many targets dilute focus and make reviews difficult. 

 Benchmarks give your targets a starting point. A benchmark is the value you compare actual results against, drawn from your own history or from common cost-optimization measures. The following table lists standard KPIs that many organizations track, from a single roll-up measure of overall efficiency down to compute, database, storage, and tagging. Cost Optimization Hub publishes the roll-up measure daily, so you have a benchmark without defining one yourself. AWS also publishes a periodic analysis of that metric across tens of thousands of opted-in accounts, so you can benchmark your score against a peer distribution. Treat target values as organization-specific: set them from your own goals and business context. 


|  Category  |  KPI  |  Description  | 
| --- | --- | --- | 
|  Efficiency  |  Cost efficiency (Cost Optimization Hub)  |  1 - (potential savings / total optimizable spend), refreshed daily on a rolling 30-day window, from Region to organization scope.  | 
|  Compute  |  EC2 commitment coverage  |  Share of eligible On-Demand Amazon EC2 usage (by cost or hours) covered by Savings Plans or Reserved Instances.  | 
|  Compute  |  Spot adoption  |  Share of interruption-tolerant EC2 usage running on Spot capacity.  | 
|  Compute  |  Savings Plans utilization  |  Committed spend consumed compared to the total hourly commitment.  | 
|  Compute  |  Reserved Instance utilization  |  Utilized reserved hours compared to total reserved hours.  | 
|  Compute  |  Average EC2 cost per normalized hour  |  EC2 cost divided by the number of normalized instance hours.  | 
|  Compute  |  vCPU cost  |  Cost per vCPU across all instances.  | 
|  Compute  |  Latest instance generation  |  Share of instances running on AWS Graviton or other current-generation types.  | 
|  Database  |  RDS commitment coverage  |  Share of eligible On-Demand Amazon RDS usage (by cost or hours) covered by Reserved Instances.  | 
|  Database  |  RDS utilization  |  Utilized reserved hours compared to total reserved hours.  | 
|  Storage  |  Optimized storage ratio  |  Cost of optimized storage tiers, such as archival or infrequent access, divided by total storage cost.  | 
|  Tagging  |  Untagged resources  |  Cost or count of untagged resources compared to total cost or count.  | 

 Near-real-time visibility into KPIs and savings opportunities lets teams act while a variance is still small. Standard dashboards built on your detailed billing data can track recommended cost-optimization KPIs and progress against custom goals. AWS Billing and Cost Management and Cost Management console provides managed dashboards, including Reservations and Savings Plans views that pair commitment coverage with utilization. Whatever tooling you choose, have every cloud financial management stakeholder use the same source. Finance and engineering can then debate decisions on shared numbers. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define expected usage levels:** Work with application owners, marketing, and business teams to establish expected demand for the workload. Account for how customer demand shifts over time and for seasonal peaks or marketing campaigns that change consumption. 

1.  **Quantify resources and cost at each usage level:** Translate expected usage into the resources required to serve it, such as larger or additional components, added data transfer, or a different service tier. Record the cost at each major usage point and predict how cost changes as usage changes. 

1.  **Set goals for usage and cost:** Combine the usage and cost projections with planned technology changes and improvement programs to define high-level goals. Each goal addresses usage, cost, and the relationship between them, and stays simple enough for people to understand what the business expects. 

1.  **Set a SMART target for each goal:** Convert every goal into a measurable target with an owner and a deadline, following the [SMART criteria](https://en.wikipedia.org/wiki/SMART_criteria). For an efficiency goal, quantify the improvement in business output per dollar and the date to reach it. For example, first-tier production compute over-provisioning stays below 10 percent of tier cost by a set date. Where a target concerns commitment coverage, you do not have to estimate the commitment it implies: in [Savings Plans Purchase Analyzer](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-purchase-analysis.html) you enter the coverage percentage of On-Demand spend you are targeting and receive the hourly commitment required to reach it, calculated from your actual historical usage and your existing Savings Plans inventory. That turns a coverage goal into a purchase-ready number, and modeling successive steps such as 80 percent then 90 percent lets you raise coverage in step with the rightsizing and idle-resource work you have already committed to. 

1.  **Select KPIs and benchmarks:** Choose KPIs that span efficiency and business outcomes from the categories described in the guidance, and set benchmark values from your own history and goals. Measure the business outcome behind each workload so the unit metrics you define are accurate and realistic. 

1.  **Track progress and review on a cadence:** Establish near-real-time visibility into your KPIs using the [Cloud Intelligence Dashboards](https://catalog.workshops.aws/awscid) KPI dashboard or an equivalent, and review actuals against targets with finance, engineering, and business stakeholders. Adjust goals and targets as business direction changes. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST01-BP01 Establish cloud budgets and forecasts](cost01-bp01.md) 
+  [COST01-BP03 Track project lifecycle](cost01-bp03.md) 
+  [COST02-BP02 Allocate costs based on workload metrics and business outcomes](cost02-bp02.md) 
+  [COST02-BP03 Monitor cost proactively](cost02-bp03.md) 

 **Related documents:** 
+  [What is a unit metric?](https://aws.amazon.com/blogs/aws-cloud-financial-management/what-is-a-unit-metric/) 
+  [Understanding your cost efficiency metric](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-cost-efficiency.html) 
+  [The AWS State of Cost Efficiency Report](https://aws.amazon.com/blogs/aws-cloud-financial-management/the-aws-state-of-cost-efficiency-report/) 
+  [Introducing Target Coverage in Savings Plans Purchase Analyzer](https://aws.amazon.com/blogs/aws-cloud-financial-management/introducing-target-coverage-in-savings-plans-purchase-analyzer/) 
+  [Visualizing and analyzing cost and usage data using Dashboards](https://docs.aws.amazon.com/cost-management/latest/userguide/dashboards.html) 

 **Related videos:** 
+  [Maximize Cost Effectiveness of generative AI workloads](https://www.youtube.com/watch?v=4Tt4Wx5lHKs) 

 **Related examples:** 
+  [KPI dashboard from the Cloud Intelligence Dashboards](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/cudos-cid-kpi.html) 

 **Related workshops:** 
+  [CFM Technical Implementation Playbooks (CFM TIPs): Foundations](https://catalog.workshops.aws/awscff/) 
+  [Cloud Intelligence Dashboards](https://catalog.workshops.aws/awscid) 