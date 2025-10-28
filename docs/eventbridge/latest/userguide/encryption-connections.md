# Encrypting EventBridge connection authorization with

AWS KMS keys

When you create or update a connection, you can specify authorization parameters for that
connection. EventBridge then securely stores those parameters in a secret in
AWS Secrets Manager. By default, EventBridge uses an AWS owned key to encrypt and
decrypt this secret. You can specify that EventBridge use a customer managed key instead.

## AWS KMS key policy for connections

The AWS KMS key policy must grant EventBridge the following permissions on your behalf:

- `kms:DescribeKey`
- `kms:GenerateDataKey`
- `kms:Decrypt`

The following policy example grants all AWS KMS permissions.

JSON

```
`{
 "Id": "key-policy-example",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Enable IAM User Permissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`012345678901`:root"
 },
 "Action": "kms:*",
 "Resource": "*"
 }
 ]
}`

```

For EventBridge to use a customer managed key, you must add a resource tag to the key with a key of `EventBridgeApiDestinations` and a value of `true`.
For more information on resource tags, see [Add tags to a KMS key](../../../kms/latest/developerguide/add-tags.md "../../../kms/latest/developerguide/add-tags.md") in the
_AWS Key Management Service Developer Guide_.

As a security best practice, we recommend you include condition
keys in the key policy to helps ensure that EventBridge uses the KMS key only for the
specified resource or account. For more information, see
[Security considerations](eb-encryption-key-policy.md#eb-encryption-event-bus-confused-deputy "eb-encryption-key-policy.md#eb-encryption-event-bus-confused-deputy").

```
"Condition": {
  "StringLike": {
    "kms:ViaService": "secretsmanager.*.amazonaws.com",
    "kms:EncryptionContext:SecretARN": [
      "arn:aws:secretsmanager:*:*:secret:events!connection/*"
    ]
  },
  "StringEquals": {
    "aws:ResourceTag/EventBridgeApiDestinations": "true"
  }
}
```

## Connection encryption

context

An [encryption
context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context") is a set of key–value pairs that contain arbitrary nonsecret
data. When you include an encryption context in a request to encrypt data,
AWS KMS cryptographically binds the encryption context to the
encrypted data. To decrypt the data, you must pass in the same encryption
context.

You can also use the encryption context as a condition for authorization in
policies and grants.

If you use a customer managed key to protect your EventBridge resources,
you can use the encryption context to identify use of the KMS key in
audit records and logs. It also appears in plaintext in logs, such as [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") and [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md").

For connections, EventBridge uses the same encryption context in all AWS KMS cryptographic
operations. The context includes a single key–value pair, which contains the secret ARN.

```
"encryptionContext": {
    "kms:EncryptionContext:SecretARN": "`secret-arn`"
}
```

## Using cross-account or cross-Region

customer managed keys for connections

You can allow users or roles in a different AWS account to use a KMS key in your
account. Cross-account access requires permission in the key policy of the KMS key and
in an IAM policy in the external user's account.

To use a customer managed key from another account, the account with the customer managed key must include the
following policy:

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::`account`:role/AmazonEventBridgeApiDestinationsInternalServiceRolePolicy"
  },
  "Action": [
    "kms:Decrypt",
    "kms:DescribeKey"
  ],
  "Resource": "*"
}
```

For more information, see [Allowing users in other accounts to use a KMS key](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md") in the
_AWS Key Management Service Developer Guide_.

## Revoking customer managed key access to

connections

Be aware that when you revoke a customer managed key--through disabling, deleting, or rotating
the key, or updating the key policy--EventBridge may have cached the key value, and so that key
may still retain access to a connection's secret for a short period of time.

To immediately revoke customer managed key access to a connection's secret, de-authorize or
delete the connection. For more information, see [De-authorizing
connections](eb-target-connection-deauthorize.md "eb-target-connection-deauthorize.md") and [Deleting
connections](eb-target-connection-delete.md "eb-target-connection-delete.md").

## Connection de-authorization due to

customer managed key errors

EventBridge de-authorizes a connection if it encounters the following errors when attempting
to encrypt or decrypt the connection's secret:

- The customer managed key has been deleted.
- The customer managed key has been disabled.
- The connection does not have the necessary permissions to access the customer managed key.

For more information, see [De-authorizing
connections](eb-target-connection-deauthorize.md "eb-target-connection-deauthorize.md").
