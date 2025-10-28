# Grant permissions for cross-account Amazon S3 storage

When setting up your SageMaker AI domain or user profile for users to access SageMaker Canvas, you
specify an Amazon S3 storage location for Canvas artifacts. These artifacts include saved
copies of your input datasets, model artifacts, predictions, and other application data. You
can either use the default SageMaker AI created Amazon S3 bucket, or you can customize the storage
location and specify your own bucket for storing Canvas application data.

You can specify an Amazon S3 bucket in another AWS account for storing your Canvas data,
but first you must grant cross-account permissions so that Canvas can access the
bucket.

The following sections describe how to grant permissions to Canvas for uploading and
downloading objects to and from an Amazon S3 bucket in another account. There are additional
permissions for when your bucket is encrypted with AWS KMS.

## Requirements

Before you begin, review the following requirements:

- Cross-account Amazon S3 buckets (and any associated AWS KMS keys) must be in the same AWS Region as
  the Canvas user domain or user profile.
- The final Amazon S3 URI for the training folder in your Canvas storage location
  must be 128 characters or less. The final S3 URI consists of your bucket path `s3://<your-bucket-name>/<folder-name>/`
  plus the path that Canvas adds to your bucket: `Canvas/<user-profile-name>/Training`. For example, an acceptable
  path that is less than 128 characters is `s3://<amzn-s3-demo-bucket>/<machine-learning>/Canvas/<user-1>/Training`.

## Permissions for cross-account Amazon S3 buckets

The following section outlines the basic steps for granting the necessary permissions
so that Canvas can access your Amazon S3 bucket in another account. For more detailed
instructions, see [Example 2: Bucket owner granting cross-account bucket permissions](../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md "../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md") in
the _Amazon S3 User Guide_.

1. Create an Amazon S3 bucket, `bucketA`, in Account A.
2. The Canvas user exists in another account called Account B. In the following steps, we refer to
   the Canvas user's IAM role as `roleB` in Account B.

Give the IAM role `roleB` in Account B permission to download
(`GetObject`) and upload (`PutObject`) objects to and from `bucketA` in
Account A by attaching an IAM policy.

To limit access to a specific bucket folder, define the folder
name in the resource element, such as
`arn:aws:s3:::<bucketA>/FolderName/*`. For more information,
see [How can I use IAM policies to grant user-specific access to
specific folders?](https://aws.amazon.com/premiumsupport/knowledge-center/iam-s3-user-specific-folder/ "https://aws.amazon.com/premiumsupport/knowledge-center/iam-s3-user-specific-folder/")

###### Note

Bucket-level actions, such as `GetBucketCors` and
`GetBucketLocation`, should be added on bucket-level
resources, not folders.

The following example IAM policy grants the required
permissions for `roleB` to access objects in `bucketA`:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::bucketA/FolderName/*",
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketCors",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::bucketA",
            ]
        }
    ]
}
```

3. Configure the bucket policy for `bucketA` in Account A to grant permissions to the IAM role `roleB` in Account B.

###### Note

Admins must also turn off **Block all public access** under the bucket
**Permissions** section.

The following is an example bucket policy for `bucketA` to grant the necessary permissions to `roleB`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/roleB"
 },
 "Action": [
 "s3:DeleteObject",
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": "arn:aws:s3:::bucketA/FolderName/*"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/roleB"
 },
 "Action": [
 "s3:ListBucket",
 "s3:GetBucketCors",
 "s3:GetBucketLocation"
 ],
 "Resource": "arn:aws:s3:::bucketA"
 }
 ]
}`

```

After configuring the preceding permissions, your Canvas user profile in Account B
can now use the Amazon S3 bucket in Account A as the storage location for Canvas
artifacts.

## Permissions for cross-account Amazon S3 buckets encrypted with AWS KMS

The following procedure shows you how to grant the necessary permissions so that
Canvas can access your Amazon S3 bucket in another account that is encrypted with AWS KMS.
The steps are similar to the procedure above, but with additional permissions. For
more information about granting cross-account KMS key access, see [Allowing users in other accounts to use a KMS key](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md") in the _AWS KMS Developer Guide_.

1. Create an Amazon S3 bucket, `bucketA`, and an Amazon S3 KMS key `s3KmsInAccountA` in Account A.
2. The Canvas user exists in another account called Account B. In the following steps, we refer to
   the Canvas user's IAM role as `roleB` in Account B.

Give the IAM role `roleB` in Account B permission to do the following:

    * Download
     (`GetObject`) and upload (`PutObject`) objects to and from `bucketA` in
     Account A.
    * Access the AWS KMS key `s3KmsInAccountA` in Account A.

The following example IAM policy grants the required
permissions for `roleB` to access objects in `bucketA` and use the KMS key `s3KmsInAccountA`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::bucketA/FolderName/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketCors",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::bucketA"
 ]
 },
 {
 "Action": [
 "kms:DescribeKey",
 "kms:CreateGrant",
 "kms:RetireGrant",
 "kms:GenerateDataKey",
 "kms:GenerateDataKeyWithoutPlainText",
 "kms:Decrypt"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:kms:us-east-1:111122223333:key/s3KmsInAccountA"
 }
 ]
}`

```

3. Configure the bucket policy for `bucketA` and the key policy for `s3KmsInAccountA`
   in Account A to grant permissions to the IAM role `roleB` in Account B.

The following is an example bucket policy for `bucketA` to grant the necessary permissions to `roleB`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/roleB"
 },
 "Action": [
 "s3:DeleteObject",
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": "arn:aws:s3:::bucketA/FolderName/*"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/roleB"
 },
 "Action": [
 "s3:GetBucketCors",
 "s3:GetBucketLocation"
 ],
 "Resource": "arn:aws:s3:::bucketA"
 }
 ]
}`

```

The following example is a key policy that you attach to the KMS key
`s3KmsInAccountA` in Account A to grant `roleB` access. For more information about
how to create and attach a key policy statement, see [Creating a key policy](../../../kms/latest/developerguide/key-policy-overview.md "../../../kms/latest/developerguide/key-policy-overview.md") in the _AWS KMS
Developer Guide_.

```
{
  "Sid": "Allow use of the key",
  "Effect": "Allow",
  "Principal": {
    "AWS": [
      "arn:aws:iam::accountB:role/roleB"
    ]
  },
  "Action": [
        "kms:DescribeKey",
        "kms:CreateGrant",
        "kms:RetireGrant",
        "kms:GenerateDataKey",
        "kms:GenerateDataKeyWithoutPlainText",
        "kms:Decrypt"
  ],
  "Resource": "*"
}
```

After configuring the preceding permissions, your Canvas user profile in Account B
can now use the encrypted Amazon S3 bucket in Account A as the storage location
for Canvas artifacts.
