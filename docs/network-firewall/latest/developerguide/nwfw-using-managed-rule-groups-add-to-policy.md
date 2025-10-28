# Adding AWS managed rule groups to your firewall policy using the console

Learn how to add one or more managed rule groups
to your Network Firewall firewall policy. Adding managed rule groups to your firewall policy
automatically implements their built-in protections across your firewall. You can add managed rule groups
either through the the Network Firewall rule groups page or from your firewall policy's detail page.

Rule groups page

###### To add one or more managed rule groups to your firewall policy from the rule groups page

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Network Firewall rule groups**.
3. In the **AWS managed rule groups** tab, choose **Add rule groups to policy**.
4. In the **Choose a firewall policy** section, select the firewall policy to add your AWS managed rule groups to.
5. Choose **Next**.
6. In the **Choose rule groups** section, choose one or more rule groups to add to your policy. You can add your own rule groups, or AWS managed rule groups.
7. Choose **Next**.
8. (Optional) On the **Add tags** page, enter a key and optional value for any tag that you want to add to this firewall policy. Tags help you organize and manage your AWS resources. For more information about tagging your resources, see [Tagging AWS Network Firewall resources](tagging.md "tagging.md").
9. Choose **Next**.
10. On the **Review and confirm** page, check the rule group settings for your policy. If you want to change any section, choose **Edit** for the section. This returns you to the corresponding step in the add rule group to policy wizard. Make your changes, then choose **Next** on each page until you come back to the review and confirm page.
11. Choose **Add rule groups to policy**.

Firewall policy detail page

###### To add one or more managed rule groups to your firewall policy from the details page

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Firewall policies**.
3. Select the policy that you'd like to add one or more AWS managed rule groups to.
4. In the **Stateful rule groups** section, in the **Actions** drop-down menu, select **Add managed stateful rule groups**.
5. Select the AWS managed rule groups to add to your policy.
6. Choose **Add to policy**.
