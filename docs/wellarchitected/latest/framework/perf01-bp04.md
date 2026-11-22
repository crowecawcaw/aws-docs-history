

# PERF01-BP04 Establish criteria for performance degradation alerts and tolerances

 Performance degradation alerts and tolerance thresholds give teams early warning of problems so they can respond before users are affected. Define what counts as degradation, set how much deviation you tolerate, and route alerts to the people who can act. 

 **Desired outcome:** 
+  You have degradation criteria and tolerance thresholds defined for each KPI. 
+  Your alerts detect problems early and reach the right people through defined channels. 
+  You have dashboards that show system health, performance, and customer impact at a glance. 
+  Your alerting framework improves over time as you learn from operational experience. 

 **Common anti-patterns:** 
+  Teams monitor components in isolation without accounting for their interdependencies or overall system health. 
+  Teams set too many sensitive alerts, producing a volume of notifications that responders learn to ignore. 
+  Teams build cluttered dashboards that obscure the current state of the system. 
+  Teams set technical thresholds without connecting them to business operations or user experience. 

 **Benefits of establishing this best practice:** 
+  Early detection reduces downtime by catching problems before they escalate into critical issues. 
+  Defined response paths shorten the time from alert to resolution. 
+  Dashboards focused on customer impact help teams prioritize the issues that matter most. 
+  Data-driven thresholds improve resource allocation and cost management. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The main failure mode is alert fatigue. If a system fires too many alerts, or fires on unactionable conditions, responders ignore them and real incidents slip by. Map each alert to a specific condition and response, and delete alerts that trigger no action. 

 Degradation criteria describe what worse means for a KPI. Tolerance defines how much worse is acceptable before you raise an alert. Normal variation is expected, so treating it as an incident generates noise. Derive tolerance from historical baselines, business objectives, and user expectations. 

 Static threshold alerts are simple and predictable. They serve variable workloads poorly because a fixed threshold is too tight at low traffic and too loose at peak. Anomaly detection adapts to changing patterns and needs no manual threshold, but it can be opaque and requires tuning before teams trust it. Multi-condition alerts combine several signals to reduce false positives, and add complexity. Match the approach to how predictable your workload is, and expect to use more than one. 

 Dashboards present alerts and metrics so responders can act quickly. Design each dashboard for its audience. An executive view emphasizes customer-driven metrics and business impact. An operational view surfaces the signals on-call engineers need to diagnose a problem. Pair dashboards with response protocols, escalation paths, and automation so a triggered alert leads to a defined action. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define degradation criteria:** Work with business and application owners to describe what performance degradation means for your workload in terms the business recognizes. Tie each criterion to a KPI so degradation is measured, not judged by feel. 

1.  **Set tolerance thresholds:** Establish acceptable tolerance for each KPI from historical data, business objectives, and user expectations. Set the band wide enough to absorb normal variation and tight enough to catch genuine degradation. 

1.  **Configure alerts:** Choose the alerting approach that fits the workload's predictability: 
   +  Threshold-based alerts for stable, well-understood KPIs. 
   +  Anomaly detection for variable workloads where a fixed line does not fit. 
   +  Multi-condition alerts that combine signals to cut false positives. 

1.  **Establish communication and response protocols:** Set up clear channels for alert notifications and define what happens when an alert fires, including alert frequency guidelines, escalation procedures, and automation of routine responses. 

1.  **Build operational dashboards:** Design dashboards for their audience so system status is clear at a glance. Focus on customer-driven metrics, optimize for fast loading and real-time use, keep presentation consistent, aggregate signals for complex systems, and confirm the views are understandable to every team member. 

1.  **Review and refine:** Reassess your alerts, thresholds, and dashboards on a cadence using what you learn from operations. Retire alerts that generate noise and adjust tolerances as the workload and business needs change. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF01-BP03 Derive and establish KPIs that validate adherence to your performance requirements](perf01-bp03.md) 
+  [PERF05-BP01 Use monitoring solutions to understand the areas where performance is most critical](perf05-bp01.md) 
+  [PERF05-BP03 Use automation to proactively remediate performance-related issues](perf05-bp03.md) 

 **Related documents:** 
+  [How to set up Amazon CloudWatch alarms to monitor I/O metrics of Amazon EBS volumes using metric math](https://aws.amazon.com/blogs/mt/how-to-set-up-amazon-cloudwatch-alarms-to-monitor-io-metrics-of-amazon-ebs-volumes-performance-using-metric-math/) 
+  [Analyzing AWS WAF logs in Amazon CloudWatch Logs](https://aws.amazon.com/blogs/mt/analyzing-aws-waf-logs-in-amazon-cloudwatch-logs/) 
+  [Enhance CloudWatch metrics with metric math functions](https://aws.amazon.com/blogs/mt/enhance-cloudwatch-metrics-with-metric-math-functions/) 

 **Related examples:** 
+  [DB Top Monitoring (AWS Samples)](https://github.com/aws-samples/db-top-monitoring) 