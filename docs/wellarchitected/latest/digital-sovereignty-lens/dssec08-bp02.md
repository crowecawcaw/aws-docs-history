# DSSEC08-BP02 Localize cryptographic operations

You may have specific requirements to ring-fence cryptographic
operations to within specific infrastructure locations. By
constructing boundaries around cryptographic operations, you can
protect both your data and cryptographic keys to meet such
requirements.

**Desired outcome:** Cryptographic
operations remain within defined geographical and jurisdictional
boundaries under your control. Keys, keystores, and cryptographic
infrastructure are protected from access by Cloud Service Provider
operators. Cryptographic functions run only in trusted
infrastructure locations. You possess verifiable attestations and
certifications for cryptographic operations, implementations, and
the infrastructure where operations are performed. Cryptographic
activities are tracked and audited within the controlled
environment.

**Common anti-patterns:**

- Sharing cryptographic keys across multiple accounts, workloads,
  or geographies.
- Using cryptographic keys to which a third-party has access, or
  which are shared with other organizations.
- Using weak or outdated cryptographic algorithms, or using
  self-designed cryptographic algorithms and implementations.

**Benefits of establishing this best
practice:**

- Underlying plaintext data remains secure and unknown to threat
  actors, even if the encrypted data is somehow obtained.
- Well-known and well-tested cryptographic algorithms and
  implementations are unlikely to have readily exploitable
  weaknesses.
- Trust boundary remains fully within the control of the workload
  owner.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Localize cryptographic operations by installing and configuring
your own key management infrastructure and hardware security
modules (HSMs) hosted on infrastructure that is managed by you.
Build authenticated and authorized APIs for external applications
(such as workloads hosted on AWS) to invoke your cryptographic
infrastructure programmatically, and apply additional in-transit
encryption to protect plain text data.

Data sovereignty requirements do not always require you to own and
manage cryptographic infrastructure and operations. The default
HSMs provided by the AWS KMS may be sufficient for your workloads.
Additionally, with _customer managed keys_
customers create and control the lifecycle of keys and key
policies they own. For use cases with more stringent requirements,
AWS KMS External Key Store (XKS) or AWS CloudHSM integration
should be considered.

### Implementation steps

Consider the following aspects while choosing your data-at-rest
encryption strategy.

1. **Use AWS KMS Regional keys and
   multi-Region Keys appropriately:** AWS KMS Regional
   keys are regional resources that never leave their AWS Region. Cryptographic operations using these keys are
   performed within the Region where the key is created. AWS KMS uses FIPS 140-2 Level 3 validated hardware security
   modules to protect your encryption keys. Given the close
   integration of AWS KMS and other AWS services, if the
   workload is deployed in a single AWS Region and uses KMS
   Regional keys, this may be sufficient to achieve sovereignty
   goals.

There is no mechanism to export AWS KMS keys in plain text,
which keeps your sensitive cryptographic material secure.
AWS KMS Multi-Region keys maintain Regional isolation for
cryptographic operations, but allow the same key material to
exist in multiple Regions for data replication scenarios.
Consider whether this will support your data availability
goals while remaining consistent with your sovereignty
goals. 2. **Consider AWS KMS External Key Store
(XKS) or AWS CloudHSM integration for strict sovereignty
requirements:** For organizations with strict
sovereignty requirements, AWS CloudHSM can be integrated
with KMS through the Custom Key Store feature, providing
dedicated hardware security modules (HSMs) within the chosen
Region. Alternatively, the AWS KMS External Key Store (XKS)
feature enables customers to use their own key management
infrastructure while still using KMS APIs, maintaining
control over the root of trust. 3. **Restrict access to keys and actions
that use keys:** When deploying workloads using a
multi-account strategy, we recommend keeping AWS KMS keys in
the same account as the workload that uses them. The AWS IAM
service can be used to control access to KMS keys and
restrict cryptographic operations using those keys.
Identity-based policies can be attached to IAM users,
groups, or roles, to control their permissions to use KMS
keys. Resource-based policies can be attached to KMS keys to
control how the keys are used. Both identity-based and
resource-based policies can be applied simultaneously. For
sovereignty requirements it may be useful to add a condition
to restrict access by AWS Region. 4. **Record and control encryption
context:** Each AWS KMS cryptographic operation
with symmetric encryption KMS keys accept an
[encryption
context](../../../kms/latest/developerguide/encrypt_context.md "../../../kms/latest/developerguide/encrypt_context.md"). This is an optional set of non-secret
key-value pairs that act as additional authenticated data
(AAD). The encryption context is not secret and not
encrypted, and appears in plaintext in AWS CloudTrail Logs
for auditing purposes. For example key-value pairs like
"department": "10103.0"
and
"classification-level": "sensitive"
can be used in IAM policies to refine or limit access to KMS
keys in your account. 5. **Consider cost and operational
burden:** Operationalizing and maintaining your own
cryptographic infrastructure in the form of external key
stores or self-managed HSM instances brings additional costs
and skills into play. You are also required to fulfill
operational requirements such as applying security updates,
plus sourcing and replacing failed hardware (in the case of
AWS KMS XKS) modules. A pragmatic approach could be to use
such infrastructure to only protect data with higher
sensitivity classification levels, or where national
regulators demand such infrastructure.

## Resources

**Related best practices:**

- [SEC08-BP01
  Implement secure key management](../security-pillar/sec_protect_data_rest_key_mgmt.md "../security-pillar/sec_protect_data_rest_key_mgmt.md")

**Related documents:**

- [Using
  IAM policies with AWS KMS](../../../kms/latest/developerguide/iam-policies.md "../../../kms/latest/developerguide/iam-policies.md")
- [Key
  policies in KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md")
- [AWS post-quantum cryptography migration plan](https://aws.amazon.com/blogs/security/aws-post-quantum-cryptography-migration-plan/ "https://aws.amazon.com/blogs/security/aws-post-quantum-cryptography-migration-plan/")
- [Establishing
  a European trust service provider for the AWS European
  Sovereign Cloud](https://aws.amazon.com/blogs/security/establishing-a-european-trust-service-provider-for-the-aws-european-sovereign-cloud/ "https://aws.amazon.com/blogs/security/establishing-a-european-trust-service-provider-for-the-aws-european-sovereign-cloud/")
- [How
  to Protect the Integrity of Your Encrypted Data by Using AWS Key Management Service and EncryptionContext](https://aws.amazon.com/blogs/security/how-to-protect-the-integrity-of-your-encrypted-data-by-using-aws-key-management-service-and-encryptioncontext/ "https://aws.amazon.com/blogs/security/how-to-protect-the-integrity-of-your-encrypted-data-by-using-aws-key-management-service-and-encryptioncontext/")

**Related videos:**

- [AWS re:Invent 2020: Do you need an AWS KMS custom key
  store?](https://www.youtube.com/watch?v=0_s2pn-84O4 "https://www.youtube.com/watch?v=0_s2pn-84O4")
- [AWS re:Invent 2022 - Protecting secrets, keys, and data:
  Cryptography for the long term](https://www.youtube.com/watch?v=9vr3oMODIUE "https://www.youtube.com/watch?v=9vr3oMODIUE")

**Related services:**

- [AWS Key Management Service (KMS)](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")
- [AWS KMS External Key Store (XKS)](../../../kms/latest/developerguide/keystore-external.md "../../../kms/latest/developerguide/keystore-external.md")
- [AWS CloudHSM](../../../cloudhsm/latest/userguide/introduction.md "../../../cloudhsm/latest/userguide/introduction.md")
