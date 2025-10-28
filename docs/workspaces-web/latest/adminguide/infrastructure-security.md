# Infrastructure security in Amazon WorkSpaces Secure Browser

As a managed service, Amazon WorkSpaces Secure Browser is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access Amazon WorkSpaces Secure Browser through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.
  WorkSpaces Secure Browser isolates service traffic by applying Standard AWS SigV4 Authentication and
  Authorization to all services. The customer resource endpoint (or web portal endpoint) is
  protected by your identity provider. You can further isolate traffic by using Multi-factor
  Authorization and other security mechanism in your identity provider (IdP).

All internet access can be controlled by configuring network settings, such as the VPC,
subnet, or security group. Multi-tenancy and VPC endpoints (PrivateLink) are not currently
supported.
