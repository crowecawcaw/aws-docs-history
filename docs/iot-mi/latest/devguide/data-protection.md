# Data protection in managed integrations

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in Managed integrations for AWS IoT Device Management. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with managed integrations for AWS IoT Device Management or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Data encryption at rest for managed integrations

Managed integrations for AWS IoT Device Management encrypts sensitive customer data at rest by default using encryption keys.

There are two types of encryption keys that are used to protect sensitive data for
managed integrations customers:

**Customer managed keys (CMK)**

Managed integrations supports the use of symmetric customer managed key that you can create, own,
and manage. You have full control over these KMS keys, including establishing and
maintaining their key policies, IAM policies, and grants, enabling and disabling them,
rotating their cryptographic material, adding tags, creating aliases that refer to the
KMS keys, and scheduling the KMS keys for deletion.

**AWS owned keys**

Managed integrations uses these keys by default to automatically encrypt sensitive customer data.
You can't view, manage, or audit their use. You don't have to take any action or change any
programs to protect the keys that encrypt your data. Encryption of data at rest by default
helps reduce the operational overhead and complexity involved in protecting sensitive data. At
the same time, it enables you to build secure applications that meet strict encryption
compliance and regulatory requirements.

The default encryption key used is AWS owned keys. Alternatively, the optional API to
update your encryption key is [`PutDefaultEncryptionConfiguration`](../APIReference/API_PutDefaultEncryptionConfiguration.md "../APIReference/API_PutDefaultEncryptionConfiguration.md").

For more information on the types of AWS KMS encryption keys, see [AWS KMS
keys](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md").

### AWS KMS usage for managed integrations

Managed integrations encrypts and decrypts all customer data using envelope encryption. This
type of encryption will take your plaintext data and encrypt it with a data key. Next, an
encryption key called a wrapping key will encrypt the original data key used to encrypt your
plaintext data. In envelope encryption, additional wrapping keys can be used to encrypt
existing wrapping keys that are closer in degrees of separation from the original data key.
Since the original data key is encrypted by a wrapping key stored separately, you can store
the original data key and encrypted plaintext data in the same location. A keyring is used
to generate, encrypt, and decrypt data keys in addition to which wrapping key is used to
encrypt and decrypt the data key.

###### Note

The AWS Database Encryption SDK provides envelope encryption for your client-side
encryption implementation. For more information on the AWS Database Encryption SDK, see
[What
is the AWS Database Encryption SDK?](../../../database-encryption-sdk/latest/devguide/what-is-database-encryption-sdk.md "../../../database-encryption-sdk/latest/devguide/what-is-database-encryption-sdk.md")

For more information on envelope encryption, data keys, wrapping keys, and keyrings, see
[Envelope
encryption](../../../kms/latest/developerguide/kms-cryptography.md#enveloping "../../../kms/latest/developerguide/kms-cryptography.md#enveloping"), [Data key](../../../database-encryption-sdk/latest/devguide/concepts.md#data-key "../../../database-encryption-sdk/latest/devguide/concepts.md#data-key"),
[Wrapping
key](../../../database-encryption-sdk/latest/devguide/concepts.md#wrapping-key "../../../database-encryption-sdk/latest/devguide/concepts.md#wrapping-key"), and [Keyrings](../../../database-encryption-sdk/latest/devguide/concepts.md#keyring-concept "../../../database-encryption-sdk/latest/devguide/concepts.md#keyring-concept").

Managed integrations requires the services to use your customer managed key for the following
internal operations:

- Send `DescribeKey` requests to AWS KMS to verify that the symmetric
  customer managed key ID provided when doing the rotation of the data keys.
- Send `GenerateDataKeyWithoutPlaintext` requests to AWS KMS to generate data
  keys encrypted by your customer managed key.
- Send `ReEncrypt*` requests to AWS KMS to reencrypt data keys by your
  customer managed key.
- Send `Decrypt` requests to AWS KMS to decrypt data by your customer managed
  key.

**Types of data encrypted using encryption keys**

Managed integrations uses encryption keys to encrypt multiple types of data stored at rest. The
following list outlines types of data encrypted at rest using encryption keys:

- Cloud--to-cloud (C2C) connector events such as device discovery and device status
  update.
- Creation of a _Managed Thing_ that represents the physical device and a
  device profile containing the capabilities for a specific device type. For more
  information on a device and device profile, see [Device](device-and-device-profile-lifecycle-management.md#device "device-and-device-profile-lifecycle-management.md#device") and [Device](device-and-device-profile-lifecycle-management.md#device "device-and-device-profile-lifecycle-management.md#device").
- Managed integrations notifications on various aspects of your device implementation. For
  more information on managed integrations notifications, see [Set up managed integrations
  notifications](managedintegrations-notifications.md#managedintegrations-notification-setup "managedintegrations-notifications.md#managedintegrations-notification-setup").
- Personally Identifiable Information (PII) of an end-user such as device
  authentication material, device serial number, end-user's name, device identifier, and
  device Amazon Resource Name (arn).

### How managed integrations uses key policies in

AWS KMS

For branch key rotation and asynchronous calls, managed integrations requires a key policy to
use your encryption key. A key policy is used for the following reasons:

- Programmatically authorize the use of an encryption key to other AWS
  principals.

For an example of a key policy used to manage access to your encryption key in
managed integrations, see [Create an encryption key](#encryption-rest-create-key "#encryption-rest-create-key")

###### Note

For an AWS owned key, a key policy is not required as the AWS owned key is owned
by AWS and you can't view, manage, or use it. Managed integrations uses the AWS owned key by
default to automatically encrypt your sensitive customer data.

In addition to using key policies for managing your encryption configuration with AWS KMS
keys, managed integrations uses IAM policies. For more information on IAM policies, see [Policies and
permissions in AWS Identity and Access Management.](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md")

### Create an encryption key

You can create an encryption key by using the AWS Management Console or the AWS KMS APIs.

**To create an encryption key**

Follow the steps for [Creating a KMS key](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the AWS Key Management Service Developer Guide.

**Key policy**

A key policy statement controls access to an AWS KMS key. Each AWS KMS key will contain only
one key policy. That key policy determines which AWS principals may use the key and how
they may use it. For more information on managing access and usage of AWS KMS keys using key
policy statements, see [Managing access using policies](../../../kms/latest/developerguide/access-glossary.md#security_iam_access-manage "../../../kms/latest/developerguide/access-glossary.md#security_iam_access-manage").

The following is an example of a key policy statement you can use for managing access
and usage to AWS KMS keys stored in your AWS account for managed integrations:

```
{
   "Statement" : [
    {
      "Sid" : "Allow access to principals authorized to use managed integrations",
      "Effect" : "Allow",
      "Principal" : {
        //Note: Both role and user are acceptable.
        "AWS": "arn:aws:iam::111122223333:user/username",
        "AWS": "arn:aws:iam::111122223333:role/roleName"
      },
      "Action" : [
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Decrypt",
        "kms:ReEncrypt*"
      ],
      "Resource" : "arn:aws:kms:region:111122223333:key/key_ID",
      "Condition" : {
        "StringEquals" : {
          "kms:ViaService" : "iotmanagedintegrations.amazonaws.com"
        },
        "ForAnyValue:StringEquals": {
          "kms:EncryptionContext:aws-crypto-ec:iotmanagedintegrations": "111122223333"
        },
        "ArnLike": {
          "aws:SourceArn": [
            "arn:aws:iotmanagedintegrations:<region>:<accountId>:managed-thing/<managedThingId>",
            "arn:aws:iotmanagedintegrations:<region>:<accountId>:credential-locker/<credentialLockerId>",
            "arn:aws:iotmanagedintegrations:<region>:<accountId>:provisioning-profile/<provisioningProfileId>",
            "arn:aws:iotmanagedintegrations:<region>:<accountId>:ota-task/<otaTaskId>"
          ]
        }
      }
    },
    {
      "Sid" : "Allow access to principals authorized to use managed integrations for async flow",
      "Effect" : "Allow",
      "Principal" : {
        "Service": "iotmanagedintegrations.amazonaws.com"
      },
      "Action" : [
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Decrypt",
        "kms:ReEncrypt*"
      ],
      "Resource" : "arn:aws:kms:region:111122223333:key/key_ID",
      "Condition" : {
        "ForAnyValue:StringEquals": {
          "kms:EncryptionContext:aws-crypto-ec:iotmanagedintegrations": "111122223333"
        },
        "ArnLike": {
          "aws:SourceArn": [
            "arn:aws:iotmanagedintegrations:<region>:<accountId>:managed-thing/<managedThingId>",
            "arn:aws:iotmanagedintegrations:<region>:<accountId>:credential-locker/<credentialLockerId>",
            "arn:aws:iotmanagedintegrations:<region>:<accountId>:provisioning-profile/<provisioningProfileId>",
            "arn:aws:iotmanagedintegrations:<region>:<accountId>:ota-task/<otaTaskId>"
          ]
        }
      }
    },
    {
      "Sid" : "Allow access to principals authorized to use managed integrations for describe key",
      "Effect" : "Allow",
      "Principal" : {
        "AWS": "arn:aws:iam::111122223333:user/username"
      },
      "Action" : [
        "kms:DescribeKey",
      ],
      "Resource" : "arn:aws:kms:region:111122223333:key/key_ID",
      "Condition" : {
        "StringEquals" : {
          "kms:ViaService" : "iotmanagedintegrations.amazonaws.com"
        }
      }
    },
    {
      "Sid": "Allow access for key administrators",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:root"
       },
      "Action" : [
        "kms:*"
       ],
      "Resource": "*"
    }
  ]
 }
```

For more information on key stores, see [Key
stores](../../../kms/latest/developerguide/key-store-overview.md "../../../kms/latest/developerguide/key-store-overview.md").

### Updating encryption configuration

The ability to seamlessly update your encryption configuration is critical to managing
your data encryption implementation for managed integrations. When you initially onboard with
managed integrations, you will be prompted to select your encryption configuration. Your options
will be either the default AWS owned keys or create your own AWS KMS key.

**AWS Management Console**

To update your encryption configuration in the AWS Management Console, open the AWS IoT service
homepage and then navigate to **Managed Integration for Unified
Control**>**Settings**>**Encryption**. In the
**Encryption settings** window, you can update your encryption
configuration by selecting a new AWS KMS key for additional encryption protection. Choose
**Customize encryption settings (advanced)** to select an existing AWS KMS
key or you can chose **Create an AWS KMS key** to create your own customer
managed key.

**API Commands**

There are two APIs used for managing your encryption configuration of AWS KMS keys in
managed integrations: `PutDefaultEncryptionConfiuration` and
`GetDefaultEncryptionConfiguration`.

To update the default encryption configuration, call
`PutDefaultEncryptionConfiuration`. For more information on
`PutDefaultEncryptionConfiuration`, see [PutDefaultEncryptionConfiuration](../APIReference/API_PutDefaultEncryptionConfiguration.md "../APIReference/API_PutDefaultEncryptionConfiguration.md").

To view the default encryption configuration, call
`GetDefaultEncryptionConfiguration`. For more information on
`GetDefaultEncryptionConfiguration`, see [GetDefaultEncryptionConfiguration](../APIReference/API_GetDefaultEncryptionConfiguration.md "../APIReference/API_GetDefaultEncryptionConfiguration.md").
