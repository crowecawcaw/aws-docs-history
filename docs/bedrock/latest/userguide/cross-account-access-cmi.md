# Cross-account access to Amazon S3 bucket for custom model import jobs

If you are importing your model from Amazon S3 bucket and using cross-account Amazon S3 you will
need to grant permissions to users in the bucket owner's account for accessing the bucket before you import your customized model. See [Prerequisites for importing custom model](custom-model-import-prereq.md "custom-model-import-prereq.md").

## Configure cross-account access to Amazon S3 bucket

This section walks you through the steps for creating policies for users in the bucket
owners's account for accessing Amazon S3 bucket.

1. In the bucket owner account, create a bucket policy that provides access to
   the users in the bucket owner's account.

The following example bucket policy, created and applied to bucket
`s3://amzn-s3-demo-bucket` by the bucket owner, grants access to
a user in bucket owner's account `123456789123`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CrossAccountAccess",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:role/`ImportRole`"
 },
 "Action": [
 "s3:ListBucket",
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket/*`"
 ]
 }
 ]
}`

```

2. In the user’s AWS account, create an import execution role policy. For `aws:ResourceAccount` specify
   account id of the bucket owner's AWS account.

The following example import execution role policy in the user's account provides the bucket owner's account id `111222333444555` access to Amazon S3 bucket `s3://amzn-s3-demo-bucket`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetObject"
 ],
 "Resource": [
 "`arn:aws:s3:::amzn-s3-demo-bucket`",
 "`arn:aws:s3:::amzn-s3-demo-bucket/*`"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "`123456789012`"
 }
 }
 }
 ]
}`

```

## Configure cross-account access to Amazon S3 bucket encrypted with a custom AWS KMS key

If you have an Amazon S3 bucket that is encrypted with a custom AWS Key Management Service (AWS KMS) key, you
will need to grant access to it to users from bucket owner's account.

To configure cross-account access to Amazon S3 bucket encrypted with a custom AWS KMS key

1. In the bucket owner account, create a bucket policy that provides access to
   the users in bucket owner's account.

The following example bucket policy, created and applied to bucket
`s3://amzn-s3-demo-bucket` by the bucket owner, grants access to
a user in bucket owner's account `123456789123`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CrossAccountAccess",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:role/`ImportRole`"
 },
 "Action": [
 "s3:ListBucket",
 "s3:GetObject"
 ],
 "Resource": [
 "`arn:aws:s3:::amzn-s3-demo-bucket`",
 "`arn:aws:s3:::amzn-s3-demo-bucket`/*"
 ]
 }
 ]
}`

```

2. In the bucket owner account, create the following resource policy to allow user's account import role to decrypt.

```
{
   "Sid": "Allow use of the key by the destination account",
   "Effect": "Allow",
   "Principal": {
   "AWS": "arn:aws:iam::"`arn:aws:iam::123456789123:role/ImportRole`"
    },
    "Action": [
          "kms:Decrypt",
          "kms:DescribeKey"
    ],
    "Resource": "*"
}

```

3. In the user’s AWS account, create an import execution role policy. For `aws:ResourceAccount` specify
   account id of the bucket owner's AWS account. Also, provide access to the AWS KMS key that is used to encrypt the bucket.

The following example import execution role policy in the user's account provides the bucket owner's account id `111222333444555` access to Amazon S3 bucket `s3://amzn-s3-demo-bucket` and the AWS KMS key `arn:aws:kms:`us-west-2:123456789098`:key/`111aa2bb-333c-4d44-5555-a111bb2c33dd``

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetObject"
 ],
 "Resource": [
 "`arn:aws:s3:::amzn-s3-demo-bucket`",
 "`arn:aws:s3:::amzn-s3-demo-bucket/*`"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "`123456789012`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:DescribeKey"
 ],
 "Resource": "arn:aws:kms:`us-west-2`:`123456789012`:key/`111aa2bb-333c-4d44-5555-a111bb2c33dd`"
 }
 ]
 }`

```
