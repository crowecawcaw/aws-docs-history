# Infrastructure security in Amazon WorkMail

###### Note

Amazon WorkMail discontinued support for Transport Layer Security (TLS) 1.0 and 1.1. If you are using TLS 1.0 or 1.1, you must upgrade the TLS version to 1.2. For more information, see [TLS 1.2 to become the minimum TLS protocol level for all AWS API endpoints](https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/ "https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/").

As a managed service, Amazon WorkMail is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS environment using the best practices for infrastructure security, see
[Infrastructure Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected Framework_.

You use AWS published API calls to access Amazon WorkMail through the network.
Clients must support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.
