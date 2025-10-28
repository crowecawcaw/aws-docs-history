# Logging and monitoring in MediaTailor

This section provides an overview of the options for logging and monitoring in
AWS Elemental MediaTailor for security purposes. For more information about logging and monitoring
in MediaTailor see [Monitoring and tagging AWS Elemental MediaTailor resources](monitoring.md "monitoring.md").

Monitoring is an important part of maintaining the reliability, availability, and performance of AWS Elemental MediaTailor and your AWS solutions. You
should collect monitoring data from all of the parts of your AWS solution so that you can more easily debug a multi-point failure if one occurs.
AWS provides several tools for monitoring your MediaTailor resources and responding to potential incidents:

## Amazon CloudWatch Alarms

Using CloudWatch alarms, you watch a single metric over a time period that you specify.
If the metric exceeds a given threshold, a notification is sent to an Amazon SNS topic or AWS
Auto Scaling policy. CloudWatch alarms don't invoke actions because they are in a particular
state. Rather, the state must have changed and been maintained for a specified number of
periods. For more information, see [Monitoring AWS Elemental MediaTailor with Amazon CloudWatch
metrics](monitoring-cloudwatch-metrics.md "monitoring-cloudwatch-metrics.md").

## AWS CloudTrail logs

CloudTrail provides a record of actions taken by a user, role, or an AWS service in
AWS Elemental MediaTailor. Using the information collected by CloudTrail, you can determine the request
that was made to MediaTailor, the IP address from which the request was made, who made the
request, when it was made, and additional details. For more information, see [Recording AWS Elemental MediaTailor API calls](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

## AWS Trusted Advisor

Trusted Advisor draws upon best practices learned from serving hundreds of thousands of AWS customers. Trusted Advisor inspects your AWS environment and
then makes recommendations when opportunities exist to save money, improve system availability and performance, or help close security gaps. All
AWS customers have access to five Trusted Advisor checks. Customers with a Business or Enterprise support plan can view all Trusted Advisor
checks.

For more information, see [AWS Trusted Advisor](../../../awssupport/latest/user/getting-started.md#trusted-advisor "../../../awssupport/latest/user/getting-started.md#trusted-advisor").
