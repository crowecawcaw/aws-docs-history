# Options for stateful rules in Network Firewall

A stateful rule group is a rule group that uses Suricata compatible intrusion
prevention system (IPS) specifications. Suricata is an open source network
IPS that includes a standard rule-based language for stateful network
traffic inspection.

When you create a Network Firewall stateful rule group from Suricata compatible rules, you can
provide the rules to the rule group creation operation in one of the following ways:

- **Standard, simple rule group specification** – With this option, Network Firewall translates your
  specification into Suricata compatible rules and
  then passes the resulting rule strings to Suricata
  for processing.
- **Domain list rule specification** – With this option, Network Firewall translates your rule
  specification into Suricata compatible rules and
  then passes the resulting rule strings to Suricata
  for processing.
- **Rule strings that are written in Suricata compatible syntax** –
  When you use this option, Network Firewall passes your rule strings to Suricata for processing.
  The sections that follow provide details for each of these options.

###### Topics

- [Standard
  stateful rule groups in AWS Network Firewall](stateful-rule-groups-basic.md "stateful-rule-groups-basic.md")
- [Suricata compatible rule strings in
  AWS Network Firewall](stateful-rule-groups-suricata.md "stateful-rule-groups-suricata.md")
- [Stateful
  domain list rule groups in AWS Network Firewall](stateful-rule-groups-domain-names.md "stateful-rule-groups-domain-names.md")
- [IP set references in Suricata compatible AWS Network Firewall rule groups](rule-groups-ip-set-references.md "rule-groups-ip-set-references.md")
- [Geographic IP filtering in Suricata compatible AWS Network Firewall rule groups](rule-groups-geo-ip-filtering.md "rule-groups-geo-ip-filtering.md")
