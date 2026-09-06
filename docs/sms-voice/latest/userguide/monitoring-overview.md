

# Monitoring AWS End User Messaging SMS
<a name="monitoring-overview"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of AWS End User Messaging SMS and your other AWS solutions. AWS provides the following monitoring tools to watch AWS End User Messaging SMS, report when something is wrong, and take automatic actions when appropriate:
+ **Amazon CloudWatch** monitors your AWS resources and the applications you run on AWS in real time. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take actions when a specified metric reaches a threshold that you specify. For example, you can have CloudWatch track CPU usage or other metrics of your Amazon EC2 instances and automatically launch new instances when needed. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).
+ **Amazon CloudWatch Logs** enables you to monitor, store, and access your log files from Amazon EC2 instances, CloudTrail, and other sources. CloudWatch can monitor information in the log files and notify you when certain thresholds are met. You can also archive your log data in highly durable storage. For more information, see the [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/).
+ **AWS CloudTrail** captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).
+ **AWS Health Dashboards**, can check and monitor the status of your AWS End User Messaging SMS environment. To check the status of the AWS End User Messaging SMS service overall, use the AWS Service Health Dashboard. To check, monitor, and view historical data about any events or issues that might affect your AWS environment more specifically, use the AWS Personal Health Dashboard. To learn more about these dashboards, see the [AWS Health User Guide](https://docs.aws.amazon.com/health/latest/ug/).
+ **AWS Trusted Advisor ** inspects your AWS environment and provides recommendations for opportunities to address security gaps, improve system availability and performance, and save money. All AWS customers have access to a core set of Trusted Advisor checks. Customers who have a Business or Enterprise support plan have access to additional Trusted Advisor checks.

  Many of these checks can help you assess the security posture of your AWS End User Messaging SMS resources as part of your AWS account overall. For example, the core set of Trusted Advisor checks includes the following:
  + Logging configurations for your AWS account, for each supported AWS Region .
  + Access permissions for your Amazon Simple Storage Service (Amazon S3) buckets, which might contain files that you import into AWS End User Messaging SMS to build segments.
  + Use of AWS Identity and Access Management users, groups, and roles to control access to AWS End User Messaging SMS resources.
  + IAM configurations and policy settings that might compromise the security of your AWS environment and AWS End User Messaging SMS resources.

  For more information, see [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html#trusted-advisor) in the *Support User Guide*.

**Topics**
+ [Monitoring with CloudWatch](monitoring-cloudwatch.md)
+ [Create CloudWatch Alarms](monitoring-sms-cw.md)
+ [Monitoring spending](monitor-spending.md)
+ [CloudTrail logs](logging-using-cloudtrail.md)
+ [Using EventBridge](monitor-event-bridge.md)