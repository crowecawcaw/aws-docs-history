

# Creating a stateful rule group

This section provides guidance for creating a stateful rule group.

**To create a stateful rule group**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Network Firewall rule groups**.

1. Choose **Create Network Firewall rule group**. 

1. On the **Describe rule group** page, provide the following information:

   1. Enter a **Name** to identify this rule group.
**Note**  
You can't change the name after you create the rule group.

   1. (Optional) Enter a **Description** for the rule group to help you identify it among your other resources.

   1. (Optional) Under **Customer managed key**, toggle the **Customize encryption settings** option to configure your customer managed key. For more information about this option, see [Encryption at rest with AWS Key Management Service](kms-encryption-at-rest.md).

   1. (Optional) Under **Tags**, enter a key and optional value for any tag that you want added to this rule group. Tags help you organize and manage your AWS resources. For more information about tagging your resources, see [Tagging AWS Network Firewall resources](tagging.md).

1. Choose **Next**.

1. On the **Choose rule group type** page, do the following:

   1. For **Rule group version**, choose **Classic**. To create a rule group for a Next Generation policy instead, see [Creating a rule group for a Next Generation policy](rule-groups-v2-creating.md).

   1. For **Rule group type**, select **Stateful rule group**. To create a stateless rule group, see [Creating a stateless rule group](rule-group-stateless-creating.md).

   1. For **Rule group format**, select **Visual rule builder**, **Text rule builder**, or **Domain list**.

   1. For **Rule evaluation order**, select the way that your stateful rules are ordered for evaluation:
      + Select **Strict order** (recommended) to provide your rules in the order that you want them to be evaluated. You can then select one or more default actions for packets that don't match any rules.
      + Select **Action order** to have the stateful rules engine determine the evaluation order of your rules. The default action for this rule order is **Pass**, followed by **Drop**, **Reject**, and **Alert** actions. This option was previously named **Default** order.

      For more information about stateful default actions for rule groups, see [Action order](suricata-rule-evaluation-order.md#suricata-default-rule-evaluation-order). For more information about stateful rule groups, see [Working with stateful rule groups in AWS Network Firewall](stateful-rule-groups-ips.md).

1. Choose **Next**.

1. (Optional) If you chose **Visual rule builder** or **Text rule builder**, on the **Rule group variables** page, define variables that your rules can reference, then choose **Next**. This page doesn't appear for the **Domain list** format.
   + Under **Rule variables**, enter variables and values for **IP set variables** and **Port variables**.
   + Under **IP set references**, choose **Add IP set reference**, enter an IP set variable name, and select an IP set reference ID. The IP set reference ID corresponds to the resource ID of the IP set Amazon Resource Name (ARN) that you want to reference. Network Firewall supports Amazon VPC managed prefix lists, resource groups, address lists, and container associations as IP set references. For more information, see [Referencing Amazon VPC prefix lists](rule-groups-ip-set-references.md#rule-groups-referencing-prefix-lists).

1. On the **Configure rules** page, add your rules. The available controls depend on the rule group format that you chose.
**Note**  
If you need to specify options that aren't available through the console, you can use one of the APIs or AWS CloudFormation. For information, see [StatefulRule](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_StatefulRule.html) in the *AWS Network Firewall API Reference* and [AWS::NetworkFirewall::RuleGroup StatefulRule](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html) in the *AWS CloudFormation User Guide*.
   + **Visual rule builder** – In the **Standard stateful rules** section, for **Rule template**, select **Custom rule** to build a rule from scratch, or select a template such as **Domain Filtering**, **Geographic IP Filtering**, or **Category matching** to prefill a common rule. Select the **Protocol**. For **Source**, **Source port**, **Destination**, and **Destination port**, keep **Any** or select **Custom** and enter values. For **Action**, select the action that you want Network Firewall to take when a packet matches the rule. For information on these options, see [Actions for stateful rules](rule-action.md#rule-action-stateful). Optionally, expand **Rule options** to review or add Suricata keyword and setting pairs. Choose **Add rule**. The rule appears in the **Rules** table.
**Note**  
Network Firewall doesn't automatically add the direction keyword `to_server`, and inspects all the packets in the flow, irrespective of the flow state.
   + **Text rule builder** – In the **Suricata compatible rule string** section, enter your rules, one rule per line.
   + **Domain list** – For **Domain names**, enter the domain names that you want to inspect for, one name specification per line. Valid domain name specifications are the following:
     + Explicit names. For example, `abc.example.com` matches only the domain `abc.example.com`.
     + Names that use a domain wildcard, which you indicate with an initial '`.`'. For example,`.example.com` matches `example.com` and matches all subdomains of `example.com`, such as `abc.example.com` and `www.example.com`. 

     (Optional) Select **Enable Route 53 Resolved IP validation** to validate destination IP addresses against the domains that Amazon Route 53 resolved. For **CIDR ranges**, select whether to inspect default or custom ranges. For **Protocols**, select the protocols you want to inspect. For **Action**, select **Allow** or **Deny**. For information on these options, see [Actions for stateful rules](rule-action.md#rule-action-stateful).
**Note**  
You can create domain list rules from traffic analysis reports. For information, see [Creating stateful rule groups from reports](reporting.md#creating-stateful-rule-groups-from-reports).

   Under **Capacity**, for **Capacity sizing**, select **Allow room to grow** (recommended), **Match current rules**, or **Custom capacity**, up to the maximum of 50,000. You can't change the capacity after you create the rule group. For information about how to calculate this, see [Setting rule group capacity in AWS Network Firewall](nwfw-rule-group-capacity.md). For information about the maximum setting, see [AWS Network Firewall quotas](quotas.md).

1. Choose **Next**.

1. On the **Review and create** page, review the settings that you've provided for the rule group, and then choose **Create**.

Your new rule group is added to the list in the **Network Firewall rule groups** page.

To use your rule group in a firewall policy, follow the procedures at [Managing your firewall policy](firewall-policy-managing.md).