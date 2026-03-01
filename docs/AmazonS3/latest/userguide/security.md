# Security in Amazon S3

###### Important

Starting in April 2026, AWS will disable server-side encryption with customer-provided keys (SSE-C) for all new buckets. In addition, SSE-C encryption will be disabled for all existing buckets in AWS accounts that do not have any SSE-C encrypted data. With these changes, the few applications that need SSE-C encryption must deliberately enable the use SSE-C via the [PutBucketEncryption](../API/API_PutBucketEncryption.md "../API/API_PutBucketEncryption.md") API after creating the bucket. In these cases, you might need to update automation scripts, CloudFormation templates, or other infrastructure configuration tools to configure these settings. For more information, see the [AWS Storage Blog post](https://aws.amazon.com/blogs/storage/advanced-notice-amazon-s3-to-disable-the-use-of-sse-c-encryption-by-default-for-all-new-buckets-and-select-existing-buckets-in-april-2026/ "https://aws.amazon.com/blogs/storage/advanced-notice-amazon-s3-to-disable-the-use-of-sse-c-encryption-by-default-for-all-new-buckets-and-select-existing-buckets-in-april-2026/").

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a
data center and network architecture that are built to meet the requirements of the most
security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared
responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security _of_ the cloud and security _in_ the cloud:

###### Security of the cloud

AWS is responsible for
protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also
provides you with services that you can use securely. The effectiveness of our security is
regularly tested and verified by third-party auditors as part of the
[AWS compliance programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn
about the compliance programs that apply to Amazon S3, see
[AWS Services in Scope by Compliance
Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").

###### Security in the cloud

Your responsibility is
determined by the AWS service that you use. You are also responsible for other factors
including the sensitivity of your data, your organization’s requirements, and applicable
laws and regulations. For Amazon S3, your responsibility includes the following areas:

- Managing your data, including [object ownership](about-object-ownership.md "about-object-ownership.md") and
  [encryption](UsingEncryption.md "UsingEncryption.md").
- Classifying your assets.
- [Managing
  access](security-iam.md "security-iam.md") to your data using [IAM roles](security-best-practices.md#roles "security-best-practices.md#roles") and
  other service configurations to apply the appropriate permissions.
- Enabling detective controls such as [AWS CloudTrail](cloudtrail-logging.md "cloudtrail-logging.md") or [Amazon GuardDuty](../../../guardduty/latest/ug/s3_detection.md "../../../guardduty/latest/ug/s3_detection.md") for
  Amazon S3.
  This documentation will help you understand how to apply the shared responsibility model
  when using Amazon S3. The following topics show you how to configure Amazon S3 to meet
  your security and compliance objectives. You'll also learn how to use other AWS services that
  can help you monitor and secure your Amazon S3 resources.

###### Note

For more information about using the Amazon S3 Express One Zone storage class with directory buckets, see [S3 Express One Zone](directory-bucket-high-performance.md#s3-express-one-zone "directory-bucket-high-performance.md#s3-express-one-zone") and [Working with directory buckets](directory-buckets-overview.md "directory-buckets-overview.md").

###### Topics

- [Security best practices for Amazon S3](security-best-practices.md "security-best-practices.md")
- [Data protection in Amazon S3](DataDurability.md "DataDurability.md")
- [Protecting data with encryption](UsingEncryption.md "UsingEncryption.md")
- [Internetwork traffic privacy](inter-network-traffic-privacy.md "inter-network-traffic-privacy.md")
- [Compliance validation for Amazon S3](s3-compliance.md "s3-compliance.md")
- [Resilience in Amazon S3](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md")
- [Infrastructure security in Amazon S3](network-isolation.md "network-isolation.md")
- [Configuration and vulnerability analysis in Amazon S3](vulnerability-analysis-and-management.md "vulnerability-analysis-and-management.md")
- [Access management](security-access-management.md "security-access-management.md")
- [Amazon Simple Storage Service data inventory](s3-data-inventory.md "s3-data-inventory.md")
