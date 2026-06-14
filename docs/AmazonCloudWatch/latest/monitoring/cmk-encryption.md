# Encryption at rest for OpenTelemetry metrics

## What is a CloudWatch Dataset

OpenTelemetry (OTel) metrics that you send to Amazon CloudWatch are stored in a resource called
a Dataset. Every AWS account has a `default` dataset in each Region where all
OTel metrics reside. The `default` dataset is the only supported dataset — you
cannot create additional datasets.

Datasets can be encrypted and tagged like other AWS resources. The dataset ARN has
the following format:

`arn:`{partition}`:cloudwatch:`{region}`:`{account-id}`:dataset/default`

To view the current encryption configuration of your dataset, use the
`GetDataset` API:

```
aws cloudwatch get-dataset \
    --dataset-identifier default
```

If a customer managed key is associated with the dataset, the response includes the
key ARN. If no customer managed key is associated, the dataset is encrypted with an AWS
owned key.

## Options for encryption at rest

CloudWatch always encrypts Dataset data at rest. By default, CloudWatch encrypts all data at rest
using AWS owned keys. You don't need to take any action to protect your data using AWS
owned keys. For more information, see [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") in the
AWS Key Management Service Developer Guide.

If you want to manage the keys that are used to encrypt your Dataset data, you can
use a customer managed key in AWS Key Management Service (AWS KMS). For more information, see [Customer
managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the AWS Key Management Service Developer Guide.

When you use a customer managed key, AWS KMS charges apply. For more information about
pricing, see [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

## How CloudWatch uses a customer managed key for Dataset encryption

###### Important

Customer managed key encryption applies to the `default` dataset. The
`default` dataset is the only supported dataset — you cannot create
additional datasets.

When you associate a customer managed key with the `default` dataset, CloudWatch
uses the key to encrypt all OTel metric data stored in that dataset.

CloudWatch uses the service principal (`cloudwatch.amazonaws.com`) directly with
key policy permissions. CloudWatch does not use grants or IAM roles to access your AWS KMS
key.

CloudWatch does not cache data keys. However, CloudWatch caches `kms:Decrypt`
responses for up to 15 minutes. Changes to a key policy might take up to 15 minutes to
take effect.

CloudWatch uses the following encryption context for all AWS KMS cryptographic
operations:

- Key: `aws:cloudwatch:arn`
- Value:
  `arn:`{partition}`:cloudwatch:`{region}`:`{account-id}`:dataset/default`

## Configuring a customer managed key for Dataset

The AWS KMS key that you use with CloudWatch Dataset must meet the following
requirements:

- The key must be a symmetric encryption key (SYMMETRIC_DEFAULT) with key usage
  ENCRYPT_DECRYPT. Asymmetric keys are not supported.
- Multi-Region keys are not supported.
- The key must be in the same AWS Region as the Dataset.
- You must specify the key as a fully qualified key ARN. Key aliases and key IDs
  are not supported.

## Configuring key policy permissions

To use a customer managed key with CloudWatch Dataset, the key policy must grant CloudWatch
permission to use the key. The following example key policy grants CloudWatch the necessary
permissions and includes confused deputy protection.

The caller who associates or uses the Dataset must have
`kms:Decrypt` permission, scoped to the CloudWatch `ViaService`
and encryption context as shown in the `AllowCallerDecrypt` statement below.
Replace `YourApplicationRole` with the IAM role used to call
CloudWatch Dataset APIs.

###### Example Key policy for CloudWatch Dataset encryption

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowCloudWatchDatasetDescribeKey",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudwatch.amazonaws.com"
            },
            "Action": "kms:DescribeKey",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "`account-id`"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:cloudwatch:`region`:`account-id`:dataset/default"
                }
            }
        },
        {
            "Sid": "AllowCloudWatchDatasetEncryption",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudwatch.amazonaws.com"
            },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "`account-id`",
                    "kms:EncryptionContext:aws:cloudwatch:arn": "arn:aws:cloudwatch:`region`:`account-id`:dataset/default"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:cloudwatch:`region`:`account-id`:dataset/default"
                }
            }
        },
        {
            "Sid": "AllowCallerDecrypt",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`account-id`:role/`YourApplicationRole`"
            },
            "Action": "kms:Decrypt",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "cloudwatch.`region`.amazonaws.com",
                    "kms:EncryptionContext:aws:cloudwatch:arn": "arn:aws:cloudwatch:`region`:`account-id`:dataset/default"
                }
            }
        }
    ]
}
```

Replace `account-id` and `region`
with your own values.

For more information about key policies, see [Key policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the
AWS Key Management Service Developer Guide.

## To associate a customer managed key with a Dataset

Use the `AssociateDatasetKmsKey` API to associate a customer managed key
with a Dataset. You must specify `default` as the dataset identifier.

To associate a customer managed key by using the AWS CLI, run the following
command:

```
aws cloudwatch associate-dataset-kms-key \
    --dataset-name default \
    --kms-key-arn arn:aws:kms:`region`:`account-id`:key/`key-id`
```

## Changing or removing encryption configuration

You can change or remove the customer managed key that encrypts your Dataset
data.

### To change the customer managed key

To replace the customer managed key, call `AssociateDatasetKmsKey` again
with a new key ARN. The caller must have `kms:Decrypt` permission on both
the current key and the new key. CloudWatch begins using the new key for subsequent encryption
operations.

### To remove the customer managed key

To remove the customer managed key and revert to AWS owned key encryption, call
`DisassociateDatasetKmsKey`. The caller must have `kms:Decrypt`
permission on the currently associated key.

```
aws cloudwatch disassociate-dataset-kms-key \
    --dataset-name default
```

###### Important

After you disassociate a customer managed key, there is a 3-hour enforcement
window during which CloudWatch still requires `kms:Decrypt` permission on the
previously associated key. Don't disable or delete the key during this window.

If your key is in a disabled state, you must re-enable the key before you can
disassociate it from the Dataset.

## Scoping down key policy access

You can use conditions in the key policy to limit access to your AWS KMS key.

Encryption context condition

Use the `kms:EncryptionContext:aws:cloudwatch:arn` condition key to
restrict key usage to your `default` Dataset.

```
"Condition": {
    "StringEquals": {
        "kms:EncryptionContext:aws:cloudwatch:arn": "arn:aws:cloudwatch:`region`:`account-id`:dataset/default"
    }
}
```

Confused deputy protection

Use the `aws:SourceArn` and `aws:SourceAccount` conditions
to prevent cross-account confused deputy attacks.

```
"Condition": {
    "StringEquals": {
        "aws:SourceAccount": "`account-id`"
    },
    "ArnLike": {
        "aws:SourceArn": "arn:aws:cloudwatch:`region`:`account-id`:dataset/default"
    }
}
```

kms:ViaService condition

Use the `kms:ViaService` condition key to restrict key usage to
requests that come from CloudWatch.

```
"Condition": {
    "StringEquals": {
        "kms:ViaService": "cloudwatch.`region`.amazonaws.com"
    }
}
```

## Monitoring CloudWatch interaction with AWS KMS

You can use AWS CloudTrail to track the requests that CloudWatch sends to AWS KMS on your behalf. The
AWS CloudTrail log entries use the service principal `cloudwatch.amazonaws.com` and a
`ViaService` value of
`cloudwatch.`{region}`.amazonaws.com`.

The following CloudTrail event names appear in log entries for CloudWatch Dataset encryption
operations:

- `GenerateDataKey`
- `Encrypt`
- `Decrypt`
- `DescribeKey`
- `ReEncrypt`

Each log entry includes the encryption context, which you can use to identify the
specific Dataset that the operation applies to.

For more information about monitoring AWS KMS key usage, see [Monitoring AWS Key Management Service](../../../kms/latest/developerguide/monitoring-overview.md "../../../kms/latest/developerguide/monitoring-overview.md") in the
AWS Key Management Service Developer Guide.
