# Internetwork traffic privacy

This topic describes how Amazon File Cache secures connections from the service to other
locations.

## Traffic between

Amazon File Cache and on-premises clients

You have two connectivity options between your private network and AWS:

- An AWS Site-to-Site VPN connection. For more information, see [What is
  AWS Site-to-Site VPN?](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md")
- An AWS Direct Connect connection. For more information, see [What is AWS Direct Connect?](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md")

You can access Amazon File Cache over the network to reach AWS-published API
operations for performing administrative tasks and Lustre ports to interact with the
cache.

Access to Amazon File Cache by using the network is through AWS-published APIs. Clients must
support Transport Layer Security (TLS) 1.2 and later. We require TLS 1.2 and recommend TLS 1.3.
Clients must also support cipher suites with Perfect Forward Secrecy (PFS), such as
Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Diffie-Hellman Ephemeral (ECDHE).
Most modern systems such as Java 7 and later support these modes. Additionally,
requests must be signed by using an access key ID and a secret access key that is
associated with an IAM principal. Or you can use the [AWS Security Token Service (STS)](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") to generate
temporary security credentials to sign requests.

## API traffic between

AWS resources in the same Region

An Amazon Virtual Private Cloud (Amazon VPC) endpoint for Amazon File Cache is a logical entity within a VPC
that allows connectivity only to Amazon File Cache. The Amazon VPC routes API requests to
Amazon File Cache and routes responses back to the VPC. For more information, see
[VPC
Endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md") in the _Amazon VPC User Guide_.
