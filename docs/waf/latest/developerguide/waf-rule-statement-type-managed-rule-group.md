**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using managed rule group

statements in AWS WAF

This section explains how managed rule group rule statements work.

The managed rule group rule statement adds a reference in your protection pack (web ACL) rules
list to a managed rule group. You don't see this option under your rule
statements on the console, but when you work with the JSON format of your web
ACL, any managed rule groups that you've added show up under the protection pack (web ACL) rules
as this type.

A managed rule group is either an AWS Managed Rules rule group, most of which are free for AWS WAF customers, or
an AWS Marketplace managed rule group. You automatically subscribe to the paid AWS Managed Rules rule groups
when you add them to your protection pack (web ACL). You can subscribe to AWS Marketplace managed rule
groups through AWS Marketplace. For more information, see [Using managed rule groups in AWS WAF](waf-managed-rule-groups.md "waf-managed-rule-groups.md").

When you add a rule group to a protection pack (web ACL), you can override the actions of rules
in the group to Count or to another rule action. For more information,
see [Overriding rule group actions in AWS WAF](web-acl-rule-group-override-options.md "web-acl-rule-group-override-options.md").

You can narrow the scope of the requests that AWS WAF evaluates with the rule
group. To do this, you add a scope-down statement inside the rule group
statement. For information about scope-down statements, see [Using scope-down statements in AWS WAF](waf-rule-scope-down-statements.md "waf-rule-scope-down-statements.md"). This can help you manage
how the rule group affects your traffic and can help you contain costs
associated with traffic volume when you use the rule group. For information and
examples for using scope-down statements with the AWS WAF Bot Control managed rule group,
see [AWS WAF Bot Control](waf-bot-control.md "waf-bot-control.md").

## Rule statement characteristics

**Not nestable** – You can't nest this
statement type inside other statements, and you can't include it in a rule
group. You can include it directly in a protection pack (web ACL).

**(Optional) Scope-down statement** – This
rule type takes an optional scope-down statement, to narrow the scope of the
requests that the rule group evaluates. For more information, see [Using scope-down statements in AWS WAF](waf-rule-scope-down-statements.md "waf-rule-scope-down-statements.md").

**WCUs** – Set for the rule group at
creation.

## Where to find this rule statement

- **Console** – During the process
  of creating a protection pack (web ACL), on the **Add rules and rule
  groups** page, choose **Add managed rule
  groups**, and then find and select the rule group that you
  want to use.
- **API** –
  [ManagedRuleGroupStatement](../APIReference/API_ManagedRuleGroupStatement.md "../APIReference/API_ManagedRuleGroupStatement.md")
