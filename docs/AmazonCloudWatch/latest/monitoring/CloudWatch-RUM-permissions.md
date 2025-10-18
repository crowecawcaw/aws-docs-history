# IAM policies to use CloudWatch RUM

To be able to fully manage CloudWatch RUM, you must be signed in as an IAM user or role that has the 
 **AmazonCloudWatchRUMFullAccess** IAM policy. Additionally, you may
 need other policies or permissions:


* To create an app monitor that creates a new Amazon Cognito identity pool for authorization, 
 you need to have the **Admin** IAM role or the **AdministratorAccess**
 IAM policy.
* To create an app monitor that sends data to CloudWatch Logs, you must be logged on to 
 an IAM role or policy that has the following permission:



```
{
    "Effect": "Allow",
    "Action": [
        "logs:PutResourcePolicy"
    ],
    "Resource": [
        "*"
    ]
}
```
* To enable JavaScript source maps in an app monitor, you will need to upload your source map files to a Amazon S3 bucket. Your IAM role or policy needs specific Amazon S3 permissions that allow creating Amazon S3 buckets, 
 setting bucket policies, and managing files in the bucket. For security, scope these permissions to specific resources. The example policy below restricts access to buckets containing `rum` in their names and uses the `aws:ResourceAccount` condition key to limit permissions to the principal account only.



```
{
    "Sid": "AllowS3BucketCreationAndListing",
    "Effect": "Allow",
    "Action": [
        "s3:CreateBucket",
        "s3:ListAllMyBuckets"
    ],
    "Resource": "arn:aws:s3:::*",
    "Condition": {
        "StringEquals": {
            "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
    }
},
{
    "Sid": "AllowS3BucketActions",
    "Effect": "Allow",
    "Action": [
        "s3:GetBucketLocation",
        "s3:ListBucket"
    ],
    "Resource": "arn:aws:s3:::*rum*",
    "Condition": {
        "StringEquals": {
            "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
    }
},
{
    "Sid": "AllowS3BucketPolicyActions",
    "Effect": "Allow",
    "Action": [
        "s3:PutBucketPolicy",
        "s3:GetBucketPolicy"
    ],
    "Resource": "arn:aws:s3:::*rum*",
    "Condition": {
        "StringEquals": {
            "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
    }
},
{
    "Sid": "AllowS3ObjectActions",
    "Effect": "Allow",
    "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:AbortMultipartUpload"
    ],
    "Resource": "arn:aws:s3:::*rum*",
    "Condition": {
        "StringEquals": {
            "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
    }
}
```
* To use your own AWS KMS keys for server-side encryption on your source map bucket, your IAM role or policy will need specific AWS KMS permissions that allows creating a key, updating the key policy, using the AWS KMS key with Amazon S3 
 and setting the encryption configuration of your Amazon S3 bucket. For security, scope these permissions to specific purposes. The example below restricts access to keys for a specific region and accountId and has similar S3 restrictions as the above example. 



```
{
    "Sid": "AllowKMSKeyCreation",
    "Effect": "Allow",
    "Action": [
        "kms:CreateKey",
        "kms:CreateAlias"
    ],
    "Resource": "*"
},
{
    "Sid": "KMSReadPermissions",
    "Effect": "Allow",
    "Action": [
        "kms:ListAliases"
    ],
    "Resource": "*"
},
{
    "Sid": "AllowUpdatingKeyPolicy",
    "Effect": "Allow",
    "Action": [
        "kms:PutKeyPolicy",
        "kms:GetKeyPolicy",
        "kms:ListKeyPolicies"
    ],
    "Resource": "arn:aws:kms:`REGION`:`ACCOUNT_ID`:key/*"
},
{
    "Sid": "AllowUseOfKMSKeyForS3",
    "Effect": "Allow",
    "Action": [
        "kms:DescribeKey",
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:GenerateDataKey"
    ],
    "Resource": "arn:aws:kms:`REGION`:`ACCOUNT_ID`:key/*"
},
{
    "Sid": "AllowS3EncryptionConfiguration",
    "Effect": "Allow",
    "Action": [
        "s3:PutEncryptionConfiguration",
        "s3:GetEncryptionConfiguration"
    ],
    "Resource": "arn:aws:s3:::*rum*",
    "Condition": {
        "StringEquals": {
            "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
    }
}
```
Other users who need to view CloudWatch RUM data but don't need to create CloudWatch RUM resources,
 can be granted the **AmazonCloudWatchRUMReadOnlyAccess** policy.
