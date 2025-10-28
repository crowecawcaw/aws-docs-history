# Verified Access endpoints

A Verified Access endpoint represents an application. Each endpoint is associated with a Verified Access group
and inherits the access policy for the group. You can optionally attach an application-specific
endpoint policy to each endpoint.

###### Contents

- [Verified Access endpoint types](#endpoint-types "#endpoint-types")
- [How Verified Access works with shared VPCs and subnets](#shared-vpc "#shared-vpc")
- [Create a load balancer endpoint for Verified Access](create-load-balancer-endpoint.md "create-load-balancer-endpoint.md")
- [Create a network interface endpoint for Verified Access](create-network-interface-endpoint.md "create-network-interface-endpoint.md")
- [Create a network CIDR endpoint for Verified Access](create-network-cidr-endpoint.md "create-network-cidr-endpoint.md")
- [Create an Amazon Relational Database Service endpoint for Verified Access](create-rds-endpoint.md "create-rds-endpoint.md")
- [Allow traffic that originates from your Verified Access
  endpoint](configure-endpoint-security-group.md "configure-endpoint-security-group.md")
- [Modify a Verified Access endpoint](modify-endpoint.md "modify-endpoint.md")
- [Modify a Verified Access endpoint policy](modify-endpoint-policy.md "modify-endpoint-policy.md")
- [Delete a Verified Access endpoint](delete-endpoint.md "delete-endpoint.md")

## Verified Access endpoint types

The following are the possible Verified Access endpoint types:

- **Load balancer** – Application requests are sent to a
  load balancer to distribute to your application. For more information, see
  [Create a load balancer endpoint](create-load-balancer-endpoint.md "create-load-balancer-endpoint.md").
- **Network interface** – Application requests are sent
  to a network interface using the specified protocol and port. For more information, see
  [Create a network interface endpoint](create-network-interface-endpoint.md "create-network-interface-endpoint.md").
- **Network CIDR** – Application requests are sent to
  the specified CIDR block. For more information, see
  [Create a network CIDR endpoint](create-network-cidr-endpoint.md "create-network-cidr-endpoint.md").
- **Amazon Relational Database Service (RDS)** – Application requests are sent to
  an RDS instance, RDS cluster, or RDS DB proxy. For more information, see
  [Create an Amazon Relational Database Service endpoint](create-rds-endpoint.md "create-rds-endpoint.md").

## How Verified Access works with shared VPCs and subnets

The following are the behaviors regarding shared VPC subnets:

- Verified Access endpoints are supported by VPC subnet sharing. A participant can create a Verified Access
  endpoint in a shared subnet.
- The participant who created the endpoint will be the endpoint owner, and the only party allowed to modify the endpoint. The VPC owner will not be allowed to modify the endpoint.
- Verified Access endpoints cannot be created in an AWS Local Zone and therefore sharing via Local
  Zones is not possible.

For more information see, [Share your VPC with other accounts](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md") in the _Amazon VPC User Guide_.
