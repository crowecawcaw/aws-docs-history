# Security in Amazon DocumentDB

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that are built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. This documentation helps you understand how to apply the shared responsibility model when using Amazon DocumentDB.
The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security _of_ the cloud and security _in_ the cloud:

- **Security of the cloud** — AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud.
  AWS also provides you with services that you can use securely.
  Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/").
  To learn about the compliance programs that apply to Amazon DocumentDB (with MongoDB compatibility), see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** — Your responsibility is determined by the AWS service that you use.
  You are also responsible for other factors including the sensitivity of your data, your organization’s requirements, and applicable laws and regulations.
  Amazon DocumentDB is authorized under Federal Risk and Authorization Management Program (FedRAMP). It has FedRAMP High authorization for AWS GovCloud (US) regions and FedRAMP Moderate authorization for AWS US East/West Regions.
  For details about AWS and compliance efforts, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/FedRAMP/ "https://aws.amazon.com/compliance/services-in-scope/FedRAMP/").

###### Note

This chapter applies to both instance-based clusters and Elastic Clusters.
For more information, see the topics below.

You also learn how to use other AWS services that help you monitor and secure your Amazon DocumentDB resources.
The following topics show you how to configure Amazon DocumentDB to meet your security and compliance objectives.

###### Topics

- [Password management with Amazon DocumentDB and AWS Secrets Manager](docdb-secrets-manager.md "docdb-secrets-manager.md")
- [Data protection in Amazon DocumentDB](security.md "security.md")
- [Identity and Access Management for Amazon DocumentDB](security-iam.md "security-iam.md")
- [Authentication using IAM identity](iam-identity-auth.md "iam-identity-auth.md")
- [Managing Amazon DocumentDB users](security.md "security.md")
- [Database access using Role-Based
  Access Control](role_based_access_control.md "role_based_access_control.md")
- [Logging and monitoring in Amazon DocumentDB](logging-and-monitoring.md "logging-and-monitoring.md")
- [Updating your Amazon DocumentDB TLS
  certificates](ca_cert_rotation.md "ca_cert_rotation.md")
- [Updating your Amazon DocumentDB TLS
  certificates — GovCloud](ca_cert_rotation_pdt.md "ca_cert_rotation_pdt.md")
- [Compliance validation in Amazon DocumentDB](security.md "security.md")
- [Resilience in Amazon DocumentDB](security.md "security.md")
- [Infrastructure security in Amazon DocumentDB](security.md "security.md")
- [Amazon DocumentDB API and interface VPC endpoints (AWS PrivateLink)](docdb-private-link.md "docdb-private-link.md")
- [Security best practices for Amazon DocumentDB](security_best_practices.md "security_best_practices.md")
- [Auditing Amazon DocumentDB events](event-auditing.md "event-auditing.md")
- [Amazon VPC and Amazon DocumentDB](vpc-docdb.md "vpc-docdb.md")
