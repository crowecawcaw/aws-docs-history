**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Monitoring with Amazon CloudWatch

You can monitor web requests and web ACLs and rules using Amazon CloudWatch, which collects and
processes raw data from AWS WAF and AWS Shield Advanced into readable, near real-time
metrics. You can use statistics in Amazon CloudWatch to gain a perspective on how your web
application or service is performing.

For more information, see [What is
CloudWatch](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md") in the _Amazon CloudWatch User Guide_.

###### Note

CloudWatch metrics and alarms are not enabled for Firewall Manager.

You can create an Amazon CloudWatch alarm that sends an Amazon SNS message when the alarm changes
state. An alarm watches a single metric over a time period that you specify, and
performs one or more actions based on the value of the metric relative to a
specified threshold over a number of time periods. The action is a notification
sent to an Amazon SNS topic or Auto Scaling policy. Alarms invoke actions for sustained state
changes only. CloudWatch alarms do not invoke actions simply because they are in a
particular state; the state must have changed and been maintained for a
specified number of periods.

###### Topics

- [Viewing metrics and dimensions](metrics_dimensions.md "metrics_dimensions.md")
- [AWS WAF metrics and dimensions](waf-metrics.md "waf-metrics.md")
- [AWS Shield Advanced metrics](shield-metrics.md "shield-metrics.md")
- [AWS Firewall Manager notifications](set-fms-alarms.md "set-fms-alarms.md")
