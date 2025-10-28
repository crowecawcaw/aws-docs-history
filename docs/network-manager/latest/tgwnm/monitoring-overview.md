# Amazon CloudWatch metrics and events

AWS provides the following monitoring tools to watch the resources in your global network,
report when something is wrong, and take automatic actions when appropriate.

- _Amazon CloudWatch_ monitors your AWS resources and the applications
  that you run on AWS in real time. You can collect and track metrics, create
  customized dashboards, and set alarms that notify you or take actions when a
  specified metric reaches a threshold that you specify. For more information, see the
  [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon EventBridge_ delivers a near-real-time stream of system events
  that describe changes in AWS resources. EventBridge enables automated event-driven
  computing, as you can write rules that watch for certain events and trigger
  automated actions in other AWS services when these events happen. For more
  information, see the _[Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md")._
- _AWS CloudTrail_ provides a record of actions taken by
  a user, role, or an AWS services in your global network, capturing all API calls
  for global network events.

###### Topics

- [Monitor with CloudWatch metrics](monitoring-cloudwatch-metrics.md "monitoring-cloudwatch-metrics.md")
- [Monitor with EventBridge](monitoring-events.md "monitoring-events.md")
- [Log API calls using CloudTrail](nm-logging-using-cloudtrail.md "nm-logging-using-cloudtrail.md")
