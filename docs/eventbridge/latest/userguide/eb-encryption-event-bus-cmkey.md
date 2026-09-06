

# Encrypting EventBridge event buses with AWS KMS keys
<a name="eb-encryption-event-bus-cmkey"></a>

You can specify that EventBridge use an AWS KMS to encrypt your data stored on an event bus, rather than use an AWS owned key as is the default. You can specify a customer managed key when you create or update an event bus. You can also update the default event bus to use a customer managed key for encryption as well. For more information, see [KMS key options](eb-encryption-at-rest-key-options.md).

 When you specify a customer managed key for an event bus, EventBridge uses that key to encrypt the following: 
+ [Custom](eb-putevents.md) and [partner](eb-saas.md) events stored on the event bus.

  Events from AWS service are encrypted using an AWS owned key.

  EventBridge does not encrypt event metadata. For more information on event metadata, see [AWS service event metadata](https://docs.aws.amazon.com/eventbridge/latest/ref/events-structure.html) in the *Events Reference*.
+ For each [rule](eb-rules.md) on the bus:
  + The rule [event pattern](eb-event-patterns.md).
  + [Target](eb-targets.md) information, including target input, [input transformers](eb-transform-target-input.md), and [configuration parameters](eb-create-rule-wizard.md#eb-create-rule-target).
+ If [event bus logging](eb-event-bus-logs.md) is enabled, the `detail` and `error` sections of log records.

If you specify a customer managed key for an event bus, you have the option of specifying a dead-letter queue (DLQ) for the event bus. EventBridge then delivers any custom or partner events that generate encryption or decryption errors to that DLQ. For more information, see [DLQs for encrypted events](eb-encryption-event-bus-dlq.md).

**Note**  
We strongly recommend specifying a DLQ for event buses, to ensure events are preserved if encryption or decryption errors occur.

You can also specify using customer managed keys for encrypting event bus archives. For more information, see [Encrypting archives](encryption-archives.md).

**Note**  
Schema discovery is not supported for event buses encrypted using a customer managed key. To enable schema discovery on an event bus, choose to use an AWS owned key. For more information, see [KMS key options](eb-encryption-at-rest-key-options.md).

## Event bus encryption context
<a name="eb-encryption-at-rest-context-bus"></a>

An [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) is a set of key–value pairs that contain arbitrary nonsecret data. When you include an encryption context in a request to encrypt data, AWS KMS cryptographically binds the encryption context to the encrypted data. To decrypt the data, you must pass in the same encryption context.

You can also use the encryption context as a condition for authorization in policies and grants.

If you use a customer managed key to protect your EventBridge resources, you can use the encryption context to identify use of the KMS key in audit records and logs. It also appears in plaintext in logs, such as [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) and [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html).

For event buses, EventBridge uses the same encryption context in all AWS KMS cryptographic operations. The context includes a single key–value pair, which contains the event bus ARN. 

```
"encryptionContext": {
    "kms:EncryptionContext:aws:events:event-bus:arn": "{{event-bus-arn}}"
}
```

## AWS KMS key policy for event bus
<a name="eb-encryption-key-policy-bus"></a>

The following example key policy provides the required permissions for an event bus:
+ `kms:DescribeKey`
+ `kms:GenerateDataKey`
+ `kms:Decrypt`

As a security best practice, we recommend you include condition keys in the key policy to helps ensure that EventBridge uses the KMS key only for the specified resource or account. For more information, see [Security considerations](eb-encryption-key-policy.md#eb-encryption-event-bus-confused-deputy).

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowEventBridgeToValidateKeyPermission",
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
    "Sid": "AllowEventBridgeToEncryptEvents",
    "Effect": "Allow",
    "Principal": {
      "Service": "events.amazonaws.com"
    },
    "Action": [
      "kms:GenerateDataKey",
      "kms:Decrypt"
    ],
    "Resource": "*",
    "Condition": {
      "StringEquals": {
          "kms:EncryptionContext:aws:events:event-bus:arn": "arn:aws:events:us-east-1:123456789012:event-bus/event-bus-arn",
          "aws:SourceArn": "arn:aws:events:us-east-1:123456789012:event-bus/event-bus-name"
        }
      } 
    }
  ] }
```

------

## AWS KMS key permissions for event bus actions
<a name="eb-encryption-key-permissions-bus"></a>

To create or update an event bus encrypted using a customer managed key, you must have the following permissions to the specified customer managed key:
+ `kms:GenerateDataKeyWithoutPlaintext`
+ `kms:Decrypt`
+ `kms:Encrypt`
+ `kms:ReEncryptFrom`
+ `kms:ReEncryptTo`
+ `kms:DescribeKey`

In addition, to perform certain event bus actions on an event bus encrypted using a customer managed key, you must have `kms:Decrypt` permission for the specified customer managed key. These actions include:
+ `[DescribeRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeRule.html)`
+ `[DisableRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DisableRule.html)`
+ `[EnableRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_EnableRule.html)`
+ `[ListRules](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListRules.html)`
+ `[ListTargetsByRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListTargetsByRule.html)`
+ `[PutRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutRule.html)`
+ `[ListRuleNamesByTarget](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListRuleNamesByTarget.html)`
+ `[PutTargets](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutTargets.html)`