

# REL06-BP03 Send notifications with real-time processing and alarming

 Real-time notifications alert responders and trigger automation the moment a metric crosses a threshold or a significant event occurs. The design challenge is setting thresholds that catch real problems without burying responders in noise. 

 **Desired outcome:** 
+  Your alarms are based on service and application metrics that reflect workload health. 
+  When an alarm threshold is breached, the appropriate personnel and systems are notified promptly. 
+  Your notification routing sends automatable events to automation and human-judgment events to people. 
+  Your alarm thresholds are reviewed and adjusted as usage changes. 

 **Common anti-patterns:** 
+  Teams set alarm thresholds too high, so vital notifications never fire. 
+  Teams set thresholds too low, so important alerts are ignored amid a flood of noise. 
+  Teams leave alarms and thresholds unchanged as usage patterns shift. 
+  Teams route alarms best handled by automation to people, which generates excessive notifications. 

 **Benefits of establishing this best practice:** 
+  You detect issues early and respond to operational incidents quickly. 
+  You reduce alert fatigue by tuning thresholds to real conditions. 
+  You shorten mean time to detection for events that affect availability. 
+  You free responders to focus on the events that need human judgment. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Alarms are useful when the thresholds behind them are chosen with care. To avoid alert fatigue, treat thresholds as values you revisit as traffic grows and access patterns change. 

 Not every alarm needs to page a person. A useful distinction separates alarms that a machine can resolve from alarms that need human judgment. For example, automatic scaling can handle compute exhaustion without paging anyone. When a business metric drops for reasons the system cannot diagnose, a person needs to investigate. Decide the response path for each alarm before you create it, and send automatable events to automation. 

 [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) suits event-driven applications that react to events from your own applications, SaaS providers, and AWS services. It ingests events from more than 200 AWS services with no resources to create and uses a structured JSON event format. Use rules to select events and forward them to targets such as AWS Lambda, Amazon SQS, and Amazon SNS. [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) suits high fan-out delivery to thousands or millions of endpoints, with typical latency under 30 milliseconds. It supports Lambda, Amazon SQS, HTTP and HTTPS endpoints, SMS, mobile push, and email. A common pattern uses an EventBridge rule to filter events and Amazon SNS to fan them out to many subscribers. 

 Notifications need to cover both your own components and the health of the AWS services your workload depends on. [AWS Health](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html) is the authoritative source for the state of your AWS resources. Route Health events to email and chat channels through [AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html), and integrate them programmatically [through Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html). If you use AWS Organizations, aggregate Health events across accounts. [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) generates the underlying alarms, supports both metric and composite alarms, and emits EventBridge events whenever an alarm changes state. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Create metric and composite alarms:** Use [Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) to watch a single metric or an expression over a number of intervals. Use a composite alarm to combine the conditions of several alarms, so it enters alarm state only when the combined rule is met, which reduces noise from correlated signals. 

1.  **Configure Amazon SNS notifications:** Attach an [Amazon SNS topic](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) to each alarm so it notifies the right subscribers when the alarm changes state. Choose subscriber protocols that match how each audience works, such as email, chat, or SMS. 

1.  **Create EventBridge rules for event-driven responses:** [Create rules in EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) that match specific CloudWatch alarm state changes and route them to targets. For example, an alarm for low disk space can trigger a Lambda function through a rule to reclaim space. See [EventBridge targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html) for the supported destinations. 

1.  **Add AWS Health notifications:** Configure [AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html) to deliver AWS Health events to email and chat, and integrate Health with EventBridge for programmatic handling. If you use AWS Organizations, aggregate Health events across accounts. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL06-BP01 Monitor all components for the workload (Generation)](rel06-bp01.md) 
+  [REL06-BP02 Define and calculate metrics (Aggregation)](rel06-bp02.md) 
+  [REL06-BP04 Automate responses to alarms](rel06-bp04.md) 
+  [REL12-BP01 Use playbooks to investigate failures](rel12-bp01.md) 

 **Related documents:** 
+  [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) 
+  [Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) 
+  [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) 
+  [Using Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) 
+  [Metrics in Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) 
+  [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) 
+  [Using CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) 
+  [Types of data that you can protect](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/protect-sensitive-log-data-types.html) 
+  [What Is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) 
+  [What is AWS Health?](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html) 
+  [What is AWS User Notifications?](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Behind the scenes: How AWS drives operational excellence & reliability (COP415)](https://www.youtube.com/watch?v=Z-eo1FMhksg) 

 **Related examples:** 
+  [One Observability Workshop](https://catalog.workshops.aws/observability/) 
+  [Amazon EventBridge to AWS Lambda with feedback control by Amazon CloudWatch Alarms](https://serverlessland.com/patterns/cdk-closed-loop-serverless-control-pattern) 

 **Related services:** 
+  [Amazon Simple Notification Service](https://aws.amazon.com/sns/) 