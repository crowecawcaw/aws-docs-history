# LSPERF02-BP02 Secure data separation by

classification

Establish clear boundaries between different data types based on
sensitivity and regulatory requirements. Maintain sensitive patient
records in encrypted, highly-available database instances with
comprehensive audit capabilities, while allowing broader access to
de-identified research datasets through separate storage mechanisms
with appropriate controls for scientific collaboration.

**Desired outcome:** Establish a
comprehensive data separation framework that clearly separates
different data types based on sensitivity levels and regulatory
requirements, providing appropriate storage, access controls, and
availability for each category.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Design your data architecture with clearly defined boundaries that
separate information based on sensitivity levels and regulatory
requirements. Implement a comprehensive data classification system
that identifies and tags data according to sensitivity, regulatory
scope, and access requirements. For sensitive patient records and
protected health information (PHI), use encrypted,
highly-available database services like Amazon RDS with multi-AZ
deployments and encryption at rest using AWS KMS customer-managed
keys.

Enable comprehensive audit logging through services like AWS CloudTrail and Amazon RDS Enhanced Monitoring to track access and
modifications to sensitive data, improving adherence to
regulations like HIPAA or GDPR.

For de-identified research datasets intended for broader
scientific collaboration, establish separate storage mechanisms
using services like Amazon S3 with appropriate bucket policies and
access controls that facilitate controlled sharing while blocking
unauthorized access. Implement robust de-identification processes
that follow established standards like HIPAA Safe Harbor or Expert
Determination methods before moving data to these collaborative
environments.

Use AWS Identity and Access Management (IAM) with attribute-based
access control (ABAC) to create fine-grained permissions based on
data classification tags, verifying that users can only access
data appropriate to their role and research needs. Consider
implementing additional safeguards like VPC endpoints and network
isolation to provide network-level separation between sensitive
and de-identified data environments.

### Implementation steps

1. Implement AWS Organizations for multi-account data
   separation.
2. Configure S3 bucket policies for sensitivity-based
   isolation.
3. Use AWS IAM for fine-grained data access controls.
4. Deploy AWS Lake Formation for centralized data governance.
5. Implement AWS KMS with Customer Managed keys for each data
   category.
