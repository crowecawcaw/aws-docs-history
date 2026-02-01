# DSPERF03-BP01 Choose open protocols and approved encryption

schemes

Using open protocols and approved encryption schemes improves your
adherence to national cybersecurity standards and industry
regulations. This also avoids vendor lock-in and supply-chain
bottlenecks, especially where adversarial states might use their
position to place technology embargoes.

**Desired outcome:** Implement
industry-standard cryptographic controls and encryption protocols
validated by certification bodies. Adhere to regulatory
requirements. Adopt pre-vetted implementations for transparency and
auditability.

**Common anti-patterns:**

- Using deprecated protocols (SSL/TLS 1.0/1.1) or implementing
  proprietary or custom encryption schemes instead of validated
  standards.
- Hardcoding encryption keys in code, failing to rotate keys
  regularly, and using weak key exchange protocols.
- Ignoring regulatory requirements and failing to verify
  encryption methods meet specific standards (FIPS or common
  criteria).
- Using different encryption approaches across services without a
  coherent strategy or documentation.
- Neglecting algorithm agility and building systems that are
  difficult to migrate to stronger encryption schemes.

**Benefits of establishing this best
practice:**

- Uses community-vetted, battle-tested cryptographic
  implementations to reduce vulnerabilities and block data
  breaches.
- Adheres to industry standards through certified encryption
  schemes while simplifying validation.
- Enables seamless integration with third-party systems and
  provides algorithm agility for evolving standards.
- Reduces vendor lock-in, optimizes costs through proven
  implementations, and maintains flexibility across providers.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Design a comprehensive cryptographic implementation strategy using
AWS services and industry standards.

Key implementation elements:

- Conduct inventory assessment of current cryptographic
  implementations across AWS services and applications
- Establish organizational standards based on NIST, FIPS, and
  industry-specific requirements
- Implement AWS KMS for centralized key management with
  standardized algorithms (AES-256, RSA-2048, ECC)
- Enforce strong protocols (TLS 1.2+) for data in transit across
  each service
- Create phased migration roadmap prioritizing high-risk areas
- Deploy continuous monitoring and compliance validation
  processes

This approach provides consistent, compliant cryptographic
controls while minimizing operational disruption.

### Implementation steps

1. Conduct an inventory assessment to document current
   cryptography and certificate management practices. Identify
   encryption methods, map key usage, and list certificate
   deployments. Identify third-party dependencies that could be
   of concern from a sovereignty point of view.
2. Implement cryptographic standards by configuring
   [AWS KMS](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") for FIPS 140-2 Security Level 3 compliance,
   NIST-approved algorithms, and industry-specific
   requirements.
3. Set up key management using
   [AWS KMS](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") to manage keys, key policies, key rotation, and
   access controls. Configure
   [AWS CloudHSM](../../../cloudhsm/latest/userguide/introduction.md "../../../cloudhsm/latest/userguide/introduction.md") when you require shared or dedicated HSM
   tenancy.
4. Verify transport security by configuring
   [AWS Certificate Manager](../../../acm/latest/userguide/acm-overview.md "../../../acm/latest/userguide/acm-overview.md") for TLS certificate management,
   automated renewal, and domain validation. Implement security
   policies to control access to certificate stores and to
   certificates.
5. Monitor compliance using
   [AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md") for compliance checks, security
   standards, and automated validation, and configure alerts
   for non-compliance.

## Resources

**Related best practices:**

- [PERF04-BP05
  Choose network protocols to improve performance](../performance-efficiency-pillar/perf_networking_choose_network_protocols_improve_performance.md "../performance-efficiency-pillar/perf_networking_choose_network_protocols_improve_performance.md")
- [SEC09-BP02
  Enforce encryption in transit](../security-pillar/sec_protect_data_transit_encrypt.md "../security-pillar/sec_protect_data_transit_encrypt.md")
- [SEC08-BP01
  Implement secure key management](../security-pillar/sec_protect_data_rest_key_mgmt.md "../security-pillar/sec_protect_data_rest_key_mgmt.md")
- [SEC08-BP02
  Enforce encryption at rest](../security-pillar/sec_protect_data_rest_encrypt.md "../security-pillar/sec_protect_data_rest_encrypt.md")
- [SEC08-BP03
  Automate data at rest protection](../security-pillar/sec_protect_data_rest_automate_protection.md "../security-pillar/sec_protect_data_rest_automate_protection.md")
- [SEC08-BP04
  Enforce access control](../security-pillar/sec_protect_data_rest_access_control.md "../security-pillar/sec_protect_data_rest_access_control.md")

**Related documents:**

- [Supported
  cryptographic algorithms](../../../kms/latest/developerguide/supported-algorithms.md "../../../kms/latest/developerguide/supported-algorithms.md")
- [Advanced
  Encryption Standard (AES)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf "https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf")
- [The
  importance of encryption and how AWS can help](https://aws.amazon.com/blogs/security/importance-of-encryption-and-how-aws-can-help/ "https://aws.amazon.com/blogs/security/importance-of-encryption-and-how-aws-can-help/")

**Related videos:**

- [AWS re:Invent 2023 - Better together: Using encryption &
  authorization for data protection (SEC333)](https://www.youtube.com/watch?v=T4_rqwfngfU "https://www.youtube.com/watch?v=T4_rqwfngfU")
- [AWS re:Inforce 2025 - Post-quantum cryptography demystified
  (DAP222)](https://www.youtube.com/watch?v=SG9ndQWH8S4 "https://www.youtube.com/watch?v=SG9ndQWH8S4")

**Related examples:**

- [AWS Network Architecture Guide](../../../vpc/latest/userguide/VPC_Scenarios.md "../../../vpc/latest/userguide/VPC_Scenarios.md")
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/")
- [AWS Reference Architecture Examples](https://aws.amazon.com/architecture/ "https://aws.amazon.com/architecture/")
- [RSA](https://www.rsa.com/ "https://www.rsa.com/")
- [Transport
  Layer Security (TLS)](https://csrc.nist.gov/glossary/term/transport_layer_security "https://csrc.nist.gov/glossary/term/transport_layer_security")

**Related services:**

- [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [AWS CloudHSM](https://aws.amazon.com/cloudhsm/ "https://aws.amazon.com/cloudhsm/")
- [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/ "https://aws.amazon.com/certificate-manager/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
