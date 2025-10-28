# Using encrypted S3 buckets for your

recommendations export

For the destination of your Compute Optimizer recommendations exports, you can specify S3 buckets
that are encrypted with either Amazon S3 customer managed keys or AWS Key Management Service (KMS)
keys.

## Prerequisites

To use an S3 bucket with AWS KMS encryption enabled, you must create a symmetric
KMS key. Symmetric KMS keys are the only KMS keys that Amazon S3 supports. For
instructions, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in
the _AWS KMS Developer Guide_.

After you create the KMS key, apply it
to the S3 bucket that you plan to use for your recommendations export. For more
information, see [Enabling Amazon S3
default bucket encryption](../../../AmazonS3/latest/userguide/default-bucket-encryption.md "../../../AmazonS3/latest/userguide/default-bucket-encryption.md") in the _Amazon Simple Storage Service User
Guide_.

## Procedure

Use the following procedure to grant Compute Optimizer the required permission to use your
KMS key. This permission is specific for encrypting your recommendations export file
when saving it to your encrypted S3 bucket.

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the left navigation menu, choose **Customer-managed
   keys**.

###### Note

Compute Optimizer recommendation exports aren't permitted for S3 buckets encrypted with
**AWS managed keys**. 4. Choose the name of the KMS key that you used to encrypt the export S3
bucket. 5. Choose the **Key policy** tab, then choose **Switch
to policy view**. 6. Choose **Edit** to edit the key policy. 7. Copy one of the following policies, and paste it into the statements section of
the key policy. 8. Replace the following placeholder text in the policy:

    * Replace `myRegion` with the source
     AWS Region.
    * Replace `myAccountID` with the account number
     of the export requester.

The `GenerateDataKey` statement allows Compute Optimizer to
call the AWS KMS API to obtain the data key for encrypting the recommendation
files. This way, the uploaded data format can accommodate the bucket encryption
setting. Otherwise, Amazon S3 rejects the export request.

###### Note

If the existing KMS key already has one or more policies attached, add
the statements for Compute Optimizer access to those policies. Evaluate the resulting set
of permissions to ensure that they're appropriate for the users who access the KMS key.

Use the following policy to allow Amazon S3 bucket keys. This policy must be used
regardless of whether S3 bucket keys are enabled or disabled. For more information, see
[Reducing the cost of SSE-KMS with Amazon S3
Bucket Keys](../../../AmazonS3/latest/userguide/bucket-key.md "../../../AmazonS3/latest/userguide/bucket-key.md") in the _Amazon Simple Storage Service User Guide_.

```
{
                "Sid": "Allow use of the key to Compute Optimizer",
                "Effect": "Allow",
                "Principal": {
                    "Service": "compute-optimizer.amazonaws.com"
                },
                "Action": [
                    "kms:GenerateDataKey",
                    "kms:Decrypt"
                ],
                "Resource": "*",
                "Condition": {"StringEquals": {
                        "aws:SourceAccount": "`myAccountID`"
                    },
                    "StringLike": {
                         "aws:SourceArn": "arn:aws:compute-optimizer:`myRegion`:`myAccountID`:*"
                     }
                }
            }
```

## Next steps

For instructions on how to export your AWS Compute Optimizer recommendations, see [Exporting your recommendations](exporting-your-recommendations.md "exporting-your-recommendations.md").

## Additional resources

- Troubleshooting — [Troubleshooting failed export jobs](troubleshooting-account-opt-in.md#troubleshooting-exports "troubleshooting-account-opt-in.md#troubleshooting-exports")
- [Exported files](exported-files.md "exported-files.md")
- [Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md").
