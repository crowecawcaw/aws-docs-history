**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Deleting a Web ACL

###### Warning

AWS WAF Classic is is going through a planned end-of-life process. Refer to your AWS Health dashboard for the milestones and dates specific to your Region.

###### Note

This is **AWS WAF Classic** documentation. You should only
use this version if you created AWS WAF
resources, like rules and web ACLs, in AWS WAF prior to November 2019, and you have not
migrated them over to the latest version yet. To migrate your web ACLs, see [Migrating your AWS WAF Classic resources to AWS WAF](waf-migrating-from-classic.md "waf-migrating-from-classic.md").

**For the latest version of AWS WAF**, see [AWS WAF](waf-chapter.md "waf-chapter.md").

###### Important

Deleting a web ACL is permanent and can't be undone. If the selected web ACL contains any rules or is associated with any CloudFront distributions,
Application load balancer or API Gateway, remove the rules and associations before deleting. Otherwise, the delete will fail.

To delete a web ACL, you must remove the rules that are included in the web ACL and
disassociate all CloudFront distributions and
Application
Load Balancers from the web ACL. Perform the following
procedure.

###### To delete a web ACL

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/").

If you see **Switch to AWS WAF Classic** in the navigation pane, select it. 2. In the navigation pane, choose **Web ACLs**. 3. Choose the name of the web ACL that you want to delete. This opens a page with the web ACL's details in the right pane.

###### Note

If you don't see the web ACL, make sure the Region selection is correct. Web ACLs that protect Amazon CloudFront distributions are in **Global (CloudFront)**. 4. On the **Rules** tab in the right pane, choose **Edit web ACL**. 5. To remove all rules from the web ACL, choose the **x** at the right of the
row for each rule. This doesn't delete the rules from AWS WAF Classic, it just removes
the rules from this web ACL. 6. Choose **Update**. 7. Disassociate the web ACL from all CloudFront distributions and
Application
Load Balancers. On the **Rules** tab,
under **AWS resources using this web ACL**, choose the
**x** for each API Gateway API, CloudFront distribution or Application Load Balancer. 8. On the **Web ACLs** page, confirm that the web ACL that you want to delete is
selected, and then choose **Delete**.
