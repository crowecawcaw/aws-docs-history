Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Data protection in Amazon Lookout for Metrics

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in Amazon Lookout for Metrics. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Lookout for Metrics or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

###### Sections

- [Encryption in transit](#security-privacy-intransit "#security-privacy-intransit")
- [Encryption at rest](#security-privacy-atrest "#security-privacy-atrest")

## Encryption in transit

Lookout for Metrics API endpoints support secure connections only over HTTPS. When you manage Lookout for Metrics resources with the
AWS Management Console, AWS SDK, or the Lookout for Metrics API, all communication is encrypted with Transport Layer Security (TLS).

For a complete list of API endpoints, see [AWS Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in
the _AWS General Reference._

## Encryption at rest

Lookout for Metrics always encrypts a detector's dataset at rest. Additionally, you can [configure Lookout for Metrics to use an encryption key](detectors-manage.md "detectors-manage.md") that you create and manage in AWS Key Management Service. These are referred to
as _customer managed_ AWS KMS key or customer managed keys. If you don't
configure a customer managed key, Lookout for Metrics uses a key that the service manages.

Additionally, Lookout for Metrics encrypts your resources' configuration at rest with a key that it manages. This includes
the names of fields or columns in your datasource that you use as [measures and dimensions](gettingstarted-concepts.md#gettingstarted-concepts-metrics "gettingstarted-concepts.md#gettingstarted-concepts-metrics"). You can't configure Lookout for Metrics to use a CMK for configuration data.
