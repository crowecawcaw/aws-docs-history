# Setting up Amazon SNS topic encryption with

server-side encryption

Amazon SNS supports server-side encryption (SSE) to protect the contents of messages using
AWS Key Management Service (AWS KMS). Follow the instructions below to enable SSE using the Amazon SNS console or
CDK.

## Option 1: Enable encryption using the

AWS Management Console

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. Navigate to the **Topics** page, select your **topic**, and choose **Edit**.
3. Expand the **Encryption** section and do the following:
   - Toggle encryption to **Enable**.
   - Select the **AWS managed SNS Key**
     (alias/aws/sns) as the encryption key. This is
     selected by default.

4. Choose **Save changes**.

###### Note

- The AWS managed key is automatically created if it doesn’t already
  exist.
- If you don’t see the key or have insufficient permissions, ask your
  administrator for `kms:ListAliases` and
  `kms:DescribeKey`.

## Option 2: Enable encryption using AWS CDK

To use the AWS managed SNS key in your CDK application, add the
following snippet:

```
import software.amazon.awscdk.services.sns.*;
import software.amazon.awscdk.services.kms.*;
import software.amazon.awscdk.core.*;

public class SnsEncryptionExample extends Stack {
    public SnsEncryptionExample(final Construct scope, final String id) {
        super(scope, id);

        // Define the managed SNS key
        IKey snsKey = Alias.fromAliasName(this, "helloKey", "alias/aws/sns");

        // Create the SNS Topic with encryption enabled
        Topic.Builder.create(this, "MyEncryptedTopic")
            .masterKey(snsKey)
            .build();
    }
}
```

## Additional information

- **Custom KMS key** – You can specify a
  custom key if required. In the Amazon SNS console, select your custom KMS key from
  the list or enter the ARN.
- **Permissions for custom KMS keys** – If
  using a custom KMS key, include the following in the key policy to allow Amazon SNS
  to encrypt and decrypt messages:

```
{
    "Effect": "Allow",
    "Principal": {
        "Service": "sns.amazonaws.com"
     },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
    ],
    "Resource": "*",
    "Condition": {
        "ArnLike": {
            "aws:SourceArn": "arn:aws:`service`:`region`:`customer-account-id`:`resource-type`/`customer-resource-id`"
        },
        "StringEquals": {
            "kms:EncryptionContext:aws:sns:topicArn": "arn:aws:sns:`your_region`:`customer-account-id`:`your_sns_topic_name`"
        }
    }
}
```

## Impact on consumers

Enabling SSE does not change how subscribers consume messages. AWS manages
encryption and decryption transparently. Messages remain encrypted at rest and are
automatically decrypted before delivery to subscribers. For optimal security, AWS
recommends enabling HTTPS for all endpoints to ensure secure transmission of
messages.
