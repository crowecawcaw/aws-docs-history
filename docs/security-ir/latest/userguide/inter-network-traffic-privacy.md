# Inter-network traffic privacy

## Traffic between service and

on-premises clients and applications

You have two connectivity options between your private network and AWS:

- An AWS Site-to-Site VPN connection. For more information, see
  [What is
  AWS Site-to-Site VPN?](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md") in the _AWS Site-to-Site VPN User Guide_.
- An Direct Connect connection. For more information, see
  [What is
  Direct Connect?](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") in the _Direct Connect User Guide_.

Access to AWS Security Incident Response via the network is through AWS published APIs. Clients must support
Transport Layer Security (TLS) 1.2. We recommend TLS 1.3. Clients must also
support cipher suites with Perfect Forward Secrecy (PFS), such as Ephemeral
Diffie-Hellman (DHE) or Elliptic Curve Diffie-Hellman Ephemeral (ECDHE). Most modern
systems such as Java 7 and later support these modes. Additionally, you must sign
requests using an access key ID and a secret access key that are associated with an
IAM principal, or you can use the
[AWS Security Token Service (STS)](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") to generate temporary
security credentials to sign requests.

## Traffic between AWS

resources in the same Region

An Amazon Virtual Private Cloud (Amazon VPC) endpoint for AWS Security Incident Response is a logical entity within a VPC that allows
connectivity only to AWS Security Incident Response. The Amazon VPC routes requests to AWS Security Incident Response and routes responses back
to the VPC. For more information, see
[VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md") in the
_Amazon VPC User Guide_. For example policies that you can use to
control access from VPC endpoints, see [Using IAM policies to control
access to DynamoDB](../../../vpc/latest/userguide/vpc-endpoints-ddb.md "../../../vpc/latest/userguide/vpc-endpoints-ddb.md").

###### Note

Amazon VPC endpoints are not accessible via AWS Site-to-Site VPN or Direct Connect.
