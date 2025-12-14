**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# AWS WAF rules that match labels

This section explains how to use a label match statement to evaluate web request labels. You can match against
_Label_, which requires the label name, or against
_Namespace_, which requires a namespace specification. For
either label or namespace, you can optionally include preceding namespaces and the
prefix in your specification. For general information about this statement type, see
[Label match rule
statement](waf-rule-statement-type-label-match.md "waf-rule-statement-type-label-match.md").

A label's prefix defines the context of the rule group or protection pack (web ACL) where the label's rule is
defined. In a rule's label match statement, if your label or namespace match string
doesn't specify the prefix, AWS WAF uses the prefix for the label match rule.

- Labels for rules that are defined directly inside a protection pack (web ACL) have a prefix
  that specifies the protection pack (web ACL) context.
- Labels for rules that are inside a rule group have a prefix that specifies the rule group
  context. This could be your own rule group or a rule group that's managed
  for you.
  For information about this, see label syntax under [Label syntax and naming requirements in AWS WAF](waf-rule-label-requirements.md "waf-rule-label-requirements.md").

###### Note

Some managed rule groups add labels. You can retrieve these through the API by calling `DescribeManagedRuleGroup`. The labels are listed in the `AvailableLabels` property in the response.

If you want to match against a rule that's in a different context than the context of your
rule, you must provide the prefix in your match string. For example, if you want to
match against labels that are added by rules in a managed rule group, you could add
a rule in your protection pack (web ACL) with a label match statement whose match string specifies the
rule group's prefix followed by your additional match criteria.

In the match string for the label match statement, you specify either a label or a
namespace:

- **Label** – The label specification for a match
  consists of the ending part of the label. You can include any number of the
  contiguous namespaces that immediately precede the label name followed by
  the name. You can also provide the fully qualified label by starting the
  specification with the prefix.

Example specifications:

    + `testNS1:testNS2:LabelNameA`
    + `awswaf:managed:aws:managed-rule-set:testNS1:testNS2:LabelNameA`

- **Namespace** – The namespace
  specification for a match consists of any contiguous subset of the label
  specification excluding the name. You can include the prefix and you can
  include one or more namespace strings.

Example specifications:

    + `testNS1:testNS2:`
    + `awswaf:managed:aws:managed-rule-set:testNS1:`
