# Logs sent to Amazon S3

**User permissions**

To enable sending logs to Amazon S3, you must be signed in with the following
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadWriteAccessForLogDeliveryActions",
 "Effect": "Allow",
 "Action": [
 "logs:GetDelivery",
 "logs:GetDeliverySource",
 "logs:PutDeliveryDestination",
 "logs:GetDeliveryDestinationPolicy",
 "logs:DeleteDeliverySource",
 "logs:PutDeliveryDestinationPolicy",
 "logs:CreateDelivery",
 "logs:GetDeliveryDestination",
 "logs:PutDeliverySource",
 "logs:DeleteDeliveryDestination",
 "logs:DeleteDeliveryDestinationPolicy",
 "logs:DeleteDelivery",
 "logs:UpdateDeliveryConfiguration"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:delivery:*",
 "arn:aws:logs:`us-east-1`:`111122223333`:delivery-source:*",
 "arn:aws:logs:`us-east-1`:`111122223333`:delivery-destination:*"
 ]
 },
 {
 "Sid": "ListAccessForLogDeliveryActions",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeDeliveryDestinations",
 "logs:DescribeDeliverySources",
 "logs:DescribeDeliveries",
 "logs:DescribeConfigurationTemplates"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowUpdatesToResourcePolicyS3",
 "Effect": "Allow",
 "Action": [
 "s3:PutBucketPolicy",
 "s3:GetBucketPolicy"
 ],
 "Resource": "arn:aws:s3:::bucket-name"
 }
 ]
}`

```

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
 "Sid": "AWSLogDeliveryWrite",
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/AWSLogs/account-ID/*",
 "Condition": {
 "StringEquals": {
 "s3:x-amz-acl": "bucket-owner-full-control",
 "aws:SourceAccount": [
 "0123456789"
 ]
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:logs:us-east-1:`111122223333`:delivery-source:*"
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
            "aws:SourceArn": ["arn:aws:logs:`us-east-1`:`0123456789`:delivery-source:*"]
        }
        }
}
```

For `aws:SourceAccount`, specify the list of account IDS for which
logs are being delivered to this bucket. For `aws:SourceArn`, specify
the list of ARNs of the resource that generates the logs, in the form
`arn:aws:logs:`source-region`:`source-account-id`:*`.
