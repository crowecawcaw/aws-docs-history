End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Cross-service confused deputy

prevention

The confused deputy problem is a security issue where an entity that doesn't have
permission to perform an action can coerce a more-privileged entity to perform the action.
In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the _calling
service_) calls another service (the _called service_). The
calling service can be manipulated to use its permissions to act on another customer's
resources in a way it should not otherwise have permission to access. To prevent this, AWS
provides tools that help you protect your data for all services with service principals that
have been given access to resources in your account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource
policies to limit the permissions that AWS Elemental MediaStore gives another service to the
resource. Use `aws:SourceArn` if you want only one resource to be associated with
the cross-service access. Use `aws:SourceAccount` if you want to allow any
resource in that account to be associated with the cross-service use.

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` global condition context key with the full ARN of the
resource. If you don't know the full ARN of the resource or if you are specifying multiple
resources, use the `aws:SourceArn` global context condition key with wildcard
characters (`*`) for the unknown portions of the ARN. For example,
`arn:aws:`servicename`:*:`123456789012`:*`.

If the `aws:SourceArn` value does not contain the account ID, such as an Amazon S3
bucket ARN, you must use both global condition context keys to limit permissions.

The value of `aws:SourceArn` must be the configuration that MediaStore publishes CloudWatch logs for in your Region and account.

The following example shows how you can use the `aws:SourceArn` and
`aws:SourceAccount` global condition context keys in MediaStore to prevent
the confused deputy problem.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ConfusedDeputyPreventionExamplePolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "mediastore.amazonaws.com"
 },
 "Action": "mediastore:`CreateContainer`",
 "Resource": [
 "arn:aws:mediastore:`us-east-2`:`333333333333`:container/`ResourceName`/*"
 ],
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:mediastore:*:`333333333333`:*"
 },
 "StringEquals": {
 "aws:SourceAccount": "`333333333333`"
 }
 }
 }
 ]
}`

```
