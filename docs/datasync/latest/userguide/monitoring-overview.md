# Monitoring your AWS DataSync transfers

Monitoring is important for maintaining the reliability and performance of your AWS DataSync
transfer activities. We recommend that you collect monitoring data so
that you can more easily debug errors if one occurs. Before you start monitoring DataSync,
however, create a monitoring plan that includes answers to the following questions:

- What are your monitoring goals?
- What resources will you monitor?
- How often will you monitor these resources?
- What monitoring tools will you use?
- Who will perform the monitoring tasks?
- Who should be notified when something goes wrong?
  AWS provides various services and tools for monitoring DataSync. You can configure some of
  these to do the monitoring for you, but some require manual intervention. We recommend that
  you automate monitoring tasks as much as possible.

###### Topics

- [Understanding data transfer performance
  counters](transfer-performance-counters.md "transfer-performance-counters.md")
- [Monitoring data transfers with Amazon CloudWatch metrics](monitor-datasync.md "monitor-datasync.md")
- [Monitoring your data transfers with task reports](task-reports.md "task-reports.md")
- [Monitoring data transfers with Amazon CloudWatch Logs](configure-logging.md "configure-logging.md")
- [Logging AWS DataSync API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [Monitoring events by using Amazon EventBridge](events.md "events.md")
- [Monitoring AWS DataSync with manual
  tools](monitoring-task-manually.md "monitoring-task-manually.md")
