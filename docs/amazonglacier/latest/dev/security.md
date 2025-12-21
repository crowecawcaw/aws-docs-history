**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Security in Amazon Glacier

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a
data center and network architecture that are built to meet the requirements of the most
security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared
responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security _of_ the cloud and security _in_ the cloud:

- **Security of the cloud** – AWS is responsible for
  protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also
  provides you with services that you can use securely. The effectiveness of our security is
  regularly tested and verified by third-party auditors as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn
  about the compliance programs that apply to Amazon Glacier (Amazon Glacier), see [AWS Services in Scope by Compliance
  Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also
  responsible for other factors including the sensitivity of your data, your organization’s requirements, and applicable laws and regulations.
  This documentation will help you understand how to apply the shared responsibility model when using Amazon Glacier. The following topics show you how to
  configure Amazon Glacier to meet your security and compliance objectives. You'll also learn how to use other AWS services that can help you to monitor
  and secure your Amazon Glacier resources.

###### Topics

- [Data Protection in Amazon Glacier](DataDurability.md "DataDurability.md")
- [Identity and Access Management for Amazon Glacier](security-iam.md "security-iam.md")
- [Logging and Monitoring in Amazon Glacier](glacier-incident-response.md "glacier-incident-response.md")
- [Compliance Validation for Amazon Glacier](glacier-compliance.md "glacier-compliance.md")
- [Resilience in Amazon Glacier](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md")
- [Infrastructure Security in Amazon Glacier](network-isolation.md "network-isolation.md")
