

# Encrypting EventBridge archives with AWS KMS keys
<a name="encryption-archives"></a>

You can specify that EventBridge use a customer managed key to encrypt events stored in an archive, rather than use an AWS owned key as is the default. You can specify a customer managed key when you create or update an archive. For more information about key types, see [KMS key options](eb-encryption-at-rest-key-options.md).

This includes:
+ Events stored in the archive
+ The event pattern, if any, specified to filter the events sent to the archive

This does not include archive metadata, such as the size of the archive or number of events it contains.

If you specify a customer managed key for an archive, EventBridge encrypts events prior to sending it to the archive, ensuring encryption in transit and at rest.

## Archive encryption context
<a name="encryption-archives-context"></a>

An [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) is a set of key–value pairs that contain arbitrary nonsecret data. When you include an encryption context in a request to encrypt data, AWS KMS cryptographically binds the encryption context to the encrypted data. To decrypt the data, you must pass in the same encryption context.

You can also use the encryption context as a condition for authorization in policies and grants.

If you use a customer managed key to protect your EventBridge resources, you can use the encryption context to identify use of the KMS key in audit records and logs. It also appears in plaintext in logs, such as [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) and [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html).

For event archives, EventBridge uses the same encryption context in all AWS KMS cryptographic operations. The context includes a single key–value pair, which contains the event bus ARN. 

```
"encryptionContext": {
    "kms:EncryptionContext:aws:events:event-bus:arn": "{{event-bus-arn}}"
}
```

## AWS KMS key policy for archives
<a name="encryption-archives-key-policy"></a>

The following example key policy provides the required permissions for an event archive:
+ `kms:DescribeKey`
+ `kms:GenerateDataKey`
+ `kms:Decrypt`
+ `kms:ReEncrypt`

As a security best practice, we recommend you include condition keys in the key policy to helps ensure that EventBridge uses the KMS key only for the specified resource or account. For more information, see [Security considerations](eb-encryption-key-policy.md#eb-encryption-event-bus-confused-deputy).

------
#### [ JSON ]

****  

```
{
  "Id": "CMKKeyPolicy",
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "events.amazonaws.com"
      },
      "Action": [
        "kms:DescribeKey"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "events.amazonaws.com"
      },
      "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt",
        "kms:ReEncrypt*"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
         "kms:EncryptionContext:aws:events:event-bus:arn": "arn:aws:events:us-east-1:123456789012:event-bus/event-bus-arn"
        }
      }
    }
  ]
}
```

------