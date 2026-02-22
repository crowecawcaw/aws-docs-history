# Understand monitoring with AWS Ground Station

Monitoring is an important part of maintaining the reliability, availability, and performance
of AWS Ground Station. AWS provides the following monitoring tools to watch AWS Ground Station, report when something is
wrong, and take automatic actions when appropriate.

- _Amazon EventBridge Events_
  delivers a near real-time stream of system events that describe changes in AWS resources.
  EventBridge Events enables automated event-driven computing, as you can write rules that watch
  for certain events and trigger automated actions in other AWS services when these events
  happen. For more information about EventBridge Events, see the
  [Amazon EventBridge
  Events User Guide](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md").
- _AWS CloudTrail_
  captures API calls and related events made by or on behalf of your AWS account and delivers
  the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts
  called AWS, the source IP address from which the calls were made, and when the calls occurred.
  For more information about AWS CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
- _Amazon CloudWatch Metrics_
  captures metrics for your scheduled contacts when using AWS Ground Station. CloudWatch Metrics enables you to
  analyze data based on your channel, polarization, and satellite ID to identify signal strength
  and errors in your contacts. For more information, see [Using Amazon CloudWatch
  metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md").
- _[AWS User Notifications](../../../notifications/latest/userguide/what-is.md "../../../notifications/latest/userguide/what-is.md")_ can be used to
  set up delivery channels to get notified about AWS Ground Station events. You receive a notification
  when an event matches a rule that you specify. You can receive notifications for events through
  multiple channels, including email,
  [Amazon Q Developer in chat applications](../../../chatbot/latest/adminguide/what-is.md "../../../chatbot/latest/adminguide/what-is.md")
  chat notifications, or
  [AWS Console Mobile Application](../../../consolemobileapp/latest/userguide/what-is-consolemobileapp.md "../../../consolemobileapp/latest/userguide/what-is-consolemobileapp.md")
  push notifications. You can also see notifications in the AWS Console
  [Notification center](https://console.aws.amazon.com/notifications/ "https://console.aws.amazon.com/notifications/"). User Notifications support
  aggregation, which can reduce the number of notifications you receive during specific events.
  Use the following topics to monitor AWS Ground Station.

###### Topics

- [Automate AWS Ground Station with
  Events](monitoring.md "monitoring.md")
- [Log AWS Ground Station API calls with AWS CloudTrail](monitoring.md "monitoring.md")
- [View metrics with Amazon CloudWatch](monitoring.md "monitoring.md")
