# Data protection in AWS CloudTrail

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
 applies to data protection in AWS CloudTrail. As described in this model, AWS is
 responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are
 responsible for maintaining control over your content that is hosted on this infrastructure.
 You are also responsible for the security configuration and management tasks for the AWS services
 that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/"). For information about data protection in Europe, see the [AWS Shared
 Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the *AWS Security
 Blog*.

For data protection purposes, we recommend that you protect AWS account
 credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:


* Use multi-factor authentication (MFA) with each account.
* Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
* Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](cloudtrail-trails.md "cloudtrail-trails.md") in the *AWS CloudTrail User Guide*.
* Use AWS encryption solutions, along with all default security controls within AWS services.
* Use advanced managed security services such as Amazon Macie, which assists in discovering
 and securing sensitive data that is stored in Amazon S3.
* If you require FIPS 140-3 validated cryptographic modules when accessing AWS through
 a command line interface or an API, use a FIPS endpoint. For more information about the
 available FIPS endpoints, see [Federal
 Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
We strongly recommend that you never put confidential or sensitive information, such as your
 customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with CloudTrail or other AWS services 
 using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
 tags or free-form text fields used for names may be used for billing or diagnostic logs. If you 
 provide a URL to an external server, we strongly recommend that you do not include credentials 
 information in the URL to validate your request to that server.

By default, CloudTrail event log files and digest files are encrypted using Amazon S3 server-side encryption (SSE).
 You can also choose to encrypt your log files and digest files with an AWS Key Management Service (AWS KMS) key. You can store
 your log files in your bucket for as long as you want. You can also define Amazon S3 lifecycle
 rules to archive or delete log files automatically. If you want notifications about log file
 delivery and validation, you can set up Amazon SNS notifications.

The following security best practices also address data protection in CloudTrail:


* [Encrypting CloudTrail log files, digest files, and event data stores with AWS KMS keys (SSE-KMS)](encrypting-cloudtrail-log-files-with-aws-kms.md "encrypting-cloudtrail-log-files-with-aws-kms.md")
* [Amazon S3 bucket policy for CloudTrail](create-s3-bucket-policy-for-cloudtrail.md "create-s3-bucket-policy-for-cloudtrail.md")
* [Validating CloudTrail log file integrity](cloudtrail-log-file-validation-intro.md "cloudtrail-log-file-validation-intro.md")
* [Sharing CloudTrail log files between AWS accounts](cloudtrail-sharing-logs.md "cloudtrail-sharing-logs.md")
Because CloudTrail logs files are stored in a bucket or buckets in Amazon S3, you should also review
 the data protection information in the Amazon Simple Storage Service User Guide. For more information, see [Data protection in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html").
