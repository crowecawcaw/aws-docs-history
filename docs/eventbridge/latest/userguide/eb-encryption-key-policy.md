

# Authorizing EventBridge to use a customer managed key
<a name="eb-encryption-key-policy"></a>

If you use a customer managed key in your account to protect your EventBridge resources, the policies on that KMS key must give EventBridge permission to use it on your behalf. You provide these permissions in a [key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html). 

EventBridge does not need additional authorization to use the default AWS owned key to protect the EventBridge resources in your AWS account.

EventBridge requires the following permissions to use customer managed keys:
+ [`kms:DescribeKey`](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html)

  EventBridge requires this permission to retrieve the KMS key ARN for the Key Id provided, and to verify that the key is symmetric.
+ [`kms:GenerateDataKey`](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html)

  EventBridge requires this permission to generate a data key as the encryption key for the data.
+ [`kms:Decrypt`](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html)

  EventBridge requires this permission to decrypt the data key that is encrypted and stored with the encrypted data.

  EventBridge uses this for event pattern matching; users never have access to the data.

## Security when using customer managed keys for EventBridge encryption
<a name="eb-encryption-event-bus-confused-deputy"></a>

As a security best practice, add an `aws:SourceArn`, `aws:sourceAccount`, or `kms:EncryptionContext:aws:events:event-bus:arn` condition key to the AWS KMS key policy. The IAM global condition key helps ensure that EventBridge uses the KMS key only for the specified bus or account.

The following example demonstrates how to follow this best practice in your IAM policy for an event bus:

```
{
      "Sid": "Allow the use of key",
      "Effect": "Allow",
      "Principal": {
        "Service": "events.amazonaws.com"
      },
      "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
      ],
      "Resource": "*",
      "Condition" : {
        "StringEquals": {
          "aws:SourceAccount": "arn:aws:events:{{region}}:{{account-id}}",
          "aws:SourceArn": "arn:aws:events:{{region}}:{{account-id}}:event-bus/{{event-bus-name}}",
          "kms:EncryptionContext:aws:events:event-bus:arn": "arn:aws:events:{{region}}:{{account-id}}:event-bus/{{event-bus-arn}}"
        }
      }
```