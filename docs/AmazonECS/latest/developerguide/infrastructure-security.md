# Infrastructure Security in Amazon Elastic Container Service

As a managed service, Amazon Elastic Container Service is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access Amazon ECS through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.
  You can call these API operations from any network location. Amazon ECS supports resource-based
  access policies, which can include restrictions based on the source IP address, so make sure
  that the policies account for the IP address for the network location. You can also use
  Amazon ECS policies to control access from specific Amazon Virtual Private Cloud endpoints or specific VPCs.
  Effectively, this isolates network access to a given Amazon ECS resource from only the specific
  VPC within the AWS network. For more information, see [Amazon ECS interface VPC endpoints (AWS PrivateLink)](vpc-endpoints.md "vpc-endpoints.md").
