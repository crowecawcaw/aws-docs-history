

# Security in Amazon S3
<a name="security"></a>

**Important**  
Amazon Simple Storage Service now applies a new default bucket security setting that automatically disables server-side encryption with customer-provided keys (SSE-C) for all new general purpose buckets. In April 2026, Amazon S3 deployed an update so all new general purpose buckets have SSE-C encryption disabled for all new write requests. For existing buckets in AWS accounts with no SSE-C encrypted objects, Amazon S3 also disabled SSE-C for all new write requests. With this change, applications that need SSE-C encryption must deliberately enable SSE-C by using the [PutBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html) API operation after creating a new bucket. For more information about this change, see [Default SSE-C setting for new buckets FAQ](default-s3-c-encryption-setting-faq.md).

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that are built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:

**Security of the cloud**  
AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. The effectiveness of our security is regularly tested and verified by third-party auditors as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to Amazon S3, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).

**Security in the cloud**  
Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your organization’s requirements, and applicable laws and regulations. For Amazon S3, your responsibility includes the following areas:
+ Managing your data, including [object ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) and [encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html).
+ Classifying your assets.
+ [Managing access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-iam.html) to your data using [IAM roles](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html#roles) and other service configurations to apply the appropriate permissions.
+ Enabling detective controls such as [AWS CloudTrail](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudtrail-logging.html) or [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/s3_detection.html) for Amazon S3.

This documentation will help you understand how to apply the shared responsibility model when using Amazon S3. The following topics show you how to configure Amazon S3 to meet your security and compliance objectives. You'll also learn how to use other AWS services that can help you monitor and secure your Amazon S3 resources. 

**Note**  
For more information about using the Amazon S3 Express One Zone storage class with directory buckets, see [S3 Express One Zone](directory-bucket-high-performance.md#s3-express-one-zone) and [Working with directory buckets](directory-buckets-overview.md).

**Topics**
+ [Security best practices for Amazon S3](security-best-practices.md)
+ [Data protection in Amazon S3](DataDurability.md)
+ [Protecting data with encryption](UsingEncryption.md)
+ [Internetwork traffic privacy](inter-network-traffic-privacy.md)
+ [Compliance validation for Amazon S3](s3-compliance.md)
+ [Resilience in Amazon S3](disaster-recovery-resiliency.md)
+ [Infrastructure security in Amazon S3](network-isolation.md)
+ [Configuration and vulnerability analysis in Amazon S3](vulnerability-analysis-and-management.md)
+ [Access management](security-access-management.md)
+ [Amazon Simple Storage Service data inventory](s3-data-inventory.md)