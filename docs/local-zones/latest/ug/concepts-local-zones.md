# AWS Local Zones concepts

These are the essential concepts in AWS Local Zones:

- Local Zone — An extension of an AWS Region in
  geographic proximity to your users, where the Local Zone infrastructure is deployed.
- VPC — A virtual private cloud (VPC) is a virtual
  network that closely resembles a traditional network that you'd operate in your own data
  center. You create subnets in your VPCs and deploy AWS resources, such as Amazon EC2 instances,
  in your subnets. A VPC can span Availability Zones, Local Zones, and Wavelength Zones.
- Local Zone subnet — A subnet that you create in a Local Zone.
  You can deploy supported AWS resources in your Local Zone subnets.
- Network Border Group — A unique group from which
  AWS advertises public IP addresses. It consists of Availability Zones, Local Zones, or Wavelength
  Zones. A pool of public IP addresses can be explicitly allocated for use in a network border
  group. Once provisioned, IP addresses cannot move between network border groups. For
  example, the `us-west-2-lax-1` network border group consists of two Local Zones in Los
  Angeles, and the `us-east-1-bos-1` network border group consists of a single Local Zone
  in Boston. You can move an IP address between the two Los Angeles Local Zones, but you cannot move
  an IP address from a Los Angeles Local Zone to the Boston Local Zone.

When creating a subnet, you will find the network border group for the Local Zones in the
**Availability Zone** drop-down list.

- Parent Region — The Region that handles some of the
  Local Zone and Wavelength Zone control plane operations, such as API calls.
- Parent Zone ID — The ID of the zone that handles
  some of the Local Zone and Wavelength Zone control plane operations, such as API calls
  For more information, see:

- [AWS Site-to-Site VPN
  concepts](../../../vpn/latest/s2svpn/VPC_VPN.md#concepts "../../../vpn/latest/s2svpn/VPC_VPN.md#concepts") in the _AWS Site-to-Site VPN User Guide_.
- [Route table concepts](../../../vpc/latest/userguide/VPC_Route_Tables.md#RouteTables "../../../vpc/latest/userguide/VPC_Route_Tables.md#RouteTables") in the _Amazon VPC User Guide_.
