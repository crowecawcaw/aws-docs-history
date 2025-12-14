**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Adding a managed rule group to a protection pack (web ACL) through

the console

This section explains how to add a managed rule group to a protection pack (web ACL) through the console.
This guidance applies to all AWS Managed Rules rule groups and to the AWS Marketplace rule groups that you're
subscribed to.

###### Production traffic risk

Before you deploy changes in your protection pack (web ACL) for production traffic, test and
tune them in a staging or testing environment until you are comfortable with
the potential impact to your traffic. Then test and tune your updated rules
in count mode with your production traffic before enabling them. For
guidance, see [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").

###### Note

Using more than 1,500 WCUs in a protection pack (web ACL) incurs costs beyond the basic protection pack (web ACL) price. For more information, see [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md "aws-waf-capacity-units.md") and [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

###### To add a managed rule group to a protection pack (web ACL) through the console

###### To add a managed rule group to a web ACL through the console

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. Choose **protection packs (web ACLs)** in the navigation pane.
3. In the **protection packs (web ACLs)** page, from the list of protection packs (web ACLs), select the one
   that you want to add the rule group to. This takes you to the page for
   the single protection pack (web ACL).
4. In your protection pack (web ACL)'s page, choose the **Rules** tab.
5. In the **Rules** pane, choose **Add
   rules**, then choose **Add managed rule
   groups**.
6. In the **Add managed rule groups** page, expand the
   selection for your rule group vendor, to see the list of available rule
   groups.
7. For each rule group that you want to add, choose **Add to protection pack (web ACL)**. If
   you want to change the protection pack (web ACL)'s configuration for the rule group,
   choose **Edit**, make your changes, and then choose
   **Save rule**. For information about the options,
   see the versioning guidance at [Using versioned managed rule groups in AWS WAF](waf-managed-rule-groups-versioning.md "waf-managed-rule-groups-versioning.md") and the guidance for
   using a managed rule group in a protection pack (web ACL) at [Using managed rule group
   statements in AWS WAF](waf-rule-statement-type-managed-rule-group.md "waf-rule-statement-type-managed-rule-group.md").
8. At the bottom of the **Add managed rule groups**
   page, choose **Add rules**.
9. In the **Set rule priority** page, adjust the order
   that the rules run as needed, then choose **Save**.
   For more information, see [Setting rule priority](web-acl-processing-order.md "web-acl-processing-order.md").
   In your protection pack (web ACL)'s page, the managed rule groups that you've added are listed
   under the **Rules** tab.

Test and tune any changes to your AWS WAF protections before you use them for production traffic. For information,
see [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").

###### Temporary inconsistencies during updates

When you create or change a protection pack (web ACL) or other AWS WAF resources, the changes take a small amount of time to propagate to all areas where the resources are stored. The propagation time can be from a few seconds to a number of minutes.

The following are examples of the temporary inconsistencies that you might notice during change propagation:

- After you create a protection pack (web ACL), if you try to associate it with a resource, you might get an exception indicating that the protection pack (web ACL) is unavailable.
- After you add a rule group to a protection pack (web ACL), the new rule group rules might be in effect in one area where the protection pack (web ACL) is used and not in another.
- After you change a rule action setting, you might see the old action in some places and the new action in others.
- After you add an IP address to an IP set that is in use in a blocking rule, the new address might be blocked in one area while still allowed in another.
