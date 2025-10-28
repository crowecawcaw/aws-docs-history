# Monitoring a channel or

multiplex using Amazon CloudWatch Events

MediaLive automatically turns the following information into events in
CloudWatch Events:

- Reporting on the [state of a
  channel or multiplex](monitor-activity-types-channel.md "monitor-activity-types-channel.md").
- [Alerts](monitor-activity-types-alerts-channels.md "monitor-activity-types-alerts-channels.md") generated when a channel is
  running.
  You can use Amazon CloudWatch Events to manage these events. For example, you can
  create event rules and deliver the events in emails or SMS messages.
  You can deliver events to a number of destinations. This chapter
  describes how to deliver them through Amazon Simple Notification Service (SNS).

For complete information about the options for managing events
using Amazon CloudWatch Events, see the [CloudWatch Events User Guide](../../../AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.md "../../../AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.md").

For complete information about using Amazon SNS, see the [SNS Developer
Guide](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md").

Note that events are emitted on a best-effort basis.

###### Topics

- [JSON
  for a state change event](monitoring-cloudwatch-json-state-change.md "monitoring-cloudwatch-json-state-change.md")
- [JSON for an
  alert event](monitoring-cloudwatch-json-alert.md "monitoring-cloudwatch-json-alert.md")
- [Option 1: Send all MediaLive events to an
  email address](option-1.md "option-1.md")
- [Option 2: Send events for specific
  channels to an email address](option-2.md "option-2.md")
