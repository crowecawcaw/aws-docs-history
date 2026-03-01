# Infrastructure security in Amazon RDS

As a managed service, Amazon Relational Database Service is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access Amazon RDS through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.
  In addition, Amazon RDS
  offers features to help support infrastructure security.

## Security groups

Security groups control the access that traffic has in and out of a DB
instance. By default, network
access is turned off to a DB instance.
You can specify rules in a security group that allow access from an IP address range, port, or security group. After ingress rules are configured,
the same rules apply to all DB instances
that are associated with that security group.

For more information, see [Controlling access with security groups](Overview.md "Overview.md").

## Public accessibility

When you launch a DB instance inside a virtual private cloud (VPC) based on the Amazon VPC
service, you can turn on or off public accessibility for that DB instance. To designate
whether the DB instance that you create has a DNS name that resolves to a public IP
address, you use the _Public accessibility_ parameter. By using this
parameter, you can designate whether there is public access to the DB instance. You can
modify a DB instance to turn on or off public accessibility by modifying the
_Public accessibility_ parameter.

For more information, see [Hiding a DB instance in a VPC from the internet](USER_VPC.md#USER_VPC.Hiding "USER_VPC.md#USER_VPC.Hiding").

###### Note

If your DB instance is in a VPC but isn't publicly accessible, you can also use an AWS Site-to-Site VPN connection or
an Direct Connect connection to access it from a private network. For more information, see
[Internetwork traffic privacy](inter-network-traffic-privacy.md "inter-network-traffic-privacy.md").
