# Internetwork traffic privacy

Connections are protected both between
Amazon Aurora and on-premises
applications and between
Amazon Aurora and other AWS resources within the same
AWS Region.

## Traffic between service and on-premises clients and applications

You have two connectivity options between your private network and AWS:

- An AWS Site-to-Site VPN connection. For more information, see [What is
  AWS Site-to-Site VPN?](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md")
- An Direct Connect connection. For more information, see [What is Direct Connect?](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md")

You get access to
Amazon Aurora through the network by using
AWS-published API operations. Clients must support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS
  1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE
  (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral
  Diffie-Hellman). Most modern systems such as Java 7 and later support
  these modes.

Additionally, requests must be signed by using an access key ID and a secret
access key that is associated with an IAM principal. Or you can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate temporary security credentials to
sign requests.
