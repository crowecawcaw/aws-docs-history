# Data protection in Amazon Q Developer

The AWS
[shared
responsibility model](http://aws.amazon.com/compliance/shared-responsibility-model/ "http://aws.amazon.com/compliance/shared-responsibility-model/") applies to data protection in Amazon Q Developer. As described in this
model, AWS is responsible for protecting the global infrastructure that runs
all of the AWS Cloud. You are responsible for maintaining control over your
content that is hosted on this infrastructure. You are also responsible for the security
configuration and management tasks for the AWS services that you use. For more information
about data privacy, see the [Data Privacy FAQ](http://aws.amazon.com/compliance/data-privacy-faq "http://aws.amazon.com/compliance/data-privacy-faq"). For information about data protection in Europe, see the [AWS Shared Responsibility Model and GDPR](http://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr "http://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr") blog post on the
_AWS Security Blog_.

For data protection purposes, we recommend that you protect AWS account
credentials and set up individual users with AWS Identity and Access Management (IAM). That
way each user is given only the permissions necessary to fulfill their job duties. We also
recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We recommend TLS 1.2 or
  later.
- Set up API and user activity logging with AWS CloudTrail.
- Use AWS encryption solutions, along with all default security controls
  within AWS services.
- Use advanced managed security services such as Amazon Macie, which assists
  in discovering and securing sensitive data that is stored in Amazon S3.
- If you require FIPS 140-2 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more
  information about the available FIPS endpoints, see [Federal Information Processing Standard
  (FIPS) 140-2](http://aws.amazon.com/compliance/fips/ "http://aws.amazon.com/compliance/fips/").
  We strongly recommend that you never put confidential or sensitive information, such as
  your customers' email addresses, into [tags](../../../tag-editor/latest/userguide/security_data-protection.md "../../../tag-editor/latest/userguide/security_data-protection.md") or free-form
  text fields such as a **Name** field. This includes when you work
  with Amazon Q or other AWS services using the AWS Management Console, API, AWS Command Line Interface (AWS CLI), or AWS
  SDKs. Any data that you enter into tags or free-form text fields used for names may be used
  for billing or diagnostic logs. For more information about how Amazon Q Developer uses content, see
  [Amazon Q Developer service improvement](service-improvement.md "service-improvement.md").

###### Topics

- [Data storage in Amazon Q Developer](data-storage.md "data-storage.md")
- [Data encryption in Amazon Q Developer](data-encryption.md "data-encryption.md")
- [Amazon Q Developer service improvement](service-improvement.md "service-improvement.md")
- [Opt out of data sharing in the IDE and command line](opt-out-IDE.md "opt-out-IDE.md")
- [Cross-region processing in Amazon Q Developer](cross-region-processing.md "cross-region-processing.md")
