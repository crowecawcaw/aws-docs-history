# Enabling audit logging

You can use audit logs to capture detailed information about your Amazon WorkMail organization usage. The audit logs can be used to monitor user’s access to mailboxes, audit for suspicious activity, and debug access control and availability provider configurations.

###### Note

The _AmazonWorkMailFullAccess_ managed policy does not include all the required permissions to manage log deliveries. If you are using this policy to manage WorkMail, make sure the principal (for example, the assumed role) used to configure log deliveries also has all the required permissions.

Amazon WorkMail supports three delivery destinations for audit logs: CloudWatch Logs, Amazon S3, and Amazon Data Firehose. For more information, see [Logging that requires additional permissions [V2]](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md") in the _[Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md")_.

In addition to the permissions listed under [Logging that requires additional permissions [V2]](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md"), Amazon WorkMail requires an additional permission to configure log delivery: `workmail:AllowVendedLogDeliveryForResource`.

A working log delivery consists of three elements:

- _DeliverySource_, a logical object that
  represents the resource or resources that send the logs. For Amazon WorkMail, it's the Amazon WorkMail
  Organization.
- A _DeliveryDestination_, which is a logical object that
  represents the actual delivery destination.
- A _Delivery_, which connects a delivery source to delivery
  destination.
  To configure log delivery between Amazon WorkMail and a destination, you can do the following:

- Create a delivery source with [PutDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md").
- Create a delivery destination with [PutDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md").
- If you're delivering logs cross-account, you must use [PutDeliveryDestinationPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.md") in the destination account to assign
  an IAM policy to the destination. This policy authorizes creating a delivery
  from the delivery source in account A to the delivery destination in account B.
- Create a delivery by pairing exactly one delivery source and one delivery
  destination by using [CreateDelivery](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md").
  The following sections provide the details of the permissions that you must have when
  you're signed in to set up log delivery to each type of destination. These permissions
  can be granted to an IAM role that you're signed in with.

###### Important

It's your responsibility to remove log delivery resources after deleting the
log-generating resource.

To remove log delivery resources after deleting the log-generating resource, follow
these steps.

1. Delete the _Delivery_ by using the [DeleteDelivery](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDelivery.md") operation.
2. Delete the _DeliverySource_ by using the [DeleteDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliverySource.md") operation.
3. If the _DeliveryDestination_ associated with the
   _DeliverySource_ that you just deleted is used only for
   this specific _DeliverySource_, then you can remove it by
   using the [DeleteDeliveryDestinations](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveryDestinations.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveryDestinations.md") operation.

## Configuring audit logging using the Amazon WorkMail

console

You can configure audit logging in the Amazon WorkMail console:

1. Open the Amazon WorkMail console at
   [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/ "https://console.aws.amazon.com/workmail/").

If necessary, change the AWS Region. In the bar at the top of the
console window, open the **Select a Region** list and
select a Region. For more information, see [Regions
and endpoints](../../../general/latest/gr/index.md "../../../general/latest/gr/index.md") in the
_Amazon Web Services General Reference_. 2. In the navigation pane, choose **Organizations**, then
choose the name of your organization. 3. Choose **Logging settings**. 4. Choose the **Audit log settings** tab. 5. Configure deliveries for the required log type using the appropriate widget. 6. Choose **Save**.

## Logs sent to CloudWatch Logs

**User permissions**

To enable sending logs to CloudWatch Logs, you must be signed in with the following
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
 "logs:DeleteDelivery"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:``111122223333``:delivery:*",
 "arn:aws:logs:`us-east-1`:``111122223333``:delivery-source:*",
 "arn:aws:logs:`us-east-1`:``111122223333``:delivery-destination:*"
 ]
 },
 {
 "Sid": "ListAccessForLogDeliveryActions",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeDeliveryDestinations",
 "logs:DescribeDeliverySources",
 "logs:DescribeDeliveries",
 "logs:DescribeLogGroups"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowUpdatesToResourcePolicyCWL",
 "Effect": "Allow",
 "Action": [
 "logs:PutResourcePolicy",
 "logs:DescribeResourcePolicies",
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:``111122223333``:*"
 ]
 },
 {
 "Sid": "AllowLogDeliveryForWorkMail",
 "Effect": "Allow",
 "Action": [
 "workmail:AllowVendedLogDeliveryForResource"
 ],
 "Resource": [
 "arn:aws:workmail:`us-east-1`:``111122223333``:organization/`organization-id`"
 ]
 }
 ]
}`

```

**Log group resource policy**

The log group where the logs are being sent must have a resource policy that includes
certain permissions. If the log group currently does not have a resource policy,
and the user
setting up the logging has the `logs:PutResourcePolicy`,
`logs:DescribeResourcePolicies`, and `logs:DescribeLogGroups`
permissions for the log group, then AWS automatically creates the
following policy for it when you begin sending the logs
to CloudWatch Logs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSLogDeliveryWrite20150319",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "delivery.logs.amazonaws.com"
 ]
 },
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:my-log-group:log-stream:*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": [
 "`111122223333`"
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

**Log group resource policy size limit
considerations**

These services must list each log group that they're sending logs to in the
resource policy. CloudWatch Logs resource policies are limited to 5,120 characters. A service
that sends logs to a large number of log groups might run into this limit.

To mitigate this, CloudWatch Logs monitors the size of resource policies used by the service
that's sending logs. When it detects that a policy approaches the size limit of
5,120 characters, CloudWatch Logs automatically enables `/aws/vendedlogs/*` in the
resource policy for that service. You can then start using log groups with names
that start with `/aws/vendedlogs/` as the destinations for logs from
these services.

## Logs sent to Amazon S3

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
 "logs:DeleteDelivery"
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
 "logs:DescribeLogGroups"
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
 "Resource": "arn:aws:s3:::`bucket-name`"
 },
 {
 "Sid": "AllowLogDeliveryForWorkMail",
 "Effect": "Allow",
 "Action": [
 "workmail:AllowVendedLogDeliveryForResource"
 ],
 "Resource": [
 "arn:aws:workmail:`us-east-1`:`111122223333`:organization/`organization-id`"
 ]
 }
 ]
}`

```

The S3 bucket where the logs are being sent must have a resource policy that
includes certain permissions. If the bucket currently doesn't have a resource policy
and the user setting up the logging has the `S3:GetBucketPolicy` and
`S3:PutBucketPolicy` permissions for the bucket, then AWS
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
 "Resource": "arn:aws:s3:::my-bucket",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": [
 "`123456789012`"
 ]
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:logs:`us-east-1`:`111122223333`:delivery-source:*"
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
 "Resource": "arn:aws:s3:::my-bucket/AWSLogs/`111122223333`/*",
 "Condition": {
 "StringEquals": {
 "s3:x-amz-acl": "bucket-owner-full-control",
 "aws:SourceAccount": [
 "`123456789012`"
 ]
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:logs:`us-east-1`:`111122223333`:delivery-source:*"
 ]
 }
 }
 }
 ]
}`

```

In the previous policy, for `aws:SourceAccount`, specify the list of
account IDs for which logs are being delivered to this bucket. For
`aws:SourceArn`, specify the list of ARNs of the resource that
generates the logs, in the form
`arn:aws:logs:`source-region`:`source-account-id`:*`.

If the bucket has a resource policy, but that policy doesn't contain the statement
shown in the previous policy, and the user setting up the logging has the
`S3:GetBucketPolicy` and `S3:PutBucketPolicy` permissions
for the bucket, that statement is appended to the bucket's resource policy.

###### Note

In some cases, you might see `AccessDenied` errors in AWS CloudTrail if
the `s3:ListBucket` permission hasn't been granted to
`delivery.logs.amazonaws.com`. To avoid these errors in your CloudTrail
logs, you must grant the `s3:ListBucket` permission to
`delivery.logs.amazonaws.com`. You must also include the
`Condition` parameters shown with the
`s3:GetBucketAcl` permission set in the preceding bucket policy.
To streamline this, instead of creating a new `Statement`, you can
directly update the `AWSLogDeliveryAclCheck` to be `“Action”:
 [“s3:GetBucketAcl”, “s3:ListBucket”]`.

### Amazon S3 bucket server-side

encryption

You can protect the data in your Amazon S3 bucket by enabling either server-side
encryption with Amazon S3-managed keys (SSE-S3) or server-side encryption with an
AWS KMS key stored in AWS Key Management Service (SSE-KMS). For more information, see [Protecting data
using server-side encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md").

If you choose SSE-S3, no additional configuration is required. Amazon S3 handles
the encryption key.

###### Warning

If you choose SSE-KMS, you must use a customer managed key, because using
an AWS managed key isn't supported for this scenario. If you set up
encryption using an AWS managed key, the logs will be delivered in an
unreadable format.

When you use a customer managed AWS KMS key, you can specify the Amazon Resource
Name (ARN) of the customer managed key when you enable bucket encryption. Add
the following to the key policy for your customer managed key (not to the bucket
policy for your S3 bucket), so that the log delivery account can write to your
S3 bucket.

If you choose SSE-KMS, you must use a customer managed key, because using an
AWS managed key isn't supported for this scenario. When you use a customer
managed AWS KMS key, you can specify the Amazon Resource Name (ARN) of the
customer managed key when you enable bucket encryption. Add the following to the
key policy for your customer managed key (not to the bucket policy for your S3
bucket), so that the log delivery account can write to your S3 bucket.

```
{
    "Sid":"Allow Logs Delivery to use the key",
    "Effect":"Allow",
    "Principal":{
        "Service":[
            "delivery.logs.amazonaws.com"
        ]
    },
    "Action":[
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
    ],
    "Resource":"*",
    "Condition":{
        "StringEquals":{
            "aws:SourceAccount":[
                "`account-id`"
            ]
        },
        "ArnLike":{
            "aws:SourceArn":[
                "arn:aws:logs:`region`:`account-id`:delivery-source:*"
            ]
        }
    }
}
```

For `aws:SourceAccount`, specify the list of account IDs for which
logs are being delivered to this bucket. For `aws:SourceArn`, specify
the list of ARNs of the resource that generates the logs, in the form
`arn:aws:logs:`source-region`:`source-account-id`:*`.

## Logs sent to

Firehose

**User permissions**

To enable sending logs to Firehose, you must be signed in with the following
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
 "logs:DeleteDelivery"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:``111122223333``:delivery:*",
 "arn:aws:logs:`us-east-1`:``111122223333``:delivery-source:*",
 "arn:aws:logs:`us-east-1`:``111122223333``:delivery-destination:*"
 ]
 },
 {
 "Sid": "ListAccessForLogDeliveryActions",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeDeliveryDestinations",
 "logs:DescribeDeliverySources",
 "logs:DescribeDeliveries",
 "logs:DescribeLogGroups"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowUpdatesToResourcePolicyFH",
 "Effect": "Allow",
 "Action": [
 "firehose:TagDeliveryStream"
 ],
 "Resource": [
 "arn:aws:firehose:`us-east-1`:``111122223333``:deliverystream/*"
 ]
 },
 {
 "Sid": "CreateServiceLinkedRole",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/aws-service-role/delivery.logs.amazonaws.com/AWSServiceRoleForLogDelivery"
 },
 {
 "Sid": "AllowLogDeliveryForWorkMail",
 "Effect": "Allow",
 "Action": [
 "workmail:AllowVendedLogDeliveryForResource"
 ],
 "Resource": [
 "arn:aws:workmail:`us-east-1`:``111122223333``:organization/`organization-id`"
 ]
 }
 ]
}`

```

**IAM roles used for resource permissions**

Because Firehose doesn't use resource policies, AWS uses IAM roles when setting
up these logs to be sent to Firehose. AWS creates a service-linked role named
**AWSServiceRoleForLogDelivery**. This
service-linked role includes the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "firehose:PutRecord",
 "firehose:PutRecordBatch",
 "firehose:ListTagsForDeliveryStream"
 ],
 "Resource": "`arn:aws:`firehose:`us-east-1`:`111122223333`:deliverystream/workmail-*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/LogDeliveryEnabled": "true"
 }
 },
 "Effect": "Allow"
 }
 ]
}`

```

This service-linked role grants permission for all Firehose delivery streams that
have the `LogDeliveryEnabled` tag set to `true`. AWS gives
this tag to the destination delivery stream when you set up the logging.

This service-linked role also has a trust policy that allows the
`delivery.logs.amazonaws.com` service principal to assume the needed
service-linked role. That trust policy is as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## Console-specific

permissions

In addition to the permissions listed in the previous sections, if you're setting
up log delivery using the console instead of the APIs, you also need the following
permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowLogDeliveryActions",
 "Effect": "Allow",
 "Action": [
 "firehose:DescribeDeliveryStream",
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:*",
 "arn:aws:firehose:`us-east-1`:`111122223333`:deliverystream/*",
 "arn:aws:s3:::*"
 ]
 },
 {
 "Sid": "ListAccessForDeliveryDestinations",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups",
 "firehose:ListDeliveryStreams",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 }
 ]
}`

```
