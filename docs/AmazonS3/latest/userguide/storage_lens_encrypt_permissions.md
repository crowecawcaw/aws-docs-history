# Using an AWS KMS key to encrypt your metrics exports

To grant Amazon S3 Storage Lens permission to encrypt your metrics exports by using a customer managed key,
you must use a key policy. To update your key policy so that you can use a KMS key to
encrypt your S3 Storage Lens metrics exports, follow these steps.

###### To grant S3 Storage Lens permissions to encrypt data by using your KMS key

1. Sign into the AWS Management Console by using the AWS account that owns the customer managed key.
2. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
3. To change the AWS Region, use the **Region selector** in the
   upper-right corner of the page.
4. In the left navigation pane, choose **Customer managed keys**.
5. Under **Customer managed keys**, choose the key that you want to use
   to encrypt the metrics exports. AWS KMS keys are Region-specific and must be in the
   same Region as the metrics export destination S3 bucket.
6. Under **Key policy**, choose **Switch to policy
   view**.
7. To update the key policy, choose **Edit**.
8. Under **Edit key policy**, add the following key policy to the
   existing key policy. To use this policy, replace the `user input
placeholders` with your information.

```
{
    "Sid": "Allow Amazon S3 Storage Lens use of the KMS key",
     "Effect": "Allow",
    "Principal": {
        "Service": "storage-lens.s3.amazonaws.com"
    },
    "Action": [
        "kms:GenerateDataKey"
    ],
    "Resource": "*",
    "Condition": {
       "StringEquals": {
           "aws:SourceArn": "arn:aws:s3:`us-east-1`:`source-account-id`:storage-lens/`your-dashboard-name`",
           "aws:SourceAccount": "`source-account-id`"
        }
     }
}
```

9. Choose **Save changes**.
   For more information about creating customer managed keys and using key policies, see the following
   topics in the _AWS Key Management Service Developer Guide_:

- [Create a
  KMS key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md")
- [Key
  policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md")
  You can also use the AWS KMS `PUT` key policy API operation ([PutKeyPolicy](../../../kms/latest/APIReference/API_PutKeyPolicy.md "../../../kms/latest/APIReference/API_PutKeyPolicy.md")) to copy the key policy to the customer managed keys that you want
  to use to encrypt the metrics exports by using the REST API, AWS CLI, and SDKs.

## Additional permissions for S3 table bucket exports

All data in S3 tables including S3 Storage Lens metrics are encrypted with SSE-S3 encryption by
default. You can choose to encrypt your Storage Lens metrics report with AWS KMS keys
(SSE-KMS). If you choose to encrypt your S3 Storage Lens metric reports with KMS keys, you must
have additional permissions.

1. The user or IAM role needs the following permissions. You can grant these
   permissions by using the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   - `kms:DescribeKey` on the AWS KMS key used

2. On the key policy for the AWS KMS key, you need the following permissions. You can
   grant these permissions by using the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms"). To use this
   policy, replace the `user input placeholders` with
   your own information.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EnableSystemTablesKeyUsage",
            "Effect": "Allow",
            "Principal": {
                "Service": "systemtables.s3.amazonaws.com"
            },
            "Action": [
                "kms:DescribeKey",
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-id`",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "`111122223333`"
                }
            }
        },
        {
            "Sid": "EnableKeyUsage",
            "Effect": "Allow",
            "Principal": {
                "Service": "maintenance.s3tables.amazonaws.com"
            },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-id`",
            "Condition": {
                "StringLike": {
                    "kms:EncryptionContext:aws:s3:arn": "`<table-bucket-arn>`/*"
                }
            }
        }
    ]
}
```
