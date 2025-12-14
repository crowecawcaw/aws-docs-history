**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Version expiration

for managed rule groups

This section explains how version expiration works for a versioned managed rule group.

If you use a specific version of a rule group, make sure that you don't keep
using a version past its expiration date. You can monitor version expiration
through the rule group's SNS notifications and through Amazon CloudWatch metrics.

If a version that you're using in a protection pack (web ACL) is expired, AWS WAF blocks any updates to the protection pack (web ACL)
that don't include moving the rule group to an unexpired version.
You can update the rule group to an available version or remove it from your protection pack (web ACL).

Expiration handling for a managed rule group depends on the rule group provider. For
AWS Managed Rules rule groups, an expired version is automatically changed to the rule group's default
version. For AWS Marketplace rule groups, ask the provider how they handle
expiration.

When the provider creates a new version of the rule group, it sets the
version's forecasted lifetime. While the version isn't scheduled to expire, the
Amazon CloudWatch metric value is set to the forecasted lifetime setting, and in CloudWatch, you'll see
a flat value for the metric. After the provider schedules the metric to expire,
the metric value diminishes each day until it reaches zero on the day of
expiration. For information about monitoring expiration,
see [Tracking version
expiration](waf-using-managed-rule-groups-expiration.md "waf-using-managed-rule-groups-expiration.md").
