# Infrastructure security in Macie

As a managed service, Amazon Macie is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access Macie through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.
  You can call these API operations from any network location. However, if you use Amazon Virtual Private Cloud
  (Amazon VPC) to host your AWS resources, you can establish a private connection between your VPC
  and Macie by creating an interface endpoint. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/"), a technology that enables you to
  privately access Macie without an internet gateway, NAT device, VPN connection, or
  AWS Direct Connect connection. We create an endpoint network interface in each subnet that you enable
  for an interface endpoint. These are requester-managed network interfaces that can serve as
  the entry point for traffic destined for Macie. For more information, see [Access AWS services
  through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.
