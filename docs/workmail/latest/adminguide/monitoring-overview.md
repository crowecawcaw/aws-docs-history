

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html). 

# Logging and monitoring in Amazon WorkMail
<a name="monitoring-overview"></a>

Monitoring and auditing your email and logs is important for maintaining the health of your Amazon WorkMail organization. Amazon WorkMail supports two types of monitoring: 
+ **Event logging** – Monitoring the email sending activity for your organization helps protect your domain reputation. Monitoring can also help you track emails that are sent and received. For more information about how to enable email event logging, see [Enabling email event logging](tracking.md).
+ **Audit logging** – You can use audit logs to capture detailed information about your Amazon WorkMail organization usage such as monitor user’s access to mailboxes, audit for suspicious activity, and debug access control and availability provider configurations. For more information, see [Enabling audit logging](audit-logging.md).

AWS provides the following monitoring tools to watch Amazon WorkMail, report when something is wrong, and take automatic actions when appropriate:
+ *Amazon CloudWatch* monitors your AWS resources and the applications that you run on AWS in real time. For example, when you enable email event logging for Amazon WorkMail, CloudWatch can track emails sent and received for your organization. For more information about monitoring Amazon WorkMail with CloudWatch, see [Monitoring Amazon WorkMail with CloudWatch metrics](monitoring-workmail-cloudwatch.md). For more information about CloudWatch, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).
+ *Amazon CloudWatch Logs* enables you to monitor, store, and access your email events and audit logs for Amazon WorkMail when email and audit logging is enabled in the Amazon WorkMail console. CloudWatch Logs can monitor information in the log files, and you can archive your log data in highly durable storage. For more information about tracking Amazon WorkMail messages using CloudWatch Logs, see [Enabling email event logging](tracking.md) and [Enabling audit logging](audit-logging.md). For more information about CloudWatch Logs, see the [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/).
+ *AWS CloudTrail* captures API calls and related events made by or on behalf of your AWS account, and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see [Logging Amazon WorkMail API calls with AWS CloudTrail](logging-using-cloudtrail.md).
+ *Amazon S3* enables you to store and access your Amazon WorkMail events in a cost-effective way. Amazon S3 provides mechanisms for managing the [event data lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html), enabling you to configure automatic deletion of old events, or configure automatic archival to [Amazon S3 Glacier](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-glacier). Note, delivery Amazon S3 is only available for audit logging events. For more information about Amazon S3, see the [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).
+ *Amazon Data Firehose* enables you to stream your event data to other AWS services such as Amazon Simple Storage Service (Amazon S3), Amazon Redshift, Amazon OpenSearch Service, Amazon OpenSearch Serverless, Splunk, and any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers, including Datadog, Dynatrace, LogicMonitor, MongoDB, New Relic, Coralogix, and Elastic. Delivery to Firehose is only available for audit logging events. For more information about Firehose, see the [Amazon Data Firehose developer guide](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html).

**Topics**
+ [Monitoring Amazon WorkMail with CloudWatch metrics](monitoring-workmail-cloudwatch.md)
+ [Monitoring Amazon WorkMail email event logs](cw-events.md)
+ [Monitoring Amazon WorkMail audit logs](monitoring-audit-logging.md)
+ [Using CloudWatch Insights with Amazon WorkMail](cw-insights.md)
+ [Logging Amazon WorkMail API calls with AWS CloudTrail](logging-using-cloudtrail.md)
+ [Enabling email event logging](tracking.md)
+ [Enabling audit logging](audit-logging.md)