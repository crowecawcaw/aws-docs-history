**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Configuring alarms and

notifications with Shield Advanced and Amazon SNS

This page provides instructions to optionally configure Amazon Simple Notification Service notifications for detected Amazon CloudWatch alarms and rate-based rule
activity. You can use these to receive notification when Shield detects an event on a
protected resource or when a rate-limit configured in a rate-based rule is exceeded.

For information about Shield Advanced CloudWatch metrics, see [AWS Shield Advanced metrics](shield-metrics.md "shield-metrics.md"). For information about Amazon SNS, see the
[Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg.md "../../../sns/latest/dg.md").

###### To configure alarms and notifications

1. Select the Amazon SNS topics that you want notification for. You can use a single Amazon SNS topic
   for all protected resources and rate-based rules, or you can choose
   different topics, customized to your organization. For example, you can
   create an SNS topic for each team that's responsible for incident response
   for a specific set of resources.
2. Choose **Next**. The console wizard advances to the resource protection review page.
