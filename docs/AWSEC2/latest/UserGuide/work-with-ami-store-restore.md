# Create a store image task

When you store an AMI in an S3 bucket, a store image task is created. You can use the
store image task to monitor the progress and outcome of the process.

###### Contents

- [Securing your AMIs](#securing-amis "#securing-amis")
- [Permissions for storing and restoring AMIs using S3](#ami-s3-permissions "#ami-s3-permissions")
- [Create a store image task](#create-store-image-task "#create-store-image-task")
- [Create a restore image task](#create-restore-image-task "#create-restore-image-task")

## Securing your AMIs

It is important to ensure that the S3 bucket is configured with sufficient security to
secure the content of the AMI and that the security is maintained for as long as the AMI
objects remain in the bucket. If this can't be done, use of these APIs is not
recommended. Ensure that public access to the S3 bucket is not allowed. We recommend
enabling [Server-side encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md")
for the S3 buckets in which you store the AMIs, although it’s not required.

For information about how to set the appropriate security settings for your S3
buckets, review the following security topics:

- [Blocking public access to your Amazon S3 storage](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md")
- [Setting default server-side encryption behavior for Amazon S3 buckets](../../../AmazonS3/latest/userguide/bucket-encryption.md "../../../AmazonS3/latest/userguide/bucket-encryption.md")
- [What S3 bucket policy can I use to comply with the AWS Config rule s3-bucket-ssl-requests-only?](https://repost.aws/knowledge-center/s3-bucket-policy-for-config-rule "https://repost.aws/knowledge-center/s3-bucket-policy-for-config-rule")
- [Enabling Amazon S3 server access logging](../../../AmazonS3/latest/userguide/enable-server-access-logging.md "../../../AmazonS3/latest/userguide/enable-server-access-logging.md")

When the AMI snapshots are copied to the S3 object, the data is then copied over TLS
connections. You can store AMIs with encrypted snapshots, but the snapshots are
decrypted as part of the store process.

## Permissions for storing and restoring AMIs using S3

If your IAM principals will store or restore AMIs using Amazon S3, you need to grant them the
required permissions.

The following example policy includes all of the actions that are required to allow an IAM
principal to carry out the store and restore tasks.

You can also create IAM policies that grant principals access to specific resources only.
For more example policies, see [Access management for AWS resources](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in the _IAM User Guide_.

###### Note

If the snapshots that make up the AMI are encrypted, or if your account is enabled for
encryption by default, your IAM principal must have permission to use the KMS key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:DeleteObject",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:PutObject",
 "s3:PutObjectTagging",
 "s3:AbortMultipartUpload",
 "ebs:CompleteSnapshot",
 "ebs:GetSnapshotBlock",
 "ebs:ListChangedBlocks",
 "ebs:ListSnapshotBlocks",
 "ebs:PutSnapshotBlock",
 "ebs:StartSnapshot",
 "ec2:CreateStoreImageTask",
 "ec2:DescribeStoreImageTasks",
 "ec2:CreateRestoreImageTask",
 "ec2:GetEbsEncryptionByDefault",
 "ec2:DescribeTags",
 "ec2:CreateTags"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Create a store image task

To store an AMI in an S3 bucket, start by creating a store image task. The time it takes
to complete the task depends on the size of the AMI. You can track the progress of the task
until it either succeeds or fails.

AWS CLI

###### To create the store image task

Use the [create-store-image-task](../../../cli/latest/reference/ec2/create-store-image-task.md "../../../cli/latest/reference/ec2/create-store-image-task.md") command.

```
aws ec2 create-store-image-task \
    --image-id `ami-0abcdef1234567890` \
    --bucket `amzn-s3-demo-bucket`
```

The following is example output.

```
{
  "ObjectKey": "ami-0abcdef1234567890.bin"
}
```

###### To describe the progress of the store image task

Use the [describe-store-image-tasks](../../../cli/latest/reference/ec2/describe-store-image-tasks.md "../../../cli/latest/reference/ec2/describe-store-image-tasks.md") command.

```
aws ec2 describe-store-image-tasks \
    --image-ids `ami-0abcdef1234567890` \
    --query StoreImageTaskResults[].StoreTaskState \
    --output text
```

The following is example output.

```
InProgress
```

PowerShell

###### To create the store image task

Use the [New-EC2StoreImageTask](../../../powershell/latest/reference/items/New-EC2StoreImageTask.md "../../../powershell/latest/reference/items/New-EC2StoreImageTask.md")
cmdlet.

```
New-EC2StoreImageTask `
    -ImageId `ami-0abcdef1234567890` `
    -Bucket `amzn-s3-demo-bucket`
```

The following is example output.

```
ObjectKey         : ami-0abcdef1234567890.bin
```

###### To describe the progress of the store image task

Use the [Get-EC2StoreImageTask](../../../powershell/latest/reference/items/Get-EC2StoreImageTask.md "../../../powershell/latest/reference/items/Get-EC2StoreImageTask.md")
cmdlet.

```
(Get-EC2StoreImageTask -ImageId `ami-0abcdef1234567890`).StoreTaskState
```

The following is example output.

```
InProgress
```

## Create a restore image task

You must specify a name for the restored AMI. The name must be unique for
AMIs in the Region for this account. The restored AMI gets a new AMI ID.

AWS CLI

###### To create a restore image task

Use the [create-restore-image-task](../../../cli/latest/reference/ec2/create-restore-image-task.md "../../../cli/latest/reference/ec2/create-restore-image-task.md") command.

```
aws ec2 create-restore-image-task \
    --object-key `ami-0abcdef1234567890`.bin \
    --bucket `amzn-s3-demo-bucket` \
    --name "`my-restored-ami`"
```

The following is example output.

```
{
   "ImageId": "ami-1234567890abcdef0"
}
```

PowerShell

###### To create a restore image task

Use the [New-EC2RestoreImageTask](../../../powershell/latest/reference/items/New-EC2RestoreImageTask.md "../../../powershell/latest/reference/items/New-EC2RestoreImageTask.md")
cmdlet.

```
New-EC2RestoreImageTask `
    -ObjectKey `ami-0abcdef1234567890`.bin `
    -Bucket `amzn-s3-demo-bucket` `
    -Name "`my-restored-ami`"
```

The following is example output.

```
ImageId         : ami-1234567890abcdef0
```
