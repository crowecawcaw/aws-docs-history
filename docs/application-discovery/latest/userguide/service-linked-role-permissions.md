AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Service-linked role permissions for

Application Discovery Service

Application Discovery Service uses the service-linked role named **AWSServiceRoleForApplicationDiscoveryServiceContinuousExport** –
Enables access to AWS Services and Resources used or managed by AWS Application Discovery Service.

The AWSServiceRoleForApplicationDiscoveryServiceContinuousExport service-linked role trusts the following services to assume the
role:

- `continuousexport.discovery.amazonaws.com`
  The role permissions policy allows Application Discovery Service to complete the following actions:

glue

`CreateDatabase`

`UpdateDatabase`

`CreateTable`

`UpdateTable`

firehose

`CreateDeliveryStream`

`DeleteDeliveryStream`

`DescribeDeliveryStream`

`PutRecord`

`PutRecordBatch`

`UpdateDestination`

s3

`CreateBucket`

`ListBucket`

`GetObject`

logs

`CreateLogGroup`

`CreateLogStream`

`PutRetentionPolicy`

iam

`PassRole`

This is the full policy showing which resources the above actions apply to:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "glue:CreateDatabase",
 "glue:UpdateDatabase",
 "glue:CreateTable",
 "glue:UpdateTable",
 "firehose:CreateDeliveryStream",
 "firehose:DescribeDeliveryStream",
 "logs:CreateLogGroup"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": [
 "firehose:DeleteDeliveryStream",
 "firehose:PutRecord",
 "firehose:PutRecordBatch",
 "firehose:UpdateDestination"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:firehose:*:*:deliverystream/aws-application-discovery-service*"
 },
 {
 "Action": [
 "s3:CreateBucket",
 "s3:ListBucket",
 "s3:PutBucketLogging",
 "s3:PutEncryptionConfiguration"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:s3:::aws-application-discovery-service*"
 },
 {
 "Action": [
 "s3:GetObject"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:s3:::aws-application-discovery-service*/*"
 },
 {
 "Action": [
 "logs:CreateLogStream",
 "logs:PutRetentionPolicy"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:logs:*:*:log-group:/aws/application-discovery-service/firehose*"
 },
 {
 "Action": [
 "iam:PassRole"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:iam::*:role/AWSApplicationDiscoveryServiceFirehose",
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "firehose.amazonaws.com"
 }
 }
 },
 {
 "Action": [
 "iam:PassRole"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:iam::*:role/service-role/AWSApplicationDiscoveryServiceFirehose",
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "firehose.amazonaws.com"
 }
 }
 }
 ]
}`

```

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.
