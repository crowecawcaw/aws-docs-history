**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using versioned managed rule groups in AWS WAF

This section explains how versioning is handled for managed rule groups.

Many managed rule group providers use versioning to update a rule group's options and capabilities.
Usually, a specific version of a managed rule group is
static. Occasionally, a provider might need to update some or all of the static
versions of a managed rule group, for example, to respond to an emerging security
threat.

When you use a versioned managed rule group in your protection pack (web ACL), you can select the
default version and let the provider manage which static version you use, or you can
select a specific static version.

###### Can't find the version you want?

If you don't see a version in a rule group's version listing, the version is probably
scheduled for expiration or already expired. After a version is scheduled for
expiration, AWS WAF no longer lets you to choose it for the rule group.

###### SNS notifications for AWS Managed Rules rule groups

The AWS Managed Rules rule groups all provide versioning and SNS update notifications except for the
IP reputation rule groups. The AWS Managed Rules rule groups that provide notifications all use the same SNS topic
Amazon Resource Name (ARN). To sign up for SNS notifications, see [Getting
notified of new versions and updates](waf-using-managed-rule-groups-sns-topic.md "waf-using-managed-rule-groups-sns-topic.md").

###### Topics

- [Version life
  cycle for managed rule groups](waf-managed-rule-groups-versioning-lifecycle.md "waf-managed-rule-groups-versioning-lifecycle.md")
- [Version expiration
  for managed rule groups](waf-managed-rule-groups-versioning-expiration.md "waf-managed-rule-groups-versioning-expiration.md")
- [Best practices for handling managed rule group
  versions](waf-managed-rule-groups-best-practice.md "waf-managed-rule-groups-best-practice.md")
