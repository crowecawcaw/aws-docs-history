# Amazon S3 bucket permissions for flow

logs

By default, Amazon S3 buckets and the objects they contain are private. Only the bucket
owner can access the bucket and the objects stored in it. However, the bucket owner
can grant access to other resources and users by writing an access policy.

If the user creating the flow log owns the bucket and has `PutBucketPolicy`
and `GetBucketPolicy` permissions for the bucket, we automatically attach
the following policy to the bucket. This policy overwrites any existing policy attached
to the bucket.

Otherwise, the bucket owner must add this policy to the bucket, specifying the AWS
account ID of the flow log creator, or flow log creation fails. For more information,
see [Using bucket policies](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md") in the
_Amazon Simple Storage Service User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSLogDeliveryWrite",
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`",
 "s3:x-amz-acl": "bucket-owner-full-control"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:logs:`us-east-1`:`123456789012`:*"
 }
 }
 },
 {
 "Sid": "AWSLogDeliveryAclCheck",
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:logs:`us-east-1`:`123456789012`:*"
 }
 }
 }
 ]
}`

```

The ARN that you specify for `my-s3-arn` depends on
whether you use Hive-compatible S3 prefixes.

- Default prefixes

```
arn:aws:s3:::`bucket_name`/`optional_folder`/AWSLogs/`account_id`/*
```

- Hive-compatible S3 prefixes

```
arn:aws:s3:::`bucket_name`/`optional_folder`/AWSLogs/aws-account-id=`account_id`/*
```

It is a best practice to grant these permissions to the log delivery service
principal instead of individual AWS account ARNs. It is also a best practice
to use the `aws:SourceAccount` and `aws:SourceArn` condition
keys to protect against [the confused
deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md"). The source account is the owner of the flow log and the
source ARN is the wildcard (\*) ARN of the logs service.

Note that the log delivery service calls the `HeadBucket` Amazon S3 API
action to verify the existence and location of the S3 bucket. You are not required
to grant the log delivery service permission to call this action; it will still deliver
VPC flow logs even if it can't confirm that the S3 bucket exists and its location.
However, there will be an `AccessDenied` error for the call to
`HeadBucket` in your CloudTrail logs.
