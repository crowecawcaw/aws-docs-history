

# Amazon CloudWatch metrics and events
<a name="monitoring-overview"></a>

AWS provides the following monitoring tools to watch the resources in your global network, report when something is wrong, and take automatic actions when appropriate.
+ *Amazon CloudWatch* monitors your AWS resources and the applications that you run on AWS in real time. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take actions when a specified metric reaches a threshold that you specify. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).
+ *Amazon EventBridge* delivers a near-real-time stream of system events that describe changes in AWS resources. EventBridge enables automated event-driven computing, as you can write rules that watch for certain events and trigger automated actions in other AWS services when these events happen. For more information, see the *[Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/).*
+  *AWS CloudTrail* provides a record of actions taken by a user, role, or an AWS services in your global network, capturing all API calls for global network events.

**Topics**
+ [Monitor with CloudWatch metrics](monitoring-cloudwatch-metrics.md)
+ [Monitor with EventBridge](monitoring-events.md)
+ [Log API calls using CloudTrail](nm-logging-using-cloudtrail.md)