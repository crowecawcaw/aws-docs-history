**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Setting rule priority

This section explains how AWS WAF uses numeric priority settings to set the evaluation order for rules.

In a protection pack (web ACL) and inside any rule group, you determine the evaluation order of the rules using numeric priority settings.
You must give each rule in a protection pack (web ACL) a unique priority setting within that protection pack (web ACL), and you must give each
rule in a rule group a unique priority setting within that rule group.

###### Note

When you manage rule groups, protection packs (web ACLs) through the console, AWS WAF assigns unique numeric priority settings
for you based on the order of the rules in the list. AWS WAF assigns the lowest numeric priority to the
rule at the top of the list, and the highest numeric priority to the rule at the bottom.

When AWS WAF evaluates any rule group, protection pack (web ACL) against a web request, it evaluates the rules
from the lowest numeric priority setting
on up until it either finds a match that terminates the evaluation or exhausts all of the rules.

For example, say you have the following rules and rule groups in your protection pack (web ACL), prioritized
as shown:

- Rule1 – priority 0
- RuleGroupA – priority 100
  - RuleA1 – priority 10,000
  - RuleA2 – priority 20,000

- Rule2 – priority 200
- RuleGroupB – priority 300

      + RuleB1 – priority 0
      + RuleB2 – priority 1

  AWS WAF would evaluate the rules for this protection pack (web ACL) in the following order:

- Rule1
- RuleGroupA RuleA1
- RuleGroupA RuleA2
- Rule2
- RuleGroupB RuleB1
- RuleGroupB RuleB2
