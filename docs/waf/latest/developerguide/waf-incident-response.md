**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Logging and monitoring in AWS WAF

This section explains how to use AWS tools for monitoring and responding to events in AWS WAF.

Monitoring is an important part of maintaining the reliability, availability, and
performance of AWS WAF and your AWS solutions. You should collect monitoring data from all
parts of your AWS solution so that you can more easily debug a multi-point failure if one
occurs. AWS provides several tools for monitoring your AWS WAF resources and responding to
potential events:

**Amazon CloudWatch alarms**
Using CloudWatch alarms, you watch a single metric over a time period that you specify. If the
metric exceeds a given threshold, CloudWatch sends a notification to an Amazon SNS topic or
AWS Auto Scaling policy. For more information, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

**AWS CloudTrail logs**
CloudTrail provides a record of actions taken by a user, role, or an AWS service in AWS WAF. Using the information collected by CloudTrail, you can determine the request that was made to AWS WAF, the IP address from which the request was made, who made the request, when it was made, and additional details. For more information, see [Logging API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

**AWS WAF protection pack (web ACL) traffic logging**
AWS WAF offers logging for the traffic that your protection packs (web ACLs) analyze. The logs include information such as the time
that AWS WAF received the request from your protected AWS resource, detailed information about the request, and the action
setting for the rule that the request matched. For more information, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md").
