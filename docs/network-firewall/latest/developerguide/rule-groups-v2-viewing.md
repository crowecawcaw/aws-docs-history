

# Viewing your rule groups in AWS Network Firewall
<a name="rule-groups-v2-viewing"></a>

The **Network Firewall rule groups** page lists the rule groups that you can use, organized into two tabs.

**Your rule groups**  
The rule groups that you created. This tab opens by default. It lists each rule group with the following columns:  
+ **Name** – The name of the rule group.
+ **Rule group version** – **Classic** or **Next Generation**.
+ **Type** – For a Classic rule group, **Stateless** or **Stateful**. For a Next Generation rule group, **Firewall** or **IPS**.
+ **Rule order** – For a Classic stateful rule group, **Action order** or **Strict order**. For a Next Generation rule group, the console shows **-**, because rule order isn't a setting you choose for these rule groups: firewall rules are always evaluated in a strict order (by hook and priority), and IPS rules are always evaluated in action order.
+ **Capacity** – The capacity setting of the rule group.

**AWS managed rules**  
The managed rule groups that AWS writes and maintains for you. This tab has a **Domain and IP rule groups** section (with the columns **Name**, **Description**, **Capacity**, and **Rule order**) and a **Threat signature rule groups** section (with the columns **Name**, **Description**, **Capacity**, **Rule order**, and **Last updated**). For more information, see [Using managed rule groups](nwfw-managed-rule-groups.md).

To view a rule group's details, select the rule group's checkbox to open a details pane at the bottom of the page, or choose the rule group's name to open its details page. The details that you see match the rule group's type. Every section has an **Edit** button that you use to change that section's settings.

Every rule group starts with a **Rule details** section that shows the **Name**, **Description**, **Engine**, **ARN**, **Use count**, and **Status**. The sections that follow depend on the rule group type:

Classic stateful rule group  
Shows a **Rule variables** section, an **IP set references** section, a **Rules** section (the rules in text form), a **Customer managed key** section, and a **Tags** section.

IPS rule group  
Shows a **Rule variables** section, an **IP set references** section, an **IPS signatures** section, a **Customer managed key** section, and a **Tags** section. The **IPS signatures** section shows each signature's description and its signature (the rule string). When you edit this section, the console opens a text box where you add, change, or remove signatures.

Firewall rule group  
Shows a **Rule variables** section, a **Firewall rules** section, and a **Tags** section. The **Firewall rules** section shows each signature's description and its signature (the rule string). When you edit this section, the console opens a text box where you add, change, or remove firewall rule signatures.

Firewall domain list rule group  
Shows a **Domain list** section, a **Customer managed key** section, and a **Tags** section. The **Domain list** section shows the **Action**, **Protocols**, **Route 53 Resolved IP validation** (**Enabled** or **Disabled**), and **Source IPs** (**Default** unless you set specific ranges), and lists the domains with a search box. When you edit this section, the console opens a page where you can change the domain names, turn **Route 53 Resolved IP validation** on or off, choose **Default** or **Custom** CIDR ranges (and enter the ranges for **Custom**), select the **HTTP** and **HTTPS** protocols, and confirm the **Action**, which is **Allow**—the only action available for a firewall engine domain list.

You can also select an AWS managed rule group to view its details.

**Note**  
When you describe a firewall rule group with the API or AWS CLI, you can request its rules in either form—as modeled rules or as rule strings—regardless of the format you used to create the rule group. Network Firewall converts between the two forms and preserves each rule's behavior, so you can author in one format and read back in the other. For example, you can create a rule group from rule strings and later describe it as modeled rules, or create it with the visual rule builder (modeled rules) and describe it as rule strings. The conversion preserves rule behavior but isn't byte-for-byte lossless. For more information about the two forms, see [Authoring firewall rules](firewall-rule-groups-authoring.md).