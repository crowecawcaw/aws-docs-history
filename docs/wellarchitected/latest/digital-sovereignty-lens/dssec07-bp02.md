# DSSEC07-BP02 Provide technical options to enhance privacy

Digital sovereignty requirements demand that organizations secure data and provide
verifiable evidence of privacy protection measures. Technical privacy enhancement options enable
organizations to process sensitive data while minimizing exposure risks. These options support
business objectives and regulatory mandates through cryptographic techniques, data minimization,
and privacy-preserving technologies.

**Desired outcome:** Sensitive data remains protected throughout
its lifecycle with technical privacy controls that minimize exposure risks. Organizations
maintain auditable evidence of privacy protection measures for regulatory adherence. Data
utility is preserved for legitimate business operations while privacy guarantees are maintained.

**Common anti-patterns:**

- Relying solely on access controls without implementing data-level privacy protections.
  This leaves sensitive information vulnerable when permission boundaries are compromised.
- Using static masking or tokenization techniques that cannot be customized per use case,
  user role or data type.
- Implementing privacy controls as an afterthought rather than baking in privacy by
  design principles into the software development lifecycle (SDLC) activities.

**Benefits of establishing this best practice:**

- Advanced privacy techniques demonstrate due diligence in protecting citizen data. They
  assist in meeting digital sovereignty requirements across multiple jurisdictions.
- Privacy-preserving technologies enable legitimate data use cases while maintaining
  strong privacy protections. This supports business innovation within regulatory constraints.
- Logging and monitoring of privacy controls provide verifiable evidence for regulatory
  audits and compliance assessments.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Organizations should implement a layered approach to data privacy. This approach combines
multiple technical controls based on data sensitivity levels and use case requirements,
including encryption, tokenization, differential privacy, and secure multi-party computation
techniques. Select and configure privacy technologies that align with your specific regulatory
requirements. Maintain data accessibility for business operations.

### Implementation steps

1. **Assess data sensitivity and privacy requirements**:
   - Conduct data mapping to identify sensitive data types including PII, PHI,
     financial information, and proprietary business data.
   - Define privacy requirements based on applicable regulations such as GDPR,
     HIPAA, CCPA, and industry-specific standards.
   - Establish data classification schemas that align with privacy protection levels
     and regulatory requirements.
   - Use Amazon Macie, AWS Glue PII Detect, Amazon Comprehend PII Detect to automatically
     discover and classify sensitive data across your AWS environment. Use
     Amazon CodeGuru to find potential privacy related leakages in your application code.

2. **Implement encryption and key management**:
   - Deploy AWS Key Management Service (KMS) with customer-managed keys for granular control over
     encryption operations.
   - Implement AWS CloudHSM for hardware-based key protection when regulatory requirements
     mandate usage of a single-tenant hardware security module (HSM).
   - Use AWS Certificate Manager for managing SSL/TLS certificates to encrypt data in transit.
   - Consider using External Key Stores, where at least one part of the encryption
     and decryption process needs to be carried outside of a cloud service provider's
     infrastructure. AWS provides an external key store implementation with the [KMS
     External Key Store (XKS)](../../../kms/latest/developerguide/keystore-external.md "../../../kms/latest/developerguide/keystore-external.md") feature and partners offer [prebuilt](https://aws.amazon.com/marketplace/pp/prodview-okhkj5cv2lski?trk=5ad469a6-4fed-484b-8f20-053172717fde&sc_channel=el "https://aws.amazon.com/marketplace/pp/prodview-okhkj5cv2lski?trk=5ad469a6-4fed-484b-8f20-053172717fde&sc_channel=el") external key store solutions on top.
   - Use AWS PrivateLink enabled endpoints to have resources in your VPC securely
     communicate with AWS Services. PrivateLink manifests as Interface and Gateway
     Endpoints at the edge of your VPC.

3. **Deploy tokenization, data masking, and privacy
   enhancements**:
   - Implement [format-preserving
     encryption (FPE)](https://en.wikipedia.org/wiki/Format-preserving_encryption "https://en.wikipedia.org/wiki/Format-preserving_encryption") to maintain data utility while protecting sensitive
     values.
   - Deploy tokenization systems that replace sensitive data with non-sensitive
     tokens.
   - Configure data masking based on user roles and access patterns.
   - Use AWS Secrets Manager to securely store and rotate tokenization keys and masking rules.
   - Deploy secure aggregation methods for statistical analysis. These methods don't
     expose individual data points. For example, provide only summary tables.
   - Go beyond aggregation methods and implement [differential
     privacy](https://en.wikipedia.org/wiki/Differential_privacy "https://en.wikipedia.org/wiki/Differential_privacy") techniques. Differential privacy embeds random noise into the
     query engine. This reduces the chances of identifying a single record having
     sensitive information while still retaining utility of the data.

4. **Establish confidential computing environments and privacy
   vaults**:
   - Deploy AWS Nitro Enclaves (part of EC2) for processing highly sensitive data
     in isolated compute environments.
   - Implement secure multi-party computation (SMPC) protocols for collaborative
     data analysis without data sharing. Consider AWS Clean Rooms to collaborate with your
     partners without sharing raw data.
   - Set up privacy vaults. Privacy vaults store PII and PHI at a single immutable
     place and provide APIs for querying. Privacy vaults also play a role towards
     reducing data sprawl and implementing data minimization. For an example of this, see
     [How to Scale for Global SaaS Growth with a Skyflow Data Privacy Vault on
     AWS](https://aws.amazon.com/blogs/apn/how-to-scale-for-global-saas-growth-with-a-skyflow-data-privacy-vault-on-aws/ "https://aws.amazon.com/blogs/apn/how-to-scale-for-global-saas-growth-with-a-skyflow-data-privacy-vault-on-aws/").

5. **Implement privacy monitoring and compliance**:
   - Set up AWS CloudTrail to log privacy-related operations including encryption,
     decryption, and data access events.
   - Configure Amazon CloudWatch to monitor privacy control effectiveness and detect
     anomalous access patterns with intelligence threat detection capabilities offered by
     Amazon GuardDuty.
   - Use AWS Config to make sure privacy controls remain properly configured and
     compliant with organizational policies.
   - Deploy AWS Security Hub to aggregate privacy and security findings across your
     environment.

6. **Enable data subject rights and consent management**:
   - Implement automated data subject access request (DSAR) processing using
     AWS Lambda and Amazon API Gateway.
   - Deploy consent management systems and track user preferences and consent
     status.

7. **Implement data minimization**:
   - Archive data not in use.
     - Use Amazon S3 lifecycle policies to archive data to Glacier.
     - Use Amazon Data Lifecycle Manager to delete Amazon Elastic Block Store (Amazon EBS) snapshots no longer in use.

   - Use Amazon DynamoDB TTL to delete items that are no longer relevant. Use cases
     include in-session game data or similar event data that have already been
     materialized to another long-term storage solution (for example to S3).
   - Do not copy datasets to enable individual use cases. Instead build data
     adapters with built-in authorization policies, and audit trails (for example HTTP
     APIs) to improve the accessibility of your datasets.
   - Minimize proliferation of database views constructed over tables. Instead use
     data access policies with column, row and cell level filters to enable predefined
     use cases.

## Resources

**Related best practices:**

- [Data Analytics Lens - Best practice 3.1 – Privacy by Design](../analytics-lens/best-practice-3.md "../analytics-lens/best-practice-3.md")
- [SEC08-BP01 Implement secure key management](../security-pillar/sec_protect_data_rest_key_mgmt.md "../security-pillar/sec_protect_data_rest_key_mgmt.md")
- [SEC08-BP02 Enforce encryption at rest](../security-pillar/sec_protect_data_rest_encrypt.md "../security-pillar/sec_protect_data_rest_encrypt.md")
- [SEC08-BP03 Automate data at rest protection](../security-pillar/sec_protect_data_rest_automate_protection.md "../security-pillar/sec_protect_data_rest_automate_protection.md")
- [SEC03-BP01 Define access requirements](../security-pillar/sec_permissions_define.md "../security-pillar/sec_permissions_define.md")
- [SEC07-BP01 Understand your data classification scheme](../security-pillar/sec_data_classification_identify_data.md "../security-pillar/sec_data_classification_identify_data.md")

**Related documents:**

- [AWS Key Management Service
  Developer Guide](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")
- [Amazon Macie User
  Guide](../../../macie/latest/user/what-is-macie.md "../../../macie/latest/user/what-is-macie.md")
- [AWS Nitro
  Enclaves User Guide](../../../enclaves/latest/user/nitro-enclave.md "../../../enclaves/latest/user/nitro-enclave.md")
- [AWS CloudHSM User
  Guide](../../../cloudhsm/latest/userguide/introduction.md "../../../cloudhsm/latest/userguide/introduction.md")
- [AWS Encryption SDK Developer Guide](../../../encryption-sdk/latest/developer-guide/introduction.md "../../../encryption-sdk/latest/developer-guide/introduction.md")
- [AWS Secrets Manager
  User Guide](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md")

**Related videos:**

- [AWS re:Inforce 2022

* Building privacy compliance on AWS (DPP101)](https://www.youtube.com/watch?v=-4OlJhFsqqU&t=1138s "https://www.youtube.com/watch?v=-4OlJhFsqqU&t=1138s")

- [AWS re:Invent 2022 - Protecting
  secrets, keys, and data: Cryptography for the long term (SEC403)](https://www.youtube.com/watch?v=9vr3oMODIUE "https://www.youtube.com/watch?v=9vr3oMODIUE")
- [AWS re:Invent 2025 - State of
  the Art: AWS data protection in 2025 (ft. Vanguard) (SEC203)](https://www.youtube.com/watch?v=MMdXKVcSH-o "https://www.youtube.com/watch?v=MMdXKVcSH-o")
- [AWS re:Invent 2025 -
  Privacy-preserving AI primitives: Building blocks for regulated industries
  (ARC328)](https://www.youtube.com/watch?v=vfkKJhllnx4 "https://www.youtube.com/watch?v=vfkKJhllnx4")
- [Cryptographic Computing:
  Protecting Data in Use - AWS Online Tech Talks](https://www.youtube.com/watch?v=7B7qaCFfdRo "https://www.youtube.com/watch?v=7B7qaCFfdRo")

**Related services:**

- [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [AWS CloudHSM](https://aws.amazon.com/cloudhsm/ "https://aws.amazon.com/cloudhsm/")
- [AWS Nitro Enclaves](https://aws.amazon.com/ec2/nitro/nitro-enclaves/ "https://aws.amazon.com/ec2/nitro/nitro-enclaves/")
- [Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/")
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/ "https://aws.amazon.com/secrets-manager/")
- [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/ "https://aws.amazon.com/certificate-manager/")
