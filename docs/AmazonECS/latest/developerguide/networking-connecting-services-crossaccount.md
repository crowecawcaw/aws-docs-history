# Best practices for networking Amazon ECS services across AWS accounts and VPCs

If you're part of an organization with multiple teams and divisions, you probably
deploy services independently into separate VPCs inside a shared AWS account or into
VPCs that are associated with multiple individual AWS accounts. No matter which way
you deploy your services, we recommend that you supplement your networking components to
help route traffic between VPCs. For this, several AWS services can be used to
supplement your existing networking components.

- AWS Transit Gateway — You should consider this networking service
  first. This service serves as a central hub for routing your connections between
  Amazon VPCs, AWS accounts, and on-premises networks. For more information, see
  [What is a transit
  gateway?](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md") in the _Amazon VPC Transit Gateways Guide_.
- Amazon VPC and VPN support — You can use this service to create site-to-site
  VPN connections for connecting on-premises networks to your VPC. For more
  information, see [What is AWS Site-to-Site VPN?](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md") in the
  _AWS Site-to-Site VPN User Guide_.
- Amazon VPC — You can use Amazon VPC peering to help you to connect multiple VPCs,
  either in the same account, or across accounts. For more information, see [What
  is VPC peering?](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md") in the _Amazon VPC Peering Guide_.
- Shared VPCs — You can use a VPC and VPC subnets across multiple AWS
  accounts. For more information, see [Working with shared VPCs](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md")
  in the _Amazon VPC User Guide_.
