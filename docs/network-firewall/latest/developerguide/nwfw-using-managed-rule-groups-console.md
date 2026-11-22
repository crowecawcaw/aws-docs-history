

# Working with AWS managed rule groups in the Network Firewall console

Through the console, you access managed rule group information when you add and edit rules in your firewall policies. Through the APIs and the command line interface (CLI), you can directly request managed rule group information.

When you use a managed rule group in your firewall policy, you can edit the following setting: 
+ **Set rule actions to alert** – Managed rule groups are designed to block traffic with `drop` rules. This setting in the API matches the **Run in alert mode** setting in the console. This overrides all rule actions in the rule group to `alert` instead. This is useful for testing a rule group before using it to control traffic.

To edit the managed rule group alert settings in your firewall policy:

**Note**  
In a Next Generation policy, managed rule groups are in the policy's **IPS rules and packages** section, so you set the override there rather than in a **Stateful rule groups** section.

------
#### [ Console ]

After you add the managed rule group to your firewall policy, from the **Policies** page, choose the firewall policy you just created. This takes you to the policy detail page where you can edit aspects of the policy, and view details about the policy.

For a Classic Network Firewall policy, in the **Network Firewall rule groups** tab, in the **Stateful rule groups** section, select the rule group that you'd like to run in alert mode, then from the **Actions** drop-down menu, select **Rule group details**. For the **Run in alert mode** setting, toggle to **Enabled** to run the rule group in alert mode.

For a Next Generation policy, choose the **IPS rules and packages** tab, choose **Edit**, and set the rule group's **Override action** to alert mode.

------
#### [ CLI ]

For a Classic Network Firewall policy, use the [StatefulRuleGroupOverride](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_StatefulRuleGroupOverride.html) setting in a `StatefulRuleGroupReference`. For a Next Generation policy, use the override setting on the IPS rule group entry in the policy's IPS section.

------