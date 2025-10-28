# Data Protection in AWS Security Incident Response

###### Contents

- [Data encryption](data-encryption.md "data-encryption.md")

The AWS
[shared
responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") applies to data protection for the AWS
Security Incident Response service. As described in this model,
AWS is responsible for protecting the infrastructure that runs the
services offered in the AWS Cloud. You are responsible for
maintaining control over your content that is hosted on this
infrastructure. You are also responsible for the security
configuration and management tasks for the AWS services that you
use. For more information about data privacy, see the
[Data
Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/"). For information about data protection in
Europe, see the
[AWS
Shared Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the
_AWS Security Blog_.

For data protection purposes, AWS security best practices state that you should protect AWS
account credentials and set up individual users with AWS IAM
Identity Center or AWS Identity and Access Management (IAM). This
way, each user is given only the permissions necessary to fulfill
their job duties. We also recommend that you secure your data in
the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We require TLS
  1.2 and recommend TLS 1.3.
- Set up API and user activity logging with AWS CloudTrail.
- Use AWS encryption solutions, along with all default security
  controls within AWS services.
- FIPS 140-3 is currently not supported by the service.

You should never put confidential or sensitive information, such
as your email addresses, into tags or free-form text fields such
as a **Name** field. This includes
when you work with AWS Support or other AWS services using the
console, API, AWS CLI, or AWS SDKs. Any data that you enter tags
or free-form text fields used for names may be used for billing or
diagnostic logs. If you provide a URL to an external server, we
**_strongly_**
recommend that you do not include credentials information in the
URL to validate your request to that server.
