# Inter-network traffic privacy in

Amazon Quick Suite

To use Amazon Quick Suite, users need access to the internet. They also need access to a compatible
browser or a mobile device with the Amazon Quick Suite mobile app installed. They don't need access to the
data sources they want to analyze. This access is handled inside Amazon Quick Suite. User connections to
Amazon Quick Suite are protected through the use of SSL. So that users can access Amazon Quick Suite, allow access
to HTTPS and Web Sockets Secure (wss://) protocol.

You can use a Microsoft AD connector and single sign-on (IAM Identity Center) in a corporate network
environment. You can further restrict access through the identity provider. Optionally, you
can also use MFA.

Amazon Quick Suite accesses data sources by using connection information supplied by the data source
owner in Amazon Quick Suite. Connections are protected both between Amazon Quick Suite and on-premises
applications and between Amazon Quick Suite and other AWS resources within the same AWS Region. For
connections to any source, the data source must allow connections from Amazon Quick Suite.

## Traffic

between service and on-premises clients and applications

You have two connectivity options between your private network and AWS:

- An AWS Site-to-Site VPN connection. For more information, see [What is AWS site-to-site
  VPN?](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md")
- An AWS Direct Connect connection. For more information, see [What is AWS direct
  connect?](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md")

If you are using AWS API operations to interact with Amazon Quick Suite through the network,
clients must support Transport Layer Security (TLS) 1.0. We recommend TLS 1.2. Clients must
also support cipher suites with Perfect Forward Secrecy (PFS), such as Ephemeral
Diffie-Hellman (DHE) or Elliptic Curve Diffie-Hellman Ephemeral (ECDHE). Most modern systems
such as Java 7 and later support these modes. You must sign requests using an access key ID
and a secret access key that are associated with an IAM principal, or you can use the
[AWS Security Token
Service (STS)](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") to generate temporary security credentials to sign requests.

## Traffic between AWS

resources in the same region

An Amazon Virtual Private Cloud (Amazon VPC) endpoint for Amazon Quick Suite is a logical entity within a VPC that allows
connectivity only to Amazon Quick Suite. The VPC routes requests to Amazon Quick Suite and routes responses back to
the VPC. For more information, see the following:

- [VPC
  endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md") in the _Amazon VPC User Guide_
- [Connecting to a Amazon VPC with Amazon Quick Suite](../../../quicksight/latest/user/working-with-aws-vpc.md "../../../quicksight/latest/user/working-with-aws-vpc.md")
