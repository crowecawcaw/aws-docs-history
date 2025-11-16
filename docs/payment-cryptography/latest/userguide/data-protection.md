# Data protection in AWS Payment Cryptography

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS Payment Cryptography. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS Payment Cryptography or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

AWS Payment Cryptography stores and protects your payment encryption keys to make them highly available while providing you with strong and flexible access control.

###### Topics

- [Protecting key material](#key-protection "#key-protection")
- [Data encryption](#data-encryption "#data-encryption")
- [Encryption at rest](#encryption-rest "#encryption-rest")
- [Encryption in transit](#encryption-transit "#encryption-transit")
- [Internetwork traffic privacy](#internetwork "#internetwork")

## Protecting key material

By default, AWS Payment Cryptography protects the cryptographic key material for payment keys managed by the service. In addition, AWS Payment Cryptography offers options for importing key material that is created outside of the service. For technical details about payment keys and key material, see AWS Payment Cryptography Cryptographic Details.

## Data encryption

The data in AWS Payment Cryptography consists of AWS Payment Cryptography keys, the encryption key material they represent, and their usage attributes. Key material exists in plaintext only within AWS Payment Cryptography hardware security modules (HSMs) and only when in use. Otherwise, the key material and attributes are encrypted and stored in durable persistent storage.

The key material that AWS Payment Cryptography generates or loads for payment keys never leaves the boundary of AWS Payment Cryptography HSMs unencrypted. It can be exported encrypted by AWS Payment Cryptography API operations.

## Encryption at rest

AWS Payment Cryptography generates key material for payment keys in PCI PTS HSM-listed HSMs. When not in use, key material is encrypted by an HSM key and written to durable, persistent storage. The key material for Payment Cryptography keys and the encryption keys that protect the key material never leave the HSMs in plaintext form.

Encryption and management of key material for Payment Cryptography keys is handled entirely by the service.

For more details, see AWS Key Management Service Cryptographic Details.

## Encryption in transit

Key material that AWS Payment Cryptography generates or loads for payment keys is never exported or transmitted in AWS Payment Cryptography API operations in cleartext. AWS Payment Cryptography uses key identifiers to represent the keys in API operations.

However, some API operations export keys encrypted by a previously shared or asymmetric key exchange key. Also, customers can use API operations to import encrypted key material for payment keys.

All AWS Payment Cryptography API calls must be signed and be transmitted using Transport Layer Security (TLS). AWS Payment Cryptography requires TLS versions and cipher suites defined by PCI as "strong cryptography". All service endpoints support TLS 1.2—1.3 and hybrid post-quantum TLS.

For more details, see AWS Key Management Service Cryptographic Details.

## Internetwork traffic privacy

AWS Payment Cryptography supports an AWS Management Console and a set of API operations that enable you to create and manage payment keys and use them in cryptographic operations.

AWS Payment Cryptography supports two network connectivity options from your private network to AWS.

- An IPSec VPN connection over the internet.
- AWS Direct Connect, which links your internal network to an AWS Direct Connect location over a standard Ethernet fiber-optic cable.

All Payment Cryptography API calls must be signed and be transmitted using Transport Layer Security (TLS). The calls also require a modern cipher suite that supports perfect forward secrecy. Traffic to the hardware security modules (HSMs) that store key material for payment keys is permitted only from known AWS Payment Cryptography API hosts over the AWS internal network.

To connect directly to AWS Payment Cryptography from your virtual private cloud (VPC) without sending traffic over the public internet, use VPC endpoints, powered by AWS PrivateLink.
For more information, see Connecting to AWS Payment Cryptography through a VPC endpoint.

AWS Payment Cryptography also supports a hybrid post-quantum key exchange option for the Transport Layer Security (TLS) network encryption protocol. You can use this option with TLS when you connect to AWS Payment Cryptography API endpoints.
