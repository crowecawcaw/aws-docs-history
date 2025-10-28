**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Version life

cycle for managed rule groups

Providers handle the following life cycle stages of a managed rule group static version:

- **Release and updates** – A managed rule group
  provider announces upcoming and new static versions of their managed
  rule groups through notifications to an Amazon Simple Notification Service (Amazon SNS) topic.
  Providers might also use the topic to communicate other important
  information about their rule groups, such as urgent required updates.

You can subscribe to the rule group's topic and configure how you want to receive
notifications. For more information see [Getting
notified of new versions and updates](waf-using-managed-rule-groups-sns-topic.md "waf-using-managed-rule-groups-sns-topic.md").

- **Expiration scheduling** – A managed rule group
  provider schedules older versions of a rule group for expiration. A version
  that's scheduled to expire cannot be added to your protection pack (web ACL) rules. After
  expiration is scheduled for a version, AWS WAF tracks the expiration with a
  countdown metric in Amazon CloudWatch.
- **Version expiration** – If you
  have a protection pack (web ACL) configured to use an expired version of a managed rule
  group, then during protection pack (web ACL) evaluation, AWS WAF uses the rule group's
  default version. Additionally, AWS WAF blocks any updates to the protection pack (web ACL)
  that don't either remove the rule group or change its version to an
  unexpired one.
  If you use AWS Marketplace managed rule groups, ask the provider for any additional
  information about version life cycles.
