# Encrypt managed query results

Athena offers the following options for encrypting [Managed query results](managed-results.md "managed-results.md").

## Encrypt using an AWS owned key

This is the default option when you use managed query results. This option
indicates that you want to encrypt query results using an AWS owned key.
AWS owned keys are not stored in your AWS account and are part of a collection
of KMS keys that AWS owns. You are not charged a fee when you use AWS owned
keys, and they do not count against AWS KMS quotas for your account.

## Encrypt using AWS KMS customer managed key

Customer managed keys are the KMS keys in your AWS account that you create, own,
and manage. You have full control over these KMS keys, which includes establishing
and maintaining their key policies, IAM policies and grants, enabling and disabling
them, rotating their cryptographic material, adding tags, creating aliases that
refer to them, and scheduling them for deletion. For more information, see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk").

## How Athena uses customer managed key to encrypt results

When you specify a customer managed key, Athena uses it to encrypt the query results when
stored in managed query results. The same key is used to decrypt the results when you call
`GetQueryResults`. When you set the state of the customer managed key to
disabled or schedule it for deletion, it prevents Athena and all users from
encrypting or decrypting results with that key.

Athena uses envelope encryption and key hierarchy to encrypt data. Your AWS KMS
encryption key is used to generate and decrypt the root key of this key
hierarchy.

Each result is encrypted using the customer managed key configured in the workgroup at the
time of encryption. Switching the key to a different customer managed key or to an AWS owned
key does not re-encrypt existing results with the new key. Deleting and disabling a
particular customer managed key only affects decryption of the results that the key
encrypted.

Athena needs access to your encryption key to perform `kms:Decrypt`,
`kms:GenerateDataKey`, and `kms:DescribeKey`
operations for encrypting and decrypting results. For more information, see
[Permissions to encrypted data in Amazon S3](encryption.md#permissions-for-encrypting-and-decrypting-data "encryption.md#permissions-for-encrypting-and-decrypting-data").

The principal that submits the query using the
`StartQueryExecution` API and reads results using
`GetQueryResults` must also have permission to the customer
managed key for `kms:Decrypt`, `kms:GenerateDataKey`, and
`kms:DescribeKey` operations in addition to Athena and Amazon S3
permissions. For more information, see [Key policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-users "../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-users").
