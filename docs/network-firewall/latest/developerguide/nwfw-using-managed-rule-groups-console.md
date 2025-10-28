# Working with AWS managed rule groups in the Network Firewall console

Through the console, you access managed rule group information when you add and edit rules
in your firewall policies. Through the APIs and the command line interface
(CLI), you can directly request managed rule group information.

When you use a managed rule group in your firewall policy, you can edit the following setting:

- **Set rule actions to alert** –
  Managed rule groups are designed to block traffic
  with `drop` rules. This setting in the
  API matches the **Run in alert
  mode** setting in the console. This
  overrides all rule actions in the rule group to
  `alert` instead. This is useful for
  testing
  a rule group before using it to
  control traffic.
  To edit the managed rule group alert settings in your firewall policy:

Console
After you add the managed rule group to your firewall policy, from the **Policies** page, choose the firewall policy you just created. This takes you to the policy detail page where you can edit aspects of the policy, and view details about the policy.

In the **Network Firewall rule groups** tab, in the **Stateful rule groups** section, choose the rule group that you'd like to run in alert mode, then from the **Actions** drop-down menu, choose **Rule group details**. For the **Run in alert mode** setting, toggle to **Enabled** to run the rule group in alert mode.

CLI
Use the [StatefulRuleGroupOverride](../APIReference/API_StatefulRuleGroupOverride.md "../APIReference/API_StatefulRuleGroupOverride.md") setting in a `StatefulRuleGroupReference`.
