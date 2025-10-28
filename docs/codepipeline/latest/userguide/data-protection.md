# Data protection in AWS CodePipeline

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS CodePipeline. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with CodePipeline or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

The following security best practices also address data protection in CodePipeline:

- [Configure server-side encryption for artifacts
  stored in Amazon S3 for CodePipeline](S3-artifact-encryption.md "S3-artifact-encryption.md")
- [Use AWS Secrets Manager to track database passwords
  or third-party API keys](parameter-store-encryption.md "parameter-store-encryption.md")

## Internetwork traffic privacy

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual network
(_virtual private cloud_) that you define. CodePipeline
supports Amazon VPC endpoints powered by AWS PrivateLink, an AWS technology that facilitates
private communication between AWS services using an elastic network interface with
private IP addresses. This means you can connect directly to CodePipeline through a private
endpoint in your VPC, keeping all traffic inside your VPC and the AWS network.
Previously, applications running inside a VPC required internet access to connect to
CodePipeline. With a VPC, you have control over your network settings, such as:

- IP address range,
- Subnets,
- Route tables, and
- Network gateways.

To connect your VPC to CodePipeline, you define an interface VPC endpoint for CodePipeline. This
type of endpoint makes it possible for you to connect your VPC to AWS services. The
endpoint provides reliable, scalable connectivity to CodePipeline without requiring an internet
gateway, network address translation (NAT) instance, or VPN connection. For information
about setting up a VPC, see the [VPC User
Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md").

## Encryption at rest

Data in CodePipeline is encrypted at rest using AWS KMS keys. Code artifacts are stored in
a customer-owned S3 bucket and encrypted with either the AWS managed key or a
customer managed key. For more information, see [Configure server-side encryption for artifacts
stored in Amazon S3 for CodePipeline](S3-artifact-encryption.md "S3-artifact-encryption.md").

## Encryption in transit

All service-to-service communication is encrypted in transit using SSL/TLS.

## Encryption key management

If you choose the default option for encrypting code artifacts, CodePipeline uses the
AWS managed key. You cannot change or delete this AWS managed key. If you use a
customer managed key in AWS KMS to encrypt or decrypt artifacts in the S3 bucket, you can change or
rotate this customer managed key as necessary.

###### Important

CodePipeline only supports symmetric KMS keys. Do not use an asymmetric KMS key to encrypt the
data in your S3 bucket.

###### Topics
