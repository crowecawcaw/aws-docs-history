

# OPS02-BP03 Regularly analyze workload metrics

 Metrics such as latency, error rate, and capacity show how a system behaves. Regular review of those metrics against expectations and business outcomes helps you make decisions: what to tune, what to investigate, and what is already working. 

 **Desired outcome:** 
+  You review your workload metrics on a defined cadence, not only when an incident forces you to. 
+  Your analysis prioritizes business outcome metrics and interprets technical metrics in relation to them. 
+  You detect unusual behavior even when a fixed threshold is hard to set in advance. 
+  You turn insights from your analysis into concrete changes in the workload. 

 **Common anti-patterns:** 
+  Teams examine metrics only during incidents and miss the trends that precede them. 
+  Analysis fixates on technical counters while ignoring the business metrics that show real impact. 
+  Organizations rely only on static thresholds and miss anomalies that fall inside those limits. 
+  Metrics from different accounts or Regions stay isolated, so no one sees the full picture of a distributed workload. 

 **Benefits of establishing this best practice:** 
+  Regular review reveals the correlation between technical performance and business outcomes. 
+  Decisions rest on current data rather than assumptions or stale reports. 
+  Anomaly detection surfaces early signs of trouble that static thresholds would miss. 
+  Teams address issues before they grow into customer-facing incidents. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Analysis compares current behavior against the workload's steady state, or its normal, healthy state. Establish that baseline first and revisit it when the workload or its traffic changes. 

 Technical metrics are abundant and easy to chart, so they can obscure the business outcome metrics that help you determine whether the workload serves its purpose. A latency graph tells you the system is slow, but a conversion metric tells you the slowness is costing sales. Read technical metrics against those business outcomes, and set your priorities based on business metrics. 

 Static thresholds are simple but limited. They work when you know the boundary between healthy and unhealthy in advance, and fail when normal behavior varies by time of day, season, or traffic pattern. While a threshold set for peak hours could generate a false alarm overnight, a threshold set for quiet periods might miss daytime problems. Anomaly detection learns the expected range from history and flags departures from it. Use static thresholds where you have a firm limit, and anomaly detection where the normal range shifts or you do not yet know the right boundary. 

 Workloads span multiple accounts and Regions, which fragments the data you need to analyze. An average hides the slow requests that damage customer experience; a high percentile such as p99 exposes them. Review percentile distributions in one view that aggregates metrics across accounts and Regions. 

 Analyze metrics in [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), which includes anomaly detection that models expected behavior and cross-account views for distributed workloads. When a metric deviates, [CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) correlates it with related telemetry and recent changes to provide a hypothesis of the probable cause. Between reviews, [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/) investigates operational signals and surfaces concerning trends with prioritized improvements. Neither replaces the review cadence: they raise candidates, and your baseline decides what is genuinely abnormal. 

 For workloads monitored in [CloudWatch Omni](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-omni.html), the review gains a consistent starting set of technical metrics from discovered services and reported RED metrics. For detail on the instrumentation that feeds these sources, see [OPS01-BP01 Develop application telemetry](ops01-bp01.md). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish the steady-state baseline:** Determine what normal looks like for your key metrics by reviewing historical data across representative time periods. Record expected ranges so that later analysis can distinguish real deviations from routine variation. Revisit the baseline when the workload or its traffic changes materially. 

1.  **Review metrics on a defined cadence:** Schedule regular reviews rather than waiting for incidents, and interpret spikes, drops, and trends against the baseline. Prioritize business outcome metrics, then trace the technical metrics that explain their movement. Assign the review to named owners so it happens consistently. 

1.  **Analyze distributions with percentiles:** Use [percentile statistics in Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Percentiles) to see how a metric is distributed rather than only its average. Percentiles reveal the tail behavior that shapes customer experience and helps you define service level targets. Where Application Signals is enabled, its [service level objectives](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html) track attainment against those targets continuously, and a burn rate that accelerates between reviews is itself a finding to analyze. 

1.  **Enable anomaly detection:** Turn on [CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) for metrics whose normal range varies or is not known in advance, and for metrics where no static threshold can work because the value cycles through peaks and troughs, such as sales by time of day. Let it learn the expected pattern, including the cycles, and alert when the metric breaks it, instead of maintaining brittle static thresholds manually. 

1.  **Analyze across accounts and Regions:** Enable [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) so the review covers the workload's whole footprint, across accounts and Regions, in one place. Use [Metrics Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.html) and [metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) to query, aggregate, and transform data across that footprint, and [query with PromQL](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL.html) where your metrics carry OpenTelemetry labels. In CloudWatch Omni, [Explore](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-explore-and-query-your-telemetry.html) runs the same PromQL against your metrics so you can describe the question in plain language and edit the resulting query. 

1.  **Include databases in the review:** Use [Amazon CloudWatch Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights.html) to analyze database performance alongside the workload metrics, moving from fleet-level health down to the load and top queries on a single database. Database behavior often explains an application-level deviation, so review the two together rather than in separate sittings. 

1.  **Add machine assistance to the review:** When a metric deviates from its baseline, start a [CloudWatch investigation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) from it so related telemetry and recent changes are correlated into a hypothesis of the probable cause. Use [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/) to investigate proactively and surface concerning trends between reviews, and route its findings to the teams that own the affected resources. 

1.  **Act on what the analysis finds:** Analysis exists to change the workload, so end every review with decisions: performance improvements where latency trends worsen, cost reductions where capacity sits idle, fixes prioritized where errors cluster, scaling plans where growth is heading, and corrections to alarms, thresholds, and baselines where they misfired. Assign each action an owner and track it to completion. When a finding is about the indicators themselves, feed it into the KPI review in [OPS02-BP01 Develop key performance indicators](ops02-bp01.md). A review that produces no decisions is itself a signal: either the workload is steady, or the metrics no longer measure what matters. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS02-BP01 Develop key performance indicators](ops02-bp01.md) 
+  [OPS02-BP02 Create actionable insights with dashboards](ops02-bp02.md) 
+  [OPS01-BP01 Develop application telemetry](ops01-bp01.md) 
+  [OPS06-BP01 Create actionable alerts](ops06-bp01.md) 

 **Related documents:** 
+  [The Wheel: how Amazon reviews service metrics weekly](https://aws.amazon.com/blogs/opensource/the-wheel/) 
+  [AWS Observability Best Practices](https://aws-observability.github.io/observability-best-practices/) 
+  [CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) 
+  [Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights.html) 
+  [CloudWatch Omni: Explore and query your telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-explore-and-query-your-telemetry.html) 
+  [AWS Well-Architected Agentic AI Lens: Tool integration and management practices](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops04.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - What's new with Amazon CloudWatch (COP363)](https://www.youtube.com/watch?v=MQmNzKZsx44) 
+  [AWS re:Invent 2025 - Move beyond reactive: Transform cloud ops with AWS DevOps Agent (COP362)](https://www.youtube.com/watch?v=JajBEYle67I) 

 **Related workshops:** 
+  [One Observability Workshop](https://catalog.workshops.aws/observability/en-US/intro) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) 