**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Adding and deleting rules from an AWS WAF Classic rule group

###### Warning

AWS WAF Classic is is going through a planned end-of-life process. Refer to your AWS Health dashboard for the milestones and dates specific to your Region.

###### Note

This is **AWS WAF Classic** documentation. You should only
use this version if you created AWS WAF
resources, like rules and web ACLs, in AWS WAF prior to November 2019, and you have not
migrated them over to the latest version yet. To migrate your web ACLs, see [Migrating your AWS WAF Classic resources to AWS WAF](waf-migrating-from-classic.md "waf-migrating-from-classic.md").

**For the latest version of AWS WAF**, see [AWS WAF](waf-chapter.md "waf-chapter.md").

You can add or delete rules in an AWS WAF Classic rule group.

Deleting a rule from the rule group does not delete the rule itself. It only removes
the rule from the rule group.

###### To add or delete rules in a rule group

(console)

1. Sign in to the AWS Management Console using the AWS Firewall Manager administrator
   account that you set up in the prerequisites, and then open the Firewall Manager console at
   [https://console.aws.amazon.com/wafv2/fms](https://console.aws.amazon.com/wafv2/fms "https://console.aws.amazon.com/wafv2/fms").

###### Note

For information about setting up a Firewall Manager administrator account, see [Creating an AWS Firewall Manager default administrator
account](enable-integration.md "enable-integration.md"). 2. In the navigation pane, choose **Switch to AWS WAF Classic**. 3. In the AWS WAF Classic navigation pane, choose **Rule groups**. 4. Choose the rule group that you want to edit.

###### Note

If you don't see the rule group that you want to edit, make sure you have the correct Region selected. For rule groups used to protect Amazon CloudFront distributions, use the **Global (CloudFront)** setting. 5. Choose **Edit rule group**. 6. To add rules, perform the following steps:

    1. Select a rule, and then choose **Add rule to rule
     group**. Choose whether to allow, block, or count requests
     that match the rule's conditions. For more information on the choices,
     see [How AWS WAF Classic works](classic-how-aws-waf-works.md "classic-how-aws-waf-works.md"). Repeat to add more rules to the
     rule group.


    ###### Note

    You cannot add rate-based rules to rule group.
    2. Choose **Update**.

7. To delete rules, perform the following steps:
   1. Choose the **X** next to the rule to delete. Repeat
      to delete more rules from the rule group.
   2. Choose **Update**.
