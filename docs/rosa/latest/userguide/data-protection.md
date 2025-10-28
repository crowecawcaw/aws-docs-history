# Data protection in ROSA

The [Overview of responsibilities for ROSA](rosa-responsibilities.md "rosa-responsibilities.md") documentation and [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") define data protection in ROSA. AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud.
Red Hat is responsible for protecting the cluster infrastructure and underlying service platform.
The customer is responsible for maintaining control over content that is hosted on this infrastructure.
This content includes the security configuration and management tasks for the AWS services that you use.
For more information about data privacy, see the [Data Privacy FAQ](http://aws.amazon.com/compliance/data-privacy-faq "http://aws.amazon.com/compliance/data-privacy-faq").
For information about data protection in Europe, see the [AWS Shared Responsibility Model and GDPR](http://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr "http://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr") blog post on the _AWS Security Blog_.

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS Identity and Access Management (IAM).
That way, each user is given only the permissions necessary to fulfill their job duties.
We also recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
- Set up API and user activity logging with AWS CloudTrail.
- Use AWS encryption solutions, along with all default security controls within AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
- If you require FIPS 140-2 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint.
  For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-2](http://aws.amazon.com/compliance/fips/ "http://aws.amazon.com/compliance/fips/").
  We strongly recommend that you never put sensitive identifying information, such as your customers' account numbers, into free-form fields such as a **Name** field.
  This includes when you work with ROSA or other AWS services using the console, API, AWS CLI, or AWS SDKs.
  Any data that you enter into ROSA or other services might get picked up for inclusion in diagnostic logs.
  When you provide a URL to an external server, don’t include credentials information in the URL to validate your request to that server.

###### Topics

- [Data encryption](data-protection-encryption.md "data-protection-encryption.md")
