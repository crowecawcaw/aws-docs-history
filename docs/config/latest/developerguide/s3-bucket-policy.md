# Permissions for the Amazon S3 Bucket for the AWS Config Delivery

Channel

###### Important

This page is about setting up the Amazon S3 Bucket for the AWS Config delivery channel. This page is not
about the `AWS::S3::Bucket` resource type that the AWS Config configuration recorder can
record.

Amazon S3 buckets and objects are private by default. Only the AWS account that created the bucket (the resource owner) has access permissions. Resource owners can grant access to other resources and users by creating access policies.

When AWS Config automatically creates an S3 bucket for you, it adds the required permissions.
However, if you specify an existing S3 bucket, you must add these permissions manually.

###### Topics

- [When Using IAM Roles](#required-permissions-in-another-account "#required-permissions-in-another-account")
- [When Using Service-Linked Roles](#required-permissions-using-servicelinkedrole "#required-permissions-using-servicelinkedrole")
- [Granting AWS Config access](#granting-access-in-another-account "#granting-access-in-another-account")
- [Cross-Account Delivery](#required-permissions-cross-account "#required-permissions-cross-account")

## Required Permissions for the Amazon S3

Bucket When Using IAM Roles

AWS Config uses the IAM role you assigned to the configuration recorder to deliver configuration history and snapshots to S3 buckets in your account.
For cross-account delivery, AWS Config first attempts to use the assigned IAM role.
If the bucket policy doesn't grant `WRITE` access to the IAM role,
AWS Config uses the `config.amazonaws.com` service principal.
The bucket policy must grant `WRITE` access to `config.amazonaws.com` to complete the delivery.
After successful delivery, AWS Config maintains ownership of all objects it delivers to the cross-account S3 bucket.

AWS Config calls the Amazon S3 [HeadBucket](../../../AmazonS3/latest/API/API_RESTBucketHEAD.md "../../../AmazonS3/latest/API/API_RESTBucketHEAD.md") API with the IAM role you assigned to the configuration recorder to confirm if the S3 bucket exists and its location.
If you do not have the necessary permissions for AWS Config to confirm, you will see an `AccessDenied` error in your AWS CloudTrail logs.
However, AWS Config can still deliver configuration history and snapshots even if AWS Config does not have the necessary permissions to confirm if the S3 bucket exists and its location.

###### Minimum permissions

The Amazon S3 `HeadBucket` API requires the `s3:ListBucket` action.

## Required Permissions for the

Amazon S3 Bucket When Using Service-Linked Roles

The AWS Config service-linked role does not have permission to put objects to Amazon S3 buckets.
If you set up AWS Config using a service-linked role, AWS Config will use the `config.amazonaws.com` service principal to deliver configuration history and snapshots.
The S3 bucket policy in your account or cross-account destinations must include permissions for the AWS Config service principal to write objects.

## Granting AWS Config access to the Amazon S3

Bucket

Complete the following steps enable AWS Config to deliver configuration history and snapshots to an Amazon S3 bucket.

1. Sign in to the AWS Management Console using the account that has the S3 bucket.
2. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
3. Select the bucket that you want AWS Config to use to deliver configuration items, and then
   choose **Properties**.
4. Choose **Permissions**.
5. Choose **Edit Bucket Policy**.
6. Copy the following policy into the **Bucket Policy Editor**
   window:

###### Security best practices

We strongly
recommend that you restrict access in the bucket policy with the
`AWS:SourceAccount` condition. This makes sure that AWS Config is granted access on behalf of
expected users only.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSConfigBucketPermissionsCheck",
 "Effect": "Allow",
 "Principal": {
 "Service": "config.amazonaws.com"
 },
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "Condition": {
 "StringEquals": {
 "AWS:SourceAccount": "`sourceAccountID`"
 }
 }
 },
 {
 "Sid": "AWSConfigBucketExistenceCheck",
 "Effect": "Allow",
 "Principal": {
 "Service": "config.amazonaws.com"
 },
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "Condition": {
 "StringEquals": {
 "AWS:SourceAccount": "`sourceAccountID`"
 }
 }
 },
 {
 "Sid": "AWSConfigBucketDelivery",
 "Effect": "Allow",
 "Principal": {
 "Service": "config.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/`[optional] prefix`/AWSLogs/`sourceAccountID`/Config/*",
 "Condition": {
 "StringEquals": {
 "s3:x-amz-acl": "bucket-owner-full-control",
 "AWS:SourceAccount": "`sourceAccountID`"
 }
 }
 }
 ]
}`

```

7. Substitute the following values in the bucket policy:
   - `amzn-s3-demo-bucket` – Name of the Amazon S3 bucket
     where AWS Config will deliver configuration history and snapshots.
   - `[optional] prefix` – An optional addition to the
     Amazon S3 object key that helps create a folder-like organization in the bucket.
   - `sourceAccountID` – ID of the account where AWS Config will deliver configuration history and snapshots.

8. Choose **Save** and then **Close**.

The `AWS:SourceAccount` condition restricts AWS Config operations to specified AWS accounts.
For multi-account configurations within an organization delivering to a single S3 bucket, use IAM roles with AWS Organizations conditions keys instead of service-linked roles. For example, `AWS:PrincipalOrgID`.
For more information, see [Managing access permissions for an organization](../../../organizations/latest/userguide/orgs_permissions_overview.md "../../../organizations/latest/userguide/orgs_permissions_overview.md") in the _AWS Organizations User guide_.

The `AWS:SourceArn` condition restricts AWS Config operations to specified delivery channels.
The `AWS:SourceArn` format is as follows: `arn:aws:config:`sourceRegion`:`123456789012``.

For example, to restrict S3 bucket access to a delivery channel in the US East (N. Virginia) Region for account 123456789012, add the following condition:

```
"ArnLike": {"AWS:SourceArn": "arn:aws:config:us-east-1:123456789012:"}
```

## Required Permissions for the

Amazon S3 Bucket When Delivering Cross-Account

When AWS Config is configured to deliver configuration history and snapshots to an Amazon S3 bucket in a different account (cross-account setup), where the configuration recorder and the S3 bucket specified for delivery channel are in different AWS accounts,
the following permissions are required:

- The IAM role you assign to the configuration recorder needs explicit permission to perform the `s3:ListBucket` operation. This is because AWS Config calls the Amazon S3 [HeadBucket](../../../AmazonS3/latest/API/API_RESTBucketHEAD.md "../../../AmazonS3/latest/API/API_RESTBucketHEAD.md") API with this IAM role to determine the bucket location.
- The S3 bucket policy must include permissions for the IAM role assigned to the configuration recorder.

The following is an example bucket policy configuration:

```
{
      "Sid": "AWSConfigBucketExistenceCheck",
      "Effect": "Allow",
      "Principal": {
        "AWS": "`IAM Role-Arn assigned to the configuration recorder`"
      },
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
}
```
