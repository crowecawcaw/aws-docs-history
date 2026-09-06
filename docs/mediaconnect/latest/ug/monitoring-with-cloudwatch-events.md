

# Monitoring with Amazon EventBridge events
<a name="monitoring-with-cloudwatch-events"></a>

EventBridge enables you to automate your AWS services and respond automatically to system events such as application availability issues or resource changes. Events from AWS services are delivered to EventBridge in near real time. You can write simple rules to indicate which events are of interest to you, and what automated actions to take when an event matches a rule.

The actions that can be automatically triggered using EventBridge include the following:
+ Invoking an AWS Lambda function
+ Invoking Amazon EC2 Run Command
+ Relaying the event to Amazon Kinesis Data Streams
+ Activating an AWS Step Functions state machine
+ Notifying an Amazon SNS topic or an Amazon SQS queue

For more information, see the [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

**Topics**
+ [MediaConnect flow state change event](monitoring-cloudwatch-events-flow-state-change.md)
+ [MediaConnect flow maintenance event](monitoring-cloudwatch-events-flow-maintenance.md)
+ [MediaConnect flow health event](monitoring-cloudwatch-events-flow-health.md)
+ [MediaConnect alert event](monitoring-cloudwatch-events-alert.md)
+ [MediaConnect source health event](monitoring-cloudwatch-events-source-health.md)
+ [MediaConnect output health event](monitoring-cloudwatch-events-output-health.md)
+ [MediaConnect output status change event](monitoring-cloudwatch-events-output-status-change.md)
+ [MediaConnect flow content quality event](monitoring-eventbridge-events-content-quality.md)
+ [MediaConnect router input content quality event](monitoring-eventbridge-events-router-input-content-quality.md)