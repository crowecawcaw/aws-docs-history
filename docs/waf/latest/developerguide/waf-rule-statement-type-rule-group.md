**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using rule group

statements in AWS WAF

This section explains how rule group rule statements work.

The rule group rule statement adds a reference to your protection pack (web ACL) rules list to a
rule group that you manage. You don't see this option under your rule statements
on the console, but when you work with the JSON format of your protection pack (web ACL), any of
your own rule groups that you've added show up under the protection pack (web ACL) rules as this
type. For information about using your own rule groups, see [Managing your own rule groups](waf-user-created-rule-groups.md "waf-user-created-rule-groups.md").

When you add a rule group to a protection pack (web ACL), you can override the actions of rules in the group
to Count or to another rule action. For more information, see [Overriding rule group actions in AWS WAF](web-acl-rule-group-override-options.md "web-acl-rule-group-override-options.md").

## Rule statement characteristics

**Not nestable** – You can't nest this
statement type inside other statements, and you can't include it in a rule
group. You can include it directly in a protection pack (web ACL).

**WCUs** – Set for the rule group at
creation.

## Where to find this rule statement

- **Console** – During the process
  of creating a protection pack (web ACL), on the **Add rules and rule
  groups** page, choose **Add my own rules and rule
  groups**, **Rule group**, and then add the
  rule group that you want to use.
- **API** –
  [RuleGroupReferenceStatement](../APIReference/API_RuleGroupReferenceStatement.md "../APIReference/API_RuleGroupReferenceStatement.md")
