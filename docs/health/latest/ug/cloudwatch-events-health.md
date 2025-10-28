# Monitoring events in AWS Health with

Amazon EventBridge

You can use Amazon EventBridge to detect and react to AWS Health events. Then, based on rules that
you create, EventBridge invokes one or more target actions when an event matches the values that you
specify in a rule. Depending on the type of event, you can capture event information, initiate
additional events, send notifications, take corrective action, or perform other actions. For
example, you can use AWS Health to receive email notifications if you have AWS resources in
your AWS account that are scheduled for updates, such as Amazon Elastic Compute Cloud (Amazon EC2) instances.

###### Notes

- AWS Health delivers events on a _durable_ basis and attempts to successfully deliver events to EventBridge at least once.
- Any EventBridge rules that you create can only receive notifications for your AWS account.
  To receive organizational events for other accounts within your AWS Organizations, see
  [Aggregating AWS Health events using organizational view and delegated administrator
  access](aggregating-health-events.md "aggregating-health-events.md").
- Public health events might take up to one hour to start sending after you create an EventBridge rule.
  You can choose between multiple target types for EventBridge as part of your AWS Health workflow,
  including:

- AWS Lambda functions
- Amazon Kinesis Data Streams
- Amazon Simple Queue Service (Amazon SQS) queues
- Built-in targets (such as CloudWatch alarm actions)
- Amazon Simple Notification Service (Amazon SNS) topics
  For example, you can use a Lambda function to pass a notification to a Slack channel when an
  AWS Health event occurs. Or, you can use Lambda and EventBridge to send custom text or SMS
  notifications with Amazon SNS when an AWS Health event occurs.

For samples of automation and customized alerts that you can create in
response to AWS Health events, see the [AWS Health Tools](https://github.com/aws/aws-health-tools "https://github.com/aws/aws-health-tools") in GitHub.

###### Topics

- [Creating EventBridge rules for AWS Region coverage](choosing-a-region.md "choosing-a-region.md")
- [Monitoring account-specific and public events for
  AWS Health](about-public-events.md "about-public-events.md")
- [Viewing paginated lists of AWS Health events on
  EventBridge](pagnation-of-health-events.md "pagnation-of-health-events.md")
- [Aggregating AWS Health events using
  organizational view and delegated administrator access](aggregating-health-events.md "aggregating-health-events.md")
- [Integrating AWS Health event monitoring and notifications
  with JIRA and ServiceNow](SMC-integration.md "SMC-integration.md")
- [Configuring an EventBridge rule to
  send notifications about events in AWS Health](creating-event-bridge-events-rule-for-aws-health.md "creating-event-bridge-events-rule-for-aws-health.md")
- [Configuring Amazon Q Developer in chat applications to
  send notifications about events in AWS Health](receive-health-events-with-aws-chatbot-event-bridge.md "receive-health-events-with-aws-chatbot-event-bridge.md")
- [Running operations on EC2 instances
  automatically in response to events in AWS Health](automating-instance-actions.md "automating-instance-actions.md")
- [Reference: AWS Health events
  Amazon EventBridge schema](aws-health-events-eventbridge-schema.md "aws-health-events-eventbridge-schema.md")
