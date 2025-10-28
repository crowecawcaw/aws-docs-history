# Firewalls and firewall endpoints in AWS Network Firewall

A Network Firewall _firewall_ defines the behavior of a network firewall, specifies the primary VPC it protects,
and determines the Availability Zones where it can be deployed. For each Availability Zone where you want to use the firewall,
you must define one subnet to serve as a _firewall endpoint_ in the firewall's configuration.
These are the primary endpoints for your firewall.

To extend your firewall's capabilities, you can create additional, or secondary, firewall endpoints using _VPC endpoint associations_.
These associations let you deploy firewall endpoints in VPCs other than the primary protected VPC and create multiple firewall
endpoints within a single Availability Zone in the firewall owner's account or other accounts with which the firewall has been shared.
For information about sharing firewalls with other accounts, see [Sharing Network Firewall resources](sharing.md "sharing.md").

You can create VPC endpoint associations for any VPC, but only in Availability Zones where the firewall already has a primary endpoint defined.
For details about creating these associations, see [Creating a VPC endpoint association](creating-vpc-endpoint-association.md "creating-vpc-endpoint-association.md").

This guide shows you how to create, manage, and troubleshoot firewalls and their endpoints, whether you're working with primary firewall endpoints or VPC endpoint associations.

###### Topics

- [Considerations for working with firewalls and firewall endpoints](firewall-and-firewall-endpoints-considerations.md "firewall-and-firewall-endpoints-considerations.md")
- [Firewall settings in AWS Network Firewall](firewall-settings.md "firewall-settings.md")
- [Understanding the differences between firewall owners and VPC endpoint association owners](firewall-owners-and-vpc-endpoint-association-owners.md "firewall-owners-and-vpc-endpoint-association-owners.md")
- [Managing a firewall and firewall endpoints in AWS Network Firewall](firewall-managing.md "firewall-managing.md")
- [Transit gateway-attached firewalls in Network Firewall](tgw-firewall.md "tgw-firewall.md")
- [Managing your firewall state table using flow operations in AWS Network Firewall](firewall-flow-operations.md "firewall-flow-operations.md")
- [Troubleshooting firewall endpoint failures in AWS Network Firewall](firewall-troubleshooting-endpoint-failures.md "firewall-troubleshooting-endpoint-failures.md")
