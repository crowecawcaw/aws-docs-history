# DSPERF02-BP02 Maintain sovereign control over encryption

keys

Sovereign key management provides organizations full control over
their encryption keys, aligning with national data residency and
sovereignty laws. For regulated industries, this blocks third-party
access to sensitive data, reduces legal risks, and meets mandates
for country-specific regulations requiring data to remain within
jurisdictional boundaries.

**Desired outcome:** Implement a
sovereign key management architecture. Maintain exclusive control
over encryption keys within designated jurisdictions. Enable
compliant cloud operations while meeting regulatory requirements.

**Common anti-patterns:**

- Using default keys without customer-managed keys (CMKs) or FIPS
  140-2/3-validated HSMs, and storing keys in non-compliant
  Regions.
- Mixing sovereign and non-sovereign key operations, granting
  overly broad IAM permissions, and lacking proper multi-factor
  authentication.
- Not implementing automated key rotation, proper versioning, or
  maintaining secure backup and recovery procedures.
- Failing to maintain proper audit trails, access logs, and
  compliance documentation for sovereign key operations.

**Benefits of establishing this best
practice:**

- Meet data sovereignty, residency, and regulatory requirements
  (for example, GDPR or CMMC) by keeping encryption keys within
  specific jurisdictions.
- Maintain exclusive control over hardware-backed cryptographic
  keys with authorized personnel access, reducing third-party
  dependencies and potential attack vectors.
- Enable detailed tracking and monitoring of key operations
  through AWS CloudTrail and AWS Config for compliance and
  security analysis.
- Implement organization-specific key usage policies and access
  controls while maintaining cryptographic independence from cloud
  provider access.
- Reduce dependency on external key management services while
  improving continuous operation through controlled key
  management.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Organizations should assess regulatory requirements to determine
appropriate key sovereignty needs. Implement AWS CloudHSM or AWS KMS External Key Store (XKS) in compliant Regions while providing
proper redundancy and compliance-aligned procedures.

- Evaluate regulatory requirements and design high-availability
  architecture with appropriate geographic distribution
- Deploy CloudHSM clusters in compliant Regions and integrate
  with AWS KMS using custom key stores
- Implement secure key lifecycle management with automated
  rotation and strict access controls
- Establish comprehensive monitoring, audit logging, and
  compliance validation processes
- Enforce least privilege access through strict IAM policies and
  key usage controls

### Implementation steps

1. Document regulatory and compliance requirements to determine
   key sovereignty needs, then design a high-availability
   architecture using
   [AWS Well-Architected Framework](../framework/welcome.md "../framework/welcome.md") with appropriate
   geographic distribution across compliant regions to verify
   that cryptographic keys meet data residency requirements
   while maintaining business continuity.
2. Deploy
   [AWS CloudHSM](../../../cloudhsm.md "../../../cloudhsm.md") clusters in compliant regions and integrate
   with [AWS KMS](../../../kms.md "../../../kms.md") using AWS KMS External Key Store (XKS) or custom
   key stores. This enables you to maintain control over
   hardware security modules while using AWS' managed
   encryption services for improved application integration and
   regulatory adherence.
3. Configure automated key rotation and lifecycle management
   through
   [AWS KMS](../../../kms.md "../../../kms.md") combined with strict
   [AWS IAM](../../../iam.md "../../../iam.md") policies and
   [AWS Secrets Manager](../../../secretsmanager.md "../../../secretsmanager.md") integration. This enforces
   least-privilege access controls managing cryptographic keys
   throughout their lifecycle and maintaining security and
   regulatory standards.
4. Enable
   [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") for audit logging,
   [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") for monitoring, and
   [AWS Config](../../../config.md "../../../config.md") with
   [AWS Audit Manager](../../../audit-manager.md "../../../audit-manager.md") for compliance validation to maintain
   complete visibility into key usage. Detect unauthorized
   access attempts, and generate compliance reports required
   for regulatory audits and security oversight.

## Resources

**Related best practices:**

- [Protecting
  data at rest](../security-pillar/protecting-data-at-rest.md "../security-pillar/protecting-data-at-rest.md")
- [SEC08-BP01
  Implement secure key management](../security-pillar/sec_protect_data_rest_key_mgmt.md "../security-pillar/sec_protect_data_rest_key_mgmt.md")

**Related documents:**

- [AWS Key Management Best Practices](https://d1.awsstatic.com/whitepapers/aws-kms-best-practices.pdf "https://d1.awsstatic.com/whitepapers/aws-kms-best-practices.pdf")
- [Introduction
  to the cryptographic details of AWS KMS](../../../kms/latest/cryptographic-details/intro.md "../../../kms/latest/cryptographic-details/intro.md")
- [Data
  Residency Whitepaper](https://d1.awsstatic.com/whitepapers/compliance/Data_Residency_Whitepaper.pdf "https://d1.awsstatic.com/whitepapers/compliance/Data_Residency_Whitepaper.pdf")

**Relate blogs:**

- [Establishing
  a European trust service provider for the AWS European
  Sovereign Cloud](https://aws.amazon.com/blogs/security/establishing-a-european-trust-service-provider-for-the-aws-european-sovereign-cloud/ "https://aws.amazon.com/blogs/security/establishing-a-european-trust-service-provider-for-the-aws-european-sovereign-cloud/")

**Related videos:**

- [Encryption
  and Key Management in AWS](https://www.youtube.com/watch?v=uhXalpNzPU4 "https://www.youtube.com/watch?v=uhXalpNzPU4")
- [Navigating
  the Complex World of Data Regulation and Compliance](https://aws.amazon.com/awstv/watch/3ab1ac49b9c/ "https://aws.amazon.com/awstv/watch/3ab1ac49b9c/")
