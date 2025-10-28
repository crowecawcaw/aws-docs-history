# Secret encryption and decryption in AWS Secrets Manager

Secrets Manager uses envelope encryption with AWS KMS
[keys](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys") and [data keys](../../../kms/latest/developerguide/concepts.md#data-keys "../../../kms/latest/developerguide/concepts.md#data-keys") to protect each secret
value. Whenever the secret value in a secret changes, Secrets Manager requests a new data key from AWS KMS
to protect it. The data key is encrypted under a KMS key and stored in the metadata of the
secret. To decrypt the secret, Secrets Manager first decrypts the encrypted data key using the KMS key
in AWS KMS.

Secrets Manager does not use the KMS key to encrypt the secret value directly. Instead, it uses the
KMS key to generate and encrypt a 256-bit Advanced Encryption Standard (AES) symmetric [data key](../../../kms/latest/developerguide/concepts.md#data-keys "../../../kms/latest/developerguide/concepts.md#data-keys"),
and uses the data key to encrypt the secret value. Secrets Manager uses the plaintext data key to encrypt
the secret value outside of AWS KMS, and then removes it from memory. It stores the encrypted copy
of the data key in the metadata of the secret.

###### Topics

- [Choosing a AWS KMS key](#security-encryption-choose-key "#security-encryption-choose-key")
- [What is encrypted?](#secret-value-encrypted "#secret-value-encrypted")
- [Encryption and decryption processes](#security-encryption-encrypt "#security-encryption-encrypt")
- [Permissions for the KMS key](#security-encryption-authz "#security-encryption-authz")
- [How Secrets Manager uses your KMS key](#security-encryption-using-cmk "#security-encryption-using-cmk")
- [Key policy of the AWS managed key
  (aws/secretsmanager)](#security-encryption-policies "#security-encryption-policies")
- [Secrets Manager encryption context](#security-encryption-encryption-context "#security-encryption-encryption-context")
- [Monitor Secrets Manager interaction with AWS KMS](#security-encryption-logs "#security-encryption-logs")

## Choosing a AWS KMS key

When you create a secret, you can choose any symmetric encryption customer managed key in the
AWS account and Region, or you can use the AWS managed key for Secrets Manager
(`aws/secretsmanager`). If you choose the AWS managed key
`aws/secretsmanager` and it doesn't already exist yet, Secrets Manager creates it and
associates it with the secret. You can use the same KMS key or different KMS keys for each
secret in your account. You might want to use different KMS keys to set custom permissions
on the keys for a group of secrets, or if you want to audit particular operations for those
keys. Secrets Manager supports only [symmetric encryption
KMS keys](../../../kms/latest/developerguide/concepts.md#symmetric-cmks "../../../kms/latest/developerguide/concepts.md#symmetric-cmks"). If you use a KMS key in an [external key store](../../../kms/latest/developerguide/keystore-external.md "../../../kms/latest/developerguide/keystore-external.md"),
cryptographic operations on the KMS key might take longer and be less reliable and durable
because the request has to travel outside of AWS.

For information about changing the encryption key for a secret, see [Change the encryption key for an AWS Secrets Manager secret](manage_update-encryption-key.md "manage_update-encryption-key.md").

When you change the encryption key, Secrets Manager re-encrypts `AWSCURRENT`, `AWSPENDING`, and `AWSPREVIOUS` versions with the new key. To avoid locking you out of the secret, Secrets Manager keeps all existing versions encrypted with the previous key. That means you can decrypt `AWSCURRENT`, `AWSPENDING`, and `AWSPREVIOUS` versions with the previous key or the new key. If you don't have `kms:Decrypt` permission to the previous key, when you change the encryption key, Secrets Manager can't decrypt the secret versions to re-encrypt them. In this case, the existing versions are not re-encrypted.

To make it so `AWSCURRENT` can only be decrypted by the new encryption key, create a new version of the secret with the new key. Then to be able to decrypt the `AWSCURRENT` secret version, you must have permission to the new key.

You can deny permission to the AWS managed key `aws/secretsmanager` and
require secrets are encrypted with a customer managed key. For more information, see [Example: Deny a specific AWS KMS key to encrypt secrets](auth-and-access_iam-policies.md#auth-and-access_examples_kmskey "auth-and-access_iam-policies.md#auth-and-access_examples_kmskey").

To find the KMS key associated with a secret, view the secret in the console or call
[ListSecrets](../apireference/API_ListSecrets.md "../apireference/API_ListSecrets.md") or [DescribeSecret](../apireference/API_DescribeSecret.md "../apireference/API_DescribeSecret.md"). When
the secret is associated with the AWS managed key for Secrets Manager
(`aws/secretsmanager`), these operations do not return a KMS key
identifier.

## What is encrypted?

Secrets Manager encrypts the secret value, but it does not encrypt the following:

- Secret name and description
- Rotation settings
- ARN of the KMS key associated with the secret
- Any attached AWS tags

## Encryption and decryption processes

To encrypt the secret value in a secret, Secrets Manager uses the following process.

1. Secrets Manager calls the AWS KMS [GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") operation
   with the ID of the KMS key for the secret and a request for a 256-bit AES symmetric key.
   AWS KMS returns a plaintext data key and a copy of that data key encrypted under the
   KMS key.
2. Secrets Manager uses the plaintext data key and the Advanced Encryption Standard (AES) algorithm
   to encrypt the secret value outside of AWS KMS. It removes the plaintext key from memory as
   soon as possible after using it.
3. Secrets Manager stores the encrypted data key in the metadata of the secret so it is available
   to decrypt the secret value. However, none of the Secrets Manager APIs return the encrypted secret
   or the encrypted data key.

To decrypt an encrypted secret value:

1. Secrets Manager calls the AWS KMS [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") operation and passes in the
   encrypted data key.
2. AWS KMS uses the KMS key for the secret to decrypt the data key. It returns the
   plaintext data key.
3. Secrets Manager uses the plaintext data key to decrypt the secret value. Then it removes the
   data key from memory as soon as possible.

## Permissions for the KMS key

When Secrets Manager uses a KMS key in cryptographic operations, it acts on behalf of the user who
is accessing or updating the secret value. You can grant permissions in an IAM policy or a
key policy. The following Secrets Manager operations require AWS KMS permissions.

- [CreateSecret](../apireference/API_CreateSecret.md "../apireference/API_CreateSecret.md")
- [GetSecretValue](../apireference/API_GetSecretValue.md "../apireference/API_GetSecretValue.md")
- [PutSecretValue](../apireference/API_PutSecretValue.md "../apireference/API_PutSecretValue.md")
- [UpdateSecret](../apireference/API_UpdateSecret.md "../apireference/API_UpdateSecret.md")
- [ReplicateSecretToRegions](../apireference/API_ReplicateSecretToRegions.md "../apireference/API_ReplicateSecretToRegions.md")

To allow the KMS key to be used only for requests that originate in Secrets Manager, in the
permissions policy, you can use the [kms:ViaService condition key](../../../kms/latest/developerguide/policy-conditions.md#conditions-kms-via-service "../../../kms/latest/developerguide/policy-conditions.md#conditions-kms-via-service") with the
`secretsmanager.`<Region>`.amazonaws.com`
value.

You can also use the keys or values in the [encryption context](../../../kms/latest/developerguide/services-secrets-manager.md#asm-encryption-context "../../../kms/latest/developerguide/services-secrets-manager.md#asm-encryption-context") as a condition for using the KMS key for cryptographic
operations. For example, you can use a [string condition operator](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String") in an IAM or key policy document, or use a [grant
constraint](../../../kms/latest/APIReference/API_GrantConstraints.md "../../../kms/latest/APIReference/API_GrantConstraints.md") in a grant. KMS key grant propagation can take up to five minutes. For more
information, see [CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md").

## How Secrets Manager uses your KMS key

Secrets Manager calls the following AWS KMS operations with your KMS key.

**GenerateDataKey**

Secrets Manager calls the AWS KMS [GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") operation
in response to the following Secrets Manager operations.

- [CreateSecret](../apireference/API_CreateSecret.md "../apireference/API_CreateSecret.md")
  – If the new secret includes a secret value, Secrets Manager requests a new data key to
  encrypt it.
- [PutSecretValue](../apireference/API_PutSecretValue.md "../apireference/API_PutSecretValue.md") – Secrets Manager requests a new data key to encrypt the
  specified secret value.
- [ReplicateSecretToRegions](../apireference/API_ReplicateSecretToRegions.md "../apireference/API_ReplicateSecretToRegions.md") – To encrypt the replicated secret, Secrets Manager
  requests a data key for the KMS key in the replica Region.
- [UpdateSecret](../apireference/API_UpdateSecret.md "../apireference/API_UpdateSecret.md")
  – If you change the secret value or the KMS key, Secrets Manager requests a new data
  key to encrypt the new secret value.

The [RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md")
operation does not call `GenerateDataKey`, because it does not change the
secret value. However, if `RotateSecret` invokes a Lambda rotation function
that changes the secret value, its call to the `PutSecretValue` operation
triggers a `GenerateDataKey` request.

**Decrypt**

Secrets Manager calls the [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") operation in response to
the following Secrets Manager operations.

- [GetSecretValue](../apireference/API_GetSecretValue.md "../apireference/API_GetSecretValue.md") and [BatchGetSecretValue](../apireference/API_BatchGetSecretValue.md "../apireference/API_BatchGetSecretValue.md") – Secrets Manager decrypts the secret value before
  returning it to the caller. To decrypt an encrypted secret value, Secrets Manager calls the
  AWS KMS [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") operation to decrypt the encrypted data key in the secret. Then, it
  uses the plaintext data key to decrypt the encrypted secret value. For batch
  commands, Secrets Manager can reuse the decrypted key, so not all calls result in a
  `Decrypt` request.
- [PutSecretValue](../apireference/API_PutSecretValue.md "../apireference/API_PutSecretValue.md") and [UpdateSecret](../apireference/API_UpdateSecret.md "../apireference/API_UpdateSecret.md")
  – Most `PutSecretValue` and `UpdateSecret` requests do
  not trigger a `Decrypt` operation. However, when a
  `PutSecretValue` or `UpdateSecret` request attempts to change
  the secret value in an existing version of a secret, Secrets Manager decrypts the existing
  secret value and compares it to the secret value in the request to confirm that they
  are the same. This action ensures the that Secrets Manager operations are idempotent. To
  decrypt an encrypted secret value, Secrets Manager calls the AWS KMS [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") operation to decrypt
  the encrypted data key in the secret. Then, it uses the plaintext data key to
  decrypt the encrypted secret value.
- [ReplicateSecretToRegions](../apireference/API_ReplicateSecretToRegions.md "../apireference/API_ReplicateSecretToRegions.md") – Secrets Manager first decrypts the secret value in
  the primary Region before re-encrypting the secret value with the KMS key in the
  replica Region.

**Encrypt**

Secrets Manager calls the [Encrypt](../../../kms/latest/APIReference/API_Encrypt.md "../../../kms/latest/APIReference/API_Encrypt.md") operation in response to
the following Secrets Manager operations:

- [UpdateSecret](../apireference/API_UpdateSecret.md "../apireference/API_UpdateSecret.md")
  – If you change the KMS key, Secrets Manager re-encrypts the data key that protects
  the `AWSCURRENT`, `AWSPREVIOUS`, and `AWSPENDING` secret versions with the new
  key.

**DescribeKey**

Secrets Manager calls the [DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md") operation to
determine whether to list the KMS key when you create or edit a secret in the Secrets Manager
console.

**Validating access to the KMS key**

When you establish or change the KMS key that is associated with secret, Secrets Manager
calls the `GenerateDataKey` and `Decrypt` operations with the
specified KMS key. These calls confirm that the caller has permission to use the
KMS key for these operation. Secrets Manager discards the results of these operations; it does
not use them in any cryptographic operation.

You can identify these validation calls because the value of the
`SecretVersionId` key [encryption context](../../../kms/latest/developerguide/services-secrets-manager.md#asm-encryption-context "../../../kms/latest/developerguide/services-secrets-manager.md#asm-encryption-context") in these requests is
`RequestToValidateKeyAccess`.

###### Note

In the past, Secrets Manager validation calls did not include an encryption context. You
might find calls with no encryption context in older AWS CloudTrail logs.

## Key policy of the AWS managed key

(`aws/secretsmanager`)

The key policy for the AWS managed key for Secrets Manager (`aws/secretsmanager`) gives
users permission to use the KMS key for specified operations only when Secrets Manager makes the
request on the user's behalf. The key policy does not allow any user to use the KMS key
directly.

This key policy, like the policies of all [AWS managed keys](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys"), is
established by the service. You cannot change the key policy, but you can view it at any time.
For details, see [Viewing a key policy](../../../kms/latest/developerguide/key-policy-viewing.md "../../../kms/latest/developerguide/key-policy-viewing.md").

The policy statements in the key policy have the following effect:

- Allow users in the account to use the KMS key for cryptographic operations only when
  the request comes from Secrets Manager on their behalf. The `kms:ViaService` condition
  key enforces this restriction.
- Allows the AWS account to create IAM policies that allow users to view KMS key
  properties and revoke grants.
- Although Secrets Manager does not use grants to gain access to the KMS key, the policy also
  allows Secrets Manager to [create grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") for the KMS key on the user's behalf and allows the account to
  [revoke any
  grant](../../../kms/latest/APIReference/API_RevokeGrant.md "../../../kms/latest/APIReference/API_RevokeGrant.md") that allows Secrets Manager to use the KMS key. These are standard elements of
  policy document for an AWS managed key.

The following is a key policy for an example AWS managed key for Secrets Manager.

JSON

```
`{
 "Id": "auto-secretsmanager-2",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow access through AWS Secrets Manager for all principals in the account that are authorized to use AWS Secrets Manager",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "*"
 ]
 },
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:CreateGrant",
 "kms:DescribeKey"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:CallerAccount": "111122223333",
 "kms:ViaService": "secretsmanager.us-west-2.amazonaws.com"
 }
 }
 },
 {
 "Sid": "Allow access through AWS Secrets Manager for all principals in the account that are authorized to use AWS Secrets Manager",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "*"
 ]
 },
 "Action": "kms:GenerateDataKey*",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:CallerAccount": "111122223333"
 },
 "StringLike": {
 "kms:ViaService": "secretsmanager.us-west-2.amazonaws.com"
 }
 }
 },
 {
 "Sid": "Allow direct access to key metadata to the account",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:root"
 ]
 },
 "Action": [
 "kms:Describe*",
 "kms:Get*",
 "kms:List*",
 "kms:RevokeGrant"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Secrets Manager encryption context

An [encryption context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context") is a
set of key–value pairs that contain arbitrary non-secret data. When you include an encryption
context in a request to encrypt data, AWS KMS cryptographically binds the encryption context to
the encrypted data. To decrypt the data, you must pass in the same encryption context.

In its [GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") and [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") requests to AWS KMS, Secrets Manager uses
an encryption context with two name–value pairs that identify the secret and its
version, as shown in the following example. The names do not vary, but combined encryption
context values will be different for each secret value.

```
"encryptionContext": {
    "SecretARN": "arn:aws:secretsmanager:us-east-2:111122223333:secret:test-secret-a1b2c3",
    "SecretVersionId": "EXAMPLE1-90ab-cdef-fedc-ba987SECRET1"
}
```

You can use the encryption context to identify these cryptographic operation in audit
records and logs, such as [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") and Amazon CloudWatch Logs, and as a condition for authorization in policies and
grants.

The Secrets Manager encryption context consists of two name-value pairs.

- **SecretARN** – The first name–value pair
  identifies the secret. The key is `SecretARN`. The value is the Amazon Resource
  Name (ARN) of the secret.

```
"SecretARN": "`ARN of an Secrets Manager secret`"
```

For example, if the ARN of the secret is
`arn:aws:secretsmanager:us-east-2:111122223333:secret:test-secret-a1b2c3`,
the encryption context would include the following pair.

```
"SecretARN": "arn:aws:secretsmanager:us-east-2:111122223333:secret:test-secret-a1b2c3"
```

- **SecretVersionId** – The second name–value
  pair identifies the version of the secret. The key is `SecretVersionId`. The
  value is the version ID.

```
"SecretVersionId": "`<version-id>`"
```

For example, if the version ID of the secret is
`EXAMPLE1-90ab-cdef-fedc-ba987SECRET1`, the encryption context would include
the following pair.

```
"SecretVersionId": "EXAMPLE1-90ab-cdef-fedc-ba987SECRET1"
```

When you establish or change the KMS key for a secret, Secrets Manager sends [GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") and [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") requests to AWS KMS to validate
that the caller has permission to use the KMS key for these operations. It discards the
responses; it does not use them on the secret value.

In these validation requests, the value of the `SecretARN` is the actual ARN of
the secret, but the `SecretVersionId` value is
`RequestToValidateKeyAccess`, as shown in the following example encryption context.
This special value helps you to identify validation requests in logs and audit trails.

```
"encryptionContext": {
    "SecretARN": "arn:aws:secretsmanager:us-east-2:111122223333:secret:test-secret-a1b2c3",
    "SecretVersionId": "RequestToValidateKeyAccess"
}
```

###### Note

In the past, Secrets Manager validation requests did not include an encryption context. You might
find calls with no encryption context in older AWS CloudTrail logs.

## Monitor Secrets Manager interaction with AWS KMS

You can use AWS CloudTrail and Amazon CloudWatch Logs to track the requests that Secrets Manager sends to AWS KMS on your
behalf. For information about monitoring the use of secrets, see [Monitor AWS Secrets Manager secrets](monitoring.md "monitoring.md").

**GenerateDataKey**

When you create or change the secret value in a secret, Secrets Manager sends a [GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") request to AWS KMS that specifies the KMS key for
the secret.

The event that records the `GenerateDataKey` operation is similar to the
following example event. The request is invoked by
`secretsmanager.amazonaws.com`. The parameters include the Amazon Resource
Name (ARN) of the KMS key for the secret, a key specifier that requires a 256-bit key,
and the [encryption context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context")
that identifies the secret and version.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AROAIGDTESTANDEXAMPLE:user01",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/user01",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2018-05-31T23:23:41Z"
            }
        },
        "invokedBy": "secretsmanager.amazonaws.com"
    },
    "eventTime": "2018-05-31T23:23:41Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "secretsmanager.amazonaws.com",
    "userAgent": "secretsmanager.amazonaws.com",
    "requestParameters": {
        "keyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
        "keySpec": "AES_256",
        "encryptionContext": {
            "SecretARN": "arn:aws:secretsmanager:us-east-2:111122223333:secret:test-secret-a1b2c3",
            "SecretVersionId": "EXAMPLE1-90ab-cdef-fedc-ba987SECRET1"
        }
    },
    "responseElements": null,
    "requestID": "a7d4dd6f-6529-11e8-9881-67744a270888",
    "eventID": "af7476b6-62d7-42c2-bc02-5ce86c21ed36",
    "readOnly": true,
    "resources": [
        {
            "ARN": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
            "accountId": "111122223333",
            "type": "AWS::KMS::Key"
        }
    ],
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}
```

**Decrypt**

When you get or change the secret value of a secret, Secrets Manager sends a [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md")
request to AWS KMS to decrypt the encrypted data key. For batch commands, Secrets Manager can reuse
the decrypted key, so not all calls result in a `Decrypt` request.

The event that records the `Decrypt` operation is similar to the
following example event. The user is the principal in your AWS account who is
accessing the table. The parameters include the encrypted table key (as a ciphertext
blob) and the [encryption context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context")
that identifies the table and the AWS account. AWS KMS derives the ID of the KMS key
from the ciphertext.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AROAIGDTESTANDEXAMPLE:user01",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/user01",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2018-05-31T23:36:09Z"
            }
        },
        "invokedBy": "secretsmanager.amazonaws.com"
    },
    "eventTime": "2018-05-31T23:36:09Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "secretsmanager.amazonaws.com",
    "userAgent": "secretsmanager.amazonaws.com",
    "requestParameters": {
        "encryptionContext": {
            "SecretARN": "arn:aws:secretsmanager:us-east-2:111122223333:secret:test-secret-a1b2c3",
            "SecretVersionId": "EXAMPLE1-90ab-cdef-fedc-ba987SECRET1"
        }
    },
    "responseElements": null,
    "requestID": "658c6a08-652b-11e8-a6d4-ffee2046048a",
    "eventID": "f333ec5c-7fc1-46b1-b985-cbda13719611",
    "readOnly": true,
    "resources": [
        {
            "ARN": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
            "accountId": "111122223333",
            "type": "AWS::KMS::Key"
        }
    ],
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}
```

**Encrypt**

When you change the KMS key associated with a secret, Secrets Manager sends an [Encrypt](../../../kms/latest/APIReference/API_Encrypt.md "../../../kms/latest/APIReference/API_Encrypt.md")
request to AWS KMS to re-encrypt the `AWSCURRENT`, `AWSPREVIOUS`, and `AWSPENDING` secret
versions with the new key. When you replicate a secret to another Region, Secrets Manager also
sends an [Encrypt](../../../kms/latest/APIReference/API_Encrypt.md "../../../kms/latest/APIReference/API_Encrypt.md") request to AWS KMS.

The event that records the `Encrypt` operation is similar to the
following example event. The user is the principal in your AWS account who is
accessing the table.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AROAIGDTESTANDEXAMPLE:user01",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/user01",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "attributes": {
                "creationDate": "2023-06-09T18:11:34Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "secretsmanager.amazonaws.com"
    },
    "eventTime": "2023-06-09T18:11:34Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Encrypt",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "secretsmanager.amazonaws.com",
    "userAgent": "secretsmanager.amazonaws.com",
    "requestParameters": {
        "keyId": "arn:aws:kms:us-east-2:111122223333:key/EXAMPLE1-f1c8-4dce-8777-aa071ddefdcc",
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT",
        "encryptionContext": {
            "SecretARN": "arn:aws:secretsmanager:us-east-2:111122223333:secret:ChangeKeyTest-5yKnKS",
            "SecretVersionId": "EXAMPLE1-5c55-4d7c-9277-1b79a5e8bc50"
        }
    },
    "responseElements": null,
    "requestID": "129bd54c-1975-4c00-9b03-f79f90e61d60",
    "eventID": "f7d9ff39-15ab-47d8-b94c-56586de4ab68",
    "readOnly": true,
    "resources": [
        {
            "accountId": "AWS Internal",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:111122223333:key/EXAMPLE1-f1c8-4dce-8777-aa071ddefdcc"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```
