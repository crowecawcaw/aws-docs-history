# Monitoring DNS activity and performance with Route 53 Global Resolver

Route 53 Global Resolver provides comprehensive visibility into DNS activity across your organization,
enabling you to identify security threats, analyze client device behavior, and maintain
compliance. This chapter covers both the monitoring tools available and detailed procedures for
setting up DNS monitoring, configuring logging destinations, and analyzing DNS data to
investigate threats and optimize performance.

AWS provides these monitoring tools to help you maintain secure, reliable DNS
service:

- _Amazon CloudWatch_ tracks DNS query volumes, response times, and security
  events in real time. Create dashboards to monitor DNS performance across locations and set
  up alarms to notify you when query volumes spike or response times increase that you
  specify. For Route 53 Global Resolver, you can monitor query volumes, response times, and filtering
  activity. For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon CloudWatch Logs_ enables you to monitor, store, and access your log files
  from Amazon EC2 instances, CloudTrail, and other sources. Route 53 Global Resolver can deliver DNS query logs directly
  to CloudWatch Logs for real-time monitoring and analysis. You can also archive your log data in highly
  durable storage. For more information, see the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
- _Amazon EventBridge_ can be used to automate your AWS services and respond
  automatically to system events, such as application availability issues or resource changes.
  Events from AWS services are delivered to EventBridge in near real time. You can write simple
  rules to indicate which events are of interest to you and which automated actions to take
  when an event matches a rule. For more information, see [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf
  of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can
  identify which users and accounts called AWS, the source IP address from which the calls
  were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [Gain DNS visibility](gr-gain-visibility-into-dns-activity.md "gr-gain-visibility-into-dns-activity.md")
- [Configure DNS monitoring](gr-configure-dns-monitoring.md "gr-configure-dns-monitoring.md")
