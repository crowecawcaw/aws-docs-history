# Encrypting EventBridge Pipes data with

AWS KMS keys

You can specify that EventBridge use a customer managed key to encrypt
pipe data stored at rest, rather than use an
AWS owned key as is the default. You can specify a customer managed key when you create or update a pipe. For more information about key types, see [KMS key options](eb-encryption-at-rest-key-options.md "eb-encryption-at-rest-key-options.md").

The pipe data EventBridge encrypts at rest includes:

- [Event patterns](eb-event-patterns.md "eb-event-patterns.md")
- [Input transformers](eb-pipes-input-transformation.md "eb-pipes-input-transformation.md")
  Events flowing through a pipe are never stored at rest.

## EventBridge Pipes encryption

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

For EventBridge Pipes, EventBridge uses the same encryption context in all
AWS KMS cryptographic operations. The context includes a single
key–value pair, which contains the pipe ARN.

```
"encryptionContext": {
    "kms:EncryptionContext:aws:pipes:arn": "`pipe-arn`"
}
```

For vended logs, EventBridge uses the following encryption context.

```
"encryptionContext": {
    "kms:EncryptionContext:SourceArn": "arn:`partition`:logs:`region`:`account`:*"
}
```

## AWS KMS key policy for EventBridge

Pipes

The following example key policy provides the required permissions for a
pipe:

- `kms:DescribeKey`
- `kms:GenerateDataKey`
- `kms:Decrypt`

As a security best practice, we recommend you include condition
keys in the key policy to helps ensure that EventBridge uses the AWS KMS key only for the
specified resource or account. For more information, see
[Security considerations](eb-encryption-key-policy.md#eb-encryption-event-bus-confused-deputy "eb-encryption-key-policy.md#eb-encryption-event-bus-confused-deputy").

JSON

```
`{
 "Id": "CMKKeyPolicy",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:role/`pipe-execution-role`"
 },
 "Action": [
 "kms:DescribeKey"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:role/`pipe-execution-role`e"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*",
 "Condition": {
 "ArnLike": {
 "kms:EncryptionContext:aws:pipe:arn": "arn:aws:pipes:`us-east-1`:`123456789012`:pipe/`pipe-name`"
 },
 "ForAnyValue:StringEquals": {
 "kms:EncryptionContextKeys": [
 "aws:pipe:arn"
 ]
 }
 }
 }
 ]
}`

```

### Permissions for

pipe logs that include execution data

If you have configured pipes logging to include execution data, the
key policy must include the following permissions for the logging
service:

- `kms:Decrypt`
- `kms:GenerateDataKey`

For more information, see [Including execution data in EventBridge Pipes logs](eb-pipes-logs.md#eb-pipes-logs-execution-data "eb-pipes-logs.md#eb-pipes-logs-execution-data").

The following example key policy provides the required permissions for pipes logging:

```
{
  "Sid": "Enable log service encryption",
  "Effect": "Allow",
  "Principal": {
    "Service": "delivery.logs.amazonaws.com"
  },
  "Action": [
    "kms:Decrypt",
    "kms:GenerateDataKey"
  ],
  "Resource": "*",
  "Condition": {
    "StringLike": {
      "kms:EncryptionContext:SourceArn": "arn:`partition`:logs:`region`:`account`:*"
    }
  }
}
```

In addition, the pipe execution role requires the `kms:GenerateDataKey` permisson.

```
{
  "Sid": "Enable log service encryption",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::`account`:role/pipe-execution-role"
  },
  "Action": [
    "kms:GenerateDataKey"
  ],
  "Resource": "*",
  "Condition": {
    "StringLike": {
      "kms:EncryptionContext:SourceArn": "arn:`partition`:logs:`region`:`account`:*"
    }
  }
}
```

The pipe execution role should also include:

```
"Action": [
    "kms:GenerateDataKey"
  ],
  "Resource": "`key-arn`",
  "Condition": {
    "StringLike": {
      "kms:EncryptionContext:SourceArn": "arn:`partition`:logs:`region`:`account`:*"
    }
  }
```
