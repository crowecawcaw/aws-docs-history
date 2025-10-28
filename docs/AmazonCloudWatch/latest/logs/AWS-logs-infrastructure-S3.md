# Logs sent to Amazon S3

When you set logs to be sent to Amazon S3, AWS creates or changes the resource
policies associated with the S3 bucket that is receiving the logs, if needed.

Logs published directly to Amazon S3 are published to an existing bucket that you
specify. One or more log files are created every five minutes in the specified
bucket.

When you deliver logs for the first time to an Amazon S3 bucket, the service that
delivers logs records the owner of the bucket to ensure that the logs are delivered
only to a bucket belonging to this account. As a result, to change the Amazon S3 bucket
owner, you must re-create or update the log subscription in the originating
service.

###### Note

CloudFront uses a different permissions model than the other services that send
vended logs to S3. For more information, see [Permissions required to configure standard logging and to access your log
files](../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md#AccessLogsBucketAndFileOwnership "../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md#AccessLogsBucketAndFileOwnership").

Additionally, if you use the same S3 bucket for CloudFront access logs and another
log source, enabling ACL on the bucket for CloudFront also grants permission to all
other log sources that use this bucket.

###### Important

If you're sending logs to an Amazon S3 bucket and the bucket policy contains a
`NotAction` or `NotPrincipal` element, adding log
delivery permissions to the bucket automatically and creating a log subscription
will fail. To create a log subscription successfully, you need to manually add
the log delivery permissions to the bucket policy, then create the log
subscription. For more information, see the instructions in this section.

If the bucket has server-side encryption using a customer managed AWS KMS key,
you must also add the key policy for your customer managed key. For more
information, see [Amazon S3](#AWS-logs-SSE-KMS-S3 "#AWS-logs-SSE-KMS-S3").

If the destination bucket has SSE-KMS and a Bucket Key enabled, the attached
customer managed KMS key policy no longer works as expected for all requests.
For more information, see [Reducing the cost of
SSE-KMS with Amazon S3 Bucket Keys](../../../AmazonS3/latest/userguide/bucket-key.md "../../../AmazonS3/latest/userguide/bucket-key.md").

If you're using vended logs and S3 encryption with a customer managed AWS KMS
key, you must use a fully qualified AWS KMS key ARN instead of a key ID when you
configure the bucket. For more information, see [put-bucket-encryption](../../../cli/latest/reference/s3api/put-bucket-encryption.md "../../../cli/latest/reference/s3api/put-bucket-encryption.md").

**User permissions**

To be able to set up sending any of these types of logs to Amazon S3 for the first
time, you must be logged into an account with the following permissions.

- `logs:CreateLogDelivery`
- `S3:GetBucketPolicy`
- `S3:PutBucketPolicy`
  If any of these types of logs is already being sent to an Amazon S3 bucket, then to set
  up the sending of another one of these types of logs to the same bucket you only
  need to have the `logs:CreateLogDelivery` permission.

**S3 bucket resource policy**

The S3 bucket where the logs are being sent must have a resource policy that
includes certain permissions. If the bucket currently does not have a resource
policy and the user setting up the logging has the `S3:GetBucketPolicy`
and `S3:PutBucketPolicy` permissions for the bucket, then AWS
automatically creates the following policy for it when you begin sending the logs to
Amazon S3.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "AWSLogDeliveryWrite20150319",
 "Statement": [
 {
 "Sid": "AWSLogDeliveryAclCheck",
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": [
 "`0123456789`"
 ]
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:logs:`us-east-1`:`111122223333`:*"
 ]
 }
 }
 },
 {
 "Sid": "AWSLogDeliveryWrite",
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/AWSLogs/`account-ID`/*",
 "Condition": {
 "StringEquals": {
 "s3:x-amz-acl": "bucket-owner-full-control",
 "aws:SourceAccount": [
 "`0123456789`"
 ]
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:logs:`us-east-1`:`111122223333`:*"
 ]
 }
 }
 }
 ]
}`

```

In the previous policy, for `aws:SourceAccount`, specify the list of
account IDS for which logs are being delivered to this bucket. For
`aws:SourceArn`, specify the list of ARNs of the resource that
generates the logs, in the form
`arn:aws:logs:`source-region`:`source-account-id`:*`.

If the bucket has a resource policy but that policy doesn't contain the statement
shown in the previous policy, and the user setting up the logging has the
`S3:GetBucketPolicy` and `S3:PutBucketPolicy` permissions
for the bucket, that statement is appended to the bucket's resource policy.

###### Note

In some cases, you may see `AccessDenied` errors in AWS CloudTrail if the
`s3:ListBucket` permission has not been granted to
`delivery.logs.amazonaws.com`. To avoid these errors in your CloudTrail
logs, you must grant the `s3:ListBucket` permission to
`delivery.logs.amazonaws.com` and you must include the
`Condition` parameters shown with the
`s3:GetBucketAcl` permission set in the preceding bucket policy.
To make this simpler, instead of creating a new `Statement`, you can
directly update the `AWSLogDeliveryAclCheck` to be `“Action”:
 [“s3:GetBucketAcl”, “s3:ListBucket”]`

## Amazon S3 bucket server-side encryption

You can protect the data in your Amazon S3 bucket by enabling either server-side
Encryption with Amazon S3-managed keys (SSE-S3) or server-side encryption with a
AWS KMS key stored in AWS Key Management Service (SSE-KMS). For more information, see [Protecting data
using server-side encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md").

If you choose SSE-S3, no additional configuration is required. Amazon S3 handles
the encryption key.

###### Warning

If you choose SSE-KMS, you must use a customer managed key, because using
an AWS managed key is not supported for this scenario. If you set up
encryption using an AWS managed key, the logs will be delivered in an
unreadable format.

When you use a customer managed AWS KMS key, you can specify the Amazon Resource
Name (ARN) of the customer managed key when you enable bucket encryption. You
must add the following to the key policy for your customer managed key (not to
the bucket policy for your S3 bucket), so that the log delivery account can
write to your S3 bucket.

If you choose SSE-KMS, you must use a customer managed key, because using an
AWS managed key is not supported for this scenario. When you use a customer
managed AWS KMS key, you can specify the Amazon Resource Name (ARN) of the
customer managed key when you enable bucket encryption. You must add the
following to the key policy for your customer managed key (not to the bucket
policy for your S3 bucket), so that the log delivery account can write to your
S3 bucket.

```
{
    "Sid": "Allow Logs Delivery to use the key",
    "Effect": "Allow",
    "Principal": {
        "Service": [ "delivery.logs.amazonaws.com" ]
    },
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "aws:SourceAccount": ["`0123456789`"]
        },
        "ArnLike": {
            "aws:SourceArn": ["arn:aws:logs:`us-east-1`:`0123456789`:*"]
        }
        }
}
```

For `aws:SourceAccount`, specify the list of account IDS for which
logs are being delivered to this bucket. For `aws:SourceArn`, specify
the list of ARNs of the resource that generates the logs, in the form
`arn:aws:logs:`source-region`:`source-account-id`:*`.
