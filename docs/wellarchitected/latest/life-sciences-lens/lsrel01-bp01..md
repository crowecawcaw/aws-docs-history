# LSREL01-BP01 Identify and protect sensitive data elements with

auditable classification.

Conduct a systematic analysis to identify sensitive data elements
(like PHI, identifiers, and lab results), establish classification
standards, and map business processes that generate or consume them.
Define which data should be anonymized, irreversibly de-identified,
or remain re-identifiable to support authorized patient re-linking
after research.

**Desired outcome:** The complete
dataset will be accessible to a broader group of individuals and
organizations. However, access to individual data elements will be
restricted to only those with the necessary permissions.

**Common anti-patterns:**

- Encrypting each data element.
- No or incorrect data classification.
- Incorrect classification of de-identify data element.

**Benefits of establishing this best
practice:**

- Enables broader data sharing and secondary analysis while
  preserving trust, meeting regulatory requirements.
- Fosters a culture of trust and appropriate data handling.
- Verifies that anonymization procedures correspond effectively
  with legal requirements and organizational goals through
  collaborative effort among technical, legal, and governance
  teams.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Consider Amazon SageMaker AI Unified Studio and AWS Lake Formation
for a unified view of data sources and consumers. This combination
of services assists you to centrally govern, secure, and globally
share data for analytics and machine learning. With AWS Lake Formation, you can enforce fine-grained access control for your
data at row, column, and cell level. This centralized access
control mechanism reduces the risk of configuration errors and
consistently enforces policies across your data access patterns,
improving the reliability of your data governance.

Use AWS Key Management Service (KMS) to securely manage and audit
encryption keys during the lifecycle of life science data like
genomics or bioscience research data. Implement automatic key
rotation and use AWS CloudTrail integration for full traceability
and recovery assurance. Forward CloudTrail logs to a dedicated
account for log integrity and to avoid tampering, supporting
reliable audit trails for regulatory verification. This provides a
resilient and highly available key management system that
consistently encrypts and decrypts data even during Regional
failover or transient service issues.

Store classification manifests (including dataset UUID, sensitive
field mappings, classification levels, and SHA-256 digests) in
Amazon S3 with S3 Object Lock enabled. This makes your
classification records immutable, stopping accidental or malicious
deletion and providing a reliable audit trail for
compliance-related and recovery scenarios. Configure appropriate
retention periods based on regulatory requirements.

### Implementation steps

1. Identify and inventory the data sources that generate or
   capture sensitive data elements, and use AWS AWS Glue Data Catalog as a centralized metadata repository. Use Amazon Macie to automatically discover and classify sensitive data
   elements, reducing manual classification errors and
   improving consistency across datasets. Add custom attributes
   in the Data Catalog to indicate if a data element requires
   de-identification, irreversible anonymization, or
   encryption. Automate this discovery and classification
   process to maintain accuracy as data elements are added,
   updated, or removed across systems.
2. Make decision which data elements to secure and protect in
   system of record. Consider using AWS KMS for creating and
   controlling encryption keys to protect data across systems.
   Consider using AWS CloudTrail for audit trail what keys are
   used by who, when, and on which data elements.
3. Consider providing a scalable decryption function or API to
   reverse data based on role and permissions at data-domain,
   row, column, or cell level.

## Resources

**Related best practices:**

- Encrypting data at rest and in transit.
- Copies of data with or without sensitive data based on need.
- Removing sensitive data for downstream systems and relying on
  source systems to make sure data is reverse traceable with
  primary keys.
- Adding features to source systems to avoid data egress even
  within the organization.

**Related documents:**

- [Guidance
  for Data Anonymization on AWS](https://aws.amazon.com/solutions/guidance/data-anonymization-on-aws/ "https://aws.amazon.com/solutions/guidance/data-anonymization-on-aws/")

**Related tools:**

- [Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/")
- [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/ "https://aws.amazon.com/sagemaker/unified-studio/")
- [AWS Lake Formation](https://aws.amazon.com/lake-formation/ "https://aws.amazon.com/lake-formation/")
- [AWS Key Management Service](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
