# Data protection in Amazon EBS

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in Amazon Elastic Block Store. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Amazon EBS or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

###### Topics

- [Amazon EBS data security](#data-security "#data-security")
- [Encryption at rest and in transit](#encryption-rest "#encryption-rest")
- [KMS key management](#key-management "#key-management")

## Amazon EBS data security

Amazon EBS volumes are presented to you as raw, unformatted block devices. These devices are logical
devices that are created on the EBS infrastructure and the Amazon EBS service ensures that the devices are
logically empty (that is, the raw blocks are zeroed or they contain cryptographically pseudorandom
data) prior to any use or re-use by a customer.

If you have procedures that require that all data be erased using a specific method, either after
or before use (or both), such as those detailed in **DoD 5220.22-M**
(National Industrial Security Program Operating Manual) or **NIST 800-88**
(Guidelines for Media Sanitization), you have the ability to do so on Amazon EBS. That block-level activity
will be reflected down to the underlying storage media within the Amazon EBS service.

## Encryption at rest and in transit

Amazon EBS encryption is an encryption solution that enables you to encrypt your Amazon EBS volumes and Amazon EBS
snapshots using AWS Key Management Service cryptographic keys. EBS encryption operations occur on the servers that host
Amazon EC2 instances, ensuring the security of both **data-at-rest** and
**data-in-transit** between an instance and its attached volume and any
subsequent snapshots. For more information, see [Amazon EBS encryption](ebs-encryption.md "ebs-encryption.md").

## KMS key management

When you create an encrypted Amazon EBS volume or snapshot, you specify an AWS Key Management Service key. By default, Amazon EBS
uses the AWS managed KMS key for Amazon EBS in your account and Region (`aws/ebs`). However, you
can specify a customer managed KMS key that you create and manage. Using a customer managed KMS key
gives you more flexibility, including the ability to create, rotate, and disable KMS keys.

To use a customer managed KMS key, you must give users permission to use the KMS key. For more
information, see [Permissions for users](ebs-encryption-requirements.md#ebs-encryption-permissions "ebs-encryption-requirements.md#ebs-encryption-permissions").

###### Important

Amazon EBS supports only [symmetric KMS keys](../../../kms/latest/developerguide/concepts.md#symmetric-cmks "../../../kms/latest/developerguide/concepts.md#symmetric-cmks"). You can't use [asymmetric KMS keys](../../../kms/latest/developerguide/symmetric-asymmetric.md#asymmetric-cmks "../../../kms/latest/developerguide/symmetric-asymmetric.md#asymmetric-cmks") to
encrypt an Amazon EBS volume and snapshots. For help determining whether a KMS key is symmetric or asymmetric,
see [Identify asymmetric KMS keys](../../../kms/latest/developerguide/identify-key-types.md#identify-asymm-keys "../../../kms/latest/developerguide/identify-key-types.md#identify-asymm-keys").

For each volume, Amazon EBS asks AWS KMS to generate a unique data key encrypted under the KMS key that you
specify. Amazon EBS stores the encrypted data key with the volume. Then, when you attach the volume to an Amazon EC2
instance, Amazon EBS calls AWS KMS to decrypt the data key. Amazon EBS uses the plaintext data key in hypervisor memory
to encrypt all I/O to the volume. For more information, see [How Amazon EBS encryption works](how-ebs-encryption-works.md "how-ebs-encryption-works.md").
