# Encryption at rest in AWS IoT FleetWise

AWS IoT FleetWise stores your data in the AWS Cloud and on gateways.

## Data at rest in the AWS Cloud

AWS IoT FleetWise stores data in other AWS services that encrypt data at rest by default.
Encryption at rest integrates with [AWS Key Management Service (AWS KMS)](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") for managing the
encryption key that is used to encrypt your asset property values and aggregate values in
AWS IoT FleetWise. You can choose to use a customer managed key to encrypt asset property values and aggregate
values in AWS IoT FleetWise. You can create, manage, and view your encryption key through AWS KMS.

You can choose an AWS owned key or a customer managed key to encrypt your data.

### How it works

Encryption at rest integrates with AWS KMS for managing the encryption key that is used to encrypt your data.

- AWS owned key – Default encryption key. AWS IoT FleetWise owns this key. You can't
  view, manage, or use this key in your AWS account. You also can't see operations on
  the key in AWS CloudTrail logs. You can use this key at no additional charge.
- Customer managed key – The key is stored in your account, which you create, own, and manage. You have full control over the KMS key. Additional AWS KMS charges apply.

### AWS owned keys

AWS owned keys aren't stored in your account. They're part of a collection of
KMS keys that AWS owns and manages for use in multiple AWS accounts. AWS services can
use AWS owned keys to protect your data.

You can't view, manage, or use AWS owned keys, or audit their use. However, you don't
need to take any action or change any programs to protect keys that encrypt your
data.

You won’t be charged a fee if you use AWS owned keys, and they don’t count against AWS KMS quotas for your account.

### Customer managed keys

Customer managed keys are KMS keys in your account that you create, own, and manage. You have full control over these KMS keys, such as the following:

- Establishing and maintaining their key policies, IAM policies, and grants
- Enabling and disabling them
- Rotating their cryptographic material
- Adding tags
- Creating aliases that refer to them
- Scheduling them for deletion

You can also use CloudTrail and Amazon CloudWatch Logs to track the requests that AWS IoT FleetWise sends to AWS KMS on
your behalf.

If you're using customer managed keys, you must grant AWS IoT FleetWise access to the KMS key stored in
your account. AWS IoT FleetWise uses envelope encryption and key hierarchy to encrypt data. Your AWS KMS
encryption key is used to encrypt the root key of this key hierarchy. For more information,
see [Envelope encryption](../../../kms/latest/developerguide/concepts.md#enveloping "../../../kms/latest/developerguide/concepts.md#enveloping") in the _AWS Key Management Service Developer Guide_.

The following example policy grants AWS IoT FleetWise permissions to use your AWS KMS key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow use of the key",
 "Effect": "Allow",
 "Principal": {
 "Service": "iotfleetwise.amazonaws.com"
 },
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*",
 "kms:DescribeKey"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Important

When you add the new sections to your KMS key policy, don't change any existing
sections in the policy. AWS IoT FleetWise can’t perform operations to your data if encryption is enabled for AWS IoT FleetWise and any of the following is true:

- The KMS key is disabled or deleted.
- The KMS key policy isn't correctly configured for the service.

### Using vision system data with encryption at rest

###### Note

Vision system data is in preview release and is subject to change.

If you have customer managed encryption with AWS KMS keys enabled on your AWS IoT FleetWise account,
and you want to use vision system data, reset your encryption settings to be compatible with complex data
types. This enables AWS IoT FleetWise to establish additional permissions needed for vision system data.

###### Note

Your decoder manifest could be stuck in a validating status if you haven't reset your encryption settings for vision system data.

1. Use the [GetEncryptionConfiguration](../APIReference/API_GetEncryptionConfiguration.md "../APIReference/API_GetEncryptionConfiguration.md") API operation to check if AWS KMS encryption is enabled. No further action is needed if the encryption type is `FLEETWISE_DEFAULT_ENCRYPTION`.
2. If the encryption type is `KMS_BASED_ENCRYPTION`, use the [PutEncryptionConfiguration](../APIReference/API_PutEncryptionConfiguration.md "../APIReference/API_PutEncryptionConfiguration.md") API operation to reset the encryption type to `FLEETWISE_DEFAULT_ENCRYPTION`.

```
aws iotfleetwise put-encryption-configuration \
      --encryption-type FLEETWISE_DEFAULT_ENCRYPTION
```

3. Use the [PutEncryptionConfiguration](../APIReference/API_PutEncryptionConfiguration.md "../APIReference/API_PutEncryptionConfiguration.md") API operation to re-enable the encryption type to `KMS_BASED_ENCRYPTION`.

```
aws iotfleetwise put-encryption-configuration \
        --encryption-type KMS_BASED_ENCRYPTION \
        --kms-key-id `kms_key_id`
```

For more information about enabling encryption, see [Key management in AWS IoT FleetWise](key-management.md "key-management.md").
