# Internetwork traffic privacy

This topic describes how Amazon S3 secures connections from the service to other locations.

## Traffic between service and

on-premises clients and applications

The following connections can be combined with AWS PrivateLink to provide connectivity between your private
network and AWS:

- An AWS Site-to-Site VPN connection. For more information, see
  [What is AWS Site-to-Site VPN?](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md")
- An Direct Connect connection. For more information, see
  [What is Direct Connect?](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md")

Access to Amazon S3 via the network is through AWS published APIs. Clients must support
Transport Layer Security (TLS) 1.2. We recommend utilizing TLS 1.3 with hybrid post-quantum key exchange. Clients must also
support cipher suites with Perfect Forward Secrecy (PFS), such as Ephemeral
Diffie-Hellman (DHE) or Elliptic Curve Diffie-Hellman Ephemeral (ECDHE). Most modern
systems such as Java 7 and later support these modes. Additionally, you must sign
requests using an access key ID and a secret access key that are associated with an
IAM principal, or you can use the [AWS Security Token Service (STS)](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") to generate temporary security credentials to sign
requests.

## Traffic between AWS resources in the

same Region

A virtual private cloud (VPC) endpoint for Amazon S3 is a logical entity within a VPC that allows
connectivity only to Amazon S3. The VPC routes requests to Amazon S3 and routes responses back
to the VPC. For more information, see [VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md") in the
_VPC User Guide_. For example bucket policies that you can use
to control S3 bucket access from VPC endpoints, see [Controlling access from VPC
endpoints with bucket policies](example-bucket-policies-vpc-endpoint.md "example-bucket-policies-vpc-endpoint.md").
