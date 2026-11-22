

# PERF05-BP05 Review metrics at regular intervals

 The metrics that matter change as the workload evolves. Traffic patterns shift, components change, and thresholds that once signaled trouble fire on normal behavior. Review metrics and alarms on a regular cadence and after significant incidents or workload changes. 

 **Desired outcome:** 
+  You review metrics, alarms, dashboards, and SLOs on a defined cadence and after significant incidents or workload changes. 
+  Your agents and MCP tools prepare a review artifact by inventorying signals, correlating telemetry, comparing baselines, and highlighting stale or missing coverage. 
+  Your workload owners validate the artifact and decide whether to add, retire, or change metrics, alarms, baselines, and thresholds. 
+  Your reviews identify which metrics supported decisions and which missing signals delayed detection or diagnosis. 
+  Your baselines and thresholds account for workload configuration, deployment, topology, and dependency changes that affect behavior. 
+  You correlate metrics across systems to explain behavior that individual signals do not show. 
+  You retire redundant metrics and add signals that improve detection, diagnosis, or business decisions. 

 **Common anti-patterns:** 
+  Teams allow metrics to remain in an alarm state for an extended period, so the alarm loses meaning. 
+  Teams create alarms without an owner or response path, including human response or automated action where the condition is well understood. 
+  Teams collect large numbers of metrics with no documented decision, SLO, alarm, dashboard, or investigation use. 
+  Teams collect metrics but never correlate them across systems for a workload-level view. 
+  Teams leave thresholds unchanged after workload patterns or component versions shift. 
+  Teams ask an agent to review metrics without granting scoped access to the required telemetry or providing workload objectives, SLOs, ownership, and architecture context. 
+  Teams accept an agent-generated review without validating the evidence or allow an agent to change metrics and alarms without owner approval. 
+  Teams schedule an automated report but establish no team ritual to review findings, assign actions, and track decisions. 

 **Benefits of establishing this best practice:** 
+  You keep monitoring relevant as the workload evolves. 
+  You reduce mechanical review work while keeping engineering judgment and decisions with workload owners. 
+  You resolve future incidents faster because each review improves the metric set. 
+  You reduce alarm noise by retiring stale metrics and correcting drifted thresholds. 
+  You detect emerging issues earlier through baselines and anomaly detection. 
+  You build a decision record that informs future instrumentation and performance work. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A threshold set for last year's traffic fires after traffic grows, and an alarm on a component you replaced is no longer helpful. When alarms pile up, the team ignores them. 

 After an incident, review which metrics helped, which added noise, and which were missing, and update monitoring based on what you find. 

 Unread metrics add storage and query cost and hide the signals that matter. Focus on metrics that drive decisions and are tied to workload objectives: response time, resource use, business outcomes, and user experience. Retire a metric that feeds no SLO, alarm, dashboard, investigation, or review. 

 Correlate metrics, logs, traces, deployments, and business signals to trace a latency change back to its component and event. Use static thresholds as baselines for stable behavior and anomaly detection for variable patterns. Revisit both baselines after traffic shifts, deployments, configuration changes, or incidents. 

 Agents and MCP servers automate the mechanical part of metric review. They inventory metrics and alarms, query alarm history and SLO compliance, correlate signals across systems, identify unused dashboards or missing instrumentation, and compare current behavior with baselines. The [AWS Observability Kiro Power](https://aws.amazon.com/about-aws/whats-new/2026/02/aws-observability-kiro-power/) is one example: it packages CloudWatch, Application Signals, CloudTrail, and AWS Documentation MCP servers with observability steering and gap analysis. Scope agent access to the required workload and use read-only tools. Owners review the artifact and approve any monitoring changes. 

 [AWS DevOps Agent custom agents](https://aws.amazon.com/devops-agent/features/) support schedule-based triggers using rate or cron expressions. Schedule a weekly or monthly custom agent to review metric usage, alarm state and noise, SLO compliance, baseline drift, missing coverage, telemetry cost, and changes since the previous review. The agent creates a durable report and routes it to the team's review workflow. During the review, owners verify the underlying data, accept or reject recommendations, assign actions, and record decisions. 

 [Amazon CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Intro.html) provides application performance monitoring, service maps, and SLOs. [CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) learns expected metric ranges, [CloudWatch Metrics Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.html) queries metrics at scale, and [CloudWatch Contributor Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) identifies contributors to high-cardinality trends. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define metrics, ownership, and decisions:** Select performance and business metrics aligned with workload objectives and SLOs. For each metric and alarm, record its owner, the decision or response it supports, and the source that produces it. 

1.  **Establish baselines for the current workload state:** Set a baseline and target for each metric and record the workload configuration, deployment, topology, and dependency state that produced it. Use [Amazon CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) for variable patterns and review the learned range after a regime change. 

1.  **Set a review cadence and automate artifact preparation:** Establish a weekly, monthly, or workload-specific interval. Configure an [AWS DevOps Agent custom agent with a schedule-based trigger](https://docs.aws.amazon.com/devopsagent/latest/userguide/custom-agents-executing-custom-agents.html), or an equivalent agent/MCP workflow, to collect evidence and produce a repeatable report before the team review. 

1.  **Review evidence and investigate deviations:** During the team ritual, verify the artifact against source metrics and dashboards. Compare current behavior with baselines, review alarm state and noise, examine component and aggregated signals, and investigate bottlenecks, missing coverage, and anomalies. Treat agent findings as hypotheses until the evidence confirms them. 

1.  **Identify corrective actions:** Translate validated findings into specific actions, such as adjusting a threshold, adding or retiring a metric, fixing a defect, scaling a resource, or changing the architecture. Assign an owner and target date to each action. 

1.  **Document findings and decisions:** Store the review artifact, evidence links, accepted and rejected recommendations, owners, and corrective actions in the team's knowledge or work-management system. 

1.  **Iterate and improve the review:** Track whether completed actions reduced alarm noise, improved detection or diagnosis, and controlled telemetry cost. Review agent precision and false positives, update its Skills or instructions, and refine the metric set and review artifact using this evidence. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF05-BP01 Use monitoring solutions to understand the areas where performance is most critical](perf05-bp01.md) 
+  [PERF05-BP03 Use automation to proactively remediate performance-related issues](perf05-bp03.md) 
+  [PERF05-BP02 Evaluate your workload performance](perf05-bp02.md) 
+  [PERF01-BP03 Derive and establish KPIs that validate adherence to your performance requirements](perf01-bp03.md) 
+  [PERF01-BP04 Establish criteria for performance degradation alerts and tolerances](perf01-bp04.md) 

 **Related documents:** 
+  [Application performance monitoring with Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Intro.html) 
+  [AWS Observability Kiro Power](https://aws.amazon.com/about-aws/whats-new/2026/02/aws-observability-kiro-power/) 
+  [AWS DevOps Agent custom SRE agents](https://aws.amazon.com/devops-agent/features/) 
+  [Executing AWS DevOps Agent custom agents](https://docs.aws.amazon.com/devopsagent/latest/userguide/custom-agents-executing-custom-agents.html) 
+  [Build bespoke operational workflows with AWS DevOps Agent custom SRE agents](https://aws.amazon.com/blogs/mt/build-bespoke-operational-workflows-with-aws-devops-agent-custom-sre-agents/) 
+  [CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) 
+  [Query metrics with CloudWatch Metrics Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.html) 
+  [Analyze high-cardinality data with CloudWatch Contributor Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) 
+  [Human validation of AI-derived incident facts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-IncidentReports-ai-facts.html) 

 **Related videos:** 
+  [Amazon's Observability Best Practices Revealed](https://aws.amazon.com/video/watch/1a569f79ca0/) 
+  [Building Effective AWS Observability Strategy](https://aws.amazon.com/video/watch/97f297a5083/) 
+  [AIOps for AWS Observability Strategy](https://aws.amazon.com/video/watch/6b95b13df68/) 

 **Related examples:** 
+  [CloudWatch Application Signals Skill Builder demo](https://github.com/aws-samples/sample-cloudwatch-application-signals-skillbuilder-demo) 
+  [Amazon CloudWatch Auto Alarms](https://github.com/aws-samples/amazon-cloudwatch-auto-alarms) 
+  [CloudWatch dashboards with AWS CloudFormation](https://github.com/aws-samples/cloudwatch-dashboards-cloudformation-sample) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) 