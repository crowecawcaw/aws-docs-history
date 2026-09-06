

# Configuring S3 destinations for scheduled queries
<a name="scheduled-queries-s3-destination"></a>

Configure Amazon S3 as a destination to store your scheduled query results as JSON files for long-term retention and analysis.

When using Amazon S3 as a destination, query results are stored as JSON files in the specified bucket and prefix. This option is ideal for archiving results, performing batch analysis, or integrating with other AWS services that process S3 data.

You can deliver query results to an Amazon S3 bucket in the same AWS account as the scheduled query or to a bucket in a different AWS account. You can also optionally encrypt query results using a customer managed AWS KMS key (SSE-KMS).

## Delivering results to an Amazon S3 bucket in the same account
<a name="scheduled-queries-s3-same-account"></a>

When the destination Amazon S3 bucket is in the same AWS account as the scheduled query, you can browse and select the bucket directly from the console.

**To configure a same-account Amazon S3 destination (console)**

1. In the **Post query results to S3** section, for **S3 bucket**, select **This account**.

1. For **Amazon S3 URI**, enter the Amazon S3 bucket and prefix where results will be stored (for example, `s3://my-bucket/query-results/`), or choose **Browse Amazon S3** to navigate and select an existing Amazon S3 location.

1. (Optional) To encrypt results with a customer managed AWS KMS key, enter the ARN of the AWS KMS key in the **KMS key ARN** field. The key must be in the same AWS Region as the destination Amazon S3 bucket. If you don't specify a AWS KMS key, the bucket's default encryption settings apply.

1. In the **IAM role for posting query results to Amazon S3** section, choose **Auto-create a new role with default permissions** to automatically set up the required permissions, or choose **Use an existing role** to select an existing IAM role with the required policies.

The destination delivery IAM role requires the following permissions:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::{{my-bucket}}/{{prefix}}/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "{{111122223333}}"
                }
            }
        }
    ]
}
```

## Delivering results to an Amazon S3 bucket in another account
<a name="scheduled-queries-s3-cross-account"></a>

You can deliver scheduled query results to an Amazon S3 bucket in a different AWS account. When using a cross-account bucket, you must provide the Amazon S3 URI and the account ID of the bucket-owning account.

**To configure a cross-account Amazon S3 destination (console)**

1. In the **Post query results to S3** section, for **S3 bucket**, select **Another account** and provide the account ID of the bucket-owning account as input.

1. For **Amazon S3 URI**, enter the full Amazon S3 URI of the destination bucket and prefix in the other account (for example, `s3://cross-account-bucket/query-results/`).

1. (Optional) To encrypt results with a customer managed AWS KMS key, enter the ARN of the AWS KMS key in the **KMS key ARN** field. The key must be in the same AWS Region as the destination Amazon S3 bucket.

1. In the **IAM role for posting query results to Amazon S3** section, choose **Auto-create a new role with default permissions** to automatically set up the required permissions, or choose **Use an existing role** to select an existing IAM role with the required policies.

Cross-account delivery requires permissions on both sides. The destination delivery IAM role in the source account requires the following permissions:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::{{cross-account-bucket}}/{{prefix}}/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "{{123456789012}}"
                }
            }
        }
    ]
}
```

The Amazon S3 bucket policy in the destination account must grant the source account's IAM role permission to write objects:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowScheduledQueryRolePutObject",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:role/{{my-s3-delivery-role}}"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::{{cross-account-bucket}}/{{prefix}}/*"
        }
    ]
}
```

## Encrypting results with a customer managed AWS KMS key
<a name="scheduled-queries-s3-kms-encryption"></a>

You can optionally specify a customer managed AWS KMS key to encrypt query results delivered to Amazon S3 using SSE-KMS. The AWS KMS key can be in the same account as the scheduled query or in a different account.

When you specify a AWS KMS key, the scheduled query uses that key to encrypt results via SSE-KMS. When you don't specify a AWS KMS key, the bucket's default encryption settings apply. If the bucket is configured with default SSE-KMS encryption using a customer managed key, the destination delivery IAM role must still have `kms:GenerateDataKey` permission on that key.

The destination delivery IAM role requires `kms:GenerateDataKey` permission on the AWS KMS key. The following example shows the required permissions for an Amazon S3 destination with a customer managed AWS KMS key:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::{{my-bucket}}/{{prefix}}/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "{{111122223333}}"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": "kms:GenerateDataKey",
            "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{key-id}}",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "s3.{{us-east-1}}.amazonaws.com"
                },
                "StringLike": {
                    "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::{{my-bucket}}*"
                }
            }
        }
    ]
}
```

When the AWS KMS key is in a different account than the destination delivery IAM role, the AWS KMS key policy in the key-owning account must explicitly grant the role access:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowScheduledQueryRoleToEncrypt",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:role/{{my-s3-delivery-role}}"
            },
            "Action": "kms:GenerateDataKey",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "s3.{{us-east-1}}.amazonaws.com"
                },
                "StringLike": {
                    "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::{{my-bucket}}*"
                }
            }
        }
    ]
}
```

**Note**  
When the AWS KMS key and the destination delivery IAM role are in the same account, the IAM identity policy alone is sufficient if the AWS KMS key policy includes the default "Enable IAM policies" root statement. An explicit AWS KMS key policy grant is only required if the key policy does not delegate to IAM.

The IAM role for posting query results to Amazon S3 must be configured separately from the IAM role for scheduled query execution. This separation allows for fine-grained access control, where the execution role can run queries while the Amazon S3 role specifically handles result delivery. Both roles must include a trust policy that allows the CloudWatch Logs service (`logs.amazonaws.com`) to assume the role.