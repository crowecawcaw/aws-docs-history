End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Cross-service confused deputy

prevention

The confused deputy problem is a security issue where an entity that doesn't have
permission to perform an action can coerce a more-privileged entity to perform the action.
In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the _calling
service_) calls another service (the _called service_). The
calling service can be manipulated to use its permissions to act on another customer's
resources in a way it shouldn't otherwise have permission to access. To prevent this, AWS
provides tools that help you protect your data for all services, with service principals
that have been given access to resources in your account.

We recommend using the [`aws:SourceArn`](../../../ IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../ IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource
policies. This limits the permissions that AWS IoT Analytics gives another service to the
resource. If you use both global condition context keys, the `aws:SourceAccount`
value and the account in the `aws:SourceArn` value must use the same account ID
when used in the same policy statement.

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` global condition context key with the full Amazon Resource
Name (ARN) of the resource. If you don't know the full ARN of the resource or if you're
specifying multiple resources, use the `aws:SourceArn` global context condition
key with wildcards (`*`) for the unknown portions of the ARN. For example,
`arn:aws:`iotanalytics`::`123456789012`:*`.

###### Topics

- [Prevention for
  Amazon S3
  buckets](#confused-deputy-prevention-with-S3 "#confused-deputy-prevention-with-S3")
- [Prevention with
  Amazon CloudWatch Logs](#confused-deputy-prevention-with-cloudwatch-logs "#confused-deputy-prevention-with-cloudwatch-logs")
- [Confused deputy prevention for customer managed AWS IoT Analytics resources](#confused-deputy-prevention-for-resources-with-customer-managed-storage "#confused-deputy-prevention-for-resources-with-customer-managed-storage")

## Prevention for

Amazon S3
buckets

If you use customer managed Amazon S3 storage for your AWS IoT Analytics data store, the Amazon S3 bucket
that stores your data may be exposed to confused deputy issues.

For example, Nikki Wolf uses a customer owned Amazon S3 bucket called
`DOC-EXAMPLE-BUCKET`. The bucket stores information for an
AWS IoT Analytics data store that was created in the Region `us-east-1`.
She specifies a policy that enables the AWS IoT Analytics service principal to query
`DOC-EXAMPLE-BUCKET` on her behalf. Nikki's coworker, Li
Juan, queries `DOC-EXAMPLE-BUCKET` from her own account and
creates a dataset with the results. As a result, the AWS IoT Analytics service principal queried
Nikki’s Amazon S3 bucket on Li's behalf even though Li ran the query from her account.

To prevent this, Nikki can specify the `aws:SourceAccount` condition or the
`aws:SourceArn` condition in the policy for
`DOC-EXAMPLE-BUCKET`.

**Specify the `aws:SourceAccount` condition**
‐ The following example of a bucket policy specifies that only the AWS IoT Analytics resources
from Nikki's account (`123456789012`) can access
`DOC-EXAMPLE-BUCKET`.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "MyPolicyID",
 "Statement": [
 {
 "Sid": "ConfusedDeputyPreventionExamplePolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "iotanalytics.amazonaws.com"
 },
 "Action": [
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:ListBucketMultipartUploads",
 "s3:ListMultipartUploadParts",
 "s3:AbortMultipartUpload",
 "s3:PutObject",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:*:*:`amzn-s3-demo-bucket`",
 "arn:aws:s3:*:*:`amzn-s3-demo-bucket`/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 }
 }
 }
 ]
}`

```

**Specify the `aws:SourceArn` condition**
‐ Alternatively, Nikki can use the `aws:SourceArn` condition.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "MyPolicyID",
 "Statement": [
 {
 "Sid": "ConfusedDeputyPreventionExamplePolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "iotanalytics.amazonaws.com"
 },
 "Action": [
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:ListBucketMultipartUploads",
 "s3:ListMultipartUploadParts",
 "s3:AbortMultipartUpload",
 "s3:PutObject",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:*:*:`amzn-s3-demo-bucket`",
 "arn:aws:s3:*:*:`amzn-s3-demo-bucket`/*"
 ],
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:iotanalytics:`us-east-1`:`123456789012`:dataset/`your-dataset`",
 "arn:aws:iotanalytics:`us-east-1`:`123456789012`:datastore/`your-datastore`"
 ]
 }
 }
 }
 ]
}`

```

## Prevention with

Amazon CloudWatch Logs

You can prevent the confused deputy problem while monitoring with Amazon CloudWatch Logs. The
following resource policy shows how to prevent the confused deputy problem with:

- The global condition context key, `aws:SourceArn`
- The `aws:SourceAccount` with your AWS account ID
- The customer resource that is associated with the `sts:AssumeRole`
  request in AWS IoT Analytics

Replace `123456789012` with your AWS account ID,
and `us-east-1` with the Region of your AWS IoT Analytics account in the
following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "iotanalytics.amazonaws.com"
 },
 "Action": "logs:PutLogEvents",
 "Resource": "*",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:iotanalytics:`us-east-1`:`123456789012`:*/*"
 },
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 }
 }
 }
 ]
}`

```

For more information about enabling and configuring Amazon CloudWatch Logs, see [Logging and monitoring in AWS IoT Analytics](monitoring.md "monitoring.md").

## Confused deputy prevention for customer managed AWS IoT Analytics resources

If you grant AWS IoT Analytics permission to perform actions on your AWS IoT Analytics resources, the
resources may be exposed to confused deputy issues. To prevent the confused deputy
problem, you can limit the permissions given to AWS IoT Analytics with the following example
resource policies.

###### Topics

- [Prevention
  for AWS IoT Analytics channels and data stores](#confused-deputy-prevention-for-channels-and-datastores "#confused-deputy-prevention-for-channels-and-datastores")
- [Cross-service confused deputy prevention for AWS IoT Analytics dataset content delivery
  rules](#confused-deputy-prevention-for-dataset-content-delivery "#confused-deputy-prevention-for-dataset-content-delivery")

### Prevention

for AWS IoT Analytics channels and data stores

You use IAM roles to control the AWS resources that AWS IoT Analytics can access on your
behalf. To prevent exposing your role to the confused deputy problem, you can
specify the AWS account in the `aws:SourceAccount` element and the ARN
of the AWS IoT Analytics resource in the `aws:SourceArn` element of the trust policy
that you attach to a role.

In the following example, replace
`123456789012` with your AWS account ID and
`arn:aws:iotanalytics:`aws-region`:123456789012:channel/DOC-EXAMPLE-CHANNEL`
with the ARN of an AWS IoT Analytics channel or data store.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ConfusedDeputyPreventionExamplePolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "iotanalytics.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:iotanalytics:`us-east-1`:`123456789012`:`channel`/`your-channel`"
 }
 }
 }
 ]
}`

```

To learn more about customer managed S3 storage options for channels and data
stores, see [`CustomerManagedChannelS3Storage`](../APIReference/API_CustomerManagedChannelS3Storage.md "../APIReference/API_CustomerManagedChannelS3Storage.md") and [`CustomerManagedDatastoreS3Storage`](../APIReference/API_CustomerManagedDatastoreS3Storage.md "../APIReference/API_CustomerManagedDatastoreS3Storage.md") in the _AWS IoT Analytics API
Reference_.

### Cross-service confused deputy prevention for AWS IoT Analytics dataset content delivery

rules

The IAM role that AWS IoT Analytics assumes to deliver dataset query results to Amazon S3 or to
AWS IoT Events can be exposed to confused deputy issues. To prevent the confused deputy
problem, specify the AWS account in the `aws:SourceAccount` element and
the ARN of the AWS IoT Analytics resource in the `aws:SourceArn` element of the trust
policy that you attach to your role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ConfusedDeputyPreventionExampleTrustPolicyDocument",
 "Effect": "Allow",
 "Principal": {
 "Service": "iotanalytics.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:iotanalytics:`us-east-1`:`123456789012`:dataset/`your-dataset`"
 }
 }
 }
 ]
}`

```

For more details about configuring dataset content delivery rules, see [`contentDeliveryRules`](../APIReference/API_CreateDataset.md#iotanalytics-CreateDataset-request-contentDeliveryRules "../APIReference/API_CreateDataset.md#iotanalytics-CreateDataset-request-contentDeliveryRules") in the _AWS IoT Analytics API Reference_.
