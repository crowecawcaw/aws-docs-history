# Working with stateful rule groups in

AWS Network Firewall

A stateful rule group is a rule group that uses Suricata compatible intrusion
prevention system (IPS) specifications. Suricata is an open source network
IPS that includes a standard rule-based language for stateful network
traffic inspection.

Stateful rule groups have a configurable top-level setting called
`StatefulRuleOptions`, which contains the
`RuleOrder` attribute. You can set this in the console
when you create a rule group, or in the API under
`StatefulRuleOptions`. You can't change the
`RuleOrder` after the rule group is created.

You can enter any stateful rule in Suricata compatible strings. For standard
Suricata rules specifications and for domain list inspection, you can alternately
provide specifications to Network Firewall and have Network Firewall create
the Suricata compatible strings for you.

As needed, depending on the rules that you provide, the stateful engine performs deep packet
inspection (DPI) of your traffic flows. DPI inspects and processes the payload data
within your packets, rather than just the header information.

The rest of this section provides requirements and additional information for
using Suricata compatible rules with Network Firewall.

###### Note

This section and others that describe Suricata-based concepts are not intended to replace or duplicate information from the Suricata documentation.
For more Suricata-specific information, see the [Suricata documentation](https://docs.suricata.io/en/suricata-7.0.8/ "https://docs.suricata.io/en/suricata-7.0.8/").

###### Previous Suricata major version upgrade

When Network Firewall upgrades to a new major version of Suricata, related changes are tracked here.

Network Firewall upgraded from Suricata version 6.0.9 to 7.0 in November of 2024. For full information about the upgrade from version 6.0.9, see
[Upgrading 6.0 to 7.0](https://docs.suricata.io/en/latest/upgrade.html#upgrading-6-0-to-7-0 "https://docs.suricata.io/en/latest/upgrade.html#upgrading-6-0-to-7-0").

The following are examples of the changes in that upgrade:

- PCRE 1 rule format is no longer supported, and has been replaced with PCRE2.
- When you specify a sticky buffer in a rule, it needs to be immediately followed by the payload keywords. For example, keywords such as `dns.query` and `tls.sni` must be followed by a content modifier.
- Keywords that use ranges, such as `itype` now require the range to be specified with the format ``min`:`max``.

###### Topics

- [Creating a stateful rule group](rule-group-stateful-creating.md "rule-group-stateful-creating.md")
- [Updating a stateful rule group](rule-group-stateful-updating.md "rule-group-stateful-updating.md")
- [Deleting a stateful rule group](rule-group-stateful-deleting.md "rule-group-stateful-deleting.md")
- [Managing evaluation order for Suricata compatible rules in AWS Network Firewall](suricata-rule-evaluation-order.md "suricata-rule-evaluation-order.md")
- [Limitations and caveats
  for stateful rules in AWS Network Firewall](suricata-limitations-caveats.md "suricata-limitations-caveats.md")
- [Best practices for writing
  Suricata compatible rules for AWS Network Firewall](suricata-best-practices.md "suricata-best-practices.md")
- [Examples of stateful rules for
  Network Firewall](suricata-examples.md "suricata-examples.md")
