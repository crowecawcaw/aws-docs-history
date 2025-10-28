**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Editing a rule group

To add or remove rules from a rule group or change configuration settings, access the rule group
using the procedure on this page.

###### Production traffic risk

If you change a rule group that you're currently using in a protection pack (web ACL), those
changes will affect your protection pack (web ACL) behavior wherever it's being used.
Be sure to test and tune all changes in a
staging or testing environment until you are comfortable with the potential
impact to your traffic. Then test and tune your updated rules in count mode with your
production traffic before enabling them. For guidance, see [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").

###### To edit a rule group

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. In the navigation pane, choose **Rule groups**.
3. Choose the name of the rule group that you want to edit. The console takes you to the
   rule group's page.

###### Note

If you don't see the rule group that you want to edit, check the Region selection inside the **Rule groups** section. For rule groups used to protect Amazon CloudFront distributions, use the **Global (CloudFront)** setting. 4. Edit the rule group as needed. You can edit the rule group's mutable properties, similar to
how you did during creation. The console saves your changes as you
go.

###### Note

If you change the name of a rule and you want the rule's metric name to reflect the change, you
must update the metric name as well. AWS WAF doesn't automatically update the metric name for a rule when you change the rule name.
You can change the metric name when you edit the
rule in the console, by using the rule JSON editor. You can also change both names through the APIs and in any JSON listing that you
use to define your protection pack (web ACL) or rule group.

###### Temporary inconsistencies during updates

When you create or change a protection pack (web ACL) or other AWS WAF resources, the changes take a small amount of time to propagate to all areas where the resources are stored. The propagation time can be from a few seconds to a number of minutes.

The following are examples of the temporary inconsistencies that you might notice during change propagation:

- After you create a protection pack (web ACL), if you try to associate it with a resource, you might get an exception indicating that the protection pack (web ACL) is unavailable.
- After you add a rule group to a protection pack (web ACL), the new rule group rules might be in effect in one area where the protection pack (web ACL) is used and not in another.
- After you change a rule action setting, you might see the old action in some places and the new action in others.
- After you add an IP address to an IP set that is in use in a blocking rule, the new address might be blocked in one area while still allowed in another.
