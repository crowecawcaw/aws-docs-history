# Monitoring Amazon GameLift Streams

Monitoring is an important part of maintaining the reliability, availability, and performance of Amazon GameLift Streams and your other AWS solutions.
AWS provides the following monitoring tools to watch Amazon GameLift Streams, report when something is wrong, and take automatic actions when
appropriate:

- _Amazon CloudWatch_ monitors your AWS resources and the applications you run on AWS in real time. You can collect and
  track metrics, create customized dashboards, and set alarms that notify you or take actions when a specified metric reaches a
  threshold that you specify.
  For
  more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- With _Amazon CloudWatch Logs_ you can monitor, store, and access your log files from services like Amazon Elastic Compute Cloud, AWS CloudTrail, and
  other sources. CloudWatch Logs can monitor information in the log files and notify you when your services meet certain thresholds. You can also
  archive your log data in highly durable storage. For more information, see the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf of your AWS account and delivers the
  log files to an Amazon Simple Storage Service bucket that you specify. You can identify which users and accounts called AWS, the source IP address from
  which the calls were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
- _Real-time performance stats_ collect application-level and shared system-level performance stats during stream sessions. You can receive these stats in real-time on the client or post-session as a CSV file in exported session files. Using this feature, you can monitor the CPU, memory, GPU, and VRAM utilization of your stream. For more information, see [Real-time performance stats](realtime-performance-stats.md "realtime-performance-stats.md").
