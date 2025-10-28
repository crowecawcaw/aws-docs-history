# Monitoring and tagging AWS Elemental MediaTailor resources

Monitoring is an important part of maintaining the reliability, availability, and
performance of AWS Elemental MediaTailor and your other AWS solutions. AWS provides the
following monitoring tools to watch MediaTailor, report when something is wrong, and take
automatic actions when appropriate:

- _Amazon CloudWatch_ monitors your AWS resources and the applications
  that you run on AWS in real time. You can collect and track metrics, create
  customized dashboards, and set alarms that notify you or take actions when a
  specified metric reaches a threshold that you specify. For example, you can have
  CloudWatch track CPU usage or other metrics of your Amazon EC2 instances and automatically
  launch new instances when needed. For more information, see the
  [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon CloudWatch Logs_ enables you to monitor, store, and access your log
  files from all interactions with your ad decision server (ADS). AWS Elemental MediaTailor
  emits logs for ad requests, redirects, responses, and reporting requests and
  responses. Errors from the ADS and origin servers are also emitted to log groups in
  Amazon CloudWatch. MediaTailor also provides information about skipped ads and the reasons they were skipped. For more information, see [Ad skipping
  troubleshooting](troubleshooting-ad-skipping-overview.md "troubleshooting-ad-skipping-overview.md"). You can also archive your log data in highly durable storage. For general
  information, see the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md"). For information on the ADS logs and how to
  access them for analysis through Amazon CloudWatch Logs Insights, see [AWS Elemental MediaTailor ADS log analysis in Amazon CloudWatch Logs
  Insights](monitor-cloudwatch-ads-logs.md "monitor-cloudwatch-ads-logs.md").

###### Topics

- [Viewing AWS Elemental MediaTailor logs](monitoring-through-logs.md "monitoring-through-logs.md")
- [Monitoring AWS Elemental MediaTailor with Amazon CloudWatch
  metrics](monitoring-cloudwatch-metrics.md "monitoring-cloudwatch-metrics.md")
- [Recording AWS Elemental MediaTailor API calls](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [Receiving AWS Elemental MediaTailor channel assembly
  alerts](channel-assembly-alerts.md "channel-assembly-alerts.md")
- [Tagging AWS Elemental MediaTailor resources](tagging.md "tagging.md")
- [Monitoring AWS media services with
  workflow monitor](monitor-with-workflow-monitor.md "monitor-with-workflow-monitor.md")
