# SEC08-BP01 Implement secure key management

Secure key management includes the storage, rotation, access
control, and monitoring of key material required to secure data at
rest for your workload.

**Desired outcome:** You have a
scalable, repeatable, and automated key management mechanism. The
mechanism enforces least privilege access to key material and
provides the correct balance between key availability,
confidentiality, and integrity. You monitor access to the keys, and
if rotation of key material is required, you rotate them using an
automated process. You do not allow key material to be accessed by
human operators.

**Common anti-patterns:**

- Human access to unencrypted key material.
- Creating custom cryptographic algorithms.
- Overly broad permissions to access key material.

**Benefits of establishing this best practice:** By establishing a
secure key management mechanism for your workload, you can help provide protection for your
content against unauthorized access. Additionally, you may be subject to regulatory requirements
to encrypt your data. An effective key management solution can provide technical mechanisms
aligned to those regulations to protect key material.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Encryption of data at rest is a fundamental security control. To
implement this control, your workload needs a mechanism to
securely store and manage the key material used to encrypt your
data at rest.

AWS offers the AWS Key Management Service (AWS KMS) to provide
durable, secure, and redundant storage for AWS KMS keys.
[Many
AWS services integrate with AWS KMS](https://aws.amazon.com/kms/features/#integration "https://aws.amazon.com/kms/features/#integration") to support encryption
of your data. AWS KMS uses FIPS 140-3 Level 3 validated hardware
security modules to protect your keys. There is no mechanism to
export AWS KMS keys in plain text.

When deploying workloads using a multi-account strategy, you
should keep AWS KMS keys in the same account as the workload that
uses them.
[This
distributed model](../../../prescriptive-guidance/latest/security-reference-architecture/application.md#app-kms "../../../prescriptive-guidance/latest/security-reference-architecture/application.md#app-kms") places the responsibility for managing
the AWS KMS keys with your team. In other use cases, your
organization may choose to store AWS KMS keys into a centralized
account. This centralized structure requires additional policies
to enable the cross-account access required for the workload
account to access keys stored in the centralized account, but may
be more applicable in use cases where a single key is shared
across multiple AWS accounts.

Regardless of where the key material is stored, you should tightly
control access to the key through the use of
[key
policies](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") and IAM policies. Key policies are the primary way
to control access to an AWS KMS key. Additionally, AWS KMS key
grants can provide access to AWS services to encrypt and decrypt
data on your behalf. Review the
[guidance
for access control to your AWS KMS keys](../../../kms/latest/developerguide/iam-policies-best-practices.md "../../../kms/latest/developerguide/iam-policies-best-practices.md").

You should monitor the use of encryption keys to detect unusual
access patterns. Operations performed using AWS managed keys and
customer managed keys stored in AWS KMS can be logged in AWS CloudTrail and should be reviewed periodically. Pay special
attention to monitoring key destruction events. To mitigate
accidental or malicious destruction of key material, key
destruction events do not delete the key material immediately.
Attempts to delete keys in AWS KMS are subject to a
[waiting
period](../../../kms/latest/developerguide/deleting-keys.md#deleting-keys-how-it-works "../../../kms/latest/developerguide/deleting-keys.md#deleting-keys-how-it-works"), which defaults to 30 days and a minimum of 7 days,
providing administrators time to review these actions and roll
back the request if necessary.

Most AWS services use AWS KMS in a way that is transparent to you

- your only requirement is to decide whether to use an AWS managed
  or customer managed key. If your workload requires the direct use
  of AWS KMS to encrypt or decrypt data, you should use
  [envelope
  encryption](../../../kms/latest/developerguide/concepts.md#enveloping "../../../kms/latest/developerguide/concepts.md#enveloping") to protect your data. The
  [AWS Encryption SDK](../../../encryption-sdk/latest/developer-guide/introduction.md "../../../encryption-sdk/latest/developer-guide/introduction.md") can provide your applications client-side
  encryption primitives to implement envelope encryption and
  integrate with AWS KMS.

### Implementation steps

1. Determine the appropriate
   [key
   management options](../../../kms/latest/developerguide/concepts.md#key-mgmt "../../../kms/latest/developerguide/concepts.md#key-mgmt") (AWS managed or customer managed)
   for the key.
   1. For ease of use, AWS offers AWS owned and AWS managed
      keys for most services, which provide encryption-at-rest
      capability without the need to manage key material or
      key policies.
   2. When using customer managed keys, consider the default
      key store to provide the best balance between agility,
      security, data sovereignty, and availability. Other use
      cases may require the use of custom key stores with
      [AWS CloudHSM](https://aws.amazon.com/cloudhsm/ "https://aws.amazon.com/cloudhsm/") or the
      [external
      key store](../../../kms/latest/developerguide/keystore-external.md "../../../kms/latest/developerguide/keystore-external.md").

2. Review the list of services that you are using for your
   workload to understand how AWS KMS integrates with the
   service. For example, EC2 instances can use encrypted EBS
   volumes, verifying that Amazon EBS snapshots created from
   those volumes are also encrypted using a customer managed
   key and mitigating accidental disclosure of unencrypted
   snapshot data.
   1. [How
      AWS services use AWS KMS](../../../kms/latest/developerguide/service-integration.md "../../../kms/latest/developerguide/service-integration.md")
   2. For detailed information about the encryption options
      that an AWS service offers, see the Encryption at Rest
      topic in the user guide or the developer guide for the
      service.

3. Implement AWS KMS: AWS KMS makes it simple for you to create
   and manage keys and control the use of encryption across a
   wide range of AWS services and in your applications.
   1. [Getting
      started: AWS Key Management Service (AWS KMS)](../../../kms/latest/developerguide/getting-started.md "../../../kms/latest/developerguide/getting-started.md")
   2. Review the
      [best
      practices for access control to your AWS KMS
      keys](../../../kms/latest/developerguide/iam-policies-best-practices.md "../../../kms/latest/developerguide/iam-policies-best-practices.md").

4. Consider AWS Encryption SDK: Use the AWS Encryption SDK with
   AWS KMS integration when your application needs to encrypt
   data client-side.
   1. [AWS Encryption SDK](../../../encryption-sdk/latest/developer-guide/introduction.md "../../../encryption-sdk/latest/developer-guide/introduction.md")

5. Enable
   [IAM Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md") to automatically review and notify if
   there are overly broad AWS KMS key policies.
   1. Consider using
      [custom
      policy checks](../../../access-analyzer/latest/APIReference/API_CheckNoPublicAccess.md "../../../access-analyzer/latest/APIReference/API_CheckNoPublicAccess.md") to verify that a resource policy
      update does not grant public access to KMS Keys.

6. Enable
   [Security Hub](../../../securityhub/latest/userguide/kms-controls.md "../../../securityhub/latest/userguide/kms-controls.md") to receive notifications if there are
   misconfigured key policies, keys scheduled for deletion, or
   keys without automated rotation enabled.
7. Determine the logging level appropriate for your AWS KMS
   keys. Since calls to AWS KMS, including read-only events,
   are logged, the CloudTrail logs associated with AWS KMS can
   become voluminous.
   1. Some organizations prefer to segregate the AWS KMS
      logging activity into a separate trail. For more detail,
      see the
      [Logging
      AWS KMS API calls with CloudTrail](../../../kms/latest/developerguide/logging-using-cloudtrail.md "../../../kms/latest/developerguide/logging-using-cloudtrail.md") section of the
      AWS KMS developers guide.

## Resources

**Related documents:**

- [AWS Key Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")
- [AWS cryptographic services and tools](../../../crypto/latest/userguide/awscryp-overview.md "../../../crypto/latest/userguide/awscryp-overview.md")
- [Protecting
  Amazon S3 Data Using Encryption](../../../AmazonS3/latest/dev/UsingEncryption.md "../../../AmazonS3/latest/dev/UsingEncryption.md")
- [Envelope
  encryption](../../../kms/latest/developerguide/concepts.md#enveloping "../../../kms/latest/developerguide/concepts.md#enveloping")
- [Digital sovereignty pledge](https://aws.amazon.com/blogs/security/aws-digital-sovereignty-pledge-control-without-compromise/ "https://aws.amazon.com/blogs/security/aws-digital-sovereignty-pledge-control-without-compromise/")
- [Demystifying
  AWS KMS key operations, bring your own key, custom key store, and
  ciphertext portability](https://aws.amazon.com/blogs/security/demystifying-kms-keys-operations-bring-your-own-key-byok-custom-key-store-and-ciphertext-portability/ "https://aws.amazon.com/blogs/security/demystifying-kms-keys-operations-bring-your-own-key-byok-custom-key-store-and-ciphertext-portability/")
- [AWS Key Management Service cryptographic details](../../../kms/latest/cryptographic-details/intro.md "../../../kms/latest/cryptographic-details/intro.md")

**Related videos:**

- [How
  Encryption Works in AWS](https://youtu.be/plv7PQZICCM "https://youtu.be/plv7PQZICCM")
- [Securing
  Your Block Storage on AWS](https://youtu.be/Y1hE1Nkcxs8 "https://youtu.be/Y1hE1Nkcxs8")
- [AWS data protection: Using locks, keys, signatures, and
  certificates](https://www.youtube.com/watch?v=lD34wbc7KNA "https://www.youtube.com/watch?v=lD34wbc7KNA")

**Related examples:**

- [Implement
  advanced access control mechanisms using AWS KMS](https://catalog.workshops.aws/advkmsaccess/en-US/introduction "https://catalog.workshops.aws/advkmsaccess/en-US/introduction")
