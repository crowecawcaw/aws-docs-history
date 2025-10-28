# Workflow monitor

groups and templates

Before you can deploy workflow monitoring to a signal map, you must create the groups and templates for CloudWatch alarms and EventBridge notifications. The CloudWatch templates
define what scenarios and thresholds will be used to trigger the alarms. The EventBridge templates will determine how these alarms are reported to you.

If you only want mappings of your connected resources and do not want to use
the monitoring template capabilities of workflow monitor, signal maps can be used without
CloudWatch and EventBridge templates. For more information about using signal maps, see:
[Signal maps](monitor-with-workflow-monitor-configure-signal-maps.md "monitor-with-workflow-monitor-configure-signal-maps.md")

###### Topics

- [CloudWatch alarm groups and templates for monitoring your AWS media workflow](monitor-with-workflow-monitor-configure-alarms.md "monitor-with-workflow-monitor-configure-alarms.md")
- [EventBridge rule
  groups and templates for monitoring your AWS media workflow](monitor-with-workflow-monitor-configure-notifications.md "monitor-with-workflow-monitor-configure-notifications.md")
