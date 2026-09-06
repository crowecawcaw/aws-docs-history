

# Monitoring and auditing S3 Files
<a name="s3-files-monitoring-logging"></a>

S3 Files integrates with the following AWS services to help you monitor your file systems:

**Amazon CloudWatch**  
By default, S3 Files metric data is automatically sent to CloudWatch at 1-minute periods, unless noted differently for some individual metrics. You can also watch a single metric over a time period that you specify, and perform one or more actions based on the value of the metric relative to a given threshold over a number of time periods. The action is a notification sent to an Amazon Simple Notification Service (Amazon SNS) topic or Amazon EC2 Auto Scaling policy.  
For more information, see [Monitoring S3 Files with Amazon CloudWatch](s3-files-monitoring-cloudwatch.md).

**CloudTrail**  
CloudTrail captures API calls and related events made by or on behalf of your AWS account and delivers log files to an Amazon S3 bucket that you specify. S3 Files logs management events including creating file systems, creating mount targets, and mounting file systems to compute instances. S3 Files does not log data events, such as file read and write operations.  
For more information, see [Logging with CloudTrail for S3 Files](s3-files-logging-cloudtrail.md).

**Topics**
+ [Monitoring S3 Files with Amazon CloudWatch](s3-files-monitoring-cloudwatch.md)
+ [Logging with CloudTrail for S3 Files](s3-files-logging-cloudtrail.md)