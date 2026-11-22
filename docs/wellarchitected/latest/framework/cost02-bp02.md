

# COST02-BP02 Allocate costs based on workload metrics and business outcomes

 To measure workload efficiency, tie spend to a business outcome, such as an order, a report, or an active user. Cost per outcome then shows whether the workload gets cheaper or more expensive as it grows. 

 **Desired outcome:** 
+  Your workload cost is expressed as a unit metric that ties spend to a business outcome. 
+  You can tell whether efficiency is improving even when total cost rises with growth. 
+  Your component-level metrics roll up into a consistent workload-level view. 
+  Your optimization decisions rest on cost-per-outcome data rather than raw spend. 

 **Common anti-patterns:** 
+  Teams track only technical metrics such as CPU or request count, with no link to business value. 
+  Cost review focuses on total spend, so healthy growth and waste look the same. 
+  Optimization starts without a baseline, so teams cannot prove whether it worked. 
+  Related workloads define efficiency differently, which makes comparison impossible. 
+  Shared resource cost is left out of the metric, understating the true cost per outcome. 
+  The unit metric uses a technical denominator (like requests or instances) that moves with architecture changes rather than business value. 

 **Benefits of establishing this best practice:** 
+  You separate cost growth caused by success from cost growth caused by waste. 
+  You justify workload investment with a defensible cost-per-outcome figure. 
+  You compare efficiency across teams and components on a common basis. 
+  You measure the return on each optimization effort over time. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A unit metric expresses cost as a ratio: total workload cost divided by a count of business outcomes. If cost per order falls while total cost climbs, the workload is scaling efficiently and the extra spend reflects more business. If cost per order rises, spend is outpacing value and optimization is overdue. 

 Pick an outcome the business already counts and cares about, so the metric means something to people outside engineering. A commerce application might measure cost per order, a data pipeline cost per gigabyte processed, an API service cost per million calls, and a machine learning workload cost per training run. A technical proxy like cost per running instance produces a vanity metric that moves with architecture changes and misses shifts in delivered value. For a workload with several components, define a metric per significant component and roll them up to a workload total without double counting. 

 Cost splits into static and variable parts. Static cost stays roughly flat regardless of volume, such as a database that runs continuously. Variable cost moves with demand. At low volume, static cost dominates and the cost per outcome looks high. As volume grows, static cost spreads across more outcomes and the unit cost falls. Separating static from variable cost shows whether to right-size a fixed component or reduce per-request cost. 

 Shared resources are the most common source of a misleading metric. When several teams run on a common cluster or database, leaving that cost out understates cost per outcome. Containerized workloads make this more tangible: tasks and pods share compute that does not divide cleanly by team. [Split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/enabling-split-cost-allocation-data.html) attributes shared compute and memory to the consuming workload, so cost and outcome cover the same work. 

 Capture a baseline before optimizing, and record expected demand and seasonality. Then you can tell whether a change in the unit metric reflects efficiency or a shift in volume. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Select the business outcome and unit metric:** Identify a small set of outcomes the business already counts, such as orders processed or reports generated, and define the cost-per-outcome ratio for each. For complex workloads, define a metric per significant component and align all of them to organizational KPIs. Document how each metric is calculated so teams measure it the same way. 

1.  **Establish a baseline and demand expectations:** Record the current cost per outcome as a reference point before making changes. Capture expected demand and seasonality so later movement in the metric can be attributed to efficiency rather than volume. 

1.  **Instrument the business metric:** Collect the outcome count from application logs or monitoring, and publish business-specific measurements as [custom Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) where a native source does not exist. 

1.  **Allocate cost to the metric:** Confirm resource tagging aligns with your organizational standard, and enable [split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/enabling-split-cost-allocation-data.html) for containerized and shared resources so the cost numerator matches the outcome denominator. Activate [cost allocation tags](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-resource-tags.html) in your Data Exports for detailed analysis. 

1.  **Build analysis and visualization:** Use [AWS Cost Explorer reports](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-reports.html) for quick views, query Data Exports with [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) for detailed analysis, and build [AWS Quick](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html) dashboards for ongoing visibility. The [KPI Dashboard](https://catalog.workshops.aws/awscid/en-US/dashboards/foundational/cudos-cid-kpi) from the AWS Cloud Intelligence Dashboards tracks optimization outcomes over time. 

1.  **Calculate and track efficiency:** Compute cost per business outcome, and track it against the baseline as demand changes. Compare peak against off-peak efficiency to find where static cost dominates, and watch the trend rather than any single reading. 

1.  **Review and improve on a cadence:** Review efficiency metrics with application, finance, and management stakeholders on a regular schedule. Record each optimization effort and its effect on the unit metric, and update the metrics as the business changes. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST02-BP01 Implement granular resource tagging for workload cost allocation](cost02-bp01.md) 
+  [COST02-BP03 Monitor cost proactively](cost02-bp03.md) 
+  [COST01-BP02 Implement goals and targets](cost01-bp02.md) 

 **Related documents:** 
+  [Best practices for tagging AWS resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) 
+  [Organizing and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) 
+  [Using split cost allocation data with Amazon CloudWatch Container Insights](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data-cloudwatch.html) 
+  [Improve cost visibility of Amazon ECS and AWS Batch with split cost allocation data](https://aws.amazon.com/blogs/aws-cloud-financial-management/la-improve-cost-visibility-of-containerized-applications-with-aws-split-cost-allocation-data-for-ecs-and-batch-jobs/) 
+  [Improve cost visibility of Amazon EKS with split cost allocation data](https://aws.amazon.com/blogs/aws-cloud-financial-management/improve-cost-visibility-of-amazon-eks-with-aws-split-cost-allocation-data/) 

 **Related videos:** 
+  [AWS CFM Talks: Creating an effective metrics strategy for your business](https://www.youtube.com/watch?v=zBO-K4RvbtM) 
+  [AWS CFM Talks: Use cost allocation strategies to understand your AWS bill](https://www.youtube.com/watch?v=g7KiVz95wjo) 
+  [The keys to AWS optimization: Container cost allocation](https://www.youtube.com/watch?v=_tj9cv_bHos) 

 **Related examples:** 
+  [What is a unit metric?](https://aws.amazon.com/blogs/aws-cloud-financial-management/what-is-a-unit-metric/) 
+  [Selecting a unit metric to support your business](https://aws.amazon.com/blogs/aws-cloud-financial-management/selecting-a-unit-metric-to-support-your-business/) 
+  [Unit metrics in practice – lessons learned](https://aws.amazon.com/blogs/aws-cloud-financial-management/unit-metrics-in-practice-lessons-learned/) 
+  [How unit metrics help create alignment between business functions](https://aws.amazon.com/blogs/aws-cloud-financial-management/unit-metrics-help-create-alignment-between-business-functions/) 
+  [How to track your cost optimization KPIs with the KPI Dashboard](https://aws.amazon.com/blogs/aws-cloud-financial-management/how-to-track-your-cost-optimization-kpis-with-the-kpi-dashboard/) 

 **Related tools:** 
+  [Cloud Intelligence Dashboards on AWS](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/getting-started.html) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon Athena](https://aws.amazon.com/athena/) 
+  [AWS Quick](https://aws.amazon.com/quick/) 
+  [AWS Data Exports](https://aws.amazon.com/aws-cost-management/aws-data-exports/) 