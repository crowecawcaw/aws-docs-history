# Encrypting event bus logs with AWS KMS in EventBridge

When sending logs, EventBridge encrypts the `detail` and `error`
sections of each log record with the KMS key specified for the event bus.
If you have specified a customer managed key for the event bus, EventBridge uses that key for encryption in transit.
Once delivered,
the record is decrypted and then re-encrypted with the KMS key specified for the log
destination.

## Event bus logs encryption

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

For event bus logs, EventBridge uses the same encryption context in all
AWS KMS cryptographic operations.

```
"encryptionContext": {
    "kms:EncryptionContext:SourceArn": "arn:`partition`:logs:`region`:`account`:*"
}
```

## AWS KMS key policy permissions for event

bus logging

For event buses using a customer managed key, you must add the following permissions to the key policy.

- Allow EventBridge to encrypt logs using the customer managed key.

```
{
  "Sid": "Enable log service encryption",
  "Effect": "Allow",
  "Principal": {
    "Service": "events.amazonaws.com"
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

- Allow the logging service to decrypt logs sent by EventBridge.

```
{
  "Sid": "Enable log delivery decryption",
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
