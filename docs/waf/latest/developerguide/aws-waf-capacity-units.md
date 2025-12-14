**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Web ACL capacity units (WCUs) in AWS WAF

This section explains what web ACL capacity units (WCUs) are and how they work.

AWS WAF uses WCUs to calculate and control the operating
resources that are required to run your rules, rule groups, and web ACLs. AWS WAF enforces WCU
limits when you configure your rule groups and web ACLs. WCUs don't affect
how AWS WAF inspects web traffic.

AWS WAF manages capacity for rules, rule groups, and web ACLs.

###### Rule WCUs

AWS WAF calculates rule capacity when you create or update a rule.
AWS WAF calculates capacity differently for each rule type, to reflect each rule's relative
cost. Simple rules that cost little to run use fewer WCUs than more complex rules
that use more processing power. For example, a size constraint rule statement uses fewer WCUs
than a statement that inspects requests using a regex pattern set.

Rule capacity requirements generally start at a base cost for the rule type and increase with complexity, for example, when you add text transformations before inspection or if you inspect the JSON
body. For information about rule capacity requirements, see the listings for the
rule statements at [Using rule statements in AWS WAF](waf-rule-statements.md "waf-rule-statements.md").

###### Rule group WCUs

The WCU requirements for a rule group are determined by the rules that you define inside the rule group. The maximum capacity for a rule group is 5,000 WCUs.

Each rule group has an immutable capacity setting, which the owner assigns at creation. This is
true for managed rule groups and rule groups that you create through AWS WAF. When
you modify a rule group, your changes must keep the rule group's WCUs within its
capacity. This ensures that protection packs (web ACLs) or web ACLs that are using the rule group remain within
their capacity requirements.

The WCUs that are in use in a rule group is the sum of the WCUs for the rules
minus any processing optimizations that AWS WAF is able to obtain by combining the
behavior of the rules. For example, if you define two rules to examine the same web
request component, and the rules each apply a particular transformation to the
component before inspecting it, AWS WAF might be able to charge you just once for
applying the transformation. The WCU cost to use a rule group in a protection pack (web ACL) is always
the fixed WCU setting that you defined at the rule group creation.

When you create a rule group, take care to set the capacity high enough to accommodate the
rules that you'll want to use throughout the rule group's lifetime.

###### Protection pack or web ACL WCUs

The WCU requirements for a protection pack (web ACL) are determined by the rules and rule groups
that you use inside the protection pack (web ACL).

- The cost of using a rule group in a protection pack (web ACL) is the rule group's capacity
  setting.
- The cost of using a rule is the rule's calculated WCUs minus any
  processing optimizations that AWS WAF is able to obtain from the protection pack (web ACL)'s
  combination of rules. For example, if you define two rules to examine the
  same web request component, and the rules each apply a particular
  transformation to the component before inspecting it, AWS WAF might be able to
  charge you just once for applying the transformation.
  The basic price for a protection pack (web ACL) includes up to 1,500 WCUs. Using more
  than 1,500 WCUs incurs additional fees, according to a tiered pricing
  model. AWS WAF automatically adjusts your protection pack (web ACL) pricing as your protection pack (web ACL) WCU usage
  changes. For pricing details, see [AWS WAF
  Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

The maximum capacity for a protection pack (web ACL) is 5,000 WCUs.

## Determining the WCUs for a rule group, protection pack (web ACL), or web ACL

As noted in prior sections, the total WCUs used in a rule group, protection pack (web ACL), or web ACL will be equal
to _or less than_ the sum of the WCUs for all of the rules
that are defined in the rule group, protection pack (web ACL), or web ACL.

In the AWS WAF console, you can see the capacity consumed when you add rules to your
protection pack (web ACL), web ACL, or rule group. The console displays the current capacity units used as you
add the rules.

Through the API, you can check the maximum capacity requirements for the rules that you
want to use in a protection pack (web ACL), web ACL, or rule group. To do this, provide the JSON listing of the
rules to the check capacity call. For more information, see [CheckCapacity](../APIReference/API_CheckCapacity.md "../APIReference/API_CheckCapacity.md") in the _AWS WAFV2 API Reference_.
