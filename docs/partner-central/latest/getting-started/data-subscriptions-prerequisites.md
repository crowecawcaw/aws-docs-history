

# Prerequisites

Before you create a data subscription, you need the following in the AWS account that is linked to your AWS Partner Central account:
+ An Amazon S3 bucket in the same AWS Region as your AWS KMS key. Opt-in AWS Regions aren't supported. For more information, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the *Amazon S3 User Guide*.
+ A customer managed AWS KMS key in the same account. AWS Partner Central encrypts every file with this key. You can't use an AWS owned key or a key from another account. Use the Amazon Resource Name (ARN) of the key, `arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}`, not an alias ARN. For more information, see [Create a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide*.
+ You can edit the bucket policy and the key policy, or an administrator can apply the policies in [Bucket policy](#data-subscriptions-bucket-policy) and [Key policy](#data-subscriptions-key-policy) for you.
+ IAM permissions for the data subscription actions. For more information, see [Controlling access to data subscriptions](data-subscriptions-iam.md).

## Bucket policy
<a name="data-subscriptions-bucket-policy"></a>

Add the following JSON policy to your bucket to let AWS Partner Central write files to the bucket on behalf of your account. If your bucket already has a policy, add the statement to that policy instead of replacing it. Replace `{{amzn-s3-demo-bucket}}` with your bucket name and `{{111122223333}}` with your AWS account ID.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowAWSDataSubscriptionsPutObject",
            "Effect": "Allow",
            "Principal": {
                "Service": "datasubscriptions.partnercentral.amazonaws.com"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{111122223333}}"
                }
            }
        }
    ]
}
```

Keep the `Resource` element as shown. If you name only a prefix in the policy, it can block deliveries. You don't give AWS Partner Central permission to read, list, or delete objects.

For more information, see [Adding a bucket policy by using the Amazon S3 console](https://docs.aws.amazon.com/AmazonS3/latest/userguide/add-bucket-policy.html) in the *Amazon S3 User Guide*.

## Key policy
<a name="data-subscriptions-key-policy"></a>

Add the following JSON statement to your key policy. With this statement, you let Amazon S3 encrypt the delivered files with your key on behalf of AWS Partner Central. Replace `{{region}}` with the Region code, `{{account-id}}` with your AWS account ID, and `{{key-id}}` with your key ID.

```json
{
    "Sid": "AllowAWSDataSubscriptionsGenerateDataKey",
    "Effect": "Allow",
    "Principal": {
        "Service": "datasubscriptions.partnercentral.amazonaws.com"
    },
    "Action": "kms:GenerateDataKey",
    "Resource": "arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": "s3.{{region}}.amazonaws.com"
        }
    }
}
```

You don't give AWS Partner Central permission to decrypt your data. For more information, see [Changing a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html) in the *AWS Key Management Service Developer Guide*.

**Note**  
Your bucket policy, your IAM policies, and your AWS KMS key policy determine who can access the delivered data. You are responsible for reviewing and limiting that access, both before you subscribe and on an ongoing basis afterward.