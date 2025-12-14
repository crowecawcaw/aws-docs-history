**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Tracking a rule group's version

expiration

This section explains how to monitor expiration scheduling for a managed rule group through Amazon CloudWatch.

If you use a specific version of a rule group, make sure that you don't keep
using a version past its expiration date.

###### Tip

Sign up for Amazon SNS notifications for managed rule groups, and keep current with managed
rule group versions. You'll benefit from the most up-to-date protections
from the rule group and stay ahead of expiration. For information, see [Getting
notified of new versions and updates](waf-using-managed-rule-groups-sns-topic.md "waf-using-managed-rule-groups-sns-topic.md").

###### To monitor expiration scheduling for a managed rule group through Amazon CloudWatch

1.  In CloudWatch, locate the expiry metrics from AWS WAF for your managed rule group. The metrics have
    the following metric names and dimensions:

        * Metric name: DaysToExpiry
        * Metric dimensions: Region, ManagedRuleGroup,
         Vendor, and Version

    If you have a managed rule group in your protection pack (web ACL) that's evaluating traffic,
    you will get a metric for it. The metric isn't available for rule groups that you don't use.

2.  Set an alarm on the metrics that you're interested in, so that you're
    notified in time to switch to a newer version of the rule group.
    For information about using Amazon CloudWatch metrics and configuring alarms, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
