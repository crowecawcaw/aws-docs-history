# Security in Amazon OpenSearch Ingestion

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a
data center and network architecture that is built to meet the requirements of the most
security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
describes this as security _of_ the cloud and security
_in_ the cloud:

- **Security of the cloud** – AWS is
  responsible for protecting the infrastructure that runs AWS services in the AWS
  Cloud. AWS also provides you with services that you can use securely. Third-party
  auditors regularly test and verify the effectiveness of our security as part of the
  [AWS compliance
  programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/").
- **Security in the cloud** – Your responsibility
  is determined by the AWS service that you use. You are also responsible for other
  factors including the sensitivity of your data, your company’s requirements, and
  applicable laws and regulations.
  This documentation helps you understand how to apply the shared responsibility model when
  using OpenSearch Ingestion. The following topics show you how to configure OpenSearch Ingestion to
  meet your security and compliance objectives. You also learn how to use other AWS services
  that help you to monitor and secure your OpenSearch Ingestion resources.

###### Topics

- [Configuring VPC access for Amazon OpenSearch Ingestion
  pipelines](pipeline-security.md "pipeline-security.md")
- [Configuring OpenSearch Ingestion pipelines for
  cross-account ingestion](cross-account-pipelines.md "cross-account-pipelines.md")
- [Identity and Access Management for
  Amazon OpenSearch Ingestion](security-iam-ingestion.md "security-iam-ingestion.md")
- [Logging Amazon OpenSearch Ingestion API calls using
  AWS CloudTrail](osis-logging-using-cloudtrail.md "osis-logging-using-cloudtrail.md")
