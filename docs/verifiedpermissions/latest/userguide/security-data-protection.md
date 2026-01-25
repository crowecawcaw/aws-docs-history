# Data protection in Amazon Verified Permissions

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") applies to data protection in Amazon Verified Permissions. As described in this model,
AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is
hosted on this infrastructure. This content includes the security configuration and
management tasks for the AWS services that you use. For more information about data
privacy, see the [Data Privacy
FAQ](https://aws.amazon.com/compliance/data-privacy-faq "https://aws.amazon.com/compliance/data-privacy-faq"). For information about data protection in Europe,
see the [AWS Shared Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS
Security Blog_.

- For data protection purposes, we recommend that you protect AWS account
  credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That
  way, each user is given only the permissions necessary to fulfill their job duties.
- We recommend that you secure your data in the following ways:
  - Use multi-factor authentication (MFA) with each account.
  - Use SSL/TLS to communicate with AWS resources. We require TLS
    1.2.
  - Set up API and user activity logging with AWS CloudTrail.
  - Use AWS encryption solutions, along with all default security controls
    within AWS services.
  - Use advanced managed security services such as Amazon Macie, which assists in
    discovering and securing sensitive data that is stored in Amazon S3.
  - If you require FIPS 140-2 validated cryptographic modules when accessing
    AWS through a command line interface or an API, use a FIPS endpoint. For
    more information about the available FIPS endpoints, see [Federal Information Processing
    Standard (FIPS) 140-2](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").

- We strongly recommend that you never put confidential or sensitive information,
  such as your customers' email addresses, into tags or free-form text fields
  such as a **Name** field. This includes when you work
  with Verified Permissions or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any
  data that you enter into tags or free-form text fields used for names may be used
  for billing or diagnostic logs. If you provide a URL to an external server, we
  strongly recommend that you do not include credentials information in the URL to
  validate your request to that server.
- Your action names should not include any sensitive information.
- We also strongly recommend that you always use unique, non-mutable, and
  non-reusable identifiers for your entities (resources and principals). In a test
  environment, you might choose to use simple entity identifiers, such as
  `jane` or `bob` for the name of an entity of type
  `User`. However, in a production system, it’s critical for security
  reasons that you use unique values that can’t be reused. We recommend that you use
  values like universally unique identifiers (UUIDs). For example, consider the user
  `jane` who leaves the company. Later, you let someone else use the
  name `jane`. That new user gets access automatically to everything
  granted by policies that still reference `User::"jane"`. Verified Permissions and Cedar
  can’t distinguish between the new user and the previous user.

This guidance applies to both principal and resource identifiers. Always use
identifiers that are guaranteed unique and never reused to ensure that you don’t
grant access unintentionally because of the presence of an old identifier in a
policy.

- Ensure that the strings that you provide to define `Long` and
  `Decimal` values are within the valid range of each type. Also,
  ensure that your use of any arithmetic operators don't result in a value outside of
  the valid range. If the range is exceeded, the operation results in an overflow
  exception. A policy that results in an error is ignored, meaning that a Permit
  policy might unexpectedly fail to allow access, or a Forbid policy might
  unexpectedly fail to block access.

## Data encryption

Amazon Verified Permissions automatically encrypts all customer data such as policies with an
AWS managed key. Amazon Verified Permissions also allows for customers to utilize a customer managed key to encrypt their data.

For detailed information about using customer managed keys for encryption, see [Encrypting Resources in Amazon Verified Permissions](security-data-protection-cmk.md "security-data-protection-cmk.md").
