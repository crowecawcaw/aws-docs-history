# Logging and monitoring for S3 Tables

Monitoring is an important part of maintaining the reliability, availability, and
performance of Amazon S3 Tables. We recommend collecting monitoring
data from your tables in table buckets so that you can more easily debug a
multipoint failure if one occurs.

AWS provides several tools for monitoring your S3 Tables resources and responding
to potential incidents.

**Amazon CloudWatch Alarms**

Using Amazon CloudWatch alarms, you watch a single metric over a time period that you
specify. If the metric exceeds a given threshold, a notification is sent to an
Amazon SNS topic or AWS Auto Scaling policy. CloudWatch alarms do not invoke actions because they
are in a particular state. Rather the state must have changed and been
maintained for a specified number of periods. For more information, see [Monitoring metrics with Amazon CloudWatch](cloudwatch-monitoring.md "cloudwatch-monitoring.md").

**AWS CloudTrail Logs**

CloudTrail provides a record of actions taken by a user, role, or an AWS service
in Amazon S3. Using the information collected by CloudTrail, you can determine the request
that was made to Amazon S3, the IP address from which the request was made, who made
the request, when it was made, and additional details. For more information, see
[Logging Amazon S3 API calls using AWS CloudTrail](cloudtrail-logging.md "cloudtrail-logging.md").

###### Topics

- [Logging with AWS CloudTrail for S3 Tables](s3-tables-logging.md "s3-tables-logging.md")
