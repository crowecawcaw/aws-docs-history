

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
+ [MediaConnect flow events](monitoring-eventbridge-flow-events.md)
+ [MediaConnect router input events](monitoring-eventbridge-router-input-events.md)
+ [MediaConnect router output events](monitoring-eventbridge-router-output-events.md)