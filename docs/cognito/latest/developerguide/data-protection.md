# Data protection in Amazon Cognito

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in Amazon Cognito (Amazon Cognito). As described in this model, AWS is
responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are
responsible for maintaining control over your content that is hosted on this infrastructure. This content includes the security configuration and management tasks for the AWS services that you use.
For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq "https://aws.amazon.com/compliance/data-privacy-faq").

For data protection purposes, we recommend that you protect AWS account credentials and
set up individual user accounts with AWS Identity and Access Management (IAM). That way each user is given only the
permissions necessary to fulfill their job duties. We also recommend that you secure your data
in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources.
- Set up API and user activity logging with AWS CloudTrail.
- Use AWS encryption solutions, along with all default security controls within AWS
  services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering
  and securing personal data that is stored in Amazon S3.
  We strongly recommend that you never put sensitive identifying information, such as your
  customers' account numbers, into free-form fields such as a **Name** field. This includes when you work with Amazon Cognito or other AWS
  services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  Amazon Cognito or other services might get picked up for inclusion in diagnostic logs. When you
  provide a URL to an external server, don't include credentials information in the URL to
  validate your request to that server.

## Data encryption

Data encryption typically falls into two categories: encryption at rest and encryption in
transit.

**Encryption at rest**

Data within Amazon Cognito is encrypted at rest in accordance with industry standards.

**Encryption in transit**

As a managed service, Amazon Cognito is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access Amazon Cognito through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.

Amazon Cognito user pools and identity pools have IAM-authenticated, unauthenticated, and token-authorized
API operations. Unauthenticated and token-authorized API operations are intended for use by
your customers, the end users of your app. Unauthenticated and token-authorized API operations
are encrypted at rest and in transit. For more information, see [List of API operations grouped by authorization
model](authentication-flows-public-server-side.md#user-pool-apis-auth-unauth "authentication-flows-public-server-side.md#user-pool-apis-auth-unauth").

###### Note

Amazon Cognito encrypts your content internally and doesn't support customer-provided
keys.
