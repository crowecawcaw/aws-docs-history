# Encrypting EMR Studio workspace notebooks and files

In EMR Studio, you can create and configure different workspaces to organize and run notebooks. These
workspaces store notebooks and related files in your specified Amazon S3 bucket. By default, these files are encrypted
with Amazon S3-managed keys (SSE-S3) with server-side encryption as the base level of encryption. You can also choose
to use customer managed KMS keys (SSE-KMS) to encrypt your files. You can do so by using the Amazon EMR management console
or through the AWS CLI and AWS SDK when creating an EMR Studio.

EMR Studio workspace storage encryption is available in all the
[Regions](emr-studio-considerations.md#emr-studio-considerations-general "emr-studio-considerations.md#emr-studio-considerations-general")
where EMR Studio is available.

## Prerequisites

Before you can encrypt EMR Studio workspace notebook and files, you must use AWS Key Management Service to [create a symmetric customer manager key (CMK)](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the same AWS account and Region as your EMR Studio.

The resource policy of your AWS KMS must have the necessary access permissions for your
EMR Studio's service role. The following is a sample IAM policy granting minimum
access permissions for EMR Studio Workspace storage encryption:

```
{
    "Sid": "AllowEMRStudioServiceRoleAccess",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::<`ACCOUNT_ID`>:role/<`ROLE_NAME`>"
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey",
        "kms:ReEncryptFrom",
        "kms:ReEncryptTo",
        "kms:DescribeKey"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:CallerAccount": "<`ACCOUNT_ID`>",
            "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::<`S3_BUCKET_NAME`>",
            "kms:ViaService": "s3.<`AWS_REGION`>.amazonaws.com"
        }
    }
}
```

Your EMR Studio service role must also have the access permissions to use your AWS KMS key. The following
is a sample IAM policy granting the minimum access permissions for EMR Studio Workspace storage
encryption:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowEMRStudioWorkspaceStorageEncryptionAccess",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey",
 "kms:ReEncryptFrom",
 "kms:ReEncryptTo",
 "kms:DescribeKey"
 ],
 "Resource": [
 "arn:aws:kms:*:123456789012:key/12345678-1234-1234-1234-123456789012"
 ]
 }
 ]
}`

```

## Create a new EMR Studio

Follow these steps to create a new EMR Studio that uses workspace storage encryption.

1. Open the Amazon EMR console at
   [https://console.aws.amazon.com/elasticmapreduce/](https://console.aws.amazon.com/elasticmapreduce/ "https://console.aws.amazon.com/elasticmapreduce/").
2. Choose **Studios**, then choose **Create Studio**.
3. For **S3 location for storage**, enter or choose an Amazon S3 path. This is the Amazon S3
   location where Amazon EMR stores workspace notebooks and files.
4. For **Service role**, enter or choose an IAM role. This is the IAM role
   that Amazon EMR assumes.
5. Choose **Encrypt Workspace files with your own AWS KMS key**.
6. Enter or choose an AWS KMS key to use to encrypt workspace notebooks and files in Amazon S3.
7. Choose **Create Studio** or **Create Studio and Launch Workspaces**.
8. Choose **Encrypt Workspace files with your own AWS KMS key**.
9. Enter or choose an AWS KMS to use to encrypt workspace notebooks and files in Amazon S3.
10. Choose **Save Changes**.

The following steps demonstrate how to update an EMR Studio and set up workspace storage encryption.

1. Open the Amazon EMR console at
   [https://console.aws.amazon.com/elasticmapreduce/](https://console.aws.amazon.com/elasticmapreduce/ "https://console.aws.amazon.com/elasticmapreduce/").
2. Choose **an existing EMR Studio from the list**, then choose **Edit**.
3. Choose **Encrypt Workspace files with your own AWS KMS key**.
4. Enter or choose an AWS KMS to use to encrypt workspace notebooks and files in Amazon S3.
5. Choose **Save Changes**.
