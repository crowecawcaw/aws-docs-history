# Creating rules for Amazon EMR events with

CloudWatch

Amazon EMR automatically sends events to a CloudWatch event stream. You can create rules that
match events according to a specified pattern, and route the events to targets to take
action, such as sending an email notification. Patterns are matched against the event
JSON object. For more information about Amazon EMR event details, see [Amazon EMR events](../../../AmazonCloudWatch/latest/events/EventTypes.md#emr_event_type "../../../AmazonCloudWatch/latest/events/EventTypes.md#emr_event_type") in the
_Amazon CloudWatch Events User Guide_.

For information about setting up CloudWatch event rules, see [Creating a CloudWatch rule that
triggers on an event](../../../AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.md "../../../AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.md").
