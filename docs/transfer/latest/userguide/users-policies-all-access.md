# Allowing read and write access to an Amazon S3

bucket

This section describes how to create an IAM policy that allows read and write access
to a specific Amazon S3 bucket. Assigning an IAM role that has this IAM policy to your
user gives that user read/write access to the specified Amazon S3 bucket.

The following policy provides programmatic read, write, and tagging access to an Amazon S3
bucket. The `GetObjectACL` and `PutObjectACL` statements are only required
if you need to enable Cross Account Access. That is, your Transfer Family server needs to access a bucket in a different account.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid":"ReadWriteS3",
 "Action": [
 "s3:ListBucket"
 ],
 "Effect": "Allow",
 "Resource": ["arn:aws:s3:::amzn-s3-demo-bucket"]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:GetObjectTagging",
 "s3:DeleteObject",
 "s3:DeleteObjectVersion",
 "s3:GetObjectVersion",
 "s3:GetObjectVersionTagging",
 "s3:GetObjectACL",
 "s3:PutObjectACL"
 ],
 "Resource": ["arn:aws:s3:::amzn-s3-demo-bucket/*"]
 }
 ]
}`

```

The `ListBucket` action requires permission to the bucket itself. The
`PUT`, `GET`, and `DELETE` actions require object
permissions. Because these are different resources, they are specified using different
Amazon Resource Names (ARNs).

To further restrict your users' access to only the `home` prefix of
the specified Amazon S3 bucket, see [Creating a session policy for an Amazon S3
bucket](users-policies-session.md "users-policies-session.md").
