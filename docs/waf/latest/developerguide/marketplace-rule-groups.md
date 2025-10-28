**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# AWS Marketplace rule groups

This section explains how to use AWS Marketplace rule groups.

AWS Marketplace rule groups are available by subscription through the AWS Marketplace console at
[AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace"). After you subscribe to an AWS Marketplace rule group, you can use it in
AWS WAF. To use an AWS Marketplace rule group in an AWS Firewall Manager AWS WAF policy, each account in your
organization must subscribe to it.

###### You can subscribe to different types of rule groups through AWS Marketplace:

- AWS WAF partner-managed rule groups
- Client-side protections
  Test and tune any changes to your AWS WAF protections before you use them for production traffic. For information,
  see [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").

###### AWS Marketplace Rule Group Pricing

AWS Marketplace rule groups are available with no long-term contracts, and no minimum
commitments. When you subscribe to a rule group, you are charged a monthly fee (prorated
hourly) and ongoing request fees based on volume. For more information, see
[AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/") and the description
for each AWS Marketplace rule group at [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace").

###### Have questions about an AWS Marketplace rule group?

For questions about a rule group that's managed by an AWS Marketplace seller and to request changes
in functionality, contact the provider's customer support team. To find contact
information, see the provider's listing at [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace").

The AWS Marketplace rule group provider determines how to manage the rule group, for example how to
update the rule group and whether the rule group is versioned. The provider also
determines the details of the rule group, including the rules, rule actions, and any
labels that the rules add to matching web requests.

## Subscribing to AWS Marketplace rule groups

You can subscribe to and unsubscribe from AWS Marketplace rule groups on the AWS WAF console.

###### Important

To use an AWS Marketplace rule group in an AWS Firewall Manager policy, each account in your organization must
first subscribe to that rule group.

###### To subscribe to an AWS Marketplace rule group

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. In the navigation pane, choose **Add-on protections**.
3. In the **AWS Marketplace** section, choose the name of a
   rule group to view the details and pricing information.

###### Tip

Use the filters to quickly sort for the rules you're most interested in. For example, you can use the
**Category** filter to view client-side protections only. 4. To subscribe to an AWS Marketplace rule group:

    1. Navigate to a rule group, then choose **Subscribe via Marketplace**.
    2. In the Marketplace page that opens, choose **View purchase options**, then choose **Subscribe**.###### Note

If you decide not to subscribe to the rule group, simply close the pop-up.

After you're subscribed to an AWS Marketplace rule group, you use it in your protection packs (web ACLs) as you do other
managed rule groups. For information, see [Creating a protection pack (web ACL) in AWS WAF](web-acl-creating.md "web-acl-creating.md").

When adding a rule group to a protection pack (web ACL), you can override the actions of rules in the rule group
and of the rule group result. For more information, see [Overriding rule group actions in AWS WAF](web-acl-rule-group-override-options.md "web-acl-rule-group-override-options.md").

## Unsubscribing from AWS Marketplace rule groups

You can unsubscribe from AWS Marketplace rule groups on the AWS Marketplace console.

###### Important

To stop the subscription charges for an AWS Marketplace rule group, you must
remove it from all protection packs (web ACLs) in AWS WAF and in any Firewall Manager AWS WAF policies, in addition to unsubscribing from it.
If you unsubscribe from an AWS Marketplace rule group but don't remove it from your protection packs (web ACLs),
you will continue to be charged for the subscription.

###### To unsubscribe from an AWS Marketplace rule group

1. Remove the rule group from all protection packs (web ACLs). For more information, see [Editing a protection pack (web ACL) in AWS WAF](web-acl-editing.md "web-acl-editing.md").
2. Open the AWS console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace "https://console.aws.amazon.com/marketplace").

The **Manage subscriptions page appears**. 3. Open the **Delivery method** list and choose **SaaS**. 4. Under **Agreement**, open the **Actions list** and choose
**Cancel subscription** next to the name of the rule group that you want to
unsubscribe from. 5. In the **Cancel subscription** dialog box, enter `confirm`, then choose
**Yes, cancel subscription**.

## Troubleshooting AWS Marketplace rule groups

If you find that an AWS Marketplace rule group is blocking legitimate traffic, you can troubleshoot the problem by performing
the following steps.

###### To troubleshoot an

AWS Marketplace rule group

1. Override the actions to count for the rules that are blocking legitimate traffic. You can
   identify which rules are blocking specific requests using either the
   AWS WAF sampled requests or AWS WAF logs. You can identify the rules by
   looking at the `ruleGroupId` field in the log or the
   `RuleWithinRuleGroup` in the sampled request. You can
   identify the rule in the pattern `<Seller Name>#<RuleGroup
Name>#<Rule Name>`.
2. If setting specific rules to only count requests doesn't solve the problem, you can
   override all of the rule actions or change the action for the AWS Marketplace rule
   group itself from **No override** to **Override
   to count**. This allows the web request to pass through,
   regardless of the individual rule actions within the rule group.
3. After overriding either the individual rule action or the entire AWS Marketplace rule group action,
   contact the rule group provider‘s customer support team to further
   troubleshoot the issue. For contact information, see the rule group
   listing on the product listing pages on AWS Marketplace.

### Contacting AWS support

For problems with AWS WAF or a rule group that is managed by AWS, contact AWS Support. For
problems with a rule group that is managed by an AWS Marketplace seller, contact the
provider's customer support team. To find contact information, see the
provider's listing on AWS Marketplace.
