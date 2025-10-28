# Security in Oracle Database@AWS

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from data
centers and network architectures that are built to meet the requirements of the most
security-sensitive organizations.

Security is a shared responsibility between AWS, OCI, and you. The shared responsibility model
describes this as security _of_ the cloud and security _in_ the cloud:

- **Security of the cloud** – AWS is responsible for protecting
  the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely.
  Third-party auditors regularly test and verify the effectiveness of our security as part of the
  [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/").
- **Security in the cloud** – Your responsibility is
  determined by the AWS service that you use. You are also responsible for other factors,
  including the sensitivity of your data, your organization's requirements, and applicable
  laws and regulations.
  This documentation helps you understand how to apply the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") when
  using Oracle Database@AWS. You also learn how to use other AWS services that help you
  to monitor and secure your Oracle Database@AWS resources.

You can manage access to your Oracle Database@AWS resources. The method you use to manage access
depends on what type of task you need to perform with Oracle Database@AWS:

- Use AWS Identity and Access Management (IAM) policies to assign permissions that determine who is allowed to manage Oracle Database@AWS resources.
  For example, you can use IAM to determine who is allowed to create, describe, modify, and delete Exadata infrastucture, VM clusters
  or tag resources.
- Use the security features of your Oracle database engine to control who can log in to the databases on a DB instance.
  These features work just as if the database was on your local network.
- Use Secure Socket Layers (SSL) or Transport Layer Security (TLS) connections with Exadata databases. For more information, see
  [Prepare for TLS Walletless Connections](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/vdosu/ "https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/vdosu/").
- Oracle Database@AWS isn't immediately accessible from the internet and deployed on private subnets in AWS only.
- Oracle Database@AWS uses many default Transmission Control Protocol (TCP) ports for various operations.
  For the full list of ports, see Default port assignments.
- To store and manage keys by using Transparent Data Encryption (TDE), which is enabled by default,
  Oracle Database@AWS uses [OCI vaults](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/keyoverview.htm "https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/keyoverview.htm")
  or [Oracle Key Vault](https://www.oracle.com/security/database-security/key-vault/ "https://www.oracle.com/security/database-security/key-vault/").
  Oracle Database@AWS doesn't support AWS Key Management Service.
- By default, the database is configured by using Oracle-managed encryption keys.
  The database also supports customer-managed keys.
- To enhance data protection, use Oracle Data Safe with Oracle Database@AWS.
  The following topics show you how to configure Oracle Database@AWS to meet your
  security and compliance objectives.

###### Topics

- [Data protection in Oracle Database@AWS](data-protection.md "data-protection.md")
- [Identity and access management for Oracle Database@AWS](security-iam.md "security-iam.md")
- [Compliance validation for Oracle Database@AWS](compliance-validation.md "compliance-validation.md")
- [Resilience in Oracle Database@AWS](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md")
- [Using service-linked roles for Oracle Database@AWS](odb-SLR.md "odb-SLR.md")
- [Oracle Database@AWS updates to AWS managed policies](odb-manpol-updates.md "odb-manpol-updates.md")
