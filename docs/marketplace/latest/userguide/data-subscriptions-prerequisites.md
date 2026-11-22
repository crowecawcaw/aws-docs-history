

# Prerequisites

Before you create a data subscription, you need the following resources in the AWS account that holds your seller registration:
+ An Amazon S3 bucket in the same AWS Region as your AWS KMS key. Opt-in AWS Regions aren't supported. For more information, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the *Amazon Simple Storage Service User Guide*.
+ A customer managed AWS KMS key in the same account. AWS Marketplace encrypts every file with this key. You can't use an AWS owned key or a key from another account. Use the Amazon Resource Name (ARN) of the key, not an alias ARN. The ARN has the following form:

  `arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}`

  For more information about creating a key, see [Create a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide*.
+ Permission to edit the bucket policy and the key policy, or an administrator who can apply the policies in [Bucket policy](#data-subscriptions-bucket-policy) and [Key policy](#data-subscriptions-key-policy) for you.
+ IAM permissions for the data subscription actions. For more information, see [Controlling access to data subscriptions](data-subscriptions-iam.md).

## Bucket policy
<a name="data-subscriptions-bucket-policy"></a>

Add the following statement to your bucket policy. The following policy allows AWS Marketplace to write files to the bucket on behalf of your account. If your bucket already has a policy, add the statement to that policy instead of replacing it.

Replace {{amzn-s3-demo-bucket}} with your bucket name and {{account-id}} with your AWS account ID.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowAWSDataSubscriptionsPutObject",
            "Effect": "Allow",
            "Principal": {
                "Service": "datasubscriptions.aws-marketplace.amazonaws.com"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "account-id"
                }
            }
        }
    ]
}
```
+ {{amzn-s3-demo-bucket}} – Replace with your bucket name.
+ {{account-id}} – Replace with your AWS account ID.

Keep the `Resource` element as shown. A policy that names only a prefix can block deliveries. The statement doesn't allow AWS Marketplace to read, list, or delete objects. For more information, see [Adding a bucket policy by using the Amazon S3 console](https://docs.aws.amazon.com/AmazonS3/latest/userguide/add-bucket-policy.html) in the *Amazon Simple Storage Service User Guide*.

## Key policy
<a name="data-subscriptions-key-policy"></a>

Add the following statement to your key policy. The following statement allows Amazon S3 to encrypt the delivered files with your key on behalf of AWS Marketplace.

Replace {{region}} with the code of the Region that holds your key.

```json
{
    "Sid": "AllowAWSDataSubscriptionsGenerateDataKey",
    "Effect": "Allow",
    "Principal": {
        "Service": "datasubscriptions.aws-marketplace.amazonaws.com"
    },
    "Action": "kms:GenerateDataKey",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": "s3.region.amazonaws.com"
        }
    }
}
```
+ {{region}} – Replace with the code of the Region that holds your key (for example, `us-east-1`).

The statement doesn't allow AWS Marketplace to decrypt your data. For more information, see [Changing a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html) in the *AWS Key Management Service Developer Guide*.

**Note**  
Your bucket policy, your IAM policies, and your AWS KMS key policy determine who can access the delivered data. You are responsible for reviewing and limiting that access, both before you subscribe and on an ongoing basis afterward.