

# REL06-BP06 Regularly review monitoring scope and metrics

 Monitoring drifts out of date as a workload and its architecture change. Review your monitoring on a regular cadence, and after significant events or changes, so it keeps pace with how the workload behaves. 

 **Desired outcome:** 
+  You review and update your monitoring strategy periodically and after significant changes. 
+  Your monitoring is anchored in service-level indicators and business metrics, not default metrics alone. 
+  You confirm that key application health indicators stay relevant as requirements evolve. 
+  You uncover and close monitoring blind spots before they hide an incident. 

 **Common anti-patterns:** 
+  Teams collect only default metrics and add nothing specific to the workload. 
+  Teams set up a monitoring strategy and never review it. 
+  Teams deploy major changes without discussing their monitoring impact. 
+  Teams trust outdated metrics to judge workload health. 
+  Teams are overwhelmed by false-positive alerts from stale thresholds. 
+  Teams focus on low-level technical metrics and exclude business metrics. 

 **Benefits of establishing this best practice:** 
+  You anticipate potential problems and confirm you can detect them. 
+  You uncover blind spots that earlier reviews missed. 
+  You reduce false-positive alerts by retiring thresholds that no longer fit. 
+  You keep monitoring aligned with the business outcomes the workload supports. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Anchor monitoring in business metrics, and those priorities shift as the business changes. A metric that mattered at launch can become irrelevant after a redesign. A new customer-facing feature can introduce a new failure mode. Center the review on *service-level indicators (SLIs)*, which measure whether the workload meets its objectives. Draw on signals from infrastructure, applications, clients, and users. A strategy built only on default metrics almost always leaves gaps, because default metrics describe the environment, not the customer experience 

 Stale thresholds are their own failure mode, which is easy to miss. When usage grows but thresholds stay fixed, alarms that once signaled trouble begin firing during normal operation. Operators learn to dismiss them, and the next real alert gets dismissed with the rest. Validating each threshold against current healthy behavior is as important as adding new metrics. During the same review, look for parts of the application that produce no telemetry at all and would fail without alarming. 

 The [Resilience Analysis Framework](https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-analysis-framework/introduction.html) guides you through identifying failure modes and the preventive and corrective controls that mitigate them. Working backward from failure modes tells you which metrics and events are worth monitoring. Schedule reviews inside your [operational readiness review (ORR)](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html), which already evaluates workload readiness. Trigger off-cadence reviews from your correction-of-error process, since each incident reveals ways to improve your monitoring. 

 Assign the monitoring review to the team that operates the workload, and set a consistent schedule. Add a monitoring-analysis checkpoint to your change management process so no significant change ships without evaluating its monitoring impact. Real user monitoring shows whether client behavior exposes coverage gaps that may not be exposed by server-side metrics. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Schedule recurring dashboard reviews:** Set a regular cadence to inspect workload dashboards, with different depths for different intervals. During each review, compare current metric values against historical values to spot trends such as rising latency, falling business throughput, or increasing failure responses. 

1.  **Investigate outliers, anomalies, and sharp changes:** Look beyond averages and medians, which can mask problems, to the highest and lowest values in the window. Investigate observations far outside normal bounds, and treat any sudden change in the quantity or direction of a metric as a prompt to add tracking. Tighten expected bounds as workload consistency improves. 

1.  **Reassess monitoring relevance:** Using the [Resilience Analysis Framework](https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-analysis-framework/introduction.html) and analysis of previous incidents, decide whether additional aspects of the application belong in scope. Review Real User Monitoring metrics to find gaps in application-functionality coverage. 

1.  **Add a monitoring step to change management:** Update your change management process so a monitoring-analysis step runs before any change is approved. This confirms that new components and behaviors will be observed once they ship. 

1.  **Fold reviews into ORR and correction of error:** Make monitoring review a standing part of your [operational readiness review](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html) and correction-of-error processes, so each incident feeds improvements back into monitoring scope. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL06-BP01 Monitor all components for the workload (Generation)](rel06-bp01.md) 
+  [REL06-BP02 Define and calculate metrics (Aggregation)](rel06-bp02.md) 
+  [REL06-BP07 Monitor end-to-end tracing of requests through your system](rel06-bp07.md) 
+  [REL12-BP02 Perform post-incident analysis](rel12-bp02.md) 
+  [REL12-BP05 Conduct game days regularly](rel12-bp05.md) 

 **Related documents:** 
+  [Why you should develop a correction of error (COE)](https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe/) 
+  [Building dashboards for operational visibility](https://builder.aws.com/content/3Ev2iw3R3ahQOM8BT4OUR0WP51z/building-dashboards-for-operational-visibility) 
+  [Using Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) 
+  [Sample queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.html) 
+  [Solutions Catalog \| AWS Observability Best Practices](https://aws-observability.github.io/observability-best-practices/) 
+  [Resilience analysis framework](https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-analysis-framework/introduction.html) 
+  [Failure mode observability](https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-analysis-framework/observability.html) 
+  [Operational Readiness Reviews (ORR) - Operational Readiness Reviews (ORR)](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html) 
+  [Failure mode observability](https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-analysis-framework/observability.html) 

 **Related examples:** 
+  [The Amazon Builders' Library: Instrumenting distributed systems for operational visibility](https://builder.aws.com/content/3EuxPBdIiiUhB5IK47p3O3fxhy7/instrumenting-distributed-systems-for-operational-visibility) 

 **Related workshops:** 
+  [One Observability Workshop](https://catalog.workshops.aws/observability/) 