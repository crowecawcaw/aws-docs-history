# Logging and Monitoring in

Amazon Location Service

Logging and monitoring are an important part of incident response. It lets you establish
a security baseline to detect deviations that you can investigate and respond to. By
implementing logging and monitoring for Amazon Location Service, you're able to maintain the reliability,
availability, and performance for your projects and resources.

AWS provides several tools that can help you log and collect data for incident
response:

**AWS CloudTrail**

Amazon Location Service integrates with AWS CloudTrail, which is a service that provides a record of
actions taken by a user, role or AWS service. This includes actions from the
Amazon Location Service console, and programmatic calls to Amazon Location API operations. These
records of action are called events. For more information, see [Logging and
monitoring Amazon Location Service with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

**Amazon CloudWatch**

You can use Amazon CloudWatch to collect and analyze metrics related to your Amazon Location Service
account. You can enable CloudWatch alarms to notify you if a metric meets certain
conditions, and has reached a specified threshold. When you create an alarm, CloudWatch
sends a notification to an Amazon Simple Notification Service that you define. For more information, see
the [Monitoring Amazon Location Service with Amazon CloudWatch](monitoring-using-cloudwatch.md "monitoring-using-cloudwatch.md").

**AWS Health Dashboards**

Using [AWS Health
Dashboards](https://status.aws.amazon.com/ "https://status.aws.amazon.com/"), you can verify the status of the Amazon Location Service service. You can
also monitor and view historical data about any events or issues that might affect
your AWS environment. For more information, see the [AWS Health User Guide](../../../health/latest/ug/what-is-aws-health.md "../../../health/latest/ug/what-is-aws-health.md").
