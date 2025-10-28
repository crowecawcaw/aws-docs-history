# Data protection in AWS Secrets Manager

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS Secrets Manager. As described in this model, AWS is
responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are
responsible for maintaining control over your content that is hosted on this infrastructure.
This content includes the security configuration and management tasks for the AWS services
that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq "https://aws.amazon.com/compliance/data-privacy-faq"). For information about data protection in Europe, see the [AWS Shared
Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security
Blog_.

For data protection purposes, we recommend that you protect AWS account credentials and
set up individual user accounts with AWS Identity and Access Management (IAM). That way each user is given only the
permissions necessary to fulfill their job duties. We also recommend that you secure your data
in the following ways:

- Use [multi-factor authentication (MFA)](../../../IAM/latest/UserGuide/best-practices.md#enable-mfa-for-privileged-users "../../../IAM/latest/UserGuide/best-practices.md#enable-mfa-for-privileged-users") with each account.
- Use SSL/TLS to communicate with AWS resources. Secrets Manager supports TLS 1.2 and 1.3 in all Regions. Secrets Manager also supports a hybrid [post-quantum key exchange option for TLS (PQTLS)](pqtls.md "pqtls.md") network encryption protocol.
- Sign your programmatic requests to Secrets Manager by using an access key ID and a secret access key associated with an IAM principal. Or you can use [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate temporary security credentials to sign requests.
- Set up API and user activity logging with AWS CloudTrail. See [Log AWS Secrets Manager events with AWS CloudTrail](monitoring-cloudtrail.md "monitoring-cloudtrail.md").
- If you require FIPS 140-2 validated cryptographic modules when accessing AWS through
  a command line interface or an API, use a FIPS endpoint. See [AWS Secrets Manager endpoints](asm_access.md#endpoints "asm_access.md#endpoints").
- If you use the AWS CLI to access Secrets Manager, [Mitigate the risks of using the AWS CLI
  to store your AWS Secrets Manager secrets](security_cli-exposure-risks.md "security_cli-exposure-risks.md").

## Encryption at rest

Secrets Manager uses encryption via AWS Key Management Service (AWS KMS) to protect the confidentiality of data at
rest. AWS KMS provides a key storage and encryption service used by many AWS services. Every
secret in Secrets Manager is encrypted with a unique data key. Each data key is protected by a KMS key.
You can choose to use default encryption with the Secrets Manager
AWS managed key for the account, or you can create your own customer managed key in AWS KMS. Using a
customer managed key gives you more granular authorization controls over your KMS key activities.
For more information, see [Secret encryption and decryption in AWS Secrets Manager](security-encryption.md "security-encryption.md").

## Encryption in transit

Secrets Manager provides secure and private endpoints for encrypting data in transit. The secure and
private endpoints allows AWS to protect the integrity of API requests to Secrets Manager. AWS
requires API calls be signed by the caller using X.509 certificates and/or a Secrets Manager Secret
Access Key. This requirement is stated in the [Signature Version 4 Signing Process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md")
(Sigv4).

If you use the AWS Command Line Interface (AWS CLI) or any of the AWS SDKs to make calls to AWS, you
configure the access key to use. Then those tools automatically use the access key to sign the
requests for you. See [Mitigate the risks of using the AWS CLI
to store your AWS Secrets Manager secrets](security_cli-exposure-risks.md "security_cli-exposure-risks.md").

## Inter-network traffic privacy

AWS offers options for maintaining privacy when routing traffic through known and
private network routes.

**Traffic between service and on-premises clients and applications**

You have two connectivity options between your private network and AWS Secrets Manager:

- An AWS Site-to-Site VPN connection. For more information, see [What is AWS Site-to-Site
  VPN?](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md")
- An AWS Direct Connect connection. For more information, see [What is AWS
  Direct Connect?](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md")

**Traffic between AWS resources in the same Region**

If you want to secure traffic between Secrets Manager and API clients in AWS, set up an [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/") to privately access
Secrets Manager API endpoints.

## Encryption key management

When Secrets Manager needs to encrypt a new version of the protected secret data, Secrets Manager sends a
request to AWS KMS to generate a new data key from the KMS key. Secrets Manager uses this data key for
[envelope encryption](../../../kms/latest/developerguide/concepts.md#enveloping "../../../kms/latest/developerguide/concepts.md#enveloping"). Secrets Manager stores
the encrypted data key with the encrypted secret. When the secret needs to be decrypted, Secrets Manager
asks AWS KMS to decrypt the data key. Secrets Manager then uses the decrypted data key to decrypt the
encrypted secret. Secrets Manager never stores the data key in unencrypted form and removes the key
from memory as soon as possible. For more information, see [Secret encryption and decryption in AWS Secrets Manager](security-encryption.md "security-encryption.md").
