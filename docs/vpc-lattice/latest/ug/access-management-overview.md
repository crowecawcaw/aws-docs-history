# Manage access to VPC Lattice services

VPC Lattice is secure by default because you must be explicit about which services and
resource configurations to provide access to and with which VPCs. You can access services
through a VPC association or a VPC endpoint of type service network. For multi-account
scenarios, you can use [AWS Resource Access Manager](sharing.md "sharing.md") to share services, resource
configurations, and service networks across account boundaries.

VPC Lattice provides a framework that lets you implement a defense-in-depth
strategy at multiple layers of the network.

- First layer – The service, resource, VPC, and
  VPC endpoint association with a service network. A VPC may be connected to a service
  network either though an association or through a VPC endpoint. If a VPC is not
  connected to a service network, clients in the VPC cannot access the service and
  resource configurations that are associated with the service network.
- Second layer – Optional network-level
  security protections for the service network, such as security groups and network
  ACLs. By using these, you can allow access to specific groups of clients in a VPC
  instead of all clients in the VPC.
- Third layer – Optional VPC Lattice auth policy.
  You can apply an auth policy to service networks and individual services. Typically,
  the auth policy on the service network is operated by the network or cloud
  administrator, and they implement coarse-grained authorization. For example,
  allowing only authenticated requests from a specific organization in AWS Organizations. For
  an auth policy at the service level, typically the service owner sets fine-grained
  controls, which might be more restrictive than the coarse-grained authorization
  applied at the service network level.

###### Note

The auth policy on the service network doesn’t apply to resource
configurations in the service network.

###### Methods of access control

- [Auth policies](auth-policies.md "auth-policies.md")
- [Security groups](security-groups.md "security-groups.md")
- [Network ACLs](network-acls.md "network-acls.md")
