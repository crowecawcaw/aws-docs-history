# Creating a stateful rule group

This section provides guidance for creating a stateful rule group.

###### To create a stateful rule group

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Network Firewall rule groups**.
3. Choose **Create Network Firewall rule group**.
4. Under **Choose rule group type**, for the
   **Rule group format**, choose **Stateful rule
   group**.

For **Rule evaluation order**, choose the way that your stateful rules are ordered for evaluation:

    * Choose **Strict order** (recommended) to provide your rules in the order that you want them
     to be evaluated. You can then choose one or more default actions for packets that don't match any rules.
    * Choose **Action order** to have the stateful rules engine determine the evaluation order of your rules. The default action for this rule order is **Pass**, followed by **Drop**, **Reject**, and **Alert** actions. This option was previously named **Default** order.

For more information about stateful default actions for rule groups, see
[Action order](suricata-rule-evaluation-order.md#suricata-default-rule-evaluation-order "suricata-rule-evaluation-order.md#suricata-default-rule-evaluation-order").

For more information about stateful rule groups, see
[Working with stateful rule groups in
AWS Network Firewall](stateful-rule-groups-ips.md "stateful-rule-groups-ips.md"). 5. Choose **Next**. 6. Enter a **Name** to identify this rule group.

###### Note

You can't change the name after you create the rule group. 7. (Optional) Enter a **Description** for the rule group to help you identify ot among your other resources. 8. For **Capacity**, set the maximum capacity you want to allow for the
stateful rule group, up to the maximum of 50,000. You can't
change this setting after you create the rule group. For information about
how to calculate this, see [Setting rule group capacity in AWS Network Firewall](nwfw-rule-group-capacity.md "nwfw-rule-group-capacity.md"). For information about the maximum
setting, see [AWS Network Firewall quotas](quotas.md "quotas.md"). 9. Choose **Next**. 10. Select the type of rule group that you want to add, from the **Stateful rule
group options**. The rest of your rule group specifications
depend on the option you choose.

###### Note

If you need to specify options that aren't available through the console,
you can use one of the APIs or AWS CloudFormation. For information, see [StatefulRule](../APIReference/API_StatefulRule.md "../APIReference/API_StatefulRule.md") in the
_AWS Network Firewall API Reference_ and [AWS::NetworkFirewall::RuleGroup StatefulRule](../../../AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.md") in the
_AWS CloudFormation User Guide_.

    * (Option) **Standard stateful rule**
     – Entry form for a basic Suricata
     rule.


    For each rule that you want in your rule
     group, specify the following information and then
     choose **Add rule**. Your added
     rules are listed in the **Rules**
     list.




    	+ Choose the protocol and source and destination settings
    	 for your rule.
    	+ For **Traffic direction**, choose whether
    	 to apply the rule to any direction or only for traffic that
    	 flows forward, from the specified source to the specified
    	 destination.


    	###### Note

    	Network Firewall doesn't automatically add the direction keyword `to_server`, and will inspect all the packets in the flow, irrespective of the flow state.
    	+ For **Action**, select the action that
    	 you want Network Firewall to take when a packet matches the
    	 rule settings. For information on these options, see [Actions for stateful rules](rule-action.md#rule-action-stateful "rule-action.md#rule-action-stateful").
    To define IP sets and ports as variables that you can reference in your rules:





    	+ In the **Rule variables** section, enter variables and values for **IP set variables** and **Port variables**.
    To add one or more references to IP set resources, such as Amazon VPC prefix lists, that you can use as variables in your rules:





    	+ In the **IP set reference** section, enter a **IP set variable
    	 name** and select an **IP set
    	 reference ID**. The **IP set
    	 reference ID** corresponds to the
    	 resource ID of the IP set Amazon Resource Name
    	 (ARN) that you want to reference. Network Firewall
    	 currently supports Amazon VPC prefix lists and resource groups as IP
    	 set references. For more information about working
    	 with IP set references in Network Firewall, see [Referencing Amazon VPC prefix lists](rule-groups-ip-set-references.md#rule-groups-referencing-prefix-lists "rule-groups-ip-set-references.md#rule-groups-referencing-prefix-lists").
    For information about these rules, see
     [Standard
     stateful rule groups in AWS Network Firewall](stateful-rule-groups-basic.md "stateful-rule-groups-basic.md").


    * (Option) **Domain list** – Specify the
     following information.


    ###### Note

    You can create domain list rules from traffic analysis reports.
     For information, see [Creating stateful rule groups from reports](reporting.md#creating-stateful-rule-groups-from-reports "reporting.md#creating-stateful-rule-groups-from-reports").





    	+ For **Domain name source**, enter the domain names that you want to
    	 inspect for, one name specification per line. Valid domain name
    	 specifications are the following:




    		- Explicit names. For example,
    		 `abc.example.com` matches only the
    		 domain `abc.example.com`.
    		- Names that use a domain wildcard, which you
    		 indicate with an initial '`.`'. For
    		 example,`.example.com` matches
    		 `example.com` and matches all
    		 subdomains of `example.com`, such as
    		 `abc.example.com` and
    		 `www.example.com`.
    	+ For **CIDR ranges**, choose whether to inspect default or custom ranges.
    	+ For **Protocols**, choose the protocols
    	 you want to inspect.
    	+ For **Action**, select the list type that
    	 you are creating, either **Allow** or
    	 **Deny**. For information on these
    	 options, see [Actions for stateful rules](rule-action.md#rule-action-stateful "rule-action.md#rule-action-stateful").
    For information about stateful domain name rules, see [Stateful
     domain list rule groups in AWS Network Firewall](stateful-rule-groups-domain-names.md "stateful-rule-groups-domain-names.md").
    * (Option) **Suricata compatible rule string**


    To define IP sets and ports as variables that you can reference in your rules:





    	+ In the **Rule variables** section, enter variables and values for **IP set variables** and **Port variables**.
    To add one or more references to IP set resources, such as Amazon VPC prefix lists, that you can use as variables in your rules:





    	+ In the **IP set reference** section, enter a **IP set variable name** and select an **IP set reference ID**. The **IP set reference ID** corresponds to the resource ID of the IP set Amazon Resource Name (ARN) that you want to reference. Network Firewall currently supports Amazon VPC prefix lists and resource groups as IP set references. For more information about working with IP set references in Network Firewall, see [Referencing Amazon VPC prefix lists](rule-groups-ip-set-references.md#rule-groups-referencing-prefix-lists "rule-groups-ip-set-references.md#rule-groups-referencing-prefix-lists").
    Paste your rules into the text box.

11. Choose **Next**.
12. (Optional) On the **Configure advanced settings** page, under **Customer managed key**, toggle the **Customize encryption settings** option to configure your customer managed key. For more information about this option, see [Encryption at rest with AWS Key Management Service](kms-encryption-at-rest.md "kms-encryption-at-rest.md").
13. Choose **Next**.
14. (Optional) On the **Add tags** page, enter a key and optional value for any
    tag that you want added to this firewall policy. Tags help you organize and
    manage your AWS resources. For more information about tagging your
    resources, see [Tagging AWS Network Firewall resources](tagging.md "tagging.md").
15. Choose **Next**.
16. Review the settings that you've provided for the rule group, then choose **Create
    stateful rule group**.
    Your new rule group is added to the list in the **Network Firewall rule
    groups** page.

To use your rule group in a firewall policy, follow the procedures at [Managing your firewall policy](firewall-policy-managing.md "firewall-policy-managing.md").
