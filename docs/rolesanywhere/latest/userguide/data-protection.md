# Data protection and privacy in IAM Roles Anywhere

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS Identity and Access Management Roles Anywhere. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with IAM Roles Anywhere or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Encryption in transit

IAM Roles Anywhere provides secure and private endpoints for encrypting data in transit. The
secure and private endpoints allow AWS to protect the integrity of API requests to
IAM Roles Anywhere. AWS requires API calls to be signed by the caller using a secret access key. This
requirement is stated in the [Signature Version 4 Signing Process](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md")
(Sigv4).

## Key management

Authenticating to IAM Roles Anywhere requires the use of asymmetric (public/private) key pairs.
IAM Roles Anywhere does not hold customer private keys. Those remain on customer instances in data
centers. Care should be taken to minimize the risk of accidental disclosure.

- Use OS file system permissions to restrict read access to the owning user.

- Never check keys into source control. Store them separately from source code to reduce
  the risk of accidentally including them in a change set. If possible, consider the use of
  a secure storage mechanism.

## Inter-network traffic privacy

When accessing AWS APIs and resources from your data center, be aware of how the traffic
is routed. Connectivity may occur via Network Address Translation (NAT) at the data center
outbound firewall, or it may occur through Virtual Private Network (VPN).
