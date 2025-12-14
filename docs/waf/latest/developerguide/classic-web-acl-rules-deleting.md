**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Deleting a rule

###### Warning

AWS WAF Classic is is going through a planned end-of-life process. Refer to your AWS Health dashboard for the milestones and dates specific to your Region.

###### Note

This is **AWS WAF Classic** documentation. You should only
use this version if you created AWS WAF
resources, like rules and web ACLs, in AWS WAF prior to November 2019, and you have not
migrated them over to the latest version yet. To migrate your web ACLs, see [Migrating your AWS WAF Classic resources to AWS WAF](waf-migrating-from-classic.md "waf-migrating-from-classic.md").

**For the latest version of AWS WAF**, see [AWS WAF](waf-chapter.md "waf-chapter.md").

If you want to delete a rule, you need to first remove the rule from the web ACLs that are using it
and remove the conditions that are included in the rule.

###### To delete a rule

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/").

If you see **Switch to AWS WAF Classic** in the navigation pane, select it. 2. To remove the rule from the web ACLs that are using it, perform the following steps for each of the web ACLs:

    1. In the navigation pane, choose **Web ACLs**.
    2. Choose the name of a web ACL that is using the rule that you want to delete.


    ###### Note

    If you don't see the web ACL, make sure the Region selection is correct. Web ACLs that protect Amazon CloudFront distributions are in **Global (CloudFront)**.
    3. Choose the **Rules** tab.
    4. Choose **Edit web ACL**.
    5. Choose the **X** to the right of the rule that you want to delete, and then choose **Update**.

3. In the navigation pane, choose **Rules**.
4. Select the name of the rule you want to delete.

###### Note

If you don't see the rule, make sure the Region selection is correct. Rules that protect Amazon CloudFront distributions are in **Global (CloudFront)**. 5. Choose **Delete**.
