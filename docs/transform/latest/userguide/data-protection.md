# Data protection in AWS Transform

The AWS
[shared
responsibility model](http://aws.amazon.com/compliance/shared-responsibility-model/ "http://aws.amazon.com/compliance/shared-responsibility-model/") applies to data protection in AWS Transform. As described in this
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
  with AWS Transform or other AWS services using the AWS Management Console, API, AWS Command Line Interface (AWS CLI), or AWS SDKs.
  Any data that you enter into tags or free-form text fields used for names may be used for
  billing or diagnostic logs. For more information about how AWS Transform uses content, see [AWS Transform service improvement](service-improvement.md "service-improvement.md").

AWS Transform stores your questions, its responses, and additional context, such as console
metadata and code in your IDE, to generate responses to your questions. For
information about how data is encrypted, see [Data encryption in AWS Transform](data-encryption.md "data-encryption.md"). For information about how AWS may use some questions
that you ask AWS Transform and its responses to improve our services, see [AWS Transform service improvement](service-improvement.md "service-improvement.md").

In AWS Transform, your data is stored in the AWS Region where your AWS Transform profile was
created.

With cross-inferencing, your requests to AWS Transform may be processed in a different Region
within the geography where your data is stored. For more information, see [Cross-Region inference](cross-region-processing.md#cross-region-inference "cross-region-processing.md#cross-region-inference").

###### Topics

- [Cross-region processing in AWS Transform](cross-region-processing.md "cross-region-processing.md")
- [Data encryption in AWS Transform](data-encryption.md "data-encryption.md")
- [AWS Transform service improvement](service-improvement.md "service-improvement.md")
