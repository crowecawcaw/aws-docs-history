**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Getting notified of new

versions and updates to a managed rule group

This section explains how to receive Amazon SNS notifications of new
versions and updates.

A managed rule group provider uses SNS notifications to announce rule group changes, like upcoming new
versions and urgent security updates.

###### How to subscribe to SNS notifications

To subscribe to notifications for a rule group, you create an Amazon SNS subscription for the
rule group's Amazon SNS topic ARN in the US East (N. Virginia) Region us-east-1.

For information about how to subscribe, see the [Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg.md "../../../sns/latest/dg.md").

###### Note

Create your subscription for the SNS topic only in the us-east-1 Region.

The versioned AWS Managed Rules rule groups all use the same SNS topic Amazon Resource Name (ARN).
For more information about AWS Managed Rules rule group notifications, see [Deployment notifications](waf-managed-rule-groups-deployments-notifications.md "waf-managed-rule-groups-deployments-notifications.md").

###### Where to find the Amazon SNS topic ARN for a managed rule group

AWS Managed Rules rule groups use a single SNS topic ARN, so you can retrieve the topic ARN from one of the
rule groups and subscribe to it to get notifications for all of the AWS Managed Rules rule groups
that provide SNS notifications.

- **Console**
  - (Option) When you add the managed rule group to your protection pack (web ACL), choose
    **Edit** to see the rule group's
    information, which includes the rule group's Amazon SNS topic ARN.
  - (Option) After you've added the managed rule group into your protection pack (web ACL), choose
    **Edit** on the protection pack (web ACL), and then select
    and edit the rule group rule to see the rule group's Amazon SNS topic
    ARN.

- **API** –
  `DescribeManagedRuleGroup`
- **CLI** – `aws wafv2
 describe-managed-rule-group --scope=<CLOUDFRONT|REGIONAL> --vendor-name <vendor>
 --name <managedrule_name>`
  For general information about Amazon SNS notification formats and how to filter the
  notifications that you receive, see
  [Parsing message formats](../../../sns/latest/dg/sns-message-and-json-formats.md "../../../sns/latest/dg/sns-message-and-json-formats.md") and
  [Amazon SNS subscription filter policies](../../../sns/latest/dg/sns-subscription-filter-policies.md "../../../sns/latest/dg/sns-subscription-filter-policies.md")
  in the Amazon Simple Notification Service Developer Guide.
