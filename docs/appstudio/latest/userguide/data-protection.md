# Data protection in AWS App Studio

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS App Studio. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS App Studio or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Data encryption

App Studio securely stores and transfers data by encrypting data at rest and in transit.

### Encryption at rest

Encryption at rest refers to protecting your data from unauthorized access by encrypting
data while stored. App Studio provides encryption at rest by default using AWS KMS keys,
and you do not need to do any additional configuration for data encryption at rest.

App Studio securely stores the following data for your applications: source code, build artifacts, metadata, and permissions information.

When using data sources that are encrypted with a AWS KMS Customer Managed Key (CMK), App Studio resources continue to be encrypted using an AWS managed key, whereas
the data in the encrypted data sources are encrypted by the CMK. For more information about using encrypted data sources in App Studio apps, see
[Use encrypted data sources with CMKs](encrypted-data-cmk.md "encrypted-data-cmk.md").

App Studio uses Amazon CloudFront to serve your app to your users. CloudFront uses SSDs which are
encrypted for edge location points of presence (POPs), and encrypted EBS volumes for Regional Edge Caches
(RECs). Function code and configuration in CloudFront Functions is always stored in an encrypted format on the
encrypted SSDs on the edge location POPs, and in other storage locations used by CloudFront.

## Encryption in transit

Encryption in transit refers to protecting your data from being intercepted while it moves between communication
endpoints. App Studio provides encryption for data in-transit by default. All communication between
customers and App Studio, and between App Studio and its downstream dependencies is protected using TLS
connections that are signed using the Signature Version 4 signing process. All App Studio endpoints use
SHA-256 certificates that are managed by AWS Certificate Manager Private Certificate Authority.

## Key management

App Studio does not support managing encryption keys.

## Inter-network traffic privacy

When you create an instance in App Studio, you choose the AWS Region where the data and resources
will be stored for that instance. Application build artifacts and metadata never leaves that AWS Region.

However, note the following information:

- Because App Studio uses Amazon CloudFront to serve your application and uses Lambda@Edge to manage
  authentication to your application, a limited set of authentication data, authorization data,
  application metadata would be accessed from CloudFront edge locations, which could be in a different Region.
- AWS App Studio transfers data across AWS Regions to enable certain generative AI features in the service. For more information
  about the features enabled by cross-Region data transfers, the type of data that moves across Regions, and how to opt out, see
  [Cross-Region data transfer in AWS App Studio](cross-region-data-transfer.md "cross-region-data-transfer.md").
