After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Data protection in Amazon FinSpace

The [AWS
shared responsibility model](http://aws.amazon.com/compliance/shared-responsibility-model/ "http://aws.amazon.com/compliance/shared-responsibility-model/") applies to data protection in Amazon FinSpace. As described
in this model, AWS is responsible for protecting the global infrastructure that runs all
of the AWS Cloud. You are responsible for maintaining control over your content that is
hosted on this infrastructure. This content includes the security configuration and
management tasks for the AWS services that you use. For more information about data
privacy, see the [Data
privacy FAQ](http://aws.amazon.com/compliance/data-privacy-faq "http://aws.amazon.com/compliance/data-privacy-faq"). For information about data protection in Europe, see the [AWS shared
responsibility model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security
Blog_.

For data protection purposes, we recommend that you protect AWS account credentials
and set up individual user with AWS Identity and Access Management (IAM). That way each user is given only the
permissions necessary to fulfill their job duties. We also recommend that you secure your
data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use TLS to communicate with AWS resources. Clients must support TLS 1.2.
- Set up API and user activity logging with AWS CloudTrail.
- Use AWS encryption solutions, along with all default security controls within
  AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in
  discovering and securing personal data that is stored in Amazon S3.
- If you require FIPS 140-2 validated cryptographic modules when accessing AWS
  through a command line interface or an API, use a FIPS endpoint. For more information
  about the available FIPS endpoints, see [Federal information processing
  standard (FIPS) 140-2](http://aws.amazon.com/compliance/fips/ "http://aws.amazon.com/compliance/fips/")
  We strongly recommend that you never put sensitive identifying information, such as your
  customers' account numbers, into free-form fields such as a **Name** field. This includes when you work with FinSpace or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into FinSpace or
  other services might get picked up for inclusion in diagnostic logs. When you provide a URL
  to an external server, don't include credentials information in the URL to validate your
  request to that server.

######

Topics

- [Data encryption in Amazon FinSpace](data-encryption.md "data-encryption.md")
- [Inter-network traffic privacy in
  Amazon FinSpace Dataset browser](inter-network-traffic-privacy.md "inter-network-traffic-privacy.md")
