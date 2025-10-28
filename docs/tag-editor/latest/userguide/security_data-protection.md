# Data protection in Tag Editor

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in Tag Editor. As described in this model, AWS is
responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are
responsible for maintaining control over your content that is hosted on this infrastructure.
You are also responsible for the security configuration and management tasks for the AWS services
that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/"). For information about data protection in Europe, see the [AWS Shared
Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security
Blog_.

For data protection purposes, we recommend that you protect AWS account
credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
- Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](../../../awscloudtrail/latest/userguide/cloudtrail-trails.md "../../../awscloudtrail/latest/userguide/cloudtrail-trails.md") in the _AWS CloudTrail User Guide_.
- Use AWS encryption solutions, along with all default security controls within AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering
  and securing sensitive data that is stored in Amazon S3.
- If you require FIPS 140-3 validated cryptographic modules when accessing AWS through
  a command line interface or an API, use a FIPS endpoint. For more information about the
  available FIPS endpoints, see [Federal
  Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  We strongly recommend that you never put confidential or sensitive information, such as your
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Tag Editor or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Data encryption

Tagging information is not encrypted. Although not encrypted, tags can contain
information used as part of your security strategy, so it's important to control who can
access tags on resources. It's especially critical that you control who can modify tags
because such access could be used to elevate one's permissions.

### Encryption at rest

There are no additional ways of isolating service or network traffic that are
specific to Tag Editor. If applicable, use AWS specific isolation. You can use the
Tag Editor API and console in a virtual private cloud (VPC) to help maximize privacy
and infrastructure security.

### Encryption in transit

Tag Editor data is encrypted in transit to the service's internal database for
backup. This is not user-configurable.

### Key management

Tag Editor is not currently integrated with AWS Key Management Service and does not support
AWS KMS keys.

## Internetwork traffic privacy

Tag Editor uses HTTPS for all transmissions between Tag Editor users and AWS. Tag Editor uses
transport layer security (TLS) 1.3, but also supports TLS 1.2.
