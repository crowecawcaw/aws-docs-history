

# Rule groups for Classic Network Firewall in AWS Network Firewall

Classic Network Firewall policies use stateless rule groups and stateful rule groups. These rule groups determine how Network Firewall evaluates packets in your network traffic inspection. For the rule group types used by Next Generation policies, see [Rule groups for Next Generation policies](rule-groups-v2.md).
+ **Stateless rule groups** – Evaluate packets in isolation. They define standard network connection attributes for examining a packet on its own, without additional context from the broader traffic flow.
+ **Stateful rule groups** – Evaluate packets in the context of traffic flow. They define criteria for examining a packet within the context of its traffic flow and other related traffic. Network Firewall uses a Suricata rules engine to process all stateful rules. You can write any of your stateful rules in Suricata compatible format. Alternatively, for domain list rules and for very basic rules, you can use an easy entry form provided by Network Firewall.

  Stateful rule groups are available in the following categories:
  + **Standard stateful rules** – Defines standard network connection attributes for examining a packet within the context of a traffic flow. For more information, see [Standard stateful rule groups in AWS Network Firewall](stateful-rule-groups-basic.md)
  + **Domain list** – Defines a list of domain names and specifies the protocol type to inspect. You can create these rules from an traffic analysis report. For more information, see [Creating stateful rule groups from reports](reporting.md#creating-stateful-rule-groups-from-reports).
  + **Suricata compatible rule strings** – Provides match and action settings, in Suricata compatible format. You can provide all of your stateful rules through this method if you want to. For more information, see [Suricata compatible rule strings in AWS Network Firewall](stateful-rule-groups-suricata.md).

The following sections describe how to create and manage these rule group types and how Network Firewall evaluates them.

**Topics**
+ [Common rule group settings in AWS Network Firewall](rule-group-settings.md)
+ [Options for stateful rules in Network Firewall](stateful-rule-group-options.md)
+ [Working with stateful rule groups in AWS Network Firewall](stateful-rule-groups-ips.md)
+ [Working with stateless rule groups in AWS Network Firewall](stateless-rule-groups-standard.md)
+ [Defining rule actions in AWS Network Firewall](rule-action.md)
+ [Setting rule group capacity in AWS Network Firewall](nwfw-rule-group-capacity.md)