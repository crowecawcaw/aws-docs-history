**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Label match rule

statement

This section explains what a label match statement is and how it works.

The label match statement inspects the labels that are on the web request
against a string specification. The labels that are available to a rule for
inspection are those that have already been added to the web request by other
rules in the same protection pack (web ACL) evaluation.

Labels don't persist outside of the protection pack (web ACL) evaluation, but you can access label metrics
in CloudWatch and you can see summaries of label information for any protection pack (web ACL) in the AWS WAF
console. For more information, see [Label metrics and dimensions](waf-metrics.md#waf-metrics-label "waf-metrics.md#waf-metrics-label") and [Monitoring and tuning your AWS WAF protections](web-acl-testing-activities.md "web-acl-testing-activities.md"). You can also see labels in the logs. For information, see [Log fields for protection pack (web ACL) traffic](logging-fields.md "logging-fields.md").

###### Note

A label match statement can only see labels from rules that are evaluated
earlier in the protection pack (web ACL). For information about how AWS WAF evaluates the rules
and rule groups in a protection pack (web ACL), see [Setting rule priority](web-acl-processing-order.md "web-acl-processing-order.md").

For more information about adding and matching labels, see [Web request labeling in AWS WAF](waf-labels.md "waf-labels.md").

## Rule statement

characteristics

**Nestable** – You can nest this statement
type.

**WCUs** – 1 WCU

This statement uses the following settings:

- **Match scope** – Set this to
  **Label** to match against the label name and,
  optionally, the preceding namespaces and prefix. Set this to
  **Namespace** to match against some or all of the
  namespace specifications and, optionally, the preceding prefix.
- **Key** – The string that you want
  to match against. If you specify a namespace match scope, this should
  only specify namespaces and optionally the prefix, with an ending colon.
  If you specify a label match scope, this must include the label name and
  can optionally include preceding namespaces and prefix.

For more information about these settings, see [AWS WAF rules that match labels](waf-rule-label-match.md "waf-rule-label-match.md") and
[AWS WAF label match examples](waf-rule-label-match-examples.md "waf-rule-label-match-examples.md").

## Where to find this rule statement

- **Rule builder** on the console –
  For **Request option**, choose **Has
  label**.
- **API** –
  [LabelMatchStatement](../APIReference/API_LabelMatchStatement.md "../APIReference/API_LabelMatchStatement.md")
