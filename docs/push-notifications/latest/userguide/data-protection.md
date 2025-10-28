# Data protection in AWS End User Messaging Push

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS End User Messaging Push. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS End User Messaging Push or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Data encryption

AWS End User Messaging Push data is encrypted in transit and at rest. When you submit data to AWS End User Messaging Push, it
encrypts the data as it receives and stores it. When you retrieve data from AWS End User Messaging Push, it transmits
the data to you by using current security protocols.

### Encryption at rest

AWS End User Messaging Push encrypts all the data that it stores for you. This includes configuration data, user
and endpoint data, analytics data, and any data that you add or import into AWS End User Messaging Push. To encrypt
your data, AWS End User Messaging Push uses internal AWS Key Management Service (AWS KMS) keys that the service owns and maintains on your
behalf. We rotate these keys on a regular basis. For information about AWS KMS, see the
[AWS Key Management Service Developer Guide](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md").

## Encryption in transit

AWS End User Messaging Push uses HTTPS and Transport Layer Security (TLS) 1.2 or later to communicate with your
clients and applications. To communicate with other AWS services, AWS End User Messaging Push uses HTTPS and TLS 1.2.
In addition, when you create and manage AWS End User Messaging Push resources by using the console, an AWS SDK, or
the AWS Command Line Interface, all communications are secured using HTTPS and TLS 1.2.

## Key management

To encrypt your AWS End User Messaging Push data, AWS End User Messaging Push uses internal AWS KMS keys that the service owns and
maintains on your behalf. We rotate these keys on a regular basis. You can't provision and use
your own AWS KMS or other keys to encrypt data that you store in AWS End User Messaging Push.

## Inter-network traffic privacy

_Internetwork traffic privacy_ refers to securing
connections and traffic between AWS End User Messaging Push and your on-premises clients and applications, and
between AWS End User Messaging Push and other AWS resources in the same AWS Region. The following features and
practices can help you ensure internetwork traffic privacy for AWS End User Messaging Push.

### Traffic between

AWS End User Messaging Push and on-premises clients and applications

To establish a private connection between AWS End User Messaging Push and clients and applications on your
on-premises network, you can use AWS Direct Connect. This enables you to link your network to an
AWS Direct Connect location by using a standard, fiber-optic Ethernet cable. One end of the
cable is connected to your router. The other end is connected to an AWS Direct Connect router. For
more information, see [What is
AWS Direct Connect?](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") in the _AWS Direct Connect User Guide_.

To help secure access to AWS End User Messaging Push through published APIs, we recommend that you comply
with AWS End User Messaging Push requirements for API calls. AWS End User Messaging Push requires clients to use Transport Layer
Security (TLS) 1.2 or later. Clients must also support cipher suites with perfect
forward secrecy (PFS), such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve
Diffie-Hellman Ephemeral (ECDHE). Most modern systems such as Java 7 and later support
these modes.

In addition, requests must be signed using an access key ID and a secret access key
that's associated with an AWS Identity and Access Management (IAM) principal for your AWS account.
Alternatively, you can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate
temporary security credentials to sign requests.

### Traffic between

AWS End User Messaging Push and other AWS resources

To secure communications between AWS End User Messaging Push and other AWS resources in the same AWS
Region, AWS End User Messaging Push uses HTTPS and TLS 1.2 by default.
