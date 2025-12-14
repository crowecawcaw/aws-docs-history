**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Step 3: Create a rule group

###### Warning

AWS WAF Classic is is going through a planned end-of-life process. Refer to your AWS Health dashboard for the milestones and dates specific to your Region.

###### Note

This is **AWS WAF Classic** documentation. You should only
use this version if you created AWS WAF
resources, like rules and web ACLs, in AWS WAF prior to November 2019, and you have not
migrated them over to the latest version yet. To migrate your web ACLs, see [Migrating your AWS WAF Classic resources to AWS WAF](waf-migrating-from-classic.md "waf-migrating-from-classic.md").

**For the latest version of AWS WAF**, see [AWS WAF](waf-chapter.md "waf-chapter.md").

A rule group is a set of rules that defines what actions to take when a particular set of
conditions is met. You can use managed rule groups from AWS Marketplace, and you can create your
own rule groups. For information about managed rule groups, see [AWS Marketplace rule groups](classic-waf-managed-rule-groups.md "classic-waf-managed-rule-groups.md").

To create your own rule group, perform the following procedure.

###### To create a rule group

(console)

1. Sign in to the AWS Management Console using the AWS Firewall Manager administrator account that you
   set up in the prerequisites, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fms](https://console.aws.amazon.com/wafv2/fms "https://console.aws.amazon.com/wafv2/fms").
2. In the navigation pane, choose **Security policies**.
3. If you have not met the prerequisites, the console displays instructions about
   how to fix any issues. Follow the instructions, and then begin this step (create
   a rule group) again. If you have met the prerequisites, choose
   **Close**.
4. Choose **Create policy**.

For **Policy type**, choose **AWS WAF Classic**. 5. Choose **Create an AWS Firewall Manager policy and add a new rule group**. 6. Choose an AWS Region, and then choose **Next**. 7. Because you already created rules, you don't need to create conditions. Choose
**Next**. 8. Because you already created rules, you don't need to create rules. Choose
**Next**. 9. Choose **Create rule group**. 10. For **Name**, enter a friendly name. 11. Enter a name for the CloudWatch metric that AWS WAF Classic will create and will associate with
the rule group. The name can contain only alphanumeric characters (A-Z, a-z,
0-9) or the following special characters: \_-!"#`+\*},./. It can't contain white
space. 12. Select a rule, and then choose **Add rule**. A rule has an action setting
that allows you to choose whether to allow, block, or count requests that match
the rule's conditions. For this tutorial, choose **Count**.
Repeat adding rules until you have added all the rules that you want to the rule
group. 13. Choose **Create**.
You are now ready to go to [Step 4: Create and apply an AWS Firewall ManagerAWS WAF Classic policy](classic-get-started-fms-create-security-policy.md "classic-get-started-fms-create-security-policy.md").
