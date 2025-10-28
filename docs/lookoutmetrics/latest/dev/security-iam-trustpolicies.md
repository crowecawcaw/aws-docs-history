Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Cross-service confused deputy prevention

The confused deputy problem is a security issue where an entity that doesn't have permission to perform an
action can coerce a more-privileged entity to perform the action. In AWS, cross-service impersonation can result
in the confused deputy problem. Cross-service impersonation can occur when one service (the _calling
service_) calls another service (the _called service_). The calling service can be
manipulated to use its permissions to act on another customer's resources in a way it should not otherwise have
permission to access. To prevent this, AWS provides tools that help you protect your data for all services with
service principals that have been given access to resources in your account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource policies to limit the
permissions that Amazon Lookout for Metrics gives another service to the resource. If you use both global condition context keys, the
`aws:SourceAccount` value and the account in the `aws:SourceArn` value must use the same
account ID when used in the same policy statement.

The most effective way to protect against the confused deputy problem is to use the `aws:SourceArn`
global condition context key with the full ARN of the resource. If you don't know the full ARN of the resource or if
you are specifying multiple resources, use the `aws:SourceArn` global context condition key with
wildcards (`*`) for the unknown portions of the ARN. For example,
`arn:aws:`servicename`::`123456789012`:*`.

The following example shows how you can use the `aws:SourceArn` and `aws:SourceAccount`
global condition context keys in Amazon SageMaker AI secret policies to prevent the confused deputy problem.

When you create a dataset in the console, or call the [GetSampleData](../api/API_GetSampleData.md "../api/API_GetSampleData.md") API operation directly, the trust
policy can't refer to a specific resource. For existing detectors, you can specify the ARN of the detector.

###### Sections

- [Setting up a dataset](#security-iam-trustpolicies-setup "#security-iam-trustpolicies-setup")
- [Updating the trust policy after setup](#security-iam-trustpolicies-general "#security-iam-trustpolicies-general")

## Setting up a dataset

When you set up an Amazon S3 dataset, the console uses the service role that you provide to read sample data from
the source bucket. For this operation, there isn't a specific resource to use for `SourceArn`. During
setup, you can use a trust policy like the following, with a wildcard (`*`) for the
`SourceArn` resource.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Principal": {
 "Service": "lookoutmetrics.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:lookoutmetrics:`us-east-2`:`123456789012`:*"
 },
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 }
 }
 }
}`

```

Replace the region name and account ID with yours. After you've created the detector, you can replace the ARN
with that of the detector. If you call the [GetSampleData](../api/API_GetSampleData.md "../api/API_GetSampleData.md") API operation directly, consider creating a
separate service role specifically for that task.

## Updating the trust policy after setup

After setup, you can update the trust policy to refer to a specific detector ARN.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Principal": {
 "Service": "lookoutmetrics.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:lookoutmetrics:`us-east-2`:`123456789012`:AnomalyDetector:`my-detector`"
 },
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 }
 }
 }
}`

```
