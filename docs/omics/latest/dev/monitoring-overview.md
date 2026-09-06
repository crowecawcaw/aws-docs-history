

# Monitoring AWS HealthOmics
<a name="monitoring-overview"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of AWS HealthOmics and your other AWS solutions. AWS provides the following monitoring tools to watch AWS HealthOmics, report when something is wrong, and take automatic actions when appropriate:
+ *Amazon CloudWatch* monitors your AWS resources and the applications you run on AWS in real time. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take actions when a specified metric reaches a threshold that you specify. For example, you can have CloudWatch track CPU usage or other metrics of your Amazon EC2 instances and automatically launch new instances when needed. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).
+ *Amazon CloudWatch Logs* enables you to monitor, store, and access your log files from Amazon EC2 instances, CloudTrail, and other sources. CloudWatch Logs can monitor information in the log files and notify you when certain thresholds are met. You can also archive your log data in highly durable storage. For more information, see the [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/).
+ *AWS CloudTrail* captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).
+ *Amazon EventBridge* is a serverless event bus service that makes it easy to connect your applications with data from a variety of sources. EventBridge delivers a stream of real-time data from your own applications, Software-as-a-Service (SaaS) applications, and AWS services and routes that data to targets such as Lambda. This enables you to monitor events that happen in services, and build event-driven architectures. For more information, see the [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/).

**Note**  
For service updates, configure and monitor your [Personal Health Dashboard](https://health.console.aws.amazon.com/health/home#/account/dashboard/open-issues). For more information on how to manage the dashboard, refer to [Getting started with your AWS Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/getting-started-health-dashboard.html).

**Topics**
+ [S3 access logging](#s3-access-logging)
+ [Monitoring HealthOmics with CloudWatch metrics](monitoring-cloudwatch.md)
+ [Monitoring HealthOmics with CloudWatch Logs](monitoring-cloudwatch-logs.md)
+ [Logging AWS HealthOmics API calls using AWS CloudTrail](logging-using-cloudtrail.md)
+ [Using EventBridge with AWS HealthOmics](eventbridge.md)

## S3 access logging
<a name="s3-access-logging"></a>

You can monitor Amazon S3 API access to HealthOmics sequence store data using the store-created access logs. You can use CloudWatch to monitor S3 access from HealthOmics API operations . CloudWatch provides visibility into Amazon S3 access originating from your own account. If you, as a data owner, share access to a third party account, access logging isn't available in CloudWatch. Instead, use the store’s S3 Access Log. which logs all S3 access to the data in the configured Amazon S3 bucket . 

Configure S3 Access Logs using the `CreateSequenceStore` or `UpdateSequenceStore` API operations. Also, make sure that the HealthOmics service principal (`omics.amazonaws.com`) has `s3:PutObject` permissions to the configured S3 prefix. 

**Note**  
Logs use the destination bucket’s default encryption configuration. If the bucket uses a customer managed key, the service principal must have access to [use the key for writing](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html).

To turn off access logging, use `UpdateSequenceStore` and set the access log configuration to blank. 