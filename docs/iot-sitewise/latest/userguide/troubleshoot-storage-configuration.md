# Troubleshoot storage settings for AWS IoT SiteWise

Use the following information to troubleshoot and resolve issues with the storage
configuration.

###### Issues

- [Error: Bucket doesn't exist](#no-s3-bucket "#no-s3-bucket")
- [Error: Access denied to Amazon S3 path](#iam-permissions "#iam-permissions")
- [Error: Role ARN can't be assumed](#iam-trust-relationship "#iam-trust-relationship")
- [Error: Failed to access cross-Region Amazon S3 bucket](#cross-region-s3-bucket "#cross-region-s3-bucket")

## Error: Bucket doesn't exist

**Solution:** AWS IoT SiteWise couldn't find your Amazon S3 bucket. Make
sure you enter the name of an existing Amazon S3 bucket in the current Region.

## Error: Access denied to Amazon S3 path

**Solution:** AWS IoT SiteWise couldn't access your Amazon S3 bucket. Do
the following:

- Make sure that you use the same Amazon S3 bucket that you specified in the IAM
  policy.
- Make sure that your role has the permissions shown in the following
  example.

###### Example permissions policy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:DeleteObject",
 "s3:GetBucketLocation",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket",
 "arn:aws:s3:::amzn-s3-demo-bucket/*"
 ]
 }
 ]
 }`

```

Replace amzn-s3-demo-bucket with the name of your Amazon S3
bucket.

## Error: Role ARN can't be assumed

**Solution:** AWS IoT SiteWise couldn't assume the IAM role on
your behalf. Make sure that your role trusts the following service:
`iotsitewise.amazonaws.com`. For more information, see [I can't
assume a role](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_cant-assume-role "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_cant-assume-role") see _IAM User Guide_.

## Error: Failed to access cross-Region Amazon S3 bucket

**Solution:** The Amazon S3 bucket that you specified is in a
different AWS Region. Make sure that your Amazon S3 bucket and AWS IoT SiteWise assets are in the same
Region.
