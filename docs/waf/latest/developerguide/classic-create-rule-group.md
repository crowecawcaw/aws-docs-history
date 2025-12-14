**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Creating an AWS WAF Classic rule group

###### Warning

AWS WAF Classic is is going through a planned end-of-life process. Refer to your AWS Health dashboard for the milestones and dates specific to your Region.

###### Note

This is **AWS WAF Classic** documentation. You should only
use this version if you created AWS WAF
resources, like rules and web ACLs, in AWS WAF prior to November 2019, and you have not
migrated them over to the latest version yet. To migrate your web ACLs, see [Migrating your AWS WAF Classic resources to AWS WAF](waf-migrating-from-classic.md "waf-migrating-from-classic.md").

**For the latest version of AWS WAF**, see [AWS WAF](waf-chapter.md "waf-chapter.md").

When you create an AWS WAF Classic rule group to use with AWS Firewall Manager, you specify which rules to add to
the group.

###### To create a rule group (console)

1. Sign in to the AWS Management Console using the AWS Firewall Manager administrator
   account that you set up in the prerequisites, and then open the Firewall Manager console at
   [https://console.aws.amazon.com/wafv2/fms](https://console.aws.amazon.com/wafv2/fms "https://console.aws.amazon.com/wafv2/fms").

###### Note

For information about setting up a Firewall Manager administrator account, see [Creating an AWS Firewall Manager default administrator
account](enable-integration.md "enable-integration.md"). 2. In the navigation pane, choose **Switch to AWS WAF Classic**. 3. In the AWS WAF Classic navigation pane, choose **Rule groups**. 4. Choose **Create rule group**.

###### Note

You can't add rate-based rules to a rule group. 5. If you have already created the rules that you want to add to the rule group,
choose **Use existing rules for this rule group** . If you want
to create new rules to add to the rule group, choose **Create rules and
conditions for this rule group**. 6. Choose **Next**. 7. If you chose to create rules, follow the steps to create them at [Creating a rule and adding conditions](classic-web-acl-rules-creating.md "classic-web-acl-rules-creating.md").

###### Note

Use the AWS WAF Classic console to create your rules.

When you've created all the rules you need, go to the next step. 8. Type a rule group name. 9. To add a rule to the rule group, select a rule then choose **Add
rule**. Choose whether to allow, block, or count requests that
match the rule's conditions. For more information on the choices, see [How AWS WAF Classic works](classic-how-aws-waf-works.md "classic-how-aws-waf-works.md"). 10. When you are finished adding rules, choose **Create**.
You can test your rule group by adding it to an AWS WAF WebACL and setting the
WebACL action to **Override to Count**. This action overrides any
action that you choose for the rules contained in the group, and only counts matching
requests. For more information, see [Creating a Web ACL](classic-web-acl-creating.md "classic-web-acl-creating.md").
