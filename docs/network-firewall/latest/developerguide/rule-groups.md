# Managing your own rule groups in AWS Network Firewall

A Network Firewall _rule group_ is a reusable set of criteria for
inspecting and handling network traffic. You add one or more rule groups to a firewall
policy as part of policy configuration. For more information about firewall policies and
firewalls, see [Firewall policies](firewall-policies.md "firewall-policies.md") and
[Firewalls and firewall endpoints](firewalls.md "firewalls.md").

You can use your own rule groups and you can use rule groups that are managed for you by AWS. For information on managed rule groups,
see [Using managed rule groups](nwfw-managed-rule-groups.md "nwfw-managed-rule-groups.md").

Network Firewall rule groups are either _stateless_ or
_stateful_. These rule groups determine how packets are evaluated in your network traffic inspection.

Stateless rule groups
Stateless rule groups evaluate packets in isolation. They define standard network connection attributes for examining a packet on its own, without additional context from the broader traffic flow.

Stateful rule groups
Stateful rule groups evaluate packets in the context of traffic flow. They define criteria for examining a packet within the context of its traffic flow and other related traffic.

Network Firewall uses a Suricata rules engine to process all stateful rules. You can write any of your stateful rules in Suricata compatible format. Alternatively, for domain list rules and for very basic rules, you can use an easy entry form provided by Network Firewall.

Stateful rule groups are available in the following categories:

- **Standard stateful rules** – Defines standard network connection attributes for examining a packet within the context of a traffic flow.
  For more information,
  see [Standard
  stateful rule groups in AWS Network Firewall](stateful-rule-groups-basic.md "stateful-rule-groups-basic.md")
- **Domain list** – Defines a list of domain names and specifies the protocol type to inspect.
  You can create these rules from an traffic analysis report.
  For more information, see [Creating stateful rule groups from reports](reporting.md#creating-stateful-rule-groups-from-reports "reporting.md#creating-stateful-rule-groups-from-reports").
- **Suricata compatible rule strings** – Provides match and action settings, in Suricata compatible format.
  You can provide all of your stateful rules through this method if you want to. For more information,
  see [Suricata compatible rule strings in
  AWS Network Firewall](stateful-rule-groups-suricata.md "stateful-rule-groups-suricata.md").

Depending on the type of rule group, you might also define rules inside the rule group.
Rules provide detailed criteria for packet inspection and specify what to do when a packet
matches the criteria. When Network Firewall finds a match between the criteria and a packet, we
say that the packet matches the rule group.

Follow the guidance in this section to manage your AWS Network Firewall rule groups.

###### Note

This section and others that describe Suricata-based concepts are not intended to replace or duplicate information from the Suricata documentation.
For more Suricata-specific information, see the [Suricata documentation](https://docs.suricata.io/en/suricata-7.0.8/ "https://docs.suricata.io/en/suricata-7.0.8/").

###### Topics

- [Common rule group settings in AWS Network Firewall](rule-group-settings.md "rule-group-settings.md")
- [Options for stateful rules in Network Firewall](stateful-rule-group-options.md "stateful-rule-group-options.md")
- [Working with stateful rule groups in
  AWS Network Firewall](stateful-rule-groups-ips.md "stateful-rule-groups-ips.md")
- [Working with stateless rule groups in
  AWS Network Firewall](stateless-rule-groups-standard.md "stateless-rule-groups-standard.md")
- [Defining rule actions in AWS Network Firewall](rule-action.md "rule-action.md")
- [Setting rule group capacity in AWS Network Firewall](nwfw-rule-group-capacity.md "nwfw-rule-group-capacity.md")
