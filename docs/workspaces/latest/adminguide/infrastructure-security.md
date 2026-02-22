# Infrastructure security in Amazon WorkSpaces

As a managed service, Amazon WorkSpaces is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access WorkSpaces through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.

###### Contents

- [Network isolation](network-isolation.md "network-isolation.md")
- [Isolation on physical hosts](physical-isolation.md "physical-isolation.md")
- [Credential Guard / Virtualization-Based Security (VBS)](credential-guard-vbs.md "credential-guard-vbs.md")
- [Authorization of corporate users](authorization.md "authorization.md")
- [Create and Stream from Interface VPC Endpoints](creating-streaming-vpc-endpoints.md "creating-streaming-vpc-endpoints.md")
- [Make Amazon WorkSpaces API requests through a VPC interface
  endpoint](interface-vpc-endpoint.md "interface-vpc-endpoint.md")
- [Create a VPC endpoint policy for Amazon WorkSpaces](api-private-link-policy.md "api-private-link-policy.md")
- [Connect your private network to your VPC](notebook-private-link-vpn.md "notebook-private-link-vpn.md")
