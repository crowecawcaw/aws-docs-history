

# SEC04-BP02 Prepare metrics, alarms, and dashboards

 Metrics, alarms, and dashboards turn security data into signals your team can act on. When you track the right measurements and present them clearly, you can spot early warning signs, respond before an incident escalates, and show whether your security posture is improving over time. 

 **Desired outcome:** 
+  You track security metrics that produce actionable signals rather than vanity counts. 
+  Your dashboards present the most relevant metrics for each workload in a form the team can read quickly. 
+  You have baseline measurements for normal behavior, so deviations stand out. 
+  Your alarms notify the right responders when a metric crosses a defined threshold. 
+  Your metrics and dashboards are protected from unauthorized access and modification. 

 **Common anti-patterns:** 
+  Teams track vanity metrics that look active but drive no decision or response. 
+  Dashboards grow so complex that responders cannot find the signal that matters. 
+  Organizations skip baseline measurement, so they cannot tell normal activity from an attack. 
+  Teams focus only on quantitative counts and ignore qualitative context. 
+  Metrics and dashboards receive no access controls, which exposes security insight to unauthorized users. 
+  Teams build dashboards and then never act on what the metrics reveal. 

 **Benefits of establishing this best practice:** 
+  Threats appear earlier, because abnormal patterns stand out against a known baseline. 
+  Response is faster, because alarms route to the responders who can act. 
+  Decisions improve, because teams measure security posture with data instead of intuition. 
+  Dashboards stay relevant, because teams review and update them as the workload changes. 
+  Security insight stays protected, because access controls keep views out of unauthorized hands. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Metric selection is a more difficult task than dashboard construction. A metric becomes useful only when it drives a decision or a response. While lagging indicators confirm what has already happened, leading indicators warn you before an incident matures, which makes them superior for detection. 

 A baseline is a prerequisite for setting thresholds. Without a baseline for normal traffic, login rates, and error volumes, any threshold you set either floods responders with noise or does not trigger during a real event. Access and authentication metrics such as failed logins, password reset frequency, failed multi-factor attempts, incomplete registrations, and unverified accounts often rise before unauthorized access succeeds. Application performance and availability metrics such as request volume, uptime, response time, throttle counts, and error counts reveal a different class of risk. A sudden shift can indicate a denial-of-service attack or a misconfigured client. 

 Dashboards force a trade-off between clarity and completeness. An overabundance of metrics can hide important signals. Design each view for a specific audience and workload area, keep it short enough for a responder to read in seconds, and let teams customize which metrics they see. 

 Metrics and alarms only reduce risk when they connect to a response. Set thresholds that alert your incident response team, and define a process for acting on those alerts. Protect the dashboards themselves, because they reveal your security posture and monitoring coverage, which is what an attacker wants to see. Review both metrics and dashboards on a cadence, and adjust as the workload changes. 

 [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) publishes metrics for most AWS services and hosts dashboards and alarms. [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) gives you a central place to monitor, store, query, and analyze log data. Detection services such as [AWS Config](https://aws.amazon.com/config/), [Amazon GuardDuty](https://aws.amazon.com/guardduty/), and [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/cspm/) generate findings that feed your alerting, and the [AWS Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/getting-started-health-dashboard.html) reports events that affect your resources. GuardDuty Extended Threat Detection produces critical-severity attack sequence findings that correlate multiple signals into a single high-confidence alert, which you should escalate immediately. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Start from published service metrics:** Review the [published CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) for the services in your workload. Build [basic CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_dashboard.html) for performance, utilization, and volume metrics as a starting point. 

1.  **Derive metrics from your logs:** Using the logs your workload already captures, apply [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) to turn log data into actionable metrics. Display these derived metrics alongside the service metrics on your dashboard. 

1.  **Set baselines, thresholds, and alarms:** Establish baseline values for your key metrics from historical data, then define thresholds that reflect abnormal behavior. Create [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) for those thresholds, and [add them to the dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-and-work-with-widgets.html) so an exposure is visible at a glance. 

1.  **Add custom widgets for gaps:** For needs that standard widgets do not meet, create [custom widgets](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_custom_widget_dashboard.html). These can pull from other data sources or present data in formats the built-in widgets do not support. 

1.  **Add account and organization health views:** Use the [AWS Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/getting-started-health-dashboard.html) to track account health, events, and upcoming changes that might affect your resources. For multiple accounts, use the organizational view or build a custom dashboard. 

1.  **Route detection findings into alerting:** Feed findings from detection services into your alarms and dashboards. [AWS Config](https://aws.amazon.com/config/) evaluates and can remediate resource configurations, [Amazon GuardDuty](https://aws.amazon.com/guardduty/) analyzes activity for threats and produces attack sequence findings for multi-stage attacks, and [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/cspm/) evaluates your environment against security standards. [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) then aggregates and prioritizes findings from these services so you can focus on the risks that matter most. 

1.  **Protect and review dashboards:** Apply access controls so only authorized users can view or change your metrics and dashboards. Revisit them on a regular cadence, and adjust as the application and its risks evolve. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC04-BP01 Configure service and application logging](sec04-bp01.md) 
+  [SEC10-BP02 Develop incident management plans](sec10-bp02.md) 
+  [SEC10-BP03 Develop and test security incident response playbooks](sec10-bp03.md) 

 **Related documents:** 
+  [Building dashboards for operational visibility](https://builder.aws.com/content/3Ev2iw3R3ahQOM8BT4OUR0WP51z/building-dashboards-for-operational-visibility) 
+  [Using Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) 

 **Related examples:** 
+  [Observability best practices on AWS](https://github.com/aws-observability/observability-best-practices) 
+  [AWS Health events intelligence dashboards](https://github.com/aws-solutions-library-samples/aws-health-events-insight) 