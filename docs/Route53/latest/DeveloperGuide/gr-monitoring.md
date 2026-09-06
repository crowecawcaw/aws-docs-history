

# Monitoring DNS activity and performance with Route 53 Global Resolver
<a name="gr-monitoring"></a>

Route 53 Global Resolver provides comprehensive visibility into DNS activity across your organization, enabling you to identify security threats, analyze client device behavior, and maintain compliance. This chapter covers both the monitoring tools available and detailed procedures for setting up DNS monitoring, configuring logging destinations, and analyzing DNS data to investigate threats and optimize performance.

AWS provides these monitoring tools to help you maintain secure, reliable DNS service:
+ *Amazon CloudWatch Logs* enables you to monitor, store, and access your log files from Amazon EC2 instances, CloudTrail, and other sources. Route 53 Global Resolver can deliver DNS query logs directly to CloudWatch Logs for real-time monitoring and analysis. You can also archive your log data in highly durable storage. For more information, see the [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/).
  + You can use metric filters to search and filter log data coming into CloudWatch Logs and create CloudWatch metrics from the log events. Use these metrics to track DNS query volumes, response times, and security events. You can also create dashboards to monitor DNS performance across locations and set up alarms to notify you when query volumes spike or response times increase. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).
+ *Amazon EventBridge* can be used to automate your AWS services and respond automatically to system events, such as application availability issues or resource changes. Events from AWS services are delivered to EventBridge in near real time. You can write simple rules to indicate which events are of interest to you and which automated actions to take when an event matches a rule. For more information, see [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/).
+ *AWS CloudTrail* captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

**Topics**
+ [Gain DNS visibility](gr-gain-visibility-into-dns-activity.md)
+ [Configure DNS monitoring](gr-configure-dns-monitoring.md)