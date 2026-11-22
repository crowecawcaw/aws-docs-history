

# OPS02-BP01 Develop key performance indicators

 Key performance indicators (KPIs) tie a workload's behavior to the business outcomes it produces. Derive each KPI from a business outcome or priority, then analyze it against its target and adjust as the workload and business change. 

 **Desired outcome:** 
+  Your KPIs express business outcomes as measurable targets, not raw technical counters alone. 
+  You track a small, agreed set of KPIs that both your technical and business teams recognize as meaningful. 
+  Each of your KPIs has an owner, a target, and a threshold that triggers investigation when crossed, and ideally earlier, when the trend puts the business outcome at risk. 
+  You review and revise your KPIs on a regular cadence as the workload and business priorities change. 

 **Common anti-patterns:** 
+  Teams monitor whatever is easy to collect and never connect those metrics to a business outcome. 
+  Organizations track dozens of indicators, so no one can tell which signal deserves attention during an incident. 
+  Teams define KPIs once and never revisit them, so the measurements drift away from current business goals. 
+  Dashboards fill with technical counters such as CPU and request counts that give no direct read on customer or revenue impact. 

 **Benefits of establishing this best practice:** 
+  A drop in a business KPI, or in the RED metrics (rate, errors, and duration) that lead it, points to a problem faster than a search through many technical counters. 
+  The impact of an incident becomes measurable: a business KPI shows how much of the business outcome is being lost, which is rarely possible from technical metrics alone. 
+  Monitoring effort concentrates on the signals that reflect business outcomes, which reduces noise and cost. 
+  Shared KPIs give technical and business teams a common language for operational health. 
+  Teams detect and act on issues before they grow into broad business impact. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A metric measures one dimension of behavior, such as request latency or error count. A KPI is a metric with a target and business meaning (for example, the latency customers tolerate before abandoning a purchase). 

 Lagging indicators, such as completed orders or monthly active users, confirm business outcomes but report them after the fact. Leading indicators, such as checkout latency or queue depth, move earlier and give you time to act, but correlate less directly with the outcome. Pair a few lagging indicators that define success with the leading indicators that help you anticipate those outcomes. 

 Alongside RED metrics (rate, errors, and duration), business outcome metrics are among the easiest signals to detect problems, and they alone measure business impact. A 30 percent drop in orders per minute quantifies impact and sets the priority of the response. 

 Vanity metrics can dilute attention because they look healthy and move reliably but do not help you meaningfully make decisions. So does KPI sprawl, where a number of preferred measurements stack up over time until the dataset is too large to use. Drop any candidate KPI that has no owner and no action. 

 KPI definition is a shared responsibility, not a task handed to one team. Business stakeholders know which outcomes matter, while engineers know which signals are measurable and how they behave. Site reliability engineering's service level indicator and service level objective model gives a useful structure. An indicator is what you measure, and an objective is the target you hold it to. [Amazon CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html) implements this model. Enable it to define service level objectives on its standard application metrics or on any CloudWatch metric. That includes the custom business metrics you publish from these steps. A business KPI then carries a target and error budget like a technical one, with burn-rate alarms that warn while budget remains. 

 [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) collects metrics from AWS services and your application. Express each KPI as a metric you can chart, alarm on, and compare against its target. CloudWatch holds infrastructure and custom business metrics together, so you can correlate a change in a business KPI with the technical signals underneath it. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Start from business outcomes:** Identify the outcomes the workload exists to produce, such as completed transactions, retained users, or fulfilled requests. Work with business stakeholders to rank these outcomes so you know which ones justify a KPI. Let this ranking, not the availability of data, drive what you measure. The Amazon retail site exists so that customers can order products, so its most important KPI is orders per minute. 

1.  **Select paired leading and lagging indicators:** For each priority outcome, choose one lagging indicator that confirms the outcome and one or two leading indicators that predict it. Confirm each indicator is measurable from telemetry the workload already emits or can emit. Keep the total set small enough that a reader can hold it in mind. 

1.  **Set targets and thresholds:** Assign each KPI a target that represents acceptable performance and a threshold that triggers investigation. Base these values on historical behavior and business tolerance, not on round numbers. Record the owner responsible for acting when a threshold is crossed. Where Application Signals is enabled, it can [create recommended service level objectives](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html) for a monitored service, which gives you a reviewed starting point instead of a blank page. 

1.  **Instrument KPIs in Amazon CloudWatch:** Publish the underlying measurements as [Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html), including custom business metrics that AWS services do not emit by default. Define each KPI as a metric or metric math expression you can chart and alarm against its threshold. With Application Signals enabled, you can also define a [service level objective](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html) directly on a business metric, and monitoring these for business outcomes helps you choose KPIs that reflect value delivered, not just requests served. 

1.  **Review and revise on a cadence:** Schedule a recurring review with technical and business teams to compare KPIs against targets and confirm they still reflect current priorities. Retire KPIs that no longer drive a decision, and add new ones as the workload changes. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS02-BP02 Create actionable insights with dashboards](ops02-bp02.md) 
+  [OPS02-BP03 Regularly analyze workload metrics](ops02-bp03.md) 
+  [OPS01-BP01 Develop application telemetry](ops01-bp01.md) 
+  [OPS01-BP02 Develop user experience telemetry](ops01-bp02.md) 

 **Related documents:** 
+  [AWS Observability Best Practices](https://aws-observability.github.io/observability-best-practices/) 
+  [Service level objectives (SLOs)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html) 
+  [Publish custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) 
+  [Send metrics using OpenTelemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/metrics-otel-send.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Implementing observability at scale: A blueprint for success (COP328)](https://www.youtube.com/watch?v=GxZ2c4XsXOw&t=265s) 

 **Related workshops:** 
+  [One Observability Workshop](https://catalog.workshops.aws/observability) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 