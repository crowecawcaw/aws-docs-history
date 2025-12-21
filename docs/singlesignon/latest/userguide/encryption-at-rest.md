# Encryption at rest

IAM Identity Center provides encryption to protect customer data at rest using the following key
types:

- **AWS owned keys (default key type)** — IAM Identity
  Center uses these keys by default to automatically encrypt your data. You can't view,
  manage, audit their use, or use AWS owned keys for other purposes. IAM Identity Center
  handles the key management entirely to keep your data secure, without your having to take
  any action. For more information, see
  [AWS
  owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") in the
  [_AWS Key Management Service
  Developer Guide_](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").
- **Customer managed keys** — In organization instances of
  IAM Identity Center, you can choose a symmetric customer managed key for encryption at rest of your workforce
  identity data such as user and group attributes. You create, own, and manage these
  encryption keys. Because you have full control of this layer of encryption, you can
  perform such tasks as:
  - Establishing and maintaining key policies to restrict access to the key to only IAM
    principals who need access, such as IAM Identity Center and [AWS managed applications](awsapps.md "awsapps.md") in
    the same AWS Organizations and their administrators.
  - Establishing and maintaining IAM policies for access to the key including cross-account
    access
  - Enabling and disabling key policies
  - Rotating key cryptographic material
  - Auditing access to your data that requires key access
  - Adding tags
  - Creating key aliases
  - Scheduling keys for deletion

To learn how to implement a customer managed KMS key in IAM Identity Center see
[Implementing customer managed KMS keys in AWS IAM Identity Center](identity-center-customer-managed-keys.md "identity-center-customer-managed-keys.md"). For more information about customer
managed keys, see
[customer
managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service Developer Guide_.

###### Note

IAM Identity Center automatically enables encryption at rest using AWS owned KMS keys to
protect customer data at no charge. However, AWS KMS charges apply when using a customer managed
key. For more information about pricing, see the
[AWS Key Management Service
pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

**Considerations for implementing customer managed keys:**

- **Dedicated keys**: We recommend creating a new dedicated customer managed KMS key for each IAM Identity Center instance rather than reusing an existing key. This approach provides clearer separation of duties, simplifies access control management, and makes security auditing more straightforward. Having a dedicated key also reduces risk by limiting the impact of key changes to a single IAM Identity Center instance.

###### Note

IAM Identity Center uses [envelope encryption](../../../encryption-sdk/latest/developer-guide/concepts.md#envelope-encryption "../../../encryption-sdk/latest/developer-guide/concepts.md#envelope-encryption") in the encryption of your workforce identity data. Your KMS key plays the role of a wrapping key that encrypts the data key that is actually used to encrypt the data.

For more information on AWS KMS, see [What is AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")

## IAM Identity Center encryption context

An [encryption context](../../../kms/latest/developerguide/encrypt_context.md "../../../kms/latest/developerguide/encrypt_context.md") is an optional set of non-secret key-value pairs that contain additional contextual information about the data. AWS KMS uses the encryption context as additional
authenticated data to support authenticated encryption. When you include an encryption context in a request to encrypt data, AWS KMS binds the encryption context to the encrypted data. To decrypt data, you include the same
encryption context in the request. Refer to the
[AWS KMS
Developer Guide](../../../kms/latest/developerguide/encrypt_context.md "../../../kms/latest/developerguide/encrypt_context.md") for more information about encryption context.

IAM Identity Center uses encryption context keys from the following: aws:sso:instance-arn, aws:identitystore:identitystore-arn, and tenant-key-id. For example, the following encryption context can appear in AWS KMS API operations
invoked by
[IAM
Identity Center API](../APIReference/welcome.md "../APIReference/welcome.md").

```

"encryptionContext": {
    "tenant-key-id": "ssoins-1234567890abcdef",
    "aws:sso:instance-arn": "arn:aws:sso:::instance/ssoins-1234567890abcdef"
}

```

The following encryption context can appear in AWS KMS API operations invoked by
[Identity
Store API](../IdentityStoreAPIReference/welcome.md "../IdentityStoreAPIReference/welcome.md").

```

"encryptionContext": {
    "tenant-key-id": "12345678-1234-1234-1234-123456789012",
    "aws:identitystore:identitystore-arn": "arn:aws:identitystore::123456789012:identitystore/d-1234567890"
}

```

## Using encryption context to control access to your customer

managed key

You can use the encryption context in key policies and IAM policies as
conditions to control access to your symmetric customer managed key. Some
of the key policy templates in the [Advanced KMS key policy statements](advanced-kms-policy.md "advanced-kms-policy.md") include such conditions to ensure the key is used only with
a specific IAM Identity Center instance.

## Monitoring your encryption keys for IAM Identity

Center

When you use a customer managed KMS key with your IAM Identity Center instance, you can use
[AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") or
[Amazon
CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") to track requests that IAM Identity Center sends to AWS KMS. The KMS
API operations that IAM Identity Center calls are listed in [Step 2: Prepare KMS key policy statements](identity-center-customer-managed-keys.md#choose-kms-key-policy-statements "identity-center-customer-managed-keys.md#choose-kms-key-policy-statements"). CloudTrail events for
these API operations contain the encryption context, which enables you to monitor AWS KMS API
operations called by your IAM Identity Center instance to access data encrypted by your
customer managed key.

Example encryption context in a CloudTrail event of an AWS KMS API operation:

```
{
"requestParameters": {
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT",
        "encryptionContext": {
            "aws:sso:instance-arn": "arn:aws:sso:::instance/ssoins-xxxxxxxxxxxxxxxx",
            "tenant-key-id": "ssoins-xxxxxxxxxxxxxxxx"
        }
    }
}

```

## AWS managed applications’ storage, encryption, and deletion of IAM Identity Center identity attributes

Some AWS managed applications that you deploy with AWS IAM Identity Center, such as AWS Systems Manager and Amazon CodeCatalyst, store specific user and group attributes from IAM Identity Center in their own data store. Encryption at rest with a customer managed KMS key in IAM Identity Center does not extend to the IAM Identity Center user and group attributes stored in AWS managed applications. AWS managed applications support different encryption methods for the data they store. Finally, when you delete user and group attributes within IAM Identity Center, these AWS managed applications may continue to store this information past its deletion in IAM Identity Center. Refer to the user guide of your AWS managed applications for encryption and security of data stored within the applications.
