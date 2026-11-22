

# COST09-BP02 Continuously review and optimize the workload

 Cloud providers release new services, features, and pricing models continuously. Each release can make part of your workload cheaper to run. A workload you never revisit drifts from the most cost-effective design. Continuous review turns those releases into savings: decide whether to adopt new capabilities, replace components, or keep the current design. 

 **Desired outcome:** 
+  You continuously evaluate running workloads against newly available services, features, and pricing models. 
+  You have a decision framework that weighs modernizing a component against maintaining it, based on total cost of ownership. 
+  You validate adopted improvements against security, compliance, and performance requirements before rollout. 
+  Your optimization is ongoing and tied to the pace of new releases, not a one-time event. 

 **Common anti-patterns:** 
+  Teams keep legacy architectures in place even when more cost-effective options exist. 
+  Reviews chase immediate cost cuts and overlook long-term operational savings. 
+  Modernization decisions are made without accounting for total cost of ownership. 
+  Modernization is delayed until technical obsolescence forces it. 
+  New service and feature releases are never evaluated against the running workload. 

 **Benefits of establishing this best practice:** 
+  Workloads stay cost-effective as new services and pricing models become available. 
+  Operational overhead falls as managed services replace self-managed components. 
+  Technical debt and maintenance cost decline. 
+  Spend stays aligned with changing business requirements. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Every modernization carries a migration cost, such as engineering time, testing, and the risk of disruption. Weigh it against the ongoing savings the change produces. A change that reduces your monthly bill can still be a poor decision if migration consumes more than it returns. The opposite failure is more common: teams defer modernization because the migration cost is visible today, while the cost of staying put is spread over years and easy to ignore. 

 Maintaining a component past its useful life has a compounding cost. As a service ages, it falls behind on features, the pool of engineers who know it shrinks, and the surrounding system accumulates workarounds. Each of these effects raises the eventual cost of change. Deciding to maintain rather than modernize is a legitimate choice, but make it an explicit decision with a known cost. Do not let a component remain in place because no one revisited it. 

 Continuous optimization starts with new releases. A replacement that removes operational work often saves more than a like-for-like price cut. It reduces both unit price and the ongoing cost to run and maintain the component. Managed and serverless options are often the highest-value candidates. Filter releases down to the few that apply to your workload, and pair continuous review with a defined intake such as the [AWS What's New](https://aws.amazon.com/new/) feed. For example, replacing a self-managed messaging tier with [Amazon Simple Email Service (Amazon SES)](https://aws.amazon.com/ses/) removes the work of running server fleets while preserving the function at lower total cost. 

 Cost is not the only criterion. A cheaper design that breaks a data residency rule, weakens a security control, or misses a performance target is not an improvement. Regional availability, data privacy regulations, security requirements, and performance targets constrain which optimizations are viable. Include these constraints in your evaluations from the start. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish a cost baseline for the workload:** Measure current cost per component before evaluating any change, so you can quantify the impact of an optimization later. Use [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) to establish baseline spend and [cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) to attribute optimization work to the right components. Track these metrics over time in the [Cloud Intelligence Dashboards](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/getting-started.html). 

1.  **Track new service and feature releases:** Set up a regular intake of release information from the [AWS What's New](https://aws.amazon.com/new/) feed and map relevant announcements to components in your workload. Focus on releases that reduce operational work or introduce more cost-effective pricing. Pass the shortlisted candidates into your scheduled reviews. 

1.  **Run architecture reviews at your cadence:** Use the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/) and a [AWS Well-Architected Agent](https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent.html) to review the workload at the cadence set by your review process, matching review depth to the workload's strategic importance. Treat each review like an initial design phase with an added focus on optimization. Evaluate candidate changes against security, compliance, Regional availability, and performance requirements before they proceed. 

1.  **Compare modernization against maintenance using TCO:** For each candidate change, weigh migration cost against long-term savings using total cost of ownership. Include quantitative measures such as direct cost reduction, cost per transaction or request against the pre-optimization baseline, and the share of identified savings actually implemented, alongside qualitative gains such as reduced operational complexity. Record the decision and its rationale, whether it is to modernize or to maintain. 

1.  **Implement, measure, and feed back:** Roll out the selected changes and measure realized savings against the baseline. Use [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) to track savings over time and confirm the change delivered its expected return. Return the results to the review process so future evaluations use better estimates. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST09-BP01 Develop a workload review process](cost09-bp01.md) 
+  [COST01-BP04 Keep up-to-date with new service releases](cost01-bp04.md) 
+  [COST05-BP06 Perform continuous cost analysis](cost05-bp06.md) 

 **Related documents:** 
+  [How to perform a Well-Architected Framework Review - Part 1](https://aws.amazon.com/blogs/mt/how-to-perform-a-well-architected-framework-review-part1/) 
+  [How to perform a Well-Architected Framework Review - Part 2](https://aws.amazon.com/blogs/mt/how-to-perform-a-well-architected-framework-review-part2/) 
+  [How to perform a Well-Architected Framework Review - Part 3](https://aws.amazon.com/blogs/mt/how-to-perform-a-well-architected-framework-review-part3/) 
+  [How to track your cost optimization KPIs with the KPI Dashboard](https://aws.amazon.com/blogs/aws-cloud-financial-management/how-to-track-your-cost-optimization-kpis-with-the-kpi-dashboard/) 
+  [This is My Architecture](https://aws.amazon.com/architecture/this-is-my-architecture) 
+  [AWS Architecture All-In series](https://aws.amazon.com/architecture/all-in-series/all-in-the-field/) 
+  [Back to Basics](https://aws.amazon.com/architecture/back-to-basics/) 
+  [How to Build This](https://aws.amazon.com/architecture/how-to-build-this/) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Optimize cost and performance and track progress toward mitigation (ARC319)](https://www.youtube.com/watch?v=keAfy8f84E0) 
+  [AWS re:Invent 2024 - Driving cost optimization at scale (MAM236)](https://www.youtube.com/watch?v=l3Vlf_k16pg) 
+  [Continuous cost and sustainability optimization](https://www.youtube.com/watch?v=bx1IL9TLxqA) 

 **Related workshops:** 
+  [How to run an AWS Well-Architected Framework Review](https://catalog.workshops.aws/howto-wafr/en-US) 
+  [Visualize and optimize cloud cost efficiency](https://catalog.us-east-1.prod.workshops.aws/workshops/7f220ab4-7c62-4d30-8d09-10010e5328c2) 

 **Related services:** 
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) 
+  [AWS Data Exports](https://aws.amazon.com/aws-cost-management/aws-data-exports/) 