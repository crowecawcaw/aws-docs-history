# Managing a firewall and firewall endpoints in AWS Network Firewall

This section describes how to create, update, and delete your firewall and its endpoints in AWS Network Firewall.

###### How Network Firewall propagates your changes

When you make any changes to a firewall, including changes to any of the firewall's components, like rule groups, TLS inspection configurations, and firewall policies, Network Firewall propagates the changes everywhere that the firewall is used. Your changes are normally applied within seconds, but there might be a brief period of inconsistency when the changes have arrived in some places and not in others. For example, if you modify a rule group so that it drops an additional type of packet, for a firewall that uses the rule group, the new packet type might briefly be dropped by one firewall endpoint while still being allowed by another.

This temporary inconsistency can occur when you first create a firewall and when you make changes to an existing firewall. Generally, any inconsistencies of this type last only a few seconds.

When you add a TLS inspection configuration to an existing firewall, Network Firewall interrupts traffic flows that match the criteria defined by the TLS inspection configuration scope configuration. Network Firewall will begin SSL/TLS decryption and inspection for new connections to the firewall.

Changes to stateful rules are applied only to new traffic flows. Other firewall changes, including changes to stateless rules, are applied to all network packets.

###### Topics

- [Creating a firewall in AWS Network Firewall](creating-firewall.md "creating-firewall.md")
- [Creating a VPC endpoint association in AWS Network Firewall](creating-vpc-endpoint-association.md "creating-vpc-endpoint-association.md")
- [Updating a firewall in AWS Network Firewall](firewall-updating.md "firewall-updating.md")
- [Deleting a firewall in AWS Network Firewall](deleting-firewall.md "deleting-firewall.md")
- [Deleting a VPC endpoint association in AWS Network Firewall](deleting-vpc-endpoint-association.md "deleting-vpc-endpoint-association.md")
