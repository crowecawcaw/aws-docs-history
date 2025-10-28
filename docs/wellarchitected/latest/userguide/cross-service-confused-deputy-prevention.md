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
policies to limit the permissions that AWS Well-Architected Tool gives another service to the
resource. Use `aws:SourceArn` if you want only one resource to be associated with
the cross-service access. Use `aws:SourceAccount` if you want to allow any
resource in that account to be associated with the cross-service use.

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` global condition context key with the full ARN of the
resource. If you don't know the full ARN of the resource or if you are specifying multiple
resources, use the `aws:SourceArn` global context condition key with wildcard
characters (`*`) for the unknown portions of the ARN. For example,
`arn:aws:wellarchitected:*:`123456789012`:*`.

If the `aws:SourceArn` value does not contain the account ID, such as an Amazon S3
bucket ARN, you must use both global condition context keys to limit permissions.

The value of `aws:SourceArn` must be a workload or lens.

The following example shows how you can use the `aws:SourceArn` and
`aws:SourceAccount` global condition context keys in AWS WA Tool to prevent
the confused deputy problem.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Sid": "ConfusedDeputyPreventionExamplePolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "wellarchitected.amazonaws.com"
 },
 "Action": "wellarchitected:`CreateWorkload`",
 "Resource": [
 "arn:aws:wellarchitected:`us-east-1`:`111122223333`:`ResourceName`/*"
 ],
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:wellarchitected:*:`123456789012`:*"
 },
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 }
 }
 }
}`

```
