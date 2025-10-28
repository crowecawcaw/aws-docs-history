**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Creating a rule group

To create a new rule group, follow the procedure on this page.

###### To create a rule group

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. In the navigation pane, choose **Rule groups**, and then
   **Create rule group**.
3. Enter a name and description for the rule group. You'll use these to
   identify the rule set to manage it and use it.

Don't use names that start with `AWS`, `Shield`,
`PreFM`, or `PostFM`. These strings are either
reserved or could cause confusion with rule groups that are managed for you
by other services. See [Recognizing rule groups provided by other services](waf-service-owned-rule-groups.md "waf-service-owned-rule-groups.md").

###### Note

You can't change the name after you create the rule group. 4. For **Region**, choose the Region where you want to store the rule
group. To use a rule group in protection packs (web ACLs) that protect Amazon CloudFront distributions,
you must use the global setting. You can use the global setting for regional
applications, too. 5. Choose **Next**. 6. Add
rules to the rule group using the **Rule builder** wizard,
the same as you do in protection pack (web ACL) management. The only difference is that you
can't add a rule group to another rule group. 7. For **Capacity**, set the maximum for the rule group's
use of protection pack (web ACL) capacity units (WCUs). This is an immutable setting. For
information about WCUs, see [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md "aws-waf-capacity-units.md").

As you add rules to the rule group, the **Add rules and set capacity**
pane displays the minimum required capacity, which is based on the rules
that you've already added. You can use this and your future plans for the
rule group to help estimate the capacity that the rule group will require. 8. Review the settings for the rule group, and choose
**Create**.
