

# Adding AWS managed rule groups to your firewall policy using the console
<a name="nwfw-using-managed-rule-groups-add-to-policy"></a>

Learn how to add one or more managed rule groups to your Network Firewall firewall policy. Adding managed rule groups to your firewall policy automatically implements their built-in protections across your firewall. You can add managed rule groups either through the Network Firewall rule groups page or from your firewall policy's detail page.

**Note**  
Where a managed rule group attaches depends on the policy type. In a *Classic Network Firewall policy*, you add a managed rule group to the policy's **Stateful rule groups** section. In a *Next Generation policy*, the IPS engine evaluates managed rule groups, so you add them to the policy's **IPS rules and packages** section. For information about the policy types, see [AWS Network Firewall firewall policy versions](firewall-policy-versions.md).

------
#### [ Rule groups page ]

**To add one or more managed rule groups to your firewall policy from the rule groups page**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Network Firewall rule groups**.

1. In the **AWS managed rule groups** tab, choose **Add rule groups to policy**.

1. In the **Choose a firewall policy** section, select the firewall policy to add your AWS managed rule groups to.

1. Choose **Next**.

1. In the **Choose rule groups** section, select one or more rule groups to add to your policy. You can add your own rule groups, or AWS managed rule groups.

1. Choose **Next**.

1. (Optional) On the **Add tags** page, enter a key and optional value for any tag that you want to add to this firewall policy. Tags help you organize and manage your AWS resources. For more information about tagging your resources, see [Tagging AWS Network Firewall resources](tagging.md).

1. Choose **Next**.

1. On the **Review and confirm** page, check the rule group settings for your policy. If you want to change any section, choose **Edit** for the section. This returns you to the corresponding step in the add rule group to policy wizard. Make your changes, then choose **Next** on each page until you come back to the review and confirm page.

1. Choose **Add rule groups to policy**.

------
#### [ Firewall policy detail page ]

**To add one or more managed rule groups to your firewall policy from the details page**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Firewall policies**.

1. Choose the name of the policy that you'd like to add one or more AWS managed rule groups to.

1. Add the managed rule groups to the section that the policy evaluates them in:
   + For a *Classic Network Firewall policy*, in the **Stateful rule groups** section, open the **Actions** drop-down menu and select **Add managed stateful rule groups**.
   + For a *Next Generation policy*, choose the **IPS rules and packages** tab, choose **Edit**, choose **Add rule group**, and then choose **Add managed rule group**.

1. Select the AWS managed rule groups to add to your policy.

1. For a Classic policy, choose **Add to policy**. For a Next Generation policy, choose **Next** to finish the edit, then choose **Save**.

------