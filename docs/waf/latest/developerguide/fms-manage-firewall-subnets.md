**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# How Firewall Manager manages your firewall subnets

This section explains how Firewall Manager manages your firewall subnets.

Firewall subnets are the VPC subnets that Firewall Manager creates for the firewall endpoints that
filter your network traffic. Each firewall endpoint must be deployed in a dedicated
VPC subnet. Firewall Manager creates at least one firewall subnet in each VPC that's within
scope of the policy.

For policies that use the distributed deployment model with automatic endpoint configuration, Firewall Manager only creates firewall subnets in Availability Zones that have a subnet with an
internet gateway route, or a subnet with a route to the firewall endpoints that Firewall Manager
created for their policy. For more information, see [VPCs and subnets](../../../vpc/latest/userguide/VPC_Subnets.md#vpc-subnet-basics "../../../vpc/latest/userguide/VPC_Subnets.md#vpc-subnet-basics") in
the _Amazon VPC User Guide_.

For policies that use either the distributed or centralized model where you specify which
Availability Zones Firewall Manager creates the firewall endpoints in, Firewall Manager creates an endpoint in
those specific Availability Zones irrespective of whether there are other resources in
the Availability Zone.

When you first define a Network Firewall policy, you specify how Firewall Manager manages the firewall subnets in each of the VPCs that are in scope. You
cannot change this choice later.

For policies that use the distributed deployment model with automatic endpoint
configuration, you can choose between the following options:

- Deploy a firewall subnet for every Availability Zone that has public subnets.
  This is the default behavior. This provides high availability of your traffic
  filtering protections.
- Deploy a single firewall subnet in one Availability Zone. With this choice,
  Firewall Manager identifies a zone in the VPC that has the most public subnets and creates
  the firewall subnet there. The single firewall endpoint filters all network
  traffic for the VPC. This can reduce firewall costs, but it isn't highly
  available and it requires traffic from other zones to cross zone boundaries in
  order to be filtered.
  For policies that use distributed deployment model with custom endpoint configuration or the
  centralized deployment model, Firewall Manager creates the subnets in the specified Availability
  Zones that are within the policy scope.

You can provide VPC CIDR blocks for Firewall Manager to use for the firewall subnets or you can
leave the choice of firewall endpoint addresses up to Firewall Manager to determine.

- If you don't provide CIDR blocks, Firewall Manager queries your VPCs for available IP
  addresses to use.
- If you provide a list of CIDR blocks, Firewall Manager searches for new subnets only in
  the CIDR blocks that you provide. You must use /28 CIDR blocks. For each
  firewall subnet that Firewall Manager creates, it walks your CIDR block list and uses the
  first one that it finds that is applicable to the Availability Zone and VPC and
  has available addresses. If Firewall Manager is unable to find open space in the VPC (with or
  without the restriction), the service won't create a firewall in the
  VPC.
  If Firewall Manager can't create a required firewall subnet in an Availability Zone, it marks the
  subnet as non-compliant with the policy. While the zone is in this state, traffic for
  the zone must cross zone boundaries in order to be filtered by an endpoint in another
  zone. This is similar to the single firewall subnet scenario.
