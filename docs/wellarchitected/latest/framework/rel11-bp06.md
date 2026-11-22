

# REL11-BP06 Send notifications when events impact availability

 Send a notification whenever a threshold is breached, even when automation has already resolved the underlying event. Automated healing keeps a workload reliable, but it can also obscure recurring problems that need a real fix. Notify the right teams so they can spot patterns, including the failures that auto-healing absorbs, and address root causes before those failures grow. 

 **Desired outcome:** 
+  Alerts reach operations teams the moment thresholds are breached, such as error rate, latency, or other critical key performance indicators (KPIs). 
+  Notifications fire even when automated healing has already resolved the event, so recurring faults stay visible. 
+  Alarms are actionable, and their volume is low enough that teams do not ignore them. 
+  Complex conditions are captured with composite alarms built from multiple underlying signals. 

 **Common anti-patterns:** 
+  Teams send too many alarms. 
+  Teams send alarms that are not actionable. 
+  Teams set alarm thresholds too high or too low. 
+  Teams do not alarm on external dependencies. 
+  Teams ignore gray failures when designing monitoring and alarms. 
+  Automation heals a fault but never notifies the team that healing was needed. 

 **Benefits of establishing this best practice:** 
+  Operational and business teams learn of a degradation immediately, cutting both mean time to detect (MTTD) and mean time to repair (MTTR). 
+  Infrequent faults that auto-healing masks are surfaced and fixed instead of accumulating. 
+  Actionable, low-volume alarms keep teams responsive rather than desensitized. 
+  Composite alarms reduce false alerts by requiring several conditions before paging. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A component that fails and self-recovers ten times a day looks healthy on a status page, but that pattern should warn you of a defect. Notification turns that recurring recovery into a signal for a human to act on. Treat the notification as a separate concern from the remediation. While remediation restores service, notification preserves the evidence that service was at risk, which you need to fix the root cause. 

 Early on, a breached threshold sends an email so a person investigates. As your observability practice matures, the same event can trigger automated remediation that resolves the issue without human involvement. Keep the notification even after automating the fix, so you retain visibility into what the automation is handling. 

 Aim for alarms that correspond to a condition someone should act on, covering failure modes your health checks miss, including gray failures and problems in external dependencies. Set thresholds that give timely warning without so many false alarms that teams learn to ignore the channel. 

 Some conditions are only meaningful in combination, and a single-metric alarm cannot express them. A composite alarm evaluates several underlying alarms together against operational logic, so it fires only when a problem pattern emerges. Use composite alarms to reduce false pages and encode business rules, such as alerting when both error rate and latency degrade at the same time. Route the resulting alerts through the channels the receiving teams monitor, whether that is email, a chat tool, or an incident tracker. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Create application alarms:** Configure alarms that detect when part of your workload is not functioning correctly, based on the KPIs and metrics you monitor. 

1.  **Create infrastructure alarms:** Configure [infrastructure alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) that indicate when to scale resources and that can drive dashboards, notifications, and scaling actions. 

1.  **Add static and composite alarms:** Use [static threshold alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) for single-metric conditions, and use [composite alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.html) to combine multiple signals into an alert driven by operational logic. 

1.  **Route notifications to the right teams:** Send alerts by invoking [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html), and link the notification to any automation for remediation or communication so responders are informed even when a fix runs automatically. 

1.  **Integrate AWS service health signals:** Add [AWS Health Aware](https://aws.amazon.com/blogs/mt/aws-health-aware-customize-aws-health-alerts-for-organizational-and-personal-aws-accounts/) to gain visibility into AWS resource degradations, and provide proactive, real-time alerts for business-essential workloads. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL11-BP01 Monitor all components of the workload to detect failures](rel11-bp01.md) 
+  [REL11-BP03 Automate healing on all layers](rel11-bp03.md) 
+  [REL06-BP03 Send notifications with real-time processing and alarming](rel06-bp03.md) 

 **Related documents:** 
+  [Create a CloudWatch alarm based on a static threshold](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) 
+  [Create a composite alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.html) 
+  [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) 
+  [What Is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) 
+  [What is Amazon SNS?](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) 
+  [Publish custom metrics (PutMetricData / EMF)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) 
+  [AWS Health Aware](https://aws.amazon.com/blogs/mt/aws-health-aware-customize-aws-health-alerts-for-organizational-and-personal-aws-accounts/) 
+  [2025 Top 10 Announcements for AWS Cloud Operations](https://aws.amazon.com/blogs/mt/2025-top-10-announcements-for-aws-cloud-operations) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Logging and monitoring in AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/security-logging-monitoring.html) 