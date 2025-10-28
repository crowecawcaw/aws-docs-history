# High-level steps for implementing AWS Network Firewall

To install and use an AWS Network Firewall firewall in your Amazon Virtual Private Cloud VPC, you configure the
firewall components and your VPC's subnets and route tables in the following high-level
steps.

- **Configure the primary VPC subnets for your firewall endpoints**
  – In the primary VPC where you'll use the firewall, in each
  Availability Zone where you want a firewall
  endpoint, create a subnet specifically for use by Network Firewall. A firewall
  endpoint can't protect applications that run in the same subnet, so reserve
  these subnets for exclusive use by the firewall. The subnets that you use for
  your primary firewall endpoints must belong to a single AWS Region and must be in
  different Availability Zones within the Region.

Network Firewall is available in
the Regions listed at [AWS service endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").

For information about managing subnets in your VPC, see
[VPCs and subnets](../../../vpc/latest/userguide/VPC_Subnets.md "../../../vpc/latest/userguide/VPC_Subnets.md")
in the _Amazon Virtual Private Cloud User Guide_.

- **Create the firewall** – Create a Network Firewall
  firewall and provide it with the specifications for each of your firewall
  subnets. Network Firewall creates a firewall endpoint in each subnet that you
  specify, available to monitor and protect the resources for the subnets whose
  traffic you send through it.
- **Configure the firewall policy** –
  Define the firewall policy for your firewall by specifying its rule groups
  and other behavior that you want the firewall to provide.
- **Modify your VPC route tables to include the firewall**
  – Using Amazon VPC ingress routing enhancements, change your routing tables to
  route traffic through the Network Firewall firewall. These changes must insert the
  firewall between the subnets that you want to protect and outside locations. The
  exact routing that you need to do depends on your architecture and its
  components.

For information about managing route tables for your VPC, see
[Route
tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md") in the _Amazon Virtual Private Cloud User
Guide_.
After you implement a firewall, you can expand its protections to additional VPCs and to multiple subnets within a single
Availability Zone for any VPC. To do this, you manage the VPCs, subnets, and route tables as described in the previous high level steps,
but you create the firewall endpoints in VPC endpoint associations, using the firewall that you've already defined.
For more information about managing firewalls and VPC endpoint associations, see [Firewalls and firewall endpoints in AWS Network Firewall](firewalls.md "firewalls.md").
