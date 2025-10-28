**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using your rule group in a protection pack (web ACL)

To use a rule group in a protection pack (web ACL), you add it to the protection pack (web ACL) in a rule group reference
statement.

###### Production traffic risk

Before you deploy changes in your protection pack (web ACL) for production traffic, test and
tune them in a staging or testing environment until you are comfortable with the
potential impact to your traffic. Then test and tune your updated rules in count
mode with your production traffic before enabling them. For guidance, see [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").

###### Note

Using more than 1,500 WCUs in a protection pack (web ACL) incurs costs beyond the basic protection pack (web ACL) price. For more information, see [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md "aws-waf-capacity-units.md") and [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

###### To use a rule group

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. In the navigation pane, choose **Rule groups**.
3. Choose the name of the rule group that you want to use.
4. Choose **Add
   rules**, and then choose **Add my own rules and rule
   groups**.
5. Choose **Rule group** and select your
   rule group from the list.
   In your protection pack (web ACL), you can alter the behavior of a rule group and its rules by setting the
   individual rule actions to Count or any other action. This can help you do things like test a rule group,
   identify false positives from rules in a rule group, and customize how a managed
   rule group handles your requests. For more information, see
   [Overriding rule group actions in AWS WAF](web-acl-rule-group-override-options.md "web-acl-rule-group-override-options.md").

If your rule group contains a rate-based statement, each protection pack (web ACL) where you use the
rule group has its own separate rate tracking and management for the rate-based rule, independent
of any other protection pack (web ACL) where you use the rule group. For more information, see [Using rate-based rule statements in AWS WAF](waf-rule-statement-type-rate-based.md "waf-rule-statement-type-rate-based.md").

###### Temporary inconsistencies during updates

When you create or change a protection pack (web ACL) or other AWS WAF resources, the changes take a small amount of time to propagate to all areas where the resources are stored. The propagation time can be from a few seconds to a number of minutes.

The following are examples of the temporary inconsistencies that you might notice during change propagation:

- After you create a protection pack (web ACL), if you try to associate it with a resource, you might get an exception indicating that the protection pack (web ACL) is unavailable.
- After you add a rule group to a protection pack (web ACL), the new rule group rules might be in effect in one area where the protection pack (web ACL) is used and not in another.
- After you change a rule action setting, you might see the old action in some places and the new action in others.
- After you add an IP address to an IP set that is in use in a blocking rule, the new address might be blocked in one area while still allowed in another.
