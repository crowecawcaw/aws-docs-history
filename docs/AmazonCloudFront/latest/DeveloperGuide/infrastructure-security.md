# Infrastructure security in Amazon CloudFront

As a managed service, Amazon CloudFront is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access CloudFront through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.
  CloudFront Functions uses a highly secure isolation barrier between AWS accounts, ensuring that
  customer environments are secure against side-channel attacks like Spectre and Meltdown.
  Functions cannot access or modify data belonging to other customers. Functions run in a
  dedicated single-threaded process on a dedicated CPU without hyperthreading. In any given CloudFront
  edge location point of presence (POP), CloudFront Functions only serves one customer at a time, and
  all customer-specific data is cleared between function executions.
