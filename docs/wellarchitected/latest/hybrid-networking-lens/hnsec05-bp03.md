# HNSEC05-BP03 Use application layer encryption

Applying TLS encryption at the application layer ensures data
confidentiality even when transmitted over untrusted networks. For
optimal security, use certificates for authentication where
available and ensure encryption requirements follow the latest
standards and best practices, allowing only secure protocols with
strong cipher suites that are regularly monitored and updated.

**Desired outcome:** Ensure that data
remains protected on lower-speed or hosted Direct Connect
connections.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Protects sensitive data regardless of Direct Connect speed or
  type
- Enables flexibility with software or application-based
  encryption
- Maintains compliance with security policies and data protection
  requirements
- Ensures end-to-end encryptions for all workloads

## Implementation guidance

- For application-layer encryption, use TLS/SSL for all
  sensitive communications.
- Use certificate-based authentication where possible.
- Periodically test and review encryption configurations and key
  management.

## Resources

- [Encryption
  in transit over external networks: AWS guidance for NYDFS and
  beyond](https://aws.amazon.com/blogs/security/encryption-in-transit-over-external-networks-aws-guidance-for-nydfs-and-beyond/ "https://aws.amazon.com/blogs/security/encryption-in-transit-over-external-networks-aws-guidance-for-nydfs-and-beyond/")
- [Hybrid
  Connectivity AWS Whitepaper](../../../whitepapers/latest/hybrid-connectivity/hybrid-connectivity.md "../../../whitepapers/latest/hybrid-connectivity/hybrid-connectivity.md").
