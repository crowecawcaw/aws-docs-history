

# Managing your own rule groups in AWS Network Firewall

A Network Firewall *rule group* is a reusable set of criteria for inspecting and handling network traffic. You add one or more rule groups to a firewall policy as part of policy configuration. For more information about firewall policies and firewalls, see [Firewall policies](firewall-policies.md) and [Firewalls and firewall endpoints](firewalls.md).

You can use your own rule groups and you can use rule groups that are managed for you by AWS. For information on managed rule groups, see [Using managed rule groups](nwfw-managed-rule-groups.md).

The rule group types you use depend on the type of firewall policy you add them to:
+ **Next Generation policies (recommended)** – Use *firewall engine* rule groups and *IPS engine* rule groups. A Next Generation policy is recommended for new firewalls. For more information, see [Rule groups for Next Generation policies](rule-groups-v2.md).
+ **Classic Network Firewall policies** – Use *stateless* rule groups and *stateful* rule groups, which remain fully supported. For more information, see [Rule groups for Classic Network Firewall](rule-groups-classic.md).

For information about the policy types, see [AWS Network Firewall firewall policy versions](firewall-policy-versions.md).

Depending on the type of rule group, you might also define rules inside the rule group. Rules provide detailed criteria for packet inspection and specify what to do when a packet matches the criteria. When Network Firewall finds a match between the criteria and a packet, we say that the packet matches the rule group.

Follow the guidance in this section to manage your AWS Network Firewall rule groups. 

**Note**  
This section and others that describe Suricata-based concepts are not intended to replace or duplicate information from the Suricata documentation. For more Suricata-specific information, see the [Suricata documentation](https://docs.suricata.io/en/suricata-8.0.3/).

**Topics**
+ [Rule groups for Next Generation policies in AWS Network Firewall](rule-groups-v2.md)
+ [Rule groups for Classic Network Firewall in AWS Network Firewall](rule-groups-classic.md)
+ [Limitations and caveats for stateful rules in AWS Network Firewall](suricata-limitations-caveats.md)
+ [Best practices for writing Suricata compatible rules for AWS Network Firewall](suricata-best-practices.md)