# Data protection in IAM Identity Center

The AWS [Shared
Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") applies to data protection in AWS IAM Identity Center. As described in this
model, AWS is responsible for protecting the global infrastructure that runs all of the AWS
cloud. You are responsible for maintaining control over your content that is hosted on this
infrastructure. You are also responsible for the security configuration and management tasks for
the AWS services that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/"). For
information about data protection in Europe, see the [AWS
Shared Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security
Blog_.

We recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with IAM Identity Center.
- Use TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
- Set up API and user activity logging with AWS CloudTrail. For information about using
  CloudTrail trails to capture AWS activities, see [Working
  with CloudTrail trails](../../../awscloudtrail/latest/userguide/cloudtrail-trails.md "../../../awscloudtrail/latest/userguide/cloudtrail-trails.md") in the _AWS CloudTrail User Guide_.
- Use AWS encryption solutions, along with all default security controls within AWS
  services.
  We strongly recommend that you never put confidential or sensitive information, such as
  your customers’ email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS IAM Identity Center, or other AWS
  services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or
  free-form text fields used for names may be used for diagnostic logs.

## Encryption in transit

IAM Identity Center protects data in transit, as it travels to and from the service, by automatically
encrypting all inter-network data using the Transport Layer Security (TLS) 1.2 or TLS 1.3
encryption protocol. Direct HTTPS requests authenticated with IAM and sent to the IAM Identity Center APIs,
Identity Store API, or OIDC API, are signed using the [AWS
Signature Version 4 Algorithm](../../../general/latest/gr/sigv4_signing.md "../../../general/latest/gr/sigv4_signing.md") to establish a secure connection.

## Data privacy

With IAM Identity Center, you retain control of your organization’s data. Your user and group
identities stored in IAM Identity Center are shared with other AWS services such as [AWS
managed applications](awsapps.md "awsapps.md") only if you enable them with IAM Identity Center, and if needed by those
services.

For additional information, see the [AWS Data Privacy
FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/").

## Data retention

IAM Identity Center stores your data such as user and group identities, and metadata, until you delete
them
from the service. When you delete an IAM Identity Center instance, the data it contains is also deleted.
